# [HASH] — Environment check reworded so a tool failing from Claude's shell triggers the ask instead of answering it

A run in Taskflowapp watched Gradle fail from its own shell, concluded it could
not compile, recorded an outstanding check and asked whether to carry on
uncompiled. It never asked whether you could build. You quoted the method back at
it, and you were right: `next-build.md` already said to check before assuming an
environment is absent.

The diagnosis settled at planning is what this build implements. The rule existed
and was read; what it failed to distinguish is the difference between "can't run
this" and "this isn't here". A session that has just watched a tool fail reads
"check whether an environment is available" as a question already answered. So the
sharper trigger is written into the rule's own sentence rather than added beside
it: a shell-side failure establishes that Claude cannot run the tool and not that
the environment is absent, which makes that failure the thing that fires the ask.

The rule's old closing clause — that a check wrongly skipped on a guess sits unrun
for weeks — came out in the same edit. Delete it and the instruction is still
complete, which is the test that makes it rationale rather than operative text.

**Files touched:** `plugin/throughliner/docs/next-build.md` — the
before-assuming-an-environment-is-absent rule reworded, three lines to six.

**Routed to Captures:** none.

Tick form: done, confirmed.

Rule gate: run — amendment to next-build.md's
before-assuming-an-environment-is-absent rule; the sharper trigger written into
the existing rule's own sentence, no new freestanding rule and nothing evicted.

Paired with [no-home-for-a-projects-tool-facts], built in the same run: that item
makes last time's answer readable, this one makes the run ask.
