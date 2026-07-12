# [HASH] — faq-template.md + faq-index-template.md — reconciled the consumer FAQ to the work-line model: removed the two dependency-graph entries ("out of order / dangling", "circular dependency"), reframed the "why does Claude read my files first" entry away from dependency-tracing, and fixed the "Cleared to run above this line" entry to say vetted-and-ready rather than "everything it depends on is accounted for"; index lines updated to match.

The work-line recut removed the dependency-tracing machinery (producer checks, out-of-order/dangling detection, circular-dependency handling), but the shipped consumer FAQ still described it — so a consumer reading those entries would expect behaviour the method no longer has. Fixed by matching the FAQ to what the model actually does now: dropped "out of order / dangling" and "circular dependency" entirely (a consumer can't hit either — dependencies are gone from the model). Dropped the "why does Claude read through my files first" entry rather than reframing it — its whole premise was dependency-tracing at queue-add time, so with that gone there was no accurate behaviour left to point the question at. Rewrote the "Cleared to run above this line" entry to say the marker means vetted/discussed-and-agreed, not "order is right and everything it depends on is accounted for," and swapped its stale "when the unattended build mode arrives" for "a /cruise run" now that /cruise ships. Index template cut to match. Completes the work-line recut's consumer-doc cleanup.

**Files touched:**
- plugin/si-plugin/templates/faq-template.md: removed 2 entries, dropped 1, rewrote 1
- plugin/si-plugin/templates/faq-index-template.md: removed 3 index lines

**Routed to Captures:** none
