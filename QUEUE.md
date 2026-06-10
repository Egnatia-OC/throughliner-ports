# QUEUE

## Batches

Worked top to bottom. Each batch of changes or tests is one /next session of either type:

- build session where changes are applied, then claude runs all tests it is able to do itself
- test session where the user runs any testing only they can do

**Narrate _build.md's purpose at the moments it's created and consulted** **[narrate-build-md-purpose]**
Depends on: [done-closeout-extraction]

_build.md isn't a passive marker; it carries the active batch's working state out of QUEUE.md (which is read-only during builds), feeds the pre_tool_use scope-lock hook, holds crash-recovery tick state, and carries rationale prose forward to /done's LOG entry. None of that is visible in the procedure docs today, so the file reads as bookkeeping or vestigial overhead. Other parts of the system narrate their value as they're invoked (dependency ownership narration, ordering reasoning, unpark surfacing); _build.md should follow the same pattern. All narration here must be [BRIEF] — one short sentence per location, not paragraphs. The point is visibility, not explanation.

Build:
- next.md: at the step where _build.md is created, add a [BRIEF] narration line stating what _build.md is for, in the user-facing terms above (working surface, scope-lock data, crash-recovery state, rationale carrier into /done).
- next.md: at the resume path (active _build.md detected at session_start), add a [BRIEF] narration line stating what's being read and why.
- done-build.md (post-[done-closeout-extraction]): at the step where _build.md is consumed and removed, add a [BRIEF] narration line stating the rationale is being re-authored from _build.md into the LOG entry.
- All three additions must be [BRIEF]. One sentence each, no paragraphs. The point is visibility, not explanation.

Test:
- Self-verifying on the next /next + /done cycle. The narration either appears at the right moments or it doesn't.

--- Push required before continuing ---

**Output tag overhaul audit: prose where a response-shape tag belongs** **[output-tag-audit]**

The procedure docs were authored before the response-shape tag system was fully in place, so some steps still describe output behaviour in prose where a tag ([SILENT], [BRIEF], [PROMPT], [DISCUSS], [SEQUENCE]) would compress the intent and apply uniformly. Prose substitutes are easy to misread and drift across docs; tags are the canonical mechanism. One known finding to seed the audit: _build.md entry ticking in next.md should be [SILENT] (crash-recovery bookkeeping, not a status report).

Audit:
- Target: setup.md, plan.md, next.md, next-build.md, next-test.md, next-audit.md, done.md
- Criteria: any step whose prose describes verbosity or interaction shape (e.g. "say nothing," "briefly note," "ask the user," "discuss tradeoffs," "one at a time") where the matching tag would carry the same intent more cleanly. Also flag tag misuse — a tag applied where the step's prose contradicts it, or a tag missing where the step's behaviour clearly needs one. For each finding: quote the prose, name the candidate tag, note whether replacement is full (tag alone) or partial (tag + retained prose).

**In-scope / out-of-scope distinction audit** **[scope-distinction-audit]**

The in-scope vs out-of-scope distinction shows up across plan.md, next.md, and plugin-behaviour.md — it governs what enters the active build, what gets noted for later, and what halts the build for scope renegotiation. The concern is whether the distinction is stated explicitly enough to be followed mechanically, or whether it currently rides on Claude's judgment without an anchor doc. If the latter, drift is invisible until a build accidentally absorbs something it shouldn't have or stops for something it should have just queued.

