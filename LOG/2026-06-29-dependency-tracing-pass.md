# 77ef065 — [dependency-tracing-pass] plan-time dependency tracing: behaviour rule + plan.md trace/producer gates + missing-producer lint framing + FAQ

/plan ordered batches from assumed or surface dependencies, never traced against the real code and SPEC, so the dependency graph broke often under heavy coding volume — batches split mid-build, test batches verified things not built yet — and /next's scope-lock and abort fired so often it read as thrash. The real failure was upstream in /plan's analysis, so this pushes the fix there: a build batch's dependencies are now traced, not asserted. Added the canonical five-obligation "Dependency tracing" rule to plugin-behaviour.md Dependency ownership — (a) trace by reading the named files plus relevant SPEC (over-declaring safe, under-declaring the bug), (b) completeness so every dependency has a producer, (c) shared-primitive scan across the other queued batches, (d) record the trace evidence in the rationale with the Depends-on line staying clean slugs, (e) the accepted limit (static tracing can't be complete per the research; /next's scope-lock + abort backstop; failure modes 4 and 5 are accepted residual). plan.md applies it at three points: Step 3 "Trace dependencies" plus a readiness Trace gate, the Step 2 promote path, and the Step 4 close-walk's new producer-existence check. post_tool_use.py reframes a Depends-on slug resolving to no producer as a missing-producer flag (advisory, never blocks; the other checks unchanged). Added a consumer FAQ entry on the tracing narration. Run-now test passed in-session: the lint fires the missing-producer flag on a no-producer Depends-on and stays silent when it resolves. The /plan tracing behaviour and the live-host lint framing are deferred host-side.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/hooks/post_tool_use.py
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none (this batch). The run's audit ([full-tag-placement-recheck]) filed [trace-rule-needs-exemplar] against this batch's text — a missing show-the-shape exemplar — for a later /plan to route.
