# cc33c1e — done.md and plan.md restyled to the law-prose standard, and the acceptance test's own arithmetic turns out to run backwards

**Why this was worth doing.** Filed on the user's decision that the restyle continues to
the rest of the corpus after `[law-prose-restyle]` shipped covering
`skill-nonspecific-rules.md` alone. These two docs went first because they are the
largest rule-bearing files and both were already scheduled for subtraction work, so
findings had somewhere to land.

**What was built — the wording lens.** Six prohibitions in `done.md` restated as the
action required: the post-scrub claim ("don't tell the user the entry is clean" →
"describe it as checked against that checklist and the credential scan, and as nothing
more"); the compaction proxy ("Never name session length, duration, message count" →
"Name the limit in the sentence's own terms and stop there"); the backfill
investigation, whose two DON'Ts were folded into the action already stated on the next
line; the staged-paths limit ("Do not describe it as covering that" → "Describe it as
making a swept edit visible, and as nothing further"); the queue-state guard; and rung
2's ending. Two in `plan.md`: the capability check's inventory sweep, and "Never write
one silently" → "Write a date only on the user's approval, asked for in the moment".

**What was built — the subordination lens**, folded in from
`[freestanding-rules-that-should-be-subordinate]` on the user's instruction. Three
parents landed. In `done.md`, length became one parent with four provisions, absorbing
the entry-split rule, the open/skip requirement, the no-restatement rule and the repeal
history, with the standalone caps paragraph deleted into the fourth unit; and the
forward-advisory became one parent with six, absorbing five previously freestanding
statements. In `plan.md`, the skip provisions became one parent with five. In
`skill-nonspecific-rules.md` — in scope for this lens only, not a second restyle — the
known instance was fixed: three separate statements about how long something should be,
none referencing the others, became one parent in the Authoring standard with the
Index-entries statement reduced to a cross-reference, "Subject to the Authoring
standard's length provision above".

**The finding worth carrying, because it inverts the acceptance test.** That test asks
for every FALL in the rule-statement count to be attributed to a merge or a deletion,
on the reasoning that subordinating two rules under one parent reduces the count. It
does not. The count ROSE in all three files: `done.md` 236 → 243, `plan.md` 311 → 318,
`skill-nonspecific-rules.md` 311 → 312.

The cause is mechanical and is not a sign that rules were added. `rule_signals.py`
counts three shapes — a bullet, a paragraph whose bold leads the line, a line inside a
typed block — and its own caveat says a rule stated in plain prose is invisible to it.
The subordination lens converts prose into bullets, which are countable. So the rise
measures how much previously-invisible prose became visible, and a restyle pass should
be *expected* to raise the count rather than lower it. Every change is attributed
statement by statement in the run's working notes: length parent +3, advisory parent
+3, one restatement becoming bold-led +1 in `done.md`; skip parent +3, date sub-topic
+1, capability restatement +1 in `plan.md`, with a residual +2 named rather than left
as a gap.

**The near-duplicate check was re-run after the pass and found nothing**, which is the
check that would catch a rewrite silently authoring a duplicate rule. That is the one
mechanical guard against this pass's characteristic failure, and it is why the
disposition calls a restyle the one pass that can silently author a rule by rewriting
one.

**The per-paragraph rationale lens did not run here.** It was folded in on 2026-08-17
and taken back out on 2026-08-19, and it lives in
`[rationale-lens-after-the-build-view]`, which ran later in this same run.

**Files touched:** `plugin/throughliner/docs/done.md`,
`plugin/throughliner/docs/plan.md`,
`plugin/throughliner/docs/skill-nonspecific-rules.md`.

**Routed to Captures:** none from this item.

FAQ: not needed because the wording of instructions Claude reads changes and nothing a
user does changes.

Rule gate: run — no rule is authored, amended or evicted; the standard being applied was admitted when the gate was, and this extends it to more files plus one lens the admission rule already contains. **A restyle is the one pass that can silently author a rule by rewriting one**, which is why the acceptance test is a count accounted for statement by statement rather than a reading.

Depth: full — reasoning contested. The acceptance test anticipated the count falling
and it rose in all three files, so the pass had to establish why before it could claim
to have met the test. **The limit inherited from the pass that worked stands
unchanged:** a flat count cannot detect a rewrite that changed a rule's meaning, so
this claims coverage of what it read and nothing more.

Built and confirmed.
