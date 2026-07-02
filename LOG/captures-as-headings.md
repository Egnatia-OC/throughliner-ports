# [HASH] — Goal run: Build [captures-as-headings] — captures now file as #### headings in QUEUE.md; lint learned the heading slug form

Captures now file as `####` headings (slug at the end of the heading line) so editor outlines show the whole capture list including Parked, where bullet captures were invisible. Reformatted QUEUE.md's parked captures (content preserved verbatim; nested sub-bullets keep their indent so the lint reads them as continuations); taught post_tool_use.py the heading form as a second slug-definition shape and made an h4 line start a parked item in the header check; canonical format statement added to plugin-behaviour.md Captures with references in plan.md, done.md's wind-down, and setup.md's QUEUE scaffold; FAQ entry + index line added, plus the stale "captures are plain bullets" FAQ line fixed. Batches keep bold titles. Run-now lint fixture passed: a heading-form slug resolves references, a genuinely dangling slug still flags, and a heading-form parked item without a Blocked by:/Parked: header still flags. Host-side test deferred (first post-reinstall /plan files a capture as a heading; the editor-outline check is the user's eyeball).

**Files touched:**
- QUEUE.md
- plugin/si-plugin/hooks/post_tool_use.py
- plugin/si-plugin/docs/plugin-behaviour.md
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/docs/done.md
- plugin/si-plugin/docs/setup.md
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none
