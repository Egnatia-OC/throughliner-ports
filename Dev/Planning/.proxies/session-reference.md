<!-- proxy | source: Dev/session-reference.md | generated: 2026-05-29 v139 | when: dip on demand -->

# Session reference

Companion to session-protocol.md. Entry shapes, footer bump lists, testing details, planning artefact lifecycles. Don't load at session open — dip into specific sections via offset/limit.

## Sections

- L7 **Two-write rule for canonical docs — RETIRED** — repo-root docs-only set deleted in v95. Historical pointers only.
- L13 **Testing** — smoke-testing in Claude Code, pre-install options, what we don't do, where outcomes go
- L33 **Automated test suite (V53 — pytest)** — `python -m pytest tests/ -v`, coverage, fixtures, relationship to smoke tests
- L55 **Response-shape tags** — five tags ([SILENT], [BRIEF], [SEQUENCE], [DISCUSS], [PROMPT])
- L69 **Footer bumps: the full list** — plugin-side leader list (12 entries), cross-cutting, version trackers
- L109 **Planning artefacts** — lifecycle table (8 entries)
- L122 **Drafts in flight** — convention + corollary (inputs must be in repo)
- L130 **BUILD-LOG entry shape** — per-session file in build-log/, 4-section template, INDEX.md prepend
- L156 **Queued batch entry shape** — 6-field template (Goal, Approach, Inputs, Outputs, Success criteria, Risks/dependencies), heading number, field order, parked batches, sizing, plugin-side disambiguation
- L192 **Open-questions entry shape** — 5-field template + 4 graduation paths + plugin-consideration note
- L232 **Ideas section entry shape** — YYYY-MM-DD one-liner format, lifecycle, bar vs OQs, plugin equivalent
- L252 **TEST-LOG entry shape** — 7-column table (Component before Test), status flips, component changes, BUILD-LOG linking
- L276 **Test sessions index shape** — INDEX.md format, naming convention, maintenance
- L294 **INVENTORY entry shape** — 5-section structure, per-component entry formats, when updated
- L317 **Research folder file shape** — naming, three structure patterns, persistence, maintenance
- L337 **Dev-side proxy file spec** — location, HTML comment header, body format, BACKLOG proxy difference, regeneration
- L369 **Plugin migration context** — V17 onwards, design docs pointer
