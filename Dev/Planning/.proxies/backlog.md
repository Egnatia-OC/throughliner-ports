<!-- proxy | source: Dev/Planning/BACKLOG.md | generated: 2026-05-28 v123 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

117 shipped/cancelled batch rows (V18–0118) in table at L12–L117. 5 queued batches with full scope at L121–L205. 7 open questions at L207–L297.

## Queued batches (L121–L205) — dev-side first, then plugin-side, then parked

- L127 **0119** — Two-turn close procedure (dev-side). Judgment + mechanical pass with `/compact` boundary. Depends on 0118.
- L143 **0122** — Dev-side structure mirroring audit. Compare dev-side vs plugin-side patterns. Absorbs 0120's dev-side work. Depends on 0121.
- L159 **0123** — Plugin-side close mechanicals + two-turn procedure. Ports 0118+0119 to plugin. Depends on dev-side 0118+0119.
- L175 **0120** — BACKLOG convergence: naming and test merge (plugin-side only). BUILD-PLAN→BACKLOG rename + TEST-LOG merge. Large surface area.
- L189 **0095** — /sovtest skill E2E validation. **PARKED.** Needs test plan rewrite after 0120 ships.

## Open questions (7 entries, L207–L297)

- L213 **Frame-correction sweep: categorical vs conditional skip** — park, low frequency
- L225 **Remote-control standby close path unspecified** — park, very low frequency
- L237 **Dev-side session-open state summary has no template** — consider during 0122
- L249 **Sub-agent warning rule boundary for scoped work** — park, low friction
- L261 **Session-open step 2 load-purpose unstated** — consider during 0122
- L273 **Cross-reference precision across dev-side docs** — park, fix opportunistically
- L285 **Plugin testing framework beyond bespoke pytest** — park until burden grows
