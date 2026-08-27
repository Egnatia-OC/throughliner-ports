# 32675a3 — "`[user]` line" becomes "`[user]` item" across the shipped docs

The method called the same thing an item everywhere except when it carried the
`[user]` tag, where it became a "line". Nothing turned on the difference — it was
residue from a queue format where a piece of user work genuinely was one line —
and it made the docs teach two words for one concept, which is precisely what the
shared-vocabulary rule built alongside it forbids.

Fourteen sites reworded. Sentences that leaned on line-ness were rephrased around
the item rather than word-swapped: "file the line" became "file it", and the item
is now "written into the queue before its first step" rather than "the line is
written before its first step".

**Sweeping LOG/ and old queue prose was refused on the item** — records keep the
vocabulary of their time, and a record edited to match later words stops being a
record of what was decided.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md` (7),
`plan.md` (5), `next-build.md` (2), `done.md` (1), `SPEC.md` (1), `CLAUDE.md` (2).
A grep for every variant across shipped docs, templates, SPEC, CLAUDE.md, FAQ and
README returns nothing.

**Routed to Captures:** none.

Retired: `[user]` line / lines — the name for a `[user]` work item, now `[user]` item / items. Recorded in `resources/retired-terms.md` as the two-word phrase, never as the bare word "line", which is load-bearing in correct writing elsewhere — the readiness line, the cleared-to-run line, an index line. A bare entry would fire the retired-term check on all of them, which is the cry-wolf failure that file already records against `CEILING`.

Rule gate: run — no rule authored; existing text corrected to one term.
