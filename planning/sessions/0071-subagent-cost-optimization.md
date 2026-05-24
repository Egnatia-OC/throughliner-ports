# 0071 — Subagent cost optimization

## Goal

Reduce planning subagent token cost from ~31.6k to under 15k for common cases (feature routing, duplicate detection, cold-start projects). The planning subagent's quality is good — push-back, duplicate detection, and BACKLOG routing all work correctly — but the cost is too high for what amounts to a lookup-and-respond operation.

## Inputs

- `research/subagent-token-costs.md` — techniques and actionable items from 2026-05-24 research
- `plugin/agents/planning.md` — current planning subagent body
- 0068 E2E observations: 31.6k tokens / 1m58s for a feature-request routing; 31.6k for a push-back response

## Outputs

- Conditional drift-check skip: bypass all five drift checks when TEST-LOG is empty and no build-log entries exist (cold-start project)
- Classify-then-dispatch: lightweight triage before loading the full planning protocol (extend 0063's classify-before-loading to cover drift checks)
- Evaluate Sonnet as planning subagent model: test whether quality holds for routing, duplicate detection, and BACKLOG edits

## Success criteria

- Planning subagent feature-request routing costs under 15k tokens on a project with no prior builds
- No quality regression: push-back, duplicate detection, and correct Suggestion/Discovery classification still work
- Drift checks still run when there's history to check against

## Risks / dependencies

- Model selection may require changes to subagent definition format — check whether `model:` is a supported frontmatter field in agent `.md` files
- Token measurement is impractical unless the desktop app surfaces it (0060 finding #8) — may need to rely on the token count shown in the UI
