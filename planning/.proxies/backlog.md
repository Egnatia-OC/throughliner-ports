<!-- proxy | source: planning/BACKLOG.md | generated: 2026-05-26 | when: session open (scan OQs); planning sessions (full routing) -->

# BACKLOG — Dev-side

93 batches (V18–0095 + V60+). 67 shipped, 3 cancelled, 1 superseded, 1 parked, 21 queued/active. 15 open questions.

## Batch list — active and queued only

Shipped/cancelled/superseded/parked rows omitted. Dip into full file (L11–L93) for history.

- L90 **0093** — Dev-side folder restructure. Move all dev-side content into `dev/`; delete frozen V39 docs and `plugin.zip`. Depends on 0091 (shipped).
- L84 **0096** — Manifest rationale field. One-line "why it exists" on MANIFEST entries.
- L85 **0088** — Build E2E test. Build-phase E2E: /before-build through /build through after-build.
- L91 **0094** — Guided testing and debugging procedure. New `/test` skill + procedure doc.
- L92 **0095** — /test skill E2E validation. Depends on 0094.
- L93 **V60+** — Remaining parked open questions.

## Open questions (15 entries, L123–L345)

- L129 **Retire "build session" — BACKLOG as sole work tracker** — parent question; cycle is ceremony on top of enforcement that works without it
- L149 **Session close as a `/close` skill** — 10-step close is failure-prone from memory; design session needed
- L145 **Planning as a `/plan` skill** — only core workflow with no skill entry point; design session needed
- L161 **Merge `/before-build` into `/build`** — UX simplification; lower priority; design session needed
- L179 **Scope file split: separate planning from build content** — 0091 shipped; still parked until split design emerges
- L143 **Remove timestamps from build-log** — audit which docs carry them
- L155 **Bulk-tersify skill for doc compression** — park until proxy layer + folder restructure ship
- L169 **Lost-feature sweep as a planning skill** — park until planning procedure stabilises
- L183 **Project-boundary hook bypass via Bash** — park, revisit if E2E surfaces writes
- L197 **Structured-markdown validator** — promote after proxy layer ships
- L209 **Plugin testing framework beyond bespoke pytest** — park
- L221 **Plugin settings layer / per-project config** — park
- L233 **Red-flag / threat-class marker** — ready to promote
- L249 **Graduate sovereign implementer onto sovereign implementer** — indefinitely shelved
- L266 **Prose-only rewrite of the method** — indefinitely parked
