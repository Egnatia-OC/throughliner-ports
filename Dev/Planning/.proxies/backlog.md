<!-- proxy | source: planning/BACKLOG.md | generated: 2026-05-27 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

98 shipped/cancelled batch rows (V18–0102) in table at L11–L99. 5 queued batches with full scope at L102–L209. 8 open questions at L211–L323.

## Queued batches (L102–L209)

- L108 **0088** — Build E2E test. Build-phase E2E: /sovrecap through /sovbuild through /sovclose.
- L126 **0094** — Guided testing and debugging procedure. New `/test` skill + procedure doc.
- L149 **0095** — /test skill E2E validation. Depends on 0094.
- L165 **0101** — Structured-markdown validator. PostToolUse validation for TEST-LOG, build-log, scope-context, proxies.
- L188 **0100** — Bash write-guard + skill escape guidance. Bash-matcher PreToolUse for file-write commands; escape guidance on all write-lock denies.

## Open questions (8 entries, L211–L323)

- L217 **Language setting for multi-language plugin support** — park until external testers
- L237 **UTF-8 BOM hardening for hook file reads** — low priority; one-line fix per site
- L249 **Pre-commit checkpoint as explicit checklist** — dev-side step 7 should name each artifact explicitly
- L261 **Idea sweep with explicit routing destinations** — enforce plugin's three-way triage on dev-side
- L273 **Opener routing table for dev sessions** — map session openers to what to load; park until 0102+0093 ship
- L285 **Performance section in dev build-log entries** — park until dogfooding closer
- L297 **Lost-feature sweep as a planning skill** — park until planning procedure stabilises
- L311 **Plugin testing framework beyond bespoke pytest** — park
