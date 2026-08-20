# [HASH] — The measurement script ships, and its re-derived figures do not become bands

Filed from INBOX mail sent by a consumer project. Verified here before filing: `measure_written_shape_length.py` existed in this project only, a `find` over `plugin/throughliner/` returned nothing, and the shipped `skill-nonspecific-rules.md` told every consumer to run it. Every consumer was directed at a path their project does not have.

Worse than a broken pointer: that same section presented its figures as "demonstrated to be sufficient, never ideal" and a limit as "traceable and revisable rather than correct". The script was the only affordance for checking or re-deriving them, so without it the figures were precisely what the rules promised they were not.

**Superseded in part, and this is the substance of the entry.** [retire-word-band-caps-keep-measurement] shipped earlier in this same run and retires every cap. What survives here is the shipping defect the item was filed for — the script moves into the plugin package. **What falls is the second half:** the re-derived figures (captures 114 / 261 / 540, build records 191 / 356 / 571, derived from the two docset regimes' own distributions with no invented multipliers) are **not** shipped as bands, because the argument that retired every cap retires these two as well. The re-derivation is not wasted: showing the old ceiling to be tighter than the era it came from is part of why the caps went at all. It lands as a record rather than as a rule.

**The move itself was folded into the retirement item earlier in the run**, because that item rewrote the always-loaded pointer to the plugin-root form, and leaving the file in `resources/` would have shipped a broken pointer for as long as the run took to reach this one. Its docstring's host-only line was repealed in the same move.

**What this item added on its own turn: both named build details were checked rather than assumed.** The `reconfigure` block already matches `reorder_queue.py`'s canonical form — one call inside a loop over both streams, not one stream missed. The first `subprocess` git read already carries `encoding="utf-8"`; the second reads raw bytes from `git cat-file --batch` deliberately and needs none.

**Their suggestion that shipping settles the transfer question is refused, and the script's own docstring is why:** a project measuring its own corpus learns its distribution, not a defensible band. Self-derivation per project stays refused, and with the caps gone there is no figure to transfer either way.

**No separate FAQ entry.** The "how long should my queue items be?" question this item's ripple named is answered by the entry written for the retirement item, and a second entry would contradict it.

**Files touched:** `plugin/throughliner/scripts/measure_written_shape_length.py` (verified; moved and rewritten under the retirement item).

**Routed to Captures:** none.

Rule gate: run — no new rule; the figures are not shipped, and the invented 0.5 and 1.5 multipliers are evicted along with every other cap. **The eviction is the multipliers**, and the bands they produced go with them under [retire-word-band-caps-keep-measurement]. Failure evidence is a consumer report plus 88% and 73% breach rates measured here. *(Transcribed from the item and narrowed to what actually shipped: the item's disposition described replacing two figures, and the retirement removed them instead.)*

Tick: done, confirmed — the script runs from its new path and both named build details were checked.
