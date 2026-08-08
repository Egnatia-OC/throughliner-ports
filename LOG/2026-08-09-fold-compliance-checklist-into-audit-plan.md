# 7a4b377 — The compliance checklist's two live lenses folded into the consistency-audit plan as full-corpus passes, and the checklist file deleted

Three standing audit documents became two, and the two plans now own all the audit
criteria.

**The state that argued for the fold.** `resources/method-compliance-audit-checklist.md`
sat alongside the two reusable plans the cycle actually runs. Its Lens 1 (4.8
authoring-compliance) pointed at the authoring heuristic's 4.8 section, which
[authoring-heuristic-has-no-live-model-pass] deleted earlier in this same run — so
that lens had nothing left to check against. Lenses 2 and 3 were live criteria the
consistency-audit plan did *not* cover: that plan asks whether the documents agree
with each other, and these ask whether the documents are well-made. Different
question, genuinely worth keeping.

**They land as passes 11 and 12, scoped full-corpus only**, with a paragraph
explaining why: passes 1–10 ask about agreement, which a span can scope; these are
quality sweeps over standing text, which a span cannot. The differential-scoping
paragraph now says explicitly that 11 and 12 are always skipped there, so a
differential run doesn't have to infer it.

- **Pass 11, response-shape tag placement** — missing, wrong, and prose-where-a-tag-belongs, with the reasoning that the tag is the mechanism and prose substitutes are what the tags exist to replace.
- **Pass 12, narration drift** — background vocabulary leaking into user-facing narration, menu-where-a-recommendation-was-due, and unconsolidated skill openings.

**The two reporting disciplines were checked at processing and were genuinely
absent**, so they had to be carried over rather than assumed. The plan's ground
rules already stated verify-before-shipping, dedupe-against-the-queue,
compare-don't-explain and no-quotas — but not search-before-reporting-something-missing,
and not reconcile-with-LOG before reporting shipped work broken. Those were the
checklist's own contributions and would have been lost with the file. Both are now
ground rules.

**The dead lens is recorded rather than silently dropped.** A short paragraph says
it returns as pass 13 if a 5-series authoring pass is ever written, and carries the
corpus-wide question it uniquely asked — *is the rule held to its own standard
consistently across docs?* — which the per-text check cannot ask. That question was
worth preserving even while the lens has nothing to point at.

CLAUDE.md's Method docs section described the checklist as the standing criteria;
it now describes all three plan docs, one per phase of the cycle, and states that
the audit plan owns all the audit criteria so there is no longer a third document
to drift.

**Files touched:**
- `resources/consistency-audit-plan.md` — passes 11 and 12 added with their full-corpus-only scoping paragraph; two reporting disciplines added to Ground rules; the returns-as-pass-13 note; differential-scoping paragraph updated.
- `resources/method-compliance-audit-checklist.md` — deleted.
- `CLAUDE.md` — Method docs section rewritten around the three plan docs.

**Routed to Captures:** none from this item.

**FAQ:** not needed because these are host-only development artifacts, not shipped in the plugin package.
