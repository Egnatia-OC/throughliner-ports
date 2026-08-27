# 32675a3 — Warn once, then do it: a direct request stops being refused by a rule

A direct do-it-now request was being refused on a rule the user had already
heard. The instance earning this rule's slot is in the 2026-08-26 build
transcript: four asks for one thing, refused each time.

The shipped rule gives one standalone warning turn — what the request crosses,
what the risk is, and briefly what could be done instead — after which the work
commences on the user's next word, whatever that word is. Both the warning and
the work go into the session's record.

**The warning is a turn of its own, and that is the user's decision rather than a
detail.** Warning and complying in the same message leaves nothing to withdraw;
splitting them is what makes the warning worth giving.

**Two carve-outs, written as `subject to` cross-references rather than
restatements** — anything leaving the machine still needs an explicit yes to the
exact text, and destruction git cannot undo still goes through the file-safety
rules. Restating either would have created a second copy to drift.

**Freestanding, after a parent was looked for and not found.** The nearest
candidate — the run procedure's repeated-request rule — governs scope growth
inside a build, not the question of whether a rule may be enforced against the
person the rules are for. Nothing was evicted, because no existing rule states
that question at all.

**Asking twice is explicitly not what unlocks this.** One warning, then the work;
a rule that yielded only on repetition would keep the original failure and just
raise its price.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md` — the
rule added to the Communication bullets, with the standalone-turn requirement and
the no-second-ask clause as subordinate paragraphs.

**Routed to Captures:** [spec-owes-warn-and-outcomes] — SPEC carries no sentence
for this behaviour, and a build does not write product truth. Filed for the next
planning run; SPEC lags that sentence, visibly, until then.

Rule gate: run — authored freestanding after a parent was looked for and not found; the recorded failure earning the slot is the four-ask instance in the 2026-08-26 build transcript; nothing is evicted for it.
