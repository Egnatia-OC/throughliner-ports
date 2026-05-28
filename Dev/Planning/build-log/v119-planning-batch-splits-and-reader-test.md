# v119 — 2026-05-28 — Planning: batch splits, reader test, mirroring audit

**What shipped.** Planning session. Contradiction/blocks audit across queued pipeline, followed by batch restructuring and two new batches.

Audit findings: (1) 0120's dev-side structural changes overlap with a new mirroring batch — stripped out and absorbed. (2) 0120's TEST-LOG merge invalidates 0095's test plan — parked note updated. (3) 0118 and 0119 are mixed dev/plugin but dev-side portions are independent — split both. (4) No other contradictions.

Changes to BACKLOG.md: 0118 rewritten as dev-side only. 0119 rewritten as dev-side only. 0120 stripped to plugin-only (naming + test merge). New 0121 (dev-side reader test — adapted from iteration playbook). New 0122 (dev-side structure mirroring audit — absorbs 0120's dev-side work, depends on 0121). New 0123 (plugin-side close mechanicals + two-turn — combined port of 0118+0119). 0095 parked note updated with 0120 dependency. Pipeline reordered: dev-side batches first (0121 → 0118 → 0119 → 0122), then plugin-side (0123 → 0120), then parked (0095).

**Decisions taken and why.** Reader test lands before all other dev-side work because it's a foundational audit — findings inform whether 0118/0119 are the right approach and what the mirroring batch should target. Dev-side close splits (0118/0119) land between reader test and mirroring audit so the mirroring audit sees session-protocol.md after close improvements. Plugin-side work deferred until dev-side patterns are proven.
