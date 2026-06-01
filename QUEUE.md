# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Commit-based logging + decision index** [Requested]
Files: `si-plugin/docs/done.md`, `si-plugin/docs/setup.md`, `si-plugin/templates/`
- [build] Restructure LOG/ from per-date files to per-commit entries — commit hash as identifier, one entry per /done
- [build] Add DECISIONS.md as thin lookup index — /done writes decision-to-commit mappings, /setup scaffolds the file
- [build] Add behaviour rules for DECISIONS.md: (1) check before re-raising decided questions, flag when user revisits a prior decision; (2) consult before inferring rationale from code — DECISIONS.md is first port of call for "why is/isn't X"

### Parked

## Ideas

Captured outside /plan. Picked up and routed during the next /plan session.

- [idea] Tighten host CLAUDE.md host/target language — current description uses "installed plugin" vs "source code" but working definitions are simpler: root-level files = host, si-plugin/ contents = target
- [idea] Make CLAUDE.md management an explicit plugin concern — the template scaffolded by /setup should clearly delineate plugin-seeded content from user-appended content, so users know where they can add their own rules without breaking plugin behaviours. Currently hard to tell what landed from /setup vs what was added later
- [test] E2E: Run /plan in consumer project, verify it creates a batch with correct format (bold title, Files list, type-marked entries)
- [test] E2E: Run /next in consumer project, verify it picks up a batch and builds all items
- [test] E2E: Run /done in consumer project, verify it routes findings to Ideas
- [question] How should Claude distinguish product-level questions ("why does my app do X?") from plugin-level questions ("why does SI work this way?") — DECISIONS.md answers the former, plugin docs answer the latter. Needs a routing rule somewhere (behaviour.md? session_start?)
- [idea] Rename "Ideas" section to "Captures" or similar — the section holds all unrouted items (tests, ideas, findings), not just ideas. Renaming would make [test] and other non-idea entries feel less out of place and give the [idea] tag clearer meaning as a type within the section

### Parked
