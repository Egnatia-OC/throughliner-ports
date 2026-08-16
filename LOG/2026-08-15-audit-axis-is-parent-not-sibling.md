# 0e62afe — An audit states its axis before it runs, and it is the parent axis unless it argues otherwise

The compliance checklist carried three lenses and said nothing about what a doc is compared *against*. Comparing siblings — `done-build.md` against `done-audit.md`, `next-build.md` against `next-audit.md` — finds wording similarity between docs that are parallel by design, where near-identical phrasing is the expected state rather than the defect. Comparing a doc against its parent finds a child restating what its parent already carries, which is genuine duplication because the child is loaded *with* the parent and the reader has both.

The worked instance is why this is not a stylistic preference. An audit reported `done-build.md` and `next.md` carrying the same rule in near-identical words. True as text, wrong as a finding: `next.md` guards *presenting* a run, `done-build.md` guards *writing a size cap into the note for the next session*, and no session reads both. Two holes, two plugs, one wording. It was refused at processing weeks later with both docs untouched — and on the parent axis it would never have been produced, since neither doc is the other's parent.

Two requirements on top of the three lenses: an audit states its axis before it runs and defaults to the parent axis, and every finding names the moment each site fires rather than only the line it sits on. The second is what would have caught the worked instance at the audit rather than weeks later, and it costs one sentence per finding.

**Noted at the gate rather than assumed:** the mechanical trigger that summons the rule gate reads staged paths under `docs-b/`, `resources/self-authoring-rules.md`, `resources/rule-maintenance.md` and `CLAUDE.md`. It does not include this checklist, which holds rules. The gate was run here by judgment, not by the trigger, and that gap is filed as [gate-trigger-misses-the-audit-checklist].

**Files touched:** `resources/method-compliance-audit-checklist.md`

**Routed to Captures:** none

Rule gate: run — admitted as an amendment to the existing three-lens checklist rather than a freestanding rule; it adds two requirements to a document whose whole content is audit criteria. Failure evidence is one worked instance plus the user's own account of a third audit running on the wrong axis without her noticing. **Nothing is evicted**; a net addition of two requirements to a host-only checklist.

FAQ: not needed — host-only, and a consumer auditing their own app has no parent/child doc structure for it to apply to.
