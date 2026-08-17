# dc52025 — a file entry contingent on an unmade decision now fails the keep-step's second limb

Reported by a consumer project: an item passed /plan, was cleared to run, and halted a build run because it stated one design question as open and instructed that it "should be settled at the start of the build rather than during it". Its file list, for the affected file, read "any affordance the link-address question settles on".

The second limb already requires stating what changes inside which files. What it did not say is that a file entry whose content depends on a decision not yet made fails that limb outright rather than partly passing it — it reads as specificity because it names a shape, while naming no file. The phrasing goes into the rule explicitly, because it is what makes the move catchable: "settled at the start of the build rather than during it" reads as care about sequencing and does the opposite, since the start of the build is still the build. A check can only catch what it has been shown.

The reporting project's suggested disposal was taken as-is: a split rather than a refusal, since most of such an item is usually finished. Their closing observation is what carried the case — a small unmade decision is still an unmade decision, and small ones are the only kind that survive a keep-step.

One thing they proposed was refused. They noted the trigger is nearly mechanical; a hook matching hedging phrases in a file list would fire on honest text, and measures that cry wolf get worked around here. It stays a judgment at the keep-step, where refusing costs a conversation rather than undoing finished work.

A reply was drafted, approved verbatim by the user, and sent into that project's mailbox after both pre-send checks passed.

Rule gate: run — admitted as a clause on plan.md's existing two-limb keep check; no freestanding rule and no always-loaded slot. One alternative refused.

**Queue changes:** [stated-open-design-question-passes-the-keep-step] kept into Processed, cleared to run.
**Work processed:** kept — [stated-open-design-question-passes-the-keep-step].
