# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## [HASH] — Sweep stray `/clear` references from setup.md and next.md close-outs

Safety sweep behind the prior two batches (push-in-commit and fix-clear-before-done). Grep across plugin/si-plugin/ for `/clear` and `/compact` turned up two surviving close-out sentences — setup.md's final "Run /plan or /next" sign-off and next.md's audit close-out (Step 6) — both still trailing the misplaced "Run `/clear` first to keep context clean." advice the prior batches had cleared from the more visible close-outs. Reasoning: when to clear or compact is a user judgment about session continuity, not a procedural nudge skill docs should issue routinely. plugin-behaviour.md had zero hits so the case-by-case review there was a no-op. Re-grep confirmed nothing survives in skill or procedure docs. `/compact` had no hits anywhere.

**Files touched:**
- plugin/si-plugin/docs/setup.md: Step "After all 5 answers" sub-step 4 — dropped trailing "Run `/clear` first to keep context clean." sentence
- plugin/si-plugin/docs/next.md: Step 6 audit close-out — dropped trailing "Run `/clear` first to keep context clean." sentence

**Routed to Captures:** none

## dfdc113 — Drop misplaced "Run `/clear` first" sentence from next.md and plan.md close-outs

next.md Step 7 and plan.md Step 4 both told the user "Run /done to record this and commit, or keep adjusting. Run `/clear` first to keep context clean." The "first" placed /clear before /done, but /done reads the conversation to write a faithful LOG entry — clearing first would strip exactly what /done draws on. The /clear advice already lives correctly at the end of /done itself, where it recommends clearing before the next skill. Fix was a one-sentence drop in each of the two close-outs; the /done offer stays, and the correctly-placed advice at the tail of /done continues to carry the guidance. This batch removes two specific sites; the queued sweep-clear-compact batch is the safety net behind it.

**Files touched:**
- plugin/si-plugin/docs/next.md: Step 7 sub-step 3 — dropped trailing "Run `/clear` first to keep context clean." sentence
- plugin/si-plugin/docs/plan.md: Step 4 sub-step 2 — dropped trailing "Run `/clear` first to keep context clean." sentence

**Routed to Captures:** none

## 710e56e — Stage sweep edits at push; warn on dirty plugin tree at session start

push-and-rezip step 8 used to stage a fixed list (zip, archive, plugin.json, LOG/), which didn't include whatever the pre-push Pass-B sweep modified in plugin/si-plugin/. Sweep edits — prose tightening to keep templates and skill docs aligned with the procedure changes being pushed — fell out of the commit and sat orphaned in the working tree across sessions. The next /next would then layer unrelated build edits on top, mixing concerns into one commit. Two complementary edits to this project's CLAUDE.md close both halves: at push, step 8 now stages every dirty path under plugin/si-plugin/ via `git status --porcelain plugin/si-plugin/` (alongside the zip, archive, plugin.json, and LOG/), so sweep edits are caught automatically going forward; at session start, a new dirty-tree check runs the same porcelain command when no _build.md is present and warns Alex if non-empty, surfacing any orphans from prior pushes before a new build layers on top. Both edits land in CLAUDE.md rather than the shipped plugin because the push-and-rezip workflow is self-hosting infrastructure, not consumer behaviour.

**Files touched:**
- CLAUDE.md: push-and-rezip step 8 stage list replaced with `git status --porcelain plugin/si-plugin/`-driven staging; new "Session-start dirty-tree check" section added between Working conventions and Push-and-rezip.

**Routed to Captures:** none

## 215f431 — Sweep "Questions resolved" leftover from done.md Plan close-out Step 1 Recap

