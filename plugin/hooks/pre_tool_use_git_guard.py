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


RESET_HARD_REASON = (
    "BLOCKED: `git reset --hard` destroys uncommitted work and cannot be "
    "undone. This is one of two git commands the method's safety guard "
    "blocks.\n\n"
    "Safer alternatives:\n"
    "- `git stash` — saves your changes so you can restore them later.\n"
    "- `git checkout -- <file>` — discards changes to one specific file.\n"
    "- `git reset --soft HEAD~1` — moves HEAD back but keeps all changes "
    "staged (nothing is lost).\n"
    "- `git reset HEAD~1` (mixed, the default) — moves HEAD back and "
    "unstages, but keeps the working tree intact.\n\n"
    "If you genuinely need to discard everything, the user can run "
    "`git reset --hard` themselves outside Claude Code."
)

PUSH_FORCE_REASON = (
    "BLOCKED: `git push --force` can overwrite commits on the remote that "
    "you or a collaborator pushed from another machine or session. This is "
    "one of two git commands the method's safety guard blocks.\n\n"
    "Safer alternative: `git push --force-with-lease`. It does the same "
    "thing but refuses to push if the remote has commits you haven't "
    "fetched — a built-in check against overwriting someone else's work.\n\n"
    "If you genuinely need a force push, the user can run it themselves "
    "outside Claude Code."
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

    if RESET_HARD.search(command):
        return emit_deny(RESET_HARD_REASON)

    if PUSH_FORCE.search(command):
        return emit_deny(PUSH_FORCE_REASON)

    return 0


if __name__ == "__main__":
    sys.exit(main())
