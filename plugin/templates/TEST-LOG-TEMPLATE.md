# TEST-LOG.md

This file records the test outcomes of every shipped build batch, one row per test. Maintained by Claude during builds and planning; the user reviews and confirms in planning sessions.

For the canonical column shape, pruning rule, ordering, and protocol, see `DOC-STRUCTURE.md` → *TEST-LOG.md structure*.

<!--
Entry format:
| 001 | YYYY-MM-DD | <session tag, OR YYYY-MM-DD if the project doesn't keep tags> | <Component name from MANIFEST.md, or plain English if cross-component> | <One-sentence test description specific enough to re-run from> | <Look and click / Run and read / Trigger and observe / Generate and inspect> | <Claude / User> | Pass / Fail / Skipped / blank | Yes (YYYY-MM-DD) / No | <observations, surprises, reason if Skipped, regression context if Fail> |

Status meanings:
- Pass — tested, behaved as expected
- Fail — tested, did not behave as expected; details in Notes
- Skipped — explicitly not tested this round; reason required in Notes
- (blank) — test session is open; user has not yet confirmed an outcome

Confirmed Explicitly meanings:
- Yes (YYYY-MM-DD) — the user named this specific row in the planning-session read-back (user-verified rows), or Claude filled in the result during after-build (Claude-verified rows); date is when the confirmation happened
- No — Status was filled in without explicit per-row user confirmation; only valid as a transient state during session-open

Type meanings:
- Look and click — open an app or interface, interact, observe behaviour
- Run and read — execute a command, read stdout/stderr or a return value
- Trigger and observe — set up conditions, trigger an event, verify the system responded
- Generate and inspect — run a process that produces a file or artefact, verify contents

Verifier meanings:
- Claude — structural/factual check verified by Claude during after-build
- User — judgement/taste/visual-nuance check requiring user confirmation

Ordering: newest-first. New rows append directly below the table header separator (`|---|...|`), pushing earlier rows downward. Within a single batch's append, rows go in recap order (lowest # at the top of that batch's block).
-->

| # | Date | Session | Component | Test Description | Type | Verifier | Status | Confirmed Explicitly | Notes |
|---|---|---|---|---|---|---|---|---|---|

---
*No-code method — Version 54.*
