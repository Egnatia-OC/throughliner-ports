# e12c14d — Goal run: Build [reference-by-slug-not-status] — added the slug-not-status wording rule to plugin-behaviour.md's Captures section

Added the slug-not-status wording rule to plugin-behaviour.md's Captures section: capture/batch prose references other queue items by slug and never asserts their status or assumes their presence, since a point-in-time status claim goes stale silently the moment the item moves and nothing mechanical flags free-prose claims; status is re-derived from LOG when the item is convened. Only the cheap preventive half was built — the convening-time re-check half was deliberately dropped for colliding with the token-drain risk named in [proactive-queue-referenced-pushback]. Host-side observed test deferred.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md

**Routed to Captures:** none
