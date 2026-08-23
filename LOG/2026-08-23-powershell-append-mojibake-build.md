# [HASH] — Scripting constraints: the encoding bullet now covers PowerShell's own file reads

The instance, from the close that filed it: three appended queue items arrived with every em-dash as mojibake, because a PowerShell step read a UTF-8 scratchpad file with `Get-Content -Raw` and no `-Encoding`, mangled the text, and wrote the mangled bytes back out through a write that was itself correctly UTF-8. It was repaired in-session and verified by reading raw bytes, per the existing check-`ascii()`-first constraint.

This ships as an amendment rather than a new bullet, and the distinction is what got it admitted at all. On its own the occurrence fails the more-than-once bar. It is not on its own: the parent is the subprocess-read encoding constraint, and the family — Windows encoding defaults silently mangling text — has now bitten at three layers, hook stdout, subprocess reads, and `Get-Content`. One bullet was reworded to name both cases; the constraints list has the same five bullets it had before.

**Files touched:** `CLAUDE.md`, scripting constraints — the subprocess-read bullet reworded to require UTF-8 on any subprocess read and any PowerShell read of a text file, with both spellings given.

**Routed to Captures:** none from this item.

Tick: done, confirmed — bullet count unchanged at five, and the reworded bullet names both cases.

Rule gate: run — amendment to the scripting-constraints subprocess-read clause, parent named; one clause reworded, no new bullet, nothing evicted. A freestanding clause was refused on the more-than-once bar, and a hook was refused because the write reaches the file through arbitrary shell text no hook can reliably parse for encoding flags.

FAQ: not needed because this is a host-only development constraint consumers never read.
