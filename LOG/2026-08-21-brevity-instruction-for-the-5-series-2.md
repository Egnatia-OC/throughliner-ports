# cc33c1e — The always-loaded licence for any length is repealed and restated as the action required

Build entry. The planning entry that processed this item is
`2026-08-21-brevity-instruction-for-the-5-series.md`.

**Why this was worth doing.** The user's position is that Claude's verbosity is the
single thing stopping her promoting the plugin beyond GitHub. She also corrected the
objection that nearly buried the item: Claude cited SPEC's claim that rationale must
ride a rule for the rule to be followed, and she identified it as a 4.8-era result.
It is. The project's own current-model research — `opus-5-instruction-compliance.md`
and `fable-5-instruction-compatibility.md`, both live and unsuperseded — records that
the 5-series is verbose by default, that length is a prompt-side control, and that a
short brevity instruction steers as well as a quantified target or a list of patterns
to kill. So the record had talked this project out of the one lever its own research
recommends: SPEC said a prose instruction to be brief "was tried first and measurably
did nothing", which is why caps were introduced — and it was tried on 4.8.

**The defect was one clause, and it was the counterweight rather than a missing
rule.** `skill-nonspecific-rules.md`'s message-shape bullet ended: *"giving every
explanation the user needs in order to act, in full sentences, at whatever length
that takes — what comes out is the padding around it: meta-narration, a restatement
of what was just shown, hedging."* On a model verbose by default, an explicit licence
for any length is the half that wins. Its second half also stated the constraint as a
list of things not to do, which the wording rule names as the signal that the action
was never specified.

**What was built.** That limb now reads: *"saying what the user needs in order to
act, in full sentences, and stopping there — except that where being readable and
being short pull apart, readable wins."* One limb out, one limb in. No word count, no
band, no pattern list — the bare-number ban is satisfied by evidence here rather than
by omission, since the research says a short instruction is as effective as either.
The readability bound ships inside the same limb, from the Fable finding: readable and
concise are different things and readability matters more where they conflict.

`grep "at whatever length that takes"` under `plugin/throughliner/docs/` returns
nothing. The file's rule-statement count was unchanged at 308, confirmed with
`rule_signals.py` — a limb replaced rather than added.

**Two refusals stand.** Siting this in a fetched doc: it must shape every message in
every skill and outside them, so it cannot be fetched. Removing the
write-then-re-read clause before a pointer: the Opus 5 guide targets verification
that buys no quality, but that clause exists for a recorded instance of pointing at
text that was not there.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md`.

**Routed to Captures:** none from this item.

FAQ: not needed because the user sees shorter replies and does nothing different,
which is the FAQ trigger's own test.

Rule gate: run — admitted as an amendment replacing one limb of the existing message-shape bullet in the always-loaded rules, subordinate rather than freestanding, so no new slot is spent. **The eviction is "at whatever length that takes"**, repealed outright along with the prohibition list that follows it; the limb is restated as the action required. **No figure is introduced**, because the research says a short instruction steers as well as a quantified one — so the bare-number ban is satisfied by evidence rather than by omission. Failure evidence is the user's sustained report across every context plus the model guide's documented default. **A hook was considered and refused: nothing mechanical reads Claude's chat output.**

Depth: short. Built and confirmed. Whether it moved anything is
`[brevity-amendment-outcome]`'s question, and the before-figures it will read are in
`2026-08-21-transcript-output-measurement-2.md`.
