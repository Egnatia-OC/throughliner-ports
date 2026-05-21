#!/usr/bin/env python3
"""
PreToolUse hook — git safety guard (V34).

Denies two destructive git commands from Bash:
  - git reset --hard  (destroys uncommitted work, irreversible)
  - git push --force / git push -f  (overwrites remote history)

Does NOT block:
  - git reset (soft/mixed)
  - git push (without --force)
  - git push --force-with-lease (safer alternative with remote-check)
  - git commit, git tag, git add, git checkout, etc.

Matcher in hooks.json is `Bash` — this hook only sees Bash tool calls.
The existing pre_tool_use.py handles Edit/Write/MultiEdit/Task checks
(locked docs, serves lines, batch boundary, adoption gate, test gate);
this file is deliberately separate because the matcher and concern
domain are different.

Output protocol: same as pre_tool_use.py — stdout receives a JSON
object with hookSpecificOutput containing permissionDecision "deny"
and permissionDecisionReason. Allow cases write nothing and exit 0.
"""

import json
import re
import sys


RESET_HARD = re.compile(r"\bgit\b.*\breset\b.*--hard\b")

# --force but NOT --force-with-lease (the safer alternative).
# Also catches the short flag -f when it follows `git push`.
PUSH_FORCE = re.compile(r"\bgit\b.*\bpush\b.*(?:--force(?!-with-lease)\b|-f\b)")


_MODE_AWARE_SUFFIX = (
    "\n\nChanging your Claude Code permission mode won't unlock this — "
    "this is a method rule enforced by the no-code-method plugin's hook, "
    "not a Claude Code permission check."
)


def _mode_suffix(permission_mode: str) -> str:
    """Return _MODE_AWARE_SUFFIX for permissive modes, empty string otherwise."""
    if not permission_mode:
        return ""
    m = permission_mode.lower()
    if "auto" in m or "bypass" in m or "accept" in m:
        return _MODE_AWARE_SUFFIX
    return ""


def make_reset_hard_reason(permission_mode: str) -> str:
    return (
        "[No-code method] BLOCKED: `git reset --hard` destroys uncommitted "
        "work and cannot be undone.\n\n"
        "What to do: use a safer alternative:\n"
        "- `git stash` — saves your changes so you can restore them later.\n"
        "- `git checkout -- <file>` — discards changes to one specific file.\n"
        "- `git reset --soft HEAD~1` — moves HEAD back but keeps all changes "
        "staged (nothing is lost).\n"
        "- `git reset HEAD~1` (mixed, the default) — moves HEAD back and "
        "unstages, but keeps the working tree intact.\n\n"
        "If you genuinely need to discard everything, the user can run "
        "`git reset --hard` themselves outside Claude Code."
        + _mode_suffix(permission_mode)
    )


def make_push_force_reason(permission_mode: str) -> str:
    return (
        "[No-code method] BLOCKED: `git push --force` can overwrite commits "
        "on the remote that you or a collaborator pushed from another machine "
        "or session.\n\n"
        "What to do: use `git push --force-with-lease` instead. It does the "
        "same thing but refuses to push if the remote has commits you haven't "
        "fetched — a built-in check against overwriting someone else's work. "
        "If you genuinely need a force push, the user can run it themselves "
        "outside Claude Code."
        + _mode_suffix(permission_mode)
    )


def emit_deny(reason: str) -> int:
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }
    json.dump(output, sys.stdout)
    return 0


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, ValueError):
        return 0

    if not isinstance(data, dict):
        return 0

    tool_input = data.get("tool_input") or {}
    command = tool_input.get("command")
    if not isinstance(command, str) or not command:
        return 0

    permission_mode = data.get("permission_mode", "")
    if not isinstance(permission_mode, str):
        permission_mode = ""

    if RESET_HARD.search(command):
        return emit_deny(make_reset_hard_reason(permission_mode))

    if PUSH_FORCE.search(command):
        return emit_deny(make_push_force_reason(permission_mode))

    return 0


if __name__ == "__main__":
    sys.exit(main())
