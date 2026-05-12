#!/usr/bin/env python3
"""
SessionStart hook for the no-code-method plugin.

Reads universal-behaviour.md (sibling file in the hooks/ directory) and emits
its contents as additionalContext via the SessionStart hook output protocol.
This ensures the universal behavioural rules are loaded into Claude's context
at the start of every session in any project where this plugin is installed.

Why SessionStart and not UserPromptSubmit (the original V18 plan):
  UserPromptSubmit hooks declared in plugin hooks.json don't execute due to
  GitHub bug anthropics/claude-code#10225. SessionStart works in plugins today,
  and given the no-code method's /clear-after-every-build discipline, it's
  functionally equivalent: every new session re-fires the hook.

Output protocol: stdout receives a JSON object with hookSpecificOutput
containing hookEventName ("SessionStart") and additionalContext (the rules
text). Exit code 0.
"""

import json
import sys
from pathlib import Path


def main() -> int:
    rules_path = Path(__file__).parent / "universal-behaviour.md"

    try:
        rules_text = rules_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        # Surface the misconfiguration to Claude rather than silently emitting
        # no rules — the user/Claude should know the plugin is broken.
        rules_text = (
            "[no-code-method plugin warning] "
            f"universal-behaviour.md not found at {rules_path}. "
            "The universal behavioural rules could not be injected. "
            "This is a plugin installation problem, not a method problem."
        )
    except OSError as exc:
        rules_text = (
            "[no-code-method plugin warning] "
            f"Could not read universal-behaviour.md ({exc}). "
            "The universal behavioural rules could not be injected."
        )

    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": rules_text,
        }
    }

    json.dump(output, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
