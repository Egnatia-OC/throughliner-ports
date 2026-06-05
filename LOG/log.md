# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## [HASH] — Thinking-work rule added to /plan Ground rules

plan.md's Ground rules already forbade building during /plan but had no inverse, leaving thinking work (audits, reviews, reconciliations/drift checks, design exploration) to be queued as batches by default — the routing call collapsed to whatever shape the previous capture took. Surfaced twice in V60 planning when both the trickle-up audit and output tag overhaul got framed as candidate batches. The new bullet pairs the existing rule: never queue thinking work as a batch, names the four recurring shapes, and gives the test — if the main work is figuring something out rather than executing on a decision, it's planning work, run it inside /plan, it spawns batches as output. Placed directly after "Never build during /plan" so the two rules read as paired.

**Files touched:**
- plugin/si-plugin/docs/plan.md: added one bullet to Ground rules after "Never build during /plan."

**Routed to Captures:** 2 — hash-backfill `git log -S` speedup (eliminates eyeball matching in /next pre-flight); /clear-before-/done close-out bug (suggested order strips the context /done needs to write the LOG entry).

## 8a01255 — Sequencing rule pulled into behaviour.md

The "one item at a time when the next action depends on the prior one" rule was relying entirely on the user's global CLAUDE.md, surfaced only through behaviour.md's tag-precedence note that defers unlabelled-step conversation to user preferences. Any install without that rule in the user's CLAUDE.md got bundle-prone close-outs and walkthroughs by default. The [SEQUENCE] tag already covered procedure steps that explicitly carried it, but the broader principle — covering any multi-part response across the session, not just tagged steps — needed to be plugin behaviour. Added as a Communication bullet rather than a new subsection to match the flat-bullet style of the rest of the section. The rule names the close-out/walkthrough hot zone explicitly because that's where the pull to bundle is strongest, and calls out alternatives as the one inversion because comparisons require seeing the options side by side.

**Files touched:**
- plugin/si-plugin/docs/behaviour.md: added one bullet at end of Communication section

**Routed to Captures:** 1 — behaviour.md spine should be always-loaded (mid-session capture, in response to repeated tag-adherence misses including the "no active build" narration this turn)
