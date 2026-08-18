# dc52025 — the hook refuses a Write onto an existing log entry, so a collision stops being silent

Processed ahead of its turn on the user's instruction, because the close following this session writes many entries at once — the largest exposure this defect has ever had.

The item had already ruled out the obvious move. A rule saying to append `-2`, `-3` on a name collision exists and was skipped, and restating a skipped rule is a failure shape this project has named twice. So this was a question about what level the fix belongs at, and the answer is the hook.

`pre_tool_use.py` refuses a Write whose target is an existing file under `LOG/`, naming the collision and pointing at the next free suffix. Mechanical, unskippable, and invisible on correct work: a genuinely new entry filename does not exist, so it never fires on a correct close. Narrow by design — Write only, never Edit, because a close legitimately edits the index and appends tails to existing entries through Edit.

The second shape was refused. A staging check catches what the hook prevents and fires at every close including all the correct ones, which is the cry-wolf pattern this project has repealed measures for twice.

The item's closing paragraph — that the Write tool appeared not to refuse an overwrite as documented — stands exactly as written: recorded, unverified, and not built on.

It is a hook change, so it does not protect the close that settled it. That close checked collisions by hand instead, and said so rather than implying cover it did not have.

Rule gate: run — one refusal added to the existing write guard, which already refuses writes by path. One alternative refused.

**Queue changes:** [log-entry-write-can-clobber-an-existing-entry] kept into Processed and placed at the top of the cleared region so it ships first.
**Work processed:** kept — [log-entry-write-can-clobber-an-existing-entry].
