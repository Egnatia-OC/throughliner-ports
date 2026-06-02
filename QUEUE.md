# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Restore response-shape tags and annotate procedure docs**
Files:
- `plugin/si-plugin/docs/behaviour.md`
- `plugin/si-plugin/docs/setup.md`
- `plugin/si-plugin/docs/plan.md`
- `plugin/si-plugin/docs/next.md`
- `plugin/si-plugin/docs/done.md`
- [build] Add response-shape tag definitions to behaviour.md ([SILENT], [BRIEF], [DISCUSS], [PROMPT], [SEQUENCE]) with composition rule. Remove the blanket "one step at a time / all at once" rule — tags replace it.
- [build] Annotate setup.md steps: interview → [SEQUENCE], results + handoff → [BRIEF, PROMPT]
- [build] Annotate plan.md steps: ideas processing → [SEQUENCE, PROMPT], questions flow → [DISCUSS, PROMPT], close out → [BRIEF, PROMPT]
- [build] Annotate next.md steps: batch presentation → [BRIEF, PROMPT], building → [SILENT], course correction → [DISCUSS, PROMPT], completion → [BRIEF, PROMPT]
- [build] Annotate done.md steps: user tests → [SEQUENCE, PROMPT], build recap → [BRIEF], mechanical phase → [SILENT], commit approval → [BRIEF, PROMPT], handoff → [BRIEF, PROMPT]

**Fix /plan Captures processing: add discussion step and make disposition type-agnostic**
Files:
- `plugin/si-plugin/docs/plan.md`
- [build] Add a discussion step before disposition — engage with the substance of each item (especially open-ended ones) before jumping to promote/park/drop
- [build] Make disposition type-agnostic — every Captures item gets the same flow regardless of type marker ([idea], [question], [build], [test])

**Rename Ideas to Captures and remove drift check**
Files:
- `plugin/si-plugin/docs/plan.md`
- `plugin/si-plugin/docs/done.md`
- `plugin/si-plugin/docs/setup.md`
- `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md`
- [build] Rename "Ideas" to "Captures" throughout all procedure docs and template
- [build] Remove drift check (Step 3) from plan.md — existing /done safeguards already cover it

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


### Parked
