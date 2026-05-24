# 0062 — HTML Crash Course guide

## Goal

Multi-page HTML guide in `crash-course/` for testers and early adopters. Same content as the reference manual, restructured for approachability: multi-page nav, SVG doc icons, plain-English rewording. A three-category tag system (`verbatim`/`adapted`/`added`) makes manual→guide parity mechanical.

## Inputs

- `Reference manual.md` (renamed in 0061)
- `plugin/docs/DOC-STRUCTURE.md`, `plugin/docs/VOCABULARY.md`

## Outputs

- `crash-course/` folder: 8 HTML pages, `styles.css`, `nav.js` (or CSS-only), SVG assets
- Updated `BUILD-METHOD.md` parity rules (spec → manual → guide chain)

## The 8 pages

1. **Home** — 30-second pitch: what, who, cost (two-session minimum).
2. **The cycle** — planning → before-build → build → after-build flow + user expectations.
3. **Your docs** — SVG icons for each project doc with plain-English descriptions.
4. **Getting started** — install, /setup cases, first session.
5. **Walkthrough** — Taskflow Day 1 worked example.
6. **The disciplines** — four mechanisms, feature pipeline, batch anatomy.
7. **Why the rules** — one block per rule with reasoning.
8. **Reference** — test types, editing surfaces, permissions, safety net, plugin internals, caveats.

Pages 1–5 = "get operational." Pages 6–8 = depth.

## Tag system

- `data-source="manual:<section-id>"` — source section
- `data-transform="verbatim"` — word-for-word; auto-update
- `data-transform="adapted"` — same concept, plainer; flag for review
- `data-transform="added"` — new context; no auto-update unless concept removed

## Open questions

1. CSS-only nav vs JS. Recommend CSS-only.
2. SVG icon style. Flat/minimal with doc name centered.
3. Hosting. Recommend local-only for now.
4. Scope. Recommend all 8 pages — content exists, work is structural.

## Risks / dependencies

- Depends on 0061 (name freed).
- Two-step parity chain is more maintenance. Tags make catch-up tractable.