Audit:
- Target: plan.md, next.md, next-build.md, next-test.md, plugin-behaviour.md
- Criteria: every passage that turns on "in scope" or "out of scope" (or synonyms — within scope, scope creep, beyond scope, the active batch's scope). For each: is the distinction defined where it's used, or assumed? Are the rules for routing out-of-scope discoveries (Captures vs halt-and-ask vs silently skip) consistent across docs? Is there a single canonical statement of what scope means in this system, or is it scattered? For each finding: quote the passage, name what's load-bearing on judgment, propose either a wording tightening or a single anchor location.

**Audit close-out recommendations across all four skills** **[close-out-audit]**
Blocks: [next-done-recommendation]

Across /setup, /plan, /next, /done, the close-out step recommends what to run next — but the shape varies skill-to-skill and the recommendations may not be consistent. Known incongruences: setup.md Step 4 unconditionally offers /next even when Q4 may not have produced a usable first batch; [next-done-recommendation] tackles /next-recommended-instead-of-/done at build completion, but that's one observed instance, not a full survey. Running the audit first means [next-done-recommendation]'s scope may shrink, expand, or be absorbed entirely — better to know before that batch is built. Findings route to Captures per the audit-batch contract; no direct edits.

Audit:
- Target: the close-out step in each of setup.md, plan.md, next.md, done.md (the final "tell the user what to run next" block in each).
- Criteria: (a) what next-skill does the close-out recommend? (b) is the recommendation unconditional, or gated on actual produced state (e.g. "only offer /next if a batch exists")? (c) is the recommendation shape consistent across the four skills, or does each skill recommend differently? (d) does any close-out implicitly recommend re-running itself, or branching to a non-immediate-next skill? (e) does the commit-and-push prompt make sense for every session shape? /plan sessions update local planning state only — pushing them treats planning work as a ship event, which it isn't. /next sessions ship plugin changes (after the push-and-rezip ritual elsewhere). Survey whether the commit-and-push offer fits each skill's actual semantics, and propose tightening (e.g. /done after /plan offers commit only; push is reserved for the rezip flow). For each finding: quote the passage, name the incongruence or gap, propose a tightening (or note that the existing wording is correct and consistent).

**Tighten Claude's completion recommendation: always /done, never /next** **[next-done-recommendation]**
Blocked by: [close-out-audit]

next-build.md's Completion section says "Run /done to record this and commit, or tighten what's already built before closing" — but Claude has been observed recommending /next instead at completion, while still inside the just-finished /next session. The mechanical safety net catches the worst case (session_start detects _build.md and routes the next /next to resume, not a fresh build) so dual builds don't actually start — but the missed /done still costs a LOG entry and a commit for the batch that just finished. The fix isn't a wording change at Step 7; the doc says the right thing already. It's tightening whatever lets Claude substitute /next for /done at completion — likely an explicit rule near "one build at a time" in plugin-behaviour.md, since that's the same principle in different framing.

Build:
- plugin-behaviour.md: add a rule near the "one build at a time" bullet stating that at build completion the only valid next-step recommendation is /done — never /next, never another build skill. Frame as the completion counterpart to "one build at a time."
- next-build.md Completion section: consider whether the close-out wording needs a [SEQUENCE] or [BRIEF] tag to reinforce that the close-out recommendation is the one place /done must be named explicitly. Apply the tag if it adds clarity; skip if the new plugin-behaviour.md rule covers it.

Test:
- Self-verifying from the rule text. No separate verification entry.

**Change LOG file boundary from per-release to per-entry** **[drop-log-per-release-split]**

The per-release log file split (log.md → log-v<VERSION>.md at each push) uses an arbitrary boundary — version groupings aren't load-bearing on any retrieve, and design threads span releases. But collapsing to one growing log.md only removes the split without improving retrieve — you still grep within the file to find an entry. The right fix is matching the file boundary to the logical boundary: each LOG entry gets its own file, so retrieve goes from index → hash → direct file open, no grep step. Entries are already per-commit; files should match. The per-commit alternative was considered in the f123eed discussion but not preserved in the LOG — this is the decision that session should have reached.

Build:
- Decide naming scheme for per-entry files. Slug-based (LOG/trickle-up-audit.md, LOG/plan-2026-06-09.md for sessions without a batch slug) avoids the hash-not-known-at-write-time problem and keeps filenames readable. Hash stays in file content + index.
- plugin/si-plugin/docs/done.md (or per-skill close-outs if [done-closeout-extraction] has landed): write each LOG entry as its own file under LOG/ instead of appending to log.md.
- plugin/si-plugin/docs/plugin-behaviour.md: update why-pipeline retrieve rule — "search LOG/index.md, then open the matched entry's file directly."
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md: update LOG/ description to reflect per-entry files. Remove "this file covers the current release" framing.
- plugin/si-plugin/skills/setup/, plan/, next/, done/ procedure docs: grep for log-v*.md, single-log-file, and per-release references; revise to describe per-entry files.
- This project's CLAUDE.md (host-only): remove steps 3–4 from push-and-rezip (push marker in log entry and cap-and-rename ritual). Add a note that existing log.md and log-v*.md files stay in place — index references work by hash, so old entries remain findable.

Test:
- Self-verifying from doc edits.
- After the next push: ask Claude a "why did we decide X" question targeting an entry in an old log-v*.md file. Verify retrieve still works through index + grep fallback for pre-migration entries.

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
- plugin/si-plugin/docs/next-audit.md intro (line 3): lead with the output contract, then describe the procedure shape (read-many-propose-many). Name target variety explicitly — procedure docs, user's spec, code, UI flows, workflow output, any other artifact — so the procedure reads as generic, not docs-specific.
- plugin/si-plugin/docs/next-audit.md Read the target section (line 7): change "Open every file named by the target" to "Read every artifact named by the target" so the procedure language doesn't assume files. Keep the criterion-pass-by-pass instruction — that generalizes cleanly.
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

**Use semantic content-type labels on approval-time fenced blocks** **[fenced-block-content-type-label]**

The "approval-time outputs go in a fenced code block" rule in plugin-behaviour.md leaves the fence's language slot unspecified, which causes the desktop app to render every approval-time block with a literal "code" label — semantically wrong over prose (parking reasons, capture wording, batch drafts, LOG entries, commit messages). The fence itself is the right visual device; the label just needs to name the content. Fix is to extend the rule: the language slot carries a short content-type tag (parking-reason, capture-draft, batch-draft, commit-message, log-entry, etc.) so the rendered label says what's actually inside. Confirmed live in the desktop app — a custom tag after the backticks renders verbatim as the block's label.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md "approval-time outputs go in a fenced code block" rule: extend with the requirement that the language slot carries a short content-type tag matching the approval-time output, and list the canonical tags (parking-reason, capture-draft, batch-draft, commit-message, log-entry, anything else surfaced while drafting).
- plugin/si-plugin/docs/plan.md and done.md: sweep approval-time references that show example outputs in fences and add the content-type tag where missing.

Test:
- Self-verifying from doc text on the next /plan or /done run — approval-time blocks render with semantic labels rather than "code."

**/plan resolves what it can; capture is only for what it can't** **[plan-resolves-by-default]**

/plan has twice (observed) deferred work it could have done in-session: once by filing a capture asking /next to re-verify line refs and quoted strings after terseness edits, once by recommending park-with-"research needed" on the fenced-block label question that /plan itself was the right home for. Both were misroutes — /next executes the top batch and doesn't parse captures; "research needed" is the same skill-self-deferral. The pattern: when work is resolvable now and /plan is the home for that kind of work, doing it now is /plan's job. Capture is reserved for things /plan genuinely can't resolve in-session — needs more data than the session has, needs design discussion across sessions, needs user input not yet available, or surfaces a structural question whose answer would gate the work. Adding the rule to plan.md ground rules names it explicitly so the default flips from defer-via-capture to resolve-now.

Build:
- plugin/si-plugin/docs/plan.md ground rules: add a bullet stating /plan resolves what it can in-session — research, queue-wide cleanup (line-ref drift, quoted-string staleness after sweeps), cross-batch reconciliation, doc verification, anything else within /plan's reach. Capture is for things /plan genuinely can't resolve: needs data, needs design discussion, needs user input, surfaces a structural question that would gate the work. Frame the rule as a default, not an absolute — the test is "can /plan resolve this with what it has right now."

Test:
- Self-verifying from doc text on the next /plan run where a resolvable-now item surfaces. Claude should do the work in-session instead of filing it as a capture.

**Detect and roll in user edits at /done commit time** **[user-edits-rollup-on-commit]**

User-made edits to target-tree files (plugin/si-plugin/) can happen at any time — mid-session, between sessions — but /done's per-build commit only stages files the build touched. Those edits sit dirty across sessions until the push-and-rezip ritual catches them at push time. Observed: 5 docs files stayed dirty across at least two sessions. The gap is /done's commit, which is the natural moment to detect and offer to include them. The push-and-rezip sweep stays as the safety net; this adds an earlier catch point.

Build:
- plugin/si-plugin/docs/done.md: at the commit step, add a sub-step — run `git status --porcelain plugin/si-plugin/`, compare against the active build's file list, surface any dirty paths outside scope with a one-line summary, and offer to stage + roll them into the commit.

**Loosen checkpoint wording: off-ramps available, not identically phrased** **[checkpoint-wording-loosen]**

The plan.md Step 2 checkpoint rule ("Offer three options every time, in uniform phrasing") pulls Claude toward rendering a numbered list at every checkpoint, which reads as bureaucratic form-fill. Observed across multiple /plan sessions — not a one-off. The rule's intent is sound (all three off-ramps available after every item), but "uniform phrasing" is being read as "identical wording each time." Loosening the wording so the three options must be available but can be delivered conversationally fixes the robotic delivery without losing the guarantee.

Build:
- plugin/si-plugin/docs/plan.md Step 2 sub-step 6 (Checkpoint): reword so the three off-ramps (continue to next, close out, share something else) are required to be available after every item, but drop "uniform phrasing" — conversational delivery that covers all three is fine.

**Add forced app-identification check to INSTALL.md routing** **[install-app-identification-check]**

The Claude Code / Claude chat app distinction is load-bearing for install routing but stated in one sentence inside Q2 that the desktop-app-confused persona read straight past. Result: confident misroute to Branch B, crash at a Customise menu hunt with no recovery path — the helping Claude would troubleshoot the missing menu rather than diagnose wrong-app. A screenshot or icon comparison goes stale; a forced positive identification check ("what does the title bar say?" or "does the window have a terminal-style input or a chat interface?") is self-correcting and version-independent. The check must happen before routing, not after — catching wrong-app after Branch B starts is too late.

Build:
- INSTALL.md Q2 section: replace or augment the current one-sentence distinction with a forced identification step — the user must report what they see (title bar text, interface description, or similar) before the guide routes them to Branch A or B.
- Add a wrong-app recovery path: if the identification check reveals the chat app, tell the user what Claude Code is and where to get it, then route to Branch A.
- Remove the "check Applications folder" hint that assumes the user can distinguish two Claude apps by name alone.

**Move AI-facing content out of the human's reading path in INSTALL.md** **[install-separate-ai-instructions]**
Depends on: [install-app-identification-check]

INSTALL.md opens with a "Note to Claude" block and closes with pacing rules — both AI-facing, both in positions the human reader hits first or last. Four out of four test personas bounced off the opening block. The guide is designed to be pasted into a Claude chat, so both human and AI content must stay in one file — but the AI content should be out of the human's natural reading path. Fix: restructure so human-readable content (what this is, who it's for, what to expect) opens the file; AI-facing instructions move to a clearly-marked section the human can skip. Folded in from [install-no-bypass-for-experienced-users]: the already-installed persona abandons the walkthrough at Step 1 — the three-question interview is dead weight for someone with Claude Code, a paid plan, and prior plugin experience — so the new introduction also carries an experienced-user bypass.

