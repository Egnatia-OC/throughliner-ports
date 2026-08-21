# [HASH] — Both branches of the /plan carve-out now ask before the write, and the process-now route writes no capture at all

Build entry. The planning entry that processed this item is
`2026-08-21-ask-before-writing-a-user-raised-capture.md`.

**Why this was worth doing.** The carve-out had a split placement: a Claude-raised
capture asked before any write, and a user-raised one was filed first and then offered
process-now-or-carry-on. Where the answer is process-now — which the rule itself
recommends, and which the user estimates is the common answer — the capture is
immediately rewritten as a work item, so the write was thrown away most of the time.

**What was built.** Both branches ask before the write. A user-raised item is offered
*capture it for later, or process it now*, still recommending process-now, with the
"anything else to add first?" clause preserved. Where the answer is process-now, nothing
is written as a capture at all: the item goes through present-and-interview and is
written once, as a work item. In `plan.md` the step's own title was changed too —
"Process-now offer after a user-filed capture" asserted the write had already happened.

**Why the "anything else to add first?" clause survives the move rather than becoming
redundant.** Asking before the write puts the question at the moment the user is still
mid-thought, which is exactly when that clause does its work. It was dropped once before
and reinstated, because it stops an idea being closed off early — so dropping it again
was refused explicitly.

**What is given up, stated rather than discovered.** Write-first exists so text reaches
the document where the user reads it in place rather than as a chat paste. Asking first
trades a little of that: for the minority answered "capture for later", the wording is
discussed in chat before it lands. That is not a breach of write-first, whose test is
recoverability and which already carries an ideation clause holding the write while a
design is unsettled — this is that clause reaching one more moment, not a new exception
to the test. Leaving the user branch alone on write-first grounds was refused on exactly
that reading.

**The FAQ hit was found by grep and would have been missed.** Its answer told consumers
that "Claude files it and asks whether you want to dig into it now", which becomes
false. That is a sync of an existing answer rather than a new entry, so no index line
changed.

`grep "File it first"` across `docs/` returns nothing. `FAQ/faq.md` is byte-identical to
its template.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md`,
`plugin/throughliner/docs/plan.md`, `plugin/throughliner/templates/faq-template.md`,
`FAQ/faq.md`.

**Routed to Captures:** none from this item.

**FAQ: updated** — the existing answer reworded to asks-then-files, with one clause on
nothing being written twice.

Rule gate: run — admitted as an amendment removing a distinction inside an existing always-loaded rule, so no freestanding rule and no slot spent; the rule gets shorter. **The eviction is the file-first ordering on the user-raised branch**, repealed in the always-loaded rules, in `plan.md` and in the FAQ answer that describes it. Failure evidence is one observed instance in this session plus the user's own estimate that the discarded path is the common one. **A hook was considered and refused:** nothing mechanical can tell a capture that was going to be processed anyway from one genuinely being filed for later.

Depth: short. Built and confirmed.
