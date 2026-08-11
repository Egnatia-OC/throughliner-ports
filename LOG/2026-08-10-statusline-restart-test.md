# 801c85a — The status-line restart test ran and produced an ambiguous result, so it is not being closed

The user quit and relaunched the desktop app, opened a fresh session, and reported
what the session-start hook told it. Claude then read the marker file, per the
item's step 4 and the check-the-world rule — the outcome was read from the file
rather than taken on report.

## What the marker shows

Nothing. `resources/testing/statusline-marker.log` still holds only its header
block. The probe never appended a line, so the desktop app never invoked the
status-line command during the restarted session.

On the item's own three-way reading, that is outcome three: the app does not run
status-line commands, the mechanism is dead in this environment,
[statusline-context-reader] is deleted, and [session-sizing-and-break-lines] falls
back to manual session-break lines.

## Why that reading is not being taken, and this is the substance of the entry

**The test could not distinguish "unsupported" from "the setting wasn't there
yet".** `.claude/settings.local.json` was edited during the previous session, while
the app was already running. If the desktop app reads its settings at launch — which
is the explanation the earlier 2026-07-31 attempt already reached for, when a live
in-session wiring produced an empty marker in exactly this way — then the app that
was quit had never seen the `statusLine` entry, and the app that relaunched was the
*first* launch to have it on disk. Under that reading a silent marker after this
restart is expected, and it says nothing about support.

The two readings are not equally likely, but neither is excluded, and the decision
they gate is large: outcome three deletes a queued item and changes how session
sizing is designed. Recording an ambiguous result as a clean negative is how a
wrong deletion gets justified later by pointing at a log entry.

**What the script is not.** It was smoke-tested by hand before the marker was
cleared — fed a payload on stdin, wrote its line correctly — so "the script is
broken" is excluded. That was the point of doing the smoke test and clearing the
file, and it did its job: it narrowed three possible explanations to two.

## What the next attempt must do differently

The setting is now on disk and has been through one full launch. So a *second*
restart discriminates: if the marker is still empty after an app that launched with
the setting already present, the settings-timing explanation is spent and outcome
three stands. Nothing else needs changing — no new script, no new wiring, one more
quit and relaunch.

The item stays in the queue rather than being closed, because it has not answered
its question. Its walkthrough was followed to the end; the test simply did not
resolve.

## Actions taken by Claude

- Read the marker file (empty but for its header).
- Confirmed from the fresh session's own report that the host is live at
  1.20.0-test5, stamp `6d898b6d8d36` — which is a separate result and a positive
  one: it is the hook-delivery liveness check the rezip ritual asks for, and it
  passed.
- Wrote the observed result into the queue item.
- Nothing deleted, no queue item closed.
