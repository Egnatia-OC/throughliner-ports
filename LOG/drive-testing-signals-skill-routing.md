# 96166c6 — Before driving a verification, check whether it already exists as tracked work — a yes/no test, not a suspicion

The trigger is a check with a yes/no answer, not a judgment about whether an urge is suspect. Before driving or walking through a test: **does this work already exist as a tracked item?** Already tracked → stop driving it and route it to /next, which walks a `[user]` item live and carries its findings through the proper close. Not tracked → the planning-session file gate already governs it, so the work cannot happen unremarked, and no new rule is needed.

**Why the trigger is that and not "am I driving testing?", which is where the original capture pointed.** Two sessions of the same shape got opposite calls, and this check is the difference between them. In the first, the verification **was already a `[user]` work item in Processed**, and driving it in chat bypassed a home it already had — so its findings scattered as loose captures instead of flowing through the close. In the second, nothing was tracked: a stuck lift-condition and a small instrument that cleared it. **A rule of "always route it into a skill" would have made the second case worse**, re-creating the exact cycling failure it was fixing, since the condition had already rolled forward across two advisories and two restarts precisely because it kept being deferred.

Recorded at that length because the intuitive rule is the wrong one and would otherwise be re-proposed.

The second limb the original capture was right about survives: this is the plan/build boundary breaking in the less-noticed direction. The familiar worry is planning leaking into an execution session; this is structured work being *executed* with no skill around it, so none of the structure applies. Same family as under-filing `[user]` work — the work happens, but untracked, so nothing records or closes it. The failure was never informality; it was bypassing existing structure.

Placed in the routing-and-discipline rules where the plan/build boundary is stated, with the file gate named as what covers the untracked case — a prohibition needs its sanctioned alternative named in the same breath — and repeated in plan.md, where it fires in practice.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/docs-b/plan.md`

**Routed to Captures:** none
