# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**CLAUDE.md template ownership**
Files: plugin/si-plugin/templates/CLAUDE-TEMPLATE.md
- [build] Delineate plugin-seeded content from user-appended content so users know where they can add their own rules without breaking plugin behaviours.

**E2E: consumer project smoke tests**
- [test] Run /plan in consumer project, verify it creates a batch with correct format (bold title, Files list, type-marked entries)
- [test] Run /next in consumer project, verify it picks up a batch and builds all items
- [test] Run /done in consumer project, verify it routes findings to Ideas

### Parked

## Ideas

Captured outside /plan. Picked up and routed during the next /plan session.

- [question] Is it a problem that scope is unlocked during /done? _build.md is deleted before the commit, meaning there's a window where no build is active but /done is still making file changes (log entries, DECISIONS.md, registry updates). Should _build.md deletion move to after the commit, or is the current order fine since /done's changes are mechanical and scoped by the procedure?
- [idea] Rename "Ideas" section to "Captures" or similar
- [idea] Drift check findings need teeth — currently /plan presents them as informational and immediately defers to the queue. Drift should be resolved (or explicitly deferred) before moving on to Ideas routing, not treated as an afterthought
- [idea] /plan Ideas routing should apply the same disposition step (promote, park, or drop) to every item regardless of type — current procedure only describes routing for [idea] and [question], causing other types to skip disposition entirely
- [idea] Host/target propagation gap — when a feature is built (e.g. DECISIONS.md), host-side docs get updated but corresponding target-side changes (scaffolds, templates, procedures) get missed. Claude needs to treat "which side?" as an active question whenever a change touches project docs, and flag when only one side has been updated

### Parked
