# [HASH] — mover-encoding-fix-verification: the UTF-8 fix works, em-dash echoed intact

**[user] walk-through of the queue-mover console encoding check. RESOLVED — the fix works.**

**The result.** The user ran a mover command in their own Windows PowerShell console and the echoed heading came back with its em-dash intact:

```
reorder_queue: deleted from Processed: #### The always-loaded rule corpus is over its ceiling — eviction is due [rule-corpus-over-ceiling]
```

No replacement character, no box, no mojibake. The UTF-8 stream reconfiguration shipped in `08c885b` — forcing `stdout`/`stderr` to UTF-8 at import — reaches the console. The item's alternative branch ("if it still mangles, the next suspect is the app's own rendering of tool output rather than Python's encoding") does not need to be taken.

**Why this needed the user.** The mangling never reproduced in either shell available to Claude — Git Bash and the PowerShell tool both printed em-dashes and `→` correctly — so the only console that could show the failure is the one the user is looking at. The capability check was re-run at hand-off rather than assumed: `read_terminal` reads a terminal Claude already drives, not the user's separate console window, and it was ruled out when the item was split.

## Two corrections made during the walk-through, both worth recording

**1. Claude's first offered command was wrong and the user hit the error.** It used a `--show` flag that does not exist; the mover replied `section must be Processed or Unprocessed, got: --show`. It failed safely — nothing was touched — but the user spent a turn on it. The cause is straightforward: the command was written from an assumption about the mover's interface instead of from `--help`, which was then checked and settled it in one call. The fix in practice is to verify a command's flags before handing it to the user, not after.

**2. `--move` echoes no heading at all**, confirmed here by running it against a scratch copy. That was already recorded by the 2026-08-11 attempt, which caught that the command offered then could not have produced the observation it asked for. Checked rather than trusted this time, and it held: `--move` prints only `Processed reordered (6 items), 3 items above the line`. **`--delete` is the only mover form that echoes an item heading.**

**How the destructive-command problem was solved.** `--delete` was the only form that would produce the observation, and running it on the real QUEUE.md would have deleted a live work item to test a console. Claude copied QUEUE.md to a temp path outside the project and had the user delete from that instead — the console rendering is what was under test, and it is identical either way. The temp copy was removed afterwards and the real queue confirmed intact.

**Observable check at close:** none on disk — the item says so itself, and it is precisely why this is a `[user]` line. The evidence is the user's report of the echoed characters, corroborated by a screenshot of their console.

**This `[user]` item is complete.**

Rule gate: not needed — a walk-through authored no rules and edited no method text.
FAQ: not needed because the fix restores expected behaviour in a development tool the user runs by hand; nothing a consumer meets has changed.
