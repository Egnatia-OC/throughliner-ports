# 7e3c1c8 — the admission test gains a no-skill limb, tightening rather than loosening it

`skill-nonspecific-rules.md`'s opening admission test and `CLAUDE.md`'s distribution clause both gain the same limb: a rule earns the always-loaded file if it fires in all four skills **or** in conversation with no skill running.

The gap was that a rule governing conduct when *no* skill runs fails the bare four-skills test — it fires in zero of four — and is rejected for the opposite of the intended reason. The test exists to keep over-specific rules out; it was silently catching over-general ones too, and the two are indistinguishable at the point it is applied, because both answer no.

The recorded instance is [post-close-tail-state], whose clause fires in the post-close tail. Its own prose names the problem and works around it by siting the clause in `done.md` instead. That works there and does not generalise: it happened to have a doc the tail had just read, and a rule firing outside a skill will not always have one.

Adding a limb was chosen over restating the test as "fires whatever is running" — vaguer than the enumeration it would replace, and easier to talk oneself into. So it is a fifth condition, and admission control is tightened, which answers the item's one real risk in the opposite direction to the way it was posed.

Two questions fell out. A no-skill rule needs no separate home: the always-loaded file already is that home, being the only thing loaded when nothing runs. And the filename stays — "skill-nonspecific" already means not tied to a skill.

Rule gate: run — a limb on an existing admission test; it constrains authoring rather than conduct.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, `CLAUDE.md`
**Routed to Captures:** none
