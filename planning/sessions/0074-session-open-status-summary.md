# 0074 — Session-open status summary

## Goal

When a session opens in a consumer project, give the user a visible rundown of project state: how many batches exist, which is next, what it involves, and ask if they'd like to proceed. Currently SessionStart injects context for Claude but nothing user-facing.

## Inputs

- `plugin/hooks/session_start.py` — current SessionStart hook (tier 3 state summary).
- `plugin/agents/planning.md` — planning subagent (current auto-route target).
- `research/e2e-round-2-observations.md` finding #5 — no session-open status summary for users.

## Outputs

- Edited `session_start.py` tier 3 state summary to include a user-facing status block in `additionalContext` that Claude will surface.
- Or: edited `universal-behaviour.md` with a "present project status on session open" rule.
- TEST-LOG rows.

## Success criteria

- On session open, the user sees: batch count, next batch name/number, what that batch involves (goal + file count), and a prompt asking if they'd like to proceed.
- The summary is concise — no more than 5-6 lines.

## Open questions for this session

- Should this be a hook-injected block (deterministic) or a prose rule (probabilistic)? Hook-injected is more reliable but harder to format attractively. Prose rule is simpler but Claude might skip it.
- Should the summary include parked/shipped batch counts, or just queued?

## Risks / dependencies

- Depends on 0069's Status: field being in place (shipped v70 — already done).
