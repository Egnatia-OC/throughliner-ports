# 0084 — Greenfield E2E: post-redesign full cycle

## Goal

Test the complete method lifecycle from scratch in the post-0079 (no subagents) and post-0080 (phase-aware permissions) architecture. A throwaway app goes through `/setup` → planning conversation → `/before-build` → `/build` → testing → commit. First E2E of the procedure-doc-driven architecture, and first-ever test of the greenfield path (new user, new app, no existing structure).

## Inputs

- Prior E2E research: `research/e2e-round-2-observations.md`.
- 0079 outputs: procedure docs at `plugin/docs/`, rewritten hooks and skills.
- 0080 outputs: phase-aware PreToolUse, updated DOC-STRUCTURE and universal-behaviour.
- Current plugin packaging: `marketplace.json`.

## Outputs

- Research file: `research/e2e-greenfield-post-redesign.md` — planning quality, permission behaviour, token costs, friction points.
- New scope files or OPEN-QUESTIONS entries for any issues found.

## Success criteria

1. `/setup` scaffolds a new project correctly (case 1: empty folder).
2. Planning conversation creates sensible batches from a vague feature description — main Claude reads procedure docs directly, no subagent indirection.
3. Phase-aware permissions work correctly: docs editable during planning, source code locked; reversed during build.
4. `/before-build` locks the batch file list without errors.
5. `/build` completes at least one batch without critical failures.
6. After-build recap, MANIFEST update, and test-confirmation gate all fire from procedure docs.
7. Session-open status summary (0074) shows correct state.
8. Token cost for the full cycle is documented as the procedure-doc architecture baseline.

## Open questions for this session

1. Which burner app? Something trivially simple with 2–3 obvious features to batch. Confirm at session open.
2. Should the test run the full pipeline including commit/tag, or stop after first successful after-build?
3. Single session or split across two (planning in one, build in another) to test session-resume?

## Risks / dependencies

- **Hard dependency on 0080.** Phase-aware permissions are central to the post-0079 editing model. Testing without them means testing incomplete state.
- **Soft dependency on procedure-doc quality.** If 0079's procedure docs are unclear, planning will drift — but that's a finding, not a blocker.
- The burner app must be simple enough that planning + one build cycle fits in a single context window.
- Plugin must be installable via local marketplace (marketplace.json current after 0079).