done.md's Plan close-out Step 1 Recap still listed "Questions resolved" as one of the bullet types to populate — a leftover from when OPEN-QUESTIONS existed as a tracked concept and got promoted out during the V47 era. The field name outlived the concept, and stale recap field names train Claude to fabricate content to fill them (a recap with "Questions resolved" as a named bullet pressures the next /done to produce something for that slot even when no questions were resolved, because empty named fields read as omissions rather than as inapplicable). The bullet got dropped. The batch was authored as a sweep rather than a single-bullet edit because drift checks also got removed in the V47-era cleanup and other recap or close-out fields could be carrying the same shape of staleness — but the sweep walked Plan close-out Steps 1–4 plus the LOG-entry template and every remaining field maps to a current concept (Batches, Captures, Spec changes, Queue changes, Parked, unpark watch), so the build collapsed to the one bullet removal.

**Files touched:**
- plugin/si-plugin/docs/done.md: Plan close-out Step 1 Recap — removed the "Questions resolved" bullet.

**Routed to Captures:** none

## 8c2e2fc — done.md recommend-next: overlap scan, continuation ask, reorder offer

done.md's two recommend-next sections (Build close-out Phase 3, Plan close-out Step 4) were collapsing to "Run /next when ready" whenever batches existed, regardless of whether unprocessed captures in the queue contradicted, invalidated, or would benefit the top batch. That shape deferred sequencing to the user — exactly the case Dependency ownership says Claude should own. Three additions tighten the close-out symmetrically across both modes: (1) an upfront overlap scan of unprocessed Captures against the top batch, mirroring next.md Step 1.4's blocker-gate, with /plan recommended if anything hits; (2) when the recommendation lands on /next, an explicit continuation ask, since back-to-back /next runs are the common pattern and the close-out is the right moment to surface it; (3) when continuing and a reorder applies, an offer to reorder the queue first so the next /next picks the right item — leaning on the general reorder-offering rule already in plugin-behaviour.md.

**Files touched:**
- plugin/si-plugin/docs/done.md: Build close-out Phase 3 prepended with overlap-scan paragraph, "More batches" branch rewritten to name the batch then ask about continuation with conditional reorder offer. Plan close-out Step 4 got the same shape — overlap scan up front, "Batches exist" branch with continuation ask and conditional reorder offer.

**Routed to Captures:** none

## 620c1b0 — Fold push offer into commit step; delete standalone Push and context phase

done.md's Build close-out Phase 4 and Plan close-out Step 5 were both routinely skipped — by the time Phase 3 / Step 4 delivered the recap-plus-recommendation, the procedure read as finished and the trailing push prompt fell off the end. Hardening the sequencing wouldn't fix the false ending; the fix is to move the push offer earlier, into the commit step where the user is already deciding what happens to the work. The commit step now asks "Commit and push, or just commit?" in the same approval moment as the commit message, so push is never gated on guessing user intent — they always get to choose, and the choice lives where it's a natural part of the close. Phase 4 and Step 5 then delete entirely, and Phase 3 / Step 4 become the genuine close (no tail sentence priming the user to wait for "what's next"). The two `/clear` reminders sitting in the deleted sections disappear as a side effect — that nudge belongs to the broader sweep-clear-compact batch, but this build removes two of its sites for free.

**Files touched:**
- plugin/si-plugin/docs/done.md: Phase 2.4 renamed "Git commit and push", sub-step 3 rewritten to fold the commit+push choice into the message approval, sub-step 4 executes the choice. Phase 3 tail sentence about Phase 4 dropped. Phase 4 deleted. Plan close-out Step 3 got the same rename + rewrite. Plan close-out Step 4 tail sentence about Step 5 dropped. Plan close-out Step 5 deleted.

**Routed to Captures:** none

## 6c32bba — Reconcile queue placement, add unpark/staleness watches and ordering narration, introduce batch slugs and dependency headers

