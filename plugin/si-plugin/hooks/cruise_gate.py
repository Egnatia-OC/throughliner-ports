#!/usr/bin/env python3
"""
Cruise red-flags gate.

A cruise run may proceed only when no red flag is open — only resolved or
accepted flags let it run (plugin-behaviour.md Red flags; [cruise-control]
concern 4). This script reads the three flag states in QUEUE.md and reports
whether the run is clear to proceed or blocked.

It is a *procedure-invoked* gate, not an event hook: there is no "skill start"
event to hang a true hook on, so cruise.md runs this at the top of the run and
before each work line (loop step b). Because red-flag screening runs the whole
time, a flag raised mid-run is open by definition and the next gate check flips
the run to a halt — an open risk and driving unattended are mutually exclusive.

Contract (so cruise.md can read the result mechanically):
  - exit 0 and print "GATE: CLEAR" when no red flag is open.
  - exit 1 and print "GATE: BLOCKED" followed by one line per open flag when
    one or more are open. cruise.md treats a non-zero exit as "do not run /
    halt", writes a BLOCKED marker, and stops.
  - exit 0 and print "GATE: CLEAR (no queue found)" when QUEUE.md is absent —
    a missing queue is not an open risk, so it does not block; the run's own
    read of the cleared region handles an empty/absent queue.

The queue path is argv[1] when given, else QUEUE.md in the current working
directory (cruise.md runs this from the project root).

Red-flag parsing is reused from session_start.py — the same `_open_red_flags`
that the session-start scan uses — so the gate and the session-start surfacing
never drift on what counts as an open flag.
"""

import os
import sys

# session_start.py sits in this same hooks/ directory, so it imports cleanly
# when this script is run directly (its directory is sys.path[0]). Reusing its
# parser keeps the gate and the session-start red-flag scan in lockstep.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from session_start import _open_red_flags  # noqa: E402


def main() -> int:
    if len(sys.argv) > 1:
        queue_path = sys.argv[1]
    else:
        queue_path = os.path.join(os.getcwd(), "QUEUE.md")

    if not os.path.isfile(queue_path):
        print("GATE: CLEAR (no queue found)")
        return 0

    open_flags = _open_red_flags(queue_path)
    if not open_flags:
        print("GATE: CLEAR")
        return 0

    print("GATE: BLOCKED")
    for flag in open_flags:
        print(f"- {flag}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
