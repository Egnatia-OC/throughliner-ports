<!-- proxy | source: Dev/Planning/BACKLOG.md | generated: 2026-05-27 v105 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

99 shipped/cancelled batch rows (V18–0104) in table at L11–L101. 8 queued batches with full scope at L105–L225. 5 open questions at L227–L303.

## Queued batches (L105–L225)

- L111 **0088** — Build E2E test. Build-phase E2E: /sovrecap through /sovbuild through /sovclose.
- L127 **0095** — /sovtest skill E2E validation. Depends on 0094 (shipped v100).
- L143 **0105** — `_method/` orientation in CLAUDE.md template. Depends on 0104 (shipped v105).
- L157 **0106** — Post-build proxy regeneration in `/sovclose`.
- L171 **0107** — Unclosed-build detection in SessionStart.
- L185 **0108** — Guided rollback procedure (`/sovrevert`). Depends on 0104 (shipped v105).
- L199 **0109** — `/sovsetup` case 4 scaffold drift detection.
- L213 **0110** — Queued-pipeline staleness sweep at close.

## Open questions (5 entries, L227–L303)

- L233 **Language setting for multi-language plugin support** — park until external testers
- L253 **UTF-8 BOM hardening for hook file reads** — low priority; one-line fix per site
- L265 **Performance section in dev build-log entries** — park until dogfooding closer
- L277 **Lost-feature sweep as a planning skill** — park until planning procedure stabilises
- L291 **Plugin testing framework beyond bespoke pytest** — park
