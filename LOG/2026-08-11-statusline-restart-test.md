# 7c9922a — Status-line restart test, second attempt [statusline-restart-test]

Walked through during the 2026-08-11 build run, after the run's 21 build items
were complete. Written as the walk-through proceeds, so a crash mid-way leaves a
record of what was actually done rather than nothing.

## Why a second attempt was needed

The first run, on 2026-08-10, did not resolve. The user quit and relaunched, and
the marker file was still empty but for its header. That reads like the third
outcome — the desktop app does not support status-line commands — but it was
deliberately not taken, because `.claude/settings.local.json` was edited while
the app was already running. The app that quit had never seen the `statusLine`
entry, and the app that relaunched was the first launch with it on disk. If the
app reads settings at launch, a silent file is exactly what that would produce
and it says nothing about support.

"The script is broken" was already excluded: it was smoke-tested by hand before
the marker was cleared.

**What makes this attempt decisive:** the setting has now been on disk through a
full launch, so a second quit-and-relaunch discriminates. Still empty means the
timing explanation is spent and the third outcome stands. No new script, no new
wiring — one more restart.

## What the outcome decides

- real percentages → the mechanism works, and [statusline-context-reader] is
  buildable with an offset threshold designed for the known undercount
- `null` values → a payload-timing problem
- file never written at all → the desktop app does not support status-line
  commands, and the mechanism is dead in this environment

## Step 1 — Claude confirms the probe is wired. DONE.

Verified at the start of the walk-through, by reading rather than recalling:

- the probe exists: `resources/testing/statusline_probe.py`
- it is set as the `statusLine` command in `.claude/settings.local.json`, with
  the absolute path to that script
- the marker file `resources/testing/statusline-marker.log` currently holds its
  header block and nothing else — so anything appearing below that block came
  from the app

The wiring survived the intervening sessions unchanged.

## Step 2 — the user quits and relaunches

**Deferred 2026-08-11 at the user's request** — they were on remote control and
away from the computer, and this step needs them at the machine to fully quit
the desktop app and confirm the process has exited. The item stays in Processed,
unchanged.

**It was already sequenced last for a related reason, and that reasoning still
holds for whoever picks it up.** Quitting the app ends the session, so this test
should be run only when the session's work is already recorded and committed —
otherwise the restart takes uncommitted work with it. Pair it with a restart
that is happening anyway; that is convenience, not a reason to wait for one.

Step 1's verification does not need repeating: the probe is wired and the marker
file holds only its header, both confirmed above. The next attempt is one
quit-and-relaunch and then a read of the marker.

## Observable check at close

The marker file's contents. Claude reads the file rather than taking the outcome
on report, per the check-the-world rule.
