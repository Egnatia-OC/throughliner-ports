# V106 — 2026-05-27 — `_method/` orientation in CLAUDE.md template

**What shipped.** Added a `## What's inside _method/` section to CLAUDE-TEMPLATE.md, between the path block and Plugin management sections. Eight bullet points covering UX.md, MANIFEST.md, BACKLOG/, build-log/, test-log/, proxies/, planning/drafts/, and research/. Written for non-coders — no jargon, no implementation details. Method version bumped to V85 (plugin 0.85.0) across 22 files.

**Decisions taken and why.** Placed the section after the path block rather than before it — the path block is mechanical (Claude parses it), while the orientation is for human readers scanning down from the product overview. No changes to setup.md needed because the content is static (same for every project) and the scaffold copies the template verbatim.

**Pivots and surprises.** None. Straightforward scope.

**Carried forward.** Nothing.
