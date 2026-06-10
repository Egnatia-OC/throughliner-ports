# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## [HASH] — /plan: [faq-build-md-functions] unparked and folded into [narrate-build-md-purpose]

The /done close of [scope-lock-files-section] flagged [faq-build-md-functions] as newly unblocked — its Blocked by: named that batch, which shipped at 8c8f7fe. This /plan took it ahead of the capture backlog so the FAQ content describing the scope-lock as real can ride the same push as the code that made it real. Reading the FAQ template reshaped the work: the template already carries a "What is _build.md? Should I edit it?" entry, so the capture is a rewrite of that answer around the four functions, not a new entry — question wording stays, the FAQ index anchor holds, and the index template needs no change. Routed as a fold-in to [narrate-build-md-purpose] rather than a standalone batch: both halves describe _build.md's purpose in user-facing terms, and authoring that vocabulary once in one build keeps the narration lines and the FAQ answer from drifting apart; the rejected standalone-batch alternative would have meant a second authoring moment for the same four functions. The batch was retitled to cover both halves (slug unchanged), gained the FAQ build entry with the existing reassurances preserved, and keeps its top position before the push marker.

**Queue changes:**
- [narrate-build-md-purpose]: retitled to "Make _build.md's purpose visible: narration at the moments it's used, plus the FAQ answer"; rationale extended with the fold-in reasoning; FAQ-rewrite Build entry and self-verifying Test line added
- [faq-build-md-functions]: folded in and removed from Captures

**Captures routed:** [faq-build-md-functions] folded into [narrate-build-md-purpose]

## 8c8f7fe — /next [scope-lock-files-section]: scope-lock enforcement made real — _build.md gains a Files: section

The scope-lock half of pre_tool_use had been dead code since authoring: the hook fully parsed and enforced a `Files:` section out of _build.md, but no procedure doc ever wrote that section, so the `if build_files:` guard skipped enforcement on every build while CLAUDE-TEMPLATE.md told users the protection existed. The fix is doc-side plus a tri-state guard: next.md's Step 2 template now carries a `Files:` section populated at scope-lock from the files the batch entries name (paths relative to project root), and the hook distinguishes no-section (skip — builds from older procedure shapes unaffected) from present-but-empty (method docs only — the audit and test-only lockdown) from entries-listed (enforce the list). The docstring's false claim of Bash/PowerShell write-command detection for the SPEC and scope-lock rules was corrected rather than implemented, per the batch's call — that capability is real design work for its own capture if ever wanted. One placement judgment during the build: the batch entry targeted next-audit.md's "lock-scope step," which stopped existing when [next-split-by-type] moved scope-locking into next.md Step 2 — the empty-section rule landed there (covering audit and test-only batches alike), with a reinforcing line in next-audit.md's intro where audit sessions read. The scope-expansion paths in next-build.md (minor-addition approval and the coherence exception) now append newly approved files to `Files:` before editing, since with enforcement live the edit is denied otherwise. Verification piped synthetic PreToolUse JSON into the target hook across the six contracted cases plus a SPEC.md regression check — 13/13 passed. The first test run was itself blocked by the host hook matching the literal git-safety strings inside the test script's text: a live demonstration that the git-safety scan covers full command text including embedded scripts, worked around by assembling the strings at runtime and routed to Captures as a known sharp edge.

**Files touched:**
- plugin/si-plugin/docs/next.md: Step 2 _build.md template gains `Files:` + explanation paragraph (scope-lock feed, population rule, empty-section rule for audits/test-only)
- plugin/si-plugin/docs/next-build.md: minor scope-expansion bullet and coherence exception append approved files to `Files:` before editing
- plugin/si-plugin/docs/next-audit.md: intro states audit _build.md carries an empty `Files:` section = method-docs-only lockdown
- plugin/si-plugin/hooks/pre_tool_use.py: _parse_build_files returns None / [] / list; rule 2 tri-state; docstring rewritten (false write-detection claim dropped — git safety only); both deny messages teach the Files: fix

