# 32675a3 — A discovery runner replaces the ritual's hand-written suite list

The rezip ritual named three suites by hand. That list went stale the moment a
fourth was written, and nothing anywhere reported the omission — a suite left off
the list is indistinguishable from a suite that passed. There were 29.

`resources/testing/run_all.py` discovers instead. **What counts as a suite is a
naming convention, not a list**: a `.py` file in the folder named `test_*.py` or
`*_check.py`. A new suite named that way is picked up with no edit, which is the
whole point.

**Anything matching neither is reported as skipped rather than passed over
silently** — a suite misnamed at birth would otherwise be invisible in exactly the
way the hand-written list was. It correctly names `statusline_probe.py`, which
reads a status line from stdin and would hang a runner that executed it.

It runs each suite through `py` rather than `python`, per the scripting
constraints, and exits non-zero on the first failure so the rituals stop rather
than warn.

**One correction to the item, made rather than left.** The item said to change
"the rezip's suite step and the release's suite step". The Release section had no
suite step at all — only Rezip did. One was added, placed before packaging, since
a release can be asked for days after the rezip with commits landed since, and it
is the last moment before something is published under a version number. Leaving
the item half-built on the strength of its own wrong premise would have been the
worse reading.

**pytest was refused** by the scripting constraints — `python` here resolves to an
application's bundled interpreter with no pytest, and its error names that
application, which sends a session chasing the wrong cause.

**Files touched:** `resources/testing/run_all.py` (new);
`resources/release-ritual.md` (both steps, and the renumbering the new one
caused).

Verified by hand: 29 suites discovered and passed, the probe correctly reported as
not run, and no ritual step now names an individual suite.

**Routed to Captures:** none.

Rule gate: run — the enumerated list in the ritual is superseded by the runner call; no method rule authored; host-only ritual text.
