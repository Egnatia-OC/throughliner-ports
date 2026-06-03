# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Test-aware planning**

Build:
- Add test execution context to plan.md: reference next.md's rules for what Claude can verify itself (code traces) vs what needs a live user session, so the planner splits test entries correctly at planning time
- Add planning rule to plan.md: user-run E2E tests get their own batch, not appended to build batches

**Remove test generation from /done**

Build:
- Remove the test generation step from /done (step 1.2). All testing is planned work — it belongs in batches via /plan, not generated ad hoc during close-out.

**Capture wording approval**

Build:
- Add rule to all skill procedure docs (next.md, done.md, plan.md): when capturing something the user raises, show the proposed wording and wait for approval before writing it to QUEUE.md

**Restore web-search-when-uncertain rule**

Build:
- Add rule to all skill procedure docs (setup.md, plan.md, next.md, done.md): when Claude is uncertain about how something works, whether a better approach exists, or needs more information to answer confidently, offer to do a web search. File all research under resources/research/ for later reference.

**Interview flow replaces "question first" disposition**

Build:
- Rewrite plan.md's capture processing loop: remove "question first" as a disposition. After presenting and discussing a capture, Claude interviews the user with follow-up questions it identifies, then asks if there's anything else to add. Only then recommend promote, park, or drop (three dispositions instead of four).
- Add in-session capture rule to plan.md: captures created during a /plan session go to the bottom of the list and get processed in order when their turn comes. No special announcement or permission check when reaching them.

### Parked

- [idea] Sizing gates rework — research filed at resources/research/batch-sizing-research.md. Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

- [idea] Pre-push consistency sweep should use direct reads, not agents — the sweep is a checklist of file reads and string comparisons. An agent adds ~60k tokens of overhead for work that takes a handful of Grep and Read calls inline. Not justified for users watching their usage.
- [idea] /done lost context on what Captures is — after completing the /done turn, Claude tried to route a new observation to memory instead of Captures in QUEUE.md. The routing rules were available in context but Claude didn't follow them. May need a reminder in the close-out or handoff step that new observations always go to Captures.
- [idea] next.md Step 1 (active build check) needs explicit output guidance for the clean-slate case. When no _build.md exists, Claude currently narrates "No active build" which reads like a failure. Add direction so Claude communicates readiness, not absence.


### Parked

- [idea] Batch cohesion ordering heuristic — the build log as decision log creates pressure for discrete builds, and batch ceremony is friction for users. Two parts: (1) queue ordering rule — builds touching an area with no related batches yet should sink (absent urgency or dependency), giving time for more captures to accumulate and make the batch worthwhile; (2) /next-time check — if related captures exist for the top batch, Claude should recommend switching to /plan to incorporate them first. Batching also touches context window management, not just coherent logging — Claude needs to think about one area of related concerns at a time. Needs design work to sharpen "no friends" and "related" into mechanical rules.
- [idea] Cruise control skill — a skill that runs build→commit→build→commit through a batch (or multiple batches) unattended, stopping only when it hits something requiring user input. Key design concerns: (1) wording that doesn't pressure Claude to push through uncertainty, (2) dependency management when Claude decides when to wrap a batch, (3) /done judgment steps can't get skipped for speed. Parked: depends on stabilizing the skills it would chain.
- [idea] Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
- [idea] /done spec check — after writing the **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. Retrospective check (at decision time) vs the current /plan pipeline gate (prospective, at planning time). Both mechanisms need more real usage before deciding how they relate.
- [idea] Pre-push sweep could be lighter if /done flagged host-side impacts at build time — accumulate a manifest of "this change affects X in project docs" during /done while context is fresh, then the push sweep checks flagged spots instead of re-reading everything. Sweep stays as safety net but gets cheaper. Design question: cross-build staleness (build 3 invalidates something build 1 touched) still needs the sweep to catch it.
