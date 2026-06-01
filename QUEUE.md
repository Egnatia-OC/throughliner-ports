# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Behaviour gaps**
Files: `si-plugin/docs/behaviour.md`
- [build] Add SPEC.md read-only rule
- [build] Add one-build-at-a-time rule
- [build] Add between-skill compact nudge

### Parked

## Ideas

Captured outside /plan. Picked up and routed during the next /plan session.

- [idea] Tighten host CLAUDE.md host/target language — current description uses "installed plugin" vs "source code" but working definitions are simpler: root-level files = host, si-plugin/ contents = target
- [idea] No skill covers committing outside builds — /done requires an active build, so /plan edits to host QUEUE.md have no commit path. Either add a lightweight commit skill or make /done stage-agnostic so it works after any skill that changes files
- [idea] Make CLAUDE.md management an explicit plugin concern — the template scaffolded by /setup should clearly delineate plugin-seeded content from user-appended content, so users know where they can add their own rules without breaking plugin behaviours. Currently hard to tell what landed from /setup vs what was added later
- [test] E2E: Run /plan in consumer project, verify it creates a batch with correct format (bold title, Files list, type-marked entries)
- [test] E2E: Run /next in consumer project, verify it picks up a batch and builds all items
- [test] E2E: Run /done in consumer project, verify it routes findings to Ideas
- [idea] Rename "Ideas" section to "Captures" or similar — the section holds all unrouted items (tests, ideas, findings), not just ideas. Renaming would make [test] and other non-idea entries feel less out of place and give the [idea] tag clearer meaning as a type within the section

### Parked
