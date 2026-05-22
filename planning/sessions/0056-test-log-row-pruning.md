# V56 — TEST-LOG row pruning

> **Promoted from OPEN-QUESTIONS in session v47 (2026-05-22).**

## Goal

Add a pruning mechanism to bound TEST-LOG.md's growth. Currently rows are never deleted, only flipped to `Superseded` when a component is substantially changed or removed. The file grows monotonically — and drift check 5 (retest after change) walks every Pass-confirmed row, scaling linearly with batches shipped.

## Inputs

- OPEN-QUESTIONS entry: "TEST-LOG row pruning"
- `plugin/docs/DOC-STRUCTURE.md` → *TEST-LOG.md structure → Pruning rule* — current rule (rows never deleted)
- `plugin/agents/planning.md` — drift check 5 walks Pass-confirmed rows; pruning affects this walk's scope
- `plugin/templates/TEST-LOG-TEMPLATE.md` — template shape
- `plugin/agents/after-build.md` — writes TEST-LOG rows; may gain pruning-related logic
- Consumer projects' TEST-LOG.md — migration target

## Outputs

- Pruning mechanism implemented — specific shape decided at session start (component-based, time-based, or manual archive)
- `plugin/docs/DOC-STRUCTURE.md` updated — pruning rule revised
- Planning subagent updated — drift check 5's row walk respects pruning
- After-build subagent updated if pruning happens automatically at build time
- `/setup` case-4 refresh applies pruning to existing consumer TEST-LOG.md if needed
- OPEN-QUESTIONS entry removed

## Success criteria

- TEST-LOG.md stops growing without bound — old rows whose components no longer exist are pruned or archived
- Drift check 5 walks fewer rows after pruning, with no loss of coverage for active components
- Pruned/archived rows are recoverable (not permanently deleted) if audit trail is needed
- No regression in the after-build → TEST-LOG row-open flow

## Open questions for this session

- **Pruning shape.** Three candidates:
  - **Component-based:** drop rows whose component no longer exists in MANIFEST.md. Cleanest signal — if the component is gone, the test row is meaningless.
  - **Time-based:** drop Superseded rows older than N versions. Requires defining N.
  - **Manual archive:** explicit per-planning-session option to archive rows to an external file. Preserves audit trail; adds a user decision point.
  Leaning: component-based as the automatic mechanism, with Superseded rows also eligible for pruning after the component is removed.
- **Where do pruned rows go?** Deleted entirely, or moved to an archive file (`TEST-LOG-ARCHIVE.md`)? Leaning: archive file — audit trail preserved, context window freed.
- **Automatic vs. manual trigger.** Should pruning run automatically (planning subagent prunes before drift check 5) or on user request? Leaning: automatic — the user shouldn't need to remember.
- **Interaction with V48 test types.** V48 adds type + verifier columns. Pruning criteria should be type-agnostic (prune by component existence, not by test type). Confirm at session start.

## Risks / dependencies

- **Audit trail loss.** Pruning removes history. Archive mechanism mitigates but adds file management. Get the balance right.
- **MANIFEST dependency.** Component-based pruning requires MANIFEST.md to be the authoritative list of active components. If MANIFEST is out of date (components removed from code but not from MANIFEST), pruning misses rows. This is already a MANIFEST maintenance issue, not new.
- **No hard dependencies** on other sessions. Placed at V56 after the test model stabilises (V48) and the automated test suite exists (V53).
