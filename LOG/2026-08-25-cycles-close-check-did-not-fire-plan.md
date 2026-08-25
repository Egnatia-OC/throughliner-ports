# 324005c — Kept: the close's cycles check reads the disk — diagnosed from the demo transcript as skipped, not clean

The user supplied the demo chat's transcript path and the read settled the open question: from /done's start to the commit the close never read CYCLES.md, carrying the opening's "no cycles doc" belief across a session that had itself created the doc — session memory covering for a file read. The fix: done.md's cycles step opens with a fresh disk read at close time, whatever earlier steps reported. Opening sites left alone — the queued verification walk-through tests them independently. Rule gate run — disposition on the item.

**Queue changes:** [cycles-close-check-did-not-fire] kept into Processed, cleared, diagnosis written in.
**Work processed:** kept — [cycles-close-check-did-not-fire].
