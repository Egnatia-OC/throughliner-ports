# [HASH] — The dead `.claude/launch.json` deleted and 52 stale allow-entries removed

`launch.json` held one configuration serving `sovereign-implementer/crash-course`, a directory that has not existed for months. Nothing here to repoint, so it is deleted rather than fixed.

`settings.local.json` carried 66 allow-entries. 52 named the retired `sovereign-implementer/` layout, the old `C:\Users\Alex\` user path from before the machine move, or directories long gone — `Dev/`, `Guides/`, `planning/sessions/`, `tests/`. Those are removed; the 14 naming something that still exists are kept, along with the statusLine command.

One thing worth recording because it was nearly got wrong: the first pass consolidated two narrow slug-specific `reorder_queue.py` entries into a wildcard and added `py` variants. That grants broader permission than the item asked for, and permission breadth is the user's call, not a build's — so it was reverted to exactly the entries that existed.

**Files touched:** .claude/launch.json (deleted), .claude/settings.local.json
**Routed to Captures:** none
Rule gate: not needed — config cleanup; no method rule changes.
