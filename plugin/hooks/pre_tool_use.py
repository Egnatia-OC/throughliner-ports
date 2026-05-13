#!/usr/bin/env python3
"""
PreToolUse hook for the no-code-method plugin.

Enforces read-only on locked source-of-truth docs during builds. Locked docs
are: UX.md, plus any additional source-of-truth docs declared in the project's
CLAUDE.md path block. BACKLOG.md and MANIFEST.md are explicitly writable and
are not locked.

When an Edit, Write, or MultiEdit targets a locked doc, the hook denies the
tool call with a reason that tells Claude to add a [FOLD-IN PENDING] block
to the Fold-ins pending section of BACKLOG.md instead. The full mechanism is
documented in NO-CODE-METHOD.md > Editing surfaces and the block format is
in DOC-STRUCTURE.md > BACKLOG.md structure > Fold-ins pending. The hook
doesn't repeat the mechanism — it names the section and lets Claude consult
those docs (or its own SessionStart-injected rules) for the specifics.

The hook is deliberately lenient on edge cases — missing CLAUDE.md, an
unparseable path block, the target file sitting outside the project root: in
all such cases it allows the tool call rather than blocking. A hook that
blocks unexpectedly is far more disruptive than one that occasionally fails
to enforce. The universal-behaviour rules surfaced via the SessionStart hook
are the soft-net for any case this hook can't deterministically catch.

Why three writing tools and not more: the method's locked-docs rule is about
deliberate written changes. NotebookEdit and other adjacent tools are not in
scope for the spine docs.

Output protocol: stdout receives a JSON object with hookSpecificOutput
containing hookEventName ("PreToolUse"), permissionDecision ("deny"), and
permissionDecisionReason (the message Claude reads). For allow-cases, the
hook writes nothing and exits 0 — the absence of a deny is an implicit allow.
"""

import json
import re
import sys
from pathlib import Path

# Tools whose calls this hook inspects. Anything outside this set is allowed
# without inspection.
WRITING_TOOLS = {"Edit", "Write", "MultiEdit"}

# Path-block keys treated as writable. Everything else in the path block —
# UX.md, plus any additional source-of-truth docs declared by the project —
# is locked.
WRITABLE_LOGICAL_NAMES = {"BACKLOG.md", "MANIFEST.md"}

# CLAUDE.md's path block is the first fenced JSON code block in the file.
# Match the contents between the opening ```json line and the closing ```.
PATH_BLOCK_PATTERN = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)


def emit_allow() -> int:
    """Allow the tool call by writing nothing. Returns exit code 0."""
    return 0


def emit_deny(reason: str) -> int:
    """Deny the tool call with the given reason text. Returns exit code 0
    (the deny itself communicates the outcome — non-zero exit is reserved
    for hook errors)."""
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }
    json.dump(output, sys.stdout)
    return 0


def parse_input():
    """Read the hook input JSON from stdin. Return dict on success, None on
    any parse failure."""
    try:
        return json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return None


def extract_path_block(claude_md_text: str):
    """Extract and parse the first fenced JSON code block from CLAUDE.md.

    Returns the parsed dict, or None if the block is missing or unparseable.
    """
    match = PATH_BLOCK_PATTERN.search(claude_md_text)
    if not match:
        return None
    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict):
        return None
    return data


def build_locked_map(project_root: Path) -> dict:
    """Read CLAUDE.md from project_root, parse the path block, and return a
    dict mapping resolved absolute path strings -> logical names for every
    LOCKED doc in the path block.

    Returns an empty dict if CLAUDE.md is missing, has no parseable path
    block, or contains no locked entries. The hook treats an empty locked
    map as "no enforcement applicable" and falls through to allow.
    """
    claude_path = project_root / "CLAUDE.md"
    try:
        text = claude_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}

    path_block = extract_path_block(text)
    if not path_block:
        return {}

    locked: dict = {}
    for logical_name, relative_path in path_block.items():
        if not isinstance(logical_name, str) or not isinstance(relative_path, str):
            continue
        if logical_name in WRITABLE_LOGICAL_NAMES:
            continue
        try:
            resolved = (project_root / relative_path).resolve()
        except OSError:
            continue
        locked[str(resolved)] = logical_name
    return locked


def make_reason(logical_name: str) -> str:
    """Build the deny-reason text Claude sees when a locked-doc edit is
    blocked. The reason tells Claude exactly where to place the proposed
    change — the *Fold-ins pending* section of BACKLOG.md — so the
    instruction is unambiguous in any project layout."""
    return (
        f"BLOCKED: {logical_name} is a locked source-of-truth doc. It is "
        f"read-only to Claude Code; only the user can edit it, in Cowork.\n\n"
        f"If you have identified a {logical_name} change that should "
        "happen, do not retry this edit. Instead, add a `[FOLD-IN PENDING]` "
        "block to the *Fold-ins pending* section of BACKLOG.md, with "
        f"destination `{logical_name}` and origin `mid-build edit attempt "
        "— <today's date>`. The user will fold the block into "
        f"{logical_name} in their next Cowork session, or drop it. "
        "Surface this addition plainly in your response to the user. "
        "Canonical block format and section placement: see DOC-STRUCTURE.md "
        "→ BACKLOG.md structure → Fold-ins pending."
    )


def main() -> int:
    data = parse_input()
    if not isinstance(data, dict):
        return emit_allow()

    tool_name = data.get("tool_name")
    if tool_name not in WRITING_TOOLS:
        return emit_allow()

    tool_input = data.get("tool_input") or {}
    file_path_str = tool_input.get("file_path")
    if not isinstance(file_path_str, str) or not file_path_str:
        return emit_allow()

    cwd_str = data.get("cwd")
    if not isinstance(cwd_str, str) or not cwd_str:
        return emit_allow()

    try:
        project_root = Path(cwd_str).resolve()
    except OSError:
        return emit_allow()

    target_path = Path(file_path_str)
    try:
        if target_path.is_absolute():
            target_path = target_path.resolve()
        else:
            target_path = (project_root / target_path).resolve()
    except OSError:
        return emit_allow()

    locked_map = build_locked_map(project_root)
    if not locked_map:
        return emit_allow()

    logical_name = locked_map.get(str(target_path))
    if not logical_name:
        return emit_allow()

    return emit_deny(make_reason(logical_name))


if __name__ == "__main__":
    sys.exit(main())
