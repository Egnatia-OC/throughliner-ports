# v104 — 2026-05-27 — Dev-side session-protocol procedural convergence

**What shipped.** Rewrote `Dev/session-protocol.md` with six additions converging dev-side session discipline with plugin-side procedure docs. Opener routing table maps six session types to load/skip/middle/close. Carried-forward read-back added to session open. Pre-commit checkpoint names every artifact explicitly. Idea sweep enforces three-way triage (BACKLOG batch, build-log "not pursued," or BACKLOG open question). Session close split into implementation (full) and lighter (planning/doc-only/ideation/E2E) paths. Batch-ordering audit added as a standalone section.

**Decisions taken and why.**
- Lighter close still includes build-log entry and footer-bump check — every session produces a tagged commit with a build-log record, regardless of type.
- Batch removal from BACKLOG is conditional in lighter close (only if the session consumed a batch), not skipped unconditionally — doc-only batches like this one still need cleanup.
- Opener routing table uses "skip doesn't mean refuse" escape clause — mid-session loads are always available.

**Carried forward.** Nothing.
