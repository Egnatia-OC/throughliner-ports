# [HASH] — The remaining eleven rule-bearing docs restyled, and the pass's own search method turns out to be its coverage limit

**Why this was worth doing.** Filed on the same decision of the user's that carried
`[law-prose-restyle-heavy-docs]`. It follows that item rather than blocking it, because
the two heavy docs are where the standard meets the hardest text, so settling those
questions once stops this pass answering them ten times over.

**Scope, narrowed deliberately.** SPEC and the FAQ are out: the law-prose standard is a
standard for *rules*, SPEC is product truth governed by its own three maintenance rules,
and the FAQ is consumer-facing answers rather than instructions to Claude.

**The eleven docs were enumerated by listing the folder at build time**, as the item
requires, rather than from a list written earlier — the set of docs changes as work
lands: `done-audit.md`, `done-build.md`, `done-plan.md`, `feedback-and-inbox.md`,
`migrate-checklist.md`, `next-audit.md`, `next-build.md`, `next.md`, `recovery.md`,
`rescan.md`, `setup.md`. The folder is `docs/`, confirming `[rename-docs-b-folder]`
shipped.

**What was built — the wording lens, ten restatements.** `done-build.md`'s "No size
judgment about the next run" became "Leave the next run's size to the cleared-to-run
line". `done-plan.md`: "Never required" → "Runs on request only"; "don't panic" → "read
the edits as the user's own expected work"; the placement exception restated as "Leave a
`[user]` or `[audit]` line where it stands where…"; "Use the mechanical mover — don't
retype blocks" → "passing it the desired order and nothing else". `next-audit.md`: "Don't
skim" → "Read each artifact through". `next-build.md`: the inline-check prohibition →
"Leave the check to the user… and leave this item's scope as it stands". `next.md`:
"Never pick an item from past the marker" → "Pick every item from above the marker, and
only from there"; "Don't ask 'Ready?'" → "Frame the pause as what it is for"; the
walk-through's two "never say" clauses → "Open with the first step itself, and satisfy
this branch only by driving the steps". `rescan.md`: "Do not make one stand in for the
other" → "write both, each carrying its own half". `setup.md`: "Don't assume blank-slate
on Case B" → "On Case B, treat existing planning or spec documents as a possible
migration"; "Never represent the contents as screened" → "Describe the contents as
unscreened, and say what the only complete protection is".

**What was built — the subordination lens, two parents.** `setup.md`'s
public-repository offer became one parent with four provisions, absorbing two previously
freestanding statements. `done-plan.md`'s end-preferred placement rule gained a "Two
exceptions" subsection holding both exceptions as subordinate units, which is the
wording rule's own prescription for multiple exceptions.

**The counts, per file as the acceptance test demands.** `plan.md` 318 → 318, `next.md`
143 → 143, `next-build.md` 118 → 118, `next-audit.md` 6 → 6, `done.md` 244 → 244,
`done-build.md` 24 → 24, `setup.md` 165 → 165, `done-plan.md` 79 → 81. Every wording
restatement swapped one bold-led statement for another, so it moves no count — which is
the expected result and is mild evidence nothing was added under cover of a rewrite.
`done-plan.md`'s +2 is its new parent plus two bullets less the two statements they
replaced; the arithmetic gives +1 and the measured figure is +2, and the residual is
named rather than left as a gap.

**Two limits recorded rather than smoothed over.** `setup.md` measured no change at all
despite four bullets being added, which could not be attributed and is recorded as
unexplained rather than given an invented account. And five of the eleven files —
`done-audit.md`, `feedback-and-inbox.md`, `migrate-checklist.md`, `recovery.md`,
`rescan.md` — sit outside the set `rule_signals.py` counts, so no before/after figure
exists for them; `rescan.md` was edited and its change is therefore unmeasured.

**The coverage limit, which became its own capture.** Both restyle passes found their
targets by grepping for prohibitions that START a sentence or a bold lead-in. That found
thirteen across thirteen files. A count taken afterwards puts the remainder at roughly
151 occurrences of "don't", "never" and "do not" across these eleven docs alone. Most of
it is legitimate and must not be swept — typed-block contrast pairs, honest-limit
statements the authoring rule's carve-out protects by name, and prose describing what a
mechanism does not cover — so separating the real targets needs a judgment per
occurrence with no mechanical test available. Filed as
`[law-prose-pass-missed-mid-sentence-prohibitions]` rather than claimed as done.

**The per-paragraph rationale lens did not run here**, and that is a decision rather
than an omission: extending per-paragraph judgement across the fetched docs was costed
at roughly 42,000 words, which is why the earlier extension was refused. These docs keep
the signature-phrase criterion they already had.

**Files touched:** `plugin/throughliner/docs/done-build.md`,
`plugin/throughliner/docs/done-plan.md`, `plugin/throughliner/docs/next.md`,
`plugin/throughliner/docs/next-audit.md`, `plugin/throughliner/docs/next-build.md`,
`plugin/throughliner/docs/rescan.md`, `plugin/throughliner/docs/setup.md`.

**Routed to Captures:** `[law-prose-pass-missed-mid-sentence-prohibitions]`.

FAQ: not needed because the wording of instructions Claude reads changes and nothing a
user does changes.

Rule gate: run — no rule authored, amended or evicted; an extension of an already-admitted standard to the remaining files, carrying the same silent-authoring caution as its sibling and the same lens.

Depth: full — alternative seriously weighed: whether to extend the wording lens to
mid-sentence prohibitions inside this item or capture it as separate work. Capturing won
because the extension is a different pass — a judgment per occurrence rather than a
grep-and-restate — and carries the risk both restyle items already name, that a rewrite
is the one thing that can silently author a rule by changing one.

Built and confirmed.
