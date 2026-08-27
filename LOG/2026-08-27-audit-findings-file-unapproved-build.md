# [HASH] — Audit findings file straight to the queue; the write-time approval is repealed

An audit presented its findings as a numbered set and waited, then handled
contested ones one at a time, then filed the survivors. The user pointed at the
double assessment: they judged the same material twice — once as a list with no
context, and again at planning when it was actually being decided.

So the present-and-wait step and the contested-findings pass are repealed.
Findings append to Unprocessed directly, and the audit says in one line how many
it filed and which audit they came from.

**Nothing is lost, because a capture was never a commitment.** Filing is open to
every chat; deciding an entry's fate is planning work. An audit finding is a
capture like any other, and the assessment that matters happens once, where it
always did.

**What replaces the approval is a prose provenance line** — "from the <name>
audit, not yet reviewed" — written into each capture's rationale like any other
provenance, and read at the decision step, which now introduces such an entry as
unreviewed audit output. So the user's single evaluation happens knowingly rather
than on material they might assume was already vetted.

**A parsed not-reviewed field was refused**: a prose line the decision step reads
suffices, and a new field needs machinery nothing else wants. **A light confirm
before filing was refused too** — it recreates the double assessment in smaller
form.

**Evicted in the same move:** the bulk-approval inversion's audit example in the
always-loaded rules, since that set no longer waits for approval. It is restated
there as a NOT-an-inversion line, so the next reader does not re-derive the old
behaviour from its absence.

**Files touched:** `plugin/throughliner/docs/next-audit.md`;
`plugin/throughliner/docs/skill-nonspecific-rules.md`;
`plugin/throughliner/docs/plan.md`. A grep for the repealed step's distinctive
words across shipped docs, FAQ, SPEC and CLAUDE.md returns nothing.

**Routed to Captures:** none.

Rule gate: run — repeal of next-audit.md's present-and-wait step and contested-findings pass, with the bulk-approval inversion's audit example evicted in the same move; the mark is a prose convention the decision step reads, not a new parsed field.
