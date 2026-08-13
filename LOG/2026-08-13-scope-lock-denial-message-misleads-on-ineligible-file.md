# 340e7ef — The scope-lock's denial message stops advising a typo hunt on a line that doesn't exist

The final `_deny` in `pre_tool_use.py` always carried the same advice: Files:
lines must be bare paths, so if this file looks listed above, check its line for
trailing text. That is useful only when the file **is** named in the list and the
match broke on an annotation. It is now conditional on the denied file's basename
appearing somewhere in the build's file list; where it does not, the message says
plainly that the file is not in the list at all.

A wrong diagnostic costs more than a missing one, because it spends the reader's
time in the wrong place — and the reader here is a run with nobody watching, at a
moment when something has already gone wrong.

Deleting the item was weighed: the case originally reported can no longer occur,
since the scope-lock returns early for every path never eligible to be listed.
What survived is polish, kept on the reasoning that these few lines are only ever
read when something has already failed.

**Files touched:** `plugin/si-plugin/hooks/pre_tool_use.py`
**Routed to Captures:** none
