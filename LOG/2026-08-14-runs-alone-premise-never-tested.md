# a216873 — plan.md's `Runs alone` justification replaced with the one that survived testing, and the refuted premise recorded

The verification behind this item was done in the planning session that processed it: a throwaway repository, a folder rename half-landed, recovery attempted from both states. Uncommitted, `git reset` then `git checkout -- .` restored the tracked tree exactly, leaving one untracked directory that `git status` named. Committed, `git revert` restored it exactly and reported the rename it was undoing. Both are one command and neither loses anything.

**So the marker's stated justification is false.** "A half-landed rename leaves paths pointing at a folder that no longer exists. Finish it, or do not start it" claims unrecoverability, and git recovers it in both states. That sentence had been quoted forward since `5234ec8`, where it was written to explain a *placement* — why a rename sat last rather than being tagged `[freeform]`. A later planning session read it as a standing constraint, found nothing enforcing it, and designed the marker to enforce it. The marker then shipped across five files. An explanatory sentence became a requirement and the requirement became a feature, without the sentence ever being checked.

**The marker is not repealed, and it survives on the reason the capture itself flagged.** A *running* /next holds file paths in its working file and its scope-lock list, and work that moves those paths underneath a run makes them stale mid-build. That hazard is about a run in flight, not about whether the tree can be put back afterwards, and no amount of recoverability touches it. So the marker is right and its reason was wrong — exactly the outcome the capture said to watch for.

**What shipped here is the correction.** `plan.md`'s section now gives the run-in-flight hazard as the reason, and records the test and its result with a do-not-restore, so this cannot be re-opened a third time.

**SPEC.md was already correct and was deliberately not touched.** SPEC carried the same refuted justification word for word, and the spec-sync gate caught it at the planning session's close and corrected it in that commit, because a false SPEC sentence is a defect fixed when noticed rather than deferred to a build. SPEC and `plan.md` were briefly out of step with SPEC holding the correct reason; this build brought `plan.md` up to it.

**Alex's stronger objection is recorded and remains live as separate work.** In her words: there always *was* a way to run something alone — put a single item above the line only — and Claude was not able to recognise it, maybe because the instructions were unclear. That is correct against the shipped docs. The reason the obvious answer looked unavailable is the method's own below-the-line rule, which forbids shelving unblocked work, so isolating one item requires a move the rules refuse. That points at the below-the-line rule rather than the marker, and it is not closed by this build.

**Files touched:** `plugin/throughliner/docs-b/plan.md`
**Routed to Captures:** none

Rule gate: not needed — no rule authored or amended. A shipped rule's stated justification is replaced with the correct one, and the refuted premise recorded as tested.
