# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**CLAUDE.md template ownership**
Files: plugin/si-plugin/templates/CLAUDE-TEMPLATE.md
- [build] Delineate plugin-seeded content from user-appended content so users know where they can add their own rules without breaking plugin behaviours.

**E2E: consumer project smoke tests**
- [test] Run /plan in consumer project, verify it creates a batch with correct format (bold title, Files list, type-marked entries)
- [test] Run /next in consumer project, verify it picks up a batch and builds all items
- [test] Run /done in consumer project, verify it routes findings to Captures

### Parked

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

- [idea] Rephrase "no active build" pre-flight message in next.md — the wording sounds alarming, like something is already wrong. It should reassure, not startle.
- [question] Should LOG entries still include test results? The recent shift toward LOG as a decision log was not discussed in the context of testing data. Deserves its own discussion.

### Parked
