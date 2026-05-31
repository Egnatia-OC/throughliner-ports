# v126 — 2026-05-28 — Session-open state summary + step 2 annotations

**What shipped.** Two prose additions to session-protocol.md resolving reader-test findings M6 and M8. Step 2's single-line doc list expanded into a sub-list with per-doc purpose phrases and line counts. New step 5 added after step 4: a state-summary template defining the expected shape (version triplet, queue depth, next batch, OQ count, notable conditions). Routing table updated — Implementation, Doc-only, Ideation, and E2E test rows now reference step 5.

**Decisions taken and why.** State summary is a numbered step (5) rather than an unnumbered paragraph — keeps routing-table references clean and aligns with the existing "Steps 1, 3, 5" in the planning row, which previously referenced a non-existent step. Batch scope said "Two OQs removed from BACKLOG" but M6 and M8 were never parked as OQ entries — they were routed directly into batch 0126. No BACKLOG removal needed.

**Pivots and surprises.** The planning row's "Steps 1, 3, 5" pre-dated step 5's existence. Adding the state-summary step retroactively fixed a stale reference — an instance of the "Cross-reference precision" OQ (B2/B3/B4/B5) resolving itself organically.
