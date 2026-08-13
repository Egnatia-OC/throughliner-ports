# [HASH] — Index-entry candidates move from scope-lock to the tick, so a run only pays for the items it actually builds

/next's lock-scope step used to pre-generate a candidate index entry for every Claude-work item before the build started. The measurement that produced this item came from a live run: scope was locked over 23 items, 23 candidates were written for roughly 2,500 output tokens, and the run was interrupted after ten. Thirteen of those candidates described work that had not happened, would be written again by a later run, and were deleted with the working file at the close.

The reasoning behind pre-generating was sound and is not being called wrong — a candidate is cheapest to produce while the item's intent is fresh. What was wrong was doing it for the whole run at once. The cost scales with run length while the benefit does not: a candidate is only ever redeemed by an item that actually builds, and no run is guaranteed to reach its end. It is the same shape as the close-cost finding built alongside it — an unconditional per-item cost with nothing permitted to notice how many items there are.

The capture raised its own objection and the objection did not survive checking, which is the part worth recording. The objection was that pre-generating doubles as a readiness check on whether an item is describable at all, so moving it after the build loses that. But skill-nonspecific-rules.md's Index entries section already assigns exactly that check to /plan's keep-step: an item whose index line cannot be written yet is not ready for Processed. The lock-scope copy was therefore a second run of a test the item had already passed. And in the one case the check was meant to cover — a scope shift — done.md re-authored the entry regardless, so the pre-generated candidate protected nothing.

There is also a benefit the capture did not claim. Written at scope-lock, a candidate is a *prediction* of what the build will do, which is why done.md carried reuse-verbatim-or-re-author branching. Written at the tick it describes what the build did. That is more accurate as well as cheaper, and it makes most of that branching dead weight — which is why done.md and done-plan.md simplify rather than merely being adjusted.

This was built in the same run as [close-cost-depth-line-never-surfaces], deliberately. Both change the same per-item completion step in next.md, and editing that step twice in two runs is how a step ends up half-rewritten. The two together make the tick the single accumulation point: `Progress:`, `Index entry candidates:` and `Changes:` now all grow one item at a time.

One consequence to note for a future reader: next.md's own warning that the rationale-pointer is safe *because* items are copied out of QUEUE.md one at a time still holds, and its cross-reference was renumbered with the step it points at.

Rule gate: run — net removal. The pre-generate instruction is deleted and the reuse branching in done.md simplifies; no new standing rule was authored.

FAQ: not needed because nothing a consumer sees or is told changes — the candidate is an internal working-file field, and the index line they read is identical either way.

**Files touched:**
- `plugin/throughliner/docs-b/next.md` — the lock-scope step's pre-generation instruction removed, its remaining sub-steps renumbered 1–4 with the within-doc cross-reference corrected, and the working-file template's `Index entry candidates:` section changed to accumulate; the per-item completion step becomes the accumulation point.
- `plugin/throughliner/docs-b/done.md` — "Reuse the pre-generated candidate" branching replaced with plain reuse.
- `plugin/throughliner/docs-b/done-plan.md` — wording corrected: planning sessions carry no candidate.

**Routed to Captures:** see this session's other entries.
