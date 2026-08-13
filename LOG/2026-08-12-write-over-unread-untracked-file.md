# 16ed591 — The interrupted-build check was already correct, so what shipped was the untracked-file habit and a note on why the exact name matters

This item had two halves and the substantive one turned out to be already done. It said to correct a `*_build.md` glob in /next's pre-flight so it matches the session-scoped name. Grepping the whole plugin finds no such pattern: `next.md` already states the file is per session, named `_build-<session-id>.md`, and that the check is for *this* session's file and no other. `session_start.py`'s leftover-working-file scan matches the session-scoped form and deliberately also recognises the retired bare names, so a project mid-build when the rename shipped is not orphaned. There was nothing left to fix.

Recorded plainly rather than logged as work performed. The item's underlying claim was re-verified anyway, since it is the evidence the whole item rests on, and it reproduces exactly: `*_build.md` matches `_build.md` and `x_build.md` but not `_build-abc123.md`. A pattern written for the retired name can never find a current working file, which would make the check report "no interrupted build" every time, silently, forever. That reasoning is now written into the pre-flight beside the requirement, so the next person editing it knows what a loosened pattern would cost.

The second half was genuinely missing and is added. Before creating any file at the project root, read the untracked list in the session's opening snapshot. A file listed there exists but has never been committed, so git holds no copy and overwriting it destroys the only version — and the editing tool will not stop you, because it reports the write as creating a new file. That is what happened: `EDITING-STATE-CONTRACT.md` sat untracked, was listed in the session's own opening context, and was overwritten without being read. The replacement is complete and correct against SPEC, which still carried every word of the contract at that moment, so the outcome is fine and the prior content is simply unknown.

It is a habit, not machinery, and is marked as one. One instance does not earn an always-loaded obligation.

One piece of the item's own reasoning was void and is named here as a fourth instance of the superseded-research problem: it resisted a new rule on the ground that "the corpus is 65% over its ceiling for this project". That ceiling had already been deleted and replaced with a growth report carrying no threshold. The conclusion — no always-loaded rule for one instance — survives on its own merits; the number behind it does not.

**Files touched:** `plugin/si-plugin/docs-b/next.md`

**Routed to Captures:** none

Rule gate: not needed — a habit added to an existing pre-flight step and an explanation written beside an existing requirement. No always-loaded rule, deliberately.
