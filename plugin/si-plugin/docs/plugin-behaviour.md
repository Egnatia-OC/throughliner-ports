# Sovereign Implementer — behaviour rules

Active in every session where the plugin is installed and the project is set up.

## Communication

- Plain language. No jargon unless the user used it first.
- Push back rather than agreeing. If an approach is wrong, say so.
- State regressions plainly — don't hide failures or apologise around them.
- Run commands yourself. Don't ask the user to run things you can run.
- When uncertain about an external fact, offer a web search rather than guessing. File research under `resources/research/`.
- When capturing something mid-skill, always ask "anything else?" before resuming.
- Sequencing multi-part responses: when the user's next action depends on the prior one, give one item per message. State the count upfront, then stop — don't preview the upcoming items, even briefly. The pull to bundle is strongest at close-outs and walkthroughs (commit instructions, smoke-test plans, audit checklists); resist it there especially. The one inversion is alternatives the user is choosing between — comparisons need everything visible at once because the choice is between them.

## Response-shape tags

Procedure docs use these tags to control verbosity and interaction per step. Tags compose freely.

- **[SILENT]** — Do the work, don't narrate it.
- **[BRIEF]** — One or two sentences max. Structured content (lists, option sets) doesn't count against the limit.
- **[DISCUSS]** — Engage substantively. Tradeoffs, concerns, recommendation.
- **[PROMPT]** — Stop and wait for user input. Never skip.
- **[SEQUENCE]** — One item at a time. Present, wait, then next. Don't preview upcoming items.

### Unlabelled steps

Brief acknowledgment if the user needs to know the step happened; no output if purely internal.

### Tag precedence

- Step-level tags override phase-level tags.
- During skill execution, procedure tags govern. User communication preferences (from CLAUDE.md) apply to unlabelled steps and conversation outside skills.

## Tool use

- For bounded checklists — a known set of files to read, fields to compare, or strings to grep — use direct tool calls (Read, Grep, Glob). Don't spawn agents.
- Agents are for open-ended exploration where the shape of the answer isn't known in advance. If you can write out the lookups before doing them, do them inline.

## Captures

- Draft capture wording and show it before writing to QUEUE.md. Include the reasoning, not just what was noticed.
- Captures append to the bottom of the Captures section.
- Don't promote captures to batches outside /plan — route to Captures and defer.
- Mid-session captures follow the same rules. No special priority.

## Why-pipeline

Rationale is prose. Carry it forward; don't collapse it into a structured "why" field.

**Preserve.** A reason originates in a capture and travels capture → batch → log as prose. At each stage Claude re-authors the prose to fit context and shows the wording to the user for approval before writing. The reasons live inline in the entry text — there is no dedicated why-field at any stage.

**Retrieve.** When asked why something exists or why a decision was made, search `LOG/log.md` and `LOG/log-v*.md` first. Only fall back to inferring from code if the log has nothing relevant.

## Scope discipline

- Route to artifacts, not memory. If it belongs in SPEC.md, QUEUE.md, REGISTRY.md, or LOG/, write it there.
- Doc routing: SPEC.md = what/who/how/why the product exists. QUEUE.md = what to work on next. REGISTRY.md = what components exist. LOG/ = what happened.
- /plan is for planning, /next is for building. Don't cross them.
- New features need a spec entry before a build entry. Pipeline: idea → question (if unclear) → SPEC.md → QUEUE.md. Threshold: if a user would see or experience the difference, update SPEC.md first.
- Don't fix things outside current scope. Note them for the queue.
- Nothing unrouted survives a session. File or drop before close.
- SPEC.md is read-only during builds. Note spec issues for /plan.
- One build at a time. Never start /next while _build.md exists.
- Empty Batches is normal — planned work is done. Run /plan to add more.

## Dependency ownership

- Claude owns sequencing — ordering, dependencies, what happens first. Don't defer to the user.
- The user owns scope — what enters the queue, what gets parked/dropped, whether to proceed. Don't proceed past a disposition choice without their say.

## File safety

- Never `git add -A` or `git add .` — stage explicitly.
- Never `git push` without asking. Never `--force`.
- Never `git reset --hard`.
- Check for secrets before committing.

## Prior decisions

- Before raising a design question, follow the Why-pipeline retrieve rule. If LOG shows it's already decided, state the prior decision. If the user revisits, flag when it was decided.
- When asked "why does the app do X?", follow the Why-pipeline retrieve rule.

## Context awareness

- If context is long mid-build, suggest completing the current file and running /done.
- When resuming (active _build.md), read it for state rather than re-exploring.
