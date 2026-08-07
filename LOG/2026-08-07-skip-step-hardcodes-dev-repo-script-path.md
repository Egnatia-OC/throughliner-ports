# 5993a10 — The queue mover's hardcoded repo path corrected in both docsets, including the frozen one

`plan.md`'s skip-to-defer step instructed `python plugin/si-plugin/scripts/reorder_queue.py …`. That path resolves only inside this development project. A consumer has no `plugin/` folder, so a session following the instruction literally fails.

**Both halves of the original report were wrong, and both were established rather than inherited.** The report also named `done-plan.md`'s close reorder as carrying the same path — it does not; that doc says to locate the script under the plugin root and all three of its invocations use `<plugin-root>/`. And the report's confident *"docset A's copy is correct too"* was false: `docs/plan.md` carried the identical hardcoded path in its own skip-to-defer text. **Two broken occurrences, not one.**

The wider grep was run at processing and did not need repeating: seven invocations across both docsets, the templates and the skills use `<plugin-root>/` correctly; two used the repo path. The only other repo-shaped paths in shipped docs are `resources/research/` and `resources/testing/`, which are project-root-relative and correct.

**What makes it a slip rather than a pattern, which is the useful part:** `plan.md`'s own keep-step, about a hundred lines above the broken line, already used `<plugin-root>/scripts/…` correctly. The right form was established in the same file and then not carried to the second invocation — in both docsets.

**Why nothing caught it here:** in this project the hardcoded path *works*, because this project genuinely has that folder. The one environment where the method is exercised most is the one where the bug is invisible by construction; it can only be found from a consumer project or by reading.

**Docset A was in scope by the user's call.** The freeze bars development, not correction, and a frozen fallback whose instruction fails in a consumer project is not a safe fallback — which is the entire reason A is kept. This is also the cleanest correction the freeze could meet: a substring change with no new prose authored, so none of the register risk the freeze exists to prevent applies.

Verified after the edit: a repo-wide grep for `plugin/si-plugin/scripts` returns nothing.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`, `plugin/si-plugin/docs/plan.md`
**Routed to Captures:** none
