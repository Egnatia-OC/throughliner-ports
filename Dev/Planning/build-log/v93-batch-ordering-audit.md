# v93 — 2026-05-26 — Planning: batch ordering audit and consistency fixes

**What shipped.** BACKLOG queued-batch reorder based on dependency analysis. Skill-rename cluster (0097/0099/0098) moved ahead of standalone batches. Five batches updated to fix stale cross-references (old skill names, deleted files). Batch-ordering audit folded into 0098's scope as a named planning-procedure step.

**Decisions taken and why.**
- Reorder: 0097 → 0099 → 0098 → 0096 → 0093 → 0088 → 0094 → 0095 → 0101 → 0100. Rationale: skill-rename cluster establishes final names; everything after uses them from the start. 0093 (folder restructure) placed after all renames for one clean path pass. 0088 (E2E) placed after architecture is final.
- Stale references fixed in same pass: 0088 (`/before-build` → `/sovrecap`, `/build` → `/sovbuild`, after-build → `/sovclose`), 0094 (`after-build.md` → `close.md`), 0096 (`after-build.md` → `close.md`), 0095 ("After-build handoff" → "`/sovclose` handoff"). Missing dependency declarations added to 0088, 0094, 0096.
- Batch-ordering audit folded into 0098 (not a separate skill). Reasoning: the audit only happens during planning, so it belongs in `/sovplan`'s procedure, not a standalone entry point.

**Pivots and surprises.** Four batches needed stale-reference fixes, not the two initially flagged — 0096 also referenced `after-build.md` in both Inputs and Outputs, and 0095 had an "After-build handoff" reference.

**Carried forward.** Nothing new.
