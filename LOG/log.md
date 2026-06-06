# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## [HASH] — Standardise approval-time outputs as fenced blocks across procedure docs

Approval-time outputs (batch drafts, capture wordings, proposed file content, recommendations, commit messages) were getting inconsistent visual treatment across plan.md / next.md / done.md — sometimes fenced, sometimes 4-space indented, sometimes inline prose. The shipped verbatim-copy rule already governed paste-target strings, but didn't cover approval outputs that aren't copy targets (a batch draft is read, not pasted). The fix names the rule once in plugin-behaviour.md Communication and sweeps the procedure sites that didn't already comply. done.md was already correct via the LOG-entry templates and verbatim-copy commit-message instructions, so it was left as-is per the batch instruction. The two rules now compose: a commit message is both verbatim-copy and approval-time, satisfied by one fenced block.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: added "Approval-time outputs go in a fenced code block" bullet to Communication, with cross-reference distinguishing it from verbatim-copy
- plugin/si-plugin/docs/plan.md: Step 2.3 Promote — explicit fenced-block instruction for batch drafts; Step 3 batch template — converted from 4-space indent to fenced markdown block
- plugin/si-plugin/docs/next.md: Step 4 Captures routing — explicit fenced-block instruction for capture wording

**Routed to Captures:** none

## cd574a8 — Tag the no-test-section decision as [SILENT] in plan.md Step 3

plan.md Step 3's Test section paragraph said when to include a Test section but not how to handle the omission case in output. That gap let Claude narrate the absence ("No Test section because the change is verifiable...") as if announcing the decision were part of the procedure. The user already wrote the rationale and knows what kind of change it is — the narration is noise. The tag system covers exactly this kind of output-behaviour rule, so the fix is one tag in the right spot rather than a prose substitute. Pairs with the parked output-tag overhaul audit, which would catch this same prose-where-tag-belongs pattern across the broader procedure docs once promoted.

**Files touched:**
- plugin/si-plugin/docs/plan.md: appended `[SILENT] when omitting...` clause to the Test section paragraph

**Routed to Captures:** none

## 3661578 — Add testing-thinking step to plan.md Step 3 batch authoring

plan.md Step 3 showed Build + Test subheadings in the template but never instructed Claude to actively think about what testing the batch would need at the moment of drafting. That omission let Test sections get skipped silently when they shouldn't, or get authored thinly because the thinking happened as an afterthought rather than as part of authoring. The fix adds the thinking explicitly, before the Test section paragraph: when drafting a batch, work through what verification the change needs, split Claude-runnable (read files, run commands, trace logic, inspect output) from user-runnable (visual, physical, subjective, separate live session), and populate the Test section with what falls out — or proceed without one when the change is self-verifying from the build entries. Either way the decision to omit gets made consciously, not by inattention. The split that used to live inside the Test section paragraph (Claude-vs-user split) was trimmed to a cross-reference since it's now the substance of the new thinking step. Pairs with the queued [SILENT] batch which governs how the no-test decision narrates rather than how it's reached.

**Files touched:**
- plugin/si-plugin/docs/plan.md: added "Think through testing when drafting" paragraph before the Test section paragraph; trimmed redundant Claude-vs-user split sentence from the Test section paragraph

**Routed to Captures:** none

## d1e9b5f — Add spectrum-options bullet to plugin-behaviour.md Communication

When Claude offers the user choices it surfaces a bounded list — deliberately, because exhaustive listings overload — but the side effect is the user only steers among what Claude chose to show. Arranging visible options along an axis (easy → hard, minimal → exhaustive) and signalling that more options exist off one or both ends gives the user steering room without bloating the list. The new bullet codifies the shape and splits it by altitude: component-level choices (one file, one bullet, one wording) use a single spectrum; choices that shape a whole feature, skill, or area use two or three axes laid out as a small table. The trigger for which altitude is the scope of the decision, not edit size. Extending a spectrum is a research moment — when the user asks to push past the ends or add an axis, or when Claude is about to extend beyond what it confidently knows even unprompted, Claude offers a web search per the Research section landed in the prior batch. The cross-reference makes the spectrum hook one concrete trigger for the broader research-volunteering behaviour, not a parallel mechanism. Bullet placed between the sequencing bullet (which shapes multi-part responses) and the verbatim-copy bullet (which shapes string presentation) since all three govern how Claude shapes user-facing output.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: added spectrum-options bullet in Communication section

