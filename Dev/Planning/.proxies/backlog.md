<!-- proxy | source: planning/BACKLOG.md | generated: 2026-05-27 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

96 shipped/cancelled batch rows (V18–0099) in table at L11–L97. 7 queued batches with full scope at L100–L253. 7 open questions at L255–L347.

## Queued batches (L100–L253)

- L106 **0103** — /tersify skill for doc compression. Guided triage + audit for reducing token cost in SOT docs.
- L133 **0102** — Dev-side session-close convergence. Proxy regen close step + response-shape tags on session-protocol.md close steps.
- L152 **0088** — Build E2E test. Build-phase E2E: /sovrecap through /sovbuild through /sovclose.
- L170 **0094** — Guided testing and debugging procedure. New `/test` skill + procedure doc.
- L193 **0095** — /test skill E2E validation. Depends on 0094.
- L209 **0101** — Structured-markdown validator. PostToolUse validation for TEST-LOG, build-log, scope-context, proxies.
- L232 **0100** — Bash write-guard + skill escape guidance. Bash-matcher PreToolUse for file-write commands; escape guidance on all write-lock denies.

## Open questions (7 entries, L255–L347)

- L261 **Language setting for multi-language plugin support** — park until external testers
- L273 **Pre-commit checkpoint as explicit checklist** — dev-side step 6 should name each artifact explicitly
- L285 **Idea sweep with explicit routing destinations** — enforce plugin's three-way triage on dev-side
- L297 **Opener routing table for dev sessions** — map session openers to what to load; park until 0102+0093 ship
- L309 **Performance section in dev build-log entries** — park until dogfooding closer
- L321 **Lost-feature sweep as a planning skill** — park until planning procedure stabilises
- L335 **Plugin testing framework beyond bespoke pytest** — park
