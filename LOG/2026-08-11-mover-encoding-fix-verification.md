# 7c9922a — Queue-mover console encoding, verification [mover-encoding-fix-verification]

Walked through during the 2026-08-11 build run, after its 21 build items were
complete. Written as the walk-through proceeds.

## Why this is the user's to run

The mangling never reproduced in either shell Claude has — Git Bash and the
PowerShell tool both printed em-dashes and `→` correctly. The only console that
shows the failure is the one the user is looking at, and Claude cannot see it.
The capability check was run rather than assumed: `read_terminal` was named as
the tool that might have done this and ruled out, along with the PowerShell tool.

## Ordering note

Walked BEFORE [statusline-restart-test], reversing the queue order. That item
asks the user to fully quit the desktop app, which ends the session — and this
run's work is not yet recorded. Claude's call, narrated rather than silent.

## Step 1 — the fix ships. DONE.

The UTF-8 stream reconfiguration landed in `08c885b`. `reorder_queue.py` forces
UTF-8 with `errors='replace'` on both stdout and stderr before any message is
emitted.

Incidental corroboration from this same run, worth recording because it is
evidence the fix is doing something: the new `queue_digest.py` was written
WITHOUT that reconfiguration and crashed on its first run — `UnicodeEncodeError`
on `→`, from an arrow inside a queue heading. Adding the same fix cured it.
So the defect class is real and reproducible in this environment; what has never
reproduced here is the *silent mangling* the user saw, as opposed to a crash.

## Step 2 — the user runs one mover command and reports the echo

A scratch fixture was used rather than the real QUEUE.md, so nothing the project
depends on is touched. Its headings carry both an em-dash and an arrow.

**Claude ran it first, at the user's request, and it proves nothing new — stated
so the clean result is not later mistaken for a resolution.** The Bash tool's
shell printed `#### First item — with an em-dash and an arrow → in the heading`
with both characters intact. That is the same shell that never reproduced the
fault, so a clean result there was the expected and already-known outcome.

**A correction worth recording, because it would have wasted the user's turn.**
The first command offered used `--move`, whose report prints a count
("Processed reordered (2 items)") and echoes no heading at all — so it could not
have tested anything. `--delete` is the path that echoes the item's heading.
Running it myself is what caught that; had it gone straight to the user, they
would have run a command incapable of producing the observation.

**Deferred 2026-08-11 at the user's request** — they were on remote control and
away from the computer, so the console this test turns on was not in front of
them. The item stays in Processed, unchanged, for a later session. Nothing is
lost: step 1 is done, the fixture is disposable, and the command is recorded
below.

The command to run, in their own terminal, against a scratch file so nothing
real is touched:

```
python "<project>/plugin/si-plugin/scripts/reorder_queue.py" <scratch>/ECHOTEST.md --delete echo-beta Processed
```

The scratch fixture lives in a session scratchpad that self-clears, so a later
session recreates it: a two-item Processed section whose headings carry an
em-dash and an arrow. Use `--delete`, not `--move`.

## Observable check at close

The user's report of the echoed characters. There is nothing on disk to read,
which is precisely why this is a `[user]` line rather than a check Claude runs.

## If it still mangles

The stream reconfiguration is not reaching the console, and the next suspect is
the app's own rendering of tool output rather than Python's encoding. Do not
close it as fixed on the strength of the fix having shipped.
