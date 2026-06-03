# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## 13c4612 — /plan session: 4 batches promoted, Plan panel dropped, context-window research

**Queue changes:**
- Promoted 4 batches: context management at skill handoffs + README model bump; fix next.md clean-slate output; reorder done.md Phase 3 handoff; add capture scan to next.md blocker gate
- Dropped the Plan panel incompatibility capture (research retained on disk)
- Added captures: capture-tag usefulness, "disposition" jargon, output-tag overhaul (absorbed the _build.md ticking item), threshold-based context management (parked)
- Fixed a structural slip: three promoted batches had landed in the Captures section mid-session; moved them up to Batches

**Why:** The /done-lost-context fix was repurposed at the user's direction from a symptom patch (a routing reminder) to a root-cause fix — prescribe /compact or /clear at every skill handoff. Web research confirmed neither the model nor plugin hooks can read context-window usage, so context management must be rule-based, not threshold-based. Plan panel integration was dropped after research showed the panel only renders via ExitPlanMode (read-only), which collides with /plan's writes and offers only marginal value for /next. README tested model set to Opus 4.6 on max effort.

**Captures routed:** 4 promoted, 1 dropped, 1 folded into a new capture; 4 new captures added (1 parked); 4 original captures left unprocessed (pull-down audit, trickle-up audit, /done close-out wording, no-test-section narration).

## 23a1da8 — /plan session: promote inline-reads rule, add capture

**Queue changes:**
- Promoted "Add inline-reads rule to behaviour.md" to top of Batches
- Added new capture: silent test-section decision narration

**Why:** Claude spawned an agent for the pre-push consistency sweep — work that only needs inline reads. Promoted a behaviour.md rule to prevent this across all skills. Session cut short to address procedure adherence issues; 9 captures remain unprocessed.

**Captures routed:** 1 promoted (inline-reads rule), 9 unprocessed
