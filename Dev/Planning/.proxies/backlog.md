<!-- proxy | source: Dev/Planning/BACKLOG.md | generated: 2026-05-28 v124 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

118 shipped/cancelled batch rows (V18–0119) in table at L12–L118. 4 queued batches with full scope at L126–L190. 7 open questions at L192–L282.

## Queued batches (L126–L190) — dev-side first, then plugin-side, then parked

- L128 **0122** — Dev-side structure mirroring audit. Compare dev-side vs plugin-side patterns. Absorbs 0120's dev-side work. Depends on 0121.
- L144 **0123** — Plugin-side close mechanicals + two-turn procedure. Ports 0118+0119 to plugin. Depends on dev-side 0118+0119.
- L160 **0120** — BACKLOG convergence: naming and test merge (plugin-side only). BUILD-PLAN→BACKLOG rename + TEST-LOG merge. Large surface area.
- L174 **0095** — /sovtest skill E2E validation. **PARKED.** Needs test plan rewrite after 0120 ships.

## Open questions (7 entries, L192–L282)

- L198 **Frame-correction sweep: categorical vs conditional skip** — park, low frequency
- L210 **Remote-control standby close path unspecified** — park, very low frequency
- L222 **Dev-side session-open state summary has no template** — consider during 0122
- L234 **Sub-agent warning rule boundary for scoped work** — park, low friction
- L246 **Session-open step 2 load-purpose unstated** — consider during 0122
- L258 **Cross-reference precision across dev-side docs** — park, fix opportunistically
- L270 **Plugin testing framework beyond bespoke pytest** — park until burden grows
