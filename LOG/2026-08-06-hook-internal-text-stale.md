# 6088ec7 — retired "batch" vocabulary cleared out of the hooks, and a docstring corrected against its own caller

Found by the overnight blitz's cross-doc consistency sweep. None of it changes
behaviour, and that is the argument for doing it: a comment is what a later
session reads to decide whether it may change the code beneath it, so text
describing a model the method retired, or contradicting the call two hundred
lines below, is a wrong instruction sitting exactly where the next reader will
trust it.

Four spots carried the retired term. `hooks.json`'s description — not internal at
all, but the plugin's own description string, which the surrounding tool can
surface — advertised "the batch file-list boundary (SPEC editable only when a
batch lists it)"; it now names the active build's file list. Three code comments
in `pre_tool_use.py` and `session_start.py` said the same thing in passing. One
of those, at `session_start.py` line 666, was not in the work item: it turned up
on the re-grep after the first pass, which is why the check was run rather than
the list trusted.

The docstring was the sharper find. `_fire_once`'s docstring told the reader that
its caller passes _build.md's creation time as the key that re-arms the advisory.
The caller passes the `Run:` line, and the comment beside that call records that
both timestamps were considered and rejected — ctime means inode-change off
Windows, so progress ticks would re-arm it, and mtime re-arms on every tick. So
a reader of the helper alone got the contract backwards, in the place that reads
most authoritatively. The corrected docstring now carries the real key, both
rejected options with their reasons, and a note that it previously disagreed with
its caller, so the old wording isn't restored by someone reasoning from the
function alone.

Deliberately left alone: the retired-format vocabulary in `migrate-checklist.md`
and `setup.md` (Batches, Parked, Deferred tests). Those docs describe the old
format a project is being migrated *from*, so the terms are correct there and
removing them would break the migration recipe.

Verified rather than assumed: `hooks.json` parses as JSON, all three hooks
compile, and a repeat grep for the term over `hooks/` now returns nothing.

Run under the overnight blitz's sanctioned departures (`resources/overnight-blitz-plan.md`):
approvals deferred, committed to branch `overnight-blitz-2026-08-06`, no push and
no release. The item was also *processed* by the blitz — filed as a capture by
its own sweep, then moved into Processed above the readiness line — under the
blitz's softened bar, which permits processing an item that is practically
already designed. Every point in it was an unambiguous repair with no design call
in any of them, which is also why they were consolidated into one work item
rather than filed separately.

FAQ: not needed because nothing here is user-facing — the changes are code
comments, a docstring, and a manifest description, and no described behaviour
changed.

**Files touched:** `plugin/si-plugin/hooks/hooks.json` (description),
`plugin/si-plugin/hooks/pre_tool_use.py` (two comments, `_fire_once` docstring),
`plugin/si-plugin/hooks/session_start.py` (two comments).
**Routed to Captures:** none.
