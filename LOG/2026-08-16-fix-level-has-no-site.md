# [HASH] — The keep-step now asks what level a fix belongs at, merged with the research clause into one rule

The rule gate fires at the wrong end. It runs "before adding any rule to the method's own text", so it only engages once someone has already decided a rule is the answer. Its fourth admission question is exactly the right one — could a hook do it instead — and it can never be reached from the other direction: looking at a broken instance and choosing how to fix it. So the default was whatever the item's author reached for first, which is the instance.

Two instances in the session that filed this, both caught by the user rather than by any check. The provenance defect was diagnosed correctly and then proposed as a text cleanup, leaving untouched the lint that certified the bad shape. The measurement defect was proposed as a replacement item until she supplied the rule — build the tool, then audit with it — which became `[tool-build-implies-an-audit]`.

Not a hook, and it cannot be one: whether an item is fixing an instance of a general problem is a judgment, not a pattern.

The item required a build-time check of whether four keep-step clauses collapse, and that check is the substance of this entry. Three of the four were in this run. This clause and `[research-cited-not-restated]` **do** collapse: both ask what must be settled before the build can be described, so they ship as one parent with two subordinate units and spend one slot instead of two. `[tool-build-implies-an-audit]` does **not**: it fires after the build is described, at placement, and merging it would put a placement rule under a description parent. The fourth, `[files-line-names-excluded-files]`, sits below the readiness line and was not in this run; the session that builds it should run the same check against what is now in place.

The answer to the level question shows up in the Files line, which already names a doc for a rule and a hook file for a hook — what was missing was the question, not a field.

**Files touched:** `plugin/throughliner/docs-b/plan.md` (the research clause and the fix-level clause merged into one keep-step rule with two subordinate units, plus the statement that the level question has no detector and cannot have one).

**Routed to Captures:** none.

**Rule gate:** run — admitted as a subordinate unit on `plan.md`'s existing keep-step, merged with the research clause rather than added beside it. Nothing evicted, and the merge means the two together spend one slot. Shipped rather than host-only: a consumer processing an item hits the same choice between fixing one occurrence and writing a rule into their own `CLAUDE.md`. Failure evidence is the two instances above, both surfaced by the user.

**FAQ:** not needed because the clause changes how Claude describes an item, not what the user does.

**Also in this chat.** Carried here as the run's final entry because `[also-in-this-chat-has-no-home-in-a-multi-item-close]` records that this section has no defined home when a close writes ten of them.

A `/rescan` ran after the build and filed `[repeal-has-no-ripple-trace]` — the diagnosis of why this run stopped twice to grow scope, and a gap the existing grep-the-ripple rule does not reach.

A design conversation then ran across several turns and produced three captures. The user proposed that the vocabulary rule over-prescribes twice: it bans a term outright where the term might be worth teaching once, and it dictates the *form* of the teaching. Her words on the first: *"a little bit of learning is ok... arguably NO jargon at all is even trickier (and possibly impossible)."* On the second: *"I don't know that we need to be prescriptive to Claude how it explains things, demanding it show first."*

**A correction that removes the only evidence behind a shipped rule.** The rules file justifies its show-first instruction with an account of something explained repeatedly until somebody opened a file and pointed. Asked about that moment, she said: *"no that just happened to be when I relented."* So the sole justification is a coincidence Claude recorded as a cause, and it stood as evidence until she was present when it was quoted back. Filed as `[vocabulary-rule-has-no-teaching-branch]`.

Her replacement design became `[teaching-method-looked-up-on-demand]`: rather than fixing a teaching form in advance, look up how to teach the specific concept at the moment an explanation fails, and choose the best method that survives the channel — including pointing at the shortest source whose text Claude can actually read before recommending it.

**And a correction to how Claude was behaving during that conversation**, which became `[ideation-loop-holds-the-write]`. Six writes went into two captures while their designs were still moving, each a full re-authoring of unfinished text. Her proposal: Claude offers to capture and holds the write until the user says they are done. Applied to the proposal itself — it was held, then written once, at 354 words against 634 and 586 for the two written incrementally. Recorded in the item as direction rather than proof, since it is one instance and still over its ceiling.

The queue lint's advisory in this chat reported flags under the *old* installed hook throughout, since the host runs a frozen copy; under the code committed here the same queue reports clean.
