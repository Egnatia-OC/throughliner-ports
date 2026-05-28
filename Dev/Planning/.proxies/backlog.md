<!-- proxy | source: Dev/Planning/BACKLOG.md | generated: 2026-05-28 v119 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

115 shipped/cancelled batch rows (V18–0117) in table at L13–L115. 7 queued batches with full scope at L118–L232. 1 open question at L234–L252.

## Queued batches (L118–L232) — dev-side first, then plugin-side, then parked

- L124 **0121** — Dev-side reader test. Three sub-agents read dev docs as stranger-Claude. Outputs ranked gap list. No deps.
- L140 **0118** — Scripted close mechanicals (dev-side). Python script for footer bumps, version updates, proxy regen. Dev-side only.
- L154 **0119** — Two-turn close procedure (dev-side). Judgment + mechanical pass with `/compact` boundary. Depends on 0118.
- L170 **0122** — Dev-side structure mirroring audit. Compare dev-side vs plugin-side patterns. Absorbs 0120's dev-side work. Depends on 0121.
- L186 **0123** — Plugin-side close mechanicals + two-turn procedure. Ports 0118+0119 to plugin. Depends on dev-side 0118+0119.
- L202 **0120** — BACKLOG convergence: naming and test merge (plugin-side only). BUILD-PLAN→BACKLOG rename + TEST-LOG merge. Large surface area.
- L216 **0095** — /sovtest skill E2E validation. **PARKED.** Needs test plan rewrite after 0120 ships.

## Open questions (1 entry, L234–L252)

- L240 **Plugin testing framework beyond bespoke pytest** — park until test maintenance burden grows
