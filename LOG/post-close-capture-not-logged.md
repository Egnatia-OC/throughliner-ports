# [HASH] — plugin-behaviour.md: stamp every capture with a filing-time commit anchor

Added a filing-time commit-stamp rule to the Captures line-format block in plugin-behaviour.md: every new capture carries "filed after `<hash>`" (the last commit that existed at filing time) in its provenance area. The why: a capture filed after a session's /done close belongs to no committed record at the moment it's made — the next session processes it and logs that, so the capture event itself was otherwise untraceable. The stamp is a filing-time estimate that flows into the LOG naturally when the item is later processed. It sits as plain prose beside the provenance label the queue lint keys on ("captured by you" / "by Claude"), so no lint change was needed; the capture-filing points in plan.md / next.md / done.md inherit the rule through their existing "per plugin-behaviour.md Captures" references, so no per-doc duplication was needed. Dogfooded live this session — the three captures filed all carry the stamp.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md
- plugin/si-plugin/templates/faq-template.md (new entry)
- plugin/si-plugin/templates/faq-index-template.md (index link)

**Routed to Captures:** none
