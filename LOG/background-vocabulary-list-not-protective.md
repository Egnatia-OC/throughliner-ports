# 96166c6 — Made the background-vocabulary rule a test rather than a list, and supplied the plain substitutions

Across one session Claude used, without defining: **"the guard"** (an improvised synonym for the hook, which cost four turns to untangle — the user finally asked outright *"by 'that guard' do you mean the hook?"*), **"the routing half"** (*"half of what"*), **"the fork"**, **"scope-lock"**, **"the capture"** as a bare noun, and **"routing"** generally. Twice the user asked for a plain summary of an item because the analysis was not readable on its own, and once said plainly *"I just do not get anything you are talking about here."*

**Not one of those terms was on the background-only vocabulary list.** That is the finding: the list names *known* leaks and protects against exactly those, and offers nothing against a term invented on the spot — which is what "the guard" was. An enumerated list is the wrong shape for this rule, because every term on it earned its place by leaking once, so it can only ever be complete for the past.

So the test becomes the rule: before using a term for a piece of the machinery, would the user have met this word in something they actually read? That is checkable against any term, including one just invented. The list is demoted to worked examples rather than deleted — it still carries the known leaks usefully — with this session's terms added.

**The plain substitutions are the addition the capture did not propose, and the one that addresses the actual failure mechanism.** A test says *avoid this word* and leaves the replacement to be invented mid-sentence; inventing under that pressure is precisely what produced "the guard". A ready phrase removes the invention rather than forbidding its result.

**One name per thing, within an explanation.** "The hook" and "the guard" were one program, and switching between them read as two — which is why that exchange cost four turns rather than one. Consistency matters more here than which name gets picked.

This is one layer up from the sibling item shipped in the same run, which decides that items are written for Claude and summarised for the user: a rule about summarising does not help if the summary uses the same untranslated vocabulary.

**Stated honestly in the doc so the build is not over-expected: this is a wording rule, and wording rules slip.** The difference from the cases where prose was judged not to be the fix at all is that **no mechanical option exists** — nothing inspects Claude's prose, and no hook could judge whether a word is jargon — so a better-shaped rule is the only lever available rather than the lazy choice. Expect an improvement over the list, not a guarantee.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`

**Routed to Captures:** none
