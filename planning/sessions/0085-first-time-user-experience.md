# 0085 — First-time user experience: /setup enforcement + build transition + parent-dir warning

## Goal

Fix the two highest-severity E2E findings and add a parent-directory advisory: (1) Claude ignores the `/setup` recommendation for uninformed users, (2) the build-transition sequence is opaque when a user tries to build before the batch is activated, and (3) no warning when a project folder sits inside another project's tree, causing Claude Code's parent-directory CLAUDE.md inheritance to poison the session.

## Inputs

- E2E research: `research/e2e-greenfield-post-redesign.md` — Findings 1 and 3.
- E2E research: `research/e2e-greenfield-post-redesign.md` — Findings 1 and 5 (parent-directory inheritance).
- `plugin/hooks/pre_tool_use.py` — `make_planning_phase_source_lock_reason()` and `check_planning_phase_source_lock()`.
- `plugin/hooks/session_start.py` — SessionStart hook (parent-directory detection target).
- `plugin/docs/procedures/before-build.md` — Recap section, `[PROMPT]` line.

## Outputs

- Modified `pre_tool_use.py`: when planning-phase source lock fires in an unadopted folder (no CLAUDE.md with method footer), the deny message says "run `/setup` first" instead of referencing BACKLOG/before-build.
- Modified `before-build.md`: recap prompt uses plain English instead of "Switch out of plan mode" jargon.
- Updated tests in `tests/` for the new deny message path.
- Updated `Reference manual.md` if the deny-message change affects documented behaviour.
- Modified `session_start.py`: detect parent-directory CLAUDE.md files and surface an advisory in the session-open summary (e.g. "Warning: a CLAUDE.md in a parent directory may affect this session").
- Added parent-directory placement constraint to `Reference manual.md`.

## Success criteria

1. In a fresh empty folder with the plugin installed, typing an app idea triggers a deny message that explicitly says "run `/setup` first."
2. After `/setup` + asking to build, the before-build recap uses language a non-coder understands.
3. Existing pytest suite passes with the new deny path.
4. When a project folder is inside another project's tree (parent directory has a CLAUDE.md), SessionStart surfaces a visible advisory.

## Open questions for this session

1. Should the deny message for unadopted folders differ between "empty folder" and "folder with pre-existing work"? The adoption gate (V29) already handles the latter — this fix targets the gap where the folder is empty (no work, so V29 doesn't fire).
2. What should replace "Switch out of plan mode"? Options: "Run `/build` to start building" (drop the plan-mode reference entirely) or explain what plan mode is in plain English.
3. Should the parent-directory advisory be a hard warning (always shown) or only when the parent CLAUDE.md looks like a different project? Claude Code walks up the tree and loads all CLAUDE.md files it finds — detecting "different project" may not be reliable.

## Risks / dependencies

- Changing deny-message text may require updating test assertions in `tests/`.
- The "plan mode" language lives in the before-build procedure doc, not in hook code — it's advisory text Claude reads, not enforced. Changing it may not change Claude's output if Claude paraphrases.
- Parent-directory detection adds a filesystem walk to SessionStart. Should be lightweight (walk up until root, check for CLAUDE.md at each level), but adds a new code path to test.
