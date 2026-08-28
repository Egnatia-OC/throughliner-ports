"""Throughliner plugin for Hermes Agent.

Translates Hermes lifecycle hooks into the Claude Code hook contract that the
vendored Throughliner Python hooks speak (vendor/throughliner/hooks/). The
vendored files are pristine upstream content; this file is the entire port
surface.

Mapping (Hermes hook -> vendored hook):
  pre_tool_call  -> pre_tool_use.py   (deny -> block; ask -> approve, which
                                       escalates to Hermes's native
                                       human-approval gate — the only "ask"
                                       channel the platform has)
  post_tool_call -> post_tool_use.py  (lint findings have no context channel
                                       here, so they go to
                                       .throughliner/pending-context.md and
                                       are drained by pre_llm_call on the
                                       next LLM call)
  pre_llm_call   -> session_start.py  (on the first LLM call of a turn;
                                       {"context": ...} injected into the
                                       user message by the host)
  pre_verify     -> stop.py           (block -> {"decision": "block", ...} =
                                       keep the turn going)
  post_llm_call  -> stashes the final response text so on_session_end can
  on_session_end -> stop.py           (block -> correction note in
                                       .throughliner/pending-context.md for
                                       the next turn's pre_llm_call)

The five method skills (setup/plan/next/rescan/done) are materialized at
plugin load into ~/.hermes/skills/throughliner/tl-<name>/SKILL.md, with
frontmatter reduced to name+description, names namespaced tl-* (the bare
"plan" name collides with Hermes's bundled software-development/plan skill;
first-come-first-served name resolution makes bare names unreliable), and
${CLAUDE_PLUGIN_ROOT} rewritten to the vendored tree's absolute path.

Everything fails open: any error here degrades to "no Throughliner", never
to a broken session.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path

LOG_PREFIX = "[throughliner]"
SKILL_NAMES = ("setup", "plan", "next", "rescan", "done")
_SKILLS_CATEGORY = "throughliner"
_PENDING_CONTEXT = "pending-context.md"
_MAX_STASHED_TURNS = 256
_MAX_STASHED_CHARS = 8_000


def _log(msg: str) -> None:
    try:
        print(LOG_PREFIX + " " + msg, file=sys.stderr)
    except Exception:
        # never throw from logging
        pass


def _resolve_vendor_root() -> Path | None:
    """THROUGHLINER_ROOT override, else the vendor tree next to this file.

    A path that is not a usable vendor tree is the same as none: the plugin
    disables itself instead of running inert hooks against missing files.
    """
    if os.environ.get("THROUGHLINER_ROOT"):
        root = Path(os.environ["THROUGHLINER_ROOT"]).expanduser().resolve()
    else:
        root = Path(__file__).resolve().parent / "vendor" / "throughliner"
    try:
        if not (root / "hooks" / "pre_tool_use.py").is_file():
            return None
    except OSError:
        return None
    return root


VENDOR_ROOT: Path | None = _resolve_vendor_root()


def _trace(cwd: str, sid: str | None, entry: dict) -> None:
    """Best-effort debug channel: one JSON line per hook fire, appended to
    <cwd>/.throughliner/.shim-<sessionID>.jsonl — the primary observation
    channel for live runs. Never throws."""
    try:
        if not cwd or not sid:
            return
        dirpath = Path(cwd) / ".throughliner"
        dirpath.mkdir(parents=True, exist_ok=True)
        line = json.dumps({"at": datetime.now(timezone.utc).isoformat(), "session": sid, **entry})
        with open(dirpath / f".shim-{sid[:40]}.jsonl", "a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except Exception:
        # tracing must never affect the session
        pass


def _python_bin() -> str:
    """The interpreter for the vendored hooks (stdlib-only)."""
    return os.environ.get("THROUGHLINER_PYTHON") or sys.executable


def _expand_plugin_root(obj):
    """Expand ``${CLAUDE_PLUGIN_ROOT}`` in hook output.

    Claude Code expands that variable in hook context on the harness side;
    Hermes does not, so the literal template would reach the model and the
    model would guess the path. The vendor code stays pristine, so the shim
    expands it here.
    """
    if isinstance(obj, str):
        return obj.replace("${CLAUDE_PLUGIN_ROOT}", str(VENDOR_ROOT))
    if isinstance(obj, dict):
        return {k: _expand_plugin_root(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_expand_plugin_root(v) for v in obj]
    return obj

def _run_hook(script: str, payload: dict, timeout: int = 30) -> dict | None:
    """Spawn a vendored hook, feed it Claude-protocol JSON on stdin, parse the
    JSON reply. Fail-open on every failure mode."""
    if VENDOR_ROOT is None:
        return None
    try:
        proc = subprocess.run(
            [_python_bin(), str(VENDOR_ROOT / "hooks" / script)],
            input=json.dumps(payload),
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=payload.get("cwd") or None,
            env={**os.environ, "CLAUDE_PLUGIN_ROOT": str(VENDOR_ROOT)},
        )
    except Exception as exc:
        _log(f"{script} spawn failed: {exc} — failing open")
        return None
    if proc.returncode != 0 and not proc.stdout:
        _log(f"{script} exited {proc.returncode}: {proc.stderr[:400]} — failing open")
        return None
    text = proc.stdout.strip()
    if not text:
        return None
    for candidate in (text, *reversed([l for l in text.splitlines() if l.strip()])):
        try:
            parsed = json.loads(candidate)
        except (json.JSONDecodeError, ValueError):
            continue
        if isinstance(parsed, dict):
            return _expand_plugin_root(parsed)
    _log(f"{script} returned non-JSON output — failing open")
    return None


def _append_pending_context(cwd: str, text: str) -> None:
    """File-mediated handoff: Hermes has no context channel on
    post_tool_call/on_session_end, so advisory findings are appended here and
    drained by pre_llm_call on the next LLM call (any session in this
    project). Best-effort; project-level so a dead one-shot's note reaches
    the next session."""
    try:
        dirpath = Path(cwd) / ".throughliner"
        dirpath.mkdir(parents=True, exist_ok=True)
        with open(dirpath / _PENDING_CONTEXT, "a", encoding="utf-8") as fh:
            fh.write(text.rstrip() + "\n")
    except Exception as exc:
        _log(f"pending-context append failed: {exc}")


def _drain_pending_context(cwd: str) -> str:
    """Read and clear the pending-context file. Returns "" when empty."""
    try:
        dirpath = Path(cwd) / ".throughliner"
        path = dirpath / _PENDING_CONTEXT
        if not path.is_file():
            return ""
        content = path.read_text(encoding="utf-8").strip()
        try:
            path.unlink()
        except OSError:
            # leave it; it will be drained next time
            pass
        return content
    except Exception:
        return ""


# ---------------------------------------------------------------------------
# Claude tool-name mapping (Hermes tool -> vendored hook tool_name)
# ---------------------------------------------------------------------------

TOOL_MAP = {
    "write_file": "Write",
    "patch": "Edit",
    "terminal": "Bash",
    "delegate_task": "Task",
    "skill_view": "Skill",
}


def _tool_input(tool_name: str, args: dict, cwd: str) -> dict:
    """Build the Claude tool_input from Hermes tool args. The vendored hooks
    read exactly: file_path (Edit/Write/MultiEdit), command (Bash), skill
    (Skill). Relative paths are resolved against cwd — the Claude protocol is
    absolute."""
    out: dict = {}
    if tool_name in ("write_file", "patch"):
        file_path = args.get("path") or args.get("file_path")
        if isinstance(file_path, str):
            out["file_path"] = file_path if os.path.isabs(file_path) else os.path.abspath(os.path.join(cwd, file_path))
    if tool_name == "terminal":
        if isinstance(args.get("command"), str):
            out["command"] = args["command"]
    if tool_name == "skill_view":
        name = args.get("name")
        if isinstance(name, str):
            # The installed skills are namespaced tl-<name>; the vendored
            # Skill arm polices the bare method names.
            bare = name[3:] if name.startswith("tl-") else name
            if bare in SKILL_NAMES:
                out["skill"] = bare
    if tool_name == "delegate_task":
        if isinstance(args.get("description"), str):
            out["description"] = args["description"]
    return out


# ---------------------------------------------------------------------------
# Skill materialization
# ---------------------------------------------------------------------------

def _materialize_skills() -> None:
    """Install the five adapted skill files into the profile skills dir
    idempotently. New files outside vendor/: frontmatter reduced to
    name+description, names tl-<name>, ${CLAUDE_PLUGIN_ROOT} rewritten to the
    real vendored path, /<name> command tokens renamed to /tl-<name>."""
    if VENDOR_ROOT is None:
        return
    base = Path.home() / ".hermes" / "skills" / _SKILLS_CATEGORY
    for name in SKILL_NAMES:
        try:
            body = (VENDOR_ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            parts = body.split("---", 2)
            if len(parts) < 3:
                _log(f"skill materialization failed for {name}: no frontmatter")
                continue
            frontmatter = parts[1]
            rest = parts[2]
            m = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
            description = (m.group(1).strip() if m else f"Throughliner {name} method.").replace('"', '\\"')
            adapted = rest.replace("${CLAUDE_PLUGIN_ROOT}", str(VENDOR_ROOT))
            adapted = re.sub(rf"(?<![\w/])/{name}(?![\w-])", f"/tl-{name}", adapted)
            new_body = f'---\nname: tl-{name}\ndescription: "{description}"\n---\n' + adapted.lstrip()
            dest = base / f"tl-{name}" / "SKILL.md"
            dest.parent.mkdir(parents=True, exist_ok=True)
            current = ""
            try:
                current = dest.read_text(encoding="utf-8")
            except OSError:
                pass
            if current != new_body:
                dest.write_text(new_body, encoding="utf-8")
        except Exception as exc:
            _log(f"skill materialization failed for {name}: {exc}")


def _brevity_content() -> str | None:
    """The vendored output style, as a system-prompt section body."""
    try:
        body = (VENDOR_ROOT / "output-styles" / "brevity.md").read_text(encoding="utf-8")
        parts = body.split("---", 2)
        return parts[2].strip() if len(parts) >= 3 else body.strip()
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Hook callbacks
# ---------------------------------------------------------------------------

# Final assistant text per session (post_llm_call -> on_session_end handoff;
# pre_verify carries its own final_response). Bounded LRU.
_last_text: "OrderedDict[str, str]" = OrderedDict()


def _stash_text(session_id: str, text: str) -> None:
    _last_text[session_id] = text[-_MAX_STASHED_CHARS:]
    while len(_last_text) > _MAX_STASHED_TURNS:
        _last_text.popitem(last=False)


def _pre_tool_call(**kwargs) -> dict | None:
    try:
        tool_name = kwargs.get("tool_name") or ""
        claude_name = TOOL_MAP.get(tool_name)
        if not claude_name:
            return None
        args = kwargs.get("args")
        if not isinstance(args, dict):
            args = {}
        cwd = os.getcwd()
        sid = kwargs.get("session_id") or ""
        payload = {
            "cwd": cwd,
            "session_id": sid,
            "tool_name": claude_name,
            "tool_input": _tool_input(tool_name, args, cwd),
        }
        out = _run_hook("pre_tool_use.py", payload)
        hso = (out or {}).get("hookSpecificOutput") or {}
        decision = hso.get("permissionDecision")
        reason = hso.get("permissionDecisionReason") or "blocked by Throughliner"
        if decision == "deny":
            _trace(cwd, sid, {"hook": "pre_tool_call", "tool": claude_name, "decision": "deny", "action": "block"})
            return {"action": "block", "message": reason}
        if decision == "ask":
            _trace(cwd, sid, {"hook": "pre_tool_call", "tool": claude_name, "decision": "ask", "action": "approve"})
            return {"action": "approve", "message": reason}
        _trace(cwd, sid, {"hook": "pre_tool_call", "tool": claude_name, "decision": "none", "action": "allow"})
        return None
    except Exception as exc:
        _log(f"pre_tool_call error — allowing (fail-open): {exc}")
        return None


def _post_tool_call(**kwargs) -> None:
    """Advisory QUEUE.md lint. No context channel here, so findings are
    parked in .throughliner/pending-context.md for the next pre_llm_call."""
    try:
        tool_name = kwargs.get("tool_name") or ""
        claude_name = TOOL_MAP.get(tool_name)
        if claude_name not in ("Write", "Edit", "Bash"):
            return None
        args = kwargs.get("args")
        if not isinstance(args, dict):
            args = {}
        cwd = os.getcwd()
        sid = kwargs.get("session_id") or ""
        out = _run_hook("post_tool_use.py", {
            "cwd": cwd,
            "session_id": sid,
            "tool_name": claude_name,
            "tool_input": _tool_input(tool_name, args, cwd),
        })
        ctx = (out or {}).get("hookSpecificOutput", {}).get("additionalContext")
        if not ctx:
            return None
        _append_pending_context(cwd, ctx)
        _trace(cwd, sid, {"hook": "post_tool_call", "tool": claude_name, "action": "pending-context-appended"})
    except Exception as exc:
        _log(f"post_tool_call error — ignoring (fail-open): {exc}")
    return None


def _pre_llm_call(**kwargs) -> dict | None:
    """SessionStart orientation on the first LLM call of a turn, plus any
    parked advisory context (lint findings, stop corrections) from earlier
    activity in this project."""
    try:
        cwd = os.getcwd()
        sid = kwargs.get("session_id") or ""
        parts: list[str] = []
        if kwargs.get("is_first_turn") and sid:
            out = _run_hook("session_start.py", {"cwd": cwd, "session_id": sid}, timeout=60)
            ctx = (out or {}).get("hookSpecificOutput", {}).get("additionalContext")
            if ctx:
                # The vendored hooks name per-session working files
                # _build-<id>.md from the hook payload's session_id; Claude
                # Code shows the model its session id natively, Hermes does
                # not, so the shim says it.
                safe_id = re.sub(r"[^A-Za-z0-9._-]", "_", sid)
                parts.append(ctx + f"\nSession ID for this session: {safe_id} — per-session working files are named with it, exactly _build-{safe_id}.md (and _freeform-{safe_id}.md for freeform work).")
        pending = _drain_pending_context(cwd)
        if pending:
            parts.append(f"[Throughliner] notes from earlier activity in this project:\n{pending}")
        if parts:
            _trace(cwd, sid, {"hook": "pre_llm_call", "first_turn": bool(kwargs.get("is_first_turn")), "context_chars": sum(len(p) for p in parts)})
            return {"context": "\n\n".join(parts)}
        return None
    except Exception as exc:
        _log(f"pre_llm_call error — injecting nothing (fail-open): {exc}")
        return None


def _post_llm_call(**kwargs) -> None:
    try:
        sid = kwargs.get("session_id") or ""
        text = kwargs.get("assistant_response")
        if sid and isinstance(text, str) and text:
            _stash_text(sid, text)
    except Exception:
        pass
    return None


def _run_stop(cwd: str, sid: str, text: str) -> dict | None:
    return _run_hook("stop.py", {
        "last_assistant_message": text,
        "cwd": cwd,
        "session_id": sid,
    }, timeout=30)


def _pre_verify(**kwargs) -> dict | None:
    """The stop check with a decision channel: fires when the agent mutated
    files this turn. block = keep the turn going with the correction."""
    try:
        text = kwargs.get("final_response")
        if not isinstance(text, str) or not text:
            return None
        cwd = os.getcwd()
        sid = kwargs.get("session_id") or ""
        out = _run_stop(cwd, sid, text)
        if out and out.get("decision") == "block" and out.get("reason"):
            _trace(cwd, sid, {"hook": "pre_verify", "decision": "block"})
            return {"decision": "block", "reason": out["reason"]}
        _trace(cwd, sid, {"hook": "pre_verify", "decision": "none"})
        return None
    except Exception as exc:
        _log(f"pre_verify error — letting the turn finish (fail-open): {exc}")
        return None


def _on_session_end(**kwargs) -> None:
    """Reliable per-turn observer: runs the stop check when pre_verify could
    not (its primary failure mode — a claimed-but-unfiled slug with no file
    mutation — is invisible to pre_verify). No decision channel here, so a
    block becomes a correction note for the next LLM call."""
    try:
        sid = kwargs.get("session_id") or ""
        text = _last_text.pop(sid, None) if sid else None
        if not text:
            return None
        cwd = os.getcwd()
        out = _run_stop(cwd, sid, text)
        if out and out.get("decision") == "block" and out.get("reason"):
            _append_pending_context(cwd, f"[Throughliner stop check] {out['reason']}")
            _trace(cwd, sid, {"hook": "on_session_end", "decision": "block", "action": "pending-context-appended"})
        else:
            _trace(cwd, sid, {"hook": "on_session_end", "decision": "none"})
    except Exception as exc:
        _log(f"on_session_end error — ignoring (fail-open): {exc}")
    return None


# ---------------------------------------------------------------------------
# Plugin registration
# ---------------------------------------------------------------------------

def register(ctx) -> None:
    if VENDOR_ROOT is None:
        _log("vendored tree not found next to the plugin (expected vendor/throughliner/) — plugin disabled")
        return
    _materialize_skills()
    brevity = _brevity_content()
    if brevity:
        try:
            ctx.register_system_prompt_section("throughliner-brevity", brevity)
        except Exception as exc:
            _log(f"brevity section registration failed: {exc}")
    ctx.register_hook("pre_tool_call", _pre_tool_call)
    ctx.register_hook("post_tool_call", _post_tool_call)
    ctx.register_hook("pre_llm_call", _pre_llm_call)
    ctx.register_hook("post_llm_call", _post_llm_call)
    ctx.register_hook("on_session_end", _on_session_end)
    ctx.register_hook("pre_verify", _pre_verify)
    _log(f"throughliner hooks registered (vendor: {VENDOR_ROOT})")
