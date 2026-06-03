# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Post-update migration detection**

Build:
- Add .si-version dotfile to /setup scaffolding, written with the current plugin version
- Add version mismatch detection to session_start — compare .si-version against plugin version, warn user to run /setup if mismatched
- Update /setup to handle existing docs (re-scaffold without overwriting user content)

Test:
- E2E: run /setup in a project that already has docs from an older plugin version — verify it handles existing files without corrupting or silently dropping content

### Parked

- [idea] Sizing gates rework — research filed at resources/research/batch-sizing-research.md. Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

- [idea] README needs operating conditions section — document the normal runtime assumptions: Opus 4.6 on high, tested in auto mode only, /compact between commits, /clear or new chat between pushes, run /setup on first use. Users need to know these to get the expected experience.
- [idea] Cruise control skill — a skill that runs build→commit→build→commit through a batch (or multiple batches) unattended, stopping only when it hits something requiring user input. Motivated by sessions where the user is just pressing yes through entire builds. Key design concerns: (1) wording must not create pressure for Claude to push through — it needs to stop genuinely when uncertain, not treat autonomy as a goal; (2) touches dependency management — Claude would need to decide at its own discretion when to wrap a batch and move to the next; (3) commit cadence and /done judgment steps still need to happen, not get skipped for speed.
- [idea] Restore web-search-when-uncertain rule — older plugin versions had a rule: when Claude is uncertain about how something works, whether a better approach exists, or needs more information to answer confidently, it should always offer to do a web search. Whether offered by Claude or requested by the user, all research gets filed under resources/research/ for later reference in the relevant build batch, log entry, or capture.


### Parked

- [idea] Batch cohesion ordering heuristic — the build log as decision log creates pressure for discrete builds, and batch ceremony is friction for users. Two parts: (1) queue ordering rule — builds touching an area with no related batches yet should sink (absent urgency or dependency), giving time for more captures to accumulate and make the batch worthwhile; (2) /next-time check — if related captures exist for the top batch, Claude should recommend switching to /plan to incorporate them first. Batching also touches context window management, not just coherent logging — Claude needs to think about one area of related concerns at a time. Needs design work to sharpen "no friends" and "related" into mechanical rules.
- [idea] Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
- [idea] /done spec check — after writing the **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. Retrospective check (at decision time) vs the current /plan pipeline gate (prospective, at planning time). Both mechanisms need more real usage before deciding how they relate.
- [idea] Pre-push sweep could be lighter if /done flagged host-side impacts at build time — accumulate a manifest of "this change affects X in project docs" during /done while context is fresh, then the push sweep checks flagged spots instead of re-reading everything. Sweep stays as safety net but gets cheaper. Design question: cross-build staleness (build 3 invalidates something build 1 touched) still needs the sweep to catch it.
