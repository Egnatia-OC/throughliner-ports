# 32675a3 — Walkthroughs end at the observable, and another project's steps are filed rather than driven

Two clauses from one recorded stall. A `[user]` item had proved what it existed to
prove and then kept going: its remaining steps were cleanup, in a different
project, and a run waited on them. The user's own words at the time were that the
hand-over was the mistake — the verification had already passed.

**A walkthrough ends at the item's observable.** Cleanup after the test gets its
own item rather than trailing steps, because a walkthrough that carries on past
the thing it was proving has no point anyone can check it against.

**A step requiring action in another project is filed, never driven.** No session
writes another project's files, so walking the user out of this project is where a
drive stalls with nothing here able to finish it. The run files it and continues.

**Driving cleanup last was refused on the item**: the stall is the leaving-the-project,
not the ordering. **A cross-project write to do it for the user was refused** by a
standing rule.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md` (a third
subordinate clause on the walkthrough requirement);
`plugin/throughliner/docs/next.md` (the walk-through branch).

**Routed to Captures:** none from the build itself.

**Applied within the hour, to the very item that produced it.** The walk-through
pass later in this run reached [cycles-due-check-verification], whose record
showed its observable check passed on 2026-08-26 with only cross-project cleanup
outstanding. Under these clauses it closed as done and the cleanup split into
[cycles-fixture-cleanup] — which is what that item's own previous record had asked
the next session to do.

Rule gate: run — two amendments: the walkthrough-authoring requirement in skill-nonspecific-rules.md and next.md's walk-through branch; parents named; nothing evicted.
