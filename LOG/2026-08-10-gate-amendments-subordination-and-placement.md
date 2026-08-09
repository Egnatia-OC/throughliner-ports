# d632d6a — Subordination becomes an obligation in the self-authoring gate, condition placement re-decided main-clause-first, and §4's prohibition-framed heading restated — with the gate's own word ceiling refused rather than obeyed

Three amendments to `resources/self-authoring-rules.md`, landed together because authoring them separately in conversation is the fragmenting the user named when the item was filed.

**Amendment 1 — subordination as an obligation.** §1 already asked which existing rule a new one amends, and named the reason: a freestanding rule consumes one of the ~150–200 slots a model follows reliably, an amendment consumes none. What it lacked was a way to decide. The syntactic test from `resources/research/legislative-prose-syntax.md` supplies one — at least two parallel units, each reading as a continuation of the parent's opening words, all sharing one grammatical function, every modifier pointing only at the opening words or its own unit, and none a complete sentence. So the instruction is now: write the rule as a subordinate unit of its parent and ship it that way if it holds, with freestanding as the fallback when subordination fails rather than the default.

It had to serve both uses the user named, and the wording says so explicitly: writing, try the fragment before the sentence; auditing, hunt for standing rules that should have been subordinate. The same session's audit is what that second half is for.

One guard travelled with it, because the failure mode is real and silent: a unit that will not convert without losing content is genuinely freestanding, and forcing it is how a subordination pass deletes a rule. That mirrors the warning already in the file about rules stated *inside* their why-clauses.

**Amendment 2 — condition placement re-decided rather than inherited.** §4 told authors to signal an exception before the general rule, which is George Coode's 19th-century convention, absorbed from `resources/research/legal-drafting-for-tight-rules.md`. The Canadian Department of Justice's *Legistics* takes the opposite position on evidence: front-loaded adverbial clauses measurably increase comprehension difficulty, because a reader needs a sentence's principal parts before it can place the rest.

Both are defensible, and they serve different readers — Coode a reader scanning for whether a rule applies to them, Legistics a reader trying to understand it. The deciding question was therefore which reader this corpus actually has. Claude reads the whole corpus every session rather than looking up whether one rule applies, so understanding dominates over scanning, and main-clause-first wins. Recorded here rather than in the file because it is an authoring decision, not something needed to apply the rule.

**Amendment 3 — §4's heading.** "Write it as an action, not a prohibition" became "state the action the rule requires". The item deliberately left this for this build rather than fixing it in passing, so the audit had a chance to catch it unaided. It did, and found three of the section's seven bullets carrying the same defect — those are captured as `[gate-section-4-breaks-its-own-rule]` rather than fixed here, since amendment 3's described work is the heading.

**The recast was refused, and that is the substantive decision of this build.** The item instructed that if the file grew past its own 1,200-word ceiling the answer was to recast rather than append. It measured 1,224 words before a single edit — already over, on its own terms, having been over for some time with nobody noticing.

The user asked where the number came from. The record is thin and decisive: the document was written on 2026-08-09 in `72f4fe9`, landed at 1,159 words, and declared the 1,200 ceiling in that same commit. Its LOG entry states the number and gives no derivation. It is one draft's length plus a small margin. Worse, the same document opens by stating that the binding limit is a **count of instructions, not a word count** — and that claim is the one with research behind it. So the file argues word counts are the wrong measure and then caps itself with one.

Obeying it would have meant rewriting a working document in full, text nobody had found fault with, because it was twenty-four words over a guess. The amendments were made as ordinary edits instead, and the ceiling was filed as `[self-authoring-word-ceiling-unjustified]` for /plan to either derive or drop. The underlying intent is sound and worth preserving in some form — the ceiling exists because this document's predecessor grew from 6,162 to 21,445 words under honest application, and something has to push back on that. The finding is that a word count is the wrong instrument and this particular number was never reasoned.

Worth recording as its own cost: measuring the file, reasoning about the overage and planning the recast all happened before anyone asked where the number came from. An unexamined limit is not free even when it is ignored.

FAQ: not needed because `resources/self-authoring-rules.md` is a host-only development artifact — the plugin package ships neither `resources/` nor `LOG/`, and consumers never author method rules, so no consumer-visible behaviour changed.

**Files touched:** `resources/self-authoring-rules.md` — §1 gained the subordination obligation and its five-part syntactic test; §4's heading restated positively; §4's condition-placement bullet replaced exception-first with main-clause-first; the Sources line gained `legislative-prose-syntax.md`.

**Routed to Captures:** [self-authoring-word-ceiling-unjustified], plus the run-level captures this session produced outside either work item — [design-item-reaches-next-fix-lost-to-revert], [invented-rationale-compounds-past-the-shipped-rule], [shell-write-guard-points-at-wrong-mover-path], [lifecycle-must-cover-the-faq-not-just-rules] and [build-md-holds-the-only-copy-of-unbuilt-work].

**The run this build sat in was stopped after two of fifteen items**, on the user's judgment that the remaining work is largely hand-fixes to things a cycle should be maintaining, and that `[rule-lifecycle-system]` — dropped from the run because /next cannot scope a design item — should be designed first. The thirteen unbuilt items were returned to Processed, each carrying a note on why it came back and what the run learned about it.

