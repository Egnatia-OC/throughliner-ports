# [HASH] — Audit: /next terminates the run at the first [user] item by spec (not model misbehaviour); filed 3 findings and corrected the Verso-transcript-as-proof record [next-stops-after-one-item]

Audited next.md and the saved Verso transcript against the 2026-07-30 design intent (run continuously; the stop-at-[user] rule was only meant to prevent interrupting contiguous Claude blocks, never to terminate). Verdict: the reported "stops after one item" is a real deviation, and its root is next.md's own spec — Step 1.2 defines the run as ending before the first [user] item, and Step 3 says "Don't build past it," then recommend /done. This confirms [reorder-home-is-plan-close]'s split (placement at /plan close; non-termination at /next). The Verso transcript is NOT proof of the bug: its single-item stop was gated (later builds depended on the item's user-run verification) and its [user] verification ran collaboratively in-session, not via a fresh /next+/done. Caveat carried: other projects' queue states aren't readable from this repo, which blocks the cross-project "cleared lines skipped" diagnostic.

**Files touched (read-only):**
- plugin/si-plugin/docs/next.md
- resources/testing/verso-next-single-item-2026-07-29.md

**Routed to Captures:** next-run-terminates-at-user-item, verso-transcript-not-bug-evidence, next-nontermination-fix-standalone, and (user-raised during handover) audit-placement-after-build-blocks, ready-stop-redundant

**Approval outcomes:** all findings approved as-is
