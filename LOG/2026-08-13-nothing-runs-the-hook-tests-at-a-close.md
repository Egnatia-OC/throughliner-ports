# 340e7ef — A close whose commit touches the hooks now runs the test suites first

CLAUDE.md gained a close obligation: where the staged paths include
`plugin/si-plugin/hooks/`, run the suites under `resources/testing/` before
committing and halt on any failure. The trigger is read from `git status`, so it
needs no judgment and fires only on sessions that could have broken a hook.

The gap was in the trigger rather than the tests. The suites already existed and
already ran in seconds, but only the rezip ritual invoked them — and a rezip
happens on request while a commit is routine, so the cheap frequent check sat
behind the rare one. A non-blocking report was weighed and lost: a report listing
known failures at every hook-touching close is what people learn to skim past.

Host-only by residence, because `resources/testing/` is not in the plugin
package and a consumer has no suites to run.

Rule gate: run — admitted. Parent named as the existing close-obligation family
(FAQ-sync, the disposition line, the epoch bump), written as a sibling of those.
Two recorded instances, not one: a `session_start.py` regression committed clean
and caught minutes later by an unrelated rezip, and an earlier period when
nothing ran the suites and a dead hook stayed invisible. Nothing displaced.

FAQ: not needed because the obligation is host-only and never fires for a
consumer.

**Files touched:** `CLAUDE.md`
**Routed to Captures:** none
