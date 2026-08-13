# [HASH] — CLAUDE.md records that this machine's `python` is Inkscape's, and what follows

Two lines in a new scripting-constraints bullet: scripts under
`plugin/si-plugin/scripts/` and `resources/` are standard-library only, and the
test suites are invoked as plain scripts, never through pytest.

On this machine `python` resolves to `C:\Program Files\Inkscape\bin\python.exe` —
an application's bundled interpreter, first on PATH, shadowing the user's own
Python 3.13, which `py` reaches. Re-verified live at processing rather than taken
from the capture.

The constraint has cost nothing so far precisely because every script here is
standard-library only, so it runs identically under any recent interpreter. What
makes it live now is the hook-test close obligation shipped in this same run: it
runs the suites at every hook-touching close, which is the moment the constraint
starts being paid. A step written as `python -m pytest` would fail here with a
message naming Inkscape, which reads as nonsense and sends a session chasing the
wrong cause.

Host-only deliberately. Consumers have their own PATH and their own interpreters,
and a rule about this machine's Inkscape installation would be noise shipped to
people it can never apply to.

The stale environment note — the global instructions claim Python 3.14 is
installed with `python` on PATH, and neither half is true — is out of scope and
belongs to no queue here. It was raised with the user directly.

Rule gate: run — admitted; parent named as the Working conventions list, written
as one bullet with the UTF-8 rules rather than two.

FAQ: not needed because it is host-only.

**Files touched:** `CLAUDE.md`
**Routed to Captures:** none
