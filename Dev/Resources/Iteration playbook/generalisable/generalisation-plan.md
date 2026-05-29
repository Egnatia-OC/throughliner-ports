# Generalisation plan

Three Iteration Playbook entries whose shapes are portable beyond method development. Each is copied here from the parent folder as a starting point. The originals remain in the playbook; these copies are the working drafts for generalisation.

The goal: turn each into something Alex can use across any project — Taskflow, future apps, method dev itself. The generalised version may become a plugin skill, a standalone prompt, or a convention baked into existing procedure docs. That decision is per-entry.


## 1. Premise check

**Current shape.** Reconcile a queued prompt (written in a prior session) against current method state before executing it. Two-column reconciliation: what the prompt assumes vs what's actually true now.

**What generalises.** The core pattern: before executing any deferred task, verify its assumptions still hold. Applies to BACKLOG batches, parked items, open questions with stale context, or any plan written more than a few sessions ago.

**Generalised form.** Input: a task description or plan entry from BACKLOG (or any deferred-work artifact). Process: read the task's stated assumptions and prerequisites, read the current project state, produce a two-column reconciliation (assumed vs actual), classify each assumption as still-valid / partially-valid / invalidated. Output: a verdict — execute as-is, execute with adjustments (stated), or re-scope.

**Possible homes.**
- A plugin skill (`/sovpremisecheck` or baked into `/sovplan` as a sub-step when unparking a batch).
- A standalone prompt Alex can paste into any session before starting deferred work.
- A convention in session-protocol.md: "before executing any queued or parked item older than N sessions, run a premise check."

**Open questions.**
- Should it be automatic (triggered when unparking) or manual (invoked by Alex)?
- How lightweight can it be? The method-dev version reads every file in the current version folder. A project-level version needs a smaller, targeted read scope — probably just the files the task would touch.


## 2. Reader test

**Current shape.** Spawn three sub-agents in parallel, each reading method docs fresh as a stranger. Three scenarios: comprehension Q&A, new-project role-play, mid-project curveball. Produces a ranked gap list (top/middle/bottom tier), not edits.

**What generalises.** The stranger-perspective stress test pattern. Works for any documentation a Claude session needs to follow correctly — UX.md, BACKLOG.md, CLAUDE.md, procedure docs, onboarding docs.

**Generalised form.** Input: which docs to test + what the docs are for (their job). Process: spawn sub-agents who read the docs cold with no project context. Each runs a scenario that exercises the docs' purpose — e.g. "you're a new Claude session opening this project for the first time; what do you do?" Output: a ranked gap list. The scenarios rotate based on what the docs do.

**Possible homes.**
- A plugin skill (`/sovreadertest`) that tests the consumer project's spine docs.
- A standalone prompt template with blanks for which docs and which scenarios.
- A dev-side convention: run a reader test before any major doc restructure ships.

**Open questions.**
- The method-dev version has specific scenarios (comprehension Q&A, new-project, mid-project curveball). A generalised version needs scenario templates that flex to different doc types. What are the universal scenario shapes?
- Sub-agent cost. Three sub-agents is expensive. Is one sub-agent with three sequential scenarios good enough, or does the parallel-stranger framing (each reads independently) matter for quality?
- The "save the gap list as a file" refinement is even more important in a general-use version — project-level reader test findings need to persist.


## 3. Rule and procedure extraction

**Current shape.** End-of-session harvest. Two prompts asked separately: (1) "anything from this session worth capturing as a standing rule?" and (2) "describe this whole thing as a procedure I could run again." Each produces a short ranked list with confidence labels, recommended homes, and clarification-vs-new flags.

**What generalises.** The reflective harvest pattern. Any session that involved iterative problem-solving, surprising corrections, or repeated patterns has extractable standing rules. The procedure-extraction variant captures any recognisable shape worth naming.

**Generalised form.** Input: a completed session with substantive work (not a one-shot lookup). Process: scan the session for patterns — corrections, surprises, repeated moves, things that worked unusually well, things that got stuck. Distinguish individual rules (small judgment calls with triggers) from procedural shapes (named multi-step workflows). For each candidate, state: the rule/shape, its trigger, where it should live, and whether it's a clarification of existing convention or genuinely new. Output: 2-4 strong candidates with rejections. Cap enforced.

**Possible homes.**
- Baked into `/sovclose` as an optional step: "before closing, check if anything from today's work is worth capturing."
- A standalone skill (`/harvest` or `/extract`) invocable at any point, not just close.
- A convention in session-protocol.md: "at close, offer one rule-extraction prompt and one procedure-extraction prompt if the session was substantive."

**Open questions.**
- Where do extracted rules go in a consumer project? The method-dev version has clear homes (CLAUDE.md, playbook, memory). A consumer project has fewer destinations — probably CLAUDE.md or a project-specific conventions file.
- Should the procedure-extraction variant use the playbook entry format (trigger/steps/output/when-wasted/refinements)? That structure is good but heavy for a consumer project. A lighter format might be better: name, when to use, what to do, what comes out.
- The "hold the cap" refinement (2-4 strong candidates) is load-bearing. Without it, the harvest inflates into a list of every small judgment call. The cap needs to ship with the generalised version.


## Next steps

1. Decide per-entry: skill, standalone prompt, or baked-in convention.
2. For any that become skills: draft the skill body, test in a consumer project (Taskflow).
3. For any that become conventions: draft the prose, place it in the right doc, test through a real session.
4. The method-dev originals in the parent folder stay as-is — they're the specialised versions. The generalised versions live here until they ship, then move to their permanent homes.
