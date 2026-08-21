# cc33c1e — The rationale lens runs: done.md loses 165 lines of history, plan.md is covered in part, and the acceptance test turns out to be undischargeable

**Why this was worth doing.** Split out of `[law-prose-restyle-heavy-docs]` on
2026-08-19 when the test that item was waiting on came back confirmed. The lens deletes
a paragraph, reads what remains, and keeps the sentence only where the instruction is
left incomplete without it. That works on text that is going to stay put — and it did
not work while work items were still feeding rationale into these docs at every build,
because the pass would strip text the next build writes back. The evidence that this was
actually happening is `resources/research/rationale-flows-from-items-into-shipped-docs.md`,
tested against git rather than argued. The condition ended when
`[split-the-cleared-region-for-concurrent-sessions]` shipped: a build now reads a derived
view carrying instructions only.

**What was built in `done.md`, every removal with its destination.** All history goes
here, to this entry, which is the destination the item names. Twenty sites: the
/setup-comparison paragraph at the close declaration; the "steps are what make the commit
safe" clause and the unconditional-read paragraph's restatement; the freeform close's
"naming it is the whole of what the tag buys" history; the one-sub-doc-carries-all-three
aside; the partial close's "restores nothing, and that is the design" restated as the
action; the advisory's entire "required artifact is the fix" paragraph, its
conditions-not-counts why-paragraph reduced to its typed block, the failed-advisory
anecdote, the reserved-slug explanation and the transient-handoff location argument; the
Also-in-this-chat section's user-quote paragraph, /rescan-relation paragraph,
post-commit-tail-as-precedent paragraph and written-on-the-entry paragraph, replaced by
two sentences; the condition-falls-out and two-placement-conventions paragraphs, keeping
the cost sentence; the dates rule's "One rule, no exceptions" and the multi-day
accommodation's closing paragraph, with the placeholder-token rule restated as the
action; the capture-belongs-to-its-session aside; the shipped-slug fourteen-item
anecdote; the backfill "pure delay for zero decision value" paragraph and the
staged-paths why-paragraph reduced to a clause; the commit-message "show it verbatim"
explanation; the shell-quoting detail and scratchpad-standing-list paragraph compressed
to one sentence; the staging-failure nineteen-entries anecdote and its
what-that-rules-out paragraph; the merge instruction restated; the overlap scan's hedge
example restated positively; the tab-completion anecdote and rung-2b history merged into
one statement; the post-commit tail's legible-dirt paragraph compressed, its
what-was-rejected paragraph removed, its staging-check paragraph restated as the action
and its render-verification anecdote removed; and the recurrence-evidence paragraph.
959 lines → 794. Statement count 244 → 235.

**What was built in `plan.md`, eight sites.** The why-both paragraph's split-reasoning
history and the conditional-read refusal; the rung-partition paragraph restated as the
operative yield requirement; rung 4's decay-deletion history; the length paragraph
restated as membership-not-order; the ripple-trace anecdote; the advisory-clear history;
the four-way-classifier history; the merge's 63-word measurement reduced to "one data
point"; the Files-line digest-brittleness explanation and the research-index and
level-question paragraphs compressed. 1,594 lines → 1,549. Statement count 318 → 322.

**The count rose while the file shrank, and that is expected for this pass rather than a
warning sign.** Several operative rules were buried in prose paragraphs and were restated
as bold-led sentences, which is what the lens requires and which makes them countable for
the first time. Line count is the signal for how much history came out; statement count
is not.

**The acceptance test is met for `done.md` and NOT met for `plan.md`, and this is
recorded as a shortfall rather than smoothed over.** The test asks that every paragraph
of both files go through the delete-and-reread test. `done.md` was read end to end across
four reads and worked section by section, so every paragraph was seen and judged.
`plan.md` was worked from targeted identification — grepping for the signatures of
history paragraphs ("Why both", "recorded because", "was rejected", "used to", "weighed
and lost") and reading around each hit. Roughly 40% of the file was read. A rationale
paragraph phrased without one of those openings was never looked at. Filed as
`[rationale-lens-plan-md-coverage-incomplete]`.

**The finding that matters more than the leftover work.** That acceptance test cannot be
discharged from the artifacts at all. "Every paragraph has been through the test" is
unfalsifiable, because a paragraph correctly judged operative and left alone looks
identical to one never read. This project has a standing pattern for exactly that defect
— the required-artifact rules that turn a silent omission into a visible one, used for
the FAQ disposition, the rule-gate line and the depth field — and this test was written
without one. Restating it as something a build can evidence is arguably the more valuable
half of the remaining work, and the capture says so.

**Files touched:** `plugin/throughliner/docs/done.md`,
`plugin/throughliner/docs/plan.md`.

**Routed to Captures:** `[rationale-lens-plan-md-coverage-incomplete]`.

FAQ: not needed because this relocates reasoning inside instructions Claude reads and
nothing a user does changes.

Rule gate: not needed — no rule is authored or amended. A pass that relocates rationale out of operative statements applies a standard already admitted, and the operational-versus-historical distinction it uses is the method's own delete-and-reread test.

Depth: full — reasoning contested: the acceptance test turned out to be unfalsifiable
from the artifacts.

**Built, UNCONFIRMED:** `plan.md` needs reading straight through, or the acceptance test
needs restating as something a build can evidence.
