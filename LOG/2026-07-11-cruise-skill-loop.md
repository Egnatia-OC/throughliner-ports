# 2b21b54 — Added /cruise skill: new SKILL.md + docs/cruise.md holding the (a)–(h) autonomous loop

Implemented [cruise-control] concern 9's loop. /cruise is a separate skill, not a /next mode — resolved 2026-07-10 because a /next-continuation flavor would force finishing a full batch before cruise was reachable, which is worst exactly for the strapped-for-time user who is cruise's core case. A thin SKILL.md points at docs/cruise.md, which holds the loop: one up-front go-ahead (no per-line reconfirm), then (a) pick top cleared line → (b) gate-check → (c) build scope-locked via next-build.md → (d) verify → (e) close-and-commit per line via done-build.md → (f) check limits → (g) advance → (h) run-end sweep + summary. Doc-efficiency is kept by reusing next-build.md/done-build.md per line rather than duplicating them. plugin.json needed no edit — skills auto-discover from skills/*/SKILL.md. Live behaviour defers to a post-reinstall check.

**Files touched:**
- skills/cruise/SKILL.md (created)
- docs/cruise.md (created)

**Routed to Captures:** [cruise-run-verification], [cruise-gate-hardstop-verification], [cruise-readiness-verification], [done-defaulted-to-retired-deferred-tests]
