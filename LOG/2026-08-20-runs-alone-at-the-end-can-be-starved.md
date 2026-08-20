# b485ee3 — The digest now reports how many cleared items sit ahead of each `Runs alone` item

Filed by Claude from the user's question about why the `docs-b` rename had not happened. The design is Claude's, deferred to in her words: "as you recommend."

**The starvation reading is refuted, and that is recorded rather than quietly dropped.** The item was filed about [rename-to-throughliner] receding; that shipped three days later. And a `Runs alone` item is not deferred indefinitely by work sitting ahead of it — /next stops **before** it, so the following run reaches it. Genuine starvation needs planning to outpace building forever, which is a throughput problem rather than a placement one.

**What survives is visibility.** One session placed six items ahead of the rename and the queue gave no sign of it. It was said out loud only because Claude happened to notice, which is the siteless-check failure this project has recorded five times. Which is why the item's own third option is refused: it floated /plan narrating the placement — and that is exactly what happened that day, unprompted and therefore unrepeatable. A fresh short session, which this method designs for, would not notice.

So the digest prints one more computed line: for each `Runs alone` item, how many cleared items sit ahead of it. A fact, like every other digest line, never a verdict — and read at /plan's opening alongside the held-work lines. No threshold, no age, no judgment, so nothing here needs a derivation.

**The two obvious fixes stay refused, with their reasons.** Placing such work first stops every run at the top. Reporting how long an item has been *cleared* needs an invented age threshold, which this project bans — whereas a count of what sits in front of it is arithmetic. `plan.md` now says how to read the number: recession, not staleness. A correctly placed item recedes each time the queue is worked, because every planning session adds newly ready work ahead of it.

A live run over this queue prints [rename-docs-b-folder] with ten cleared items ahead of it, which is exactly the recession the item was filed about — and it was measured rather than asserted.

**Files touched:** `plugin/throughliner/scripts/queue_digest.py` (the computed block), `resources/testing/test_queue_digest.py` (two cases, including one asserting a computed zero prints "none" rather than looking like a check that never ran), `plugin/throughliner/docs-b/plan.md` (the opening read, which now names three blocks rather than two). SPEC.md is not listed — its digest paragraph was rewritten in the planning session that kept this. No FAQ entry: this changes what a planning opening reports, not anything the user does.

**Routed to Captures:** none.

Rule gate: run — no rule is authored. **The disposition is that a mechanical check replaces a prose rule**, which is this project's own stated test for retiring a noticing, and the eviction is the narration fix this item proposed, refused on the record above rather than shipped alongside.

Tick: done, confirmed — two new digest cases pass and the live run reports as designed.
