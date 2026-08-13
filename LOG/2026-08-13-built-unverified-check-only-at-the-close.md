# [HASH] — /plan's two clearing moves now defer to the close's built-but-unverified rule instead of being blind to it

done-plan.md carries the rule that an item must not be cleared where its prose names a dependency that LOG records as built but not yet verified — built alone is not enough. plan.md carried it nowhere, although both of its insertion points are clearing moves: the keep-step clears an item with `--marker-after` in the same call that places it, and the below-the-line revisit lifted on "has the blocker shipped?", where *shipped* does not distinguish built from verified.

The repair follows an exact precedent rather than inventing a shape. The `[user]`/`[audit]` end-preference rule had the same defect — a placement rule living in the close while /plan's two insertion points were blind to it — and was fixed by giving each insertion point a clause that *names* the close's rule instead of restating it. Naming rather than restating is what keeps two copies from drifting, so done-plan.md keeps the statement and plan.md gains two references to it.

The tidy instinct was to hoist the rule into skill-nonspecific-rules.md instead. That was refused on that file's own stated admission test: a rule belongs there only if it fires in all four skills, and this one fires in two.

Rule gate: run — amendment, no slot spent. Both clauses name done-plan.md's existing rule rather than restating it, per the self-authoring gate's `subject to` guidance, so no second copy exists to drift.

FAQ: updated "What does it mean when work sits below the 'cleared to run' line?" — a new paragraph saying that "shipped" means built and checked, so a held item can stay put after its blocker was visibly built. No index line added; the entry already existed.

**Files touched:**
- `plugin/throughliner/docs-b/plan.md` — the keep-step's mover paragraph gains a clause naming the close's rule; the below-the-line revisit's lift table gains a built-only-is-not-enough branch, and its "shipped" prose is defined as built and verified.
- `FAQ/faq.md` — the below-the-line entry extended.

**Routed to Captures:** see this session's other entries.
