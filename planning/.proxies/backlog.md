<!-- proxy | source: planning/BACKLOG.md | generated: 2026-05-26 | when: session open (full read recommended); planning sessions -->

# BACKLOG — Dev-side

88 shipped/cancelled batch rows (V18–0092) in table at L11–L87. 5 queued batches with full scope at L91–L207. 15 open questions at L208–L415.

## Queued batches (L91–L207)

- L97 **0096** — Manifest rationale field. One-line "why it exists" on MANIFEST entries.
- L117 **0088** — Build E2E test. Build-phase E2E: /before-build through /build through /sovclose.
- L135 **0093** — Dev-side folder restructure. Move all dev-side content into `dev/`.
- L171 **0094** — Guided testing and debugging procedure. New `/test` skill + procedure doc.
- L194 **0095** — /test skill E2E validation. Depends on 0094.

## Open questions (15 entries, L208–L415)

- L214 **Retire "build session" — BACKLOG as sole work tracker** — parent question; cycle is ceremony on top of enforcement
- L228 **Session close as a `/close` skill** — 10-step close is failure-prone; design session needed
- L242 **Planning as a `/plan` skill** — only core workflow with no skill entry point
- L256 **Merge `/before-build` into `/build`** — UX simplification; lower priority
- L270 **Separate planning content from build content** — scope files eliminated v91; internal-structure question remains; parked
- L284 **Remove timestamps from build-log** — audit which docs carry them
- L296 **Bulk-tersify skill for doc compression** — park until doc structure stable
- L310 **Lost-feature sweep as a planning skill** — park until planning procedure stabilises
- L324 **Project-boundary hook bypass via Bash** — park
- L338 **Structured-markdown validator** — promote after proxy layer ships
- L350 **Plugin testing framework beyond bespoke pytest** — park
- L362 **Plugin settings layer / per-project config** — park
- L374 **Red-flag / threat-class marker** — ready to promote
- L388 **Graduate sovereign implementer** — indefinitely shelved
- L407 **Prose-only rewrite** — indefinitely parked