plugin-behaviour.md was internally inconsistent: "Captures append to the bottom" and "Claude owns sequencing — ordering, dependencies, what happens first" contradicted each other. Mechanical FIFO left no room for the ordering judgment the other rule said Claude owned, and the same gap applied to batches. The reconciliation makes placement Claude-directed where applicable (revision-of, depends-on, belongs-next-to) with oldest-first as the explicit fallback; Parked stays append-only because parked items aren't processed in order, so ordering judgment is moot. Dependency ownership then expanded from a placement-time check into ongoing curation — Unpark watch (flag parked items newly unblocked) and Staleness watch (flag items the surrounding code or rules have moved past) — both surfacing at the natural read-state moments (/plan Step 1, /next Step 1.4, /done close-outs). The third ownership rule is narration: any time ordering judgment is exercised — non-default placement, reorder, unpark, staleness flag, even the explicit "appending here because no dependency applies" case — the reasoning gets named briefly at the moment of judgment, because silent ownership reads as no ownership. The artifact-level expression of the same ownership is `Depends on:` / `Blocks:` headers under each batch title (omit either when empty rather than writing `none`), paired with stable kebab-case slugs as `**[slug]**` markers on the title line — immutable, grep-able, reorder-safe. The three pieces (annotation, narration, watches) cover the same ownership at artifact, action, and ongoing-curation levels. The backfill pass walked the existing 14 batches and the one parked item, assigned slugs, populated headers from dependencies already named inline in rationales (push-in-commit blocks recommend-next-overlap and sweep-clear-compact; fix-clear-before-done blocks sweep-clear-compact; install-guide blocks e2e-install-guide), and rewrote two prose references to use slugs so the new rule applies retroactively rather than only to future batches.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: Captures placement rewritten; Dependency ownership gained five sub-rules (Unpark watch, Staleness watch, Narrate the ordering work, Depends on/Blocks headers, Stable batch slugs).
- plugin/si-plugin/docs/plan.md: Step 1 gains unpark + staleness scans before the entry question; Step 3 ordering bullet aligned to dependency-then-fallback with narration; Step 3 batch authoring template adds slug marker and Depends on/Blocks header lines.
- plugin/si-plugin/docs/next.md: Step 1.4 blocker gate adds unpark-candidate and stale-batch scans; Step 4 routing references the placement rule.
- plugin/si-plugin/docs/done.md: Phase 1.3 routing references the placement rule; Phase 2.2 staleness sweep broadened from "what this build changed" to any staleness from any cause plus a same-pass unpark sweep; Phase 3 Recommend next and Plan close-out Step 4 Recommend next now surface unpark candidates.
- QUEUE.md: assigned slugs to all 14 current batches and the parked sizing-gates-rework; populated Depends on/Blocks headers where dependencies exist; rewrote two prose references to use slugs.

**Routed to Captures:** none

## ac461c4 — Add reorder-offering rule to plugin-behaviour.md Dependency ownership

Dependency ownership already named Claude as the owner of sequencing, but the rule stopped at ownership without naming the action it requires. In practice that left a gap where Claude could spot an ordering issue, narrate the dependency, and stop — ownership in name only. The added bullet closes the gap: when an ordering issue is spotted (a capture or batch belongs elsewhere based on dependencies), the obligation is to offer to reorder the queue, not just name the dependency verbally. Captures and batches both have order — a capture moved up changes /plan's processing order, a batch moved up changes /next's pick order — and both are valid reorders for Claude to offer. The rule lives in plugin-behaviour.md so /plan and /done both inherit it without restating; /next routes reorder intent back to /plan per Step 5.1.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: added one bullet to Dependency ownership covering the offer-to-reorder obligation and that captures and batches are both valid reorder targets.

**Routed to Captures:** none

## 2055d97 — Tighten Why-pipeline preserve and retrieve rules

plugin-behaviour.md's Why-pipeline section already preserved rationale as prose and pointed retrievals at LOG, but two gaps blunted the rules. Preserve named the abstract failure mode ("don't collapse into a structured why-field") without naming the concrete collapse-shapes a future doc or skill designer would actually reach for — one-line summaries, dedicated why-fields, typed taxonomies — so the same mistake stayed easy to remake. The expansion calls each shape out by name with the failure mode woven in as inline prose: a one-line summary truncates the reasoning chain to a label; a dedicated why-field breaks the inline carry the pipeline depends on and trains empty-field habits; a typed taxonomy is never complete and forces nuance into the closest pre-defined slot. The rule modelling what it asks for — prose-with-why, not a labelled field — is itself part of the lesson. Retrieve previously pointed at log.md and log-v*.md as the first read, with index.md mentioned only as "the entry point"; the new shape makes index.md the actual first search since its one-line-per-entry summaries point to candidate entries faster and more accurately than scanning full prose, then full rationale opens from the matched entries. Prior decisions inherits the change through its existing cross-reference.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: Why-pipeline > Preserve expanded with three named collapse-shapes; Retrieve rewritten to route through LOG/index.md first.

