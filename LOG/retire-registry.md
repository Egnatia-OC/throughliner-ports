# [HASH] — Retired REGISTRY.md — the write-only inventory doc removed across the plugin and this project (architecture 4 docs → 3)

REGISTRY.md was write-only: scaffolded at setup, rewritten at every /done, presence-checked at session start, and listed in the scope-lock's editable method docs — but nothing ever read its content to make a decision. Its only justification was a human-facing component map, and the non-coder it serves never opened it. The better replacement is live: a user who wants to know what their app contains asks Claude in-session, which explores the actual code — accurate, contextual, zero maintenance. So the architecture drops from four project docs to three: SPEC, QUEUE, LOG.

This batch removed every operational trace of REGISTRY. setup.md no longer scaffolds it (the SPEC template's doc list went four → three, the standalone REGISTRY.md template block is gone, and the Case B mention is trimmed); the /setup SKILL description dropped it. Both hooks lost it: session_start.py no longer checks for the file or flags it missing, and pre_tool_use.py dropped it from the method-docs editable set (both still compile, no orphaned references). The procedure docs lost it: next.md / next-audit.md / next-freeform.md dropped it from their method-docs lists, next-build.md lost the "REGISTRY is not build scope" line, done.md and done-plan.md dropped it from staged paths, and done-build.md and done-freeform.md lost their "Update REGISTRY" steps (done-build was renumbered 1.3→1.2, 1.4→1.3, 1.5→1.4 and its two within-doc step references fixed). plugin-behaviour.md dropped REGISTRY from the route-to-artifacts and doc-routing lines and — folding in the agnosticism decision — reworded the SPEC description from "what/who/how/why the product exists" to "the project exists." CLAUDE-TEMPLATE.md and the FAQ template (plus its index) lost their REGISTRY entries; this project's own CLAUDE.md and dogfood FAQ were brought to match. This project's REGISTRY.md was deleted.

One safety guard was added rather than removed. A /setup re-run in an already-adopted project may still hold a REGISTRY.md from an older version, so setup.md's migration scaffolding now retires it — but not blind. It reads the file first; if it holds only the old scaffold, it removes it quietly, but if the user added real content, it leaves the file, surfaces what's there, and asks where that content should go before removing anything. The why: blind retirement on re-run would delete content a consumer actually used (the Taskflow spec-trim audit named REGISTRY as a relocation home for a component detail).

A full-repo grep sweep confirmed no dangling references remain. The only REGISTRY mentions left are intentional (setup.md's retirement step, the queue push marker, and the new deferred-test lines) or excepted (LOG history, research notes, and the reader-test fixture — the fixture's staleness is filed as a capture).

**Files touched:**
- plugin/si-plugin/docs/setup.md — stopped scaffolding REGISTRY; added the re-run retirement step with a content-safety check
- plugin/si-plugin/skills/setup/SKILL.md — dropped REGISTRY from the description
- plugin/si-plugin/hooks/session_start.py — removed the presence check and the missing-scaffold flag
- plugin/si-plugin/hooks/pre_tool_use.py — removed REGISTRY from the method-docs editable set
- plugin/si-plugin/docs/next.md, next-audit.md, next-freeform.md — removed REGISTRY from the method-docs lists
- plugin/si-plugin/docs/next-build.md — removed the "REGISTRY is not build scope" line
- plugin/si-plugin/docs/done.md, done-plan.md — dropped REGISTRY from staged paths
- plugin/si-plugin/docs/done-build.md, done-freeform.md — removed the "Update REGISTRY" steps (done-build renumbered, two refs fixed)
- plugin/si-plugin/docs/plugin-behaviour.md — removed REGISTRY from the routing lines; SPEC desc "product" → "project"
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md, faq-template.md, faq-index-template.md — removed the REGISTRY entries
- CLAUDE.md — removed REGISTRY from the architecture, file tree, Push sweep list, Method docs, and design-for-fresh files list (4 → 3 docs)
- FAQ/faq.md, FAQ/index.md — removed the REGISTRY entry (dogfood copy)
- REGISTRY.md — deleted

**Routed to Captures:** reader-test-workflow.js still models the retired REGISTRY doc (filed as an unprocessed capture for a later decision — update or retire the dev-only test fixture).
