# 3633c7d — Shell-write matcher test suite added and wired into the rezip ritual; file-safety gains the two missing routes

Built in the 2026-08-08 overnight blitz. Both limbs of the item shipped, and its test did exactly the job it was built for.

Limb 1: `resources/testing/test_pre_tool_use_shell_writes.py` drives `pre_tool_use` as a subprocess with real PreToolUse payloads — the two command shapes that actually slipped (a heredoc append to a template, a heredoc multi-site substitution in a procedure doc), a computed-path case pinning the deliberate fail-open as intended, plus build-scoping and non-writing-command cases. Six cases, all green. Wired into CLAUDE.md's rezip ritual beside the other two suites, since an unwired suite guards nothing.

Limb 2: `docs-b/plugin-behaviour.md`'s file-safety routes grow from three to five, naming the cheap safe path for the two shapes that actually tempt the shell — appending to the end of a long file (read the tail, anchor an Edit on it) and multi-site substitution (sequential Edits / MultiEdit, never a scripted pass). Stated as sanctioned routes, not a louder prohibition, per the mover's own lesson.

The finding: the matcher denies only out-of-scope targets, and both real slips wrote **in-scope** files — so the mechanical check would have caught neither. That coverage claim was exactly what the item said had to be tested rather than reasoned about; the hook was left unchanged (extending the denial to in-scope targets is a hook-behaviour design call) and the gap filed.

**Files touched:** resources/testing/test_pre_tool_use_shell_writes.py (new), plugin/si-plugin/docs-b/plugin-behaviour.md, CLAUDE.md
**Routed to Captures:** [shell-write-matcher-blind-to-in-scope-targets]
FAQ: not needed because these are rules about which tool Claude reaches for, invisible to a consumer.
