# [HASH] — `Blocked by:` reserved for genuine blockers, with ordering preference carried by placement plus a sentence

This came from the Understudy project, reporting a session that re-pointed a held item's `Blocked by:` at a different item rather than lifting it, reasoning that building on unconfirmed work would make faults hard to attribute. That is an ordering preference, not a dependency.

**Understudy then withdrew their own worked example**, and the item demanded a fresh case or deletion. Their two held items were not a sequencing preference dressed as a dependency: both named a blocker that LOG records as built and never verified, and `done-plan.md` says plainly that built-alone is not enough to clear a dependent. The placement was correct; what was wrong was the argument given for it.

**The fresh case came from the processing session itself.** `[redundancy-audit-did-not-cover-subdocs]` is an audit that should run after a set of eight redundancy builds, because it audits the docs those builds change. `Blocked by:` names one slug, so expressing that as a dependency would have meant picking an arbitrary member of the set — and worse, it would have pushed the item below the readiness line, out of the region a run works.

**But the case argues against a new field rather than for one, and that is the finding.** The intent was carried instead by placing the item last in the cleared region and writing one sentence into its prose saying what it should follow. That survives a reorder, because the sentence is the relationship and the position is only where it runs — consistent with the always-loaded rule that position never encodes a relationship, rather than in tension with it. It worked: the audit ran last in today's run, after the eight builds it audits.

**So the real defect in both cases is the same, and it is not a missing field.** It is that `Blocked by:` gets reached for to express ordering, and `Blocked by:` sends an item below the line where the user cannot see it during an ordinary run. That is precisely what cost Understudy two designed items and their user's confidence that a feature was queued at all. A field would need parsing by the lint, the digest and the run — the three-sites cost this project already documents — to buy something a convention buys for nothing.

**Rescoped from a new field to a stated convention**, and shipped rather than host-only, since the original instance came from a consumer project. Stating the reserved half is what stops the misuse, and the misuse is the whole harm.

**A reply is owed to Understudy on their correction**, and is offered at this close.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`
**Routed to Captures:** none

Rule gate: run — admitted as an amendment to the existing `Blocked by:` rule, written as a subordinate clause of it, so no slot is spent. Two pointable instances, one from a consumer project and one from the processing session. Not hookable: the lint can see that `Blocked by:` names a slug, never whether the relationship it claims is real.
