# [HASH] — Five prohibition-only rules rewritten to state the action they require [prohibitions-rewritten-as-actions]

Consolidates five findings of the prohibition-and-subordination audit, approved as a set by the user. Consolidating by fix-shape rather than by file is Claude's recommendation, agreed by them: one criterion applied once across its instances, which is also how the audit found them.

**The criterion is the user's own principle:** anything described in terms of what not to do only means the rule of what TO do was never adequately described. A prohibition is a signal to go back and specify the action, not a wording to polish; where no action can be stated, that is the finding.

**The five, each with its positive form already available — so this was rewording, not redesign.**

1. **The authoring gate's §4** — the sharpest, because this is the rule that polices the failure, demonstrating it at the moment it is forbidden. Its heading reads "write it as an action, not a prohibition" and its own bullets were "Avoid provisos", "Don't mix conditions and exceptions in one sentence", "Don't hide exceptions". A rule that cannot be stated in its own form is evidence for the principle rather than an exception to it. Now: state the rule bare and put the qualification in structure; one idea per provision, a sentence each; put every exception where a reader will meet it.
2. **done.md's judgment steps** — forbade skipping them even if the user says "just commit", with no positive statement anywhere in the done family. A session reading only that knew one path was closed and none was open. Now stated positively, and moved into the body because [trailing-rules-sections-repealed] deletes the section it lived in.
3. **done.md's meta-description ban** — the positive (show the message itself verbatim) was inferable from the block above but never stated.
4. **next-build.md's "No pre-edit preview" heading** — a heading is what a skimming session sees and how a procedure doc is navigated, so a prohibition there is the version most likely to be read and least likely to say what to do. Now "Make the edit, then say what changed."
5. **setup.md's first-item block** — one "yes" row against four "no" rows, governing the first thing a brand-new user ever sees written into their own queue. The positive covers all four, and the refusals collapse into one clause naming the tempting case.

**Overlap handled deliberately.** done.md's judgment-steps line is both a prohibition and a member of a restating Rules section, and both items were told to say what they left the other. This one wrote the positive form into the body and left the redundant bullet for the repeal.

**Files touched:** `resources/self-authoring-rules.md`, `plugin/si-plugin/docs-b/done.md`, `plugin/si-plugin/docs-b/next-build.md`, `plugin/si-plugin/docs-b/setup.md`
**Routed to Captures:** none from this item
