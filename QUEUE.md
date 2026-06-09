# QUEUE

## Batches

Worked top to bottom. Each batch of changes or tests is one /next session of either type:

- build session where changes are applied, then claude runs all tests it is able to do itself
- test session where the user runs any testing only they can do

**E2E: stranger-Claude subagent simulations across 4 install scenarios** **[e2e-install-guide]**

Replacing the single user-run live-chat test (aborted c5e32d8). A single path through INSTALL.md is insufficient coverage and routing it to the user is slow. Instead, Claude orchestrates four parallel stranger-Claude subagents — each given a fresh-stranger persona and the contents of INSTALL.md, with no prior SI context — to read the guide cold and report where they would get stuck. Cold read (not interactive walkthrough) catches structural gaps cheaply; interactive simulation is deferred unless a later need surfaces. Findings synthesize across scenarios (de-dup, group by area) and route to Captures for /plan to process. No direct edits to INSTALL.md — this batch's output is findings, not changes.

Build:
- Orchestrate four subagents in parallel, one per scenario:
  1. Cold-stranger, nothing installed — persona has never used Claude Code, doesn't know what a plugin is, no Claude Code installed.
  2. Desktop-app confusion — persona has the Claude desktop chat app and assumes that is Claude Code.
  3. Free-plan user — persona has Claude Code installed on the free plan, doesn't know plugins need a paid plan.
  4. Already-installed, fresh project — persona has Claude Code + paid plan + has installed other plugins, never SI.
