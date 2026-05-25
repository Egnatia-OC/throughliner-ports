# 0073 — Stop hook before-build→build auto-chain fix

## Goal

Fix the Stop hook so it doesn't auto-chain from before-build into build. Currently `stop.py:322-324` redirects whenever unticked files exist in the top batch, but it doesn't distinguish "just locked by before-build" from "mid-build, continue building."

## Inputs

- `plugin/hooks/stop.py` — current Stop hook code (lines 322-324 are the key location).
- `research/e2e-round-2-observations.md` finding #2 — Stop hook auto-chains before-build→build.

## Outputs

- Edited `stop.py` with fix: check whether any files are already ticked. Zero ticked = just locked by before-build (exit silent). Some ticked = mid-build (redirect to continue).
- Tests in `tests/` covering the new logic.
- TEST-LOG rows.

## Success criteria

- After before-build completes, the Stop hook does not auto-redirect to batch-executor.
- Mid-build (some files ticked, some not), the Stop hook still redirects correctly.
- Existing Stop hook tests pass.

## Open questions for this session

- None. The fix is well-defined from E2E observation.

## Risks / dependencies

- Edge case: what if a batch has zero files (Goal-only batch)? Current architecture doesn't support this, so not a risk.
