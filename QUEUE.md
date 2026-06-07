# QUEUE

## Batches

Worked top to bottom. Each batch of changes or tests is one /next session of either type:

- build session where changes are applied, then claude runs all tests it is able to do itself
- test session where the user runs any testing only they can do

**E2E: install guide drives a fresh Claude chat through SI setup** **[e2e-install-guide]**
Depends on: install-guide

Once INSTALL.md and the README reframing exist, the only meaningful verification is the actual flow it's meant to support: a fresh Claude chat with no prior context, given the repo link and "guide me through setup." This catches three things at once — whether Claude finds INSTALL.md from the README pointer, whether the opening interview questions land for a real user, and whether the branched walkthrough (Claude Code install → paid plan → plugin install) runs cleanly. Splitting this from the build batch keeps the build commit clean and gives the test its own LOG entry, since the result is feedback (does the guide work?) not changed files.

Test:
- E2E (user-run, separate live session): open a fresh Claude chat at claude.ai with no prior context. Paste the SI repo URL. Say "guide me through setup." Observe whether Claude finds INSTALL.md, runs the opening interview, and walks through the branches cleanly. Report findings as captures (anything Claude missed, mis-paced, or routed to the terminal when it shouldn't have).

**Refresh reader-test-workflow.js to match current SI shape** **[reader-test-refresh]**

The reader-test workflow's fake project has drifted from how SI actually works now: it includes a DECISIONS.md doc and routes design rationale through it, queue entries are type-tagged inline as [build]/[test]/[idea]/[question], and the mirrored CLAUDE.md likely shows the older shape too. Running the workflow as-is mostly measures drift between current docs and a stale fake project, not drift between current docs and real reader comprehension — so findings come out noisy and signal is lost. The refresh aligns the fake project with current SI (LOG-based why-pipeline, Build/Test subheadings + Captures section, current CLAUDE.md template), re-checks the session-start hook output strings against the current session_start.py, and audits the 5 stock user questions for ones now trivially answered or phrased in ways a real user wouldn't. The synthesis FAQ vs Other split stays — user-question-shaped findings feed the FAQ template, procedure findings feed procedure docs; collapsing would lose that signal. FAQ template staleness gets handled downstream by running the refreshed workflow, not as upfront work here.

Build:
- resources/reader-test-workflow.js: drop FAKE_DECISIONS and DECISIONS.md references; replace with a short FAKE_LOG showing 1-2 entries in current format (inline prose rationale, **Files touched:** block).
- resources/reader-test-workflow.js: rewrite FAKE_QUEUE to use bold batch titles with Build/Test subheadings and a separate Captures section; drop inline [build]/[test]/[idea]/[question] type tags.
- resources/reader-test-workflow.js: rewrite FAKE_CLAUDE_MD to mirror current plugin/si-plugin/templates/CLAUDE-TEMPLATE.md.
- resources/reader-test-workflow.js: verify SESSION_NO_BUILD and SESSION_ACTIVE_BUILD strings against current plugin/si-plugin/hooks/session_start.py output; update if drifted.
- resources/reader-test-workflow.js: audit the 5 USER_QUESTIONS; replace any now trivially answered by current docs or phrased in ways a real user wouldn't.
- resources/reader-test-workflow.js: leave the synthesis FAQ/Other split intact.

Test:
- Run the refreshed workflow once (user-triggered, requires ultracode/opt-in). Inspect the synthesis output: do findings reflect real comprehension gaps in current docs, or do they still flag old-shape mismatches? Route useful findings to QUEUE Captures.

**Trickle-up audit: rules that belong in plugin-behaviour.md** **[trickle-up-audit]**

The four procedure docs (setup.md, plan.md, next.md, done.md) likely repeat rules that aren't skill-specific. Repeated rules cost token budget at every skill load and drift between copies; plugin-behaviour.md exists so cross-skill rules are stated once. This audit finds the candidates and surfaces them as captures for /plan to route — no direct edits, per the audit-batch contract.

Audit:
- Target: setup.md, plan.md, next.md, done.md
- Criteria: rules stated in more than one of the four; rules that aren't skill-specific even when they appear in only one; anything reading like communication, captures, why-pipeline, dependency ownership, or file safety guidance (those categories already live in plugin-behaviour.md). For each finding: name the rule, name the doc(s) it appears in, note whether plugin-behaviour.md already has a related rule, and propose a target location.

**Output tag overhaul audit: prose where a response-shape tag belongs** **[output-tag-audit]**

The procedure docs were authored before the response-shape tag system was fully in place, so some steps still describe output behaviour in prose where a tag ([SILENT], [BRIEF], [PROMPT], [DISCUSS], [SEQUENCE]) would compress the intent and apply uniformly. Prose substitutes are easy to misread and drift across docs; tags are the canonical mechanism. One known finding to seed the audit: _build.md entry ticking in next.md should be [SILENT] (crash-recovery bookkeeping, not a status report).

Audit:
- Target: setup.md, plan.md, next.md, done.md
- Criteria: any step whose prose describes verbosity or interaction shape (e.g. "say nothing," "briefly note," "ask the user," "discuss tradeoffs," "one at a time") where the matching tag would carry the same intent more cleanly. Also flag tag misuse — a tag applied where the step's prose contradicts it, or a tag missing where the step's behaviour clearly needs one. For each finding: quote the prose, name the candidate tag, note whether replacement is full (tag alone) or partial (tag + retained prose).

**In-scope / out-of-scope distinction audit** **[scope-distinction-audit]**

The in-scope vs out-of-scope distinction shows up across plan.md, next.md, and plugin-behaviour.md — it governs what enters the active build, what gets noted for later, and what halts the build for scope renegotiation. The concern is whether the distinction is stated explicitly enough to be followed mechanically, or whether it currently rides on Claude's judgment without an anchor doc. If the latter, drift is invisible until a build accidentally absorbs something it shouldn't have or stops for something it should have just queued.

Audit:
- Target: plan.md, next.md, plugin-behaviour.md
- Criteria: every passage that turns on "in scope" or "out of scope" (or synonyms — within scope, scope creep, beyond scope, the active batch's scope). For each: is the distinction defined where it's used, or assumed? Are the rules for routing out-of-scope discoveries (Captures vs halt-and-ask vs silently skip) consistent across docs? Is there a single canonical statement of what scope means in this system, or is it scattered? For each finding: quote the passage, name what's load-bearing on judgment, propose either a wording tightening or a single anchor location.

**Tighten Claude's completion recommendation: always /done, never /next** **[next-done-recommendation]**

next.md Step 7's close-out says "Run /done to record this and commit, or keep adjusting" — but Claude has been observed recommending /next instead at completion, while still inside the just-finished /next session. The mechanical safety net catches the worst case (session_start detects _build.md and routes the next /next to resume, not a fresh build) so dual builds don't actually start — but the missed /done still costs a LOG entry and a commit for the batch that just finished. The fix isn't a wording change at Step 7; the doc says the right thing already. It's tightening whatever lets Claude substitute /next for /done at completion — likely an explicit rule under Scope discipline in plugin-behaviour.md, since "one build at a time" is the same principle in different framing.

Build:
- plugin-behaviour.md: add a rule under Scope discipline stating that at build completion the only valid next-step recommendation is /done — never /next, never another build skill. Frame as the completion counterpart to "one build at a time."
- next.md Step 7: consider whether the close-out wording needs a [SEQUENCE] or [BRIEF] tag to reinforce that the close-out recommendation is the one place /done must be named explicitly. Apply the tag if it adds clarity; skip if the new plugin-behaviour.md rule covers it.

Test:
- Self-verifying from the rule text. No separate verification entry.

**Fold unpark candidates into the Step 2 capture-processing loop** **[fold-unparks-into-step-2]**

When /plan's Step 1 unpark scan finds Parked items that the surrounding work has unblocked, there's currently no structural home for them — the procedure says to "surface findings" but doesn't route them anywhere, so they get smushed into the entry question alongside the Captures summary. That collides two decision surfaces: the read-state report and the entry question. Folding unpark candidates into Step 2 reuses the loop the user already knows: each unblocked Parked item enters the SEQUENCE as if it were a capture, sourced from Parked instead of Captures. The user gets the same promote / keep-parked / drop choice in the same shape, processed before Captures (Parked items have been waiting longest).

Build:
- plan.md Step 1: keep the unpark + staleness scans, but reframe the output as "candidates feeding Step 2" rather than "findings to narrate before the entry question." Drop the smushed-into-narration shape.
- plan.md Step 2: add a sub-section above the existing Captures loop stating that unpark candidates from Step 1 are processed first, using the same five-sub-step loop (present + interview, recommend, execute, remove, checkpoint). Recommend wording is the same three options — except "park" means "keep parked" for items already in Parked, and "promote" means "move out of Parked into Batches as a full batch entry." Drop removes the Parked item entirely.
- plan.md Step 1 entry question: revert to clean "Do you have something to discuss, or ready to process Captures?" — no candidates folded in. Unpark candidates surface only inside Step 2.
- plan.md Step 2 count statement: include unpark candidates in the upfront count ("5 items. First: ...") so the SEQUENCE rule applies uniformly.

Test:
- Self-verifying from the procedure text on next /plan run with unpark candidates present. No separate verification entry.

**Narrate _build.md's purpose at the moments it's created and consulted** **[narrate-build-md-purpose]**

_build.md isn't a passive marker; it carries the active batch's working state out of QUEUE.md (which is read-only during builds), feeds the pre_tool_use scope-lock hook, holds crash-recovery tick state, and carries rationale prose forward to /done's LOG entry. None of that is visible in the procedure docs today, so the file reads as bookkeeping or vestigial overhead. Other parts of the system narrate their value as they're invoked (dependency ownership narration, ordering reasoning, unpark surfacing); _build.md should follow the same pattern. All narration here must be [BRIEF] — one short sentence per location, not paragraphs. The point is visibility, not explanation.

Build:
- next.md: at the step where _build.md is created, add a [BRIEF] narration line stating what _build.md is for, in the user-facing terms above (working surface, scope-lock data, crash-recovery state, rationale carrier into /done).
- next.md: at the resume path (active _build.md detected at session_start), add a [BRIEF] narration line stating what's being read and why.
- done.md: at the step where _build.md is consumed and removed, add a [BRIEF] narration line stating the rationale is being re-authored from _build.md into the LOG entry.
- All three additions must be [BRIEF]. One sentence each, no paragraphs. The point is visibility, not explanation.

Test:
- Self-verifying on the next /next + /done cycle. The narration either appears at the right moments or it doesn't.

**Drop per-release log file split; one growing log.md** **[drop-log-per-release-split]**

The push-and-rezip ritual currently caps log.md at each push and renames it log-v<VERSION>.md, starting a fresh log.md. The justification was that Claude could understand a version's changes as a coherent set — but that doesn't match how the why-pipeline retrieve actually works. Retrieve goes through LOG/index.md by git hash, then opens specific entries; cross-entry cohesion within a release isn't load-bearing on any lookup. Design threads span releases anyway, so the split doesn't mark a real boundary. One growing log.md going forward. Existing log-v*.md files stay where they are — index references work by hash, so old entries remain findable across whichever file holds them.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md: update the why-pipeline retrieve rule. Remove the "or LOG/log-v*.md" branch from the open-matched-entries instruction; retrieve becomes "search LOG/index.md, then open the matched entry in LOG/log.md."
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md: check for and remove references to per-release log files, archived release files, or "this file covers the current release" framing in LOG/log.md heading text.
- plugin/si-plugin/skills/setup/, plan/, next/, done/ procedure docs: grep for log-v*.md and per-release-log references; remove or revise so they describe a single growing log.md.
- This project's CLAUDE.md (host-only, doesn't propagate via plugin update): remove steps 3 and 4 from the push-and-rezip section (the push marker and the cap-and-rename ritual). Version bumping stays; the rename and the fresh log.md creation go. Add a short note that pre-existing log-v*.md files are archived from the old scheme and stay in place — retrieve still works via hash.

Test:
- Self-verifying from the doc edits.
- After the next push: ask Claude a "why did we decide X" question targeting an entry that lives in an archived log-v*.md file. Verify retrieve still works through the index + grep — confirming nothing breaks from leaving old log files in place under the new scheme.

### Parked

- **[sizing-gates-rework]** Sizing gates rework — research filed at resources/research/batch-sizing-research.md. Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

- FAQ edit: incorporate the four functions of _build.md as an entry for users who wonder what _build.md does or whether it's vestigial. The four functions: (1) carries the active batch's working state out of QUEUE.md, which is read-only during builds; (2) feeds the pre_tool_use scope-lock hook (which files this build may touch); (3) holds crash-recovery tick state so resumed sessions don't re-derive from a partial commit; (4) carries rationale prose forward into /done's LOG entry. Shelved: don't promote until [reader-test-refresh] has run and the refreshed reader test's findings have been routed — those findings may shape what belongs in the FAQ and how it's worded, so editing the FAQ first risks immediate rework.

- Procedure docs leak internal sequence language ("loop," "Step 2," etc.) into Claude's user-facing chat. Observed in this /plan session: Claude said "the loop" and "Step 2" multiple times before the user flagged it as unintelligible jargon. Plugin-behaviour.md already states that internal procedure terms must not appear in output the user sees, but plan.md (and likely other procedure docs) describe the capture-processing sequence in terms like "the Step 2 loop" without flagging that this naming is Claude-facing only. Fix candidates: audit procedure docs for sequence-naming language that could leak (the output-tag-audit batch may catch some of this; this capture is the narrower sibling about *naming* rather than *output shape*); add an explicit reminder near the loop description that the structure name is internal and chat references should use plain terms ("the next item," "moving through the items one at a time").

- Audit batch type's definition is too narrow: current wording (in next.md and plan.md, wherever audit is described) likely leans on "Claude systematically reads target docs against criteria," which embeds two assumptions that don't generalize — Claude as the reader, and docs as the targets. The defining property of an audit batch is actually its output contract: findings, not changed files, routed through Captures. The "who reads" (Claude, the user via a workflow, a simulated reader) and the "what's read" (procedure docs, the user's spec, their code, UI flows, test outputs) are implementation details. Generalize the definition to "output is findings to Captures, no direct edits to artifacts" so it reads cleanly for any user building any kind of project. Downstream effect: [reader-test-refresh] could be reclassified Build + Audit instead of Build + Test, since the workflow run produces findings routed through Captures — surface that reclassification as part of the same fix or as a follow-up capture once the definition lands.

### Parked

- Add scenarios to reader-test-workflow.js — after [reader-test-refresh] lands and the refreshed workflow has been run once, evaluate which scenarios are still undertested and worth adding. Known blind spots regardless of refresh outcome: /setup interview (untested), push-and-rezip sweep (untested — lives in this project's CLAUDE.md, not plugin docs, so coverage question is whether it should even be in scope for plugin reader-tests), mid-build resume from a real _build.md (current next.md sim covers fresh /next, not resume), /done plan-mode close-out (current sim only covers build close-out), empty-queue handling, audit-batch flow (planning-as-work). Decision deferred because the refreshed first run may surface blind spots not on this list, or may show that scenario count matters less than scenario specificity. Promote as one or more build batches once scenarios are picked.

- Batch cohesion ordering heuristic — the build log as decision log creates pressure for discrete builds, and batch ceremony is friction for users. Queue ordering rule: builds touching an area with no related batches yet should sink (absent urgency or dependency), giving time for more captures to accumulate and make the batch worthwhile. Batching also touches context window management, not just coherent logging — Claude needs to think about one area of related concerns at a time. Needs design work to sharpen "no friends" and "related" into a mechanical rule. (The companion /next-time check — recommend switching to /plan if related captures exist for the top batch — shipped as the next.md blocker-gate capture scan.)
- Cruise control skill — a skill that runs build→commit→build→commit through a batch (or multiple batches) unattended, stopping only when it hits something requiring user input. Key design concerns: (1) wording that doesn't pressure Claude to push through uncertainty, (2) dependency management when Claude decides when to wrap a batch, (3) /done judgment steps can't get skipped for speed. Parked: depends on stabilizing the skills it would chain.
- Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
- /done spec check — after writing the **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. Retrospective check (at decision time) vs the current /plan pipeline gate (prospective, at planning time). Both mechanisms need more real usage before deciding how they relate.
- Threshold-based context management — if hooks ever gain token usage fields (e.g. `context_usage_pct`), the plugin could recommend `/compact` or `/clear` based on actual utilization instead of rule-based triggers. Research filed at resources/research/context-window-hook-access.md. Parked: depends on Anthropic adding token data to hook event input.
- Pre-push sweep could be lighter if /done flagged host-side impacts at build time — accumulate a manifest of "this change affects X in project docs" during /done while context is fresh, then the push sweep checks flagged spots instead of re-reading everything. Sweep stays as safety net but gets cheaper. Design question: cross-build staleness (build 3 invalidates something build 1 touched) still needs the sweep to catch it.
