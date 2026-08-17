# dc52025 — the content stamp stops hashing the version key, so it stops lying right after a rezip

The rezip installs a `-testN` version and the push resets it; separately, the content stamp hashes the installed plugin's files and a session compares it against the source. Both correct alone, and together they made the stamp report the host as stale immediately after a refresh — measured, not reasoned about: identical stamps after installing, then two different values after the version-clean and no other edit.

The obvious fix — excluding `plugin.json` wholesale — was refused on the item's own objection. The stamp exists to catch edits that bump no version, and dropping the file would make a renamed plugin or an altered description invisible to it. So `content_stamp()` reads that file as JSON, drops the `version` key, and hashes the rest. One function, run on both sides, so the two cannot disagree.

One consequence is written down rather than left to be discovered: a pure release bump, where only the version changes, will no longer move the stamp. That is correct rather than a loss — the stamp answers whether the installed host matches the source, and in that case it does.

The stamp's description in CLAUDE.md and the ritual's comparison step both say what is excluded and why, so the exclusion is not something a later session finds in the code and mistakes for an oversight.

Rule gate: run — a narrowing of the existing `content_stamp()` definition; no new mechanism, nothing always-loaded, nothing evicted.

**Queue changes:** [push-clean-breaks-the-content-stamp] kept into Processed, cleared to run.
**Work processed:** kept — [push-clean-breaks-the-content-stamp].
