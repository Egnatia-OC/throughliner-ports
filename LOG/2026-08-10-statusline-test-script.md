# 10d6474 — The status-line probe written and wired, ready for the restart test

Split from [statusline-restart-test] at the keep-step because the work is mixed:
writing and wiring the probe is entirely Claude's, and only the restart is the
user's. That split also closes the recording gap [walkthrough-work-unrecorded]
found — as its own build item this work is scoped, recorded and committed like any
other, rather than happening invisibly inside a walk-through.

`resources/testing/statusline_probe.py` reads the status-line JSON from stdin,
pulls `context_window.used_percentage`, appends it with a timestamp to
`resources/testing/statusline-marker.log`, and prints `SL-TEST ctx=…` so the status
bar itself shows whether the probe ran. It is set as the `statusLine` command in
`.claude/settings.local.json`.

Two decisions worth recording. The marker lives in the repo rather than the session
scratchpad because it has to survive an application restart, and the scratchpad
does not — that restart is the whole test. And the script records what it received
literally, distinguishing a `null` value from a missing key, because those are
different findings and flattening them would lose the one distinction the test
exists for.

It was smoke-tested by hand — fed a payload on stdin, wrote its line correctly —
and the marker then cleared to a header block explaining that anything below it
came from the app. That matters for reading the result: a silent file after the
restart now means the app never ran the probe, not that the script is broken.

The marker path is recorded in [statusline-restart-test] so the user's report has
something concrete to read, which was this item's stated done-when.

This is scaffolding for one observation. The script, its marker and the settings
entry are all deleted once the test has reported — that delete-time is written into
the script's own docstring.

**Files touched:** new `resources/testing/statusline_probe.py`, new
`resources/testing/statusline-marker.log`, `.claude/settings.local.json`, `QUEUE.md`.

**FAQ: not needed because** it is local test scaffolding in this project only,
never shipped in the plugin.

**Routed to Captures:** none from this item.
