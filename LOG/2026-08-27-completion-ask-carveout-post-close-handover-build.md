# [HASH] — One exception to the no-completion-asks bar, keyed on two recorded facts

The bar on asking whether `[user]` work is done is strong and stays strong. It
leaves three routes to knowing: the item was walked to its end this session, the
user volunteered it, or its walkthrough named an observable check that passed.

**One case shuts all three by construction**, and that is what earned the
exception through the restatement test. Where an item's own record shows it was
handed to the user for completion *after a close*, and it names no observable the
method can reach: the work happened in a chat that has ended, so nobody can walk
it; there is nothing in the world to check; and the only remaining route asks the
user to volunteer something they were handed days ago. The bare rule cannot be
restated to cover it — the failure is not in the wording.

Without the ask, such an item is re-presented as unstarted. Both admitting
instances are in the 2026-08-26 build transcript: the re-presentation itself, and
a barred ask that would have resolved it.

**The key is both facts together, and the text says so twice.** An item without a
recorded hand-over never qualifies; neither does one naming something checkable.
One ask, then take the answer.

**Three softer routes were refused on the item.** Softening the bar generally —
worse than either recorded failure. Relying on /rescan — the failing case is a
closed chat. A notification or watcher — mail is fire-and-forget, a standing
refusal.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md` (the
carve-out beside the completion-inference routes, with the restatement-test
reasoning written as operative text rather than an attached why);
`plugin/throughliner/docs/next.md` (the walk-through branch's open-the-record
step, which is where it fires). SPEC's sentence for this was already written at
the planning session ahead of the build.

**Routed to Captures:** none.

Rule gate: run — an exception to the no-completion-asks rule, taken through the restatement test: the bare rule cannot be restated to cover this case because all three inference routes are shut by construction; the admitting instances are the re-presentation failure and the successful barred ask, both in the 2026-08-26 build transcript. Nothing evicted.
