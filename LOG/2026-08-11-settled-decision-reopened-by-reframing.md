# 7c9922a — The prior-decision retrieve reads the whole record, not LOG alone [settled-decision-reopened-by-reframing]

The instance is Claude's failure; the user caught it, and their words were that they were confused and had not realised it would affect reasoning across the item.

**What happened.** An item was kept whole after Claude recommended against splitting it by stage and the user agreed. Roughly twenty minutes later, mid-design, Claude asked whether to "ship the two computable stages now and leave three for later" — the same split by readiness rather than by stage, not named as such. The user objected; Claude withdrew it and answered from the earlier decision, where the answer had been available all along.

**Why it is a gap rather than only a slip.** The behaviour rules cover the neighbouring case in full: when the *user* proposes something that would reverse what the record holds, run the retrieve before agreeing. There was no counterpart for **Claude** re-opening a decision made minutes earlier — and a within-session decision is the one case where no retrieve is needed to know it exists, because Claude was present for it.

**The admission gate was run and initially said no**, which is recorded because it shaped what got built. Question 1 asks whether this has failed more than once in a way you can point to. It has failed once. As a *new* rule it stops there.

**What changed the answer was finding the existing rule would already have caught it, and is simply under-scoped.** The Prior-decisions bullet said: run the retrieve, and **if LOG shows it's decided**, state the prior decision. The decision had already been written into the item's own prose before the reframed question was asked — so the record held it, and the rule pointed at the wrong place to look. It named LOG when the method has several sources, and most decisions live in QUEUE prose until a close. So the build is a scope correction to a rule already occupying its slot, consuming none.

**The honest weakness, recorded by Claude against its own recommendation.** It is a convenient reading, produced by the party that made the mistake it excuses. If a later session judges this a one-instance rule admitted under a favourable description, the evidence to re-test is here: one instance, and the argument that the under-scoping is a defect independent of it. The user was offered the plain test — defer until a second instance — and chose the correction.

**What is deliberately NOT built:** no new check at question-asking time, and no rule about Claude re-opening its own reasoning. That is the freestanding version, it fails question 1, and it belongs to the family of shipped rules that do not fire — three of which were recorded the same day.

**Files touched:** `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`
**Routed to Captures:** none from this item
