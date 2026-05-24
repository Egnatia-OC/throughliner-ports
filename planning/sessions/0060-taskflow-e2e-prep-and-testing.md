# 0060 — Taskflow E2E prep and testing

## Goal

Migrate Taskflow docs from V34 to current structure, then run the plugin against Taskflow for the first real-project E2E test since V35.

## Inputs

- Taskflowapp at `C:\Users\Alex\Desktop\Taskflow Planning\Planning in here\Taskflowapp`
- Deferred smoke tests: V43 mode-aware messaging, V45 fold-in carve-out, V46 automated test pass, V48 BACKLOG folder-split, V49 batch structure, V49 research folder, V50 build-log folder

## Outputs

- Taskflow docs migrated to V50+ structure
- E2E test notes from plugin-driven session
- Test notes formatted for next dev-side planning round

## Prep work completed (v61)

1. ✅ Lifted read-only restriction on Taskflowapp permanently
2. ✅ Deleted orphans (backup CLAUDE.md, duplicate SYSTEM-PROMPT.md, stray .md.md)
3. ✅ Resolved fold-ins (V34 footers on UX.md, SYSTEM-PROMPT.md)
4. ✅ Fixed path references
5. ✅ Plugin installed at v0.55.0 via local marketplace
6. ✅ Added subagent-warning rule to global CLAUDE.md

## /setup case 4 results (v61)

- ✅ CLAUDE.md rewritten to V55 template, TEST-LOG 8→10 columns, BACKLOG → folder (22 batches), footers V34→V55
- ❌ BUILD-LOG folder migration missed (fixed manually session 3)
- **Total cost: ~163k tokens** (37.9k detection + 36.2k plan + 88.8k execution)

## E2E findings

1. **Setup token cost too high.** 37.9k for case detection. Should classify first, load docs after.
2. **BUILD-LOG folder migration missed.** Case 4 doesn't convert BUILD-LOG.md → build-log/. → Fixed in 0064.
3. **No project-boundary enforcement.** Session can write outside project root. → Fixed in 0065.
4. **Desktop app plugin management friction.** `/plugin` doesn't work in desktop app; stale versions require settings.json edit. → Documented in 0067.
5. **Batch stubs are placeholder.** V47 stubs block before-build. Need real planning content first.
6. **Permission prompt flood.** Subagents prompt on every tool call in Accept edits. → Audited in 0066.
7. **Planning explores code before docs.** Spawned Haiku agent for a question answerable from UX.md. → Fixed in 0063.
8. **Token cost not observable.** Desktop app UI limitation — count disappears on next message.
9. **Before-build correctly gates on placeholders.** Correct behaviour — placeholder stubs rightly blocked.

## Status

Paused after before-build. Three subagents tested (setup, planning, before-build); two untested (batch-executor, after-build). Nine findings → six scopes (0063–0068).
