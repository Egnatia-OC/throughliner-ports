# [HASH] — A fixture suite for the queue lint's never-fired flags

New suite at `resources/testing/test_queue_lint_flags.py`, importing the hook's
`lint()` by path and asserting it flags a slugless work-item heading, a missing
section heading, a red-flag state outside cleared/uncleared, and prose sitting
under no work item. It carries a control — a well-formed queue must produce no
warnings — and checks that valid red-flag states are *not* flagged, since a
check that fires on correct input is worse than none. All seven checks pass.

Only the blocked-by flag had ever fired in practice, because the real queue has
never contained the others. An unexercised check is not a passing check; it is a
check nobody has ever seen work, which is why this needed a fixture rather than
an observation.

**One correction to the item, and it changed what got built.** It listed "missing
provenance" as the fourth flag. There is no such check and there should not be —
provenance is a prose convention, explicitly not lint-checked. Orphaned prose was
the fourth never-fired check, so the suite covers that instead, and the suite's
own docstring records the correction.

The item was rescoped to this one strand at processing, at the user's decision,
because the four had genuinely different fates. Item 4, the /done family, needed
no build: eighteen index entries share commit `16ed591`, one summary commit across
a multi-item run with per-entry files named by slug, so the family has been
exercised thoroughly. Items 1 and 2 left the queue as fate decisions — the
three-strikes halt is a procedure rule with nothing to unit-test, and /setup
scaffolding a fresh folder cannot be run from here at all under the
operate-on-the-folder-you-opened rule. Both stand recorded as **known-unverified**,
which is the honest state rather than a claim they were checked.

Host-only: `resources/testing/` is not in the plugin package. The suite runs as a
plain script, never under pytest.

**Files touched:** `resources/testing/test_queue_lint_flags.py`
**Routed to Captures:** none
