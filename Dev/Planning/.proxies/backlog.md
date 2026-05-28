<!-- proxy | source: Dev/Planning/BACKLOG.md | generated: 2026-05-29 v132 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

Shipped history (122 batches, V18–0133) now in build-log/INDEX.md — no longer inline. 5 queued batches (1 parked, 4 active) at L19–L117. 3 open questions at L120–L149. Ideas section at L152.

## Queued batches (L19–L117)

- L21 **0095** — /sovtest skill E2E validation. **PARKED.** Needs test plan rewrite after 0120 ships (0120 now shipped v129).
- L39 **0134** — Session-start routing clarifications. Resolve three routing-comprehension gaps from plugin reader test.
- L53 **0135** — Convergence reader test (stage 1 — initial reconciliation). Full overlap map between plugin-side and dev-side method.
- L67 **0130** — /sovsetup case 1 retest (post-fix verification). Verifies cowboy-test fixes (v113), method-infra whitelist (v115), language setting (v117), BACKLOG rename (v129). Includes step-by-step test protocol.
- L93 **0131** — Build lifecycle retest (post v115–v129 changes). Full pipeline /sovplan → /sovgit. Chains from 0130. Includes step-by-step test protocol.

## Open questions (3 entries, L120–L149)

- L126 **Volunteered test results vs. mechanical read-back** — accept user-provided results or insist on per-row read-back?
- L134 **Re-batching snapshot state after split** — what happens to active-build.md after carve-out?
- L142 **Step-by-step test protocol — where should it live?** — testing.md, universal-behaviour.md, or both? Cowboy tests exempt.

## Ideas (L152)

Empty.
