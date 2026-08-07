# [HASH] — The editing-state closing marker gated on adoption, by separating the two jobs one SPEC check was doing

**The asymmetry, verified by reading both hooks.** `pre_tool_use.py` returns early when `SPEC.md` is absent, so the **opening** marker is written only in adopted projects. `post_tool_use.py` wrote the **closing** marker *before* its `SPEC.md` check. So in a folder that never adopted the plugin, every edit left a closing marker for a session that never opened one — `.throughliner/editing-<session>.json` files accumulating in the user's unrelated projects, uncovered by any gitignore, since /setup is what adds that entry and those folders have never run it.

**Which side moves did not need deciding, and that is recorded so it is not re-opened.** SPEC already states the intended behaviour in the editing-state contract's own limits: *"the signal only exists where the plugin is installed and the project adopted."* The documentation is right and the code contradicted it, so the code moved.

**The thing the fix must not break, and didn't.** The closing marker's placement carries a deliberate comment: it is written before the **QUEUE.md** gate because the signal covers every edited document, not only the queue. That reasoning is correct and survives untouched. The actual bug was that a single `SPEC.md` check was serving two different jobs in one function — "is this project adopted" and "does the queue lint apply" — and only the second was gating anything, because it sat below the marker write. The fix separates them into a named `is_adopted` read, gates the marker on adoption, and leaves the lint gate exactly where it was.

Kept as its own item rather than folded into the documentation sweep it was found in, because it changes a **published contract another application is built against** and deserves its own scrutiny and its own entry.

The hook schema checks pass after the change.

**One consequence worth stating for the companion app:** the contract is now exactly what SPEC always claimed — the signal exists only where the plugin is installed and the project has run /setup. A reader meeting no `.throughliner/` folder treats it as "nothing is happening", which is also what every non-plugin project looks like. This has not yet reached a consumer; it needs this commit and a release first.

**Files touched:** `plugin/si-plugin/hooks/post_tool_use.py`
**Routed to Captures:** none
