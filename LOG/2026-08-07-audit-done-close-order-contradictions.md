# [HASH] — Three collisions inside the close family resolved: scan order, approval frame, and the push offer at a combined close

**Scan order.** `done.md` said in two places that the wind-down re-scan runs before the LOG entry is drafted, while the `[user]`-item close and the handmade close both ordered entry-then-scan. The ordering is load-bearing rather than cosmetic: the scan exists so its captures land in the entry's "Routed to Captures:" line, and running it after means amending that line as a working-tree edit *after* the user approved it. Both stragglers now run the scan first, with the reason stated at each site rather than left to the reader to infer. All four close paths now agree.

**Approval frame.** `done.md` declared the frame "identical for every flavor" — write the entry to its LOG file first — while the handmade close told sessions to show entries for approval before writing. That half was resolved toward write-first as part of [show-then-write-survives-at-step-level], which owned the sweep; the declaration is now true rather than aspirational.

**The push offer at a combined close.** `done.md` supports a /plan close that also closes a completed `[user]` item; `done.md` says a push offer applies; `done-plan.md` says a planning close never offers push. No carve-out on either side said which wins.

It resolves **toward offering**, and the reasoning is recorded rather than the rule simply being asserted: the stated reason for suppressing is that a planning commit ships nothing, and a completed `[user]` item is not nothing — it is real project progress the user did, and leaving it unpushed is the outcome the suppression was never aimed at. So the test is whether the commit carries anything beyond planning bookkeeping. If it does, offer; if it is purely queue and log housekeeping, don't. The override in `done-plan.md` now states that it yields in exactly that case.

Kept separate from [show-then-write-survives-at-step-level] at the user's decision even though both touch `done.md`, with ownership stated in both items so a later build would not guess: that item owned the write-first sweep across all six sites, this one owned the done-family ordering contradictions. Whichever ran second re-grepped before editing, which is what happened.

**Files touched:** `plugin/si-plugin/docs-b/done.md`, `plugin/si-plugin/docs-b/done-plan.md`
**Routed to Captures:** none