**Routed to Captures:** none

## 6fd7fed — Add between-captures checkpoint to plan.md Step 2

plan.md Step 2 sequenced captures back-to-back with no checkpoint between them — the "anything else?" interview check sat *within* a capture but not *between* them, so any mid-sequence intent (wrap up, surface a new capture, close out before the end) forced the user to interrupt the presentation. The fix adds sub-step 5 as a Checkpoint after each capture is routed: three uniform-phrased options every time — continue to the next capture, close out (jump to Step 4), or share something else (loop back into Step 2 with the new item). On the last capture, option 1 drops out naturally without needing different wording — the same pattern Step 1's entry question uses. Codifies behaviour Claude was already inferring this session.

**Files touched:**
- plugin/si-plugin/docs/plan.md: added Step 2 sub-step 5 (Checkpoint) with [PROMPT] tag.

**Routed to Captures:** none

## f15e8e8 — Scan for downstream revision before recommending promote on structural captures

/plan Step 2's Recommend step had no procedural check for downstream revision exposure before recommending a capture be promoted. The session that triggered this fix promoted an "affirmative batch-definition" capture as structural, then absorbed three queued captures later when the /audit capture pivoted to "audit as batch type" — the conflict was visible at original promote time but no step asked the question. The fix adds a downstream-impact scan to the Promote bullet, sitting alongside the concrete-outputs requirement from the adjacent batch. Trigger is rule shape rather than edit size: a capture installing a *structural* rule (defines what something is, frames how other captures get evaluated) gets the scan; a localized fix doesn't. When the scan surfaces a conflict, Claude flags it at recommend time, names the conflict, and offers three options — process the downstream capture first, hold this one, or proceed accepting the possible later revision. The two requirements compose: concrete-outputs forces the recommendation to be specific enough to be approved knowingly; the downstream-impact scan forces it to be specific enough to *check* against other captures.

**Files touched:**
- plugin/si-plugin/docs/plan.md: Step 2 sub-step 2 Promote bullet — appended a "Downstream-impact scan" clause keyed to structural-rule shape.

**Routed to Captures:** none

## 533fc85 — Require concrete work-product in /plan promote recommendations

/plan Step 2 sub-step 2 used to recommend promote/park/drop before the batch entry was drafted, which meant the user could approve "promote" without seeing what would actually get built. This session's promote bridged the gap by naming concrete outputs organically — but style isn't a guarantee, and a different model could recommend promote in abstract terms, leaving the user to approve blind. The fix is structural: the Promote bullet now requires the recommendation to describe what would actually get built in user-recognizable work-product terms (which files, what subsection or rule, what gets added/removed/rewritten — not just the topic or intent). Paired with a forcing-function clause that closes the recursive case — if sub-step 1's interview hasn't yielded enough to describe outputs concretely, the recommendation isn't ready, and Claude returns to interviewing rather than recommending. Park and Drop bullets unchanged. The lead-in's "Recommend one disposition" phrasing was deliberately left alone — the queued "disposition" jargon sweep is the right place for it, and folding the change in here would have polluted this batch's commit and LOG entry.

**Files touched:**
- plugin/si-plugin/docs/plan.md: Step 2 sub-step 2 Promote bullet — expanded with work-product description requirement and return-to-interviewing forcing function.

**Routed to Captures:** none

## ee15451 — Audit becomes a third batch type with its own /next procedure

