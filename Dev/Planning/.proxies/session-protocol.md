<!-- proxy | source: Dev/session-protocol.md | generated: 2026-05-29 v135 | when: every session open -->

# Session protocol

Always-read file. Session lifecycle: open → middle → close. Opener routing table with blended-opener priority rule. Differentiated close paths. Doc-code parity audit. Version numbers.

## Sections

- L1 **Session protocol** — title + orientation (points to session-reference.md for entry shapes, footer lists, etc.)
- L11 **The unit of work: a session** — one session = one commit + one tag
- L15 **Three numbers to keep distinct** — session tag (v), method version (V), batch number (NNNN)
- L29 **Session open** — 4-step load sequence (git describe with fallback, read plugin docs, read BACKLOG.md, batch-input check)
- L46 **Opener routing table** — 6 session types: implementation, doc-only, planning, ideation, E2E test, remote-control standby → load/skip/middle/close. Blended-opener priority rule (L56): E2E > Implementation > Planning > Ideation > Doc-only > Standby. Informal-modifier note.
- L65 **Session middle** — three shapes: implementation, doc-only, planning
- L79 **Session close** — two paths, both split into judgment pass + `/compact` boundary + mechanical pass
- L83 **Implementation close (full)** — 11 steps in two turns. Turn 1 (judgment): parity → frame sweep → build-log → idea sweep (3-way triage) → turn boundary (`/compact`). Turn 2 (mechanical): footers (bump_version.py) → proxies (bump_version.py + review) → pre-commit checkpoint → commit → tag → push. Uses `git diff` as dev-side equivalent of plugin's `## Close handoff` section.
- L136 **Lighter close** — 9 steps in two turns. Turn 1 (judgment): idea sweep → build-log → turn boundary (`/compact`). Turn 2 (mechanical): footers (bump_version.py) → proxies (bump_version.py + review) → checkpoint → commit → tag → push. Skips doc-code parity and frame-correction. Conditional batch removal in checkpoint.
- L185 **Batch-ordering audit** — 4 checks after BACKLOG structural changes: forward-dep scan, stale-ref scan, reorder, fix scope text
- L198 **Doc-code parity** — during-session + close-time audit (6-item checklist)
- L217 **Guide parity (Guides/crash-course/)** — data-source/data-transform attribute chain
