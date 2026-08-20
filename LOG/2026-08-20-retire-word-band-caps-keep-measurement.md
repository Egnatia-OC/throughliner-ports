# b485ee3 — Every written-shape length cap retired; the measurement stays and now ships

The user's decision, in her own words: the numbered caps are *"too arbitrary and we have realer leads now."*

The argument that settles it came from the tool itself. `measure_written_shape_length.py`'s docstring refuses to print a band beside a distribution, because *"a band printed inside the distribution report would be a threshold read off the thing being questioned."* The shipped bands were exactly that — the middle of what this corpus had already written. The script declined to do the thing the rules did.

This project had already accepted that argument once, one layer up: the rule-corpus ceiling was removed on the ground that it had lost its derivation and no defensible replacement existed. The word bands were the surviving instance of a pattern already retired. Three facts sat behind the decision rather than a mood — the rules' own caveat called the figures lengths *demonstrated to be sufficient, never ideal*, which describes past behaviour rather than setting a standard; the re-derivation the day before had to exclude three shapes of five for want of defensible data; and acting on a breach measured 8%, 3% and 9% across three passes.

**What must not happen, because it is a known failure, and it was weighed here rather than assumed.** A prose instruction to be concise shipped first and measurably did nothing, which is the recorded reason the bands were figures at all. Retiring figures back to prose walks into that. The replacement is neither: it is structure — the build block and the relocation of history along the seam it creates, shipped in this same run. That lever is aimed at where text lives rather than how it is worded, and it is untried.

What stays is the position, not the arithmetic. Both failures are real: a record too thin to rebuild intent from fails as surely as one too long to get through, and the second is the one this method has actually produced at scale. Only the numbers claiming to locate that line are gone.

**Folded in from [word-band-script-does-not-ship], which came later in the same run:** the script moved to `plugin/throughliner/scripts/` here rather than two items later, because this item rewrote the always-loaded pointer to the plugin-root form and leaving the file in `resources/` would have shipped a broken pointer for as long as the run took to reach the other item. Its docstring's host-only line was repealed in the same move. This is the merge operation the rule shipped elsewhere in this run describes: the host is rewritten and what came out is named.

`--bands` now exits with an error naming the repeal rather than silently doing something else — a flag that quietly does something different is worse than one that says it is gone.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (the band table and its five derivation paragraphs; two later band references), `plan.md` (the keep-step read), `done.md` (the entry and index-line reads, and the historical note about the repealed 20% cap, which now records that its absolute replacement went too), `resources/measure_written_shape_length.py` moved to `plugin/throughliner/scripts/` with `BANDS`, `band_status` and `bands_report` deleted and a new `current_report` added, `faq-template.md` and `faq-index-template.md` with their `FAQ/` copies.

**Routed to Captures:** none.

Rule gate: run — **the disposition is an eviction and nothing is authored.** Five figures and their breach actions are repealed across four live files, along with the derivation paragraphs defending them; no rule replaces them, and the replacement is a structural item already in the queue. Failure evidence is the tool's own refusal to self-derive, three shapes left unmeasurable at the last re-derivation, and three passes yielding 8%, 3% and 9%.

Tick: done, confirmed — the script runs in both surviving modes and `--bands` errors as designed.
