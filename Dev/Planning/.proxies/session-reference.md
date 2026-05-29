<!-- proxy | source: Dev/session-reference.md | generated: 2026-05-29 v135 | when: dip on demand -->

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
- L190 **Open-questions entry shape** — 5-field template + 4 graduation paths
- L228 **TEST-LOG entry shape** — 7-column table, status flips, component changes, BUILD-LOG linking
- L252 **Plugin migration context** — V17 onwards, design docs pointer
