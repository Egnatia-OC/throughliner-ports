<!-- proxy | source: Dev/session-protocol.md | generated: 2026-05-29 v136 | when: every session open -->

# Session protocol

Always-read file. Session lifecycle: open → middle → close. Opener routing table with blended-opener priority rule. Differentiated close paths. Doc-code parity audit. Version numbers.

## Sections

- L1 **Session protocol** — title + orientation (points to session-reference.md for entry shapes, footer lists, etc.)
- L11 **The unit of work: a session** — one session = one commit + one tag
- L15 **Three numbers to keep distinct** — session tag (v), method version (V), batch number (NNNN)
- L29 **Session open** — 5-step load sequence (git describe with fallback, read plugin docs, read BACKLOG.md, batch-input check, OQ blocker check, state summary)
- L47 **Opener routing table** — 6 session types: implementation, doc-only, planning, ideation, E2E test, remote-control standby → load/skip/middle/close. Blended-opener priority rule (L62): E2E > Implementation > Planning > Ideation > Doc-only > Standby. Informal-modifier note.
- L66 **Session middle** — three shapes: implementation, doc-only, planning
- L78 **Mid-session rules** — no stealth fixes, no unplanned refactoring (with prerequisite and re-batching carve-outs), mid-session compact nudge
- L88 **Session handoff** — 4-step protocol for when context runs low mid-session (tick completed, annotate in-progress, record decisions, notify). Handoff notes block consumed by next session.
- L101 **Session close** — mandatory (not advisory). Two paths, both split into judgment pass + `/compact` boundary + mechanical pass
- L107 **Implementation close (full)** — 11 steps in two turns. Turn 1 (judgment): parity → frame sweep → build-log → idea sweep (4-way triage incl. red-flag routing) → turn boundary (`/compact`). Turn 2 (mechanical): footers (bump_version.py) → proxies (bump_version.py + review) → pre-commit checkpoint → commit → tag → push. Uses `git diff` as dev-side equivalent of plugin's `## Close handoff` section.
- L161 **Lighter close** — 9 steps in two turns. Turn 1 (judgment): idea sweep → build-log → turn boundary (`/compact`). Turn 2 (mechanical): footers (bump_version.py) → proxies (bump_version.py + review) → checkpoint → commit → tag → push. Skips doc-code parity and frame-correction. Conditional batch removal in checkpoint.
- L210 **Batch-ordering audit** — 4 checks after BACKLOG structural changes: forward-dep scan, stale-ref scan, reorder, fix scope text
- L223 **Doc-code parity** — during-session + close-time audit (6-item checklist)
- L242 **Guide parity (Guides/crash-course/)** — data-source/data-transform attribute chain
