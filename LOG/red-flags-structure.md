# [HASH] — red-flags structure: section atop QUEUE.md, /plan routing with state, /done consent record

The structural half of the red-flags feature. The screen-and-surface rule and the three flag states already shipped in plugin-behaviour.md ([red-flags-screen-rule]); this batch built where flags live and how they move through their states.

A Red flags section now sits at the top of QUEUE.md — the first thing seen each session — in both the scaffolded template (setup.md) and this project's own queue. /plan gained a fourth capture route alongside promote/park/drop: a red flag moves into that section carrying a state (open, resolved, or accepted) instead of becoming a batch, and its state can change during planning — open → resolved when the risk is designed out, open → accepted when the user is warned and chooses to proceed. /done records an accepted flag's decision in the session LOG as the informed-consent trail. The consumer-facing docs (CLAUDE template, this project's CLAUDE.md, the FAQ) document the section and the three states. The autopilot gate that reads these states is deliberately not built here — it belongs to the future cruise-control skill.

One design choice weighed during the build: the /done recording was placed as a "stated once" section in done.md with pointers in all four close-out sub-docs, rather than only in done-plan.md. Acceptance is a planning-shaped decision, but the screen rule fires every session, so a flag could be accepted in a build, test, or audit close too — the consent record shouldn't depend on acceptance happening only in /plan.

**Files touched:**
- plugin/si-plugin/docs/setup.md — Red flags section in the scaffolded QUEUE.md template
- QUEUE.md — Red flags section at the top of this project's queue
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md — Red flags in the QUEUE.md format description
- CLAUDE.md — Red flags in both QUEUE.md descriptions (Architecture + Method docs)
- plugin/si-plugin/docs/plan.md — red-flag routing as a fourth capture route; state carried and changed during planning
- plugin/si-plugin/docs/done.md — new "Accepted red flags" stated-once section; pointers added in done-plan.md, done-build.md, done-test.md, done-audit.md
- plugin/si-plugin/templates/faq-template.md + faq-index-template.md — consumer FAQ entry on red flags and the three states, plus index line

**Routed to Captures:** Expedite deleting the /next pre-flight deferred-tests re-presentation (points at [deferred-test-lifecycle]).
