# [HASH] — plan — [release-ritual-opens-its-record] kept: the ritual opens the item that scheduled it and writes its record at the end

From the release trace: the v1.21.0 ritual ran post-close, never opened the release-pick item, and executed its final steps with no record under its slug. Barring post-close releases lost on structure — the ritual commits, and a session's one commit is the close's, so post-close is the only slot. The ritual gains its own record discipline instead: a queue read at the top, a record write at the end. Host-only.

**Queue changes:** [release-ritual-opens-its-record] filed and cleared; [release-ran-outside-any-skill] deleted as merged.
**Work processed:** kept — [release-ritual-opens-its-record].
Rule gate: run at the keep — host-only ritual amendment; recorded on the item.
