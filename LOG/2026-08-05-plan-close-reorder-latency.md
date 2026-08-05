# 1332c55 — reorder_queue.py usage message lists all four invocation forms; done-plan.md reorder step names the cheapest invocation for small changes

The three-minute reorder question resolved into a discoverability failure rather than a capability gap: the mover's relative-move forms (`--move <slug> BEFORE|AFTER <anchor>`) already shipped, but its abbreviated usage message printed only two of its four forms, so a session hitting an error learned the tool was less capable than it is — and the 2026-08-05 close restated a full 23-slug order twice when two relative moves would have done it. The measurement question (script vs deliberation time) stays open and is deliberately not guessed at; what shipped is the reframed fix the item stated after its own correction. The usage message now lists every form, closing with the cheap-vs-full guidance; done-plan.md's reorder invocation block leads with the small-change relative form (the common case under the change-scoped rule) and names the full-order form as the expensive path reserved for a genuine whole-section re-sort.

Overnight blitz run 2, phase 3 (branch overnight-blitz-2026-08-05b): processed and built under the blitz plan's softened bar and sanctioned departures — approvals deferred to branch review, no push.

**Files touched:** plugin/si-plugin/scripts/reorder_queue.py, plugin/si-plugin/docs-b/done-plan.md
**Routed to Captures:** none
FAQ: not needed because the mover is internal machinery the user never invokes.
