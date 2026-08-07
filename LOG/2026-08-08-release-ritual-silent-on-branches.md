# [HASH] — Release trigger gains a branch condition: fires only on main; the spreading-risk escape is merge-sooner

Built in the 2026-08-08 overnight blitz. CLAUDE.md's release check now states: check the branch first, and on any branch other than `main` the release check does not run — it fires at the first /done after the merge. The written rule carries the two pieces the processing decided must be explicit: this is not a quality condition and must not be read as precedent for one (a branch check is the same mechanical kind as the file check, and the ritual's bar on readiness judgments stands untouched); and when a held release contains an actively-spreading fix, the escape is to expedite the **merge**, never to release from the branch — one route built from the red-flag triage that already exists, preserving the audit gate and the single version line. The rejected branch-release-with-own-version-convention alternative is recorded as a permanent version fork accepted for a temporary situation. The branch-cycle section gains the reciprocal pointer, since the two rules were each written without the other in view and that silence is how the gap arose. Host-only: consumers have no release ritual.

**Files touched:** CLAUDE.md
**Routed to Captures:** none
FAQ: not needed because the release ritual and branch cycle are host-only; consumer projects never see either.
