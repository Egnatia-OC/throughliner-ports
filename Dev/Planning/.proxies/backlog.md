<!-- proxy | source: Dev/Planning/BACKLOG.md | generated: 2026-05-29 v134 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

Shipped history (124 batches, V18–0135) now in build-log/INDEX.md — no longer inline. 7 queued batches (3 parked, 4 active) at L19–L150. 5 open questions at L152–L197. Ideas section at L200.

## Queued batches (L19–L150)

- L21 **0095** — /sovtest skill E2E validation. **PARKED.** Needs test plan rewrite after 0120 ships (0120 now shipped v129).
- L39 **0136** — Dev-side rules reconciliation. Prose equivalents of 10 plugin behavioural rules + C03/C04 contradictions. Targets session-protocol.md, CLAUDE.md.
- L53 **0137** — Dev-side workflow reconciliation. Five close/open procedure steps (G11-G12, G22-G24). Targets session-protocol.md.
- L67 **0138** — Dev-side structure reconciliation. Entry shapes for 5 undocumented dev artifacts (G17-G21) + C10/C16. Targets session-reference.md.
- L81 **0139** — Plugin lighter-close hardening. Four missing steps (G13-G16) flowing from dev side to plugin close.md. Implementation batch.
- L95 **0130** — /sovsetup case 1 retest. **PARKED** v134. Waiting on reconciliation (0136–0139). Includes step-by-step test protocol.
- L123 **0131** — Build lifecycle retest. **PARKED** v134. Waiting on reconciliation (0136–0139). Includes step-by-step test protocol.

## Open questions (5 entries, L152–L197)

- L158 **TEST-LOG columns — 10 vs 7** — keep dev's 7-column simplification or migrate to plugin's 10-column for convergence?
- L166 **Batch lifecycle on completion — remove vs preserve** — dev removes from BACKLOG; plugin preserves with Status: shipped. Which model?
- L174 **Volunteered test results vs. mechanical read-back** — accept user-provided results or insist on per-row read-back?
- L182 **Re-batching snapshot state after split** — what happens to active-build.md after carve-out?
- L190 **Step-by-step test protocol — where should it live?** — testing.md, universal-behaviour.md, or both? Cowboy tests exempt.

## Ideas (L200)

Empty.
