# [HASH] — Write a documented QUEUE.md migration checklist Claude follows to convert an old-format project

The one project doc that reliably falls behind as the method evolves is a project's QUEUE.md format (old `## Red flags` / `## Batches` / `### Parked` / `## Deferred tests` / `## Captures` → the two-section model). Phase 1 of the former [migrate-skill]: a checklist Claude follows in an ordinary session, no new skill and no hook change.

Home decided at build: promoted into a shipped plugin doc so consumers whose projects fall behind can migrate too, rather than staying a host-only artifact. New plugin/si-plugin/docs/migrate-checklist.md carries the target shape, the judgment rules a find-and-replace can't make (accepted/resolved red flag → work item if work remains or LOG history if done; old batch/parked/deferred-test → work items by judgment; method boilerplate re-copied not regenerated; drop empty placeholders), a preserve-everything guard, and the Hexboard live-validation record. Wired into setup.md's Step 2C (migration scaffolding) as sub-step "1a. Convert an old-format QUEUE.md," loaded on demand. The pre-existing host recipe (resources/queue-two-section-migration-recipe.md) was marked superseded and kept as the historical/validation record. The FAQ "out of date / offers /setup" entry was extended to note queue-format conversion (draft-before-write).

**Files touched:**
- plugin/si-plugin/docs/migrate-checklist.md — NEW shipped checklist
- plugin/si-plugin/docs/setup.md — Step 2C sub-step pointing to it
- resources/queue-two-section-migration-recipe.md — marked superseded
- plugin/si-plugin/templates/faq-template.md — extended the out-of-date entry

**Routed to Captures:** none
