# 7a161aa — the close's commit-message file moved from the project root to the session scratchpad

Every procedure-following close raised a permission popup at its commit step, and
the cause was our own safety check rather than anything in the app. The commit
core told the close to write `COMMIT_MSG.tmp` into the project root, on the
grounds that the build scope-lock is off by then — true, and beside the point.
The scope-lock was never the only gate. With no active build, `pre_tool_use.py`
runs the planning file-gate, which asks on any project write outside its
quiet-list, and a root temp file isn't on that list. Hook asks override
auto-accept by design, so the popup read as the app ignoring a setting that was
plainly switched on.

The fix is the one the method already prescribes everywhere else: a commit
message file is a temp file the project never keeps, so it goes to the session
scratchpad. That directory is exempt from every gate, sits outside the repo, and
clears itself — which retires the delete step as well as the popup. The false
sentence about the root being writable is replaced with the real explanation, so
a later session doesn't restore the old shape on the same reasoning.

Two things this close is deliberately not doing. Docset A carries the identical
instruction and the identical untrue claim, which contradicts the work item's own
statement that docset A never prescribed the temp file; that correction is
outside this run's described work and is captured instead, for a session that can
weigh it against the freeze. And no SPEC sentence was made wrong — SPEC describes
the planning file-gate as asking before an unexpected write, which is exactly
what it was doing, correctly, on a file that should never have been there.

Run under the overnight blitz's sanctioned departures (`resources/overnight-blitz-plan.md`):
approvals deferred, work committed to branch `overnight-blitz-2026-08-06`, no push
and no release.

FAQ: not needed because the change removes a spurious permission prompt rather
than altering anything the FAQ describes — the existing entry on the planning
file-gate stays accurate, and it now fires only on writes that genuinely warrant
a look.

**Files touched:** `plugin/si-plugin/docs-b/done.md` (commit core step 5 —
scratchpad path, delete step retired, writability explanation corrected).
**Routed to Captures:** [docset-a-commit-msg-tmp-same-bug].
