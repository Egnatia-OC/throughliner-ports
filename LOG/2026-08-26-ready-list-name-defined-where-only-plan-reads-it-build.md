# 2c76e53 — "The ready list" moved into the always-loaded rules, where its three sites can actually read it

From the compliance audit's distribution lens. `plan.md` declared "the ready list"
the standing plain-English name for the cleared region and said it is "used
identically in every session's asks" — a claim the rule could not deliver on. It
fires at /plan's recommend step, at /next's off-ramp when the run is presented, and
at /done when the close reports what is ready. Only the first of those reads
`plan.md`; the other two load their own docs and the always-loaded rules, neither
of which carried the name.

So the fix is distribution rather than wording. The name now sits in
`skill-nonspecific-rules.md`'s Vocabulary section, where every skill and every
no-skill conversation reads it, and it passes that file's own admission test: it
fires in more than one skill and in plain conversation too.

The declaring sentence in `plan.md` was evicted in the same edit so nothing is
doubled — the recommend step keeps only the usage, with a cross-reference.

**Files touched:**
`plugin/throughliner/docs/skill-nonspecific-rules.md` — the one-sentence naming
rule added to Vocabulary.
`plugin/throughliner/docs/plan.md` — the declaration removed, usage kept.

**Routed to Captures:** none.

Tick form: done, confirmed — a grep for "ready list" across the shipped docs finds
exactly one declaration and one usage, and the recommend step still reads complete.

Rule gate: run — a distribution move: one rule relocated into the always-loaded
file with its old statement evicted in the same move, nothing new admitted.
