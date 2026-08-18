# 7e3c1c8 — the content stamp ignores plugin.json's version, so a rezip stops reading as stale

`content_stamp()` in `session_start.py` now hashes `plugin.json` with its `version` key dropped, through a new `_plugin_json_without_version()`. One function, run on both sides, so the two cannot disagree. Unparseable JSON returns unchanged — a stamp that still moves beats one that raises inside a session start.

The version string is the one field the two packaging rituals deliberately disagree about: the rezip sets a `-testN` suffix, the push resets it, and neither changes what the plugin does. Left in, it made the stamp report the host stale immediately after every rezip — measured at `b4bb37b9c1b6` on both sides right after installing, then `654c88680de8` against `b4bb37b9c1b6` after the version-clean and no other edit. A check that answers wrongly in its most common case is the cry-wolf shape this project has repealed measures for before.

Excluding the whole file was refused on the item's own objection: a renamed plugin or an altered description would then become invisible to a stamp built to catch edits that bump no version. Verified against that objection rather than assumed — a version-only change leaves the stamp still, while a description change and an ordinary package-file change both move it.

One consequence, written down rather than discovered later: a pure release bump, where only the version changes, no longer moves the stamp. That is correct — the stamp answers whether the installed host matches the source, and in that case it does.

`CLAUDE.md` and `release-ritual.md` both now say what is excluded and why.

Rule gate: run — a narrowing of the existing stamp definition; nothing evicted.

**Files touched:** `plugin/throughliner/hooks/session_start.py`, `CLAUDE.md`, `resources/release-ritual.md`
**Routed to Captures:** none
