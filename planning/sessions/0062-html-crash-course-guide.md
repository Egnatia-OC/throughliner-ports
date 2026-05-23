# 0062 — HTML Crash Course guide

## Goal

Create a multi-page HTML guide in its own folder, taking the "Crash Course" name from the renamed reference manual (0061). The guide is aimed at testers and early adopters — the same content as the reference manual but structured for approachability: multi-page navigation, SVG doc icons, value-proposition context, and plain-English rewording of technical passages. A three-category tag system makes the manual → guide parity chain mechanical.

## Inputs

- `Reference manual.md` (renamed from `Crash course.md` in 0061 — the factual source)
- The 8-page structure sketched in ideation (see below)
- `plugin/docs/DOC-STRUCTURE.md` (for accurate doc descriptions)
- `plugin/docs/VOCABULARY.md` (for term definitions)

## Outputs

- `crash-course/` folder at repo root containing:
  - `index.html` — home page (what this is, who it's for)
  - `cycle.html` — the four-phase cycle at a glance, with user expectations woven in
  - `docs.html` — SVG doc-icon map with plain-English descriptions of each project doc
  - `getting-started.html` — install, /setup cases, first session
  - `walkthrough.html` — Taskflow Day 1 worked example
  - `disciplines.html` — the four core mechanisms, feature pipeline, batch anatomy
  - `why.html` — reasoning behind each rule
  - `reference.html` — test types, editing surfaces, permissions, safety net, what's inside the plugin, caveats
  - `styles.css` — shared stylesheet
  - `nav.js` — left-sidebar outline navigation (or CSS-only if feasible)
  - SVG assets for the doc-icon map
- Updated `BUILD-METHOD.md` doc-code parity rules to include the two-step chain: spec → reference manual → HTML guide
- Updated `CLAUDE.md` to reference the new guide

## The tag system

Each HTML page uses data attributes to mark content origin relative to the reference manual:

- `data-source="manual:<section-id>"` — which manual section this content derives from
- `data-transform="verbatim"` — copied word-for-word from the manual; auto-update on manual change
- `data-transform="adapted"` — same concept, plainer language; flag for review on manual change
- `data-transform="added"` — value-proposition or explanatory content not in the manual; no auto-update needed unless the underlying concept was removed or fundamentally changed

The parity pass at session close: update the reference manual first (existing process), then scan the HTML guide's tagged sections for any whose `data-source` references a changed manual section. Verbatim sections update automatically; adapted sections get flagged; added sections are left alone.

## The 8-page structure

1. **Home** (`index.html`) — 30-second pitch: what the plugin does, who it's for, what it costs (two-session minimum per feature). Short. Links to "start here."
2. **The cycle** (`cycle.html`) — at-a-glance flow of planning → before-build → build → after-build. What happens in each phase. What's expected of you at each stage (user expectations woven in, not a separate list). Possibly a simple flow diagram.
3. **Your docs** (`docs.html`) — SVG icons for each project doc (CLAUDE.md, UX.md, BACKLOG/, MANIFEST.md, TEST-LOG.md, build-log/). Each icon carries the doc name; below it, a plain-English sentence about what the doc is and why you care.
4. **Getting started** (`getting-started.html`) — install steps, the five /setup cases, first session walkthrough. Practical, step-by-step.
5. **Walkthrough** (`walkthrough.html`) — Taskflow Day 1. The worked example from the manual, lightly edited for HTML format.
6. **The disciplines** (`disciplines.html`) — the four core mechanisms ("user needs this because" line, flag taxonomy, feature pipeline, test-confirmation gate). "The method absorbs mid-stream ideation." Batch anatomy.
7. **Why the rules** (`why.html`) — one block per rule, explaining the reasoning. For the tester who hits something that feels arbitrary. Includes tag-and-push reasoning (why you should commit and tag after every build).
8. **Reference** (`reference.html`) — test types and Claude/user split, editing surfaces, permissions and modes, safety net, what's inside the plugin, caveats, landscape comparison, "when you need more."

Pages 1–5 are the "get operational" path. Pages 6–8 are depth for when you want it.

## Success criteria

- The 8 HTML pages render correctly in a browser with left-nav outline navigation
- Every factual claim in the guide matches the reference manual
- The tag system is applied consistently — every content section carries `data-source` and `data-transform` attributes
- SVG doc icons render on the docs page
- A parity pass can mechanically identify which guide sections need review after a manual change

## Open questions for this session

1. **CSS-only nav vs JavaScript.** A left-sidebar outline could be CSS-only (using anchor links and `:target` or details/summary) or use minimal JS for expand/collapse and scroll-spy. Recommend CSS-only for simplicity — the guide is static content, not an app.
2. **SVG icon style.** Flat/minimal document icons with the doc name centered? Or something more illustrative? The user mentioned "large svg icons of pages with doc names in the middle" — confirm style before building.
3. **Where to host.** The guide is static HTML in the repo. GitHub Pages could serve it directly from the `crash-course/` folder. Or it stays local-only for now and hosting comes later. Recommend local-only for this session; hosting is a separate decision.
4. **Initial content scope.** Port all 8 pages in one session, or start with pages 1–5 (the "get operational" path) and defer 6–8? The manual already has all the source content, so porting is mostly restructuring + adding value context + adapting language. Recommend all 8 — the content exists; the work is structural.

## Risks / dependencies

- **Depends on 0061.** The name "Crash Course" must be freed before this guide can claim it.
- **Maintenance burden.** The two-step parity chain (spec → manual → guide) is more work than the current one-step chain. The tag system mitigates this but doesn't eliminate it. If the guide falls behind the manual, the tags make catch-up tractable.
- **HTML is not Claude's strongest output format.** The initial HTML/CSS may need manual polish. Plan for a review pass after the initial port.
