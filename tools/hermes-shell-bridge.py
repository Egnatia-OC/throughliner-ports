#!/usr/bin/env python3
"""Shell-hook bridge for the manual (no-plugin) Throughliner install.

Hermes shell hooks execute a command with the hook payload on stdin and read
a directive from stdout. The vendored hooks speak Claude-protocol envelopes
(`hookSpecificOutput.permissionDecision`, ...), which shell hooks do not
parse — this bridge translates:

  pre_tool_call  -> pre_tool_use.py   deny -> {"action":"block","message"}
                                       ask  -> {"action":"block","message"}
                                       (shell hooks have no approve channel,
                                       so the subagent cost gate degrades
                                       from "ask" to "deny with explanation")
  post_tool_call -> post_tool_use.py  findings -> .throughliner/
                                       pending-context.md (drained by
                                       pre_llm_call)
  pre_llm_call   -> session_start.py  (is_first_turn only) -> {"context"}
                                       + drained pending-context notes
  pre_verify     -> stop.py           block -> {"decision":"block","reason"}
  post_llm_call  -> stashes the final response text to
                    .throughliner/.last-response-<sid>.txt so on_session_end
  on_session_end -> stop.py           (reads the stash) block -> parked note

Exit code: always 0. The bridge fails open on every error — it never blocks
a tool or injects a bad directive.

Usage in ~/.hermes/config.yaml:

  hooks:
    pre_tool_call:
      - command: "/path/to/this/repo/tools/hermes-shell-bridge.py pre_tool_call"
    post_tool_call:
      - command: "/path/to/this/repo/tools/hermes-shell-bridge.py post_tool_call"
    pre_llm_call:
      - command: "/path/to/this/repo/tools/hermes-shell-bridge.py pre_llm_call"
    pre_verify:
      - command: "/path/to/this/repo/tools/hermes-shell-bridge.py pre_verify"
    post_llm_call:
      - command: "/path/to/this/repo/tools/hermes-shell-bridge.py post_llm_call"
    on_session_end:
      - command: "/path/to/this/repo/tools/hermes-shell-bridge.py on_session_end"

The vendored tree is resolved from THROUGHLINER_ROOT, else from this file's
location (<repo>/tools/ -> <repo>/vendor/throughliner).
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

TOOL_MAP = {
    "write_file": "Write",
    "patch": "Edit",
    "terminal": "Bash",
    "delegate_task": "Task",
    "skill_view": "Skill",
}
SKILL_NAMES = ("setup", "plan", "next", "rescan", "done")
_PENDING_CONTEXT = "pending-context.md"


def _vendor_root() -> Path | None:
    if os.environ.get("THROUGHLINER_ROOT"):
        root = Path(os.environ["THROUGHLINER_ROOT"]).expanduser().resolve()
    else:
        root = Path(__file__).resolve().parent.parent / "vendor" / "throughliner"
    try:
        if not (root / "hooks" / "pre_tool_use.py").is_file():
            return None
    except OSError:
        return None
    return root


VENDOR_ROOT = _vendor_root()


def _log(msg: str) -> None:
    try:
        print("[throughliner-bridge] " + msg, file=sys.stderr)
    except Exception:
        pass


def _python_bin() -> str:
    return os.environ.get("THROUGHLINER_PYTHON") or sys.executable


def _run_hook(script: str, payload: dict, timeout: int = 30) -> dict | None:
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
    if proc.returncode not in (0, 2) and not proc.stdout:
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
            return parsed
    return None


def _tool_input(tool_name: str, args: dict, cwd: str) -> dict:
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
            bare = name[3:] if name.startswith("tl-") else name
            if bare in SKILL_NAMES:
                out["skill"] = bare
    return out


def _append_pending(cwd: str, text: str) -> None:
    try:
        dirpath = Path(cwd) / ".throughliner"
        dirpath.mkdir(parents=True, exist_ok=True)
        with open(dirpath / _PENDING_CONTEXT, "a", encoding="utf-8") as fh:
            fh.write(text.rstrip() + "\n")
    except Exception:
        pass


def _drain_pending(cwd: str) -> str:
    try:
        path = Path(cwd) / ".throughliner" / _PENDING_CONTEXT
        if not path.is_file():
            return ""
        content = path.read_text(encoding="utf-8").strip()
        try:
            path.unlink()
        except OSError:
            pass
        return content
    except Exception:
        return ""


def main(argv: list[str]) -> int:
    event = argv[1] if len(argv) > 1 else ""
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    if VENDOR_ROOT is None:
        _log("vendored tree not found — bridge inert")
        return 0

    try:
        if event == "pre_tool_call":
            tool_name = payload.get("tool_name") or ""
            claude_name = TOOL_MAP.get(tool_name)
            if not claude_name:
                return 0
            args = payload.get("tool_input") or {}
            if not isinstance(args, dict):
                args = {}
            cwd = payload.get("cwd") or os.getcwd()
            out = _run_hook("pre_tool_use.py", {
                "cwd": cwd,
                "session_id": payload.get("session_id") or "",
                "tool_name": claude_name,
                "tool_input": _tool_input(tool_name, args, cwd),
            })
            hso = (out or {}).get("hookSpecificOutput") or {}
            decision = hso.get("permissionDecision")
            reason = hso.get("permissionDecisionReason") or "blocked by Throughliner"
            if decision == "deny":
                print(json.dumps({"action": "block", "message": reason}))
            elif decision == "ask":
                # No approve channel in shell hooks: the cost gate degrades
                # to a deny with the explanation.
                print(json.dumps({
                    "action": "block",
                    "message": reason + "\n\n[Throughliner] Shell hooks cannot prompt for approval; re-run this work without a subagent, or use the plugin install for the interactive gate.",
                }))
            return 0

        if event == "post_tool_call":
            tool_name = payload.get("tool_name") or ""
            claude_name = TOOL_MAP.get(tool_name)
            if claude_name not in ("Write", "Edit", "Bash"):
                return 0
            args = payload.get("tool_input") or {}
            if not isinstance(args, dict):
                args = {}
            cwd = payload.get("cwd") or os.getcwd()
            out = _run_hook("post_tool_use.py", {
                "cwd": cwd,
                "session_id": payload.get("session_id") or "",
                "tool_name": claude_name,
                "tool_input": _tool_input(tool_name, args, cwd),
            })
            ctx = (out or {}).get("hookSpecificOutput", {}).get("additionalContext")
            if ctx:
                _append_pending(cwd, ctx)
            return 0

        if event == "pre_llm_call":
            extra = payload.get("extra") or {}
            cwd = payload.get("cwd") or os.getcwd()
            sid = payload.get("session_id") or ""
            parts = []
            if extra.get("is_first_turn") and sid:
                out = _run_hook("session_start.py", {"cwd": cwd, "session_id": sid}, timeout=60)
                ctx = (out or {}).get("hookSpecificOutput", {}).get("additionalContext")
                if ctx:
                    safe_id = re.sub(r"[^A-Za-z0-9._-]", "_", sid)
                    parts.append(ctx + f"\nSession ID for this session: {safe_id} — per-session working files are named with it, exactly _build-{safe_id}.md (and _freeform-{safe_id}.md for freeform work).")
            pending = _drain_pending(cwd)
            if pending:
                parts.append(f"[Throughliner] notes from earlier activity in this project:\n{pending}")
            if parts:
                print(json.dumps({"context": "\n\n".join(parts)}))
            return 0

        if event == "post_llm_call":
            # Stash the final response for on_session_end (separate process
            # per hook fire, so the handoff is via file).
            cwd = payload.get("cwd") or os.getcwd()
            sid = payload.get("session_id") or ""
            text = (payload.get("extra") or {}).get("assistant_response")
            if isinstance(text, str) and text and sid:
                try:
                    dirpath = Path(cwd) / ".throughliner"
                    dirpath.mkdir(parents=True, exist_ok=True)
                    (dirpath / f".last-response-{sid[:40]}.txt").write_text(text[-8000:], encoding="utf-8")
                except Exception:
                    pass
            return 0

        if event == "on_session_end":
            cwd = payload.get("cwd") or os.getcwd()
            sid = payload.get("session_id") or ""
            stash = (Path(cwd) / ".throughliner" / f".last-response-{sid[:40]}.txt")
            text = ""
            try:
                if stash.is_file():
                    text = stash.read_text(encoding="utf-8")
                    stash.unlink()
            except OSError:
                pass
            if not text:
                return 0
            out = _run_hook("stop.py", {
                "last_assistant_message": text,
                "cwd": cwd,
                "session_id": sid,
            }, timeout=30)
            if out and out.get("decision") == "block" and out.get("reason"):
                _append_pending(cwd, f"[Throughliner stop check] {out['reason']}")
            return 0

        if event == "pre_verify":
            cwd = payload.get("cwd") or os.getcwd()
            sid = payload.get("session_id") or ""
            text = payload.get("final_response")
            if not isinstance(text, str) or not text:
                return 0
            out = _run_hook("stop.py", {
                "last_assistant_message": text,
                "cwd": cwd,
                "session_id": sid,
            }, timeout=30)
            if out and out.get("decision") == "block" and out.get("reason"):
                print(json.dumps({"decision": "block", "reason": out["reason"]}))
            return 0

        return 0
    except Exception as exc:
        _log(f"{event} error — failing open: {exc}")
        return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
