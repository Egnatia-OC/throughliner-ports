# 672ca2f — Recut the /next family to the two-section work-line model

/next still spoke the old batch model — it picked a "batch" from a Batches section, read Build/Test/Audit/Freeform subheadings, and carried push-markers, a Captures-scanning blocker gate, and unpark/staleness scans, all dependency machinery the redesign removed. This recut moves the whole /next family onto the flat two-section model: Processed holds work lines, each Claude-work by default or `[user]`, and /next self-scopes — deriving its editable Files list from the lines it's about to build rather than copying a pre-authored list.

It also settles how work-type survives the recut. The test type is retired: a check Claude can run is part of building, and a check needing the user is a `[user]` work line handed over. Build, audit, and freeform stay as distinct execution flavors — genuinely different procedures — now selected from a leading marker on the work line (`[audit]`, `[freeform]`, unmarked = build, `[user]` = handover) instead of a queue subheading. The flavor marker leads the line while the slug stays at the end, so the hooks' end-anchored slug check is never fooled by a leading tag.

next.md became a full rewrite (reads Processed, forms a run of top consecutive Claude-work lines to the first `[user]` line or the cleared marker, self-scopes, routes each line by flavor); next-build.md dropped its Test-entries section and moved to self-scoping; next-audit.md and next-freeform.md moved to the work-line model; next-test.md was deleted. The flavor markers were defined in plugin-behaviour.md and plan.md, and an FAQ entry explains the flavors.

**Files touched:**
- plugin-behaviour.md, plan.md — flavor markers defined at the point where `[user]` is defined; plan's keep-step settles the flavor at processing time
- next.md — full rewrite to the work-line router
- next-build.md — self-scoping; Test-entries section removed
- next-audit.md, next-freeform.md — recut to the work-line model
- next-test.md — deleted
- faq-template.md, faq-index-template.md — flavors entry added; freeform entry de-tested

**Routed to Captures:** none
