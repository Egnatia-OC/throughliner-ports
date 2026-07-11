# 9f7ad66 — plugin-behaviour.md Communication + faq-template.md/faq-index-template.md — added a fresh-session handoff-offer rule that fires on the user's own fatigue/degradation signal and offers a paste-ready handoff prompt (why + scope inline), plus a matching FAQ entry and its index line. — session-handoff-offer.md

Added a Communication rule to plugin-behaviour.md: when the user reports the session is degrading — dragging, worse replies, or a filling usage bar — Claude offers both a fresh session and a paste-ready handoff prompt carrying state forward. The trigger rests on the user's own report, stated plainly, because Claude has no internal gauge of context filling — it only learns a session is wearing thin when the user surfaces it. The why travels inline with the rule: a non-coder won't know a fresh session is the fix or that a handoff prompt is possible, so Claude names both at the signal. Chosen as a plain behaviour rule over folding a pickup-line into the LOG, which would tax every skill open with a standing check for an occasional need. Authored 4.8-shaped (positive action, exemplar line, stated scope of every skill + plain conversation, why inline). Shipped alongside a matching FAQ entry + index line so a consumer meeting the offer has an answer.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md — new Communication bullet (the handoff-offer rule)
- plugin/si-plugin/templates/faq-template.md — new FAQ entry on the handoff-prompt offer
- plugin/si-plugin/templates/faq-index-template.md — matching index link

**Routed to Captures:** [install-move-breaks-marketplace-path]
