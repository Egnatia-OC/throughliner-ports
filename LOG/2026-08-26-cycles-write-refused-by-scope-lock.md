# 3b094b5 — CYCLES.md joins the scope-lock's standing planning list, so the cycle-authoring rule can run where it fires

plan.md's keep-step tells a planning session to write a cycle definition into `CYCLES.md` with the user present, and `pre_tool_use.py`'s standing planning surface did not include that file — so the write was refused and the session correctly filed the definition as work instead. Two documents disagreeing, one of which had to move.

The rule won and the lock moved. Rewording the keep-step to file a definition as a build was refused at planning: a build settling a cycle's observable is exactly what the with-the-user-present instruction exists to prevent. The consumer project that hit this named the contradiction itself, unprompted, which is the refusal working as designed even while the rule behind it was wrong.

The build added `CYCLES.md` to `quiet_files` with a one-line reason beside it, and updated the three places the list is written out in prose: the rule-4 docstring, `_is_plan_quiet_path`'s docstring, and the denial message a refused session actually reads. plan.md's standing-list bullet gained the file too. One thing the item expected was not there: `skill-nonspecific-rules.md` carries no written standing list, so there was nothing to edit — recorded rather than silently skipped.

Verified by driving the hook directly rather than by attempting the guarded write in this project: a planning-shaped payload naming `CYCLES.md` was allowed, and one naming an out-of-list path was still denied.

**Files touched:** `plugin/throughliner/hooks/pre_tool_use.py`, `plugin/throughliner/docs/plan.md`.
**Routed to Captures:** none.
**Depth:** short.
**Tick:** done, confirmed.
Rule gate: run — an amendment to the scope-lock's standing planning list, its parent rule; nothing evicted — the list gains the one member the keep-step's own cycle-authoring rule already names.
