# [HASH] — /plan's opening now warns when this chat's own build has not closed, so degraded lifts are named instead of silent

Build entry; the planning record is `2026-08-21-revisit-depends-on-a-log-that-the-close-writes.md`. The below-the-line revisit reads LOG, and a build run writes no LOG until its close — so a /plan run in the same chat correctly declines every lift depending on the run's work, silently. The cheapest fix was kept: /plan's Step 1 gains one branch — where this chat's build working file still exists, say once in the opening narration that lifts and shipped-flags depending on the run's work will not resolve until /done runs. The revisit itself is unchanged; reading the working file's ticks as truth was refused as a second source of truth about what shipped.

**Files touched:** `plugin/throughliner/docs/plan.md`.
**Routed to Captures:** none from this item.
Tick: done, confirmed — edit read back in place.
FAQ: not needed because the user sees one extra warning line and does nothing different.
Rule gate: run — admitted as an amendment to plan.md's opening (Step 1's read-state step gains one warning branch). No freestanding rule, no always-loaded slot, nothing evicted.
