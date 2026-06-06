# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## [HASH] — /plan session: 3 batches promoted (research reframe, spectrum options, index-entry shape), 2 captures added

Three captures became batches this session, each landing in plugin-behaviour.md territory. The research-volunteering reframe addresses Claude's reluctance to offer research because the offer reads to itself as admitting a knowledge gap — the new section frames the offer as face-saving rather than face-losing, with a wide trigger (any time extra background would meaningfully inform the work) since offering is cheap and the user always filters. The spectrum-options batch fixes the bounded-list shape that lets users only steer among what Claude chose to show — visible options get arranged along a spectrum with off-the-ends extensions hinted, altitude-scaled (single spectrum for component-level, 2-3 axes tabular for whole-feature decisions), with a research-extension hook bound to the broader research rule. The index-entry batch fused two captures: the question of length limits on LOG index entries, and the parked coherence-test reframe. Both resolved to the same underlying rule — the index is Claude-facing, what an entry needs is artifact + nature of change with enough specificity for why-pipeline retrieve to decide whether to open the log entry. Length follows from that. The coherence test becomes "can you write the index entry now?" — when yes, the batch is ready, and the entry can be pre-generated in /next and reused by /done. Two new captures came out of the session: inconsistent visual treatment of output types Claude produces (batch drafts, recommendations, commit messages) across plan.md/next.md/done.md, and a rule that Claude's dependency-management ownership should be narrated rather than silent so the user perceives the value.

**Queue changes:**
- 3 batches added (research-volunteering reframe; spectrum options; index-entry shape + coherence test reframe — joint batch placed adjacent to "Promote recommendation must name concrete outputs")
- 2 captures added (output-types visual consistency; dependency-management narration)
- 4 captures removed (the 4 that became the 3 promoted batches)

**Captures routed:** 3 promoted, 2 added

## bc9b8e2 — /next batch presentation slimmed to title + gist + entry counts

Step 1.5 of next.md was dumping the full batch text — title plus every entry — at the moment the user was about to confirm a build. The user had just written that text in QUEUE.md and could open it anytime, so the re-render was noise without information. The new shape gives them what they actually need at that moment: which batch (title), what it's about (one-line gist drawn from the rationale), and how big (entry counts split build / test). The full text isn't lost — it moves into _build.md the moment they confirm, which is where it's actually referenced during execution. Two captures came out of the build: a faster LOG-hash-backfill design (single `git log -n 1` for the common case, `git grep -l` to short-circuit when clean, scope restricted to LOG/log.md and LOG/index.md so archived files containing the literal string `[HASH]` in prose don't false-positive) to fold into the already-queued backfill batch; and a /next scope-discipline rule — drop the "Adding to scope instead" sub-section that lets out-of-scope ideas leak into the active build's commit and log entry, replace with a narrower exception keyed to why-pipeline coherence.

**Files touched:**
- plugin/si-plugin/docs/next.md: Step 1.5 presentation bullet rewritten

**Routed to Captures:** faster LOG hash backfill (fold-in note for existing batch); /next no-fold-into-scope rule

## 1a74685 — /plan: parked 2 stuck audit captures under new /audit skill dependency; 6 new captures from session

The trickle-up audit and output-tag overhaul audit have been stuck in Captures across 6-7 /plan rounds — each session, new captures crowded them out, and /plan's dialogic capture-by-capture flow doesn't fit the read-many-propose-many shape audit work actually has. This session parked both pending a new /audit-skill capture that proposes a dedicated procedure for audit work (target on invocation, systematic read, propose moves, output to captures or batches). Five other captures came out of side-discussions: an affirmative-batch-definition fix (plan.md Ground rules has the negative form but no positive statement that batches are build-or-test only); a /next routing rule for mid-build discoveries of user-runnable testing; a /plan instruction to think about testing when authoring a batch; an append-vs-ordering rule tension between plugin-behaviour.md's two existing statements (captures append to bottom vs Claude owns sequencing) with a reconciliation of Claude-directed-where-applicable, oldest-first as default; and a between-captures checkpoint for /plan Step 2 so the user isn't forced to interrupt to /done. Alex also edited the QUEUE.md preamble inline to correct an inaccurate "builds first, then tests" framing — some batches have no build section. Item 3 (repo installation guide) opened mid-interview and remained in active Captures for next session.

**Queue changes:**
- 2 captures moved to Parked (trickle-up audit, output-tag overhaul audit) with dependency note on /audit skill
- 6 captures added (affirmative batch definition; /next user-testing routing; /plan testing during batch authoring; /audit skill design; append-vs-ordering rule reconciliation; between-captures checkpoint)
- QUEUE.md preamble inline-edited by user replacing "builds first, then tests" with build-session / test-session description
- LOG/index.md and LOG/log-v1.7.0.md: [HASH] placeholder for v1.7.0 entry backfilled to e5d3ca4

**Captures routed:** 2 parked
