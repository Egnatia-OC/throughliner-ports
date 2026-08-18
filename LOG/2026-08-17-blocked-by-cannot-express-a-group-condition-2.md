# 7e3c1c8 — Blocked by: takes several slugs, and the item lifts only when all of them resolve

`Blocked by:` is widened from one slug to a comma-separated list. An extension of a field that already exists rather than a new mechanism.

The ripple was traced by grepping the literal across the repository before any file list was written, as a hook-enforced format change requires. Three parsers read only the first slug and were changed: `session_start.py`'s dependency facts, `queue_digest.py` (where `blocked_by` becomes a list and the cycle walk becomes a depth-first search over the blocker graph, since a loop can now run through any named blocker), and `reorder_queue.py`'s dependent scan — that last one mattering most, because a dependent whose *second* blocker is being deleted is exactly the item whose premise needs re-examining.

**`post_tool_use.py` needed no change, verified rather than assumed.** Its lint already collected every `[slug]` on the line and iterated them, so it was multi-slug capable before the field was.

Docs, the FAQ template and the FAQ copy reworded; SPEC's "Lifting shelved work" paragraph too. Proved end to end on a scratch queue: session_start reports both pairs, the digest prints both blockers with their locations, the lint accepts the item, and all five existing suites still pass.

Two alternatives were refused on the record. A named-group state is a new state with its own lifecycle, and inventing states is the failure this method has caught repeatedly. Do-nothing was the tempting one, costing nothing — and it misfiles designed, buildable work as a capture, which is what `Blocked by:` was built to replace.

The cost was accepted knowingly: about fifteen live files for a problem that has arisen once.

Rule gate: run — a widening of an existing field; no freestanding rule and no new state.

**Files touched:** `plugin/throughliner/hooks/session_start.py`, `plugin/throughliner/scripts/queue_digest.py`, `plugin/throughliner/scripts/reorder_queue.py`, `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, `plugin/throughliner/docs-b/plan.md`, `plugin/throughliner/docs-b/done-plan.md`, `plugin/throughliner/templates/faq-template.md`, `FAQ/faq.md`, `SPEC.md`, `CLAUDE.md`
**Routed to Captures:** none
