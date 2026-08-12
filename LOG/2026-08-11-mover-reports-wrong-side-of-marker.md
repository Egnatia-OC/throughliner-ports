# 7c9922a — The queue mover's side-of-marker report is guarded, with the regression test the defect earned [mover-reports-wrong-side-of-marker]

Filed by Claude from a live instance: the mover reported an item as sitting below the readiness marker when it had placed it above, and the file disagreed with the tool.

**Why it mattered more than a wrong message.** The mover exists so a session does not have to hand-edit and hand-verify queue structure, and its crossing messages are trusted — the session that found this had acted on those messages three times without re-reading the file. A message that is usually right and occasionally inverted is worse than no message: a session told an item is held would leave it held, or would "fix" a placement that was already correct.

**The root cause, found by reading the code rather than guessing.** Two earlier theories were both wrong and were recorded so they would not be retried — it is not a stale marker index, and not the horizontal rules in the moved item's prose. The actual defect: the report loop called `heading_slug` unguarded, and that function matches **any** line ending in `[slug]`, not only a `#### ` heading. So `Blocked by: [slug]` on a held item matched too, and the loop keeps the last match. The fix's shape was already in the file — the only other call site is guarded by `ITEM_RE` — so this was one line.

**Why the trigger is a common and growing case, not a rare glitch.** A `Blocked by:` line naming the moved item is exactly what exists whenever the move matters: clearing an item that other work waits on. And the false report ran in the dangerous direction, saying "waiting, NOT cleared to run" about an item that was cleared.

**The regression test earned its place, unlike its sibling.** [mover-console-encoding-mangles-output] shipped without one because the failure would not reproduce in any available shell. This reproduces deterministically from a fixture.

**The first fixture was wrong, and the test caught it rather than me.** With one cleared item, "AFTER alpha" spans the marker — an item's block runs to the next heading — so the moved item legitimately lands below it. That is the positional ambiguity the report exists to surface, not a bug. Two cleared items fixes it, and the fixture now records why so nobody simplifies it back.

**Verified against the pre-fix code**, which is what makes it a regression test rather than one that passes either way: the same fixture places the item at line 8, above the marker at line 14, and the old code reports BELOW. Six checks, all passing on the new code.

**Files touched:** `plugin/si-plugin/scripts/reorder_queue.py`, `plugin/si-plugin/scripts/test_reorder_queue.py` (new)
**Routed to Captures:** none from this item
