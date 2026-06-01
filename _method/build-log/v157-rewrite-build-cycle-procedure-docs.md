# v157 — 2026-06-01 — Build-cycle procedure doc rewrite

**What shipped.** Three procedure docs rewritten to fix fundamental design problems. before-build.md (115→55 lines) became read-only — removed all BACKLOG writes, Files/Tests population, batch-sizing splits. build.md (~120 lines) absorbed Files/Tests population from before-build and introduced [Build]/[E2E] test-type markers plus an explicit "Do not run /sovclose yourself" rule. close.md (227→77 lines) collapsed 18 steps into 4 with two [PROMPT] stops — prevents Claude from absorbing close silently. TEST-LOG rows 071–079.

**Decisions taken and why.** Two [PROMPT] stops in close (not three) — a third stop between finalization steps would create a pause with nothing for the user to do. Test-type distinction uses inline markers [Build]/[E2E] on test entries rather than separate sections — keeps tests together and makes routing self-describing. Files/Tests population lives in build.md's snapshot step (not planning) so batches stay clean until build time.

**Pivots and surprises.** BACKLOG parser skips batches without Files: sub-section — discovered when the new batch (created without Files:) was invisible to the parser. Added Files: to the planning-created batch to unblock. Self-correction during close: opening line of close.md said "three" stops but implementation had two — caught by Claude test, fixed immediately.

## Performance
- **Batch completion:** Complete
- **Files in batch:** 3
- **Carve-outs:** None
- **Claude-verified tests:** 7 Pass, 0 Fail (of 7 total)
- **User-verified tests:** 2 pending