Audit work — systematic reviews of procedure docs for repetition, drift, prose-where-tag-belongs, and similar concerns — had been stuck in Captures for 6-7 /plan rounds because /plan's dialogic capture-by-capture flow doesn't fit the read-many-propose-many shape audits actually have, and new incoming captures kept crowding them out. The earlier framing was a separate /audit skill, but that added a skill name the user would have to learn when the choice is mechanical (the queue says which procedure to run). The cleaner shape lands here: audit becomes a third batch type alongside build and test, /next branches on batch type after pre-flight the same way /done branches on stage, and the new Audit procedure section walks Claude through lock-scope → systematic read against criteria → compile findings → present one at a time for capture/drop → route approvals to Captures → close without source-file edits. The planning-discipline catch that motivated the original "no thinking work as a batch" rule is preserved: audit batches don't edit files directly, so their output still flows through Captures where /plan can convert findings into normal build batches with the usual dialogue. plan.md gets two paired changes in Ground rules — an affirmative three-type rule ("Batches are build, test, or audit work, in any combination. Nothing else.") sitting alongside the softened negative rule that now scopes itself to *build* batches and names audit work as the exception — plus an Audit subheading in the Step 3 batch template (Target / Criteria) and a dedicated sizing gate that asks whether the target and criteria are specific enough to write the audit prompt without further dialogue. The two parked audit captures (trickle-up audit, output-tag overhaul audit) plus the in-scope/out-of-scope distinction audit are now candidates for /plan to convert into audit batches.

**Files touched:**
- plugin/si-plugin/docs/plan.md: Ground rules — added affirmative three-type rule; softened thinking-work rule to scope to *build* batches with audit as named exception. Step 3 — added Audit subheading (Target / Criteria) to batch template; updated the post-template sentence to "Build, Test, and/or Audit subheadings"; added Audit batch sizing gate after the Readiness gate.
- plugin/si-plugin/docs/next.md: Step 1.5 — entry counts updated to "(build / test / audit)". Step 1.6 — new batch-type branch (Build/Test continue to Step 2; Audit jumps to the new section). New "Audit procedure" section between Step 7 and Rules, with six sub-steps covering lock-scope, systematic read against criteria, finding compilation, [SEQUENCE, PROMPT] one-at-a-time disposition, fenced-block capture drafts, and close without source edits.

**Routed to Captures:** none

## 4c9ee70 — Define index-entry shape and reframe sizing as a single readiness gate

LOG/index.md is Claude-facing — it exists so a why-pipeline retrieve can decide which entry to open without reading every entry's full prose. The old "~one line" framing in the LOG conventions was a proxy for human scannability that didn't match how the index is actually used. The new rule in plugin-behaviour.md states what an index entry must contain — artifact touched and the nature of the change, with enough substance to make the open/skip call — and explicitly drops any absolute length cap. Length follows from the content requirement: usually one line, sometimes two for multi-thread sessions. The same definition does double duty as the batch readiness gate in plan.md: if you can't write the candidate index entry yet, the batch isn't specific enough — keep interviewing. That collapses Step 3's two sizing gates (specificity bullet + 5-test verification-burden rule) into one. /next now pre-generates the candidate at lock-scope time and stores it in _build.md alongside the batch entry, so /done can reuse it verbatim when the build ran as planned and re-author against the same rule when scope shifted. The 5-test rule and its echo in next.md's sizing-principle paragraph are both gone — sizing now keys to coherence, not test count.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: added "Index entries" section after Why-pipeline; Why-pipeline > Retrieve cross-references it
- plugin/si-plugin/docs/plan.md: Step 3 sizing gates rewritten as single readiness gate, verification-burden bullet dropped
- plugin/si-plugin/docs/next.md: Step 2 sub-step 1 added (pre-generate candidate index entry); _build.md template gained `Index entry candidate:` line; Step 4 sizing-principle paragraph dropped
- plugin/si-plugin/docs/done.md: Build close-out 2.1 + Plan close-out 2 — index line references Index entries rule; Build close-out 2.1 reuses _build.md's pre-generated candidate when scope matches

**Routed to Captures:** none

## a0c6a63 — Standardise approval-time outputs as fenced blocks across procedure docs

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
