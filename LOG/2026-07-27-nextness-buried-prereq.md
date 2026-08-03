# 053c608 — plan.md keep-step + plugin-behaviour: split a buried user-only gating prerequisite into its own [user] line at processing time

Observed live in a consumer project: one subproject's real blocker — an approval only a third party could give, which gated the whole tool — lived only as prose inside that item's rationale, never filed as its own trackable `[user]` line, so a concrete gating action was invisible as next-work until the user asked. Nothing caught the buried prerequisite at processing time, when the item was first kept.

This build added a check to plan.md's Step 2 keep-step: when keeping an item, scan its rationale for a gating action that is user-only AND gates the item or other work; if found, split it into its own `[user]` work line (own slug) and reference it by slug from the original, rather than leaving it embedded. plugin-behaviour.md's user-only-discovery → `[user]`-line rule was extended to fire at processing time (the keep-step), not only mid-execution.

Distinct from the shipped rule it extends: [user-work-surfacing-and-todo] files *mid-session discoveries* as `[user]` lines; this fires when reviewing an item's *existing prose during the keep-step*. Half 1 of the original capture (a processed item stranded below the marker as "not ready" when its dependency had shipped) is subsumed by [plan-no-below-line-revisit] and needed no build here.

**Files touched:**
- plan.md (Step 2 Keep — "Split out a buried user-only prerequisite before keeping")
- plugin-behaviour.md (user-only-discovery rule — "This also fires at processing time" clause)

No SPEC/FAQ — internal /plan processing discipline, not a new user-facing feature.

**Routed to Captures:** none
