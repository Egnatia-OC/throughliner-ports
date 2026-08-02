# b931278 — Audited docset B against docset A and filed twelve fidelity findings

Docset B was authored in a single run by subtraction from docset A, and only one of its eleven docs — next.md's pre-flight — was ever independently judged. The author and the judge were the same session, which is exactly the weak spot the authoring checkpoint flagged at the time. This audit was queued to close that gap while docset B is still inert, before phase 3's rezip makes it govern live sessions, because fixing a file no session loads is cheap and fixing one that steers real sessions is not.

All eleven doc pairs were read against three criteria: every rule in A survives in B or was deliberately dropped; no rule's scope silently narrowed or widened; no typed block asserts something the prose didn't say. Twelve findings came out, all approved as drafted and all filed to Unprocessed.

The most consequential is that docset B nowhere defines what makes an editor "recorded" — docset A states it twice, as any value other than the literal `not recorded` — while docset B's own setup still writes that literal string when the user skips the question. So a B session can read a skipped field as a recorded editor and send a pointer the user cannot open, with no copy of the text in chat. Second is a class rather than a single loss: docset A carries twenty-seven explicit `Scope:` clauses and B carries two, and at least one of those drops real reach information, the spec-sync gate's statement that its plan-close branch covers setup and method-doc-only sessions. Third, the capture line-format block — the one shape all three hooks parse — is malformed in B and positions the user-credit and commit stamp in a layout the prose never states. The rest are individually smaller: a dropped scaffold instruction, a dropped approval step, a widened trigger, several rules whose supporting mechanism or exception was shed with the why-clause it travelled in.

The audit's premise held up. Subtraction is lossy by design, and the losses that matter were not the why-clauses it meant to shed but rules that had been *stated inside* those clauses — an exception at the end of a sentence, a definition in a parenthetical, a mechanism named in a subordinate clause. That is the pattern to carry into any future subtraction pass: the risk is not in what a paragraph argues, it is in what a paragraph quietly defines while arguing.

One divergence went the other way and is recorded so it is not later read as drift: docset B corrects a wrong within-doc cross-reference that docset A gets wrong, pointing at sub-step 2 where A points at sub-step 3.

**Files touched:** read-only — `plugin/si-plugin/docs-b/` (11 docs) against `plugin/si-plugin/docs/` (11 docs). The audit edited nothing.

**Routed to Captures:** 12 — docset-b-editor-recorded-definition, docset-b-scope-clause-loss, docset-b-setup-log-dir, docset-b-capture-format-block, docset-b-paste-targets-rule, docset-b-spec-sync-quote-rule, docset-b-file-structure-trigger, docset-b-spec-change-routing, docset-b-handmade-close-approval, docset-b-planning-stage-red-flags, docset-b-midsession-capture-priority, docset-b-user-prereq-derivation.

**Approval outcomes:** all twelve findings approved as-is; none dropped or reworded.
