<!-- proxy | source: Dev/Planning/BACKLOG.md | generated: 2026-05-27 v103 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

98 shipped/cancelled batch rows (V18–0102) in table at L11–L99. 10 queued batches with full scope at L103–L257. 8 open questions at L259–L371.

## Queued batches (L103–L257)

- L109 **0111** — Dev-side session-protocol procedural convergence. Six plugin-side structures into session-protocol.md. Resolves 3 OQs.
- L129 **0088** — Build E2E test. Build-phase E2E: /sovrecap through /sovbuild through /sovclose.
- L145 **0095** — /sovtest skill E2E validation. Depends on 0094 (shipped v100).
- L161 **0104** — Sov-prefix rename for remaining skills. `/setup` → `/sovsetup`, `/research` → `/sovresearch`, `/test` → `/sovtest`, `/tersify` → `/sovtersify`.
- L175 **0105** — `_method/` orientation in CLAUDE.md template. Depends on 0104.
- L189 **0106** — Post-build proxy regeneration in `/sovclose`.
- L203 **0107** — Unclosed-build detection in SessionStart.
- L217 **0108** — Guided rollback procedure (`/sovrevert`). Depends on 0104.
- L231 **0109** — `/sovsetup` case 4 scaffold drift detection.
- L245 **0110** — Queued-pipeline staleness sweep at close.

## Open questions (8 entries, L259–L371)

- L265 **Language setting for multi-language plugin support** — park until external testers
- L285 **UTF-8 BOM hardening for hook file reads** — low priority; one-line fix per site
- L297 **Pre-commit checkpoint as explicit checklist** — dev-side step should name each artifact explicitly
- L309 **Idea sweep with explicit routing destinations** — enforce plugin's three-way triage on dev-side
- L321 **Opener routing table for dev sessions** — map session openers to what to load
- L333 **Performance section in dev build-log entries** — park until dogfooding closer
- L345 **Lost-feature sweep as a planning skill** — park until planning procedure stabilises
- L359 **Plugin testing framework beyond bespoke pytest** — park
