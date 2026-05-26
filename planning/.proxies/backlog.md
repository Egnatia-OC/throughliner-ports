<!-- proxy | source: planning/BACKLOG.md | generated: 2026-05-26 | when: session open (scan OQs); planning sessions (full routing) -->

# BACKLOG — Dev-side

93 batches (V18–0095 + V60+). 66 shipped, 3 cancelled, 1 superseded, 1 parked, 22 queued/active. 11 open questions.

## Batch list — active and queued only

Shipped/cancelled/superseded/parked rows omitted. Dip into full file (L11–L93) for history.

- L89 **0092** — BUILD-METHOD split and dev-side proxies. Depends on 0091 (shipped v87).
- L90 **0093** — Dev-side folder restructure. Depends on 0091, 0092.
- L84 **0096** — Manifest rationale field. One-line "why it exists" on MANIFEST entries.
- L85 **0088** — Build E2E test. Build-phase E2E: /before-build through /build through after-build.
- L91 **0094** — Guided testing and debugging procedure. New `/test` skill + procedure doc.
- L92 **0095** — /test skill E2E validation. Depends on 0094.
- L93 **V60+** — Remaining parked open questions.

## Open questions (11 entries, L123–L275)

- L129 **Scope file split: separate planning from build content** — 0091 shipped; still parked until split design emerges
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
