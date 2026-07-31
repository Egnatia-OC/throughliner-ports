# ca03428 — /done reads handmade edits as expected work (don't-panic) and absorbs standalone handmade-work wrap-up

Two jobs. Job 1 — a File-safety behaviour rule: uncommitted edits Claude didn't make are read by default as the user's expected handmade work, not a broken repo; confirm and fold them in, never report as damage or reset. It's a disposition, so it's wording, not a hook. Job 2 — /done gains a standalone handmade-work close (no _build.md, no planning): confirm the edits are the user's, write a date-named LOG entry (`handmade-<date>`), and commit; the routing now splits a no-_build.md close into planning vs handmade-work. When standalone edits span several distinct logical changes, Claude writes a separate entry per change by judgment rather than one lump — better recall later; the exact granularity defers to the two-section LOG-index question. Never required, always available — it's the home freeform's close used to own, which is why [retire-freeform] depended on it shipping first.

**Files touched:**
- plugin/si-plugin/docs/done.md — routing split + "Standalone handmade-work close" section + LOG-naming list
- plugin/si-plugin/docs/plugin-behaviour.md — File-safety don't-panic bullet
- SPEC.md — /done capability
- plugin/si-plugin/templates/faq-template.md + faq-index-template.md — new entry + index line

**Routed to Captures:** none
