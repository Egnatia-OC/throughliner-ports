# 0ae69d6 — /plan's wind-down re-scan and Step 3 removed entirely; the fourth off-ramp reworded to "run /done"

The user's account was right and the shipped document disagreed with it, which was the defect: `plan.md` still carried a "Wind-down re-scan" section stating that **/plan runs the FULL re-scan** while /done runs a file-only version, a "Step 3: Close out", and a checkpoint off-ramp naming closing as a phase. A session following the document did exactly what the user had been correcting — offering to wind down and close at nearly every checkpoint.

**Three cuts and one rewording, as decided at processing.**

- The wind-down re-scan section: removed entirely. Checked before deciding, as the capture asked — `done.md`'s version runs at **every** close whatever the session type and is file-only, so removing /plan's loses no filing at all. The single thing lost is processing a surfaced capture in the same session, which is the cycle working rather than a gap.
- Step 3: removed entirely, **not thinned a second time**. It had already been hollowed out to "run /done, or keep planning", and that is precisely what let it survive — it looks harmless while remaining a step whose job is to steer toward closing. A step that only suggests running /done is a close-out phase by another name. Four lines of plain statement replace it.
- The fourth off-ramp: **reworded, not deleted** — the user's correction to Claude's recommendation, in their words: close out is simply replaced with "run /done". Claude had proposed removing the option. That was wrong for a reason worth recording: with Step 3 and the section both gone, nothing in the document would have named /done at all, and the user's exit would be invisible. The rewording keeps the exit visible while removing the false implication — *"close out now (Step 3)"* describes a phase /plan performs; *"run /done"* names a command the user runs. Applied at both sites the four routes are recited.
- One stale reference fixed on the way: the end-of-queue gate told sessions not to "slide into the wind-down re-scan or the close", naming a step that no longer exists.

**Nothing removed from `done.md`.**

**The coupling with [cycle-summary-at-every-skill-opening] was respected** — that item landed first in this same run, which is what leaves `plan.md` naming /done at all, as step 3 of the work cycle at the document's opening. A session now learns where /done sits at the start, as part of the loop, rather than being nudged toward it at the end.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`.

**Routed to Captures:** none.

Rule gate: run — this is an EVICTION, not an authoring. A whole section and a whole step were repealed and one string reworded; the always-loaded count is untouched because `plan.md` is fetched, but `plan.md` itself is materially shorter. No rule was added anywhere.
Retired: `Wind-down re-scan (/plan's copy)` — the /plan-side full re-scan, superseded by done.md's file-only version which runs at every close. `Step 3: Close out` — /plan's close-out phase, superseded by /done.
FAQ: not needed because the user-visible behaviour that changes is Claude no longer offering to close at every checkpoint — an offer going away, which needs no entry. The four routes including "run /done" are covered by the new steer-a-planning-session entry written under [faq-backfill] in this same run.
