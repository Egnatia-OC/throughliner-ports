# [HASH] — /plan's two neutral gates say "run /done" instead of "close out", and the retired phrase is listed so the check can see the next instance

Captured by Alex on 2026-08-13, in her words: it's not "close out" anymore,
that's a retired plan feature — it's just "or run /done".

`plan.md` used the phrase in two user-facing gates, the last-item off-ramp and the
neutral end-of-queue gate, while the same document stated a few lines later that
there is no close-out phase in /plan. The phrase named an action the user cannot
take, so a gate written to be neutral offered a real option and a phantom one,
with no way for a non-coder to tell which was which.

**Only the two user-facing sentences changed.** `close-out` as an internal noun —
the build close-out, the audit close-out, the sub-doc headings in the done family —
is procedure-internal vocabulary and correctly named, so a global replace would
have been wrong.

**Settled at processing, including the question Alex raised.** She asked where the
procedure goes, given that agreeing to close out runs a real sequence of steps. It
goes nowhere: that procedure is /done's and always was. Nothing is relocated by
this item and nothing she does changes — she says the word, /done runs, the same
steps as before. The phrase was a name for /done's work that implied a planning
step which does not exist.

**One thing found while listing the retired term, which is a finding rather than
part of the plan.** Adding `close-out phase` to `resources/retired-terms.md` would
have made the checker fire on `plan.md`'s own sentence recording the retirement —
"There is no close-out phase here" names the term without any of the retirement
wording the detector looks for. That is the cry-wolf failure the list's own rules
warn about, caught before it shipped rather than after. The sentence was reworded
to say the phase is retired and no longer exists, which is both more accurate and
what the detector needs. Verified by running the board: the signal reports clean.

**Rule gate: run** — not an authoring change but a wording correction plus one
line of source data, which the gate's eviction section already treats as part of a
retirement rather than a new rule. Nothing admitted, nothing evicted.

**Retired:** `close-out phase` — a phase of /plan, retired 2026-08-12 and listed
now so the check can see the next instance. Listed as the two-word phrase and
never the bare `close-out`, because every internal use of that word is correct.

**Files touched:** `plugin/throughliner/docs-b/plan.md`,
`resources/retired-terms.md`.

**Routed to Captures:** none.
