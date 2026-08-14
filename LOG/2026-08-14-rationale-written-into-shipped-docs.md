# [HASH] — Audit: about 1,050 words of rationale in the shipped procedure docs, 255 of them always-loaded, filed as eight cut items plus a second-pass audit

Filed 2026-08-13 by Claude mid-run from its own conduct, after Alex asked what had
made the turn expensive. Run as an audit rather than a build on the decision taken
at processing: the judgement is per paragraph and the docs are large, so a build
would have been a long unattended run making hundreds of judgement calls with
nobody watching. An audit edits nothing, so every proposed cut is approved before
it leaves the docs.

**The rule being tested.** The operative statement stays bare, and why a rule is
worded as it is — which alternative lost, what the trade-off was — goes to the LOG
entry that decided it. The research behind it is explicit that why-clauses
travelling with every rule are the over-prescription the 5-series guidance says
degrades output. The test applied per paragraph: delete it and read what remains —
a complete, correctly applicable instruction means what was deleted was rationale;
an unfinished or misapplicable one means it was operative and stays.

**Coverage, stated plainly because the honest limit is part of the finding.** The
pass applied **one systematic criterion across all thirteen files** — bolded
why-paragraphs and defeated-alternative markers ("was rejected", "was refused",
"recorded so it is not…", "Note what this replaces") — rather than reading 42,554
words paragraph by paragraph. That is the shape the defect takes most often and it
is not the only shape. It was presented to Alex as a floor rather than an
inventory, and she approved the whole set with nothing contested.

**Eight findings, by document.** Four paragraphs in `skill-nonspecific-rules.md`
(~255 words, and the highest-value cut on the list, since a word removed there is a
word saved in every session forever); `next.md`'s bulk-removal post-mortem (~195,
the largest single one); `done-plan.md`'s two repealed-step explanations (~130, the
clearest case, since the reasoning is about text already gone); three paragraphs in
`plan.md` (~200); `done.md`'s close-date argument (~90); two in `done-build.md`
(~105); `next-build.md`'s spec-sync replacement note (~75); and
`migrate-checklist.md`'s show-first explanation (~60).

**Two paragraphs tested the other way and are recorded as staying**, so a later
build does not sweep them up: `next-build.md`'s "The reason clause fires every
time" — it says *when* the clause fires, which is the rule — and the second
paragraph of `plan.md`'s deletion-branch note, which carries the operative
statement that re-examining a held item is the user's fate decision, something the
branch table does not say.

**One finding is filed as explicitly contestable rather than as an ordinary cut.**
`migrate-checklist.md`'s paragraph fails the test cleanly, but its working function
is to stop a later session reading show-first there as an exception to write-first
and "correcting" it. The doc is fetched rather than always-loaded, so the saving is
small and a keep would be defensible.

**The complication the item flagged at filing held up in practice.** The judgement
is genuinely hard at the keyboard, because the gate admits *operative* purpose
clauses — a reason needed to apply the rule correctly is reclassified as part of the
rule rather than stripped. The failure is not that any why is wrong; it is that the
reclassification test goes unrun, and its absence defaults to keeping the prose.
Two paragraphs were caught this way *during* the same run that audited for them, at
`next.md`'s off-ramp and `next-build.md`'s new table row — written, tested, and cut
at the moment of authoring rather than found later.

**Files touched:** read `plugin/throughliner/docs-b/` (all thirteen files). Edited
nothing.

**Routed to Captures:** nine — `[cut-rationale-snr]`,
`[cut-rationale-next-bulk-removal]`, `[cut-rationale-done-plan]`,
`[cut-rationale-plan]`, `[cut-rationale-done-close-date]`,
`[cut-rationale-done-build]`, `[cut-rationale-next-build]`,
`[cut-rationale-migrate-checklist]`, and `[rationale-audit-second-pass]`.

**Approval outcomes:** all eight findings approved as-is, nothing dropped or
reworded. Alex then asked, in her own words, for a capture describing an audit that
might pick up some more — filed as the ninth, naming the shapes one criterion
structurally cannot see: unmarked paragraphs with no signature phrase, rationale
folded into the back half of a sentence that begins as a rule, worked examples
standing in for reasoning, evidence attached as a subordinate clause, and anything
inside a fenced block, which this pass did not read as prose at all.
