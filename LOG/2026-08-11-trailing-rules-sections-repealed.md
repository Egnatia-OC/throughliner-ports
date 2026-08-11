# [HASH] — Three trailing Rules sections repealed, after checking line by line that the body really restates them [trailing-rules-sections-repealed]

Consolidates three audit findings approved by the user. Each item's own text anticipated this, noting the pattern across the three is one shape.

**Why a restating summary is a defect rather than a convenience.** Two copies of a rule in one document can be edited apart, and nothing mechanical notices when they disagree. It is also the shape the eviction rules name: a clearer restatement that leaves the prior standing has doubled the text rather than merged it.

**The repeal was verified per line rather than performed wholesale**, because a restating section is only safe to delete where the body genuinely restates it — and forcing the repeal is how a pass deletes a live rule. That check changed what happened in two of the three files.

**next.md** — bullets 1 and 2 confirmed restated in its own body. Bullet 3 was **not**, and it is the sharpest case the item named: its substance lives in `next-build.md`, which carried the /done recommendation but not the "never /next, never another build" half or its reason. A cross-doc duplicate is invisible to whoever edits either file, which is exactly why it drifted. Consolidated into `next-build.md`'s Completion step first, then the section deleted.

**setup.md** — only two of six bullets were genuine duplicates, matching the item's "at least two". The other four — use the user's language, follow up on a vague answer, write files once discovery has covered X, ask before a scaffolding choice that is the user's, and the adopt-the-folder framing — had no home in the body at all. They were **moved** into the interview and discovery sections rather than dropped. Repealing them as "duplicates" would have deleted four live rules.

**done.md** — both bullets repealed cleanly. The judgment-steps rule was relocated to the body by [prohibitions-rewritten-as-actions] in the same run, and the routing bullet was already restated at the top of the file.

`next-build.md`'s "Rules during build" survives: it is body content, not a restating summary.

**Files touched:** `plugin/si-plugin/docs-b/next.md`, `plugin/si-plugin/docs-b/next-build.md`, `plugin/si-plugin/docs-b/setup.md`, `plugin/si-plugin/docs-b/done.md`
**Routed to Captures:** none from this item
