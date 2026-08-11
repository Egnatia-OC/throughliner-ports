# 08c885b — The self-authoring gate gained an admission test for exceptions: restate first, admit only on a recorded instance

Captured by the user on 2026-08-10 with a block attached — no further exception-shaped rule may be admitted until this is in place. Mixed authorship: the block and the underlying principle are the user's; the design is Claude's, agreed in the processing interview.

**Why this designed out smaller than it was filed.** §4 already settled *where* an exception is written — main clause first, `subject to <X>` as a cross-reference rather than a restatement, multiple exceptions in their own subsection. And the narrow why-clause exception this item said to design alongside was repealed and replaced by the purpose-clause test on 2026-08-10, so that half was already spent. What remained missing was **admission**: nothing in the document said how an exception earns its place at all.

**The design reuses the purpose-clause test's shape rather than inventing one.** That test runs admission on evidence → protection by grammar → review from the drafting note. This one mirrors it: restate the rule so it needs no exception; where restatement genuinely fails, require a recorded instance of the bare rule producing a wrong outcome; and cite that instance in the LOG entry so a later auditor can ask whether it is still a live risk. The middle bar exists because every author believes their own rule is the edge case — which is the shape under which the predecessor document grew from 6,162 to 21,445 words while being honestly applied.

**The worked case is also the item that triggered the block.** [derivation-required-for-limits] was drafted as *a bare number is banned, except where it derives from a proportion, from research, or from an external constraint*. It restates without loss as **a limit must state what it was derived from** — the same rule, with no exception in it. The first test disposes of the case that produced the block, which is the strongest available evidence that the test is the right one.

**The count question is answered "no number", deliberately.** The item asked whether a rule with more than some number of exceptions is evidence it was never worked out. Claude recommended against writing that number and the user agreed: it would be a bare limit requiring its own derivation under [derivation-required-for-limits], with no data to derive it from. The restatement test does the same work without counting — a rule accreting exceptions is one whose exceptions each failed restatement, which is visible on the face of it. This also dissolves the mutual-constraint problem the item worried about, since nothing admitted here is a limit.

**The test was used in this same run, which is the honest test of it.** [write-first-report-without-write] asked whether a whole-queue migration is a third show-first exception. Applying limb 1, the write-first rule restated without loss — from "does a revert fully undo it?" to "is the previous version recoverable without the user's help?" — and the migration case fell out of the restated test rather than needing an exception. No exception was admitted anywhere in this run.

**What it unblocks:** [derivation-required-for-limits] and [index-line-length-proportional-cap], both held below the line on the user's block. The first must be rewritten to the exception-free wording above before it ships, rather than built as drafted. Both are now lint-flagged as blocked by a slug no longer in the queue, which is the "blocker shipped" case for /plan's below-line revisit to lift.

**Files touched:**
- `resources/self-authoring-rules.md` — new §1 subsection "Admitting an exception — restate first", cross-referenced from §4's exception bullets so placement and admission point at each other.

Host-only file: consumers never author method rules, so no SPEC, README or FAQ sync applies.

**Routed to Captures:** none.

FAQ: not needed because the change is host-only — it governs how the method's own rules are authored, which consumers never do and never see.

Self-authoring gate: run, and this item IS an addition to it. The rule it adds passed its own admission test — it names its parent (§4's exception bullets), it restates as a positive action rather than a prohibition, and it was admitted on a recorded instance ([derivation-required-for-limits]) rather than on a belief that exceptions need governing.