Build:
- INSTALL.md: move the "Note to Claude" frontmatter and the pacing rules block into a single clearly-marked AI-facing section (e.g., at the end of the file, or in a collapsed block with a "skip this" label).
- INSTALL.md: add a brief human-facing introduction at the top — what the guide is, who it's for, what to expect from the walkthrough.
- INSTALL.md: include an experienced-user bypass line in the introduction — "already have Claude Code and a paid plan?" — pointing via in-page anchor to the identification check, and Branch B beyond it. The bypass skips the interview, never the app-identification check.
- Verify the restructured guide still works when pasted into a Claude chat: Claude must still find and follow the AI instructions despite their new position.

**Surface paid-plan requirement before INSTALL.md interview** **[install-paid-plan-upfront]**

The paid-plan requirement (Pro minimum) is introduced at Q3 of the install interview with no preamble. Cold-stranger persona left to google pricing and didn't come back; free-plan persona hit it as a contradiction of lived experience. "Pay-as-you-go API credit" reads as uncapped to non-coders; plan limits aren't stated. Moving the requirement before Q1 turns it into an informed-consent gate — users who can't or won't pay learn that immediately instead of three questions in.

Build:
- INSTALL.md: add a brief upfront section before Q1 stating that a paid Claude Pro plan is required (not Max — Pro is sufficient), with a pointer to Anthropic's pricing page rather than an embedded dollar figure.
- INSTALL.md: remove or rewrite Q3's current paid-plan discovery so it doesn't re-ask what the upfront section already established. If Q3 serves a routing purpose beyond the paywall check, keep the routing and drop the discovery.
- INSTALL.md: clarify what "within plan limits" means in plain language — what happens when you hit the limit, is it a hard stop or a throttle.
- INSTALL.md Step 1 routing: replace "no paid plan" with "free plan or no plan" (or equivalent unambiguous phrasing) so free-plan users don't self-route past the paywall gate. If the upfront section makes this routing line redundant, remove it.

