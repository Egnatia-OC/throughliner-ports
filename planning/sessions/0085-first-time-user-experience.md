# 0085 — First-time user experience: /setup enforcement + build transition

## Goal

Fix the two highest-severity E2E findings: (1) Claude ignores the `/setup` recommendation for uninformed users, and (2) the build-transition sequence is opaque when a user tries to build before the batch is activated.

## Inputs

- E2E research: `research/e2e-greenfield-post-redesign.md` — Findings 1 and 3.
- `plugin/hooks/pre_tool_use.py` — `make_planning_phase_source_lock_reason()` and `check_planning_phase_source_lock()`.
- `plugin/docs/procedures/before-build.md` — Recap section, `[PROMPT]` line.

## Outputs

- Modified `pre_tool_use.py`: when planning-phase source lock fires in an unadopted folder (no CLAUDE.md with method footer), the deny message says "run `/setup` first" instead of referencing BACKLOG/before-build.
- Modified `before-build.md`: recap prompt uses plain English instead of "Switch out of plan mode" jargon.
- Updated tests in `tests/` for the new deny message path.
- Updated `Reference manual.md` if the deny-message change affects documented behaviour.

## Success criteria

1. In a fresh empty folder with the plugin installed, typing an app idea triggers a deny message that explicitly says "run `/setup` first."
2. After `/setup` + asking to build, the before-build recap uses language a non-coder understands.
3. Existing pytest suite passes with the new deny path.

## Open questions for this session

1. Should the deny message for unadopted folders differ between "empty folder" and "folder with pre-existing work"? The adoption gate (V29) already handles the latter — this fix targets the gap where the folder is empty (no work, so V29 doesn't fire).
2. What should replace "Switch out of plan mode"? Options: "Run `/build` to start building" (drop the plan-mode reference entirely) or explain what plan mode is in plain English.

## Risks / dependencies

- Changing deny-message text may require updating test assertions in `tests/`.
- The "plan mode" language lives in the before-build procedure doc, not in hook code — it's advisory text Claude reads, not enforced. Changing it may not change Claude's output if Claude paraphrases.
