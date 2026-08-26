# 3b094b5 — The close's cycles check now reads the disk at close time instead of trusting the opening's belief

Diagnosed from the demo chat's transcript before this build: the check was skipped rather than run-and-found-clean. That chat's /next pre-flight correctly reported no cycles doc, the build then created `CYCLES.md` mid-run, and from /done's start to the commit the close never read the file from disk — it carried the opening's "no cycles doc" belief across a session that had itself created the doc. Session memory covered for a file read, which is the exact failure the design-for-fresh-sessions rule names.

So the step's trigger moved. done.md's cycles due-ness step now opens by reading the project root for `CYCLES.md` at close time, and says plainly that a doc created this session counts and that the opening's no-cycles-doc report is stale the moment anything creates one. The `[SILENT]`-when-clean tagging is unchanged.

Two things were refused at planning and are recorded here so they are not re-proposed. Mirroring the wording into plan.md and next.md's opening sites: those run at session start where no stale belief exists. And a required close-time artifact line for the check: a line at every close whether or not cycles exist is the cry-wolf shape this project has repealed measures for twice.

**What this fix does not cover, found the same day it shipped.** The verification walk-through ran its deferred opening-site test later in this session, and the opening failed too — a fresh /plan in that project, with the file on disk and the cycle due, filed nothing and said nothing. So the two live failures share a cause this item does not name. Filed as [cycles-check-fires-nowhere]. This build fixes a real defect and is not the whole story, and the entry says so rather than letting a shipped fix imply a solved problem.

**Files touched:** `plugin/throughliner/docs/done.md`.
**Routed to Captures:** [cycles-check-fires-nowhere] — filed during the walk-through, not by this item's build.
**Depth:** short.
**Tick:** done, confirmed.
Rule gate: run — an amendment to done.md's cycles due-ness step, its parent: the step's trigger becomes a fresh disk read, superseding the wording that let a remembered opening state stand in for one.
