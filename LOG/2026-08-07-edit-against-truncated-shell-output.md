# [HASH] — Two file-safety clauses: an old_string comes from the file's bytes, and a method doc is never scratch space

Both land in `docs-b/plugin-behaviour.md`'s file-safety section, beside the modified-on-disk rule whose neighbours they belong among.

**An Edit's `old_string` comes from a tool that returns the file's bytes — Read, or a grep returning whole lines — never from shell output.** Stated in its general form too, since it is broader than Edit: text that has passed through a display-formatting command is not a copy of the file.

**The decisive property is that you cannot tell from the output whether it was truncated**, and that is why the rule keys on the *source* of the text rather than on inspecting it. A line cut at 120 characters looks exactly like a 120-character line — no marker, no ellipsis, nothing to notice. The trap covers `cut`, `head -c`, column-limited `git log --oneline`, a pager, and a grep whose match window clipped the line. What happens when it slips is silent corruption rather than an error: Edit matches on substrings, so a truncated line matches the *start* of the real one and the replacement is spliced into its middle. That happened — a stray token ended up inside a work item's prose, and the queue lint could not see it, because the damage was in a rationale line and the structure stayed valid.

**A method document is never scratch space.** No placeholder, anchor, or temporary token written into QUEUE.md, SPEC.md or a LOG entry as a step toward a later edit. The risk is not the token's lifetime — it is that any interruption between the two edits commits it, leaving it in a tracked file with nothing flagging it.

This sits beside the never-retype rule but is not covered by it: never-retype is about *content corruption*, and says nothing about using a live document as *working space*, where the content is fine and the temporary state is the problem.

**The clause names three legitimate routes in the same breath**, and that is not decoration. This project has recorded from three walked-into failures that a prohibition stated at a moment of real pressure reliably produces an invented escape, and an invented move is worse because nothing recognises it. So: the mover (`reorder_queue.py`) for block relocation; a single well-anchored Edit where the mover doesn't fit; the session scratchpad for anything genuinely needing scratch space.

**The rule's standing is honest rather than confident:** no hook sees where a string came from, so there is no mechanical route, and this same session then broke the shell-write half twice — filed as [shell-heredoc-write-immediately-after-authoring-the-rule].

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`
**Routed to Captures:** [shell-heredoc-write-immediately-after-authoring-the-rule]
