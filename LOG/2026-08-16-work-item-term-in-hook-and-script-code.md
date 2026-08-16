# d82f538 — Three user-facing warnings stop calling an Unprocessed block a "work item"

Only items in Processed are work items; before that they are captures or unprocessed entries. That definition shipped with the parent item. This is the half that was split out so the definition could ship without touching hook internals.

**The strings fall into three groups, and reading them answered both open questions at once.**

*Already correct, and left alone.* One sentence in the queue lint says "Processed holds work items but the cleared-to-run marker is missing". That sentence genuinely is about Processed, so the term is right there and renaming it would introduce an error.

*User-facing and genuinely wrong — this is the whole build.* The slug warning and the orphan-prose warning both fire on Unprocessed entries and both print at consumers, plus the equivalent report and refusal strings in the queue mover. These are user-facing text wearing code's clothes. They now say **"entry"**, which is true in both sections.

*Parser-internal, and deliberately NOT changed.* Roughly forty comments, docstrings and identifiers describing a block the parser handles identically in either section. They stay, on the user's decision: they carry real risk — these are the files that lint and move the queue — for no user-visible gain, and the term there is arguably accurate about what the code does. **If they are ever renamed it must be to "entry" or "heading block", never to the user's vocabulary**, because adopting her vocabulary would make the code claim a distinction it does not actually draw.

**The cost of leaving them, accepted rather than dismissed.** The double meaning the parent item removed survives in the comments, which is where this project has repeatedly found its stale text. That is accepted because it is now *recorded* as a decision with a stated reopening shape, rather than left as unnoticed residue — the difference between a known limit and rot.

One suite pinned the orphan-prose text and was updated with the string, found by grepping the asserted text before editing rather than by discovering the failure.

Depth: short.

Rule gate: not needed — no rule authored or amended. Three user-facing message strings corrected to match a definition the parent item already shipped.

FAQ: not needed — a warning message uses a correct word where it used a wrong one.

**Files touched:** `plugin/throughliner/hooks/post_tool_use.py`, `plugin/throughliner/scripts/reorder_queue.py`, `resources/testing/test_queue_lint_flags.py`.

**Routed to Captures:** none from this item.
