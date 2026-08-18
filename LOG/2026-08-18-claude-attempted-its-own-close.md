# [HASH] — Claude attempted to run the close itself, and the search halved the item by confirming the explanation was right

The user brought a screenshot from another project: Claude wrote "Now closing the session", attempted the close command, got **"Failed to run skill"** in red, and said *"I can't run the close myself — it's reserved for you to invoke."*

Claude's first reading filed two defects, the second being that the explanation was a true-sounding rule standing in for a mechanical cause — the invented-rationale family. **A search settled it the other way and that half is withdrawn.** All five skills carry `disable-model-invocation: true`, whose documented meaning is exactly that Claude cannot auto-invoke them and only the user can, used for work with side effects or user-controlled timing. The explanation *was* the mechanical cause. The withdrawal is kept on the item rather than deleted, because the wrong reading is the intuitive one and a later session would re-file it.

**One defect survives.** The plugin ships that flag and no procedure doc says so, so a session attempts the invocation and shows the user a red failure mid-close, where a non-coder has least context. The fix has a parent and costs no slot: the communication rule already says to run every command you can run yourself, handing one over only in the cases the rules name, and it gains one named case.

The search also surfaced an open Claude Code issue reporting that skills with that flag cannot be invoked by the user either — refuted for this setup in the same session, since the user typed the plan command and it ran. Nothing filed.

**Queue changes:** [claude-cannot-invoke-its-own-skills] filed from a user-supplied screenshot, halved at processing, cleared.
**Work processed:** kept — [claude-cannot-invoke-its-own-skills].
