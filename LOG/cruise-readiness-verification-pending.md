# [HASH] — Added a verification-pending clause to plan.md's cleared-to-run rule (reframed: dependency tracing was removed by the recut)

Implemented [cruise-control] concern 8's named gap. The batch assumed plan.md's dependency tracing existed to extend, but the work-line recut had removed dependency tracing entirely — dependencies are gone from the model, and relationships survive only as prose slug references. Reframed with the user's approval onto the mechanism that exists now: the cleared-to-run line positioning in plan.md's close. A processed line stays below the marker if it depends, by a prose slug reference, on work that's built but not yet verified live — clearing only once that verification lands. The why is autonomy: a cleared line can be built unattended by /cruise, so clearing one resting on built-but-unverified work would stack committed work on a foundation that might later fail its check. post_tool_use.py was left untouched — verification state isn't structurally encoded in the queue, so a lint can't see it. Also broadened the design-refs capture to flag the stale "dependency tracing" mechanism name. Host-side.

**Files touched:**
- docs/plan.md

**Routed to Captures:** none
