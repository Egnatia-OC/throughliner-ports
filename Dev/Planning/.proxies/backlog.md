<!-- proxy | source: Dev/Planning/BACKLOG.md | generated: 2026-05-28 v121 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

115 shipped/cancelled batch rows (V18–0124) in table at L12–L115. 7 queued batches with full scope at L119–L233. 8 open questions at L235–L337.

## Queued batches (L119–L233) — dev-side first, then plugin-side, then parked

- L125 **0125** — Dev-side opener routing completeness. Blended-opener rule + disambiguation sequencing + git-unavailable fallback. No deps.
- L141 **0118** — Scripted close mechanicals (dev-side). Python script for footer bumps, version updates, proxy regen. Dev-side only.
- L155 **0119** — Two-turn close procedure (dev-side). Judgment + mechanical pass with `/compact` boundary. Depends on 0118.
- L171 **0122** — Dev-side structure mirroring audit. Compare dev-side vs plugin-side patterns. Absorbs 0120's dev-side work. Depends on 0121.
- L187 **0123** — Plugin-side close mechanicals + two-turn procedure. Ports 0118+0119 to plugin. Depends on dev-side 0118+0119.
- L203 **0120** — BACKLOG convergence: naming and test merge (plugin-side only). BUILD-PLAN→BACKLOG rename + TEST-LOG merge. Large surface area.
- L217 **0095** — /sovtest skill E2E validation. **PARKED.** Needs test plan rewrite after 0120 ships.

## Open questions (8 entries, L235–L337)

- L241 **Frame-correction sweep: categorical vs conditional skip** — park, low frequency
- L253 **Remote-control standby close path unspecified** — park, very low frequency
- L265 **Informal opener modifiers unmapped** — consider folding into 0125
- L277 **Dev-side session-open state summary has no template** — consider during 0122
- L289 **Sub-agent warning rule boundary for scoped work** — park, low friction
- L301 **Session-open step 2 load-purpose unstated** — consider during 0122
- L313 **Cross-reference precision across dev-side docs** — park, fix opportunistically
- L325 **Plugin testing framework beyond bespoke pytest** — park until burden grows
