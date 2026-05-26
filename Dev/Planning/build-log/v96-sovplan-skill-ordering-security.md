# V78 — 2026-05-27 — /sovplan skill + ordering principles + [SECURITY] marker

**What shipped.** New `/sovplan` skill wrapping the planning procedure doc. Ordering principles added to `planning.md` (dependency flow, project-structure, security bias, stale-reference avoidance) with a batch-ordering audit step. `[SECURITY]` marker defined in DOC-STRUCTURE and VOCABULARY — informational inline tag for entries touching sensitive surfaces. SessionStart enhanced to surface top 3 queued batches with goal summaries in the session-open status block. Routing openers table updated to reference `/sovplan`. Red flags rule updated to propagate `[SECURITY]` markers.

**Decisions taken and why.**
- `[SECURITY]` is informational, not hook-enforced. Hooks add complexity and false-positive risk for a marker that's primarily a prioritization input. Two audiences: user sees it reviewing their spec; Claude uses it to bias security-shaped work earlier during ordering.
- Top-3 queued batches show all queued when an active batch exists (since "Next up" already shows the active one) but skip the first queued when no active batch exists (since "Next up" already shows it). This avoids duplicating the top batch in the status output.
- Ordering principles live in planning.md rather than a new doc — they're judgment guidance for an existing procedure, not a separate workflow.

**Pivots and surprises.** Alex manually executed the dev-side folder restructure (batch 0093) during this session with different design choices from the spec: `Dev/` instead of `dev/`, product docs into `Guides/` instead of staying at root, `Archive/` renamed to `Iteration playbook/` under `Dev/Resources/`. Path references updated across all dev-side docs, test suite path depths fixed (3 files), README updated. 184 tests pass from new location.

**Carried forward.** None.
