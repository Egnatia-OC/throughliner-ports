# ee99142 — next-build.md Context-management section — removed the false "if context is running low" self-detection framing; kept the finish-vs-close-partial advice for when the user reports the squeeze

next.md's "if context runs long mid-build" stop was removed in an earlier session because /next can't self-detect context filling — Claude only learns a session is wearing thin when the *user* says so (plugin-behaviour.md's fresh-session-handoff rule). next-build.md's "## Context management" section still carried the same false premise: it opened "If context is running low, prefer in order: …", presupposing the self-detection. Reworded so the section states plainly that /next can't sense the context window filling and reframes the finish-vs-close-partial guidance as what to do *when the user reports the squeeze*, paired with the fresh-session handoff offer. Target-side; live after reinstall.

**Files touched:**
- plugin/si-plugin/docs/next-build.md (Context management section)

**Routed to Captures:** none
