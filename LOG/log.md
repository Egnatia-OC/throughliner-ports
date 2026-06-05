# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## [HASH] — Plugin-behaviour spine re-anchored at skill invocation with authoritative framing

behaviour.md was the method's spine but drifted across sessions: it loaded once at session start under the ambient "additional context" framing, with no header asserting authority, while procedure docs at skill invocation pushed 100+ lines of newer material that out-prominenced it. Three structural changes close the gap. The file is renamed to plugin-behaviour.md so its scope is self-describing. The session_start hook now wraps the file's contents with "=== PLUGIN-WIDE BEHAVIOUR RULES (active every session, govern every skill) ===" / "=== END BEHAVIOUR RULES ===" so the framing reads as governing rules rather than ambient notes; SPEC/QUEUE/REGISTRY status, version warnings, and FAQ index stay outside the wrapped block. Each SKILL.md (plan, next, done) gained one line above the "Read and follow the procedure" pointer that re-anchors plugin-behaviour.md as governing this skill at a level above the procedure, so the spine arrives alongside the procedure with equal recency. Internal references in plan.md, done.md, CLAUDE.md, REGISTRY.md, and the live reader-test-workflow.js were all updated to the new filename. This batch supersedes the earlier "mirror response shape tags into CLAUDE.md and template" batch — that was a partial mirror compensating for unreliable spine loading; with the spine now reliably loaded and authoritatively framed, mirroring is unnecessary.

**Files touched:**
- plugin/si-plugin/docs/behaviour.md → plugin/si-plugin/docs/plugin-behaviour.md (rename)
- plugin/si-plugin/hooks/session_start.py: behaviour_path retargeted; behaviour_rules append wrapped in authoritative header/footer
- plugin/si-plugin/skills/plan/SKILL.md, skills/next/SKILL.md, skills/done/SKILL.md: each gained a one-line re-read pointer above the procedure-read line
- plugin/si-plugin/docs/plan.md, docs/done.md: 2 references each updated to plugin-behaviour.md
- CLAUDE.md: example-list reference updated
- REGISTRY.md: docs-list reference updated
- resources/reader-test-workflow.js: BEHAVIOUR path constant updated

**Routed to Captures:** none

## 11c81a2 — /plan session: process 3 captures, promote behaviour-rules restructuring batch

Three captures processed before the user closed the session: the /clear-before-/done close-out misordering (next.md and plan.md both tell the user to /clear before running /done, but /done reads the conversation to write the LOG entry, so clearing first strips what /done draws on), the slow hash-backfill procedure (`git log --diff-filter=A` and blame both require eyeball matching of titles to commits and full-log reading for orientation; `git log -S "<title>" --pretty=%h -- LOG/` returns the hash mechanically), and behaviour.md not reliably governing skill behaviour despite the session_start hook already loading it. The third capture's premise turned out to be partly wrong — the hook does inject behaviour.md — but the symptom (inconsistent tag adherence) is real, so investigation continued in-session. Doc-injection chain checked across all three skills: SKILL.md is 13 lines and jumps straight from "user invoked /next" to "read the procedure," with no re-anchor to the spine; procedure docs (100+ lines, just-read, high prominence) then out-prominence the ambient session-start injection. Three combined fixes resolved as one batch: rename behaviour.md to plugin-behaviour.md so the filename describes its scope, wrap the injected text in an authoritative header inside the hook output so the model treats it as governing rules, and add one line to each SKILL.md re-loading the file before the procedure doc. The queued "Mirror response shape tags into CLAUDE.md and template" batch was dropped as superseded — it was a partial mirror compensating for unreliable spine loading. Session ended at capture 4 of 12 because the user closed early; remaining 9 captures stay in QUEUE.md for the next /plan session.

**Queue changes:**
- Added (position 1): "Re-anchor plugin-wide behaviour rules at skill invocation and inject them with authority"
- Added (position 8): "Fix /clear-before-/done close-out order"
- Added (position 9): "Speed up LOG hash backfill with `git log -S`"
- Removed: "Mirror response shape tags into CLAUDE.md and template" (superseded)

**Captures routed:** 3 promoted (/clear close-out misordering, hash-backfill speedup, behaviour.md authoritative loading); 9 remain unprocessed.

## f97990f — Thinking-work rule added to /plan Ground rules

plan.md's Ground rules already forbade building during /plan but had no inverse, leaving thinking work (audits, reviews, reconciliations/drift checks, design exploration) to be queued as batches by default — the routing call collapsed to whatever shape the previous capture took. Surfaced twice in V60 planning when both the trickle-up audit and output tag overhaul got framed as candidate batches. The new bullet pairs the existing rule: never queue thinking work as a batch, names the four recurring shapes, and gives the test — if the main work is figuring something out rather than executing on a decision, it's planning work, run it inside /plan, it spawns batches as output. Placed directly after "Never build during /plan" so the two rules read as paired.

**Files touched:**
- plugin/si-plugin/docs/plan.md: added one bullet to Ground rules after "Never build during /plan."

**Routed to Captures:** 2 — hash-backfill `git log -S` speedup (eliminates eyeball matching in /next pre-flight); /clear-before-/done close-out bug (suggested order strips the context /done needs to write the LOG entry).

## 8a01255 — Sequencing rule pulled into behaviour.md

The "one item at a time when the next action depends on the prior one" rule was relying entirely on the user's global CLAUDE.md, surfaced only through behaviour.md's tag-precedence note that defers unlabelled-step conversation to user preferences. Any install without that rule in the user's CLAUDE.md got bundle-prone close-outs and walkthroughs by default. The [SEQUENCE] tag already covered procedure steps that explicitly carried it, but the broader principle — covering any multi-part response across the session, not just tagged steps — needed to be plugin behaviour. Added as a Communication bullet rather than a new subsection to match the flat-bullet style of the rest of the section. The rule names the close-out/walkthrough hot zone explicitly because that's where the pull to bundle is strongest, and calls out alternatives as the one inversion because comparisons require seeing the options side by side.

**Files touched:**
- plugin/si-plugin/docs/behaviour.md: added one bullet at end of Communication section

**Routed to Captures:** 1 — behaviour.md spine should be always-loaded (mid-session capture, in response to repeated tag-adherence misses including the "no active build" narration this turn)
