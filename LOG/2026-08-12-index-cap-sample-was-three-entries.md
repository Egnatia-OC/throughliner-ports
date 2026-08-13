# 16ed591 — The 20% index-line cap was measured against the whole corpus, found to be measuring the wrong thing, and repealed

The cap said an index line must stay within 20% of the length of the entry it points to. It was derived from three entries of 968, 1,055 and 1,738 words. Measuring all 416 index lines that have an entry file to measure against turns that derivation inside out.

The cap is monotonic in **entry** length, not in line length. Not one of the fifteen entries over 1,000 words breaches it — the worst sits at 19.9%. Five of 96 breach it at 500–999 words, 61 of 227 at 200–499, and 51 of 78 under 200 words, where the median line is already over the cap. The worst breaches are all short entries carrying entirely ordinary lines: a 34-word line against an 87-word entry reads at 39%, and a 46-word line against a 96-word entry at 48%.

So the cap does not measure what it was written to measure. It was written to stop an index line restating its entry. What it actually measures is how short the entry is. On the corpus it governs it fires 117 times and, on the evidence of its worst cases, essentially never on the thing it was aimed at. The three entries in the original sample all fall in the two longest buckets, where the breach rate is 0–5% — the sample was unrepresentative of entry length specifically, and entry length is the variable that drives the whole result.

The item predicted this outcome in advance and said what to do if it landed, which is what was done: the proportion is dropped, and the cap is replaced by the requirement it was standing in for — an index line must support the open-or-skip decision without restating the entry. That test was already in the rule and needs no figure.

No replacement number. Scoping a cap to entries above some length reintroduces a bare figure, banned twice already in this project; and absolute length discriminates nothing, since the longest lines in the corpus (340, 231, 224 words) all point at the longest entries and all read correctly.

The cost is real and was weighed rather than waved off: the rule becomes unenforceable by script, at a moment when this project has been deliberately preferring mechanical checks to judgment. The counter is the measurement itself. A mechanical check that fires 117 times against work nobody thinks is wrong is worse than no check, because it is learned past and then ignored everywhere.

A second site turned up by grep and was not named in the item: the close restated the bound at its index-line step. It now carries the same no-cap wording and an explicit do-not-restore.

The distribution is filed as a durable finding rather than summarised here, because a later session asking whether 20% was defensible must be able to re-read the numbers rather than take this on trust. The count also differs from the 87 the item recorded — a different denominator and a corpus that has grown — and the finding says so rather than reconciling it, because nothing turns on which figure is right.

**Files touched:** `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`, `plugin/si-plugin/docs-b/done.md`, `resources/research/index-line-length-distribution.md`

**Routed to Captures:** none

Rule gate: run — this is a repeal. A limit is removed and nothing takes its place, which the derivation rule requires be explained rather than left silent; the explanation and the measurement are written in beside the repealed figure so a later reader meets the evidence before restoring it. The always-loaded text is net shorter for a rule, not longer.
