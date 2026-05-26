<!-- proxy | source: planning/session-protocol.md | generated: 2026-05-26 | when: every session open -->

# Session protocol

Always-read file. Session lifecycle: open → middle → close. Doc-code parity audit. Three version numbers.

## Sections

- L1 **Session protocol** — title + orientation (points to session-reference.md for entry shapes, footer lists, etc.)
- L12 **The unit of work: a session** — one session = one commit + one tag
- L16 **Three numbers to keep distinct** — session tag (v), method version (V), scope-file number (NNNN)
- L34 **Session open** — 4-step load sequence (git describe, read plugin docs, scan OQs, read scope file)
- L46 **Session middle** — three shapes: implementation, doc-only, planning
- L58 **Session close: 10 steps** — parity → frame sweep → footers → build-log → ideas → checkpoint → commit → tag → delete scope → push
- L82 **Doc-code parity** — during-session + close-time audit (6-item checklist)
- L100 **Guide parity (crash-course/)** — data-source/data-transform attribute chain
