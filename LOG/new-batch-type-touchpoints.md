# [HASH] - CLAUDE.md: note the four touch-points a new batch type must wire

When a batch introduces a new batch type it must wire four places or ship half-working - the spec-edit type was caught half-wired once (it omitted next.md's router). The Working conventions now name the four: next.md (execution routing), done.md (close routing), post_tool_use.py's ALLOWED_SUBHEADINGS (the lint), and plan.md's Step 3 batch structure. Host-only: consumers never author batch types, so this stays in this CLAUDE.md, not shipped plan.md.

**Files touched:**
- CLAUDE.md

**Routed to Captures:** none
