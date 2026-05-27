<!-- proxy | source: planning/BACKLOG.md | generated: 2026-05-27 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

97 shipped/cancelled batch rows (V18–0103) in table at L11–L98. 6 queued batches with full scope at L101–L227. 9 open questions at L229–L341.

## Queued batches (L101–L227)

- L107 **0102** — Dev-side session-close convergence. Proxy regen close step + response-shape tags on session-protocol.md close steps.
- L126 **0088** — Build E2E test. Build-phase E2E: /sovrecap through /sovbuild through /sovclose.
- L144 **0094** — Guided testing and debugging procedure. New `/test` skill + procedure doc.
- L167 **0095** — /test skill E2E validation. Depends on 0094.
- L183 **0101** — Structured-markdown validator. PostToolUse validation for TEST-LOG, build-log, scope-context, proxies.
- L206 **0100** — Bash write-guard + skill escape guidance. Bash-matcher PreToolUse for file-write commands; escape guidance on all write-lock denies.

## Open questions (9 entries, L229–L341)

- L235 **Language setting for multi-language plugin support** — park until external testers
- L255 **UTF-8 BOM hardening for hook file reads** — low priority; one-line fix per site
- L267 **Pre-commit checkpoint as explicit checklist** — dev-side step 6 should name each artifact explicitly
- L279 **Idea sweep with explicit routing destinations** — enforce plugin's three-way triage on dev-side
- L291 **Opener routing table for dev sessions** — map session openers to what to load; park until 0102+0093 ship
- L303 **Performance section in dev build-log entries** — park until dogfooding closer
- L315 **Lost-feature sweep as a planning skill** — park until planning procedure stabilises
- L329 **Plugin testing framework beyond bespoke pytest** — park
