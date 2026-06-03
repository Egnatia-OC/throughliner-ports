# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Skill handoff polish**
- [build] Audit all skill-to-skill handoff prompts across /setup, /plan, /next, and /done — for each, simulate the prompt text and summarise the immediate context the user is in when they see it, then polish for clarity and flow
- [build] Fix /done handoff ordering — push question first, then "run /next or /plan when ready" if not pushing
- [build] Fix /next batch presentation prompt — replace "Ready to start? (yes / adjust scope)" with a simple "Ready?" and route to /plan if the user wants changes

**Batch entry format: replace inline type tags with subheadings**
Why: Type tags ([build], [test]) are Claude's routing metadata visible to the user, cluttering batch presentation with implementation details.
- [build] Replace inline [build]/[test] type markers with Build/Test subheadings in the batch format — update plan.md Step 3, and all procedure docs that reference entry types by inline tag (next.md, done.md, setup.md, behaviour.md)
- [build] Update templates (CLAUDE-TEMPLATE.md, faq-template.md, faq-index-template.md) to reflect the new format
- [build] Reformat existing QUEUE.md batches to use the new subheading format

**Mid-build scope expansion protocol**
- [build] Add mid-build capture routing to /next procedure — when user raises something out of scope, default to capturing it and ask "anything else?" before resuming
- [build] Add "anything else?" loop to all skills after any capture moment — currently the user has to interrupt to share a second thought
- [build] Add "add to scope" workaround as an explicit last-resort option, framed as out-of-procedure behaviour requiring user confirmation

**Post-update migration detection**
- [build] Add .si-version dotfile to /setup scaffolding, written with the current plugin version
- [build] Add version mismatch detection to session_start — compare .si-version against plugin version, warn user to run /setup if mismatched
- [build] Update /setup to handle existing docs (re-scaffold without overwriting user content)
- [test] E2E: run /setup in a project that already has docs from an older plugin version — verify it handles existing files without corrupting or silently dropping content

### Parked

- [idea] Sizing gates rework — research filed at resources/research/batch-sizing-research.md. Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.




### Parked

- [idea] Batch cohesion ordering heuristic — the build log as decision log creates pressure for discrete builds, and batch ceremony is friction for users. Two parts: (1) queue ordering rule — builds touching an area with no related batches yet should sink (absent urgency or dependency), giving time for more captures to accumulate and make the batch worthwhile; (2) /next-time check — if related captures exist for the top batch, Claude should recommend switching to /plan to incorporate them first. Batching also touches context window management, not just coherent logging — Claude needs to think about one area of related concerns at a time. Needs design work to sharpen "no friends" and "related" into mechanical rules.
- [idea] Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
- [idea] /done spec check — after writing the **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. Retrospective check (at decision time) vs the current /plan pipeline gate (prospective, at planning time). Both mechanisms need more real usage before deciding how they relate.
- [idea] Pre-push sweep could be lighter if /done flagged host-side impacts at build time — accumulate a manifest of "this change affects X in project docs" during /done while context is fresh, then the push sweep checks flagged spots instead of re-reading everything. Sweep stays as safety net but gets cheaper. Design question: cross-build staleness (build 3 invalidates something build 1 touched) still needs the sweep to catch it.
