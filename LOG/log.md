# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## [HASH] — Sequencing rule pulled into behaviour.md

The "one item at a time when the next action depends on the prior one" rule was relying entirely on the user's global CLAUDE.md, surfaced only through behaviour.md's tag-precedence note that defers unlabelled-step conversation to user preferences. Any install without that rule in the user's CLAUDE.md got bundle-prone close-outs and walkthroughs by default. The [SEQUENCE] tag already covered procedure steps that explicitly carried it, but the broader principle — covering any multi-part response across the session, not just tagged steps — needed to be plugin behaviour. Added as a Communication bullet rather than a new subsection to match the flat-bullet style of the rest of the section. The rule names the close-out/walkthrough hot zone explicitly because that's where the pull to bundle is strongest, and calls out alternatives as the one inversion because comparisons require seeing the options side by side.

**Files touched:**
- plugin/si-plugin/docs/behaviour.md: added one bullet at end of Communication section

**Routed to Captures:** 1 — behaviour.md spine should be always-loaded (mid-session capture, in response to repeated tag-adherence misses including the "no active build" narration this turn)
