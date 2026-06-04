# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## [HASH] — V60 planning: capture sweep, structural rules, hash-backfill fix

The session opened by catching the top batch — "Audience-framing anchor and skill-output language audit" — for embedding audit passes that the queued "thinking work isn't a batch" rule will forbid. Restructured: the concrete CLAUDE.md anchor stayed as a small batch; the audit passes dropped (no parked planning entries — those aren't a queue shape). Two parked entries with the same problem (Trickle-up audit, Output tag overhaul audit) got moved back to active Captures rather than left as planning-batch-shaped Parked items.

Capture processing then surfaced eight new batches. Several were tightly user-facing — brief batch display at /next start (the full re-render was content the user just wrote), commit message and body as paired copyable fenced blocks with a single combined approval, and a general rule about verbatim-copy strings going into fenced blocks because the desktop app's Ctrl+C grabs the whole message. Two structural rules for /plan landed: the no-test-section omission gets tagged `[SILENT]` instead of narrated; promote recommendations must describe what would actually get built in terms the user recognizes, with a forcing function that says if the interview hasn't yielded that yet, the recommendation isn't ready. This came from realizing concrete-output framing has been bridged by model style this session — and that won't survive future model upgrades.

The hash-backfill bug got a clean fix: /done currently writes LOG with a `[HASH]` placeholder, commits, runs rev-parse, replaces, and amends — but the amend rewrites the hash, so every recorded hash is wrong (13c4612 vs 44ab617 this session). The fix moves the backfill out of /done entirely. /done commits with the placeholder. The next /plan or /next session, at start, scans for `[HASH]` placeholders and fills them in from the commit that introduced each entry. The infill rides along on whatever commit that session later makes. No amend, no second commit.

Two batches strengthened behaviour.md rules. Why-pipeline preserve was expanded to name the three rationale-collapse shapes (one-line summaries, dedicated why-fields, typed taxonomies) and include its own why woven in as prose — modeling what the rule asks for. Why-pipeline retrieve was updated to use LOG/index.md first (the one-line-per-entry summary) before reading full log files, making "why is the app like this?" answers faster and more accurate. The mirror-tags-into-CLAUDE.md batch closes a related gap: response shape tags only load on-demand via behaviour.md, so when /plan drafts procedure-doc changes, prose substitutes leak in. Mirroring the tags into the always-loaded CLAUDE.md makes tag use the default move.

A real-world bug in push-and-rezip got addressed: step 8's staging list is hardcoded and doesn't include whatever the pre-push consistency sweep touched, so sweep edits get orphaned in the working tree across sessions and later builds layer changes on top. Fix is two complementary parts: at push, stage every dirty path in plugin/si-plugin/ instead of a fixed list; at session start with no active build, warn if the plugin tree is dirty so orphans are visible before /next.

A feedback memory got saved: use response shape tags rather than prose substitutes when authoring procedure docs. The user flagged this pattern twice in one session — once via the existing audit capture, once during the no-test-section [SILENT] discussion when I proposed prose instead of the tag.

**Queue changes:**
- Replaced batch 1 (Audience anchor in this project's CLAUDE.md — smaller scope, audit dropped)
- Added 8 batches at positions 5–12
- Moved 2 entries from Parked back to active Captures (Trickle-up audit; Output tag overhaul audit)

**Captures routed:** 7 promoted; 2 skipped (audits, left active); 0 parked; 0 dropped

## 24b5feb — Remove the [idea]/[question] capture tags

The two places these tags lived in the plugin's shipped surface — faq-template.md and CLAUDE-TEMPLATE.md — disagreed about what the tags meant. The FAQ presented [idea] and [question] as parallel categories of capture; the idea → question pipeline in plan.md and behaviour.md treats them as sequential refinement stages in a discussion (a raw idea gets sharpened into a question only when a real decision needs resolving). No procedure branches on the tags at runtime — they're cosmetic. Two contradictory definitions of dead syntax was getting shipped to every new project at /setup. Fix is removal, not reconciliation: captures become plain bullets that carry their own reasoning inline, which matches the "don't collapse rationale into structure" principle already informally observed across captures. The faq-template line about Captures was rewritten as "Captures are plain bullets — each carries its own reasoning inline." The CLAUDE-TEMPLATE parenthetical "([idea]/[question] tags)" became "(plain bullets)." The "I just had an idea" FAQ answer dropped the "as an [idea] entry" phrase. The live QUEUE.md had 16 leading `[idea] ` tokens stripped — 15 under Captures (per the literal batch scope) and one more under Batches > Parked (Sizing gates rework), folded in mid-build as a one-line consistency call so the file ends up tag-free.

**Files touched:**
- plugin/si-plugin/templates/faq-template.md: rewrote Captures-description sentence and "I just had an idea" answer to drop tag references.
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md: changed "([idea]/[question] tags)" to "(plain bullets)" in the QUEUE.md doc line.
- QUEUE.md: stripped leading "[idea] " from all 16 bullets (15 under Captures + 1 under Batches > Parked).

**Routed to Captures:** none

## 3da827c — /plan session: queue one-item-at-a-time and thinking-work-isn't-a-batch rules

Two structural rules surfaced from a single /plan session. The first came from auditing Alex's global CLAUDE.md against the test "would the plugin behave differently if installed on someone else's CLAUDE.md?" — the multi-part-response sequencing block (one per message when dependent, count upfront, no preview, alternatives-inversion) was the only universal-shaped rule whose absence would change skill close-outs and walkthroughs on another install. The plugin currently delegates this to the user's CLAUDE.md via the tag-precedence note in behaviour.md; the broader principle belongs in behaviour.md as plugin behaviour. Other items in global CLAUDE.md (push-back over agreement, don't perform enthusiasm, environment-specific defaults) read as personal style and were left out. The second rule emerged live: Claude framed both the trickle-up audit and the output tag overhaul as candidate batches when both are planning work whose output is decisions, not changed files. The current Ground rules section says "Never build during /plan" but has no inverse — nothing stops planning work from being queued as a batch, and the default becomes whatever shape the previous capture took. Naming the recurring shapes (audits, reviews, reconciliations/drift checks, design exploration) gives the routing decision a clear test. The rule's boundary is fuzzy at the edges — find-and-rewrite audits with bounded per-finding judgment may belong as batches; this came up around the audience-framing batch already queued, deferred for now.

**Queue changes:**
- Added: "Pull 'one item at a time' rule into behaviour.md" (bottom of Batches)
- Added: "Add 'thinking work isn't a batch' rule to plan.md" (below the above)

**Captures routed:**
- Absorbed into the new batches: Pull-down audit, "one item at a time" rule
- Parked: Trickle-up audit, Output tag overhaul audit
- Dropped (already covered by audience-framing batch): Disposition jargon
