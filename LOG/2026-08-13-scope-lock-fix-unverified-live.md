# [HASH] — The default argument that made the scope-lock bug silent is gone

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
