# d6efa7c — The LOG depth decision becomes a required field written at the tick, because an absent line was never a signal anyone could see

The short-form LOG entry has been the documented default for some time, and it has effectively never fired. The Understudy project measured why: closing an eleven-item /next run cost about 15,500 output tokens in one turn, and although the mechanism for buying full depth existed — a depth line written into the build working file during the build — exactly two of the eleven items wrote one, and all eleven were then written at near-full depth. Following the rule as stated would have roughly halved that turn.

The diagnosis came from reading the three docs rather than from the report, and it has two halves. The first is that the rule had no site. It sat as a floating sentence at the end of next-build.md's "Rules during build", hanging off no step, while the step that always runs — next.md's per-item completion — did not mention depth at all. This project has already established that a standing rule with no site does not fire; it is the same reason plan.md's rung re-check was hung on the pick rather than left free-floating.

The second half is that the signal is an **absence**. No depth line meant short form, so at the close a deliberate "short" and an item nobody considered look identical. Honouring the default would have meant hunting item by item for something that is not there, against eleven items whose reasoning was all simultaneously fresh and every one of which felt worth telling at length. The information was in the file and correct; nothing surfaced it at the moment of writing.

So the fix is a required field rather than a stronger reminder. Anything optional is still invisible when skipped, which is the whole problem — and a required field is the shape this method already trusts twice over, in the FAQ-sync disposition and the `Rule gate:` line. Both work by turning a silent omission into a visible one. That was the alternative seriously weighed and rejected: a more emphatic version of the same floating sentence would have failed the same way, because the failure was never a lack of emphasis.

Two things the capture named were deliberately left alone. The index-line overshoot the report also measured is already bounded by the open-or-skip criterion, and the proportional cap that used to sit there was repealed on measurement — re-scoping it would mean inventing a replacement number, which this project bans. And the structural tension the report named honestly stays unfixed: one LOG entry per built item is unconditional, so close cost scales linearly with run size, while the method correctly forbids advising how many items a run should take, since Claude has no gauge of context filling. Both rules are right on their own terms. The only real lever is where the user puts the cleared-to-run line, and that stays true.

Rule gate: run — amendment, no slot spent. The parent is next-build.md's existing depth sentence, which is repealed in the same move rather than left standing alongside the new field.

FAQ: not needed because the existing entry "My session records used to be long. Why are some of them short now?" already describes the short-form default, and this build makes that default actually fire rather than changing what a consumer is told.

**Files touched:**
- `plugin/throughliner/docs-b/next.md` — the per-item completion step goes from two things to three: tick, record `Depth:`, remove. Tick still goes first, so the interruption ordering is unchanged.
- `plugin/throughliner/docs-b/next-build.md` — the floating depth sentence rewritten to state the field's two values and to name the tick as the moment it is written.
- `plugin/throughliner/docs-b/done-build.md` — the LOG-entry step now reads each item's field rather than inferring from an absent line; a missing field is read as short and noted as a discipline slip.

**Routed to Captures:** see this session's other entries.
