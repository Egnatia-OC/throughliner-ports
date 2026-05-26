<!-- proxy | source: planning/BACKLOG.md | generated: 2026-05-26 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

95 shipped/cancelled batch rows (V18–0099) in table at L11–L96. 9 queued batches with full scope at L98–L309. 7 open questions at L312–L407.

## Queued batches (L98–L309)

- L104 **0098** — /sovplan skill + planning ordering principles. Planning skill wrapping planning.md; ordering principles; SessionStart top-3 summary; universal `[SECURITY]` marker.
- L134 **0096** — Manifest rationale field. One-line "why it exists" on MANIFEST entries.
- L154 **0102** — Dev-side session-close convergence. Proxy regen close step + response-shape tags on session-protocol.md close steps.
- L173 **0093** — Dev-side folder restructure. Move all dev-side content into `dev/`.
- L209 **0088** — Build E2E test. Build-phase E2E: /sovrecap through /sovbuild through /sovclose.
- L227 **0094** — Guided testing and debugging procedure. New `/test` skill + procedure doc.
- L250 **0095** — /test skill E2E validation. Depends on 0094.
- L266 **0101** — Structured-markdown validator. PostToolUse validation for TEST-LOG, build-log, scope-context, proxies.
- L289 **0100** — Bash write-guard + skill escape guidance. Bash-matcher PreToolUse for file-write commands; escape guidance on all write-lock denies.

## Open questions (7 entries, L312–L407)

- L318 **Pre-commit checkpoint as explicit checklist** — dev-side step 6 should name each artifact explicitly
- L330 **Idea sweep with explicit routing destinations** — enforce plugin's three-way triage on dev-side
- L342 **Opener routing table for dev sessions** — map session openers to what to load; park until 0102+0093 ship
- L354 **Performance section in dev build-log entries** — park until dogfooding closer
- L366 **Bulk-tersify skill for doc compression** — park until doc structure stable
- L380 **Lost-feature sweep as a planning skill** — park until planning procedure stabilises
- L394 **Plugin testing framework beyond bespoke pytest** — park