**Clarify plugin upload path and drop hedge in INSTALL.md** **[install-upload-path-clarity]**

All four test personas stalled at the plugin upload step. The UI path (Customise → + → Create a plugin → browse for .zip) is correct but "Create a plugin" reads as authoring, not installing — three personas hesitated or bailed. The guide's hedge "usually in the top menu or settings area" signals uncertainty and erodes trust. The path is known; the label is counterintuitive. Fix: state the path confidently, warn that "Create a plugin" is the upload path despite the name, add a screenshot, drop the hedge.

Build:
- INSTALL.md: replace the current breadcrumb with the confirmed path — Customise (top left) → + icon on the left → "Create a plugin" → browse and select the downloaded .zip. Drop "usually in the top menu or settings area."
- INSTALL.md: add a one-line heads-up before the "Create a plugin" step that the label is misleading — it's the upload/install path, not an authoring tool.
- INSTALL.md: add a screenshot of the Plugins screen showing the + icon and the "Create a plugin" option, so users can visually confirm they're in the right place.

**Add provenance and download expectation to INSTALL.md GitHub link** **[install-download-provenance]**

The raw GitHub URL for downloading si-plugin.zip triggered suspicion across all four test personas — "FlintCraftTech" doesn't match "Sovereign Implementer," the URL looks like an unknown-sender zip download, and nothing tells the user what happens when they click. Fix: add a one-line provenance statement (FlintCraftTech is the publisher account, Sovereign Implementer is the plugin) and tell the user what to expect (file auto-downloads as si-plugin.zip, or right-click > Save As if it opens in the browser).

Build:
- INSTALL.md: add a provenance line immediately before or after the download URL explaining the name mismatch and confirming it's the official source.
- INSTALL.md: add a one-line expectation — what happens when you click (auto-download as si-plugin.zip), and what to do if it doesn't (right-click > Save As).

**Define "open a project folder" action in INSTALL.md smoke test** **[install-define-open-folder]**

The install guide tells the user to "open a project folder in Claude Code" without defining what that means or what the physical action is. CS doesn't know if they need a special folder or what "open" looks like in the app. The install guide's job ends at "plugin works" — the smoke test just needs any folder open, not a real project. Defining project setup belongs in /setup. Fix: replace "open a project folder" with a concrete action for the smoke test context, and defer real project setup to /setup.

Build:
- INSTALL.md Step B.5 and Step 2: replace "open a project folder in Claude Code" with a concrete instruction — create an empty folder, then open it in Claude Code via File > Open Folder (or whatever the current action is). Frame it as a smoke-test step, not project setup.
- INSTALL.md: add a one-line note that /setup handles real project setup once the plugin is confirmed working.

**Specify the /setup smoke test in INSTALL.md: success signal, failure signal, diagnostics before uninstall** **[install-setup-smoke-test-underspecified]**

The "type /setup" smoke test doesn't say where to type, whether to press Enter, what success looks like, or what failure looks like — the cold-stranger and free-plan personas both stalled there, and the current failure path jumps straight to gear-icon > Uninstall before ruling anything else out. One wrinkle from discussion: plugin skills can render namespaced in the command menu (this project's sessions run /sovereign-implementer:plan, not bare /plan), so a guide that says "/setup should appear" may strand a reader looking at a differently-labelled entry — the success signal must match what the menu literally shows.

Build:
- INSTALL.md smoke-test step: rewrite the "type /setup" instruction to name where to type (the chat box), that a menu of commands appears as you type, which entry to look for, and that Enter runs it. Before writing the success signal, ask the user to confirm the exact menu rendering in the current desktop app (bare /setup vs namespaced form); write it to match.
- INSTALL.md smoke-test step: describe the failure signal explicitly — what the reader sees when the plugin isn't registered (no matching entry appears as they type).
- INSTALL.md failure path: replace the jump-to-uninstall with a diagnostic ladder — (1) check the plugin is present and enabled in the Customise plugin list, (2) start a fresh session, since skills register at session start and a pre-install session won't see them, (3) uninstall and reinstall as the last resort.

