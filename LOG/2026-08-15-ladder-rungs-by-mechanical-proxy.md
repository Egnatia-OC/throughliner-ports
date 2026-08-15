# [HASH] — The ordering ladder cut from six rungs to three, every one mechanical

The user's own experience is the evidence: across several planning sessions she watched Claude struggle to reason across a long queue, ran a tersification in a separate chat and replaced QUEUE.md wholesale to buy about ten percent — and reported that nothing helped as much as ordering by line count. Her proposal was line count as a stand-in for design completeness, and file order as a stand-in for decay.

**One half rests on a stronger leg than the one she gave it, and the correction matters.** Line count is weakly supported as a proxy for design completeness and was partly contradicted the same session: of eight items processed in length order, the two that could not be kept at all were the longest and the fourth-longest. At the top of the distribution, length tracks repeated enrichment without resolution rather than readiness. But the ordering worked anyway, for her second reason — long items are what make the queue expensive to reason across, so processing them first is what shortens it fastest. That benefit does not depend on the proxy being accurate. Resting the rung on design completeness would make it falsifiable in a way it does not need to be; resting it on cost-of-reading makes it true by construction.

Three rungs remain: an uncleared red flag in Unprocessed, unblock-potential, longest first by line count. **Rung 3 is total**, which is the structural point — longest-first never exhausts, so nothing can sit beneath it, and the ladder is really a default with two overrides. That is what killed file order, her own finding, along with the observation that putting file order first would kill longest-first instead.

Three rungs were deleted, each for a stated reason. *Unsticks a stalled cleared region* — the digest already surfaces placement contradictions at the opening, directly to the user, and the rung was the convoluted second route to the same information. *Cheap to settle* — cancelled out by recent work, and its stated criterion contradicted itself, calling itself "checkable, not judged" while including subject matter, which cannot be checked without reading every item's prose. *Decay*, then *file order* — decay collapsed into file order because Unprocessed is only appended to, and file order then died as unreachable. **The consequence, named rather than left to be discovered: staleness is no longer an ordering concern at all.** It keeps a surfacing route — the digest flags an item whose premise cites shipped work, at the opening — so the concern is not lost, only removed from ordering.

**Unblock-potential is kept deliberately, and the reason must survive any later compression pass. In her words: this is reasoning, but of a type Claude excels at — running a dependency graph.** That is the line between what stays and what was cut: following citations between items is mechanical in the way that matters; judging whether two items feel related is not.

**The built wording then failed and she corrected it.** The first version lost both mechanisms — rung 2 read as picking a single item rather than ordering the section by citation count, and rung 3 said "longest first" without naming line count, which is the whole reason the rung is cheap: an entry's last line number minus its first, one subtraction off numbers already in front of you, with nothing counting words and nothing judging how finished an entry looks.

Two defects found by her questions while settling this were fixed in the same build: the digest's placement-contradictions block stated no caveat despite matching a fixed set of known phrases, and rung 5's criterion contradicted its own claim to be checkable.

**Files touched:** `plugin/throughliner/docs-b/plan.md`, `plugin/throughliner/scripts/queue_digest.py`, `SPEC.md`

**Routed to Captures:** none

Rule gate: run — admitted, and it is a **net subtraction**: three rungs and one offer are deleted, one caveat sentence is added to a script's output, and the ladder's prose shrinks by more than half.

FAQ: not needed because the ladder is internal and never offered — the user sees one line naming the order used, unchanged in form.
