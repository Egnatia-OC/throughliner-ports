# [HASH] — session_start.py: backfill now loudly flags a committed entry whose hash placeholder didn't resolve

The LOG hash-backfill demonstrably works in this project, but scrolly-thing's failure (2026-07-16) showed it can fail silently and accumulate unnoticed. Two candidate root causes by inspection: (A) `git log -S <entry_title>` returns nothing when the index line's text was reworded after commit; (B) a consumer session closing without committing the LOG loses the fill and the placeholder persists.

This build makes silent failure loud, independent of root cause. Added a `_file_is_committed(cwd, relpath)` helper; `backfill_log_hashes` now flags any placeholder that stayed unresolved while its entry file is *already committed* in git — it should have resolved — collecting the anomalous files and appending a one-line session-start notice naming the count and files, instead of the old silent `continue`. The already-committed check avoids false-alarming on the current session's own not-yet-committed entry, whose unfilled placeholder is normal. Confirming the scrolly-thing root cause against its real data is left as a follow-up; this turns silent accumulation into a noticed signal regardless of cause.

Both hooks were syntax-checked after the edit. No FAQ — the notice is a rare internal diagnostic, and the backfill mechanism is background-only.

**Files touched:**
- plugin/si-plugin/hooks/session_start.py (`_file_is_committed` helper; backfill anomaly notice)

**Routed to Captures:** none
