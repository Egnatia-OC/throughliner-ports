# 0063 — Subagent efficiency pass

## Goal

Reduce token cost and execution time across all five subagents by enforcing doc-first ordering, deferring doc reads until after classification, and replacing inner agent spawns with direct reads. The E2E test (0060) showed setup costing ~163k tokens and planning costing ~75k+ for a single scope-existence check — patterns likely to repeat in batch-executor and after-build.

## Inputs

- E2E findings 1 and 7 from `planning/sessions/0060-taskflow-e2e-prep-and-testing.md`
- All five subagent bodies: `plugin/agents/planning.md`, `plugin/agents/before-build.md`, `plugin/agents/batch-executor.md`, `plugin/agents/after-build.md`, `plugin/agents/setup.md`

## Outputs

- All five subagent bodies updated with:
  - Classify/triage step before any doc loading (setup: detect case before reading DOC-STRUCTURE/VOCABULARY; planning: check scope existence in UX.md/BACKLOG before exploring code)
  - Explicit "do not spawn inner agents for work that can be a direct Read or Grep" instruction
  - Doc-first ordering where applicable (planning: check docs before codebase; batch-executor: read Files list and Inputs resources, nothing else)
- Audit log of inner agent spawns found and removed/replaced (in the scope file or build-log entry)

## Success criteria

- Setup case detection uses fewer than 15k tokens (down from 37.9k)
- Planning scope-existence check completes without spawning a code-exploration agent
- No subagent body contains instructions that would cause front-loaded reads of docs irrelevant to the current classification path

## Risks / dependencies

- Token cost targets are estimates — actual reduction depends on how Claude interprets the instructions. May need iteration.
- The batch-executor and after-build subagents haven't been E2E tested yet, so the audit is based on reading the bodies rather than observed behaviour.
