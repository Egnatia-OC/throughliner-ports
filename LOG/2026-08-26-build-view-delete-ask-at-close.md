# [HASH] — The generated build view gets the lifecycle it never had: deleted silently at the close, ignored by the scaffold

Reported from a demo build session's close, which ended on "Shall I delete BUILD-VIEW.md?" — machinery leaking into the close's narration, and exactly the over-asking this method removes.

Checked at planning by grep, and the finding was worse than the report: the lifecycle had never been specified at all. next.md regenerates the view at each run's start and no doc said anything else about it — nothing cleaned it, nothing ignored it in a consumer repo. So the demo session improvised a question into a genuine gap, and this project's own `.gitignore` carrying the file was evidence of the gap rather than the fix, since it was hand-made and never shipped.

The lifecycle is now silent. The close deletes the view before committing — every run rebuilds it from the queue, so nothing is lost — and the scaffold ignores it so a mid-session copy never lands in a repository. setup.md writes the ignore line on both paths: the `.gitignore` scaffold step for new projects, and the settings-reconcile list for existing ones.

Refused at planning: gitignore-and-leave with no close cleanup, since a stale view sitting in the project invites a later session to read it as current; and keeping the ask, which is the reported defect.

**Files touched:** `plugin/throughliner/docs/done.md`, `plugin/throughliner/docs/setup.md`.
**Routed to Captures:** none.
**Depth:** short.
**Tick:** done, confirmed — no doc directs or permits asking the user about the view's lifecycle.
Rule gate: run — an amendment completing the build-view mechanism, its parent in next.md's generated-view rule, with the lifecycle it never had; nothing evicted.
