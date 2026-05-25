# 0077 — Greenfield E2E: burner app from scratch

## Goal

Test the most important untested path: "I have an idea for an app" → `/setup` → planning subagent creates batches → before-build → build → after-build. Uses a throwaway app (Polite Fart Announcer or similar) so the user genuinely doesn't know what the batches should look like — forcing the planning subagent to do real work, not just validate existing structure.

## Inputs

- `research/e2e-round-2-observations.md` finding #8 — planning-from-scratch never tested.
- `plugin/agents/planning.md` — planning subagent body.
- `plugin/agents/before-build.md`, `plugin/agents/batch-executor.md`, `plugin/agents/after-build.md`.
- `plugin/hooks/session_start.py` — session open behaviour.
- Whatever plugin version is current when this runs (ideally after 0071–0074 fixes).

## Outputs

- E2E test notes: planning quality, batch structure, token costs, friction points.
- Research file: `research/e2e-greenfield-observations.md`.
- New scope files or OPEN-QUESTIONS entries for any issues found.

## Success criteria

- Planning subagent creates sensible batches from a vague feature description without user hand-holding.
- At least one batch runs through before-build → build → after-build without critical failures.
- Token cost for planning-from-scratch is documented (baseline for future optimization).
- Any new findings are routed (scope file, OQ entry, or fold-in) before session close.

## Open questions for this session

- Which burner app? "Polite Fart Announcer" was mentioned in v71 — a silly Android/web app with obvious features to batch. Confirm with Alex at session open.
- Should this run against the full pipeline (including commit/tag) or stop after first successful after-build?
- Desktop app or CLI session for the test?

## Risks / dependencies

- Soft dependency on 0071–0074: the known stop-hook bug (0073) and missing status summary (0074) will fire during this test if not yet fixed. Acceptable — document as known issues and focus findings on planning quality. Hard dependency: none.
- The burner app needs to be simple enough that one planning session + one build cycle fits in a single context window.
