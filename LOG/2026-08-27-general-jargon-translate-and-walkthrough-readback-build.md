# 32675a3 — Developer and testing words join the translate-away list

The vocabulary rule's translate-in-passing list named method-internal terms — step
numbers, procedure filenames, tag names. It said nothing about ordinary developer
and testing vocabulary, which is just as opaque to the audience and far more
likely to slip out, because it does not feel like jargon to the person using it.

The list gains that class, with **"fixture"** as the recorded specimen. The test
is not a word list — the class is open-ended — but whether the term names anything
in the user's own files. Enumerating banned words was refused on the item for
exactly that reason.

**And the walk-through branch reads a hand-over step back for such terms before it
goes out**, extending the check the halt-text clause already models. That is the
moment the cost lands: the user is about to act on those words with nobody to ask.

The explained-once arm is untouched — a term that earns an explanation still gets
one.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md` (the
in-passing list); `plugin/throughliner/docs/next.md` (the read-back clause, ahead
of the verify-any-command rule).

**Routed to Captures:** [walkthrough-jargon-broken-by-its-own-author] — this rule
was broken within the hour, by this session, in the walk-through pass that
followed. A step was handed over reading "Developer Portal → Bot → Privileged
Gateway Intents → Message Content Intent → Save Changes", with no read-back and no
indication where any of it sits on screen, and the user said plainly that they did
not understand it. Re-explaining it as five located steps worked immediately.

That instance is the strongest evidence the rule is right and the weakest possible
evidence that stating it is enough — which is what the capture is for.

Rule gate: run — two amendments to named parents: the vocabulary rule's in-passing list gains the general developer-and-testing class, and the walk-through branch gains the read-back clause the halt-text clause already models; nothing evicted.
