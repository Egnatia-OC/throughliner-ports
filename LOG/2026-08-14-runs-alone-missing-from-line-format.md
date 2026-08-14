# [HASH] — `Runs alone` added to the canonical line-format block, and its second definition replaced by a pointer

The always-loaded Captures section documents every marker a work item can carry — `Blocked by:`, `Red flag · State:`, the flavor tags — and omitted this one, in the one place a session goes to learn what a work item may contain. That block is described in the same doc as the exact shape the hooks parse against, which is what made the omission the sharper half of the finding.

`plan.md` defined the marker at the authoring site and `next.md` at the consumption site, both carrying the same "binds /next and nothing else" caveat and the same not-`[freeform]` distinction. The definition now sits once, at the authoring site, and `next.md` keeps only the run-bound mechanics — which item stops a run, which is built then ends one — plus a pointer.

**This waited on `[runs-alone-premise-never-tested]` and was lifted when that resolved in-session.** Writing the marker into the canonical block is precisely wiring it into one more site, and consolidating its two definitions is rewriting text a repeal would have deleted. With the premise refuted and the marker surviving on the run-in-flight hazard instead, nothing here was at risk of being torn out. It was placed immediately after that item so the corrected reason landed first.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, `next.md`
**Routed to Captures:** none

Rule gate: not needed — no rule authored or amended. An existing marker is added to the canonical line-format block it was missing from, and a duplicated definition is stated once.
