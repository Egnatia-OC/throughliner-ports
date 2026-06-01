# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

### Parked

## Ideas

Captured outside /plan. Picked up and routed during the next /plan session.

- [idea] Tighten host CLAUDE.md host/target language — current description uses "installed plugin" vs "source code" but working definitions are simpler: root-level files = host, plugin/si-plugin/ contents = target
- [idea] Make CLAUDE.md management an explicit plugin concern — the template scaffolded by /setup should clearly delineate plugin-seeded content from user-appended content, so users know where they can add their own rules without breaking plugin behaviours. Currently hard to tell what landed from /setup vs what was added later
- [test] E2E: Run /plan in consumer project, verify it creates a batch with correct format (bold title, Files list, type-marked entries)
- [test] E2E: Run /next in consumer project, verify it picks up a batch and builds all items
- [test] E2E: Run /done in consumer project, verify it routes findings to Ideas
- [question] How should Claude distinguish product-level questions ("why does my app do X?") from plugin-level questions ("why does SI work this way?") — DECISIONS.md answers the former, plugin docs answer the latter. Needs a routing rule somewhere (behaviour.md? session_start?)
- [idea] Add DECISIONS.md to SPEC.md as fifth project doc
- [question] Is it a problem that scope is unlocked during /done? _build.md is deleted before the commit, meaning there's a window where no build is active but /done is still making file changes (log entries, DECISIONS.md, registry updates). Should _build.md deletion move to after the commit, or is the current order fine since /done's changes are mechanical and scoped by the procedure?
- [idea] Rename "Ideas" section to "Captures" or similar — the section holds all unrouted items (tests, ideas, findings), not just ideas. Renaming would make [test] and other non-idea entries feel less out of place and give the [idea] tag clearer meaning as a type within the section

### Parked
