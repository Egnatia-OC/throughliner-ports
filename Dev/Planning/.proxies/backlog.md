<!-- proxy | source: Dev/Planning/BACKLOG.md | generated: 2026-05-28 v120 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

116 shipped/cancelled batch rows (V18–0121) in table at L13–L116. 8 queued batches with full scope at L119–L250. 12 open questions at L252–L402.

## Queued batches (L119–L250) — dev-side first, then plugin-side, then parked

- L125 **0124** — Dev-side close procedure fixes. Three fixes: batch-removal timing asymmetry, stale step-number xref, proxy format spec unlocated. No deps.
- L142 **0125** — Dev-side opener routing completeness. Blended-opener rule + disambiguation sequencing + git-unavailable fallback. No deps.
- L158 **0118** — Scripted close mechanicals (dev-side). Python script for footer bumps, version updates, proxy regen. Dev-side only.
- L172 **0119** — Two-turn close procedure (dev-side). Judgment + mechanical pass with `/compact` boundary. Depends on 0118.
- L188 **0122** — Dev-side structure mirroring audit. Compare dev-side vs plugin-side patterns. Absorbs 0120's dev-side work. Depends on 0121.
- L204 **0123** — Plugin-side close mechanicals + two-turn procedure. Ports 0118+0119 to plugin. Depends on dev-side 0118+0119.
- L220 **0120** — BACKLOG convergence: naming and test merge (plugin-side only). BUILD-PLAN→BACKLOG rename + TEST-LOG merge. Large surface area.
- L234 **0095** — /sovtest skill E2E validation. **PARKED.** Needs test plan rewrite after 0120 ships.

## Open questions (12 entries, L252–L402)

- L258 **Lighter close step reordering rationale** — fold into 0124 or defer
- L270 **Frame-correction sweep: categorical vs conditional skip** — park, low frequency
- L282 **Doc-only batch-input check: skip rule underspecified** — fold into 0124/0125
- L294 **Remote-control standby close path unspecified** — park, very low frequency
- L306 **Informal opener modifiers unmapped** — consider folding into 0125
- L318 **Dev-side session-open state summary has no template** — consider during 0122
- L330 **Sub-agent warning rule boundary for scoped work** — park, low friction
- L342 **Session-open step 2 load-purpose unstated** — consider during 0122
- L354 **Duplicate batch 0102 in shipped batch table** — fix as one-line cleanup
- L366 **Cross-reference precision across dev-side docs** — park, fix opportunistically
- L378 **Lighter-close naming vs doc-only batches** — consider during 0124
- L390 **Plugin testing framework beyond bespoke pytest** — park until burden grows
