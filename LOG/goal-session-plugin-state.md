# [HASH] - CLAUDE.md: fix the goal-session doc for how plugin enable/disable really works

The Goal sessions section assumed the plugin is off (scope-lock and session-start hook silent), but disabling a plugin mid-session does not stop its hooks - components only re-apply on /reload-plugins or a restart, and an open bug has disabled plugins still firing SessionStart hooks. The section now states the correct way to run plugin-off (disable AND start a fresh session, i.e. a full app restart on desktop), pointing to the research file, softens the (plugin off) framing to an aim, and makes the procedure robust to the plugin being left on (the aggregate _build.md must list every file so the scope-lock cannot deny an edit; the hand-backfill is a backstop that may correctly find nothing). Host-only.

**Files touched:**
- CLAUDE.md

**Routed to Captures:** none
