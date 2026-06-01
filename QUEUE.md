# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Queue restructure**
Files:
- `si-plugin/docs/plan.md`
- `si-plugin/docs/next.md`
- `si-plugin/docs/done.md`
- `si-plugin/docs/setup.md`
- [build] Update target plan.md — batch creation, ideas processing, sizing gates apply to batches not entries
- [build] Update target next.md — pick up batches instead of entries, mid-build course-correction procedure, compact as last resort
- [build] Update target done.md — route findings to host Ideas section, not just LOG
- [build] Update target setup.md — scaffold host QUEUE.md in the new batch/ideas format
- [test] Verify /plan creates batches with correct format
- [test] Verify /next picks up a batch and builds all items
- [test] Verify /done routes findings to Ideas

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

### Parked
