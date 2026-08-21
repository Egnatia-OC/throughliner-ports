# d9468f3 — the offer to process a user-raised capture comes after the write, and most of those writes are thrown away

Alex raised this from an instance minutes earlier in the same chat, and gave the shape she wants in her own words: instead of "filing it", *"do you want to capture this now for later, or go straight through to processing?"* Her estimate is the evidence the item rests on — **she would answer processing about 90% of the time**, because the item is in current memory and there is no time like the present, in which case the write need not happen at all.

**The asymmetry in the shipped rules.** The /plan carve-out in `skill-nonspecific-rules.md` puts the offer before any write when *Claude* raises something and after the write when the *user* does. It then gives the reason for the Claude-side placement: *"Asking after the write costs a write that is thrown away, since a capture answered 'work it now' is immediately rewritten as a work item."* That reasoning names no author. It applies to both branches identically, and only one branch was built on it — which reads as something nobody re-examined rather than something anyone chose. Her 90% is what turns a symmetry argument into a measured one: a cost paid rarely is a rounding error, a cost paid nine times in ten is the common path.

**A second failure, separate and Claude's.** In the prompting instance the offer was not made at all — the capture was written, reported as "filing it", and the next message asked about closing. Both the wait and the non-optional "anything else to add first?" clause were skipped. The rule as written would already have caught most of this, so the doc defect and the compliance failure are two things and the item fixes only the first. That is stated in the item rather than left implicit.

**What the grep found that the discussion had not.** The repeal trace turned up a shipped FAQ answer telling consumers that "Claude files it and asks whether you want to dig into it now", which becomes false — a fourth site, and one that would have shipped wrong had the file list come from the conversation.

**Two refusals recorded.** Leaving the user branch alone on write-first grounds: write-first's test is recoverability, and its ideation clause already holds writes while a design is unsettled, so this is that clause reaching one more moment rather than a new exception. And dropping "anything else to add first?" as redundant once the question moves earlier: it was dropped once before and reinstated, and asking earlier is when it does most of its work.

**What is given up, stated rather than discovered.** For the minority answered "capture for later", the wording is discussed in chat before it lands, which is a little less of write-first's put-it-where-she-reads-it.

Rule gate: run — an amendment removing a distinction inside an existing always-loaded rule, so no freestanding rule and no slot spent; the rule gets shorter. The eviction is the file-first ordering on the user-raised branch, repealed in the always-loaded rules, in `plan.md` and in the FAQ answer describing it. Failure evidence is one observed instance plus the user's own estimate that the discarded path is the common one. A hook was considered and refused: nothing mechanical can tell a capture that was going to be processed anyway from one genuinely filed for later.

**Queue changes:** [ask-before-writing-a-user-raised-capture] filed and kept into Processed the same turn, cleared, with a build block.
**Work processed:** kept — [ask-before-writing-a-user-raised-capture].
