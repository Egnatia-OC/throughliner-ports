# [HASH] — The dispositions window fixed and the surfacing narrowed to refusals-only with a required close line

Two defects merged at the keep: a planning opening ran the listing and never surfaced it, and the listing itself printed "176 on record (since the last planning session)" — the window claim false. The cause, established by reading the code as the item required: the planning-entry finder matched `...-plan.md` filenames, which no longer exist since the per-entry split named planning records by slug, so the boundary was never found and the window silently became full history.

Built: `_latest_planning_entry()` finds the boundary by a planning entry's body fields (Queue changes / Work processed), newest-first, with the filename pattern kept for pre-split entries; verified live — the windowed listing now reports 0 entries since yesterday's planning session against 363 in full history. Each disposition line is marked where it records a refusal and the listing prints a refusal count, which is what the narrowed surfacing reads: CLAUDE.md now has the /plan opening carry one short line only where the window holds a refused proposal — silence otherwise, the quiet-when-fine shape — and a planning close's LOG entry carries one required line either way, refusals surfaced or none since last session, the FAQ-sync required-artifact shape.

Tick: done, confirmed — windowed 0 vs full-history 363, refusal count printed, CLAUDE.md passage amended.

**Files touched:** resources/rule_signals.py, CLAUDE.md
**Routed to Captures:** none
Rule gate: run — amends CLAUDE.md's surface-the-listing-at-a-/plan-opening rule, its named parent: the always-surface instruction is narrowed to refusals-only-with-silence-otherwise (that narrowing is the eviction), and the close-entry line is added as a subordinate required-artifact clause in the FAQ-sync shape. Failure evidence: the 2026-08-19 non-surfacing instance plus the unusable 176-entry listing at two openings.
FAQ: not needed because this is host-only; the listing does not ship.
