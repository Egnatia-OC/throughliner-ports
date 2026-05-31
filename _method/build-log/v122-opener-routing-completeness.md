# v122 — 2026-05-28 — Dev-side opener routing completeness

**What shipped.** Three additions to `Dev/session-protocol.md`: git-unavailable fallback in step 1 (points to CLAUDE.md *Current state* with staleness check), blended-opener rule below the routing table (explicit priority ordering: E2E > Implementation > Planning > Ideation > Doc-only > Standby, sequential thread handling, disambiguation sequencing), and informal-modifier note (availability context, not session types). Resolved OQ "Informal opener modifiers unmapped."

**Decisions taken and why.** Priority ordering stated explicitly rather than leaving it inferrable from practice — a stranger-Claude shouldn't have to guess. Informal modifiers folded into the blended-opener paragraph as a trailing sentence rather than a separate rule, because they're a special case of the same routing logic.

**Pivots and surprises.** None. Batch was small and well-scoped.
