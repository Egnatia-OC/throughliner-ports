# [HASH] — [unpark-scan-mixed-trigger] unpark scan checks every slug even on a mixed slug+behavioural Blocked-by: plan.md Step 1 + plugin-behaviour.md mirror

A mixed `Blocked by:` header (one or more slugs plus a behavioural tail) once let a parked item sit shelved for weeks though its blocker slugs had shipped — cruise-control, whose Blocked-by mixed two shipped slugs with "a few goal sessions run," so the whole header read as a behavioural trigger and the mechanical slug check was skipped, leaving the user to raise it by hand (2026-06-23). The rule to check slugs already existed; it just didn't fire alongside a behavioural tail. Sharpened it in two mirrored places: plan.md Step 1 unpark scan now carries an explicit mixed-trigger clause — when a header names slugs and a behavioural condition, still check every named slug against LOG/index.md and surface the item as an unpark candidate if any has shipped, regardless of the behavioural half's state — and plugin-behaviour.md Dependency ownership Unpark watch mirrors the same clause so the canonical rule and the procedure step stay in step. Procedure-sharpening only, no hook: per the slipped-rule escalation heuristic the cost of this slip is mild and self-correcting, so it earns sharper wording, not standing mechanical friction (a lint backstop was deferred to the [lint-reflags-citations-within-session] decision). Verification deferred host-side.

**Files touched:**
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/docs/plugin-behaviour.md

**Routed to Captures:** none
