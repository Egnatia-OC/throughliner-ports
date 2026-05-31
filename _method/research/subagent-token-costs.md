# Subagent token cost reduction — research

*2026-05-24*

## Question

The planning subagent costs 31.6k tokens for a single feature-request routing. What techniques reduce subagent costs in Claude Code plugins?

## Findings

### Model selection

Subagent definitions can specify a lighter model. Sonnet is ~40% cheaper than Opus with minimal quality loss on planning/research tasks. Haiku is too error-prone for judgment-heavy work (compounding mistakes). This is the simplest lever.

### Conditional doc loading

The planning subagent reads UX.md, BACKLOG (all batches), MANIFEST, DOC-STRUCTURE, VOCABULARY, and universal-behaviour on every invocation — then runs five drift checks. On a cold start (no previous builds, empty TEST-LOG), drift checks find nothing. Conditionally skipping drift checks when there's nothing to drift against could halve the planning cost.

### Scoped vs full protocol

"Route this feature request" and "run the full planning protocol with drift checks, test-session close, and idea sorting" are very different workloads. A classify-then-dispatch pattern — lightweight triage first, full protocol only when needed — could prevent the planning subagent from doing unnecessary work.

### CLAUDE.md size

CLAUDE.md injects into every request. A 5,000-token CLAUDE.md is a 5,000-token tax on every turn. Taskflow's is moderate, but the plugin's SessionStart hook also injects behavioral rules via additionalContext, adding to the per-turn cost.

### Reported savings

- 40–70% on focused tasks with tight scoping
- 30–50% from clearing between tasks
- Model downgrade alone: ~40%

## Actionable for sovereign-implementer

1. **Skip drift checks on cold start.** If TEST-LOG is empty and no build-log entries exist, skip all five drift checks.
2. **Consider Sonnet for planning subagent.** Quality appeared sufficient for routing and BACKLOG edits in E2E testing.
3. **Classify-then-dispatch.** Lightweight triage before loading the full planning protocol. Already partially implemented (0063's "classify before loading") but drift checks still run unconditionally.
4. **Measure per-phase cost.** Instrument which planning subagent phases (doc loading, drift checks, idea sorting, BACKLOG editing) consume the most tokens to target optimization.

## Sources

- [Claude Code Token Optimization (Build to Launch)](https://buildtolaunch.substack.com/p/claude-code-token-optimization)
- [Manage costs effectively — Claude Code Docs](https://code.claude.com/docs/en/costs)
- [7 Practical Ways to Reduce Claude Code Token Usage (KDnuggets)](https://www.kdnuggets.com/7-practical-ways-to-reduce-claude-code-token-usage)
- [Reduce Claude Code Costs 60% (systemprompt.io)](https://systemprompt.io/guides/claude-code-cost-optimisation)
- [Cut Claude Code Costs 70% (Branch8)](https://branch8.com/posts/claude-code-token-limits-cost-optimization-apac-teams)
