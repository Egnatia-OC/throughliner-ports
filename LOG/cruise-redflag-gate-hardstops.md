# [HASH] — Added cruise red-flags gate (hooks/cruise_gate.py) blocking a run on any open flag, plus hard-stops in cruise.md

Implemented [cruise-control] concerns 4 and 8. cruise_gate.py is a procedure-invoked gate script — not an event hook, since no skill-start event exists to wire one to — that reuses session_start.py's `_open_red_flags` so the gate and the session-start red-flag scan never drift on what counts as open. Contract: exit 0 `GATE: CLEAR` / exit 1 `GATE: BLOCKED` + the open flags. cruise.md runs it at the top of the run and before each line; any open flag blocks the run outright (absolute, because a mechanical check can't judge a risk's relevance on the one category you least want it guessing), and a flag raised mid-run flips to a halt. Hard-stops: iteration ceiling (default 12), no-progress after 3 repeats, and a best-effort budget — each writes BLOCKED and exits. Fixture-tested 5/5 in-session. Host-side; live verification deferred to reinstall.

**Files touched:**
- hooks/cruise_gate.py (created)
- docs/cruise.md

**Routed to Captures:** none
