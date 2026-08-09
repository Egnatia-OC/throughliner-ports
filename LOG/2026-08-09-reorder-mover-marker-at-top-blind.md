# [HASH] — Nothing built: the queue mover's marker-at-top fix was already shipped, and the queue had gone on asking for it

This item asked for `split_blocks` in `reorder_queue.py` to detect a cleared-to-run marker sitting above every work item, plus a test case for that shape. Both already exist. The function scans the section preamble and sets `marker_above_all`; the suite carries three dedicated cases — a plain reorder, an explicit `--marker-after`, and a `--move` — and all three pass. `LOG/index.md` records the work shipping at `f9326dc`, among "the queue mover's `--delete`, `--move-section`, BEFORE/AFTER anchors and two marker bugs".

The item was written before that commit and was never removed from Processed afterwards, so /next presented it as ready work. It was caught only because the build began by reading the function it was about to change.

This is worth an entry despite building nothing, because it is the second recorded instance of the pattern `[emergency-revert-playbook]` names as its lead finding: **after a rollback, the queue keeps asking for work that is already done.** The first was seven instances in the session immediately following the emergency revert, each caught by accident. Two independent occurrences move that finding from an observation to something the shipped recovery guidance can assert, which it now does — it leads that document, and the reasoning is that it costs the most and announces itself least.

The check that catches it is cheap and is now written down where a recovering session will read it: before building anything in the sessions after a rollback, look for the item's slug in the LOG, and treat that suspicion as the default for the whole recovery period rather than a one-off.

**Files touched:** none — `plugin/si-plugin/scripts/reorder_queue.py` and `resources/testing/test_reorder_queue.py` were read and found already correct.

**Routed to Captures:** none.

FAQ: not needed because nothing shipped and no user-facing behaviour changed.