**INSTALL.md endings polish: collapse "Updating later", add an end-of-guide close** **[install-updating-later-section-is-padding]**
Depends on: [install-separate-ai-instructions]

The "Updating later" section repeats the install steps the reader just finished — uninstall, download, repeat — and the already-installed persona registered it as trust-eroding padding. A one-liner that points back at the steps instead of restating them carries the same information without the filler, and stays correct when the download and upload wording changes under the other install batches. Folded in from [install-step2-trailing-ellipsis-reads-as-truncated]: the free-plan persona read the Step 2 First-run pointer's trailing prose and was unsure whether the guide had been cut off — an explicit close line marks the end of the human path, which after [install-separate-ai-instructions] sits just before the skippable AI-facing section rather than at the literal bottom of the file.

Build:
- INSTALL.md "Updating later" section: collapse to a single line — "To update: uninstall via the gear icon, download the latest zip from the same URL, and repeat the upload."
- INSTALL.md: add a one-line close at the end of the human reading path — "That's the end of the install guide — your friend's project is now ready to start" — placed just before the AI-facing section once the restructure has moved it to the back.

**Preserve rejected-alternative reasoning in LOG entries** **[log-rejected-alternative-reasoning]**
Depends on: [done-closeout-extraction]

Observed at f123eed: a /plan discussed and resolved a concern about one growing log.md getting too large to read, but the LOG entry recorded only the conclusion — not the concern or the reasoning that addressed it. Two sessions later the user couldn't retrieve why the alternative was rejected and second-guessed the decision, and the log-split design got relitigated. The why-pipeline's preserve rule carries rationale forward, but "rationale" currently means the reasoning behind the decision made, not the reasoning against the alternatives considered. The trigger needs a boundary so entries don't bloat: discussion-level consideration qualifies — a concern raised and resolved, an alternative seriously weighed — passing mentions don't. The intuitive-but-rejected path is the case that most needs preserving.

Build:
- plugin-behaviour.md why-pipeline Preserve rule: extend the definition of rationale to include concerns raised and resolved and alternatives seriously weighed, carried with why they lost. State the trigger boundary: discussion-level consideration qualifies, passing mentions don't, and decisions where the rejected path is the intuitive one always qualify.
- The LOG-entry-writing step in the /done per-type sub-docs (post-[done-closeout-extraction] shape): add one reinforcing check at writing time — does this entry carry any concern that was resolved or alternative that was weighed? Keep it to a single line pointing at the why-pipeline rule; don't restate the rule per sub-doc.

### Parked

- **[sizing-gates-rework]** Sizing gates rework — research filed at resources/research/batch-sizing-research.md.
  Parked: further research needed on session-length as a mid-build split indicator before the rework is actionable.
  Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session. Processed captures (slug assigned, dependencies scanned) sit above the `---` divider; unprocessed raw captures collect below. See plan.md Capture and parking discipline.

- **[trickle-up-next-md-duplicates]** next.md and the per-type docs restate 4 rules already in plugin-behaviour.md — SPEC read-only (next-build.md:38, next-test.md:23 = pb:86), don't fix outside scope (next-build.md:39 = pb:84), state regressions plainly (next-build.md:40, next-test.md:24 = pb:9), one build at a time (next.md:67 = pb:87). Wording has already drifted slightly between copies. Remove the duplicates from next.md and the per-type docs; the non-duplicated rules in those sections stay (scope expansion ask and REGISTRY not build scope in next-build.md; entries are the contract and per-entry ticking in next.md).

- **[trickle-up-setup-md-no-jargon]** setup.md restates "plain language, no jargon" from plugin-behaviour.md — "Use the user's language — don't rephrase into jargon" (line 139 = pb:7). The universal rule already covers the interview case. Remove from setup.md.

- **[trickle-up-hash-backfill-duplication]** LOG hash backfill procedure is duplicated word-for-word in plan.md (line 30) and next.md (line 9). Not a rule — a mechanical procedure — so plugin-behaviour.md isn't the target. Duplication means both docs need updating when the procedure changes.
  Blocked by: [log-hash-backfill-in-done] — that batch consolidates the backfill into done.md, removing both copies. If it lands as designed, this finding is resolved as a side effect.

- **[trickle-up-ask-when-unsure]** next.md line 70 ("Unsure about an implementation choice? Ask. Don't guess and build wrong.") is universal but has no equivalent in plugin-behaviour.md. Applies to every skill — /plan ordering calls, /setup scaffolding choices, /done routing decisions. Add a generalized version to plugin-behaviour.md Communication ("When uncertain, ask. Don't guess and proceed." or similar), then remove the next.md copy.

