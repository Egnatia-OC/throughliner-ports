# v118 — 2026-05-28 — Build-phase close handoff artifact

**What shipped.** `## Close handoff` section in the build snapshot (`active-build.md`). Build procedure appends one-liners per file as they're ticked — noting new names, renamed concepts, shifted frames, invalidated doc references. Close procedure reads this section first for doc-parity, frame-correction, and build-log narrative, falling back to Files: list scanning for legacy snapshots without the section.

**Decisions taken and why.** Close handoff is build-time context, not permanent scope — excluded when writing the batch back to BUILD-PLAN as shipped. This keeps BUILD-PLAN clean and avoids accumulating stale per-file notes. Mechanical changes that don't affect close steps are skipped (not every ticked file gets a handoff entry).

**Pivots and surprises.** Procedure docs (`plugin/docs/procedures/*.md`) carry footers but weren't in session-reference.md's footer bump list — bumped them anyway since the rule says "every method-side footer bumps." Gap noted for idea sweep. Also found batch 0120 uncommitted from a previous session — included in this commit.

## Performance
- **Batch completion:** Complete
- **Files in batch:** 5 (build.md, close.md, DOC-STRUCTURE.md, VOCABULARY.md, session-protocol.md)
- **Carve-outs:** None
- **Claude-verified tests:** 0 (no testable code — doc-only changes)
- **User-verified tests:** 0 pending