**Routed to Captures:** none

## 43c6da8 — Reframe research-volunteering as face-saving in plugin-behaviour.md

Claude's default reluctance to offer web searches reads — to Claude itself — as admitting a knowledge gap, so the offer gets withheld even at moments where extra background would meaningfully inform the work. The Communication bullet about offering web searches names the *what* but doesn't address the *why-not* that keeps the behaviour from firing. The new Research section sits directly above Captures and reframes the offer from three angles: framing (checking current information is normal diligence in a fast-moving field, not a knowledge gap to hide), stakes (under-researched assumptions can cost a week of wrong work that's costly to undo, so when stakes are high the offer matters most), and how it reads to the user (waiting to be reminded the internet exists reads as weak; volunteering reads as capable). The trigger is wide on purpose — "any time extra background would meaningfully inform the work" — paired with the cheap-offer note (the user can always decline) so the bar to offer is low. External systems, libraries, and APIs are called out as one illustrative example rather than the rule, since the trigger is "would more current information change what we do next," not a fixed category list. The existing Communication bullet stays in place as the *what*; the new section is the *why*.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: added "## Research" section above "## Captures"

**Routed to Captures:** none

## 16fb410 — /plan session: 6 batches promoted, reconcile batch expanded with annotation+slugs pillar

Seven captures processed across two segments (the conversation compacted mid-session). Six promoted as new batches, one folded, one dropped, plus three parked-item updates. The six promotions: standardising output-type visual treatment across plan.md/next.md/done.md (fenced-block rule for approval-time outputs, distinct from the shipped verbatim-copy rule); documenting next.md build-abort mechanics (delete _build.md, return batch to QUEUE.md per Dependency ownership, route captures, write LOG entry describing the attempt); narrowing next.md Step 7's "keep adjusting" close-out language so adjustments mean within-scope tightening of already-built entries, not raising new items; sweeping done.md Plan close-out for removed-concept leftovers (drop "Questions resolved" + any other V47 OQ-era field — stale field names train Claude to fabricate); sweeping plugin/si-plugin/ for "disposition" jargon (replace with "promote, park, or drop" — Alex flagged she has trouble parsing the word herself, so external non-coders will too); and a downstream-impact scan in plan.md Step 2's Recommend step that fires when a capture installs a structural rule, so Claude flags downstream Captures that could revise or invalidate it before the user approves promote. The fold: dependency-management narration into the queued reconcile-append-vs-ordering batch, since the narration is what makes the placement/unpark/staleness work visible — silent ownership reads as no ownership. The drop: putting method docs under a single folder — CLAUDE.md autoload pins the file at root regardless, so the move is partial; ongoing per-session click cost outweighs occasional tidiness. The split: the /next-isn't-for-thinking-work capture separated three ways — the audit thread parked (in-scope/out-of-scope distinction audit, pending the audit-as-batch-type batch), and the two concrete next.md edits promoted as their own batches for distinct LOG entries. The audit-as-batch-type pivot from the prior session showed up again here: two existing parked audits (trickle-up, output-tag overhaul) still referenced the abandoned "/audit skill" framing, so their park notes got rewritten to point at the audit-as-batch-type batch dependency. At close-out, a question about reading dependencies at a glance across sessions led to expanding the reconcile batch with a fourth pillar — one-line `Depends on:` / `Blocks:` headers under each batch title plus stable kebab-case slugs (so references like "the queued reconcile batch" and "the two prior batches" become grep-able and reorder-safe), with a one-pass backfill so existing batches inherit the structure rather than waiting for organic adoption. The reconcile batch now covers four pillars at three levels of ownership: placement (reconciliation), narration (action-level), watches (ongoing curation), and annotation+slugs (artifact-level visibility).

**Queue changes:**
- 6 batches added: standardise output-type visual treatment (placed adjacent to verbatim-copy territory); build-abort mechanics + "keep adjusting" rewrite (placed before the mid-build user-testing routing batch); done.md Plan close-out leftover sweep (placed before stage-sweep-at-push); "disposition" jargon sweep (placed adjacent to the /clear-/compact sweep); downstream-revision scan (placed adjacent to the concrete-outputs batch)
- 1 batch expanded twice: reconcile-append-vs-ordering (folded in dependency narration mid-session; then folded in dependency annotation + stable slugs + one-pass backfill at close-out, with title and rationale extended accordingly)
- 7 captures removed from active Captures: 6 routed to promoted batches, 1 folded, 1 dropped (one of the 6 is the split that also generated a parked entry); Captures section now empty
- 1 new parked entry added: in-scope / out-of-scope distinction audit (third thread of the split capture)
- 2 existing parked notes rewritten: trickle-up audit and output-tag overhaul audit — repointed from "/audit skill" to "audit-as-batch-type batch"

**Captures routed:** 6 promoted, 1 folded, 1 dropped, 1 new parked, 2 parked-notes updated

## 93b73a5 — /plan session: 4 batches promoted including audit-as-batch-type pivot; 1 capture dropped after sanity check

Six captures processed. Four promoted into batches and one dropped after a sanity check; the fifth promotion was absorbed mid-session by the audit-as-batch-type pivot. The big move was the /audit-skill capture, which started as "design a separate /audit skill" and pivoted in conversation to "audit becomes a third batch type, /next branches on batch type the same way /done branches on stage, audit output routes through Captures." That pivot created tension with a small batch promoted three captures earlier ("Affirmatively define what a batch is" — build/test, nothing else); the user chose to supersede rather than layer, so the small batch was deleted from the queue and the audit batch absorbed its job in three-type form (build/test/audit). The audit batch also softens the existing thinking-work rule (thinking work doesn't become a *build* batch, but audit work can become an audit batch whose output is Captures-only). The other three promotions were tighter: a sweep for `/clear` and `/compact` references in skill and procedure docs to land after the two prior batches that remove the known sites; a next.md rule routing mid-build discoveries of unplanned user-runnable testing through Captures rather than inline-prompting or extending scope; and a plan.md Step 3 sub-step making the testing-thinking explicit at batch-authoring time, paired adjacent to the queued [SILENT] tag batch that controls how the no-test decision narrates. The dropped capture (done.md Plan Step 5 shouldn't exist) was already covered by the queued "Fold push offer into commit step" batch; `git log -S` confirmed the two commits that introduced Push-and-context were targeted close-out splits, not a carryover wave, so no further audit needed. One new capture surfaced during /done itself: the Plan close-out Step 1 recap field still lists "Questions resolved" as a bullet type, a leftover from when OPEN-QUESTIONS existed as a tracked concept.

**Queue changes:**
- 4 batches added: audit as a batch type (placed where the absorbed affirmative-definition batch was, before "Promote recommendation must name concrete outputs"); add testing-thinking step to plan.md Step 3 (placed adjacent to the [SILENT] tag batch); sweep `/clear` and `/compact` references (placed after "Fix /clear-before-/done close-out order"); route mid-build user-testing discoveries to Captures (placed after the sweep batch).
- 1 batch deleted: "Affirmatively define what a batch is" (absorbed by audit-as-batch-type pivot)
- 6 captures removed from Captures: 5 routed to promoted batches (one of those batches subsequently absorbed); 1 dropped
- 1 capture added: done.md Plan close-out Step 1 recap field — drop "Questions resolved" as OPEN-QUESTIONS leftover

**Captures routed:** 4 promoted, 1 dropped, 1 added

## d0d8c8e — Verbatim-copy strings get fenced blocks; commit title + body share one approval

The desktop app's Ctrl+C copies the whole assistant message, so a string is only cleanly copyable when it sits alone in its own fenced block. The plugin-behaviour rule now states that explicitly and covers the full set of cases — commit messages, commit bodies, paste-ready prompts, shell commands the user runs elsewhere — so the same shape applies wherever a copy-need surfaces, not just /done's commit step. Done.md's commit steps (Build 2.4 and Plan 3) were splitting commit title and body across two approval turns, which was redundant ceremony once the fenced-block rule exists: both halves are now presented as adjacent fenced blocks in one message and approved together. The rule lives in plugin-behaviour.md (one place), and the done.md steps cross-reference it rather than restating the why.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: added Communication bullet for verbatim-copy strings
- plugin/si-plugin/docs/done.md Section 2.4 (Build close-out commit): combined title + body into single approval, cross-referenced the new rule
- plugin/si-plugin/docs/done.md Section 3 (Plan close-out commit): same change

**Routed to Captures:** none

## fecdf76 — /plan session: 3 batches promoted (research reframe, spectrum options, index-entry shape), 2 captures added

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
