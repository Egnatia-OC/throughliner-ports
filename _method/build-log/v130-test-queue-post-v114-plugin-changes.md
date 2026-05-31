# v130 — 2026-05-28 — Planning: test queue for post-v114 plugin changes

**What shipped.** Two E2E test batches queued (0130, 0131) covering untested plugin code from v113–v129. 0130: /sovsetup case 1 retest verifying cowboy-test fix sweep (v113), method-infra whitelist (v115), language setting and BOM hardening (v117), and BACKLOG rename (v129). 0131: full build lifecycle retest covering phase detection (v115), session-length safeguards (v116), close handoff artifact (v118), two-turn close with consumer bump_version.py (v128), and BACKLOG convergence (v129). Both batches include a step-by-step test protocol paragraph to enforce one-step-at-a-time guided walkthroughs. One OQ added: permanent home for step-by-step test protocol (testing.md vs universal-behaviour.md vs both).

**Decisions taken and why.** Split into two test batches rather than one combined run — setup and build lifecycle exercise different code paths and the setup test's output feeds the build test. Cowboy tests excluded from the step-by-step protocol — those are freeform user exploration, not guided walkthroughs. Test protocol added per-batch as a stopgap pending the OQ resolution.

**Pivots and surprises.** None.
