<!-- proxy | source: Dev/Planning/BACKLOG.md | generated: 2026-05-27 v110 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

100 shipped/cancelled batch rows (V18–0109) in table at L11–L107. 6 queued batches with full scope at L110–L237. 1 open question at L240–L258.

## Queued batches (L110–L237)

- L116 **0088** — Build E2E test. Build-phase E2E: /sovrecap through /sovbuild through /sovclose.
- L132 **0095** — /sovtest skill E2E validation. Depends on 0094 (shipped v100).
- L148 **0110** — Queued-pipeline staleness sweep at close. Includes lost-feature sweep fold-in and concurrent-build detection.
- L166 **0112** — Skill split: `/sovdeliberate`, `/sovideate`, and `/sovplan` narrowing. Includes build-snapshot architecture, BACKLOG→BUILD-PLAN rename, mode-aware git steps, OQ accumulation nudge.
- L198 **0113** — Session-length safeguards. Pre-build sizing + mid-session compact nudge.
- L216 **0114** — Language setting for multi-language plugin support. Includes BOM hardening fold-in.

## Open questions (1 entry, L240–L258)

- L246 **Plugin testing framework beyond bespoke pytest** — park until test maintenance burden grows
