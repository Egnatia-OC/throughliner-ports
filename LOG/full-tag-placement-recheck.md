# 77ef065 — [full-tag-placement-recheck] audit: read all 13 procedure docs against the 3-lens compliance checklist; 3 findings routed to Captures

First run of the routine method-compliance audit checklist built this same session ([method-compliance-checklist]). Read every procedure doc once — setup.md, plan.md, the next family (next.md, next-build.md, next-test.md, next-audit.md, next-freeform.md), the done family (done.md, done-build.md, done-test.md, done-plan.md, done-audit.md, done-freeform.md), and plugin-behaviour.md — applying all three lenses (4.8 authoring-compliance, response-shape tag placement, narration drift), deliberately including the docs freshly edited earlier in this run so the audit grades current state. Findings only; no edits to the docs read, per the audit's route-to-Captures contract. Three findings filed raw to Captures for a later /plan to route:

- [readiness-line-narration-frequency] — the readiness line double-narrates across plan.md Step 4 and done-plan.md, and narrating it every close even when unmoved sits in tension with the method's anti-nag principle. From this run's [readiness-line]. (tag placement + narration drift)
- [trace-rule-needs-exemplar] — the new tracing rules in plan.md Step 3 and plugin-behaviour.md Dependency ownership lack a show-the-shape exemplar, the 4.8 pass's single strongest lever, and are inconsistent on that point with neighbouring Step 3 rules. From this run's [dependency-tracing-pass]. (4.8 authoring-compliance)
- [done-freeform-recommend-hedge-gap] — done-freeform.md Phase 3 omits the "state the scan result either way; the clean case is a plain assessment, not a hedge" framing its sibling done docs (build/test/audit) all carry. Pre-existing drift. (narration drift + cross-doc consistency)

Two of the three grade this run's own fresh edits — exactly the periodic-sweep gap the checklist exists to close (an authoring-time check never re-examines what it just shipped). The findings get scoped in a later /plan that processes them.

**Files touched:**
- none — audit, read-only. The routed findings are the QUEUE.md Captures additions.

**Routed to Captures:** [readiness-line-narration-frequency], [trace-rule-needs-exemplar], [done-freeform-recommend-hedge-gap]
