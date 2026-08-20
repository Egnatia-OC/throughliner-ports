# b485ee3 — The method's own skills are named as a hand-over case, so a close stops showing a red error

Captured by the user from a screenshot of another project running this method, at the end of a planning session.

What happened, in order: Claude wrote "Now closing the session", attempted `/throughliner:done`, and the app answered **"Failed to run skill"** in red. Claude then said: *"I can't run the close myself — it's reserved for you to invoke."*

**The second defect originally recorded here is withdrawn.** All five skills carry `disable-model-invocation: true`, whose documented meaning is that Claude cannot auto-invoke them and only the user can — the flag for work with side effects or user-controlled timing, which a close is. So the explanation Claude gave was the mechanical cause, not a true-sounding rule standing in for one. The withdrawal stays on the record because the wrong reading is the intuitive one.

One defect survives. The plugin ships that flag and no procedure doc said so, so a session attempts the invocation and shows the user a red failure mid-close, where a non-coder has least context.

The always-loaded communication rule already says to run every command you can run yourself, handing one over only in the cases the rules name. It gains one named case: the method's own skills — name the command and hand it over, never attempt it. The flag was verified present in all five shipped `SKILL.md` files before the rule was written, so it states a fact about the package rather than a guess.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, that rule's hand-over cases. Not SPEC.md, which already says the close is the user's to run. No FAQ entry: nothing the user does changes.

**Routed to Captures:** none.

Rule gate: run — a named case added to an existing always-loaded rule, subordinate rather than freestanding, so no slot is spent and nothing is evicted. Failure evidence is one instance, which is thin and admitted as such; what carries it is that the failure is visible to the user and the fix is three words of an existing sentence.

Tick: done, confirmed — the flag verified present in all five shipped skills.
