# [HASH] — next-build.md: a build-time file-granularity heuristic for the AI-edited project

Added a "File structure — split by independent unit" section to next-build.md. The heuristic Claude recommends when building: split genuinely independent units (a self-contained tool, a standalone path) into their own files, because the AI does the editing — an edit's blast radius is one file, the AI reasons over less at once, and a mistake stays contained by the file boundary; but keep content that must be reasoned about as a connected whole in one file, because the AI reasons less well across files than within one. It's a recommendation Claude offers, not a hard rule. Home was settled in the build as next-build.md; reinforcing it as a SPEC principle was judged unnecessary — this is method build behaviour, not product truth, so next-build.md is the right and only home.

**Files touched:**
- plugin/si-plugin/docs/next-build.md
- plugin/si-plugin/templates/faq-template.md (new entry)
- plugin/si-plugin/templates/faq-index-template.md (index link)

**Routed to Captures:** none
