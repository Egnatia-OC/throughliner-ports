# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## 3da827c — /plan session: queue one-item-at-a-time and thinking-work-isn't-a-batch rules

Two structural rules surfaced from a single /plan session. The first came from auditing Alex's global CLAUDE.md against the test "would the plugin behave differently if installed on someone else's CLAUDE.md?" — the multi-part-response sequencing block (one per message when dependent, count upfront, no preview, alternatives-inversion) was the only universal-shaped rule whose absence would change skill close-outs and walkthroughs on another install. The plugin currently delegates this to the user's CLAUDE.md via the tag-precedence note in behaviour.md; the broader principle belongs in behaviour.md as plugin behaviour. Other items in global CLAUDE.md (push-back over agreement, don't perform enthusiasm, environment-specific defaults) read as personal style and were left out. The second rule emerged live: Claude framed both the trickle-up audit and the output tag overhaul as candidate batches when both are planning work whose output is decisions, not changed files. The current Ground rules section says "Never build during /plan" but has no inverse — nothing stops planning work from being queued as a batch, and the default becomes whatever shape the previous capture took. Naming the recurring shapes (audits, reviews, reconciliations/drift checks, design exploration) gives the routing decision a clear test. The rule's boundary is fuzzy at the edges — find-and-rewrite audits with bounded per-finding judgment may belong as batches; this came up around the audience-framing batch already queued, deferred for now.

**Queue changes:**
- Added: "Pull 'one item at a time' rule into behaviour.md" (bottom of Batches)
- Added: "Add 'thinking work isn't a batch' rule to plan.md" (below the above)

**Captures routed:**
- Absorbed into the new batches: Pull-down audit, "one item at a time" rule
- Parked: Trickle-up audit, Output tag overhaul audit
- Dropped (already covered by audience-framing batch): Disposition jargon
