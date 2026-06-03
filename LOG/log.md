# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## c28297e — Add capture scan to next.md blocker gate

**Files touched:**
- plugin/si-plugin/docs/next.md: added a fourth bullet to Step 1's blocker gate that scans Captures for items relevant to the top batch, flags any that contradict, invalidate, or would benefit the batch, and recommends switching to /plan if found. Placed after the existing questions check and before the unconfirmed-tests check.

Captures can land between /plan and /next. The blocker gate already checks SPEC.md and unresolved questions but didn't look at fresh captures — a relevant capture could contradict or improve the batch about to be built. The existing questions bullet already handled the narrow case of capture-section questions affecting the current batch; the new bullet generalises that to all captures (ideas too), keeping it as a separate check so the questions bullet stays focused on its own concern.

**Routed to Captures:** none

## 5b67dc3 — Split done.md Build close-out handoff into recommend + push phases

**Files touched:**
- plugin/si-plugin/docs/done.md: split Phase 3 into Phase 3 "Recommend next" (queue-state recommendation, its own turn) and Phase 4 "Push and context" (push prompt + branching context guidance — `/clear` after push, `/compact` if not)

The old Phase 3 bundled three things into a single turn: a queue-state recommendation, a push prompt, and a blanket `/clear` instruction. Bundling defeats the recommendation — the user needs to absorb what's next before deciding whether to push, and the right context-management move depends on whether they pushed. Splitting makes both decisions sequential and gives the context guidance a real branch. Plan close-out's step 4 has the same anti-pattern; routed to Captures rather than fixed in this batch.

**Routed to Captures:** Plan close-out step 4 has the same bundled-handoff shape — symmetry candidate for /plan.

## 39663a4 — Fix next.md clean-slate output for active build check

**Files touched:**
- plugin/si-plugin/docs/next.md: Added `[SILENT]` tag to active build check (Step 1 point 1), added explicit "no output" direction for the clean-slate path

This fix has been attempted four times and kept getting lost. The active build check narrates "No active build" when no _build.md exists, which reads like a failure to users — the check is internal bookkeeping and should be silent. The fix is two things: the `[SILENT]` tag so the output rules suppress it, and an explicit sentence covering the no-_build.md path so Claude doesn't improvise output for the "nothing found" case.

**Routed to Captures:** none

## 8bc750a — Context management at skill handoffs + README model

**Files touched:**
- plugin/si-plugin/docs/behaviour.md — removed "Between skills, nudge compact if context is long" bullet from Context awareness (superseded by per-skill lines)
- plugin/si-plugin/docs/setup.md — appended "/compact or /clear" handoff line to Step 4
- plugin/si-plugin/docs/plan.md — appended the same line to Step 4 Close out
- plugin/si-plugin/docs/next.md — appended the same line to Step 7 Completion
- plugin/si-plugin/docs/done.md — appended "/clear after commit" line to both handoff sections (Build close-out Phase 3 and Plan close-out Step 4)
- README.md — "Opus 4.6 on high-output mode" → "Opus 4.6 on max effort"

