# V111 — 2026-05-28 — Queued-pipeline staleness sweep at close

**What shipped.** Four new mechanisms from batch 0110, split between hooks and procedure docs based on whether they're pattern-matchable or judgment-based. (1) Concurrent-build detection in SessionStart: warns when `Status: active` batch has unticked files (distinct from existing unclosed-build detection where all files are ticked). (2) OQ staleness detection in SessionStart: flags open questions whose `Surfaced` session tag is 20+ sessions behind the latest build-log session number. (3) Queued-pipeline staleness sweep as close step 9: after a build, greps all queued/parked batches and OQs for references to file paths renamed, deleted, or moved in the build. (4) Lost-feature check as close step 10: scans for parked batches whose parking conditions were met and orphaned carried-forward items from recent build-log entries. Method version bumped to V89 (plugin 0.89.0).

**Decisions taken and why.** Split enforcement between hooks (mechanical, pattern-matchable) and procedure doc (judgment-based). Concurrent-build detection and OQ staleness are purely regex on status lines and surfaced tags — hooks. Staleness sweep needs build context (which files were renamed) that hooks don't have — procedure doc. Lost-feature check requires semantic judgment about parking rationales — procedure doc. Decided against file-existence checks on queued batch Files: entries because queued batches often list files that will be *created* during the build, producing false positives.

**Pivots and surprises.** None.

**Carried forward.** Nothing.

## Performance
- **Batch completion:** Complete
- **Files in batch:** 7 (session_start.py, close.md, VOCABULARY.md, Reference manual.md, INVENTORY.md, reference.html, test fixtures)
- **Carve-outs:** None
- **Claude-verified tests:** 7 Pass, 0 Fail (of 7 total)
- **User-verified tests:** 0 pending
