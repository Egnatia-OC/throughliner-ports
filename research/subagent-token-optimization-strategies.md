# Subagent token optimization strategies — 2026-05-25

Source: Gemini research compilation (multi-site synthesis), plus web-verified findings. Filed for reference during 0071 (subagent cost optimization) and any future subagent work.

## Key facts about subagent token costs

- Subagents use 4–7x more tokens than single-agent sessions; up to 15x with complex parallel fan-out.
- Every spawn pays ~16k+ tokens for context bootstrapping (system prompt, file structures, tool definitions).
- Parent summaries from subagent returns balloon the main context on every subsequent prompt.
- Never use a subagent for minor single-step actions — 8,000+ tokens of initialization for a task the parent could do for 200.

## When subagents actually save money

- **Preventing main-chat bloat:** Isolating heavy test logs or code searches means you pay for those tokens once, not on every subsequent reply.
- **Prompt caching:** Repeat reads of the same codebase hit cached data at 10% of standard token prices.

## Five optimization strategies

### 1. Chain of Draft constraints

Force internal reasoning into dense shorthand. Directive: "Limit total internal reasoning to under 40 words using shorthand notation, technical symbols, and bullet points only."

Savings: 20–80%. Best for heavy multi-file code analysis.

### 2. Explicit low-effort directives

For deterministic tasks (regex, file structure, JSON parsing), bypass heavy reasoning. Directive: "This task requires simple pattern matching, not complex multi-step logical deduction. If you find yourself thinking for more than one step, stop."

Savings: 30–50%. Best for routine refactoring, formatting, linting.

### 3. Strip tool definitions

Every tool description costs hundreds of tokens on every message loop. Create ultra-narrow single-purpose agents — if an agent only searches code, strip file-writing permissions entirely.

Savings: 15–40%. Best for read-only search bots and specific API callers.

### 4. Enforce strict output formats

Ban conversational filler in subagent returns. Demand structured outputs (XML tags or similar) containing only raw data.

Savings: 10–30%. Best for deep subagents communicating back to the parent.

### 5. Strategic prefills to short-circuit inner monologues

Prefill the assistant's response opening to signal immediate execution, bypassing planning phases.

Savings: variable. Best when you know exactly what output shape to expect.

## Model selection via frontmatter

Custom agent definitions support a `model:` field in YAML frontmatter. Values: `opus`, `sonnet`, `haiku`. Sonnet is the default if omitted. Confirmed via [Claude Code subagents docs](https://code.claude.com/docs/en/sub-agents) and multiple third-party guides (2026-05-25).

Example: `model: sonnet` routes the agent to Sonnet — ~40% cheaper than Opus with minimal quality loss on structured planning tasks.

## CLAUDE.md loading control

Not all subagents load CLAUDE.md. Built-in Explore and Plan agents skip it entirely (hardcoded). Custom agents can opt out via frontmatter:

```yaml
---
name: "ultra-lean-regex-searcher"
description: "Finds literal text patterns in the directory"
loadProjectInstructions: false
---
```

Setting `loadProjectInstructions: false` cuts off CLAUDE.md injection, saving thousands of bootstrapping tokens per invocation.

**Nested architecture.** Claude Code supports directory-based CLAUDE.md. A subagent working inside a subdirectory (e.g. `tests/`) ignores the root CLAUDE.md and only loads `tests/CLAUDE.md` if it exists. Shifting task-specific rules into local subdirectory files limits what each subagent reads.

## Applicability to this project's plugin subagents

The plugin's five subagents (planning, before-build, batch-executor, after-build, setup) are invoked via Claude Code's agent system — we control their system prompts (the `.md` bodies in `plugin/agents/`) but NOT the tool definitions they receive (Claude Code injects those) and NOT prefills (not exposed in the agent API).

What we CAN apply:
- Strategy 1 (Chain of Draft): add reasoning-constraint directives to agent bodies.
- Strategy 2 (Low effort): add explicit "don't over-think" signals for routine operations (e.g. planning subagent's drift checks on empty state).
- Strategy 3 (Tool stripping): partially — agent definitions can specify which tools are available, limiting the tool-definition payload.
- Strategy 4 (Output format): enforce terse structured returns in agent bodies.

What we CAN investigate:
- `loadProjectInstructions: false`: our subagents currently need CLAUDE.md for the path block (doc locations). If path discovery moved to a different mechanism, this could cut CLAUDE.md injection entirely. Worth evaluating per-subagent — some may not need it.

What we CANNOT apply (Claude Code agent SDK limitation):
- Strategy 5 (Prefills): no mechanism to prefill agent responses.
- Direct control over context bootstrapping size — that's Claude Code infrastructure.