- Each subagent prompt: persona statement, the contents of INSTALL.md inline (don't make them fetch it), goal ("you want to start using this thing"), report instructions ("read it cold, name every point where you'd get stuck, confused, or stop — don't try to execute, just report"). No turn-taking simulation.
- Synthesize the four findings lists: de-dup findings that surfaced across multiple personas, group by area of INSTALL.md (or by guide-stage if more useful), preserve which scenarios surfaced each finding so signal isn't lost.
- Append the synthesized findings to QUEUE.md Captures (unprocessed section), one capture per grouped finding, each tagged with which scenarios surfaced it.

Test:
- Self-verifying: the four subagent reports + synthesized findings list either land in Captures cleanly or they don't. Quality of findings gets judged at the next /plan when they're processed.

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

**Audit close-out recommendations across all four skills** **[close-out-audit]**
Blocks: [next-done-recommendation]

Across /setup, /plan, /next, /done, the close-out step recommends what to run next — but the shape varies skill-to-skill and the recommendations may not be consistent. Known incongruences: setup.md Step 4 unconditionally offers /next even when Q4 may not have produced a usable first batch; [next-done-recommendation] tackles /next-recommended-instead-of-/done at build completion, but that's one observed instance, not a full survey. Running the audit first means [next-done-recommendation]'s scope may shrink, expand, or be absorbed entirely — better to know before that batch is built. Findings route to Captures per the audit-batch contract; no direct edits.

Audit:
- Target: the close-out step in each of setup.md, plan.md, next.md, done.md (the final "tell the user what to run next" block in each).
- Criteria: (a) what next-skill does the close-out recommend? (b) is the recommendation unconditional, or gated on actual produced state (e.g. "only offer /next if a batch exists")? (c) is the recommendation shape consistent across the four skills, or does each skill recommend differently? (d) does any close-out implicitly recommend re-running itself, or branching to a non-immediate-next skill? (e) does the commit-and-push prompt make sense for every session shape? /plan sessions update local planning state only — pushing them treats planning work as a ship event, which it isn't. /next sessions ship plugin changes (after the push-and-rezip ritual elsewhere). Survey whether the commit-and-push offer fits each skill's actual semantics, and propose tightening (e.g. /done after /plan offers commit only; push is reserved for the rezip flow). For each finding: quote the passage, name the incongruence or gap, propose a tightening (or note that the existing wording is correct and consistent).

**Tighten Claude's completion recommendation: always /done, never /next** **[next-done-recommendation]**
Blocked by: [close-out-audit]

next.md Step 7's close-out says "Run /done to record this and commit, or tighten what's already built before closing" — but Claude has been observed recommending /next instead at completion, while still inside the just-finished /next session. The mechanical safety net catches the worst case (session_start detects _build.md and routes the next /next to resume, not a fresh build) so dual builds don't actually start — but the missed /done still costs a LOG entry and a commit for the batch that just finished. The fix isn't a wording change at Step 7; the doc says the right thing already. It's tightening whatever lets Claude substitute /next for /done at completion — likely an explicit rule near "one build at a time" in plugin-behaviour.md, since that's the same principle in different framing.

Build:
- plugin-behaviour.md: add a rule near the "one build at a time" bullet stating that at build completion the only valid next-step recommendation is /done — never /next, never another build skill. Frame as the completion counterpart to "one build at a time."
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

**Move LOG hash backfill from /next into /done** **[log-hash-backfill-in-done]**

LOG entries reference the commit hash of the build that landed them, but /done writes the entry before the commit hash exists — so the entry ships with a `[HASH]` placeholder and /next Step 1.1 backfills it next session. That works but is slow: grep two files, batch-read them, run `git log` for the hash, edit both placeholders. The hash is unknown at write time but known one second after /done commits. Moving the backfill into /done — run `git log -n 1 --pretty=%h` after the commit lands, edit both `[HASH]` placeholders inline, `git commit --amend --no-edit` — eliminates /next Step 1.1 entirely and lands each session with its hash already inline. The amend looks like it brushes against the "prefer new commits over amending" global rule, but the rule exists to protect against rewriting history others might have pulled; on an unpushed local commit made one second ago, that risk is zero — this is the rule's intended safe-case exception.

Build:
- plugin/si-plugin/docs/done.md: after the build commit step, add a backfill step — run `git log -n 1 --pretty=%h -- LOG/log.md`, edit the `[HASH]` placeholders in LOG/log.md and LOG/index.md to the returned hash, then `git commit --amend --no-edit`. Brief note that the amend is safe here (unpushed, seconds-old, local).
- plugin/si-plugin/docs/next.md Step 1: remove the LOG hash backfill sub-step entirely (currently Step 1's "Backfill LOG hashes first" block).
- plugin/si-plugin/docs/plan.md Step 1: same removal — plan.md's "Backfill LOG hashes first" block at the top of Step 1 goes too, since the new scheme guarantees no stale placeholders.

Test:
- Self-verifying on the next /done run: the commit ships with hashes inline, and the next /next session finds nothing to backfill.

**Vocabulary rule: name background-only terms; require translate-or-omit when narrating** **[narration-vocabulary]**

plugin-behaviour.md already says internal procedure terms must not appear in user-facing chat, but the rule rides on Claude's judgment of which terms count as internal. Observed leakage in the last /plan session ("the loop," "Step 2") shows the rule is too abstract to catch the actual offenders. The fix is to name them: a short Vocabulary section listing background-only terms (loop, Step N, Phase X, sub-step, pass, gate, batch slug, etc.) and the companion rule — when narrating to the user, translate to user-facing language ("the next item," "moving through them one at a time") or omit the structural reference entirely. Marker-based enforcement (inline tags on internal terms in procedure prose) is deferred to a follow-up capture; ship the rule first, see whether Claude leaks despite the explicit list, then decide.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md: add a Vocabulary section under Communication listing the background-only terms (loop, Step N, Phase X, sub-step, pass, gate, batch slug, plus any others surfaced while drafting). State the translate-or-omit rule with one or two short examples ("the loop" → "the next item" or omit).
- plugin/si-plugin/docs/plugin-behaviour.md: cross-link the new section to the existing "no internal terms in user-facing chat" rule so the relationship is explicit — the new section sharpens the old rule by naming the offenders, not replacing it.

Test:
- Self-verifying on the next /plan or /next run: does Claude still narrate in structural terms, or does the explicit list catch it.

**Generalize audit-batch definition: lead with output contract, drop docs-as-target framing** **[audit-definition]**

The audit-batch type was written from the SI-developing-itself case (Claude reads procedure docs against criteria) and the wording reflects that. plan.md's thinking-work exception names the defining property as "systematic read of target docs against fixed criteria"; the sizing gate's vague-target example is "the procedure docs"; next.md's Audit procedure intro frames the shape as "systematic read of the target"; Step 2 says "Open every file named by the target." All four embed docs-as-target. The real defining property is the output contract — findings to Captures, no direct edits to artifacts — and that's what differentiates audit from build and test. Reader is always Claude; what gets read (procedure docs, the user's spec, code, UI flows, workflow output, any other artifact) is an implementation detail. Generalizing the wording lets audit cover any artifact type without rewriting the definition each time a new audit shape comes up. Doesn't change procedure substance — read-many-propose-many still describes how audits run — just lifts the assumptions out of the type's definition.

Build:
- plugin/si-plugin/docs/plan.md ground rules (line 11, thinking-work exception): reframe so the exception is keyed on the output contract (findings to Captures, no direct edits) rather than "systematic read of target docs against fixed criteria." The audit exception exists because audit work preserves the no-direct-edits property the rule against thinking-work-as-build-batch was protecting; that's the load-bearing reason, not the read-docs shape.
- plugin/si-plugin/docs/plan.md Step 3 (Audit batch sizing gate, line 107): keep the gate's substance (target + criteria specific enough that Claude can apply them) but broaden the vague-target example beyond "the procedure docs" so the gate reads as generic ("the docs", "the code", "the UI flows" — pick one or two).
- plugin/si-plugin/docs/next.md Audit procedure intro (line 172): lead with the output contract, then describe the procedure shape (read-many-propose-many). Name target variety explicitly — procedure docs, user's spec, code, UI flows, workflow output, any other artifact — so the procedure reads as generic, not docs-specific.
- plugin/si-plugin/docs/next.md Step 2 (line 181): change "Open every file named by the target" to "Read every artifact named by the target" so the procedure language doesn't assume files. Keep the criterion-pass-by-pass instruction — that generalizes cleanly.
- Sweep setup.md and done.md for stray audit-as-docs-read references; revise to match the generalized framing if any are found.

Test:
- Self-verifying from the doc text. After the rewrite, the audit-batch wording reads cleanly for any artifact type without requiring "(but adapt to your case)" handwaving.

**Pre-existing content handling in /setup Case B** **[setup-preexisting-content-handling]**

Setup.md is silent on what to do with pre-existing non-method content in a Case B folder (some content present, no method docs). Observed in a real /setup run on a tax-prep folder with one pre-existing brief: Claude judgment-called to peek at the brief before Q1 (used it to frame a clarifier without pre-answering) and to leave it untouched during scaffolding while naming it in the closing message. Both calls landed, but a different run could skip the peek (asking Q1 cold and missing context) or pre-answer Q1 from the brief (bundling, against the rules). The fix is to make both behaviours explicit so they don't ride on judgment.

Build:
- plugin/si-plugin/docs/setup.md Case B branch: add a rule that Claude peeks at any pre-existing user content before Q1 — use it to frame the question with a parenthetical clarifier if useful, never to pre-answer it. One short example showing the framing-vs-bundling line.
- plugin/si-plugin/docs/setup.md Case B branch: add a rule that pre-existing user content is left untouched during scaffolding and explicitly named in the closing message as a source doc the user can refer back to.

Test:
- Self-verifying on the next /setup run in a Case B folder.

**Forbid illustrative expansion in /setup Q4 batch entry** **[setup-q4-no-expansion]**

Setup.md Q4's rule is currently "Use the user's words, don't expand or split — scope decisions belong in /plan." Observed in a real /setup run: Claude wrote the batch with parenthesized examples drawn from a pre-existing source doc ("e.g. overlocker receipt, mortgage interest %"). Parenthesized examples read as illustrations not commitments, but they're still expansion beyond the user's words — and a queue entry with examples looks like the user agreed to those items even when they're in parens. The rule needs tightening: no expansion at all, even illustrative. If examples would clarify what's in scope, the place is a Q4 follow-up question to the user, not a parenthetical in the written entry.

Build:
- plugin/si-plugin/docs/setup.md Q4 rule: tighten the existing "Use the user's words, don't expand or split" to forbid illustrative expansion explicitly — "Use the user's words verbatim. No expansion, no illustrative examples, no parentheticals drawn from visible context. If examples would clarify scope, ask a Q4 follow-up; don't smuggle them into the entry."
- plugin/si-plugin/docs/setup.md Q4 rule: note that the existing one-follow-up-max rule for vague answers covers the case where examples actually are needed.

Test:
- Self-verifying on the next /setup run where Q4 is answered and visible source content exists.

**Project-agnosticism sweep: rewrite setup.md to read for non-app projects too** **[setup-project-agnosticism-sweep]**

setup.md is the on-ramp every project enters through, and its current wording assumes the user is building an app: the five interview questions, the Step 4 close-out, the Step 1 folder-state cases, and the three scaffolded doc templates (SPEC.md, QUEUE.md) all use app-building framing ("building," "components," "functionality," "source code," "builds first then tests"). The behaviour-agnosticism audit (fac25ab) surfaced 11 findings; 8 collapse into one sweep of mechanical-or-near-mechanical rewords applied across setup.md and its scaffolded templates. The three more substantive findings — REGISTRY.md noun choice (Q3.5 interview question), the spec-entry-trigger threshold across project types, and plugin-behaviour.md doc-routing — are held in separate captures for their own consideration. This sweep changes wording only; no interview-flow changes, no rule-trigger changes.

Build:
- plugin/si-plugin/skills/setup/setup.md Q1: reword to "What is this project, and who is it for?" (drop "building"). From [setup-q1-agnostic-wording].
- plugin/si-plugin/skills/setup/setup.md Q2: reword to "What's the core of it — the main thing it produces, organises, or does?" (drop "functionality / does"). From [setup-q2-agnostic-wording].
- plugin/si-plugin/skills/setup/setup.md Q3 examples: replace software-only example set with 3–4 examples spanning software + non-software projects. From [setup-q3-agnostic-examples].
- plugin/si-plugin/skills/setup/setup.md Q4: reword inclusively — "What's the first thing to build or do? What would you want to have working or made progress on by the end of today?" Keeps build-shape framing for app projects, adds do/progress framing for others. From [setup-q4-inclusive-wording].
- plugin/si-plugin/skills/setup/setup.md Step 4 close-out: reword to "Run /plan to scope your first batch, or /next if you're ready to start the first batch." (drop "ready to build"). From [setup-step4-close-out-wording].
- plugin/si-plugin/skills/setup/setup.md Step 1 folder-state cases: reword Case A / Case B to "No content" / "Content exists" (or similar project-agnostic phrasing). From [setup-step1-case-wording].
- plugin/si-plugin/skills/setup/setup.md SPEC.md template (line 48): reword "What the app is" to "What the project is". From [setup-spec-template-agnostic].
- plugin/si-plugin/skills/setup/setup.md QUEUE.md template (line 63): reword "Each batch is one /next session — builds first, then tests." to "Each batch is one /next session. Subheadings name the kind of work (Build, Test, Audit)." From [setup-queue-template-type-complete].

Test:
- Self-verifying from the doc text. After the rewrite, setup.md reads cleanly for a tax-prep, records-keeping, research, or writing project as well as for an app project.
- E2E follow-up (user-run, separate live session, queue as separate batch if desired): rerun /setup in a non-app folder and observe whether the questions land cleanly.

**Reframe /plan Step 1 entry + follow-up as sequencing, not either/or** **[plan-step1-sequencing]**

plan.md Step 1's entry question ("Do you have something to discuss, or ready to process Captures?") and its follow-up after a discussion item ("Anything else, or ready for Captures?") both use "or" framing that reads as a branch — discuss-vs-process — when /plan always processes Captures and a discussion item is just an optional pre-step. The misreading surfaced twice in the 7563bc0+1 /plan: Claude reproduced the framing in the read-state summary ("if processing...") and bundled an unrelated housekeeping decision onto it as a conditional, the same wording bug surfacing in Claude's own output. Fix the wording so processing reads as the destination and discussion as the optional thing that happens first if there is one.

Build:
- plugin/si-plugin/docs/plan.md Step 1 entry question: replace "Do you have something to discuss, or ready to process Captures?" with wording that frames processing as the destination — e.g. "Anything to discuss before we process Captures?" Keep the empty-Captures branch ("If Captures is empty, ask what they'd like to work on.") as-is.
- plugin/si-plugin/docs/plan.md Step 1 follow-up after a discussion item: replace "Anything else, or ready for Captures?" with matching wording — e.g. "Anything else before Captures?"
- plugin/si-plugin/docs/plan.md Step 1 branching structure ("If the user has something" / "When ready: Move to Step 2"): adjust so the prose matches the new framing — discussion items run first if present, then Step 2 always runs, no either/or branch.

Test:
- Self-verifying from the doc text on the next /plan run. The entry question and follow-up should read as sequencing, and Claude shouldn't reproduce "if processing" or similar branching framing in narration.

### Parked

- **[sizing-gates-rework]** Sizing gates rework — research filed at resources/research/batch-sizing-research.md.
  Parked: further research needed on session-length as a mid-build split indicator before the rework is actionable.
  Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session. Processed captures (slug assigned, dependencies scanned) sit above the `---` divider; unprocessed raw captures collect below. See plan.md Capture and parking discipline.

- **[setup-registry-template-and-noun]** setup.md REGISTRY.md template (lines 78–82, scaffolded into user's REGISTRY.md) assumes projects have "components" (software-architecture term) and that builds are the only thing that adds to the registry: "Components that exist in this project. Updated after each build." A tax-prep project might register a receipts folder, a lender list, a year-end packet — not components, and entered via audit or freeform work, not builds. Proposal: add a Q3.5-style interview prompt — "what are this project's parts called?" — and use the user's own noun in the scaffolded REGISTRY.md. Decouple the update trigger from "build" too ("Updated as the project grows" or similar). Held out of the project-agnosticism sweep — the Q3.5 proposal adds a new interview question, not just a reword; deserves its own consideration. From [behaviour-agnosticism-audit].

- **[spec-entry-trigger-rethink]** plugin-behaviour.md line 83 spec-entry pipeline assumes the project ships features to an external user: "New features need a spec entry before a build entry. … Threshold: if a user would see or experience the difference, update SPEC.md first." For a personal records-keeping or tax-prep project there are no "features" and the owner is the only "user." Reword project-agnostic — replace "new features" with something like "new scope items" or "new project properties," and broaden the threshold ("if the project's output or shape changes in a way someone would notice"). Needs further thinking — the noun "features" is load-bearing (it names what triggers a spec entry) and the audience for "noticeable" differs by project: for owner-only projects the audience is the owner themselves ("you would notice"), for external-user projects it's a third party ("someone would notice"). A clean reword has to capture both shapes — or the rule splits per project type. Not a one-shot reword; held out of the project-agnosticism sweep. From [behaviour-agnosticism-audit].

- **[plugin-behaviour-doc-routing-agnostic]** plugin-behaviour.md line 81 doc routing assumes the project is a product made of components: "SPEC.md = what/who/how/why the product exists. … REGISTRY.md = what components exist." A records-keeping or tax-prep project has neither — it has organised material, not a product with parts. Reword project-agnostic, e.g. "what/who/how/why the project exists" and a neutral noun for the project's constituent things (parts? entries? items?), or demote per-project-type. The "product" → "project" reword is mechanical; the "components" → ? noun decision is the same problem as [setup-registry-template-and-noun] in a second location.
  Blocked by: [setup-registry-template-and-noun] — inherits whichever noun strategy that batch decides on (Q3.5 user-supplied noun vs neutral fallback). From [behaviour-agnosticism-audit].

- **[blocked-by-trigger-flavors]** Dependency ownership's `Blocked by:` slug convention doesn't distinguish between three trigger flavors: **landing** (B needs A's changes in the target), **findings** (B was generated by A's findings; can run in parallel), **clarity** (B needs to know what A clarified, satisfied at A's completion regardless of whether outputs land). The slug-shipped default in plugin-behaviour.md is landing-shaped; findings- and clarity-shaped dependencies happen to fire correctly when "ships" means "findings routed," but the convention is ambiguous and category errors are possible. The existing prose-tail condition mechanism (e.g. "Blocked by: [slug] + observed leakage after it ships") is where finer-grained triggers can be encoded. Two options: (1) add a brief note under Dependency ownership naming the three flavors and pointing to the prose tail as the encoding site, (2) trust per-case reasoning. Real example surfaced 1b7d359: [ship-freeform-next-type]'s `Blocked by: [behaviour-agnosticism-audit]` line was clarity-shaped — the audit clarified that the type set was expanding, and that was the unpark trigger, not the audit's findings landing as target changes. Got the call right organically, but a silent default Blocked-by line written without reasoning could land on the wrong trigger.

- **[e2e-install-guide reshape]** Reshape [e2e-install-guide] from a single user-run live-chat E2E into Claude-run stranger-Claude subagent simulations covering multiple user/setup scenarios. Rationale: a single user-run test only catches what one path through the install guide reveals, and routing it to the user is slow and depends on their session capacity. Subagent simulations let Claude play out variants in parallel — different Claude Code states (not installed / installed / installed on free plan), different OSes, different starting confusions ("what's a plugin," "I already have Claude" desktop-app confusion, etc.) — each subagent given the INSTALL.md and a fresh-stranger persona, observing where the guide breaks down. Output is a synthesized findings list, routed back to Captures. /plan to design the scenario set, the subagent prompt shape, and how findings synthesize.

- **[abort-reshape-routing]** /next Step 5 abort-and-requeue handles two things — the batch (return to QUEUE.md) and any captures that surfaced during the attempt (route to Captures as normal). It has no slot for the third thing: the reshape direction or learning that *motivated* the abort. In this session (ada58ef+1) the reshape direction got routed as a capture by judgment call so /plan would pick it up — without that judgment call, the direction would have lived only inside the LOG entry, where /plan doesn't read at planning time, and the batch would have re-presented itself at the next /next unchanged. Possible tightenings: (a) add an explicit sub-step under Step 5 — "if the abort surfaces a reshape direction the queue needs, route it as a capture pointing at the batch slug before recommending /done"; (b) frame the captures sentence more broadly to cover reshape-direction as well as side-findings; (c) accept the judgment-call shape and trust the recap. The (a) tightening is probably right because the trigger is mechanical — abort + batch returned + reshape direction in conversation = capture needed — and the cost of missing it is the same batch re-presenting unchanged.

---

- **The fenced-code-block default for approval-time outputs is right, but the "code" label is wrong.** plugin-behaviour.md's "approval-time outputs go in a fenced code block" rule is sound — the fence is a useful visual device saying "this is a drafted artifact, not discussion content," and the across-the-board treatment keeps the signal uniform. The problem is the desktop app rendering: fenced blocks now show a "code" label at the top, which is semantically wrong when the content is prose (parking reasons, capture wording, batch drafts, LOG entries). Previously fenced blocks rendered unlabelled. Need to find what fence variant or alternative markdown construct the current Claude desktop app supports that preserves the visual demarcation without the misleading label. Surfaced 1b7d359 /plan.

- /plan tried to pass queue-state work onto /next during 7563bc0+1 session: when terseness edits across procedure docs created staleness in batch line refs and quoted strings, Claude filed a capture asking /next to "re-verify line refs and quoted strings at batch-execute time" rather than doing the verification in-place during /plan. User pushed back — /next executes the top batch, it doesn't parse captures or do queue-wide verification, and capture-routing is /plan's job. The misroute pushed thinking work past its proper home. Pattern to prevent: /plan handles queue-wide fixups (cross-batch staleness, line-ref drift, quoted-string updates) while context is fresh, not by filing them as captures for downstream skills to discover. Possible mechanism — add an explicit rule under plan.md ground rules or plugin-behaviour.md that /plan owns queue-wide cleanup at the moment it surfaces; capture is for things /plan genuinely can't resolve now (needs more data, needs design discussion, needs user input). If the fix is "do it now," doing it now is /plan's job.

- Procedure docs grow with each captured bug but the bug-discovery rate doesn't fall — observed across multiple /plan sessions including 7563bc0+1. User's frame: "we describe these things to no end but more and more problems just keep emerging." Two readings: (a) docs format is wrong and a more structured form (tree-stacked prose, hierarchical bullets, diagrams) would compress without losing meaning and reduce mis-reading; (b) the bug-emergence is the captures-as-tests mechanism working, not the docs failing, and reformatting won't change the rate. User's intuition is (a); Claude pushed back toward (b) but the concern is real either way. Worth holding to see if a real fix shape emerges — maybe partial restructuring of genuinely hierarchical sub-step content, maybe a different way of writing rationale that resists over-literal interpretation, maybe an accepted ceiling on what prose can do and a different mechanism takes over (more aggressive simplification cycles, periodic full rewrites instead of accretion). Don't promote until the shape is clearer; this is a capture-and-watch.

- **[user-edits-rollup-on-commit]** The user can edit target-tree files at any time (mid-session, between sessions). Those edits should be detected at the next commit moment, surfaced briefly, and rolled into that commit alongside whatever the session produced — not left in the working tree to be discovered later or to layer wrongly under subsequent edits. The push-and-rezip ritual in CLAUDE.md already does this at push time (step 8 stages every dirty path in plugin/si-plugin/). The gap is /done's per-build commit, which only stages files the build touched. Today's case: 5 docs files have been dirty since at least the c5e32d8 session; an earlier session was told about the edits but still didn't commit them. Fix shape: at /done commit time (and possibly at /next start as a detection point), run `git status --porcelain plugin/si-plugin/`, surface any dirty paths outside the active scope with a one-line summary, and offer to stage + roll them in. Should not be complicated — detect, name, roll in.

- The Step 2 checkpoint sub-step in plan.md ("Offer three options every time, in uniform phrasing: (1) continue, (2) close out, (3) share something else") read as bureaucratic form-fill in the 7563bc0+1 /plan, with each checkpoint rendered as a numbered list. The rule has been in place across multiple /plan sessions where the conversation felt easier — so the issue isn't the rule itself getting stricter, it's that this session pulled toward a literal reading of "uniform phrasing" + numbered options when earlier sessions rendered the same intent conversationally. Two possible fixes, not mutually exclusive: (a) loosen the rule's wording so "uniform" doesn't read as "render the same list every time" — keep the requirement that all three off-ramps are available after every item, drop the prescription of how they're presented; (b) note that this pattern also showed up alongside heavier fenced-block use and more formal sub-step narration in the same session, so the pull may be toward overall procedure-literalism, not just this one rule. Worth holding the capture until the pattern is observed in a second session to know whether it's session-specific or a real drift.

### Parked

- **[narration-vs-menu-drift]** Observed during 1b7d359 /plan: Claude defaulted to menu-style options ("file as capture, drop it, or commit to the rule now?") when narrating a recommendation would have been more appropriate. Dependency ownership's narration rule ("narrate the ordering work" — exercise judgment, recommend) is supposed to catch this. The mechanism failed under exploratory back-and-forth tone — the pull toward "lay out the options" was stronger than the pull toward "state the recommendation, let user push back." Worth watching whether this generalizes: when the conversation gets exploratory, does Claude soften from recommendation-narration into menu-listing? If so, the narration rule needs tightening — possibly explicit text that menu-style enumeration of equally-weighted options is *not* narration when Claude actually has a preference, and the recommendation must come first with the menu as fallback.
  Parked: single observation; watch for recurrence before tightening narration rule.

- **[parked]** Decide whether to add an inline marker for internal-only terms in procedure prose. The marker would let procedure docs flag internal terms inline so the translate-or-omit rule fires mechanically rather than relying on Claude matching against the vocabulary list each time.
  Blocked by: [narration-vocabulary] + observed leakage after it ships

- **[user-execution-batch-shape]** When the user is the executor of a batch (gather these receipts, identify the lender, call the ATO) rather than Claude, the existing build/test/audit shapes don't quite fit. Build batches assume Claude executes; test batches are about verification; audit batches are read-and-route. A user-execution batch sits closest to a test batch in mechanics (user runs steps, Claude facilitates), but it's not verification — it's the primary work. Observed during /setup on a tax-prep folder: queueing batches that were mostly user-action items felt weird, even though step-by-step communication rules in plugin-behaviour.md would handle the running well. Three possible landings: (a) new `User:` subheading alongside Build/Test/Audit, (b) covered by existing types + freeform once shipped, (c) framing-only — "build" means "user does it" in non-coder projects, no new structure. Decision premature without running several user-execution batches first.
  Parked: needs experience running 2-3 user-execution batches in the tax project before the right landing is clear.

- **[freeform-on-demand]** On-demand form of freeform: `/next freeform` with no queued batch required. Trigger case: user has applied (or is about to apply) handmade changes — manual file reorganization, content the user produced outside the chat — and wants Claude to wrap up the work (record in LOG, commit). Use case is more speculative than queue-driven freeform (we can't always name a true prospective trigger in advance), but expected user demand justifies shipping it as a quick-and-dirty path; queue-driven remains the primary safety valve. /plan-side discipline gate still applies in spirit — Claude asks at /next freeform time "could this be build, test, or audit?" before defaulting. The captures-append constraint applies here too (see [ship-freeform-next-type]). Rides alongside [ship-freeform-next-type] rather than replacing it; both unpark together.
  Blocked by: [ship-freeform-next-type]

- **[ship-freeform-next-type]** Add a fourth /next type — freeform — for sessions that don't fit build/test/audit. Two forms coexist: **queue-driven** (planned freeform work, /plan scopes it as a batch, /next picks it up) and **on-demand** (`/next freeform` with no queued batch; see [freeform-on-demand]). Queue-driven is the primary safety valve — it exists so users don't suffer when the session type they need hasn't been recognized as its own type yet; better to ship freeform than block on type design. The expectation is that recurring freeform use cases will surface real new types over time (the audit type emerged this way). Both forms apply the same /plan-side or /next-side discipline gate: "could this be build, test, or audit?" before allowing freeform; require a one-line statement of why none fit. **Captures-append constraint (both forms):** when freeform contents would yield captures (test outcomes, feature ideas, changes to the system being built itself, anything needing /plan-side routing — as opposed to records or content destined for the project's own artifacts), Claude warns the user that /next can only append to Captures, not process them. Offer the choice: abort the freeform session and present the findings in /plan instead (where they'll be processed properly), or continue knowing further processing will have to happen in a later /plan. This protects against silently misrouting work that should have entered through /plan.
  Parked: shape worked out 7563bc0; deferred until ready to commit to procedure-doc edits across setup/plan/next/done.

- **[parked: behind reader-test-refresh]** FAQ edit: incorporate the four functions of _build.md as an entry for users who wonder what _build.md does. The four functions: (1) carries the active batch's working state out of QUEUE.md, which is read-only during builds; (2) feeds the pre_tool_use scope-lock hook (which files this build may touch); (3) holds crash-recovery tick state so resumed sessions don't re-derive from a partial commit; (4) carries rationale prose forward into /done's LOG entry.
  Blocked by: [reader-test-refresh] + its findings routed — those findings may shape what belongs in the FAQ and how it's worded.

- Add scenarios to reader-test-workflow.js — evaluate which scenarios are still undertested and worth adding. Known blind spots regardless of refresh outcome: /setup interview (untested), push-and-rezip sweep (untested — lives in this project's CLAUDE.md, not plugin docs, so coverage question is whether it should even be in scope for plugin reader-tests), mid-build resume from a real _build.md (current next.md sim covers fresh /next, not resume), /done plan-mode close-out (current sim only covers build close-out), empty-queue handling, audit-batch flow (planning-as-work). Promote as one or more build batches once scenarios are picked.
  Blocked by: [reader-test-refresh] + refreshed workflow run once — the refreshed first run may surface blind spots not on this list, or may show that scenario count matters less than scenario specificity.

- Batch cohesion ordering heuristic — the build log as decision log creates pressure for discrete builds, and batch ceremony is friction for users. Queue ordering rule: builds touching an area with no related batches yet should sink (absent urgency or dependency), giving time for more captures to accumulate and make the batch worthwhile. Batching also touches context window management, not just coherent logging — Claude needs to think about one area of related concerns at a time. (The companion /next-time check — recommend switching to /plan if related captures exist for the top batch — shipped as the next.md blocker-gate capture scan.)
  Parked: needs design work to sharpen "no friends" and "related" into a mechanical rule.

- Cruise control skill — a skill that runs build→commit→build→commit through a batch (or multiple batches) unattended, stopping only when it hits something requiring user input. Key design concerns: (1) wording that doesn't pressure Claude to push through uncertainty, (2) dependency management when Claude decides when to wrap a batch, (3) /done judgment steps can't get skipped for speed.
  Parked: depends on stabilizing the skills it would chain — no fixed trigger, conscious revisit only.

- **[self-hosting-support-during-setup]** Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping, **and the dependency-management discipline** (host-vs-target distinction as it governs batch ordering, the host-side-after-push-marker rule, the `--- Push required before continuing ---` queue convention, and the `(host-side)` annotation on `Depends on:`). All of this carries into the new project's CLAUDE.md. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
  Parked: scoping unclear — interview question vs separate skill vs scaffolded template.

- /done spec check — after writing the **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. Retrospective check (at decision time) vs the current /plan pipeline gate (prospective, at planning time).
  Parked: both mechanisms need more real usage before deciding how they relate.

- Threshold-based context management — if hooks ever gain token usage fields (e.g. `context_usage_pct`), the plugin could recommend `/compact` or `/clear` based on actual utilization instead of rule-based triggers. Research filed at resources/research/context-window-hook-access.md.
  Blocked by: Anthropic adding token data to hook event input — external trigger, no slug.

- Pre-push sweep could be lighter if /done flagged host-side impacts at build time — accumulate a manifest of "this change affects X in project docs" during /done while context is fresh, then the push sweep checks flagged spots instead of re-reading everything. Sweep stays as safety net but gets cheaper.
  Parked: design question about cross-build staleness (build 3 invalidates something build 1 touched) still needs the sweep to catch it — unresolved.
