<!-- proxy | source: Dev/session-protocol.md | generated: 2026-05-27 | when: every session open -->

# Session protocol

Always-read file. Session lifecycle: open → middle → close. Opener routing table. Differentiated close paths. Doc-code parity audit. Version numbers.

## Sections

- L1 **Session protocol** — title + orientation (points to session-reference.md for entry shapes, footer lists, etc.)
- L11 **The unit of work: a session** — one session = one commit + one tag
- L15 **Three numbers to keep distinct** — session tag (v), method version (V), batch number (NNNN)
- L29 **Session open** — 5-step load sequence (git describe, read plugin docs, read BACKLOG.md, batch-input check, carried-forward read-back)
- L43 **Opener routing table** — 6 session types: implementation, doc-only, planning, ideation, E2E test, remote-control standby → load/skip/middle/close
- L60 **Session middle** — three shapes: implementation, doc-only, planning
- L74 **Session close** — two paths based on session type
- L78 **Implementation close (full)** — 11 steps: parity → frame sweep → footers → build-log → idea sweep (3-way triage) → proxies → pre-commit checkpoint (named artifacts) → commit → tag → remove batch → push
- L117 **Lighter close** — 8 steps: idea sweep → build-log → footers → proxies → checkpoint → commit → tag → push. Skips doc-code parity and frame-correction. Conditional batch removal.
- L151 **Batch-ordering audit** — 4 checks after BACKLOG structural changes: forward-dep scan, stale-ref scan, reorder, fix scope text
- L164 **Doc-code parity** — during-session + close-time audit (6-item checklist)
- L183 **Guide parity (crash-course/)** — data-source/data-transform attribute chain
