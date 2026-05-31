# v120 — 2026-05-28 — Dev-side reader test: gap list and BACKLOG routing

**What shipped.** Reader test (batch 0121) run against four dev-side docs using three parallel sub-agents — comprehension Q&A, fresh session role-play, curveball multi-thread opener. Ranked gap list saved to `Dev/Resources/research/dev-side-reader-test-findings.md`. Two new queued batches (0124 close procedure fixes, 0125 opener routing completeness) and 11 new open questions added to BACKLOG from the findings.

**Decisions taken and why.** Top-tier gaps (5) grouped into two batches rather than one — close-procedure fixes (T2/T3/T4) are independent of opener-routing fixes (T1/T5). M9 (disambiguation sequencing) folded into batch 0125 rather than kept as an OQ because it's a sub-aspect of the blended-opener rule. Bottom-tier findings B2–B5 clustered into one OQ (cross-reference precision) rather than four, since they share a root cause.

**Pivots and surprises.** All three agents independently flagged the blended-opener routing gap (T1) — the strongest signal in the test. The curveball agent's reflection was the richest; comprehension Q&A found the most mechanical issues; fresh-session role-play was intermediate. Matches the source prompt's note that comprehension Q&A historically surfaced the most gaps.
