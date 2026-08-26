# 2c76e53 — Verification guidance now says to read a check's exit status from the tool, not from a pipeline around it

A run put a Gradle build through a pipe ending in `tail`, read the exit status, and
reported the compile as succeeding. Gradle had already failed; the status belonged
to `tail`. Claude caught it later and said so plainly.

A false pass is worse than no check at all. The tick that follows reads "done,
confirmed", which is the one tick form asserting that something ran and passed —
whereas an unconfirmed tick at least names what still needs running. And the
trigger is the natural thing to do with a build log: trim the noise.

The fix is written as the action rather than as a warning: read a check's exit
status from the tool itself — a bare invocation, or the tool's own status captured
explicitly — and trim its output separately. The hazard rides inside the sentence
as the reason, because without it the instruction reads as arbitrary.

**The two sibling sites were checked and needed nothing**, which is itself the
finding the item asked for. `done-build.md` has no pipes and no suite step at all —
that step lives in this project's own CLAUDE.md, host-only. `resources/release-ritual.md`
chains its suites with `&&`, which short-circuits correctly.

**Files touched:** `plugin/throughliner/docs/next-build.md` — verification guidance
gains one action-stating sentence.

**Routed to Captures:** release-ritual-suite-step-stale — filed rather than fixed,
because it is outside this item's scope. That check turned up two other things in
the release ritual's step 3: it invokes `python`, which on this machine resolves to
Inkscape's bundled interpreter, and it names three test suites when
`resources/testing/` now holds around twenty, so a release's stop-on-failure gate
covers a shrinking fraction of what exists.

Tick form: done, confirmed.

Rule gate: run — amendment to next-build.md's verification guidance, nothing new
admitted, nothing evicted.