**Why:** Claude loses routing accuracy as context degrades late in sessions — prescribing context management at every skill handoff addresses the root cause instead of patching individual symptoms. The rule splits by what just happened: `/compact` or `/clear` (user's choice) between skills where nothing has been committed, `/clear` specifically after /done because a commit always happens (and possibly a push). Offering `/compact` OR `/clear` between skills rather than just `/compact` preserves choice — some sessions warrant the deeper reset that `/clear` provides even when nothing has been committed. Scope expansion approved mid-build: behaviour.md's "Between skills, nudge compact if context is long" bullet was removed because the new per-skill lines supersede it — keeping both would have created contradictory rules. README tested-model line updated to match current desktop-app terminology. During /done close-out, four files surfaced as orphaned-tightening from a prior pre-push sweep (next.md, setup.md, CLAUDE-TEMPLATE.md, faq-template.md); build edits to next.md and setup.md had layered on top before the mix was caught. Recovered via `git checkout HEAD` on the two mixed files, re-applied just the build change; the two templates remain orphaned for the next push. Underlying staging gap routed to Captures.

**Routed to Captures:** 1 — push-and-rezip step 8 doesn't stage sweep-modified files

## 3a51184 — Add inline-reads rule to behaviour.md

**Files touched:**
- plugin/si-plugin/docs/behaviour.md — added "Tool use" section (2 bullets) between Response-shape tags and Captures

**Why:** Last session Claude spawned an agent for the pre-push consistency sweep — a sequential checklist that only needs a handful of Read and Grep calls. No procedure told it to use agents, but nothing told it not to. The fix is a general rule that applies across all skills so the failure mode doesn't recur in some other lookup procedure. Placed the rule under a new "Tool use" section: first bullet says direct tool calls (Read, Grep, Glob) for bounded checklists — a known set of files to read, fields to compare, strings to grep; second bullet says agents are for open-ended exploration where the shape of the answer isn't known in advance, with the embedded heuristic "if you can write out the lookups before doing them, do them inline." The heuristic in the second bullet is doing the load-bearing work — it gives Claude a concrete test rather than relying on the fuzzy bounded/open-ended distinction alone.

**Routed to Captures:** none

## 2f2a0f2 — Wire up the why-pipeline across behaviour/plan/done

**Files touched:**
- plugin/si-plugin/docs/behaviour.md — added "Why-pipeline" section (Preserve + Retrieve halves); rewrote Prior decisions bullets to point at the retrieve rule
- plugin/si-plugin/docs/plan.md — Step 3 batch structure now uses inline prose rationale instead of a labelled `Why:` line; Step 2.3 Promote and pipeline description updated to match
- plugin/si-plugin/docs/done.md — dropped [SILENT] from Phase 2; both LOG entry templates (Build close-out 2.1 and Plan close-out section 2) drop the `**Why:**` field in favour of inline prose; LOG write tagged [DISCUSS, PROMPT] with draft-and-approve flow

**Why:** The why-pipeline existed in fragments across the procedure docs but wasn't named or owned, and the retrieval half had never fired — Claude always inferred why-questions from code rather than searching the log. This build names the pipeline as a single thing and gives it two explicit halves. Preserve: rationale travels capture → batch → log as prose, re-authored at each stage with user approval, never collapsed into a structured `Why:` field. Retrieve: when asked why something exists, search LOG/log.md and LOG/log-v*.md first; only fall back to code if nothing relevant. The cross-doc changes line up with that: plan.md and done.md no longer carve out a labelled `Why:` field (which had been quietly bypassing user approval at the /done stage), and done.md's LOG write is now [DISCUSS, PROMPT] — closing the one place where rationale was being written without the user seeing the wording. Test entry deferred: the runtime check ("ask Claude why X exists, confirm it reads LOG first") needs push + reinstall + fresh session because target edits don't affect host behaviour. Sanity-demoed the rule manually mid-build (asked "why does the inline-reads rule exist?" → found in LOG entry 23a1da8 without code inference).

**Routed to Captures:** 1 capture added during /next — "/next shouldn't dump the full batch at session start" — but routed before the build proper began.

## a72a721 — /plan session: promote why-pipeline + tag removal, add 3 captures

**Queue changes:**
- Promoted "Wire up the why-pipeline: preserve prose rationale, retrieve from log" to top of Batches
- Promoted "Remove the [idea]/[question] capture tags" to bottom of Batches
- Added 3 captures: promote-before-draft visibility; one-item-at-a-time rule for behaviour.md; don't-collapse-rationale-into-structure rule for behaviour.md

**Why:** The why-pipeline (rationale carried capture → batch → log, then retrievable to answer "why does X exist") is the foundational system that's never actually worked end-to-end — preservation re-authors too freely, retrieval has never fired (Claude always infers from code, never reads the log). Promoted to top of queue ahead of the five touch-up fixes. Design crystallised mid-session: reasons are prose, never collapsed into one-line fields or typed taxonomies; capture wording → batch wording → log wording carries the prose forward with user approval at each stage; retrieval rule directs Claude to search the log first. Capture tags [idea]/[question] confirmed dead: nothing branches on them, and the two definitions contradict (faq-template.md frames them as parallel categories; plan.md/behaviour.md describe them as sequential refinement stages). Three behaviour captures surfaced live during the session: user approved promotion before seeing concrete entries (visibility gap in /plan); Claude sent walls of text instead of one item at a time (Alex's global preference should be plugin-wide); designing the why-pipeline almost collapsed rationale into structured fields before user corrected it — the prose-not-structure principle generalises beyond the why-pipeline batch.

**Captures routed:** 1 capture promoted (tag removal); 1 emergent batch promoted (why-pipeline, surfaced mid-interview); 3 new captures added; 7 original captures left unprocessed.

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
