# TEST-LOG.md

One row per test for every shipped build batch. Maintained by Claude during builds and planning; user reviews and confirms in planning sessions. Full spec: `DOC-STRUCTURE.md` → *TEST-LOG.md structure*.

<!--
Row format:
| 001 | YYYY-MM-DD | <session tag or date> | <Component from MANIFEST> | <Test description, specific enough to re-run> | <Type> | <Claude / User> | <Status> | <Confirmed Explicitly> | <Notes> |

Status: Pass (behaved as expected), Fail (didn't — details in Notes), Skipped (reason in Notes), blank (open session, not yet confirmed).

Confirmed: Yes (YYYY-MM-DD) — per-row confirmation done; No — transient pre-confirmation state.

Types: Look and click, Run and read, Trigger and observe, Generate and inspect.

Verifier: Claude (structural/factual, filled during after-build) or User (judgement/visual, confirmed in planning read-back).

Ordering: newest-first. New rows go directly below the header separator.
-->

| # | Date | Session | Component | Test Description | Type | Verifier | Status | Confirmed Explicitly | Notes |
|---|---|---|---|---|---|---|---|---|---|

---
*No-code method — Version 70.*
