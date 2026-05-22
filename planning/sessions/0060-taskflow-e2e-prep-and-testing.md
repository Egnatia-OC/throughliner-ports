# 0060 — Taskflow E2E prep and testing

## Goal

Prepare Taskflow's docs for a plugin-driven build cycle (structural migration from V34 to current), then run the plugin against Taskflow in a parallel session to gather E2E test notes. This is the first real-project test since V35, covering the six versions of deferred smoke tests (V43–V50).

## Inputs

- Taskflowapp folder at `C:\Users\Alex\Desktop\Taskflowapp` (write access required — read-only restriction lifted for this session)
- Taskflowapp's current spine docs in `no-code-method/` subfolder (BACKLOG.md, MANIFEST.md, UX.md, BUILD-LOG.md, TEST-LOG.md)
- Taskflowapp's CLAUDE.md (written by `/setup` at V34)
- Deferred smoke-test list from dev-project CLAUDE.md → *What's next*: V43 mode-aware messaging, V45 fold-in section carve-out, V46 automated test pass, V48 BACKLOG folder-split, V49 batch structure, V49 research folder, V50 build-log folder

## Outputs

- Taskflowapp docs migrated to V50 structure (BACKLOG folder, build-log folder, fold-ins resolved, orphaned files removed)
- E2E test notes from a planning-and-build cycle run with the plugin active in a parallel Taskflow session
- Test notes formatted as input for the next dev-side planning round (before 0054)

## Success criteria

- Taskflowapp's docs pass `/setup` case 4 structural migration cleanly
- At least one planning-and-build cycle completes in the parallel plugin session
- Test notes captured for every deferred smoke-test item
- No regressions in Taskflowapp's existing planning docs (content preserved, structure updated)

## Prep work (done from this dev-side session)

1. Lift read-only restriction on Taskflowapp in this project's CLAUDE.md (session-scoped or permanent — decide at session start)
2. Delete orphaned files: root-level `SYSTEM-PROMPT.md` (duplicate of the one declared in the path block), `CLAUDE.md.foreign-backup-2026-05-21`
3. Resolve the two pending fold-ins (UX.md and SYSTEM-PROMPT.md version footers)
4. Structural migration: BACKLOG single-file → folder format, BUILD-LOG single-file → folder format

## E2E test (user-driven in parallel session)

5. User toggles SI plugin on in a separate Taskflow Claude Code session
6. Run a planning-and-build cycle with the plugin driving
7. Observe plugin behaviour against every deferred smoke-test item
8. Bring observations back to this session as test notes

## Open questions for this session

- Should the Taskflowapp read-only restriction be lifted permanently (since future E2E testing will recur) or restored after this session?
- The `no-code-method/` subfolder convention in Taskflowapp: does the current plugin handle spine docs in a subfolder (via the CLAUDE.md path block), or does `/setup` case 4 move them to project root?
- Is one planning-and-build cycle enough, or should we attempt two to test the full loop (build → test notes → next planning)?

## Risks / dependencies

- Two sessions writing to Taskflowapp simultaneously (this session for prep, parallel session for E2E) could cause file conflicts. Mitigation: complete all prep work before the parallel session starts.
- Plugin version at install time must be current (V50 / 0.50.0). If the local marketplace install is stale, the E2E test won't exercise the right code.
- The parallel session is user-driven — test quality depends on which Taskflow batches the user chooses to build and how thoroughly the plugin's behaviour is observed.
