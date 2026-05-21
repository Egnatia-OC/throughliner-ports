# TEST-LOG.md

> **FROZEN at method version V39, 2026-05-21 (shelved in session v40).** The live template is at `plugin/templates/TEST-LOG-TEMPLATE.md` — that's what `/adopt` scaffolds. The two-write rule that kept this copy aligned has been shelved (see `BUILD-METHOD.md` → *Two-write rule for canonical docs*). Restoring two-write maintenance is one `planning/OPEN-QUESTIONS.md` promotion away if a real audience for the no-plugin template set emerges.

This file records the test outcomes of every shipped build batch, one row per test. Maintained by Claude during builds and planning; the user reviews and confirms in planning sessions.

For the canonical column shape, pruning rule, ordering, and protocol, see `DOC-STRUCTURE.md` → *TEST-LOG.md structure*.

<!--
Entry format:
| 001 | YYYY-MM-DD | <session tag, OR YYYY-MM-DD if the project doesn't keep tags> | <Component name from MANIFEST.md, or plain English if cross-component> | <One-sentence test description specific enough to re-run from> | Pass / Fail / Skipped / blank | Yes (YYYY-MM-DD) / No | <observations, surprises, reason if Skipped, regression context if Fail> |

Status meanings:
- Pass — tested, behaved as expected
- Fail — tested, did not behave as expected; details in User Notes
- Skipped — explicitly not tested this round; reason required in User Notes
- (blank) — test session is open; user has not yet confirmed an outcome

Confirmed Explicitly meanings:
- Yes (YYYY-MM-DD) — the user named this specific row in the planning-session read-back; date is when the confirmation happened
- No — Status was filled in without explicit per-row user confirmation; only valid as a transient state during session-open

Ordering: newest-first. New rows append directly below the table header separator (`|---|...|`), pushing earlier rows downward. Within a single batch's append, rows go in recap order (lowest # at the top of that batch's block).
-->

| # | Date | Session | Component | Test Description | Status | Confirmed Explicitly | User Notes |
|---|---|---|---|---|---|---|---|

---
*No-code method — Version 39.*
