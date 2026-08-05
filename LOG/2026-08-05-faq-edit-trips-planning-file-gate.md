# 3affa20 — pre_tool_use.py planning quiet-list gains FAQ/; templates/ deliberately keeps asking, recorded in a code comment

The host CLAUDE.md makes FAQ disposition a hard close gate, so a planning close that updates FAQ/faq.md is doing exactly what the method mandates — and FAQ/ was not on the planning file-gate's quiet-list, so the mandated edit surfaced a permission ask at every such close. Repeated benign asks are what train a user to click through the one that matters. The two paths got opposite answers, per the processing decision: FAQ/ joins the quiet-list (scaffolded method material, same family as LOG/ — not the thing the user is building); templates/ keeps asking, deliberately, because editing a template changes what every future consumer receives — exactly the class of change the gate exists to surface. The exclusion is recorded as a decision in `_is_plan_quiet_path`'s docstring so a later session doesn't read the asymmetry as an unfinished job and "complete" it. Verified: FAQ writes pass silently in a planning session; templates/ and arbitrary files still prompt. The quiet-list ships, so this reaches consumers, and is right for them too — FAQ/ is method material in their projects as well.

Overnight blitz run (branch overnight-blitz-2026-08-05b): built under the blitz plan's sanctioned departures — approvals deferred to the branch review, no push.

**Files touched:** plugin/si-plugin/hooks/pre_tool_use.py
**Routed to Captures:** none
FAQ: not needed because the change removes a spurious prompt; nothing new is put in front of the user.
