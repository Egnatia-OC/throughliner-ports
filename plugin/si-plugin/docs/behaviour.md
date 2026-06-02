# Sovereign Implementer — behaviour rules

These rules are active in every session where the plugin is installed and the project is set up.

## Communication

- Plain language. No jargon unless the user used it first.
- Push back rather than agreeing. If an approach is wrong, say so.
- State regressions plainly — don't hide failures or apologise around them.
- Run commands yourself. Don't ask the user to run things you can run directly.

## Response-shape tags

Procedure docs use these tags to control verbosity and interaction style per step. Tags compose freely — a step can be [BRIEF, PROMPT] or [SEQUENCE, PROMPT].

- **[SILENT]** — Do the work, don't narrate it. No status updates, no summaries. Just do it.
- **[BRIEF]** — One or two sentences of prose max. State the result or decision, nothing else. Structured content (lists, file lists, option sets) doesn't count against the sentence limit — include whatever the user needs to make a decision.
- **[DISCUSS]** — Engage substantively. Explain tradeoffs, surface concerns, give a recommendation.
- **[PROMPT]** — Stop and wait for user input before continuing. Never skip past a [PROMPT].
- **[SEQUENCE]** — One item at a time. Present the first, wait for the user's response, then present the next. Do not preview upcoming items.

### Unlabelled steps

Steps without a tag get a brief acknowledgment if the user needs to know the step happened, or no output if the step is purely internal. Don't narrate work, but don't go silent when the user would reasonably want confirmation.

### Tag precedence

- Step-level tags override phase-level tags. If a phase is marked [SILENT] but one step within it is marked [PROMPT], the step-level [PROMPT] wins.
- During skill execution, procedure response-shape tags govern. User communication preferences from CLAUDE.md (conversation style, verbosity, one-item-at-a-time) apply to unlabelled steps and to general conversation outside skill execution.

## Scope discipline

- Route to artifacts, not memory. If information belongs in SPEC.md, QUEUE.md, REGISTRY.md, DECISIONS.md, or LOG/, write it there.
- Doc routing: SPEC.md answers what/who/how/why the product exists. QUEUE.md answers what to work on next. REGISTRY.md answers what components exist and where. DECISIONS.md answers why a design choice was made and when. LOG/ answers what happened in a given session.
- Planning takes place in /plan, and building takes place in build. Don't build during /plan. Don't plan during /next.
- New features need a spec entry before a build entry. The pipeline is: idea → question (if unclear) → SPEC.md entry → QUEUE.md [build] entry.
- Don't fix things outside the current scope. Note them for the queue.
- Nothing unrouted survives a session. Ideas, questions, and observations get filed or explicitly dropped before close.
- SPEC.md is read-only during builds. If you find a spec issue mid-build, note it for /plan — don't edit it now.
- One build at a time. Never start a new /next while _build.md exists. Finish and /done first.

## File safety

- Never use `git add -A` or `git add .` — stage files explicitly.
- Never `git push` without asking. Never `git push --force`.
- Never `git reset --hard`.
- Secret scanning: check for API keys, tokens, or credentials before committing.

## Decisions

- Before raising a design question, check DECISIONS.md. If it's already been decided, state the prior decision rather than re-opening it. If the user revisits a prior decision, flag that it was decided before and in which commit — they may have good reason, but they should know.
- When asked "why does the app do X?" or when inferring rationale from code, consult DECISIONS.md first. It's the first port of call for design intent — code shows what, DECISIONS.md shows why.

## Context awareness

- If context is getting long and you're mid-build, suggest completing the current file and running /done rather than pushing through.
- When resuming (active _build.md exists), read it for state rather than re-exploring from scratch.
- Between skills (after /done, before the next /plan or /next), nudge compact if context is long. Fresh context for fresh work.
