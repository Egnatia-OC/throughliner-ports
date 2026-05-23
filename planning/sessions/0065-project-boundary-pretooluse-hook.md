# 0065 — Project-boundary PreToolUse hook

## Goal

Add a new deny path to the PreToolUse hook that blocks Edit, Write, and MultiEdit calls targeting paths outside the project root. During the 0060 E2E test, a Taskflow session with the plugin installed could write to any path on the filesystem, including the plugin's own source code in a different folder.

## Inputs

- E2E finding 3 from `planning/sessions/0060-taskflow-e2e-prep-and-testing.md`
- `plugin/hooks/pre_tool_use.py` (existing PreToolUse hook)

## Outputs

- New deny path in `pre_tool_use.py`: when the tool is Edit, Write, or MultiEdit, resolve the target file path and check whether it falls inside the project root (available from the hook's input as `cwd` or equivalent). Deny with a `[No-code method]` message if outside.
- Mode-aware suffix on the deny message (matching V43 pattern)
- Test coverage in `tests/` for the new deny path

## Success criteria

- Edit/Write/MultiEdit to a path outside the project root is denied with a clear message
- Edit/Write/MultiEdit to a path inside the project root passes through (existing behaviour unchanged)
- Existing deny paths (locked docs, batch file list, etc.) unaffected

## Open questions for this session

- Should Bash tool calls that write outside the project root also be blocked? Bash is harder to inspect (arbitrary commands), but `cd /other/folder && ...` or explicit absolute paths in shell commands are the same class of risk. Decide at session start — may be a separate scope if complex.
- How does Claude Code pass the project root to hook scripts? Confirm the mechanism before implementing.

## Risks / dependencies

- None — this is a standalone new deny path with no dependencies on other scopes.
