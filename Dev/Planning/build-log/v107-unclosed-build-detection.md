# V107 — 2026-05-27 — Unclosed-build detection in SessionStart

**What shipped.** SessionStart now detects when an active batch has all `Files:` entries ticked but `/sovclose` was never run. When detected, a prominent warning names the batch and instructs Claude to prompt the user to run `/sovclose` before starting new work. The unclosed-build status also appears in the user-facing session-open status block. Works in both single-file and folder-mode BACKLOG. Four new tests added (positive detection, status summary integration, two false-positive guards). Method version bumped to V86 (plugin 0.86.0) across 23 files.

**Decisions taken and why.** Detection uses `Status: active` + all files ticked rather than checking for a missing build-log entry. This is sufficient because `/sovclose` always transitions status to `shipped` — so an active-with-all-ticked batch is definitionally unclosed. It also catches partial `/sovclose` runs (where the session died mid-close before the status transition). Batch 0106 (post-build proxy regeneration) was skipped as already implemented by close.md step 11.

**Pivots and surprises.** None. Clean implementation matching scope.

**Carried forward.** Nothing.