- **[setup-registry-template-and-noun]** setup.md REGISTRY.md template (lines 78–82, scaffolded into user's REGISTRY.md) assumes projects have "components" (software-architecture term) and that builds are the only thing that adds to the registry: "Components that exist in this project. Updated after each build." A tax-prep project might register a receipts folder, a lender list, a year-end packet — not components, and entered via audit or freeform work, not builds. Proposal: add a Q3.5-style interview prompt — "what are this project's parts called?" — and use the user's own noun in the scaffolded REGISTRY.md. Decouple the update trigger from "build" too ("Updated as the project grows" or similar). Held out of the project-agnosticism sweep — the Q3.5 proposal adds a new interview question, not just a reword; deserves its own consideration. From [behaviour-agnosticism-audit].

- **[spec-entry-trigger-rethink]** plugin-behaviour.md line 83 spec-entry pipeline assumes the project ships features to an external user: "New features need a spec entry before a build entry. … Threshold: if a user would see or experience the difference, update SPEC.md first." For a personal records-keeping or tax-prep project there are no "features" and the owner is the only "user." Reword project-agnostic — replace "new features" with something like "new scope items" or "new project properties," and broaden the threshold ("if the project's output or shape changes in a way someone would notice"). Needs further thinking — the noun "features" is load-bearing (it names what triggers a spec entry) and the audience for "noticeable" differs by project: for owner-only projects the audience is the owner themselves ("you would notice"), for external-user projects it's a third party ("someone would notice"). A clean reword has to capture both shapes — or the rule splits per project type. Not a one-shot reword; held out of the project-agnosticism sweep. From [behaviour-agnosticism-audit].

- **[plugin-behaviour-doc-routing-agnostic]** plugin-behaviour.md line 81 doc routing assumes the project is a product made of components: "SPEC.md = what/who/how/why the product exists. … REGISTRY.md = what components exist." A records-keeping or tax-prep project has neither — it has organised material, not a product with parts. Reword project-agnostic, e.g. "what/who/how/why the project exists" and a neutral noun for the project's constituent things (parts? entries? items?), or demote per-project-type. The "product" → "project" reword is mechanical; the "components" → ? noun decision is the same problem as [setup-registry-template-and-noun] in a second location.
  Blocked by: [setup-registry-template-and-noun] — inherits whichever noun strategy that batch decides on (Q3.5 user-supplied noun vs neutral fallback). From [behaviour-agnosticism-audit].

- **[blocked-by-trigger-flavors]** Dependency ownership's `Blocked by:` slug convention doesn't distinguish between three trigger flavors: **landing** (B needs A's changes in the target), **findings** (B was generated by A's findings; can run in parallel), **clarity** (B needs to know what A clarified, satisfied at A's completion regardless of whether outputs land). The slug-shipped default in plugin-behaviour.md is landing-shaped; findings- and clarity-shaped dependencies happen to fire correctly when "ships" means "findings routed," but the convention is ambiguous and category errors are possible. The existing prose-tail condition mechanism (e.g. "Blocked by: [slug] + observed leakage after it ships") is where finer-grained triggers can be encoded. Two options: (1) add a brief note under Dependency ownership naming the three flavors and pointing to the prose tail as the encoding site, (2) trust per-case reasoning. Real example surfaced 1b7d359: [ship-freeform-next-type]'s `Blocked by: [behaviour-agnosticism-audit]` line was clarity-shaped — the audit clarified that the type set was expanding, and that was the unpark trigger, not the audit's findings landing as target changes. Got the call right organically, but a silent default Blocked-by line written without reasoning could land on the wrong trigger.

- **[e2e-install-guide reshape]** Reshape [e2e-install-guide] from a single user-run live-chat E2E into Claude-run stranger-Claude subagent simulations covering multiple user/setup scenarios. Rationale: a single user-run test only catches what one path through the install guide reveals, and routing it to the user is slow and depends on their session capacity. Subagent simulations let Claude play out variants in parallel — different Claude Code states (not installed / installed / installed on free plan), different OSes, different starting confusions ("what's a plugin," "I already have Claude" desktop-app confusion, etc.) — each subagent given the INSTALL.md and a fresh-stranger persona, observing where the guide breaks down. Output is a synthesized findings list, routed back to Captures. /plan to design the scenario set, the subagent prompt shape, and how findings synthesize.

- **[faq-build-md-functions]** FAQ edit: incorporate the four functions of _build.md as an entry for users who wonder what _build.md does. The four functions: (1) carries the active batch's working state out of QUEUE.md, which is read-only during builds; (2) feeds the pre_tool_use scope-lock hook (which files this build may touch); (3) holds crash-recovery tick state so resumed sessions don't re-derive from a partial commit; (4) carries rationale prose forward into /done's LOG entry.

- **[abort-reshape-routing]** /next Step 5 abort-and-requeue handles two things — the batch (return to QUEUE.md) and any captures that surfaced during the attempt (route to Captures as normal). It has no slot for the third thing: the reshape direction or learning that *motivated* the abort. In this session (ada58ef+1) the reshape direction got routed as a capture by judgment call so /plan would pick it up — without that judgment call, the direction would have lived only inside the LOG entry, where /plan doesn't read at planning time, and the batch would have re-presented itself at the next /next unchanged. Possible tightenings: (a) add an explicit sub-step under Step 5 — "if the abort surfaces a reshape direction the queue needs, route it as a capture pointing at the batch slug before recommending /done"; (b) frame the captures sentence more broadly to cover reshape-direction as well as side-findings; (c) accept the judgment-call shape and trust the recap. The (a) tightening is probably right because the trigger is mechanical — abort + batch returned + reshape direction in conversation = capture needed — and the cost of missing it is the same batch re-presenting unchanged.

---







- Procedure docs don't explicitly require an approval ask after showing a draft. plan.md Step 2 sub-step 4 says "Don't write to QUEUE.md until approved" and the approval-time-outputs rule in plugin-behaviour.md says to show drafts in fenced blocks — but neither says "ask for approval." The ask is implied, not stated. Observed across multiple /plan sessions: Claude shows the draft, then goes silent, leaving the user to figure out what to do. Fix shape: add an explicit instruction (or [PROMPT] tag) at the draft-showing moment requiring a follow-up ask.

- **Research isn't being filed unless the user explicitly asks.** plugin-behaviour.md says "File research under `resources/research/`," but observed across sessions: when Claude does a web search or works through external facts mid-conversation, the findings stay in chat and never land as a file. The conclusion gets used in the moment, then evaporates. Next session it's gone, and the next /plan that hits the same question redoes the work (or offers to, like just now on the fenced-block "code" label question — research had been done, but I couldn't find it because it wasn't filed). Fix shape: file research as a `resources/research/<topic>.md` note by default whenever a web search or external lookup yields a non-trivial finding, not only when the user asks. Surfaced 0b77f78+1 /plan.

- /next's abort path (Step 5) tells the user to run /done after an abort, but only for aborts that happen after scope-lock (when _build.md exists). When /next aborts before scope-lock — as happened with [plugin-behaviour-walkthrough-1], which was caught at pre-flight — there's no _build.md, no batch was removed from the queue, and the session still produced work (hash backfill, captures filed) that needs committing. The observed behaviour: Claude said "Run /plan" instead of "Run /done," skipping the commit step entirely. The gap is that /next has no abort path for pre-scope-lock aborts. Fix shape: add a pre-scope-lock abort step that routes to /done (for the commit) before /plan, or at minimum names /done as the next step so the session's work gets recorded.

- Skill docs are user-message priority, not system-prompt priority — the built-in system prompt outranks them on verbosity and tone. This is the architectural reason [SILENT], [BRIEF], and the response-shape tag system don't hold on 4.7/4.8: the tags compete with helpfulness training and lose. Six techniques from Anthropic's own docs could close the gap: (1) move mechanical enforcement to hooks (deterministic, can't be skipped), (2) add "why" context to behavioral tags so compliance aligns with helpfulness instead of fighting it, (3) use positive quantified constraints ("output zero text") over abstract ones ("be silent"), (4) explicit scope statements on rules that apply throughout, (5) keep skill docs under 500 lines with progressive disclosure, (6) verify effort level (xhigh recommended for 4.8 agentic work). Research filed at resources/research/model-instruction-compliance.md. Implications for [output-tag-audit] and the response-shape tag system broadly — the audit's criteria should account for the priority architecture, not just tag-vs-prose cleanup.

- plan.md's thinking-work rule (line 11) has two gaps that combined to let a thinking batch through. First, "Never queue thinking work as a *build* batch" — the "build" qualifier implies thinking work as other batch types is fine. Second, the rule frames audit as "the one exception" to the thinking-work prohibition, when audit isn't thinking work at all — audit produces findings (routed to Captures), thinking work produces decisions. Treating audit as an exception to the thinking-work rule muddies the boundary: anything with a systematic-read shape looks like it qualifies for the "exception," even when its output is decisions, not findings. Observed: [plugin-behaviour-walkthrough-1] and [plugin-behaviour-walkthrough-2] promoted as audit batches, but their output is a routing decision list — thinking work wearing an audit shape. Fix: drop the "build" qualifier so the rule covers all batch types, and reframe audit as a separate category rather than an exception — audit produces findings-to-Captures, thinking work produces decisions, and the two don't overlap.

<!-- Plugin-ability audit findings, filed 2026-06-10 (plugin disabled for a free audit session). Goals: shrink always-on doc surface for less-capable models, move mechanical enforcement into hooks per resources/research/model-instruction-compliance.md, spend tokens where they buy compliance depth. -->

- **[scope-lock-files-section]** The pre_tool_use scope-lock (rule 2: during a build, only files in _build.md's `Files:` section are editable) is dead code — no procedure doc ever writes a `Files:` section. next.md Step 2's _build.md template has Entry / Index entry candidate / Progress / Changes only, so the hook's `_parse_build_files` finds nothing and its `if build_files:` guard skips enforcement on every build. The system believes this works: CLAUDE-TEMPLATE.md tells users "Only touch files listed in the active build scope," and [faq-build-md-functions] lists "feeds the pre_tool_use scope-lock hook" as a _build.md function. Fix shape: add a `Files:` section to the _build.md template, populated at scope-lock time from the files the batch entries name; next-build.md's scope-expansion approval appends to it; the hook then enforces for real. Related gap in the same file: the docstring claims Bash/PowerShell write-command detection for rules 1–2, but the code returns after the git checks — either implement minimal detection (redirects, Set-Content/Out-File targeting SPEC.md) or correct the docstring so future sessions don't trust phantom coverage.

- **[hash-backfill-as-hook]** The LOG hash backfill is the most mechanical procedure in the plugin — grep for `[HASH]`, run git log, replace in two files — yet it's specified twice as model-executed procedure (plan.md Step 1, next.md Step 1.1) and queued to move into done.md as more model-executed procedure ([log-hash-backfill-in-done]). Research technique #1 (resources/research/model-instruction-compliance.md): anything that must happen mechanically should be a hook, because hooks are deterministic and can't be skipped. session_start.py could do the entire backfill in Python — find placeholders, resolve hashes, edit in place, report one line via additionalContext — zero model reasoning, zero procedure-doc lines, identical behaviour on weak and strong models. Revises [log-hash-backfill-in-done]: the hook version supersedes the /done+amend design if it lands. Also resolves [trickle-up-hash-backfill-duplication] by deleting both procedure copies rather than consolidating them.

- **[queue-format-lint-hook]** The QUEUE.md format spec (slugs, `Blocked by:`/`Parked:` headers, processed/unprocessed divider, Build/Test/Audit subheadings, `Depends on:` slug references) lives as front-loaded prose in plan.md and plugin-behaviour.md that the model must hold in its head while writing. A less-capable model will drift the format, and today nothing catches drift until a later session trips over it. A PostToolUse hook on Edit/Write to QUEUE.md (and _build.md) could lint structure mechanically — batch missing a slug, parked item missing its removal-state header, divider deleted, `Depends on:` pointing at a nonexistent slug, unknown subheading — and feed warnings straight back, so the model corrects at write time instead of complying from memory. Long-term this inverts the doc burden: enforcement moves to the hook and format prose in the procedure docs can shrink to examples — doc surface down and reliability up at once, per research technique #1. Shares a Python queue-parser with [hash-backfill-as-hook]-style tooling if both land.

- **[git-add-safety-hook-gap]** plugin-behaviour.md File safety forbids `git add -A` / `git add .` (and done.md restates it twice — see [trickle-up-done-md-file-safety]), but pre_tool_use only blocks `reset --hard` and `push --force`. The blanket-add rule is exactly as mechanical as the two that are enforced — a regex on the command — and a weaker model is far more likely to reach for `git add -A` than for `push --force`. Extend the git-safety section to deny `git add -A` / `git add .` / `git add --all` and `git commit -a`/`-am`, with a denial message teaching explicit staging. Once enforced, the doc restatements can shrink to one line — the hook's message does the teaching at the moment it matters.

- **[behaviour-doc-double-load]** plugin-behaviour.md — the largest doc — is injected in full by session_start at every session start, and /plan, /next, and /done each then instruct "Re-read them before continuing," so a normal skill session carries two full copies. The re-read has a purpose (the injected copy ages out of a compacted context), but paying double on every session to insure against occasional compaction is backwards. Options: (a) keep the injection, drop the re-read line from the three SKILL.md files — cheapest, trusts the injected copy; (b) drop the injection, keep the skill-time re-read — rules arrive exactly when a skill needs them, but conversation outside skills loses them; (c) inject a compact always-on core (the rules that govern outside-skill behaviour: captures, communication, file safety) and let skills load the full doc — progressive disclosure, the research-recommended shape, and the smallest standing surface for less-capable models. (c) costs the most restructuring; (a) is a one-line edit per skill available today.

- **[tag-definitions-compliance-rewrite]** Concrete application of the filed compliance research (see the research capture above on skill docs being user-message priority): rewrite the five response-shape tag definitions in plugin-behaviour.md using the three wording techniques that survive priority conflicts — a why-clause aligning the tag with helpfulness ("[SILENT] — this step is internal bookkeeping; narrating it buries what the user actually needs"), positive quantified constraints ("output zero text," "exactly one item, then stop" instead of "don't narrate," "one at a time"), and explicit scope statements ("applies to every output in this skill run"). Then apply the same treatment to the two or three most-violated prose rules — the bundling/SEQUENCE rule and the show-draft-then-ask rule are the observed offenders. Deliberate token bump: a tag definition that costs twice as many tokens but actually holds on 4.7/4.8 is a good trade; the current bare definitions are cheap and ignored. Belongs alongside [output-tag-audit] — that audit finds prose-where-tag-belongs, this rewrites what the tags say once found, and its criteria should assume the rewritten definitions.

- **[session-start-dirty-tree-check]** session_start reports project state but not git state. A consumer project with uncommitted changes at session start almost always means the previous session ended without /done — work sitting unrecorded and uncommitted that a non-coder won't notice for weeks (observed in this project: 5 docs files dirty across two-plus sessions, and the host CLAUDE.md now carries a manual dirty-tree check as compensation). Add `git status --porcelain` to session_start and emit one line when dirty: "N files have uncommitted changes from a previous session — /done will pick them up." Deterministic, zero model reasoning, and it generalizes the host-side check into the plugin so every consumer project gets it. Complements [user-edits-rollup-on-commit], which catches the same orphans later, at /done's commit step.

- **[zip-pycache-hygiene]** si-plugin.zip ships `si-plugin/hooks/__pycache__/session_start.cpython-314.pyc` — confirmed by listing the current zip's entries. __pycache__ is gitignored so the repo stays clean, but push-and-rezip step 7 (Compress-Archive) packs from disk, so every user install carries a stale compiled artifact for a Python version they may not have. Harmless today, but stale bytecode shipped beside its source is the kind of mystery a future debugging session burns an hour on. Fix: delete or exclude `__pycache__` before zipping. Host-side change to this project's CLAUDE.md push ritual, not a target-doc change, so it needs the manual-update path.

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
