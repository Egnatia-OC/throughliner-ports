# [HASH] — Added advisory forward-recommendation capture: /done files a "Last session advises…" note atop Unprocessed; /plan consumes and clears it

A forward recommendation at session close lived only in chat, so acting on it required the user to remember it — the next-ness-lives-in-memory failure. Fix: when /done's "Recommend next" step makes a concrete recommendation, it files an advisory capture at the top of Unprocessed, worded as advice ("Last session advises processing X next"). The advisory is a transient orientation handoff, not a work line: the next /plan reads it, lets it inform the order discussion, and deletes it once order is agreed — whether the recommendation was followed or not. It never moves into Processed and is never run through keep/delete. When the recommendation is generic ("run /plan when you have more"), no advisory is filed.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: added "Forward-recommendation advisory" subsection under Captures
- plugin/si-plugin/docs/done-build.md: added advisory filing step to Phase 3
- plugin/si-plugin/docs/done-plan.md: added advisory filing step to Section 3
- plugin/si-plugin/docs/done-audit.md: added advisory filing step to Phase 3
- plugin/si-plugin/docs/plan.md: added advisory consumption step to Step 1
- plugin/si-plugin/templates/faq-template.md: added "Last session advises…" FAQ entry
- plugin/si-plugin/templates/faq-index-template.md: added index line
- SPEC.md: added "Forward-recommendation advisory" paragraph in How it works

**Routed to Captures:** none
