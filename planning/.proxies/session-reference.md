<!-- proxy | source: planning/session-reference.md | generated: 2026-05-26 | when: dip on demand -->

# Session reference

Companion to session-protocol.md. Entry shapes, footer bump lists, testing details, planning artefact lifecycles. Don't load at session open — dip into specific sections via offset/limit.

## Sections

- L1 **Session reference** — title + orientation
- L7 **Two-write rule for canonical docs** — SHELVED in v40. Repo-root docs frozen at V39. Retained for resume-ability.
- L19 **Testing** — smoke-testing in Claude Code, pre-install options, what we don't do, where outcomes go
- L45 **Automated test suite (V53 — pytest)** — `python -m pytest tests/ -v`, coverage, fixtures, relationship to smoke tests
- L62 **Footer bumps: the full list** — plugin-side leader list (13 entries), docs-only (shelved), cross-cutting, version trackers
- L94 **Planning artefacts** — lifecycle table (9 entries: BACKLOG queued batches, drafts, INVENTORY, BACKLOG, feasibility docs, build-log, test-log, session-protocol, session-reference)
- L108 **Drafts in flight** — convention + corollary (inputs must be in repo)
- L116 **BUILD-LOG entry shape** — per-session file in build-log/, 4-section template, INDEX.md prepend
- L134 **Open-questions entry shape** — 5-field template + 4 graduation paths
- L162 **TEST-LOG entry shape** — 7-column table, status flips, component changes, BUILD-LOG linking
- L180 **Plugin migration context** — V17 onwards, design docs pointer
