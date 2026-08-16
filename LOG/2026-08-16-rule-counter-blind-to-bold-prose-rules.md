# d82f538 — Three permitted shapes for an always-loaded rule statement, as an authoring constraint rather than a counting change

The item arrived claiming the rule counter scores bold-prose rules as zero. **That diagnosis was corrected at processing by reading the pattern instead of the account of it:** the counter matches a bold lead-in at the start of a stripped line, so it does reach bold prose, and `CLAUDE.md` — written almost entirely that way — scores 147.

The real blind spot is narrower and cannot be closed by widening anything. What is invisible is a rule stated in **plain prose**, or with its bold somewhere other than the start of the line. No regex reaches those: a rule written as an ordinary sentence mid-paragraph is indistinguishable from explanation by any mechanical test. So "widen the pattern" was refused as impossible rather than merely worse, and the only real option was the other one.

The settlement is an authoring constraint. An always-loaded rule statement is written as a bullet, as a paragraph whose bold leads the line, or as a line inside a typed block — the three shapes the counter can see, and the three both always-loaded files already use throughout. A rule in any other shape is a defect at authoring time, caught where it is written rather than counted later.

**The live consequence, and why this was not deferred.** [law-prose-restyle] carries "the count of always-loaded rule statements must not rise" as its mechanical acceptance test, and it is a rewriting pass over the counted file. That test could be defeated by rewriting rules into plain prose — the count would fall or hold flat while nothing was removed. The caveat was written onto that item in the same move, so the one mechanical check on the largest authoring pass in the queue no longer has a hole the pass can walk through.

The growth report now prints which three shapes it counts and which it cannot see, on the same principle as its other stated limits: a measurement that does not say what it misses invites being read as complete.

Depth: short.

Rule gate: run — admitted as an authoring constraint on always-loaded rules, amending the existing account of how a rule is written rather than adding a rule about behaviour; it spends no slot because it governs form, not conduct. Nothing evicted, and one proposed option refused as impossible. Failure evidence is one measured instance: a shipped disposition claimed net always-loaded rule text would fall, and the count rose.

FAQ: not needed — consumers never author method rules.

**Files touched:** `CLAUDE.md`, `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, `resources/rule_signals.py`, `QUEUE.md` (the caveat onto [law-prose-restyle]).

**Routed to Captures:** none from this item.
