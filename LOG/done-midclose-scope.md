# [HASH] — Mid-close scope rule: a new build/design directive arising at /done routes out, only a fix completing the just-built work's own verification folds in — plugin-behaviour.md Routing and discipline + done-build.md Phase 1 + FAQ. Goal-session batch 5 of 5.

From the 2026-06-17 Taskflow session (the same one behind batch 1): a header redesign — new design work — got built during /done because a device appeared mid-close and verification was running there. No rule governed whether /done should take on a new directive that arises during close-out, so Claude improvised.

The line this batch draws, stated in plugin-behaviour.md's Routing and discipline: a new build or design directive that arises during a close routes out — a fresh /next, or a capture if it isn't urgent — even when the user raises it mid-close and even if it looks small, because /done records and commits finished work and is not a build session. The one exception: a fix that completes the just-built work's own verification (a genuine bug in what this build was meant to deliver) folds in, because it finishes the build rather than adding scope. The strong counter-reading is preserved inline: verification naturally lands near the close and shipping known-broken work would be worse than fixing it there — which is exactly why a build-completing fix is the fold-in exception while new scope is not.

done-build.md gains a "Mid-close directive — new scope vs build-completing fix" subsection in Phase 1 that applies the general rule at the build close, pointing back to plugin-behaviour.md rather than restating it. An FAQ entry ("Why did Claude say my new change has to wait for a fresh session?") and its index line ship.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: added the mid-close new-scope-routes-out / build-completing-fix-folds-in rule to Routing and discipline.
- plugin/si-plugin/docs/done-build.md: added the "Mid-close directive" Phase 1 subsection.
- plugin/si-plugin/templates/faq-template.md + faq-index-template.md: added the new-change-waits FAQ entry + index line.
- QUEUE.md: removed the batch; added its deferred-test line.

**Routed to Captures:** none.
