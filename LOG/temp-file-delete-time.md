# [HASH] — plugin-behaviour.md: a work item referencing a temp saved file must declare a delete-time

Added a "Temporary files and session artifacts" subsection under Research and evidence filing in plugin-behaviour.md. Two rules: prevention (route temp files to the scratchpad directory upstream so they never enter the project) and, when a temp file must live in the project because a work item references it, the work line must declare a specific delete-time up front. This is prevention, not a later sweep — the file's removal is owned by a named condition from the moment it's created. The original item's second half — an automated sweep of unspecified temp files — was dropped in /plan as unsound (kept-now ≠ keep-forever; new files are git-visible; historical files predate the feature so no session owns knowledge of them).

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md (one subsection shared with session-file-cleanup)

**Routed to Captures:** none
