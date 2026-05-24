# 0068 — Taskflow E2E round 2

## Goal

Full build cycle (planning → before-build → build → after-build) against Taskflow with 0063–0067 fixes in place. Tests the two untested subagents (batch-executor, after-build) and confirms efficiency/boundary fixes landed.

## Inputs

- 0060 findings (baseline)
- Fixes from 0063–0067
- Taskflow batch 0001 with real scope-context content (must be filled beforehand)

## Outputs

- E2E notes for batch-executor and after-build
- Regression check on setup, planning, before-build
- Token cost and permission prompt observations

## Success criteria

- At least one full build cycle completes
- Planning token cost materially lower than 0060's ~75k (0063 fix)
- Permission prompts reduced or documented as unfixable (0066)

## Prep required

- Fill Taskflow batch 0001 in a dedicated planning session. Without this, before-build gates again.

## Risks / dependencies

- Depends on 0063, 0064, 0065. 0066/0067 nice-to-have.
- Token cost observation impractical unless desktop app improves (0060 finding #8).
