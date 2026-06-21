# 29ba751 - plugin-behaviour.md + FAQ: record a privacy/security risk found during planning in Red flags with a state, not inline-only

The Red flags mechanism was written for build sessions; a genuine risk surfaced and designed out during /plan was folded into a map as an inline note, never entered in Red flags with a state. Inline-only handling is a soft version of silently-fix-and-move-on, and buries the why-trail a later session would need. The rule now records a planning-stage risk in Red flags carrying its close-state (resolved if designed out in-session, open if carried into the build, accepted if the user proceeds). The screening threshold is unchanged, so it adds no noise.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md
- plugin/si-plugin/templates/faq-template.md

**Routed to Captures:** none
