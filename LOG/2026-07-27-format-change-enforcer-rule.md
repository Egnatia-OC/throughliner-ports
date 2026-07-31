# 053c608 — CLAUDE.md: added host wiring rule to trace a hook-enforced-format change's scope by grep

Observed 2026-07-15 (building [redflag-cleared-uncleared-model]): when a work item changes a format or enum the hooks enforce, the change ripples to every doc naming the values, the hook validating them, and the consumer templates + FAQ. Nothing at plan time traced that ripple, so the file list got written from the design discussion rather than a grep — the red-flag-states change missed post_tool_use.py's valid-state set (which would have rejected every new `State: cleared` marker) plus done-family docs, setup.md, CLAUDE-TEMPLATE.md, and two FAQ entries. /next's self-scoping caught it, but only by halting mid-run — the interruption an unattended run shouldn't need.

Decision (2026-07-27): fix as a plan-time authoring rule, not accepted-cost. Added a CLAUDE.md host rule in the same family as "A new batch type touches four places": when a work item changes a hook-enforced format or enum, its scope is traced by grepping the format's literal values across the repo — naming the enforcing hook AND every doc/template/FAQ that names the values — rather than written from the design discussion. Host-only: consumers don't author hook-enforced formats, so it stays in this project's CLAUDE.md, not shipped plan.md. Complements [next-surfaces-discovery-as-blocking-ask] — plan-time tracing shrinks the ripples /next must catch; when it still catches one, it captures rather than blocks.

**Files touched:**
- CLAUDE.md (project root, Working conventions — new "A hook-enforced-format change traces its ripple by grep" rule)

Authored against the 4.8 section of resources/authoring-heuristic.md. No plugin-package change.

**Routed to Captures:** none
