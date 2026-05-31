# V67 — 2026-05-25 — Phase-aware editing surfaces

**What shipped.** PreToolUse hook now detects project phase via BACKLOG batch status and flips editing permissions accordingly. During planning: source-of-truth docs (UX.md, additional docs) are directly editable; source code is locked. During build: source-of-truth docs locked (with existing footer + proposed-edits carve-outs); batch file list open. Four new helper functions (`detect_phase`, `is_path_block_doc`, `is_research_file`, `check_planning_phase_source_lock`). Eight new tests in `TestPlanningPhasePermissions`. Docs updated across universal-behaviour.md, DOC-STRUCTURE.md, VOCABULARY.md, Reference manual, all procedure docs, crash-course HTML. OPEN-QUESTIONS item 3 (proposed-edit UX friction) largely resolved — the ceremony is eliminated during planning.

**Decisions taken and why.** (1) Phase detection uses batch `Status: active` rather than a separate state file — the parser already exposes it and it's the ground truth. (2) MANIFEST stays writable during both phases because it mirrors codebase state which changes during build. (3) `research/` files are exempt from the planning-phase source lock — they're project docs, not source code. (4) V39 read-before-edit gate and test-confirmation gate fire only during build — both are irrelevant when source code is already locked.

**Pivots and surprises.** Existing test fixtures had no `Status: active` line, so `detect_phase()` returned "planning" and broke 5 existing tests. Fixed by adding the status line to the build-phase fixture rather than special-casing the logic.

**Carried forward.** OPEN-QUESTIONS item 3 can be formally dropped — all seven items now resolved.
