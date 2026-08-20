# [HASH] — An item finishing outside this project must name what would show it done, or say nothing does

Filed during a /next walk-through at the user's instruction. Mixed authorship: she raised the question that found it — why the site was being edited from here when it belongs to another project — and the diagnosis is Claude's.

[report-url-404] was a `[user]` line waiting on a page existing at flintcraft.tech/report, work on a different project. The page had been up for some time. Nothing here learned that, and the item sat in the cleared region as ready work until a walk-through fetched the URL and found it live. No harm that time, and that is not the point: the item recorded an observable check, so the walk-through ran the check instead of asking whether the work was done. The cost was one wasted run slot and a moment of reasonable confusion about whether Claude was reaching into another project.

**The checking side already works and the defect was upstream of it.** The walk-through rule already checks the world where an item names an observable result. Nothing required an item to *carry* one when one existed.

So at the keep-step, an item whose completion happens outside this project **names what would show it done** — a URL, a file, a branch — or states plainly that nothing observable exists. **The second half carries as much weight as the first**, and it is the part that gets left out: it is what tells a later run to ask rather than check, instead of leaving it to guess which case it is in, and it makes "waits until the user mentions it" a stated design rather than something that reads like an oversight.

**Notification is refused rather than merely unbuilt**, on [inbox-delivery-unconfirmed]'s own finding: mail is fire-and-forget in both directions, so a notice nobody must read moves the problem rather than closing it. That refusal is now operative text in `feedback-and-inbox.md`, so a later session meets the argument rather than the conclusion.

The general shape stays honest: an observable check rescues cases where "done" leaves a trace a fetch or file test can find. It rescues nothing where completion is visible only to the user or inside another project's records — the larger class. That is why the say-so-plainly half exists.

**Files touched:** `plugin/throughliner/docs-b/plan.md` (the keep-step clause) and `feedback-and-inbox.md` (that work finishing elsewhere is never learned by notification). SPEC.md is not listed — its sentence was rewritten in the planning session that kept this. No FAQ entry: this changes what a queue item carries, not anything the user does.

**Routed to Captures:** none.

Rule gate: run — admitted as an amendment to the existing check-the-world clause, sited at the keep-step where the item is authored rather than restated where it is read; no always-loaded slot and no freestanding rule. **Nothing is evicted, stated plainly.** Failure evidence is one instance, [report-url-404], which is thin and carried by the amendment shape rather than by weight of cases.

Tick: done, confirmed by reading both clauses back; no code, so no suite applies.
