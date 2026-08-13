# 340e7ef — The default argument that made the scope-lock bug silent is gone

`_is_method_doc` in `pre_tool_use.py` no longer declares `session_id: str = ""`.
That default is the mechanism that made the original bug invisible: called with
two arguments it resolved this session's working file as `_build-unknown.md`,
matched nothing, and denied every write without any error. Every caller passes
the id correctly today; nothing stopped the next one omitting it and
reintroducing the identical failure. It was the only such default left in either
hook. The docstring now says why the argument is required.

The item's headline premise was already falsified at processing — the host
carries the fix, confirmed by matching build stamps — so what shipped here is the
guard against recurrence rather than the fix itself. Nothing waits on it.

Checked and clean, recorded so nobody re-runs it: no suite under
`resources/testing/` calls the function at all, and all five pass unchanged.

**Files touched:** `plugin/si-plugin/hooks/pre_tool_use.py`
**Routed to Captures:** none

---

## After the close — the rezip that made this run live

Written after `340e7ef` was committed and pushed, so it is a tail rather than
part of the record above.

The user asked for a rezip. The installed host went from `1.20.0-test8` to
`1.20.0-test9`, and the content stamps matched exactly on both sides —
`158761527ddf` over `plugin/si-plugin` and over the installed cache directory —
so the snapshot genuinely took rather than reporting a silent no-op. All six
suites under `resources/testing/` passed before the install, `__pycache__` was
cleared, and the cache was pruned to the last three builds plus the new one.

**The liveness half was proved rather than assumed, which is the point of that
step.** After a full app restart, the fresh session's own start reported plugin
`1.20.0-test9` and build stamp `158761527ddf` — the same value computed from the
source before the restart — and the rules file loaded in that session carried
this run's own edits. A well-formed hook that is silently dropped looks identical
to a working one from the writing side; a session saying what it received is what
distinguishes them.

**So this entry's guard is now live**, along with every other host-side change in
the run: the mail step, the capture offer, the checkpoint specimen, the changed
close recommendation, and the deny-message fix.

One step of the rezip ritual was not completed and is recorded as not done rather
than passed: it asks for the CLI's version to be compared against the desktop
app's. The CLI is `2.1.220`; there is no way to read the app's version from a
session, so the comparison did not happen.

The test-suffix version numbering continued from the installed host's `-test8`
rather than restarting at `-test1`, which is what the literal wording of the
ritual would give now that the push has cleaned the base version. Continuing the
line keeps each cache directory distinct and the sequence readable.
