# [HASH] — The rezip and release rituals gain a target-versus-installed stamp comparison, and it was used for real later in the same run

The step that caught a shipped bug was the one nothing required. Now it is
required.

**The gap, concretely.** The Rezip ritual's step 5 proves the hooks are alive —
three test suites before the restart, a delivery check in the fresh session asking
what actually arrived. None of that answers *is the installed copy the same build
as the source?*, which is the question the build stamp exists for. The stamp is
reported at every session start and was compared by hand, if anyone thought of it.

**Why it earns a step rather than a habit.** It caught a real shipped bug on the
day it was written down. The `.in_use` exclusion went out matching a filename when
`.in_use` is a directory; the test accompanying it passed because it built its own
fixture; and the only thing that found it was recomputing both stamps after the
reinstall and seeing them differ when they could not legitimately differ. That
comparison was run only because the stamp mechanism happened to be what was under
test. On any other rezip nobody would have looked.

**It is cheap and mechanical, which is the whole argument.** One command after the
reinstall hashes `plugin/si-plugin` and the cache directory for the version just
installed. Immediately after a reinstall with no edits in between they must be
identical, so a difference is unambiguous rather than a judgment: either the
snapshot didn't take, or the stamp function itself is wrong. Both are worth
stopping for. The command is written out in full in the ritual so nobody has to
reconstruct it.

**One limitation is recorded beside it rather than left implied.** This checks that
the installed copy matches the source. It cannot tell you the stamp function is
computing the right thing — that was the bug underneath, and it was caught only
because the two directories were known byte-identical by an independent route
(`diff -rq`). A stamp comparison that quietly agrees for the wrong reason is
possible, so this is a cheap net, not a proof.

**Settled at processing: prose steps only, not `hook_schema_check.py`.** The
capture left that open. The comparison is meaningful only in the one moment
immediately after a reinstall, which makes it a ritual step rather than a test;
putting it in the suite would make a repo-scoped suite start reaching into the
installed copy elsewhere on the machine, for no gain, since the suite cannot know
whether a reinstall just happened. That dissolved the grouping with
[session-start-test-asserts-retired-model-branch], which had been grouped here on
the assumption both would edit that file.

**It got its first real use inside this same run**, about an hour later: the rezip
that shipped [postcompact-firing-probe] ran the new step and both stamps read
`5cd5411acdb8`.

**Files touched:**
- `CLAUDE.md` — Rezip ritual step 4 gains the comparison between the CLI update and the restart instruction, with the command, the reason and the limitation; Release ritual step 11 references the same check, noting a release ships to consumers so a failed snapshot matters more there.

**Routed to Captures:** none from this item.

**FAQ:** not needed because the rezip and release rituals are host-only development procedure; consumers install from the marketplace and never run them.
