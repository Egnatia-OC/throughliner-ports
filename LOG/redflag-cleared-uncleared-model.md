# [HASH] — Rework red flags to a two-state cleared/uncleared model, with clearing forced at processing

The three-state model (open / resolved / accepted) held a distinction the queue didn't need to carry. Whether a risk was designed out or consciously accepted matters enormously — but it matters as a *record*, not as queue state, and the LOG is what preserves records. So the states collapse to two, with how it cleared written into the LOG.

The load-bearing change is *when* clearing happens. Clearing is now the explicit moment of processing: a line reaches Processed only with its flag cleared, so cleared is the only state a flag ever carries in Processed. That makes the cleared region red-flag-safe by construction, which is what let the old "/next can't build an open red flag" gate be removed — a cleared flag's label simply rides through to the LOG. Replacing the gate is a backstop: an uncleared flag reaching Processed should be impossible, so if /next meets one it stops rather than building. If a flag genuinely can't be cleared, its capture returns to the bottom of Unprocessed — the one shelving move — never parked in Processed, guaranteeing every risk is eventually cleared or its line deleted.

An alternative considered and rejected: keeping "open" as a third state for a risk carried into a build unaddressed. It lost because it reintroduces exactly what the cleared-region model removes — a line in Processed that /next must refuse to build, the very gate this rework deletes. "Decided but the risk stands" is not a Processed state; it's a capture.

Scope grew mid-build, with approval. The line named its touch points as plugin-behaviour.md, plan.md, next.md, session_start.py and SPEC — but the three states were hard-coded in post_tool_use.py's valid-state set, which would have flagged every new `State: cleared` marker as invalid, and named across the whole done family, setup.md, CLAUDE-TEMPLATE.md and two FAQ entries. A state model cannot ship in halves, so the four unnamed files were added to scope rather than split into a follow-up. That gap is captured as [format-change-names-its-enforcer].

Verified after the change: the lint accepts cleared/uncleared and rejects the old three states; both edited hooks compile.

**Files touched:**
- plugin/si-plugin/hooks/post_tool_use.py: valid-state set → {cleared, uncleared}; docstring and warning message
- plugin/si-plugin/hooks/session_start.py: flag scan → State: uncleared; surfacing text → "UNCLEARED RED FLAG(S)"
- plugin/si-plugin/docs/plugin-behaviour.md: marker enum (2 spots), planning-stage para, Flag states rewritten, "Lifecycle at ship" → "Lifecycle"
- plugin/si-plugin/docs/plan.md: processing-discipline bullet and the keep-a-risk step
- plugin/si-plugin/docs/setup.md: Processed-section marker enum
- plugin/si-plugin/docs/done.md: "Accepted red flags" → "Recording a cleared red flag"; lifecycle-at-close reworked to carry-through + backstop
- plugin/si-plugin/docs/done-plan.md: made the primary clearing recorder
- plugin/si-plugin/docs/done-build.md: 1.4 red-flag close → carry cleared flag + backstop
- plugin/si-plugin/docs/done-audit.md: an audit doesn't clear — surfaced risk files as an uncleared capture
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md: two-state marker description
- plugin/si-plugin/templates/faq-template.md: two FAQ entries rewritten
- plugin/si-plugin/templates/faq-index-template.md: two anchors updated

**Routed to Captures:** [format-change-names-its-enforcer]
