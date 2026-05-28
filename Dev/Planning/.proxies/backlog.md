<!-- proxy | source: Dev/Planning/BACKLOG.md | generated: 2026-05-28 v122 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

116 shipped/cancelled batch rows (V18–0125) in table at L12–L116. 6 queued batches with full scope at L120–L217. 7 open questions at L220–L321.

## Queued batches (L120–L217) — dev-side first, then plugin-side, then parked

- L126 **0118** — Scripted close mechanicals (dev-side). Python script for footer bumps, version updates, proxy regen. Dev-side only.
- L140 **0119** — Two-turn close procedure (dev-side). Judgment + mechanical pass with `/compact` boundary. Depends on 0118.
- L156 **0122** — Dev-side structure mirroring audit. Compare dev-side vs plugin-side patterns. Absorbs 0120's dev-side work. Depends on 0121.
- L172 **0123** — Plugin-side close mechanicals + two-turn procedure. Ports 0118+0119 to plugin. Depends on dev-side 0118+0119.
- L188 **0120** — BACKLOG convergence: naming and test merge (plugin-side only). BUILD-PLAN→BACKLOG rename + TEST-LOG merge. Large surface area.
- L202 **0095** — /sovtest skill E2E validation. **PARKED.** Needs test plan rewrite after 0120 ships.

## Open questions (7 entries, L220–L321)

- L226 **Frame-correction sweep: categorical vs conditional skip** — park, low frequency
- L238 **Remote-control standby close path unspecified** — park, very low frequency
- L249 **Dev-side session-open state summary has no template** — consider during 0122
- L261 **Sub-agent warning rule boundary for scoped work** — park, low friction
- L273 **Session-open step 2 load-purpose unstated** — consider during 0122
- L285 **Cross-reference precision across dev-side docs** — park, fix opportunistically
- L297 **Plugin testing framework beyond bespoke pytest** — park until burden grows
