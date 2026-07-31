# fda7b07 — done-plan.md: same reorder places `[audit]` items end-preferred too

Extended the same /plan-close reorder rule to `[audit]` items. An audit forces a stop for the user to approve its findings — the same interruption problem as a `[user]` line splitting a contiguous Claude block — so `[audit]` items are positioned end-preferred after contiguous build/write blocks, exactly like `[user]` lines, with build-order still winning on a real dependency. Shipped as one rule in done-plan.md covering both flavors (implemented together with [reorder-home-is-plan-close]).

**Files touched:**
- plugin/si-plugin/docs/done-plan.md: Reorder both sections — Processed placement rule (shared with [reorder-home-is-plan-close])

**Routed to Captures:** none
