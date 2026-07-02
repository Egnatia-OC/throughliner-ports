# e12c14d — Goal run: Build [proactive-queue-referenced-pushback] — proactive record-check added to plugin-behaviour.md's Prior decisions

Added the proactive record-check to plugin-behaviour.md's Prior decisions: when a user-proposed change would alter or reverse something the record already holds, run the Why-pipeline retrieve (LOG/index.md first, at most one entry) before agreeing, and cite any prior decision found. The trigger is deliberately narrow — never on new-work suggestions — to bound token cost; the named watch-line (over-reading the index across too many proposals) rides in the deferred test. Host-side observed test deferred.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md

**Routed to Captures:** none
