# 0078 — Post-fix E2E validation (Taskflow)

## Goal

Re-run a build cycle against Taskflow after 0072–0074 ship, confirming the critical fixes work in a real session: after-build stays out of source code, Stop hook doesn't auto-chain from before-build, and session-open status summary appears.

## Inputs

- `research/e2e-round-2-observations.md` — the findings being validated.
- Taskflowapp at `C:\Users\Alex\Desktop\Taskflow Planning\Planning in here\Taskflowapp`.
- Shipped versions of 0072 (after-build boundary), 0073 (stop-hook fix), 0074 (status summary).
- 0071 (subagent cost optimization) — verify Sonnet quality and cold-start gate.

## Outputs

- E2E test notes: pass/fail on each targeted fix, any new regressions.
- Research file: `research/e2e-post-fix-validation.md`.
- Updated OPEN-QUESTIONS or new scope files if regressions found.
- If all five v71 priority actions pass: close out `research/e2e-round-2-observations.md` with a "validated" footer.

## Success criteria

- After-build does NOT attempt to edit source/gradle files when a build error exists. It surfaces the failure in the recap instead.
- After before-build completes, the Stop hook exits silently (no auto-redirect to batch-executor).
- On session open, the user sees batch count, next batch, and a proceed prompt.
- No new critical regressions introduced by the fixes.
- If 0071 shipped: planning token cost measurably lower than the 31.6k baseline. Sonnet handles push-back, duplicate detection, and Suggestion/Discovery classification without quality regression. Cold-start gate fires correctly on Taskflow (which has prior builds — gate should NOT skip drift checks).

## Open questions for this session

- Which Taskflow batch to test? Batch 0001 was used in 0068 — use the next untested batch to avoid repeating the same code paths.
- Should we intentionally trigger a build failure to validate the after-build boundary? (e.g. introduce a deliberate syntax error pre-build.)

## Risks / dependencies

- **Hard dependency on 0072, 0073, 0074 all being shipped.** Do not run until all three land.
- Taskflow state may have drifted since v71 — check BACKLOG status and batch availability at session open.
