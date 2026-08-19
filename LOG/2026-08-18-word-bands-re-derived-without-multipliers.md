# 02ec308 — the word bands re-derived from measured percentiles, with the invented multipliers evicted

A consumer project reported that the always-loaded rules tell every user to run `resources/measure_written_shape_length.py --bands`, and that no such file exists in a consumer project. Verified here: it sits in this project only, a `find` over the plugin package returns nothing, and line 711 of the shipped rules names it. The script's own docstring says "host-only dev artifact", so this is a shipped rule citing a deliberately unshipped tool rather than an oversight.

The user then asked how the figures were built, and the answer did not survive the asking. Only the middle number was measured — a July median. The floor was that halved and the ceiling that multiplied by one and a half, both conventions with no reason for their specific ratio, and both passing the method's own derivation test only because *any* multiplier is technically "a proportion of the thing it governs".

**Her correction moved the boundary and is what made the re-derivation possible: the split is not calendar months but the docset change** — before 2026-08-02 is docset A on Opus 4.8, after is docset B on the 5-series. On that cut, floor, middle and ceiling are each read off the two regimes' own distributions and split down the middle. Captures become 114 / 261 / 540 and build records 191 / 356 / 571.

Two findings fell out. The old ceiling is **tighter than the era it claims to represent** — docset A's own top quarter runs past it. And every shape moved by roughly the same factor, which looks like the writer changing rather than discipline slipping.

Planning records and index lines keep their old figures: 42 samples and an unmeasured shape respectively. Work items cannot be cut this way at all, since an item filed under one docset and enriched under the next belongs to neither.

**Queue changes:** [word-band-script-does-not-ship] filed from mail and kept into Processed, cleared.
**Work processed:** kept — [word-band-script-does-not-ship].