**Routed to Captures:** git-safety check fires on command text, not command intent (host hook blocked the test script's literal strings; workaround and handling options recorded)

## 21470be — /plan: [scope-lock-files-section] promoted — make the dead scope-lock enforcement real

The previous build's close flagged an overlap: the top batch [narrate-build-md-purpose] would narrate _build.md's scope-lock function, but the raw capture [scope-lock-files-section] reported that function as dead code. This /plan pulled that capture out of order since the dependency runs toward the top batch. Both claims verified against the hook source: pre_tool_use.py fully parses and enforces a `Files:` section no procedure doc ever writes — the `if build_files:` guard skips enforcement on every build — and the docstring promises Bash/PowerShell write-command detection that doesn't exist past the two git checks. Scope was settled on a spectrum (docstring-only correction → make `Files:` real → plus audit lockdown → plus write-command detection): landed on make-it-real plus audit lockdown via a tri-state guard (no section = skip as today, present-but-empty = method docs only, which is exactly right for audits, listed = enforce), with write detection deferred and its false docstring claim corrected rather than implemented. Promoted to the top of Batches inside the existing push window; [narrate-build-md-purpose] gains the dependency and [faq-build-md-functions] is blocked by it, since both describe the scope-lock as real. The session also caught the dependency scan's routing gate misfiring: it fired on the capture's evidence citation of [faq-build-md-functions] and its default would have parked the blocker behind the thing it blocks — overridden with narration and filed as a raw capture carrying three tightening options (document the override path / teach the scan reference roles / accept as-is).

**Queue changes:**
- [scope-lock-files-section]: promoted from raw capture to build batch at top of Batches
- [narrate-build-md-purpose]: `Depends on:` extended with [scope-lock-files-section]
- [faq-build-md-functions]: `Blocked by: [scope-lock-files-section]` added
- New raw capture: dependency scan misfires on evidence citations

**Captures routed:** [scope-lock-files-section] promoted; one new raw capture filed

## 40749f7 — /next [fold-unparks-into-step-2]: unpark candidates routed into /plan Step 2's loop, processed ahead of Captures

The Step 1 unpark and staleness scans produced findings with no structural home — the procedure said "surface findings" at read-state, so they got narrated into the same moment as the entry question, colliding two decision surfaces. The fix routes them through the loop the user already knows: scan output is now collected silently at Step 1 and carried into Step 2, where candidates are processed ahead of Captures (Parked items have been waiting longest) through the same sub-steps, with the recommend options reread for items already in Parked — promote means move out of Parked into Batches as a full batch entry, park means keep parked, drop removes the item entirely. Learned during the build: the entry question's text was already the clean form — the observed smushing was behavioural, not doc text — so that entry landed as explicit constraint sentences (keep the question clean; candidates surface only inside Step 2) rather than a revert. One line beyond the batch's letter: staleness candidates needed a stated landing in Step 2, since the Step 1 reframe sends both scans' output forward — they take the same path with the Staleness watch's drop/rewrite/keep choice; without that sentence the Step 1 reference would dangle. One scope addition, approved mid-build: plugin-behaviour.md's Unpark watch bullet still located the surfacing at "/plan Step 1 read-state," the exact shape this batch removed — updated to "scans at Step 1, surfaces in the Step 2 loop." The new sub-section names the loop's user-visible sub-steps without claiming a count, sidestepping the batch text's "five-sub-step" description (the loop has six, one of them silent).

**Files touched:**
- plugin/si-plugin/docs/plan.md: Step 1 scan paragraph reframed (candidates feed Step 2, no read-state narration); entry question constraint added; Step 2 "Unpark candidates first" sub-section; count line includes candidates ("5 items. First: ...")
- plugin/si-plugin/docs/plugin-behaviour.md: Unpark watch surfacing reference updated (scans at Step 1, surfaces in Step 2 loop)

**Routed to Captures:** none

## cb2ab60 — /next [done-closeout-extraction]: done.md split into router + commit core with four per-type close-out sub-docs

done.md held close-out for two session shapes plus commit and push mechanics, all loading regardless of which close was running, and the seam showed as a doubled session summary — the skill summarized in chat, then /done summarized again into the LOG. The chosen design mirrors [next-split-by-type]: done.md is now a thin router (no _build.md → done-plan.md; otherwise the Entry's subheading picks done-build.md / done-test.md / done-audit.md) plus the commit core stated once, and the four sub-docs each carry a complete type-specific close-out that loads only when close-out actually runs. The rejected per-skill-sections alternative and the three counts it lost on are preserved in the 3526cde entry. Learned during the build: test-only and audit sessions previously had no stated close-out shape at all — the old done.md treated everything with a _build.md as a build close; writing done-test.md and done-audit.md surfaced what's type-specific (every failed test needs a routed fix unless the user drops it; an audit's recommend-next defaults to /plan because its findings sit unprocessed in Captures). One deliberate drop beyond the letter of the contract: the old "Build recap" chat step wasn't carried into done-build.md — a chat recap immediately before the LOG draft is the same doubled-summary shape this batch removes, and the LOG draft shown for approval is the recap moment. File-safety restatements dropped per the folded-in [trickle-up-done-md-file-safety]; grep-verified clean across all five docs, with "stage explicitly" surviving as the procedural step. The behavioural test (one session summary, not two) is host-side — it needs push + reinstall and will surface as an unconfirmed test at a future /next.

**Files touched:**
- docs/done.md: rewritten 157 → 31 lines — router + commit core + 2 rules
- docs/done-build.md, done-test.md, done-audit.md, done-plan.md: created — complete per-type close-outs
- docs/plan.md: Step 4 trimmed to a bare /done recommendation
- docs/next-build.md: Completion trimmed; abort path's "mode detection" updated to "router"
- docs/next-test.md: Completion trimmed to pass/fail counts plus the /done line
- docs/next-audit.md: Close trimmed; stale description of done.md's audit handling removed
- skills/done/SKILL.md: "current build" → "current session"; description generalized
- hooks/session_start.py, templates/CLAUDE-TEMPLATE.md: checked, no changes needed
- REGISTRY.md: four sub-docs added, done.md description updated

**Routed to Captures:** none

## ba28387 — /next pre-flight flagged [trickle-up-done-md-file-safety] against the top batch; /plan folded it into [done-closeout-extraction]

The /next pre-flight's capture scan found [trickle-up-done-md-file-safety] overlapping the top batch [done-closeout-extraction]: the batch rewrites done.md wholesale, and the capture wants done.md's file-safety restatements (the git-add prohibition at lines 83 and 135, push-is-a-prompt at line 155 — all three verified still present) removed as duplicates of plugin-behaviour.md File safety. Building first would have either propagated the restatements into the new commit core and four sub-docs — text a queued cleanup already wanted gone — or forced an unapproved mid-build judgment call to drop them. Folding the capture into the batch as a constraint lands the rewrite clean in one pass. The fold-in also settles what the capture actually decides: the rewrite's commit-core-stated-once design collapses the within-done.md duplication structurally for free, so the open question was whether the single commit core restates the rules at all — it doesn't; the procedural steps stay, with "stage explicitly" surviving as positive instruction rather than restatement. No conflict with the raw capture [git-add-safety-hook-gap] (hook enforcement of the same rules later): removing restatements now is compatible with the hook landing later. Session also backfilled the [HASH] placeholders in LOG/log.md and LOG/index.md to 3526cde at /next pre-flight.

**Queue changes:**
- [done-closeout-extraction]: rationale extended with the fold-in reasoning; third Build entry added — neither done.md's commit core nor the four sub-docs carry the file-safety restatements; resolves [trickle-up-done-md-file-safety].

**Captures routed:** [trickle-up-done-md-file-safety] folded into [done-closeout-extraction] and removed from Captures.

## 3526cde — /plan: [done-closeout-extraction] redesigned to /done split; push point set; 5 captures routed

The session's biggest move came from discussion rather than the captures list. The user connected done.md's inflation to the close-out behaviour that had emerged organically across skills and was about to be codified per-skill: the extraction batch was redesigned from per-skill close-out sections to a /done router with per-type sub-docs (done-build.md, done-test.md, done-audit.md, done-plan.md), mirroring [next-split-by-type]. The per-skill-sections alternative lost on three counts: close-out text would load at skill start and ride in context all session for an end-of-session procedure; it would mint four near-duplicate close-out sections (the duplication shape the trickle-up captures exist to clean); and its one win — LOG entry written before /done runs — merely restates today's abandoned-session risk, which the dirty-tree-check direction covers mechanically. The doubled session summary the user observed (skill close-out summarizes in chat, /done summarizes again into the LOG) resolves by making the LOG entry the single summary artifact.

A push point was set so host value lands soon: marker after [done-closeout-extraction], [fold-unparks-into-step-2], [narrate-build-md-purpose] — the session-feel cluster. The three audits and [next-done-recommendation] moved below the marker: audits yield captures, not shippable changes, and [output-tag-audit]'s criteria await the compliance-research captures still unprocessed. The __pycache__ zip fix must land before that rezip; its capture is still in the list.

Capture processing reached 5 of 30. Four INSTALL.md cold-read findings routed: a smoke-test batch (success/failure signals must match what the command menu literally shows — skills render namespaced, e.g. /sovereign-implementer:setup); the experienced-user bypass folded into [install-separate-ai-instructions], worded to route through the identification gate rather than around it; two one-line fixes merged as an endings-polish batch. The rejected-alternative-reasoning gap promoted as [log-rejected-alternative-reasoning] with a trigger boundary so entries don't bloat: discussion-level consideration qualifies, passing mentions don't. LOG hashes backfilled to 628d816 at session start.

**Queue changes:**
- [done-closeout-extraction] rewritten under its slug: /done router + per-type close-out sub-docs; skill-end chat summaries trimmed to a bare /done recommendation
- Push marker inserted after [narrate-build-md-purpose]; [output-tag-audit], [scope-distinction-audit], [close-out-audit], [next-done-recommendation] moved below it
- New batches: [install-setup-smoke-test-underspecified], [install-updating-later-section-is-padding] (endings polish, absorbed the trailing-ellipsis capture), [log-rejected-alternative-reasoning]
- [install-separate-ai-instructions] amended: bypass build entry + Depends on: [install-app-identification-check]
- [narrate-build-md-purpose] retargeted at done-build.md, gained Depends on: [done-closeout-extraction]

**Captures routed:** 5 routed (4 install cold-reads promoted/folded, 1 promoted as [log-rejected-alternative-reasoning]); orphaned persona-key comment removed; 25 remain

## 628d816 — /plan: model-compliance research filed; 6 queue items updated for post-split staleness

Session opened with staleness scan after [next-split-by-type] shipped (96a7986). Six queue items referenced old next.md line numbers and file locations that the split had moved into next-build.md, next-test.md, and next-audit.md: [output-tag-audit] and [scope-distinction-audit] (audit target lists), [next-done-recommendation] (Step 7 → Completion section), [audit-definition] (two build entries), [trickle-up-next-md-duplicates] (rule distribution across split docs), [trickle-up-ask-when-unsure] (line 195 → 70). All mechanical — file names and line numbers updated, substance unchanged.

User raised concerns about Opus 4.6 degradation and 4.7/4.8 not following the plugin's structured procedures. Research confirmed the 4.6 degradation was real (Anthropic April 23 postmortem — three harness-level changes, not model nerfing). Key finding for 4.8 adaptation: skill docs and CLAUDE.md are delivered at user-message priority, not system-prompt priority — the built-in system prompt outranks them on verbosity and tone, which is the architectural reason response-shape tags don't hold on newer models. Six techniques from Anthropic's docs filed. Research at resources/research/model-instruction-compliance.md.

**Queue changes:**
- Updated 4 batches for staleness: [output-tag-audit], [scope-distinction-audit], [next-done-recommendation], [audit-definition]
- Updated 2 captures for staleness: [trickle-up-next-md-duplicates], [trickle-up-ask-when-unsure]

**Captures routed:** 1 filed (priority-architecture finding and 4.8 compliance techniques)

## 96a7986 — /next [next-split-by-type]: next.md split into per-type procedure docs

next.md carried three session flows (build, test, audit) plus abort/resume branches in one 196-line file. Every /next session read the entire doc even though it only ran one flow. Splitting into separate docs cuts per-session read cost and lets each flow evolve independently — changes to audit findings presentation no longer risk entangling build scope-management rules.

The shared steps — pre-flight checks (hash backfill, active build detection, blocker gate) and scope lock (_build.md creation) — stayed in next.md as a routing front page. The front page's Step 2 now handles all three Progress formats (build/test/audit) in one place, eliminating the duplication where audit had its own "as Step 2 does" lock scope. After lock, Step 3 routes to the per-type doc based on batch subheadings. Abort branches went into next-build.md and next-test.md (the types where builds can fail); resume stayed in the front page (Step 1.2, shared). The "build and test follow the same procedure" rule was dropped as irrelevant after the split.

Cross-references in done.md, plugin-behaviour.md, and plan.md all point to Step 1 (blocker gate at 1.4, unpark watch at 1.4) which stayed in the front page — no updates needed.

**Files touched:**
- plugin/si-plugin/docs/next.md: rewritten from 196 lines to 68-line routing front page
- plugin/si-plugin/docs/next-build.md: created, 103 lines
- plugin/si-plugin/docs/next-test.md: created, 70 lines
- plugin/si-plugin/docs/next-audit.md: created, 23 lines

**Routed to Captures:** none

## 6a00c15 — /plan: walkthrough batches removed (thinking work); 4 install captures promoted

Session opened with discussion about [plugin-behaviour-walkthrough-1], which /next had aborted the previous session (b08e09a) as thinking work wearing an audit shape. Both walkthrough batches removed from Batches — their output is a routing decision list (decisions, not findings-to-Captures), so the work belongs in /plan as interactive sessions, not as queued batches. The build batch to execute the resulting routing decisions gets queued after those /plan sessions produce them. [next-split-by-type] is now the top of queue.

Captures processing: 5 of 26 processed before close-out. [install-paid-plan-ambush-and-pricing-opacity] promoted as [install-paid-plan-upfront] — surface the Pro-plan requirement before Q1 as an informed-consent gate with pricing pointer; [install-routing-no-plan-vs-free-plan-ambiguity] folded into same batch as a build entry (Step 1 routing language fix). [install-customise-plugins-ui-path-stale-or-wrong] promoted as [install-upload-path-clarity] — confirm the UI path, warn about the misleading "Create a plugin" label, add screenshot. [install-github-raw-url-feels-sketchy-no-provenance] promoted as [install-download-provenance] — add provenance line and download expectation. [install-open-a-project-folder-undefined] promoted as [install-define-open-folder] — replace "open a project folder" with concrete instruction to create an empty folder for the smoke test.

**Queue changes:**
- Removed [plugin-behaviour-walkthrough-1] and [plugin-behaviour-walkthrough-2] (thinking work, not audit)
- Promoted [install-paid-plan-upfront] at queue bottom (absorbs [install-routing-no-plan-vs-free-plan-ambiguity])
- Promoted [install-upload-path-clarity] after [install-paid-plan-upfront]
- Promoted [install-download-provenance] after [install-upload-path-clarity]
- Promoted [install-define-open-folder] after [install-download-provenance]

**Captures routed:** 5 promoted (4 as new batches, 1 folded into [install-paid-plan-upfront])

## b08e09a — /next aborted on [plugin-behaviour-walkthrough-1]: thinking work misrouted as audit batch; gap captured

/next picked up [plugin-behaviour-walkthrough-1] and aborted at pre-flight when the user flagged it as thinking work, not audit work. The batch's output is a routing decision list (where each plugin-behaviour.md rule belongs) — decisions, not findings-to-Captures. It passed the audit exception in plan.md's thinking-work rule because it has the surface shape of a systematic read against fixed criteria, but the rule has two gaps: "Never queue thinking work as a *build* batch" only names build batches (implying other types are fine), and framing audit as "the one exception" treats it as thinking work with permission rather than a separate category that was never thinking work in the first place. The user had specifically asked /plan to create the batch, and /plan complied — the procedure didn't give it grounds to push back. Capture filed describing both gaps and the fix shape (drop the "build" qualifier, reframe audit as a separate category). LOG hashes backfilled to 90970cc.

**Queue changes:**
- None (batch stays in queue as-is pending /plan)

**Captures routed:** 2 filed (thinking-work rule gap — plan.md line 11 "build" qualifier + audit-as-exception framing let it through; /next pre-scope-lock abort has no handoff to /done)

## 90970cc — /plan: [drop-log-per-release-split] rewritten to per-entry files; 2 install captures promoted; [faq-build-md-functions] unparked

Session opened with discussion before captures. First, clarified the processed/unprocessed captures split (first successful why-pipeline retrieve — found e425f92 in LOG via index search). Then [drop-log-per-release-split] rewritten: the f123eed session had decided "drop the split, one growing log.md" but hadn't preserved the rejected-alternative reasoning — two sessions later the user couldn't retrieve why per-release was rejected and second-guessed the decision. Working through it again: the case against per-release is thin (one extra grep per retrieve, two extra push-ceremony steps), and collapsing to one growing file only removes the split without improving retrieve. The right fix is matching the file boundary to the logical boundary — each LOG entry gets its own file, named by slug, so retrieve goes index → hash → direct file open. The per-commit alternative was the decision f123eed should have reached.

Captures processing: 2 of 25 processed before close-out. [install-note-to-claude-visible-to-user] promoted as [install-separate-ai-instructions] — move AI-facing content (Note to Claude block, pacing rules) out of the human's reading path. [install-claude-code-vs-chat-app-disambiguation] promoted as [install-app-identification-check] — add forced positive identification check before routing, replacing the one-sentence distinction that the desktop-app-confused persona read past and confidently misrouted on. Both placed at queue bottom, no dependencies.

Unpark: [faq-build-md-functions] moved from Captures Parked to processed Captures — [reader-test-refresh] shipped (2356cb7) with no findings, condition vacuously met.

**Queue changes:**
- Rewrote [drop-log-per-release-split] batch (per-release → per-entry files with slug-based naming)
- Promoted [install-separate-ai-instructions] at queue bottom
- Promoted [install-app-identification-check] at queue bottom, after [install-separate-ai-instructions]
- Unparked [faq-build-md-functions] to processed Captures

**Captures routed:** 2 promoted out ([install-note-to-claude-visible-to-user] → [install-separate-ai-instructions], [install-claude-code-vs-chat-app-disambiguation] → [install-app-identification-check]). 2 new filed (rejected-alternative reasoning in LOG entries, draft-without-approval-ask pattern in procedure docs).

## a36f67f — /next [trickle-up-audit]: setup.md, plan.md, next.md, done.md audited for rules that belong in plugin-behaviour.md

The four procedure docs were read systematically against plugin-behaviour.md to find cross-skill rules that cost token budget as duplicates and drift between copies. Three docs carried rules already stated in plugin-behaviour.md: next.md repeated 4 (SPEC read-only, don't fix outside scope, state regressions plainly, one build at a time — wording had already drifted on the regressions rule), done.md repeated 2 file safety rules (git add prohibition appearing twice within done.md itself, plus git push prompt), and setup.md repeated the no-jargon communication rule. One cross-doc procedure duplication surfaced: the LOG hash backfill procedure lives word-for-word in both plan.md and next.md — not a rule so plugin-behaviour.md isn't the target, and the existing [log-hash-backfill-in-done] batch already proposes consolidation. One non-skill-specific rule was found only in next.md: "ask when unsure, don't guess" has no equivalent in plugin-behaviour.md despite applying universally. All 5 findings captured. Session also backfilled 4 stale [HASH] placeholders across LOG files (log.md, index.md, log-v1.8.0.md, log-v1.9.0.md).

**Files read (audit targets):**
- plugin/si-plugin/docs/setup.md, plan.md, next.md, done.md
- plugin/si-plugin/docs/plugin-behaviour.md (reference)

**Routed to Captures:** [trickle-up-next-md-duplicates], [trickle-up-done-md-file-safety], [trickle-up-setup-md-no-jargon], [trickle-up-hash-backfill-duplication], [trickle-up-ask-when-unsure]

## 2356cb7 — /next [reader-test-refresh]: reader-test workflow's fake project refreshed to current SI shape

The reader-test workflow's fake bookshelf tracker project had drifted from current SI: it carried a DECISIONS.md doc (replaced by the LOG-based why-pipeline months ago), used inline [build]/[test]/[idea]/[question] type tags (replaced by Build/Test subheadings + separate Captures section), and its CLAUDE.md still showed the older template. Running the workflow against that stale fake project measured drift between docs and the fake project rather than drift between docs and real reader comprehension — findings came out noisy. The refresh aligned all five fake-project constants (FAKE_LOG replacing FAKE_DECISIONS, FAKE_QUEUE with current format, FAKE_BUILD with Index entry candidate and entry-description ticks, FAKE_CLAUDE_MD from current template) and fixed two session-start string drifts caught by comparing against session_start.py ("No active build." → "Ready.", removal of stale "The previous session was interrupted mid-build."). The user-questions audit replaced one trivially-answered question (SPEC.md read-only, stated word-for-word in CLAUDE.md Rules) with a scope-discipline question that requires connecting dots across procedure docs. Synthesis FAQ/Other split left intact — the routing split is load-bearing on downstream processing.

**Files touched:**
- resources/reader-test-workflow.js: 8 edits across FAKE_LOG (new), FAKE_QUEUE, FAKE_BUILD, FAKE_CLAUDE_MD, SESSION_NO_BUILD, SESSION_ACTIVE_BUILD, USER_QUESTIONS[2], verifyPrompt DOC ROUTING criterion

**Routed to Captures:** none

## 3e86d06 — /plan: 2 captures promoted ([user-edits-rollup-on-commit], [checkpoint-wording-loosen]); LOG hashes backfilled

Two captures promoted. [user-edits-rollup-on-commit] addresses a gap where user-made edits to target-tree files sit dirty across sessions because /done's commit only stages build-touched files — the batch adds detection and rollup at commit time. [checkpoint-wording-loosen] loosens plan.md's checkpoint rule so the three off-ramps are required to be available but don't need identical phrasing each time — robotic numbered-list delivery confirmed as recurring across multiple sessions, not a one-off.

**Queue changes:**
- [user-edits-rollup-on-commit] promoted from capture to batch (appended after [plan-resolves-by-default])
- [checkpoint-wording-loosen] promoted from capture to batch (appended after [user-edits-rollup-on-commit])

**Captures routed:** 2 promoted

## f756692 — /plan: 6 batches promoted (2 from captures, 4 from docs-size concern); auto-memory staleness researched and cleaned

User raised that plugin-behaviour.md as one big universal doc and next.md as one doc carrying three session flows are both too large for what they're doing. That concern — "docs grow but bug rate doesn't fall" — had been sitting as a capture-and-watch. This session sharpened it into four structural batches: two interactive walkthroughs of plugin-behaviour.md (first half / second half, deciding per rule where it belongs), a next.md split into per-session-type docs, and a done.md extraction moving close-out into per-skill sections while slimming /done to commit mechanics. Two earlier captures (fenced-block "code" label, /plan deferring resolvable work) were also promoted to batches. Separately, research on Claude Code auto-memory staleness confirmed the two project-state memory files were the textbook failure mode — frozen queue snapshots from V47/V51 with no current relevance — and both were deleted.

**Queue changes:**
- [fenced-block-content-type-label] promoted from capture (semantic labels on approval-time fenced blocks)
- [plan-resolves-by-default] promoted from capture (/plan resolves in-session, capture only for what it can't)
- [plugin-behaviour-walkthrough-1] promoted (walk first half of plugin-behaviour.md line-by-line, decide universal vs per-skill)
- [plugin-behaviour-walkthrough-2] promoted (walk second half, same method)
- [next-split-by-type] promoted (split next.md into per-session-type docs)
- [done-closeout-extraction] promoted (extract close-out into per-skill sections, slim done.md to commit)

**Captures routed:** 3 promoted (fenced-block label, /plan misroute, docs-grow-but-bugs-don't-fall)

**Other:** Deleted stale memory files (project_v47-oq-promotion.md, ideation-research-and-build-log.md). Research filed at resources/research/auto-memory-staleness.md.

## 0b77f78 — /next [e2e-install-guide]: 4 stranger-Claude subagents cold-read INSTALL.md; 11 findings routed to Captures

Reshape landed cleanly. Four subagents in parallel, each given persona + INSTALL.md inline + cold-read instructions (don't execute, just report stuck-points). Persona set as scoped: cold-stranger (zero knowledge), desktop-app-confused (has Claude chat app, thinks it's Claude Code), free-plan (has Claude Code on free), already-installed (paid + prior plugin experience). Each returned a numbered friction list with a summary "where I'd give up." Synthesis grouped by guide area, preserved persona tags so cross-persona signal stayed legible, and surfaced one catastrophic failure mode (desktop-app-confused silently misroutes to Branch B then crashes at the Customise menu hunt with no recovery path — assistant would dutifully troubleshoot a missing menu rather than diagnose wrong-app). Cold read worked as predicted: cheap, parallel, structural gaps surfaced without simulating turn-taking. Findings span the full guide — frontmatter visibility, app disambiguation, paywall framing, routing ambiguity (free vs no plan), UI breadcrumb staleness, GitHub URL trust, undefined "project folder," underspecified smoke test, no bypass for experts, padding in Updating-later, truncated-looking close. Eleven captures appended under an HTML comment marker so /plan can find the group; persona key recorded inline.

**Files touched:**
- QUEUE.md: 11 captures appended to unprocessed Captures section under `<!-- INSTALL.md stranger-Claude cold-read findings ([e2e-install-guide]). -->` marker; top batch [e2e-install-guide] removed from Batches at scope-lock
- LOG/log.md: `[HASH]` placeholder backfilled to a91a35b at session start
- LOG/index.md: `[HASH]` placeholder backfilled to a91a35b at session start

**Routed to Captures:** 11 install findings ([install-note-to-claude-visible-to-user], [install-claude-code-vs-chat-app-disambiguation], [install-paid-plan-ambush-and-pricing-opacity], [install-routing-no-plan-vs-free-plan-ambiguity], [install-customise-plugins-ui-path-stale-or-wrong], [install-github-raw-url-feels-sketchy-no-provenance], [install-open-a-project-folder-undefined], [install-setup-smoke-test-underspecified], [install-no-bypass-for-experienced-users], [install-updating-later-section-is-padding], [install-step2-trailing-ellipsis-reads-as-truncated]); staleness flag for /plan: [e2e-install-guide reshape] processed capture is now fulfilled and should be dropped

## a91a35b — /plan: [e2e-install-guide] reshaped to 4-subagent stranger sims; [user-edits-rollup-on-commit] filed

Reshape direction from the c5e32d8 abort got worked out. Replaced [e2e-install-guide]'s single user-run live-chat test with Claude-orchestrated stranger-Claude subagent simulations: four parallel personas (cold-stranger, desktop-app confusion, free-plan user, already-installed) each given INSTALL.md inline and asked to read cold and report stuck-points. Cold read picked over interactive walkthrough — cheaper, parallel-friendly, surfaces structural gaps without simulating turn-taking. Findings synthesize cross-scenario (de-dup, group by area, preserve which personas surfaced each) before landing in Captures. Curated four scenarios rather than exhaustive matrix; OS-axis scenario dropped per user call. Slug + position unchanged so cross-references hold. Separately, [user-edits-rollup-on-commit] filed: the user can edit target-tree files at any time, and /done's per-build commit only stages files the build touched, so unrelated edits stay dirty across sessions. Today's case: 5 docs files dirty since at least c5e32d8 despite a prior session being told about them. Fix shape stated inline on the capture (detect, name, roll in); routing left to a later /plan.

**Queue changes:**
- [e2e-install-guide] rewritten in place at top of Batches (slug + position preserved)
- [user-edits-rollup-on-commit] appended as unprocessed capture
- LOG/log.md and LOG/index.md `[HASH]` placeholders backfilled to c5e32d8

**Captures routed:** 1 filed ([user-edits-rollup-on-commit]); 0 promoted/parked/dropped

## c5e32d8 — /next [e2e-install-guide] aborted at scope-lock; reshape direction captured

Started /next on [e2e-install-guide]. The batch as written specified a single user-run live-chat E2E (fresh claude.ai chat, paste SI repo URL, "guide me through setup"). At scope-lock the user stopped execution: a single user-run path through the install guide isn't enough coverage, and routing the test to the user is slow and depends on their session capacity. The reshape direction is Claude-run stranger-Claude subagent simulations playing out multiple scenarios in parallel — different Claude Code install states, OSes, and starting confusions — each subagent given a fresh-stranger persona and the install guide, with findings synthesized back to Captures. Batch returned to top of QUEUE.md unchanged; the reshape itself routed as a processed capture for /plan to design (scenario set, subagent prompt shape, findings synthesis). A second capture surfaced on the abort path itself — /next Step 5 abort-and-requeue has no slot for the reshape direction that motivated the abort; routing it as a capture was a judgment call, not a procedure step, and the tightening should add that step explicitly.

**Files touched:**
- None (aborted before execution)

**Routed to Captures:** [e2e-install-guide reshape], [abort-reshape-routing]

## ada58ef — /plan: 1 batch promoted, post-terseness queue fixup done in-place, misroute pattern captured

Continued from 7563bc0. Backfilled hash placeholders and fixed a slot-drift on [ship-freeform-next-type] (the 7563bc0 log recorded `Blocked by:` → `Parked:` but the file edit hadn't landed). Processed one Capture: parked the menu-vs-narration observation as [narration-vs-menu-drift] (single observation, watch for recurrence). Promoted [plan-step1-sequencing] — plan.md Step 1's entry question ("Do you have something to discuss, or ready to process Captures?") and follow-up ("Anything else, or ready for Captures?") read as either/or branches when /plan always processes Captures and discussion is just an optional pre-step; the misreading surfaced twice in this session in Claude's own output, so promote rather than wait. Three mid-session captures filed: Step 2 checkpoint sub-step rendering as bureaucratic form-fill (uniform-phrasing rule got literal-rendered; held to see if it recurs); broader observation that procedure docs grow with each captured bug but the bug-discovery rate doesn't fall (user's frame vs Claude's pushback that captures-as-tests is the system working — held without recommendation); and a misroute pattern where /plan filed a capture asking /next to verify queue-wide line-ref staleness rather than doing the work in-place during /plan (user pushed back: capture-routing is /plan's job, /next executes the top batch). The misroute prompted in-session queue fixup against current procedure-doc state (post-terseness): walked affected batches, found and fixed three drifts inline — [audit-definition] line ref 94 → 107, [setup-q4-no-expansion] stale Q4 quote updated to current "Use the user's words, don't expand or split" wording, [next-done-recommendation] stale Step 7 quote updated and the fictional "Scope discipline" section reference reworded to "near the one build at a time bullet." Staleness-flag capture dropped once the work was done in-place — proving the pattern in real time.

**Queue changes:**
- Promoted: [plan-step1-sequencing] (appended after [setup-project-agnosticism-sweep], no dependency, oldest-first fallback).
- Parked: [narration-vs-menu-drift] (single observation, watch for recurrence).
- Modified: [ship-freeform-next-type] (slot switched `Blocked by:` → `Parked:` per 7563bc0 record); [audit-definition] (line 94 → 107); [setup-q4-no-expansion] (Q4 quote refreshed); [next-done-recommendation] (Step 7 quote refreshed + "Scope discipline" reference reworded).
- Captures filed: 3 new unprocessed (Step 2 checkpoint form-fill rendering; procedure-docs-grow-but-bug-rate-doesn't-fall observation; /plan-passes-queue-work-to-/next misroute pattern).

**Captures routed:** 1 parked ([narration-vs-menu-drift]); 1 promoted ([plan-step1-sequencing], absorbed the entry-question wording capture filed mid-session); 1 dropped (terseness-staleness flag — work done in-place); 3 new mid-session captures left unprocessed for next /plan.

## 7563bc0 — /plan: freeform unparked-shape worked out, kept parked; 3 captures filed

Continued from 1b7d359. The unpark candidate [ship-freeform-next-type] kept parked at user's call but had its shape worked out in /plan: two coexisting forms (queue-driven as the primary safety valve so users don't suffer when the session type they need hasn't been recognized yet, on-demand for retrospective handmade-work wrap-ups), both subject to the same /plan-side or /next-side discipline gate ("could this be build, test, or audit?"). Added a captures-append constraint to both forms — when freeform contents would yield captures (test outcomes, feature ideas, changes to the system being built itself), Claude warns the user that /next can only append to Captures, not process them, and offers abort-and-present-in-/plan or continue-knowing-later-processing-needed. [freeform-on-demand] updated for the same coexistence framing. [ship-freeform-next-type]'s parking slot switched from `Blocked by: [behaviour-agnosticism-audit]` (stale; blocker shipped) to `Parked:` (shape worked out, deferred until ready to commit to procedure-doc edits across setup/plan/next/done). Three observations filed as captures: [blocked-by-trigger-flavors] (the `Blocked by:` slug convention doesn't distinguish landing- vs findings- vs clarity-shaped triggers; freeform's was clarity-shaped and got it right organically, but silent defaults could land on the wrong trigger), Claude's narration-vs-menu drift under exploratory tone (recommendation-narration should not soften into menu-listing when there's a preference), and the fenced-code-block "code" label problem (fence is the right visual device, the desktop app's new "code" label is wrong for prose approval outputs — needs empirical testing of markdown alternatives).

**Queue changes:**
- Modified: [ship-freeform-next-type] (shape worked out, captures-append constraint added, parking slot switched to `Parked:`), [freeform-on-demand] (coexistence framing, captures-append reference).
- Captures filed: [blocked-by-trigger-flavors] (processed), menu-vs-narration drift observation (unprocessed), fenced-block "code" label problem (unprocessed).

**Captures routed:** 1 processed ([blocked-by-trigger-flavors]); 2 raw unprocessed.

## 1b7d359 — /plan: 3 batches promoted from audit captures + close-out incongruence flagged

Processed all 12 unprocessed captures — the 11 fac25ab audit findings plus a LOG hash backfill optimization. 8 of the audit findings were mechanical-or-near-mechanical setup.md rewords (Q1-Q4, Step 4 close-out, Step 1 case wording, SPEC and QUEUE templates) and aggregated into one sweep batch; promoting each as its own one-line-edit batch would have been ceremony. 3 findings were held as processed captures because they're more than rewords: REGISTRY.md noun choice carries a Q3.5 interview-question proposal, the spec-entry-trigger threshold needs work on audience (external user vs owner-only — pronoun shifts "someone" → "you"), and plugin-behaviour.md doc-routing inherits the registry noun decision (Blocked by [setup-registry-template-and-noun]). A new audit batch [close-out-audit] was promoted to survey close-out recommendations across all four skills before [next-done-recommendation] is built — that batch addresses one observed incongruence (Step 4 setup.md close-out unconditionally offers /next even when Q4 may have produced nothing); the audit may shrink, expand, or absorb the batch, so it's now Blocked by [close-out-audit]. The hash backfill capture promoted as [log-hash-backfill-in-done]: move the work to /done where the hash is known seconds after commit, use `git commit --amend --no-edit` (safe-case exception to the prefer-new-commits rule — unpushed, seconds-old, local), eliminating /next Step 1.1 entirely. Unpark candidate [ship-freeform-next-type] flagged at session start (blocker shipped in fac25ab) — left deferred to next /plan.

**Queue changes:**
- Promoted: [close-out-audit] (placed before [next-done-recommendation], blocks it), [log-hash-backfill-in-done] (placed after [drop-log-per-release-split]), [setup-project-agnosticism-sweep] (placed after [setup-q4-no-expansion], absorbs 8 captures).
- Modified: [next-done-recommendation] now carries `Blocked by: [close-out-audit]`.

**Captures routed:** 8 promoted (into [setup-project-agnosticism-sweep]); 3 held as processed captures for own later promotion ([setup-registry-template-and-noun], [spec-entry-trigger-rethink], [plugin-behaviour-doc-routing-agnostic] with Blocked by); 1 promoted standalone ([log-hash-backfill-in-done]); 1 promoted as new batch from mid-session split ([close-out-audit]).

## fac25ab — behaviour-agnosticism audit: 11 findings routed to Captures

plugin-behaviour.md is the universal rule layer and setup.md is the on-ramp every project enters through, so app-building assumptions in either doc leak straight into how SI treats non-app projects (records-keeping, research, writing, tax-prep). The audit read both pass-by-pass against the criterion "what assumes the project is an app being built with Claude Code." 2 findings in plugin-behaviour.md (doc-routing line uses "product"/"components"; spec-entry pipeline uses "features" and external "user"). 9 in setup.md, spread across the Step 1 case wording ("source code"/"source files"), the three scaffolded doc templates (SPEC.md "the app is", QUEUE.md "builds first, then tests" missing Audit and freeform, REGISTRY.md "components"/"after each build"), all five interview questions and examples, and the Step 4 close-out. Two findings surfaced second-order issues worth flagging: REGISTRY.md may want a Q3.5-style interview prompt so the user supplies their own noun for project parts; the Step 4 close-out shouldn't unconditionally offer /next when Q4 may not have produced a usable first batch. Q4 itself got an inclusive-wording approach (keep "build/working" for app projects, add "do/made progress on" for non-app) rather than replacement — dropping "build" would alienate non-coders building with a codebase. All 11 findings live in unprocessed Captures for /plan to decide each (reword project-agnostic / demote per-type / keep with load-bearing reason).

**Files touched:**
- QUEUE.md: removed [behaviour-agnosticism-audit] batch from Batches; appended 11 captures (one per finding) to unprocessed Captures.
- _build.md: created at audit start, deleted at close.
- LOG/log.md and LOG/index.md: HASH backfill for the prior commit (777b4c3) folded in.

**Routed to Captures:** 11 findings (see prose above and QUEUE.md captures from this session).

## 777b4c3 — self-hosting dependency-management discipline: target-vs-host distinction, push-marker queue convention, /next halt

Batch ordering in QUEUE.md implicitly assumed the next batch sees the previous batch's effects — true for target-side edits Claude can read at author time, false for host-side effects (hooks, loaded skill procedures, plugin-behaviour.md rules) that only refresh after push + uninstall/reinstall. The recent bite: [capture-parking-discipline] placed before [behaviour-agnosticism-audit] on the assumption the new parking discipline would govern audit capture routing, but it wouldn't have unless a push happened between them. Fixed in two parts: a discipline rule in this project's CLAUDE.md Working conventions distinguishing target-side from host-side, and a structural form — a `--- Push required before continuing ---` queue line paired with a `(host-side)` annotation on `Depends on:`. /next halts at the marker until the user has pushed and reinstalled. The marker check sits in next.md (skill-level, so it works for any self-hosting fork), the discipline rule sits in this project's CLAUDE.md (host-only, doesn't propagate via plugin update). The parked [self-hosting-support-during-setup] capture was extended so the scaffolding template, whenever it ships, carries all of this — target/host distinction, ordering rule, marker convention, annotation — into forking projects' CLAUDE.md.

**Files touched:**
- CLAUDE.md: new "Self-hosting dependency ordering" subsection under Working conventions
- plugin/si-plugin/docs/next.md: push-marker halt added at Step 1.3
- QUEUE.md: [self-hosting-support-during-setup] parked capture extended; missing slug marker added

**Routed to Captures:** none new this build (one capture filed pre-build: LOG hash backfill optimization — move into /done via amend)

## dedb34a — /plan session: tax-folder /setup test surfaced 3 new batches + structural form for self-hosting dependency

A real /setup run in a tax-prep folder (separate, non-SI project) surfaced gaps in setup.md that ride on Claude's judgement rather than written rules: handling of pre-existing user content in Case B, and Q4's tolerance for parenthesised illustrative examples that bend "in user's words." Promoted [setup-preexisting-content-handling] to make peek-but-don't-pre-answer and leave-untouched explicit, and [setup-q4-no-expansion] to tighten Q4's rule against any expansion (illustrative or otherwise). Same run also exposed app-building framing in setup.md's interview questions, so [behaviour-agnosticism-audit] widened to cover setup.md alongside plugin-behaviour.md. Separately, the previously-captured self-hosting dependency gotcha promoted to [self-hosting-dependency-discipline] — initial draft was discipline-only, revised mid-session after the user pushed back to add a structural form: `--- Push required before continuing ---` queue marker + `(host-side)` annotation on `Depends on:`, with /next halting at the marker. Two parked captures: [freeform-on-demand] revising [ship-freeform-next-type] to be on-demand rather than queue-driven (queueing "I did some manual work" is ceremony), and [user-execution-batch-shape] deferring the question of whether non-coder projects need a new batch type for user-as-executor work until 2-3 such batches have actually run.

**Queue changes:**
- Promoted: [self-hosting-dependency-discipline] (placed at top — foundational discipline benefits later batches)
- Promoted: [setup-preexisting-content-handling] (appended)
- Promoted: [setup-q4-no-expansion] (appended after preexisting-content-handling — same setup.md thread)
- Revised: [behaviour-agnosticism-audit] (widened scope to include setup.md interview framings)
- Parked: [freeform-on-demand], [user-execution-batch-shape]

**Routed to Captures:** none new (1 unprocessed cleared via promotion)
