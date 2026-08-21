# 35261b5 — The close files its forward advisory about half the time, measured from git after Alex reported it had stopped

Alex reported that forward advisories seemed to have stopped over the last couple of days and that she had been having to ask for them, where Claude used to file them unprompted. Checked rather than taken, and it holds — but what stopped is narrower than the report, and the difference is the finding.

**The recommendations are still being made. They have stopped being written down.** Yesterday's close made a concrete one — the text Alex carried by hand into this session, that planning rather than a build is where it should start, naming the overlap between [setup-migration-gate-is-epoch-3-shaped] and [convert-cleared-items-to-build-blocks]. That is exactly what the advisory exists for. Nothing reached the queue, so it survived only because she pasted it.

**Measured across the last five closes: three filed nothing.** `d9468f3` cleared the previous advisory and filed none, `b485ee3` filed one, `cb50e2b` cleared and filed none, `7e3c1c8` filed one, `dc52025` cleared and filed none. Each close deletes the consumed note and only sometimes adds a new one.

**The step is intact, which rules out the obvious explanation.** Nothing was repealed or reworded: `done.md` still carries "File the forward-recommendation advisory" in full, with the reserved `[forward-advisory]` slug, the write-conditions-not-counts rule and the flavour deltas. This is a correctly worded obligation with a stated site that does not fire.

**The likeliest cause is position, and it is measurable.** The step sits at line 880 of a 925-line file — the tail of the largest document in the method, reached only after 7,443 words of it, with the record already written and the commit in sight. That is the toll [done-md-carries-other-flavours-material] measures.

**The fix is a required artifact, which is the one shape with teeth here, and it is an amendment rather than a new mechanism.** The close writes `Advisory: filed — <slug>` or `Advisory: not needed — <why>` into its session record. The parent is explicit: the `Rule gate:` obligation was itself authored as *"the FAQ-sync rule's shape extended to a second subject, not a new obligation"*. This is the third subject on that shape, for the same stated reason — a required artifact turns a silent omission into a visible one, and "not needed because the recommendation was generic" is a claim a later reader can disagree with.

**A mechanical check was refused.** Nothing can detect whether an advisory was *owed*, because the trigger is whether this close made a concrete recommendation and that lives in the conversation. A check firing on every advisory-less close would fire wrongly every time the recommendation was legitimately generic — the cry-wolf shape this project has repealed measures for twice.

**The cost is stated rather than discovered: this one ships.** FAQ-sync and the rule gate are both host-only, so consumers write neither line. This is the first close-line obligation a consumer pays. Admitted anyway, because the feature it guards is one they have and are silently losing.

**This is the sixth instance in the corpus of a correctly worded rule with a stated site failing to fire**, after the provenance rule, the file-the-blocker rule, the INBOX-opening step, the subagent-cost rule and the gate's own halt instruction. The corpus's own conclusion about that class already stands: "state the rule again, or state it harder" is not a candidate direction, which is why this reaches for an artifact instead.

**One correction made in the session and worth carrying.** The placement argument given to Alex was that /next would build exactly one item because [rename-docs-b-folder] sits second and carries `Runs alone`. Inserting this item pushed the rename to third, so a run builds two. The placement stands — this is the more urgent of the two — but the arithmetic offered for it was wrong when it was offered.

**Queue changes:** [advisory-step-does-not-fire] filed and kept into Processed at the top of the cleared region, ahead of [split-action-defeats-the-bands-in-aggregate], with a build block and three refusals recorded. Non-default placement, narrated at the time.
**Work processed:** kept — [advisory-step-does-not-fire].

Rule gate: run — the disposition was written onto the item at the keep-step, with Alex present. Admitted as a third subject on the existing close-line obligation shape, subordinate to a mechanism already shipped twice, sited in a fetched procedure doc so no always-loaded slot is spent. Nothing evicted. Failure evidence is three misses in five closes measured from git, plus one instance observed end to end.

FAQ: not needed because nothing a user does changes — a consumer sees one more line in a session record and acts no differently.
