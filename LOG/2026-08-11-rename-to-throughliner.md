# 08c885b — The Throughliner rename reached and returned unbuilt: its first step is already done, and its ripple is wider than the item states

Not built. This entry records why, so the next session that reaches the item starts from what the grep found rather than from the item's own file list.

**The run reached this item last, having built eleven others.** Two things stopped it, and neither is a reason to abandon it.

**The item's step 1 is spent.** Its migration plan opens with "rename the GitHub repo", on which the 301 redirect and the whole big-bang design depend. `git remote -v` reports the remote is already `FlintcraftTech/throughliner`. The item treats the repository name and the plugin slug as one job; they are two different strings, and only the slug is still wrong. What genuinely remains is the plugin's identity inside the repo — the `sovereign-implementer` slug, the marketplace `renames` map, the folder name, and the positioning rewrite.

**The build-time identity grep — run because CLAUDE.md requires a hook-enforced-identity change to trace its ripple by grepping the literal strings — found files the item's candidate list misses.** `plugin/si-plugin/output-styles/concise-sovereign.md`, whose own filename carries the old identity and so needs a file rename rather than a text substitution; `plugin/si-plugin/scripts/scrub_sweep.py`; `.claude/launch.json` and `.claude/settings.local.json`; and the `plugin/si-plugin/` folder itself. That last one makes this a rename **with a file move in it**, which is a different shape of change from the one the item's Files line describes.

That is scope growth against the described work, and next-build.md routes significant growth to a split rather than an in-flight scope-add — so the run stopped and asked, rather than expanding an identity rename at the end of a twelve-item session. The item's own guidance says the same thing in its own words: this is a large atomic change and shouldn't be swept up mid-run.

**What must not be swept in, recorded because a find-and-replace would take it.** `resources/research/*`, `resources/plugin-behaviour-retired.md` and the LOG are history. Renaming identity strings inside them would falsify the record of what was decided under the old name.

**Two items were filed rather than left in conversation:** [throughliner-repo-rename], the remaining GitHub-side work — which narrowed on inspection from "rename the repo" to "confirm nothing is needed, and reserve the old name so the redirect stays permanent" — and [rename-item-needs-reshaping], carrying the findings above so the item can be re-scoped at /plan instead of re-derived at the next build.

**Files touched:** none.

**Routed to Captures:** [throughliner-repo-rename], [rename-item-needs-reshaping].

FAQ: not needed because nothing shipped — the identity rename's user-facing entry belongs with the build that actually lands it.
