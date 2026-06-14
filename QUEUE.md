# QUEUE

## Batches

Worked top to bottom. Each batch of changes or tests is one /next session of either type:

- build session where changes are applied, then claude runs all tests it is able to do itself
- test session where the user runs any testing only they can do

**Red flags, part 1: the screen-and-surface rule and the three flag states** **[red-flags-screen-rule]**
Blocks: [red-flags-structure]

Reintroduces the old plugin's "Red flags — screen and surface" behaviour — the security half of the red-flags feature now described in SPEC.md. Claude actively screens for risks that could expose the user's data or their users' data, or amount to a breach, and surfaces each as a red flag in plain English instead of building past it silently. Flagging, not fixing: Claude names and routes the risk, it doesn't quietly handle it. The rule lives in plugin-behaviour.md so it fires in every session type — including mid-build, where Claude is writing the very code that could expose data. It also defines the three flag states, because the future autopilot gate (designed into cruise control) will read them: only resolved or accepted clear the gate, open blocks it. Accepted is informed consent recorded in the LOG — what the user was warned about and that they chose to proceed — the trail that protects them if a breach surfaces later. Scoped to security, privacy, and breach risk specifically; the mechanism leaves room for other flag types without building them now. Hardened from the start so an eager model doesn't smooth past the warning — firing when it matters is the entire point.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md: add the red-flags screen-and-surface rule, compliance-hardened from the start (why-clause, positive constraint, explicit scope, per resources/research/model-instruction-compliance.md). Claude screens every session type — capture, plan, build — for anything that could expose the user's or their users' data or amount to a breach, and raises a red flag in plain English naming the risk; it surfaces and routes, never silently fixes or ships past. Scope: security, privacy, and breach risk specifically.
- plugin/si-plugin/docs/plugin-behaviour.md: define the three flag states — open (raised, not yet addressed), resolved (risk designed out or fixed), accepted (user consciously accepted it, recorded in the LOG as informed consent). State that the future autopilot gate reads these: only resolved or accepted clear it, open blocks.

Test:
- Self-verifying from the doc text. Behavioural watch after reinstall: a genuine data-exposure risk in later work draws a plain-English red flag rather than silence; any miss is a mandatory capture.

**Red flags, part 2: the section, routing, and consent record** **[red-flags-structure]**
Depends on: [red-flags-screen-rule]

The structural half of the red-flags feature: where flags live and how they move through their states. Builds on [red-flags-screen-rule], which defines the rule and the three states this batch routes against. A Red flags section is added at the top of QUEUE.md — the first thing seen each session, per SPEC.md — both in the scaffolded template for new projects and in this project's own QUEUE.md. /plan learns to route a red-flag capture into the section and carry its state. /done records an accepted flag's decision in the LOG, the informed-consent trail. A consumer FAQ entry explains what a red flag is and what the three states mean. The autopilot gate is not built here — it's designed into cruise control later and reads the states this batch maintains.

Build:
- plugin/si-plugin/docs/setup.md QUEUE.md template: add a Red flags section at the top of the scaffolded QUEUE.md, above Batches — empty by default, with a one-line description of what collects there.
- This project's QUEUE.md: add the same Red flags section at the top, above Batches, empty for now.
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md and this project's CLAUDE.md: document the Red flags section in the QUEUE.md format description.
- plugin/si-plugin/docs/plan.md: route a capture filed as a red flag into the Red flags section, carrying its state; a flag's state can change during planning (open → resolved or accepted).
- plugin/si-plugin/docs/done.md (or the relevant sub-doc): when a flag is accepted, record the decision in the LOG entry — what the user was warned about and that they chose to proceed.
- plugin/si-plugin/templates/faq-template.md (+ index line): FAQ entry — what a red flag is, the three states, and what "accepted" means (a recorded, informed choice).

Test:
- Self-verifying from doc text for structure. Behavioural, host-side (after reinstall): the next red flag Claude raises lands in the Red flags section with a state; an accepted flag's decision shows up in the LOG. Needs the deferred-test discipline — flag at /done if it can't run.

**Forbid illustrative expansion in /setup Q4 batch entry** **[setup-q4-no-expansion]**

Setup.md Q4's rule is currently "Use the user's words, don't expand or split — scope decisions belong in /plan." Observed in a real /setup run: Claude wrote the batch with parenthesized examples drawn from a pre-existing source doc ("e.g. overlocker receipt, mortgage interest %"). Parenthesized examples read as illustrations not commitments, but they're still expansion beyond the user's words — and a queue entry with examples looks like the user agreed to those items even when they're in parens. The rule needs tightening: no expansion at all, even illustrative. If examples would clarify what's in scope, the place is a Q4 follow-up question to the user, not a parenthetical in the written entry.

Build:
- plugin/si-plugin/docs/setup.md Q4 rule: tighten the existing "Use the user's words, don't expand or split" to forbid illustrative expansion explicitly — "Use the user's words verbatim. No expansion, no illustrative examples, no parentheticals drawn from visible context. If examples would clarify scope, ask a Q4 follow-up; don't smuggle them into the entry."
- plugin/si-plugin/docs/setup.md Q4 rule: note that the existing one-follow-up-max rule for vague answers covers the case where examples actually are needed.

Test:
- Self-verifying on the next /setup run where Q4 is answered and visible source content exists.

**Setup close-outs name /done; scaffolding creates the repo** **[setup-closeout-redesign]**

From three [close-out-audit] findings (e120f3d), routed together as one design decision. setup.md is the only skill whose session ends never name /done. Step 4 closes with "/plan or /next" and stops. Step 2C's migration close does the same and reads no project state. So the scaffolded files sit uncommitted, no LOG entry gets written, and the project record starts with a gap — a consumer's first session teaches them to skip the close-out habit. The /next offer also contradicts setup's own Q4 rule: the interview deliberately writes the first entry rough and defers scoping to /plan, yet the close-out sends that unscoped entry toward execution. Two gaps surfaced at routing ride along. A fresh consumer folder has no git repository, so a /done recommendation is only honest once scaffolding creates one. And /done routes by _build.md, so a migration close can't blindly recommend /done when an interrupted build is present — the right pointer there is resuming the build.

Build:
- plugin/si-plugin/docs/setup.md Step 2 scaffold list: create a git repository when none exists, as part of scaffolding — silent and mechanical, like the rest of the scaffold. This is what makes the /done close work in a fresh consumer folder.
- plugin/si-plugin/docs/setup.md Step 4 close-out: replace "Run /plan to scope your first batch, or /next if you're ready to build" with a close that recommends /done. The file-list display stays as consent display — it shows what appeared in the folder; the LOG entry /done writes remains the session's single summary. State that relationship in one line.
- plugin/si-plugin/docs/setup.md Step 2C item 4: make the migration close state-aware — leftover _build.md present: name the interrupted build and recommend resuming it with /next, noting the migration changes get picked up at that build's close; otherwise recommend /done, matching Step 4.
- plugin/si-plugin/docs/done-plan.md: widen the close-out to setup-shaped sessions — the entry template's framing covers scaffolding sessions (what was set up and why, not "queue changes"), and recommend-next gains a branch: a fresh project whose only batch is the rough Q4 entry recommends /plan, never /next, because that entry is deliberately unscoped.

Test:
- Doc edits self-verifying. Behavioural, host-side (after push + reinstall): the next real /setup run in a fresh folder — repo created silently, close names /done, /done writes a setup-shaped LOG entry and commits the scaffold. Needs the deferred-test discipline — flag at /done if it can't run.

**Project-agnosticism sweep: rewrite setup.md to read for non-app projects too** **[setup-project-agnosticism-sweep]**

setup.md is the on-ramp every project enters through, and its current wording assumes the user is building an app: the five interview questions, the Step 4 close-out, the Step 1 folder-state cases, and the three scaffolded doc templates (SPEC.md, QUEUE.md) all use app-building framing ("building," "components," "functionality," "source code," "builds first then tests"). The behaviour-agnosticism audit (fac25ab) surfaced 11 findings; seven collapse into one sweep of mechanical-or-near-mechanical rewords applied across setup.md and its scaffolded templates. The Step 4 close-out reword originally counted here moved to [setup-closeout-redesign], which replaces that line entirely. The three more substantive findings — REGISTRY.md noun choice (Q3.5 interview question), the spec-entry-trigger threshold across project types, and plugin-behaviour.md doc-routing — are held in separate captures for their own consideration. This sweep changes wording only; no interview-flow changes, no rule-trigger changes.

Build:
- plugin/si-plugin/docs/setup.md Q1: reword to "What is this project, and who is it for?" (drop "building"). From [setup-q1-agnostic-wording].
- plugin/si-plugin/docs/setup.md Q2: reword to "What's the core of it — the main thing it produces, organises, or does?" (drop "functionality / does"). From [setup-q2-agnostic-wording].
- plugin/si-plugin/docs/setup.md Q3 examples: replace software-only example set with 3–4 examples spanning software + non-software projects. From [setup-q3-agnostic-examples].
- plugin/si-plugin/docs/setup.md Q4: reword inclusively — "What's the first thing to build or do? What would you want to have working or made progress on by the end of today?" Keeps build-shape framing for app projects, adds do/progress framing for others. From [setup-q4-inclusive-wording].
- plugin/si-plugin/docs/setup.md Step 1 folder-state cases: reword Case A / Case B to "No content" / "Content exists" (or similar project-agnostic phrasing). From [setup-step1-case-wording].
- plugin/si-plugin/docs/setup.md SPEC.md template: reword "What the app is" to "What the project is". From [setup-spec-template-agnostic].
- plugin/si-plugin/docs/setup.md QUEUE.md template: reword "Each batch is one /next session — builds first, then tests." to "Each batch is one /next session. Subheadings name the kind of work (Build, Test, Audit)." From [setup-queue-template-type-complete].

Test:
- Self-verifying from the doc text. After the rewrite, setup.md reads cleanly for a tax-prep, records-keeping, research, or writing project as well as for an app project.
- E2E follow-up (user-run, separate live session, queue as separate batch if desired): rerun /setup in a non-app folder and observe whether the questions land cleanly.

**setup.md goes tag-free: self-contained prose carries the behaviour** **[setup-self-contained-no-tags]**

From [output-tag-audit], the structural finding. setup.md's response-shape tags reference definitions that live in plugin-behaviour.md, which is injected only in adopted projects — and /setup's working cases run unadopted, so the tags are undefined tokens there. The prose restatements beside them are the real carriers. Decided at routing: setup.md stays deliberately self-contained in prose, and the tags come out — the alternative (inlining a compact copy of the definitions) creates a second, weaker copy that drifts, which is the duplication this arc keeps removing. Extends the [trickle-up-ask-when-unsure] precedent that setup.md carries its own copies by design. setup.md is exempt from [tag-restatement-trim] for the same reason.

Build:
- plugin/si-plugin/docs/setup.md: remove the three tag tokens ([BRIEF], [SEQUENCE, PROMPT], [BRIEF, PROMPT]). At each spot, check the adjacent prose carries everything the tag claimed — stop-and-wait, one-per-message, brevity — and write the missing piece where it doesn't. Locate by content, not line numbers.
- plugin/si-plugin/docs/setup.md, near the top: add one line stating why this doc carries no response-shape tags — its sessions run before the behaviour rules load, so prose carries the behaviour. This guards against a future session "fixing" the inconsistency by re-adding tags.
- plugin/si-plugin/docs/setup.md, the two untagged interaction spots from the same audit, landed as prose per this batch's decision: in Case C, make the wait explicit — tell the user, offer /plan, stop, and wait for their answer. In the Step 2 scaffolding, add a line that the work runs without narration — the close-out reports the file list, so nothing is lost by staying quiet.

Test:
- Self-verifying from the doc text. Behavioural: the next live /setup run should still ask one question per message and wait — now on prose alone.

**Key the spec-entry trigger on SPEC.md itself, not "features"** **[spec-entry-trigger-rethink]**

The pipeline rule — "New features need a spec entry before a build entry … Threshold: if a user would see or experience the difference" — assumes the project ships features to external users. Owner-only projects have neither, and the capture feared the rule would have to split per project type. It doesn't: both load-bearing problems dissolve by keying the trigger on the spec rather than a category of change — if landing the change would make SPEC.md's description of the project wrong or incomplete, update SPEC.md first. "Features" disappears (refactors pass untouched because they change no spec sentence; new capabilities, scope changes, and new output types all trip it, any project type); the audience question evaporates rather than getting answered, since noticeability was always a proxy for "the product truth changed" and the new form tests that directly. Mechanically checkable on a weak model: read SPEC.md — /plan already requires that — and ask whether any sentence in it goes wrong or incomplete. The per-type split stays rejected: two rules are double maintenance, one self-referential test covers both shapes. Same noun-free move as [setup-registry-template-and-noun]. From [behaviour-agnosticism-audit].

Build:
- plugin/si-plugin/docs/plugin-behaviour.md Routing and discipline, spec-entry pipeline bullet: replace the features-noun trigger and the noticeability threshold with the self-referential form — if landing this change would make SPEC.md's description wrong or incomplete, update SPEC.md first. Keep the pipeline sequence (idea → question if unclear → SPEC.md → QUEUE.md) unchanged.
- plugin/si-plugin/docs/plan.md ground rules, the pipeline line: matching reword — "spec entry (if it changes the product)" keyed to SPEC.md truth the same way, so the canonical statement and the restatement can't drift.

Test:
- Self-verifying from doc text: the rule reads cleanly for an app project and a tax-prep project alike, with no audience named.

**Self-hosting notes audit: inventory every self-hosting rule and judgment, wherever it lives** **[self-hosting-notes-audit]**

Self-hosting misses keep surfacing: designs authored without self-hosting context (the deferred-test close check that only pays in self-hosting, user-caught 2026-06-12), and rules whose halves live in different places — next.md halts on push markers while the convention telling /plan to write them lives only in this project's CLAUDE.md, so shipped plan.md has never heard of them. The cause: self-hosting knowledge accumulated in this project's CLAUDE.md and in session judgment rather than in the method. This audit opens a distribution arc. The inventory routes to Captures per the audit contract; the /plan that processes the findings authors the follow-on batches — those can't be authored today because their content is the findings. Each note then relocates to its right home with its rationale attached, per the why-pipeline. Three candidate homes: shipped procedure docs, generalized, when the note is method behaviour; this project's CLAUDE.md, when purely local workflow; the parked [self-hosting-support-during-setup] design scope, when it's consumer-facing self-hosting convention for /setup to scaffold — the inventory is that item's design input, its trigger unchanged. A CLAUDE.md staging stage (copy everything in first, distribute later) was weighed and dropped: Captures is already a complete, committed inventory, and staging adds write-then-remove churn. In exchange, distribution is relocation, never copying — the new home lands and the CLAUDE.md source comes out in the same batch, so no danglers survive — and the arc ends with a CLAUDE.md sweep for stragglers. Reading QUEUE.md as part of the target means decided-but-unshipped notes ([push-marker-hard-direction]) enter the inventory without waiting to land, which is what frees this audit to be placed by urgency rather than after the queue settles. Why distributed-with-rationale at all: rules hold best stated where they're used with their why attached (resources/research/model-instruction-compliance.md), and the post-June-20 weaker-model sessions need the relevant information in hand in the doc that's loaded when it matters.

Audit:
- Target: this project's CLAUDE.md; plugin/si-plugin/docs (all procedure docs and plugin-behaviour.md); plugin/si-plugin/hooks (denial and report text); plugin/si-plugin/templates; QUEUE.md (batches, parked items, captures); SPEC.md; resources/research/; LOG/index.md, opening entry files only where an index line signals self-hosting content.
- Criteria: every rule, convention, or judgment that exists because this project builds the plugin it runs — host/target distinction, push-and-rezip, reinstall gating and host-side effects, push markers, host-side deferred tests, dirty-tree checks, version and zip mechanics, all-use-is-testing — plus judgment calls that only make sense under self-hosting (a session's own behaviour being the thing under test). For each finding: the note, where it lives today, a candidate home (shipped-generalized / this project's CLAUDE.md / the parked /setup-scaffolding scope — candidate only; the decision is /plan's), and whether its rationale is written anywhere.

**Reframe /plan Step 1 entry + follow-up as sequencing, not either/or** **[plan-step1-sequencing]**

plan.md Step 1's entry question ("Do you have something to discuss, or ready to process Captures?") and its follow-up after a discussion item ("Anything else, or ready for Captures?") both use "or" framing that reads as a branch — discuss-vs-process — when /plan always processes Captures and a discussion item is just an optional pre-step. The misreading surfaced twice in the 7563bc0+1 /plan: Claude reproduced the framing in the read-state summary ("if processing...") and bundled an unrelated housekeeping decision onto it as a conditional, the same wording bug surfacing in Claude's own output. Fix the wording so processing reads as the destination and discussion as the optional thing that happens first if there is one. Folded in from an [output-tag-audit] finding: the same two lines are stop-and-wait moments with no [PROMPT], and Step 1's scan block says "collect them silently" with no [SILENT]. Tag-only fixes. They ride along here because this batch rewrites two of the three lines anyway — tagging text another batch rewrites would collide.

Build:
- plugin/si-plugin/docs/plan.md Step 1 entry question: replace "Do you have something to discuss, or ready to process Captures?" with wording that frames processing as the destination — e.g. "Anything to discuss before we process Captures?" Keep the empty-Captures branch ("If Captures is empty, ask what they'd like to work on.") as-is. Tag the question [PROMPT].
- plugin/si-plugin/docs/plan.md Step 1 follow-up after a discussion item: replace "Anything else, or ready for Captures?" with matching wording — e.g. "Anything else before Captures?" Tag it [PROMPT].
- plugin/si-plugin/docs/plan.md Step 1 unpark + staleness scan block: tag it [SILENT]. The prose already says "collect them silently" — the tag makes it binding.
- plugin/si-plugin/docs/plan.md Step 1 branching structure ("If the user has something" / "When ready: Move to Step 2"): adjust so the prose matches the new framing — discussion items run first if present, then Step 2 always runs, no either/or branch.

Test:
- Self-verifying from the doc text on the next /plan run. The entry question and follow-up should read as sequencing, and Claude shouldn't reproduce "if processing" or similar branching framing in narration.

**Approval-time outputs render as blockquotes with a content-type lead-in** **[approval-display-blockquotes]**

Supersedes [fenced-block-content-type-label], whose label design assumed a fence language slot. User feedback (2026-06-11): the desktop app's fenced blocks don't wrap, so long drafts run off-screen and get read incompletely — defeating the fence's purpose, exact text read and approved. Blockquotes wrap. The standard, live-tested through a full /plan session: approval-time and verbatim displays render as markdown blockquotes, with a bold lead-in line above the quote naming the content type (batch draft, capture draft, commit message, log entry, parking reason). One exception: content whose exact characters are the substance — code, shell commands — keeps a fence, because rendering would corrupt it. Trade-off accepted at routing: a blockquote renders markdown, so syntax slips in a drafted entry are invisible to the approval read. Division of labour recorded: the human approves meaning; [queue-format-lint-hook] checks structure at write time.

Amended after the 2026-06-12 /done close (f05e336): the commit title and body still arrived as fences while the same close used a blockquote for the LOG entry. The cause: done.md's commit core explicitly instructs fenced blocks and points at plugin-behaviour.md's verbatim-copy rule, so the local instruction beat the decided standard. Two consequences carry into the build list — the verbatim-copy rule needs the rewrite too, not just the approval-time rule, and the sweep has a confirmed offender pinned in done.md's commit core. One design input: Claude runs git commit itself, so commit messages were never a real paste target. They move wholly to blockquote. Genuine paste targets — paste-ready prompts, shell commands the user runs in a separate terminal — keep fences under the exact-characters exception.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md, the approval-time outputs rule: rewrite from fence to blockquote-with-lead-in, carrying the why (fences don't wrap; an unread draft defeats approval), the canonical content-type labels, and the code-keeps-fences exception.
- plugin/si-plugin/docs/plugin-behaviour.md, the verbatim-copy rule: rewrite to the same standard with the sharper boundary — fences remain only for genuine paste targets, strings the user lifts and pastes or runs elsewhere (paste-ready prompts, shell commands for a separate terminal); commit messages are not paste targets because Claude runs git commit itself, so they render as blockquotes under the approval-time rule.
- Sweep every procedure doc naming "fenced code block" at an approval or display moment — plan.md's promote sub-step, next-build.md's two capture-routing spots, next-test.md's, next-audit.md's (check what remains of it after [audit-findings-bulk-approval]), and the done family — and point each at the new standard. Locate by content, not line numbers. Confirmed offender to hit: done.md's commit core, the commit-message presentation step, whose explicit "each in its own fenced code block" instruction is what overrode the standard at the f05e336 close.

Test:
- Behavioural, host-side (after push + reinstall): the next /plan or /done approval draft arrives as a labelled blockquote that wraps. Needs the deferred-test discipline — flag at /done if it can't run.
- Behavioural, host-side, the pinned case: the next /done commit step presents title and body as blockquotes, fences gone. Needs the deferred-test discipline — flag at /done if it can't run.

**Require an explicit ask after every approval-time draft** **[approval-ask-after-draft]**

Procedure docs show drafts for approval but never say to ask. plan.md's promote step says "Don't write to QUEUE.md until approved," the approval-time rule says to fence the draft, and the stop-and-wait tag already sits on the promote step — so Claude stops, but stopping silently satisfies all of it. Observed across multiple /plan sessions and confirmed as direct user feedback: the draft appears, then silence, leaving the user to figure out what's wanted. The fix sits one level above any single skill, because /done's LOG entries and commit messages and /setup's drafts can all fail the same way: every approval moment must end with the question.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md "approval-time outputs go in a fenced code block" rule: extend so presenting the block is only half the move — the message must end with an explicit ask naming the decision needed (e.g. "Approve this wording?", "Write it to the queue?"). Silence after a draft fails the rule even when Claude has stopped to wait. Author the rule compliance-hardened from the start — why-clause plus positive constraint per resources/research/model-instruction-compliance.md (e.g. "a draft isn't actionable until the user knows what's being asked; end the message with the question") — rather than hardening it in a later pass.

Test:
- Self-verifying from doc text on the next /plan or /done run — every draft shown for approval should be followed by an explicit ask.

**Captures and batch entries authored plain: complete, not compressed** **[human-readable-authoring]**

User feedback (2026-06-11), surfaced by the first verbatim-first presentation: captures and batch rationales were written in long clause-chained sentences — dense Claude-for-Claude style that the co-reading human couldn't comfortably read, at filing time, at presentation, and at approval. One batch rationale had to be rewritten live before the user could understand what she was approving; the plain rewrite carried the same content and was approved as the replacement. The load-bearing insight: what Claude needs from these artifacts is completeness — facts, references, conditions preserved — not syntactic compression. Same information, shorter sentences, one idea per sentence; the modest token cost is accepted. Home is plugin-behaviour.md because every skill drafts these — /next routes discoveries to Captures mid-build, /done routes stragglers at close, /plan writes both.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md Captures rule: add the authoring standard, compliance-hardened from the start (why-clause, positive constraint, explicit scope per resources/research/model-instruction-compliance.md) — keep everything (facts, references, conditions); write it in short sentences, one idea per sentence; the human co-reads this text and approves it, so unreadable is unapprovable. This is the canonical statement.
- plugin/si-plugin/docs/plugin-behaviour.md, the why-pipeline's rationale-authoring guidance: one line extending the same standard to batch rationales and pointing at the canonical statement — no duplication.

Test:
- Behavioural on later sessions of any skill: freshly authored captures and rationales read in plain sentences without losing references or conditions. Already validated live across this session's drafts.

**Show-before-write keyed to the action, not the loop** **[show-before-write]**

plan.md already says never write batch entries without showing the exact text first, but the rule rides on the loop's beats — and the beats live in conversation memory. Observed 2026-06-11, deep in a compacted session: a recommendation concrete enough to read as a draft merged the two approval beats, and an entry was written unshown. The hardened form needs no memory of which beat the item is on, because it keys to the write itself: the message immediately before any QUEUE.md batch write must contain the entry text verbatim, and approval attaches to shown text, never to a described shape. Sibling insurance to [plan-state-artifact], which fixes the structural cause; this rule holds even with no state at all.

Build:
- plugin/si-plugin/docs/plan.md ground rules: harden the show-first rule to the action-keyed form, compliance-hardened from the start (why-clause, positive constraint, explicit scope per resources/research/model-instruction-compliance.md) — the message immediately before any QUEUE.md batch write contains the entry verbatim; approval attaches to shown text, not to a described shape; a recommendation, however concrete, is not a draft.

Test:
- Behavioural, host-side (after push + reinstall): later /plan sessions write nothing to the queue without the verbatim entry in the immediately preceding message. The case to watch is late-session, after compaction — where the original slip happened.

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

**Session-start dirty-tree warning** **[session-start-dirty-tree-check]**
Depends on: [user-edits-rollup-on-commit]

session_start reports project state but not git state. A consumer project dirty at session start almost always means the previous session ended without /done — work sitting unrecorded that a non-coder won't notice for weeks (observed here: five doc files dirty across two-plus sessions, compensated by a manual check in this project's CLAUDE.md). The hook generalizes that check so every consumer project gets it: git status --porcelain at session start, one line when dirty. The Depends on is real, not thematic: the warning's promise — "/done will pick them up" — only becomes true once [user-edits-rollup-on-commit] teaches /done to offer dirty out-of-scope paths into its commit. Silent when _build.md exists: mid-build dirt is expected, not orphaned. Sibling to the hook cluster ([hash-backfill-as-hook], [queue-format-lint-hook], [git-add-safety-hook-gap]); shares session_start.py with the backfill hook, so whichever builds second sees the other's changes.

Build:
- plugin/si-plugin/hooks/session_start.py: run git status --porcelain; when non-empty and no _build.md is present, emit one line via additionalContext — "N files have uncommitted changes from a previous session — /done will pick them up."
- This project's CLAUDE.md (host-only, does not propagate via reinstall): remove the manual "Session-start dirty-tree check" section — the hook supersedes it. Accepted: a brief gap between this edit and the reinstall that activates the hook.

Test:
- Claude-run: session_start.py against a fixture repo — dirty tree without _build.md warns with the correct count; dirty with _build.md stays silent; clean stays silent.
- Host-side (after push + reinstall): live one-liner at the next session start with known dirt. Needs the deferred-test discipline — flag at /done if it can't run.

**Per-session /plan state artifact: _plan.md** **[plan-state-artifact]**
Depends on: [session-start-dirty-tree-check]

The capture-processing loop runs several beats per item, and the session's position in it lives only in conversation memory. A long compacted session lost a beat and wrote an entry unshown — the exact failure [short-session-design-target] predicts: memory covering for missing structure. "Planning sessions stay short" was the assumption, and 2026-06-11 disproved it. /next already externalizes execution state to _build.md; planning gets the same treatment. The artifact pays beyond the slip: it survives compaction, gives an interrupted /plan a resume path through session_start the way an interrupted build has one, and hands /done a mechanical record of what was routed where instead of a reconstruction from conversation. Sibling: [show-before-write] is the zero-state insurance at the write action; this batch removes the structural cause. The Depends on is real: one build entry extends the dirty-tree warning that batch installs.

Build:
- plugin/si-plugin/docs/plan.md: create _plan.md when capture processing begins — carried candidates, the item list, current item, beat reached. Update at each beat transition; append each routed item with its disposition (promoted, parked, dropped — with slug). One line per item so updates stay cheap.
- plugin/si-plugin/hooks/session_start.py: detect a leftover _plan.md the way _build.md is detected — report an interrupted planning session and point /plan at resuming from the recorded item and beat. Shares this file with the other hook batches; whichever builds second sees the other's changes.
- plugin/si-plugin/docs/done-plan.md: read _plan.md's routed list when writing the LOG entry; delete the artifact at close — same lifecycle as _build.md.
- plugin/si-plugin/hooks/pre_tool_use.py: verify _plan.md presence doesn't trip any build-scope behaviour; adjust only if it does.
- The dirty-tree warning from [session-start-dirty-tree-check]: extend its silence condition — uncommitted changes with _plan.md present are expected mid-plan, same as mid-build dirt with _build.md. Locate by content.
- plugin/si-plugin/templates/faq-template.md (+ index line): FAQ entry — what _plan.md is, why it appears in the project, why not to delete it.

Test:
- Claude-run: session_start.py against a fixture repo — leftover _plan.md detected with the right report line; neither artifact present, silent.
- Host-side (after push + reinstall): interrupt a /plan mid-processing, open a new session, watch for the resume offer. Needs the deferred-test discipline — flag at /done if it can't run.

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

Observed at f123eed: a /plan discussed and resolved a concern about one growing log.md getting too large to read, but the LOG entry recorded only the conclusion — not the concern or the reasoning that addressed it. Two sessions later the user couldn't retrieve why the alternative was rejected and second-guessed the decision, and the log-split design got relitigated. The why-pipeline's preserve rule carries rationale forward, but "rationale" currently means the reasoning behind the decision made, not the reasoning against the alternatives considered. The trigger needs a boundary so entries don't bloat: discussion-level consideration qualifies — a concern raised and resolved, an alternative seriously weighed — passing mentions don't. The intuitive-but-rejected path is the case that most needs preserving.

Build:
- plugin-behaviour.md why-pipeline Preserve rule: extend the definition of rationale to include concerns raised and resolved and alternatives seriously weighed, carried with why they lost. State the trigger boundary: discussion-level consideration qualifies, passing mentions don't, and decisions where the rejected path is the intuitive one always qualify.
- The LOG-entry-writing step in the /done per-type sub-docs (post-[done-closeout-extraction] shape): add one reinforcing check at writing time — does this entry carry any concern that was resolved or alternative that was weighed? Keep it to a single line pointing at the why-pipeline rule; don't restate the rule per sub-doc.

**File research by default when findings are non-trivial** **[research-filing-default]**

plugin-behaviour.md says where research goes (resources/research/) but never when — so filing only happens when the user asks, and findings from mid-conversation web searches stay in chat and evaporate. Observed across sessions; the trigger case was the fenced-block label question, where research had been done but couldn't be retrieved later because it never became a file, and the next /plan offered to redo the search. The fix flips the default: filing is part of using a finding, not a separate request. Visibility matters too — a silent rule can't be checked, so the file gets named in chat when it lands. A /done close-out backstop ("did research happen this session that isn't filed?") was considered and held in reserve in case leakage continues after the rule lands.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md Research section: add the default-filing rule — when a web search or external lookup yields a non-trivial finding, file it under resources/research/<topic>.md as part of using it, not only on request. Threshold: a finding that informed a decision or would have to be redone if lost gets filed; a fact checked once and discarded doesn't. Claude names the file in chat when it lands.
- plugin/si-plugin/docs/plugin-behaviour.md Communication section: fold the existing "File research under resources/research/" line into the Research section so one canonical statement remains.

Test:
- Self-verifying on the next session where a web search yields a real finding — the file should land and be named in chat without the user asking.

**Relationships exist only if written: position never encodes** **[relationships-must-be-written]**

Caught live this session: Claude stripped a Blocks: header from a batch draft, reasoning that adjacency in the queue already carried the relationship — exactly the positional encoding the slug convention exists to prevent, one step earlier than the convention reaches. The existing rule governs how references are written (slugs, never positional pointers) but not the decision of whether to write one, so "placement carries it" passes the current wording while losing the relationship to the next reorder. The user caught it; the rule should have.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md Dependency ownership: add the missing half to the slug-reference bullet — relationships between queue items exist only if written, in a header or as a slug reference in prose; queue position never encodes a relationship; placement is a convenience layered on top, never the carrier. Carry the why: queue order changes every session, so anything encoded as position is one promote or reorder away from silently vanishing.

Test:
- Self-verifying from doc text. Behavioural confirmation on the next /plan that places related batches — the relationship should land in a header even when the batches end up adjacent.

**Name the Blocked-by trigger flavors; non-default triggers must be written** **[blocked-by-trigger-flavors]**

The Blocked by: convention reads "the named slug shipped" as the firing condition, but dependencies carry at least three trigger flavors — landing (B needs A's changes in the tree), findings (B was generated by A's findings), clarity (B needs what A clarified, satisfied the moment the question resolves). The flavor difference is operational, not taxonomic: the unpark watch reads headers mechanically, and a clarity-shaped item under a ships-the-slug reading stays parked past its real readiness — observed live in the 2026-06-10 /plan, where a capture's blocker fired at decision time while the blocking batch remained unshipped, and earlier at 1b7d359. The fix adds no syntax and no flavor field (a closed taxonomy would force nuance into slots — the why-pipeline's own warning): the bare slug form keeps its landing-shaped default, and whenever the real trigger is anything else, the prose tail must state the firing condition. The flavors get named as illustrations of when that's needed, not as a classification to fill in.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md Dependency ownership, the Blocked by / Parked bullet: add the note — bare slug fires when the named item's changes ship (landing, the default); any other trigger (findings-generated, satisfied-at-decision, external event) must be written in the prose tail ("Blocked by: [slug] — satisfied once X is decided"). Name the three flavors with one example each, including that clarity-shaped triggers can fire at /plan-decision time before anything ships.

Test:
- Self-verifying from doc text. Behavioural on future unpark scans: items with non-landing tails fire at their stated condition, not at slug-ship.

**Force the Parked: choice and end its staleness exemption** **[parked-slot-discipline]**

Two accumulation risks share the Parked: slot. Filing: items with nameable behavioural triggers were twice filed Parked: even though the rule says trigger-means-Blocked-by — the slot choice rides on judgment with no forcing question. Review: plan.md's opening scan reads Parked: items only to skip them, so nothing ever asks whether the project has evolved past one; meaningless accumulation is the failure mode. A hand-run sweep already converted the backlog (2026-06-10 /plan, zero Parked: items left); this batch makes the discipline structural so the sweep never needs repeating. Placed after [blocked-by-trigger-flavors] — both shape the same slot-choice rule area.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md, the Blocked by / Parked bullet: filing as Parked: requires first affirming that no nameable trigger exists. State plainly that a behavioural trigger with no slug is a valid Blocked by: tail — the observed misfilings treated slug-less triggers as unparkable.
- plugin/si-plugin/docs/plan.md Step 1 scan: include Parked: items in the staleness watch (drop, rewrite, or keep), replacing "skip unless something else flags them."

Test:
- Behavioural on later /plan sessions: the next trigger-bearing item filed lands in Blocked by:, and the next scan visibly weighs Parked: items instead of skipping them.

**Present the working item verbatim-first: quote before thinking** **[capture-verbatim-first]**

After "continue to the next item," Claude reads and thinks first while the user sits with nothing until the full presentation lands. The fix, designed and live-tested across a full /plan session (2026-06-11): the turn opens with a one-line preamble ("here it is, my thoughts to follow" or similar) and the item quoted verbatim, and only then does analysis begin. The live trial surfaced the load-bearing detail: ordering the text on the page isn't enough — the quote must be *sent* before the thinking starts, or it arrives bundled with the analysis and the waiting problem survives. No fresh read is needed; the queue is already loaded from the session's start. Deliberately silent on the rendering device — the approval-time display standard owns that. /next's pre-flight has the same waiting problem, observed 2026-06-11 in a live /next: hashes backfilled, queue read, blocker gate run, and the batch only appeared after all of it. The same fix lands there in this batch. Because the user now reads batch text at the pre-flight moment, it must read plainly — [human-readable-authoring] owns that standard; this display moment adds a second reason for it. A second /next-side instance landed 2026-06-12, after the standard was decided: the batch again arrived bundled with the gate findings and the Ready ask, with nothing blocking an immediate send — confirming on the /next side that the quote must be sent as its own beat, not just placed first. The backfill-first wait seen in both instances has since dissolved on its own: [hash-backfill-as-hook] shipped and deleted the backfill from /next's pre-flight, so nothing precedes the queue read and the build entry below stands as written. A third instance landed 2026-06-12, in the /plan session processing these very captures: the working item again arrived bundled with its analysis, and the user caught it. The standard could not have been more salient — this batch had been amended minutes earlier in the same session. That settles the mechanism question: session awareness doesn't carry the behaviour; only the installed procedure text does. A fourth instance followed one item later, straight past an explicit in-session promise to send separately: the item needed no file reads, so quote and analysis were composed as one message and bundled by construction — in this harness, only tool work or a message end separates sends. The fix therefore can't be stated as intent ("send first"); the procedure must name what sits between the quote and the analysis.

Build:
- plugin/si-plugin/docs/plan.md Step 2, present-and-interview sub-step: the turn opens with the one-line preamble and the item's verbatim text, sent before any analysis or file reads begin; engagement and sharpening follow in the same turn. Covers unpark candidates the same way — they enter the same loop. Name the separator: after the quote is sent, re-read the item from QUEUE.md to confirm the quoted text matches the file — this read is what makes the quote a send rather than a paragraph, and it catches context-drifted quotes before they're discussed (corrections follow immediately if the file differs).
- plugin/si-plugin/docs/next.md pre-flight: as soon as QUEUE.md is read, check the queue top for a halt marker (a one-line mechanical read — if one sits there, the halt is what gets sent). Otherwise send the top batch verbatim — one preamble line, then the batch text — before the blocker gate and the rest of pre-flight thinking run. Gate findings arrive as follow-up after the batch is visible.

Test:
- Host-side (after push + reinstall): in the next /plan, the quote should land as its own beat before the analysis arrives — not bundled with it; in the next /next, the top batch the same way before pre-flight findings. Needs the deferred-test discipline — flag at /done if it can't run.

**Deferred-test lifecycle: tick state at determination, runnability tails, /plan batch-rolling, reinstall flag** **[deferred-test-lifecycle]**

From a capture raised at the [git-add-safety-hook-gap] /done (2026-06-12); execution channel redesigned at the 2026-06-12 /plan before building. Deferred tests have no execution trigger: the section makes pending tests visible, but nothing tasks anyone with producing the confirming event, so "Confirmed by:" lines describe observations that only happen if someone deliberately acts or happens to notice. [deferred-tests-structural-home] solved surfacing; this solves executing. The trigger-flavor observation is the spine: reinstall-gated tests, the dominant flavor in self-hosting, have a mechanically detectable runnable moment — session_start already reports a version mismatch after a plugin update. Grounded against the current eight-line backlog, runnability splits into deliberately runnable (Claude can produce the event on demand), near-automatic (the event occurs in almost any session), and observational (confirmable only by watching behaviour). Runnability is recorded at authoring time as a prose tail, not a closed taxonomy — the same move as [blocked-by-trigger-flavors]. The original design here extended /next's pre-flight from re-present to re-present-and-offer. Rejected at the amendment: at pre-flight the user came to start a batch, and the backlog is information with no action slot at that moment — host-side lines wait on a reinstall, user-run lines need their own session, and the listing sits between the user and the batch they asked for, growing as lines accumulate. Execution channels through the queue instead: /plan rolls runnable lines into test batches — several gathered into one batch, or single lines attached to a test batch already being authored. Two trigger moments, both judgment rather than a hard count, since accumulation rate is project-local: the Step 1 scan noticing rollable lines, and test-batch authoring time. Test batches only, never build batches: a user-run test riding in a build batch would stop an unattended next→done→next run, and test sessions are already where user involvement is the work itself. External-event lines can't roll; they stay in the section until their event fires. /next's pre-flight deferred-tests step is deleted outright. /done gains a cheap close-out backstop — did this session's own activity confirm a pending line? It pays mainly in self-hosting, where the session's behaviour is the thing under test; it stays universal because no mechanical self-hosting flag exists to condition on, and in a consumer close it costs one section read. Two folds ride along unchanged. From the /clear-resilience discussion: _build.md's Progress has no "couldn't run" state, so a mid-session determination that a test can't run lives only in conversation — post-/clear, /done misreads the unticked entry as unfinished work; the fourth tick state writes the determination into the file at the moment it's made. And the section's scope statement (test-only, shipped-work-only) currently exists nowhere. session_start.py is shared with [session-start-dirty-tree-check] and [plan-state-artifact] — whichever builds second sees the others' changes, per the standing convention.

Build:
- plugin/si-plugin/docs/done.md, Deferred tests section: add the scope statement — the section holds only verification for shipped work; test failures and emergent test needs route to Captures, keeping /plan's ownership of new work. Extend the line format: "Confirmed by:" gains a runnability tail stating whether Claude can deliberately produce the confirming event, the user must, or an external event must fire.
- plugin/si-plugin/docs/next.md, pre-flight deferred-tests step: delete it outright — nothing about deferred tests remains in pre-flight; surfacing moves to /plan.
- plugin/si-plugin/docs/plan.md Step 1 scans: read the Deferred tests section alongside Parked — lines whose tails say Claude-runnable or user-run are rolling candidates, carried into Step 2 as one move (roll these lines into a test batch, or attach to one being planned this session), not per-line interviews. External-event lines stay without comment.
- plugin/si-plugin/docs/plan.md Step 3, near the Test-section guidance: when authoring a test batch, check the Deferred tests section for pending lines that can ride along.
- plugin/si-plugin/hooks/session_start.py: when the version-change report fires and QUEUE.md's Deferred tests section is non-empty, add one line to the report — deferred tests may now be live-testable; /plan can roll them into a test batch.
- plugin/si-plugin/docs/done.md close-out: add the backstop check — read the Deferred tests section; if this session's own activity confirmed a pending line, remove it and record the confirmation in the LOG entry. One section read when nothing fires.
- plugin/si-plugin/docs/next.md Progress formats, plus next-build.md and next-test.md test-entry steps: add the fourth tick state, `- [x] Test description — deferred (reason)`, written at the moment a test is determined unrunnable in this session.
- plugin/si-plugin/docs/done-build.md and done-test.md: verify-completion treats deferred-ticked entries as closeable, not unfinished; the write-deferred-tests step converts each deferred-ticked entry into a queue line mechanically.
- Lifecycle-description sweep — four places currently say /next re-presents the section: QUEUE.md's Deferred tests intro (this project), this project's CLAUDE.md Method docs description (host-only, does not propagate), plugin/si-plugin/templates/CLAUDE-TEMPLATE.md QUEUE.md description, and plugin/si-plugin/templates/faq-template.md's deferred-tests entry. Update each to the new lifecycle: /done writes lines, /plan rolls runnable ones into test batches, /done's close check backstops confirmations.

Test:
- Claude-run: session_start.py against a fixture — version mismatch with a non-empty Deferred tests section adds the line naming /plan; mismatch with empty section stays silent; no mismatch stays silent.
- Behavioural, host-side (after push + reinstall): the first session after the update shows the hook's deferred-tests line; the next /plan proposes rolling the runnable backlog — the current eight lines are the natural exercise; a later /next pre-flight shows no deferred-tests listing. Needs the deferred-test discipline — flag at /done if it can't run.

**Drop the skill-time re-read of plugin-behaviour.md** **[behaviour-doc-double-load]**

session_start injects plugin-behaviour.md in full every session, and /plan, /next, and /done each instruct a re-read — so every skill session carries the largest doc twice. The re-read insures against compaction aging out the injected copy, but paying double on every session to insure against an occasional event is backwards, and the short-session design target (post-June-20 weak-model sessions) shrinks the compaction risk further. Alternatives weighed: dropping the injection instead would gut outside-skill behaviour — mid-session captures happen precisely outside skills — and the progressive-disclosure restructure (compact core injected, full doc at skill time) costs a content split while the doc is still in flux under the queued audits, and is the *larger* footprint for skill sessions anyway since its skill-time load lands on top of the standing core. Revisit the restructure once the compliance arc settles the doc. /setup is deliberately untouched: it runs in unadopted projects where the injection may not fire, so its own load may be the only copy.

Build:
- plugin/si-plugin/skills/plan/SKILL.md, skills/next/SKILL.md, skills/done/SKILL.md: remove the "Re-read them before continuing" instruction. Keep the sentence naming plugin-behaviour.md as governing the skill — authority stays stated; only the duplicate load goes.

Test:
- Self-verifying from doc text. Behavioural watch after reinstall: any rule-leakage observed in a long session post-change is a mandatory capture (possible future: re-inject after compaction if the desktop app ever supports a compaction hook).

**Classify reference roles in the dependency scan: dependency vs evidence** **[dependency-scan-reference-roles]**

The routing gate parks any capture that names another item — "even if Claude reads the reference as incidental." But references run both ways: the observed case (40749f7+1) cited another item as evidence, and the default would have parked the blocker behind the thing it blocks, inverting the graph. The 2026-06-10 /plan confirmed the distribution problem: four captures in one pass carried evidence citations needing narrated overrides — in a capture style that requires including reasoning and origin, evidence citations may be the majority of references, so the default is tuned backwards. As written, every correct override is a rule violation, which trains a weak model to misroute or to treat rules as optional. Fix keeps the mechanism mechanical — classification by linguistic marker, not vibes: forward-looking language ("once X ships," "after Y," "depends on," "needs") keeps the park default; backward-looking language ("observed at," "see," "surfaced during," "from") lifts it, with the recommendation required to name the reference and its role so wrong classification stays user-catchable; ambiguous keeps the park default, the safe side. Matches the "dependency or citation?" language in [queue-format-lint-hook]'s advisory check.

Build:
- plugin/si-plugin/docs/plan.md Step 2 dependency-scan sub-step: replace the "even if incidental" rule with the two-role classification and its marker lists, the narration requirement for evidence-classified references, and the ambiguity default.
- plugin/si-plugin/docs/plan.md Capture and parking discipline, "Routing gate before recommendation" bullet: same change — the canonical statement and the step must not drift apart.

Test:
- Behavioural on the next /plan pass over citation-bearing captures: evidence citations route without false parking, and each classification is named at recommend time.

**State the short-session design target in CLAUDE.md** **[short-session-design-target]**

Observed on the first Fable day: development tipped to one long session, and three procedure gaps surfaced only because session memory covered them — gaps stop hurting under a capable model, so they stop getting found, while consumers and the post-June-20 development model still hit them. All three named gaps now have structural homes ([deferred-tests-structural-home], the push-ritual backfill folded into [hash-backfill-as-hook], and /next's blocker-gate capture scan), but the principle itself lives only in conversation memory — the exact failure mode it names. A third fix shape, a deliberate-freshness regression ritual, was considered and dropped: after June 20 the development model is the weaker model, so every session becomes the regression test naturally, and building a ritual for a ten-day window is process for its own sake.

Build:
- This project's CLAUDE.md, Rules for Claude: add the design-target rule — the system must work for fresh, short sessions on the weaker model; the files must suffice without session memory; conversation memory is a convenience, never a dependency.
- Same file, the route-observations rule (the "all use of the plugin is testing the plugin" bullet): sharpen with the named trigger — any moment Claude notices session memory covering for something the docs or files should carry is a mandatory capture.

Test:
- Self-verifying from doc text. The behavioural check arrives free after June 20: every short weak-model session exercises the contract.

**Install the scope anchor: one definition of build scope, wired through the docs** **[scope-anchor]**
Blocks: [scope-boundary-rule], [trickle-up-next-md-duplicates]

From [scope-distinction-audit]. Build scope has no canonical definition. The working definition assembles from three places, and plugin-behaviour.md — the only doc injected into every session — says "don't fix things outside current scope" without defining current scope. This batch installs one Scope statement in plugin-behaviour.md and points the skill docs at it. The statement also connects the two enforcement layers no doc currently relates: the entries' described work is the definition, enforced by judgment; the Files: list is its mechanical approximation, enforced by the hook as a backstop. A build can stay within listed files and still exceed the described work, so passing the hook never by itself makes work in-scope. The word "scope" also loses its second sense — the Dependency ownership bullet stops using it for project scope, leaving build scope as the word's only meaning. plan.md gains the authoring side: entries feed the lock, so build entries name their files, and scope gets decided at planning time instead of ask-by-ask at build time. Must land before [trickle-up-next-md-duplicates] deletes next-build.md's restatement — otherwise the rule's only remaining statement uses a term no doc defines.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md: add the Scope statement — build scope is the active batch's entries' described work; the Files: list in _build.md is its mechanical approximation, enforced by the pre_tool_use hook as a backstop; passing the hook never by itself makes work in-scope; work outside scope routes to Captures.
- plugin/si-plugin/docs/plugin-behaviour.md, Dependency ownership: reword "The user owns scope" to "The user owns what enters the queue, what gets parked or dropped, and whether a build expands."
- Grep "scope" across the procedure docs for other project-scope-sense uses; reword those the same way. Build scope becomes the word's only remaining meaning.
- plugin/si-plugin/docs/next.md and next-build.md: point their scope-definition statements at the anchor instead of restating it; keep the skill-specific rules. Locate by content, not line numbers.
- plugin/si-plugin/docs/next-build.md, Scope management: reword the scope-expansion ask from file-shaped to work-shaped — name the work, then the files it needs, listed or not — so work growing inside an already-listed file triggers the same ask a new file would.
- plugin/si-plugin/docs/plan.md Step 3, near the batch structure: build entries name the files they touch; the scope-lock is populated from them; an entry naming no files leaves the lock at method-docs-only. Files that don't exist yet count as named when the entry says what gets created and where.
- plugin/si-plugin/docs/plan.md, readiness gate: add the matching check — can the Files: list be populated from these entries?

Test:
- Grep the definition phrasing across the docs after the edit: one canonical statement in plugin-behaviour.md, pointers elsewhere.
- Grep "scope" for surviving project-scope-sense uses — expect none.

**Define the boundary moves: the discovery decision rule and routing move, stated once** **[scope-boundary-rule]**
Depends on: [scope-anchor]

From [scope-distinction-audit], two findings that are one thought. First: Claude-noticed out-of-scope discoveries have no defined routing move — "note them for the queue" names no destination, no mechanics, no timing, so a weak model can hold them in conversation memory, the exact failure the short-session design target forbids. The fix collapses the three-way split by noticer: who noticed doesn't change the artifact, so Claude-noticed discoveries take the same capture flow user-raised items already get — draft, show, "anything else?", resume — at the moment of noticing. Test failures keep their at-close path; interrupting a test run is the one case with a real reason to defer. Second: the decision rule for mid-session discoveries is real but never stated — needed → ask or split; not needed → capture and continue; premise broken → halt — visible only across five separate passages. It gets stated once, in plugin-behaviour.md beside the routing move, because "not needed → capture and continue" is that move; duplicating it per skill doc recreates the drift the trickle-up arc is removing. The skill docs' sections then read as elaborations of one rule.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md, Routing and discipline: replace "note them for the queue" wording with the defined move — Claude-noticed discoveries route to Captures at the moment of noticing, per the same capture flow as user-raised items (draft, show, "anything else?", resume).
- plugin/si-plugin/docs/plugin-behaviour.md, same spot: state the decision rule once — needed to complete the batch's entries → ask to add (minor) or propose splitting (significant); not needed → capture and continue; premise broken → halt and course-correct.
- plugin/si-plugin/docs/next-build.md (Rules during build) and next-test.md (Rules during test): replace their "note them for the queue" wording with a pointer to the defined move. Locate by content, not line numbers.
- plugin/si-plugin/docs/next-build.md and next-test.md, Scope management: open each section with a pointer to the decision rule so the existing passages read as its elaborations.

Test:
- Grep "note them for the queue" (and close variants) across the procedure docs after the edit — expect zero hits.
- Behavioural: the next /next session that meets a Claude-noticed discovery routes it at the moment of noticing, not "for the queue" at an undefined later.

**Remove rule duplicates from next.md and the per-type docs** **[trickle-up-next-md-duplicates]**
Depends on: [scope-anchor]

next.md and the per-type docs restate four rules that plugin-behaviour.md already carries: SPEC read-only (next-build.md, next-test.md), don't fix outside scope (next-build.md), state regressions plainly (next-build.md, next-test.md), one build at a time (next.md). Wording has already drifted slightly between copies — the cost of duplication made visible. Trickle-up discipline: plugin-behaviour.md is the canonical home; skill docs carry only what's skill-specific. This extends the same bet as [behaviour-doc-double-load]: post-dedup, these rules live in the session-start injection alone — the consistent direction, not a new exposure. Locate every removal by rule text, not the capture's line refs — the docs have been edited since filing.

Build:
- plugin/si-plugin/docs/next-build.md: remove the SPEC read-only, don't-fix-outside-scope, and state-regressions-plainly restatements. Keep the section's skill-specific rules (scope-expansion ask, REGISTRY not build scope).
- plugin/si-plugin/docs/next-test.md: remove the SPEC read-only and state-regressions-plainly restatements.
- plugin/si-plugin/docs/next.md: remove the one-build-at-a-time restatement. Keep entries-are-the-contract and per-entry ticking.

Test:
- Grep the four rule phrasings across next.md and the per-type docs after the edit — remaining hits should be in plugin-behaviour.md only.

**Make SPEC a normal doc: spec edits become a planned build batch** **[spec-edit-batch-type]**
Depends on: [scope-anchor]

Decided 2026-06-13. Right now SPEC.md is special. It is read-only during builds (the pre_tool_use hook enforces this) and edited directly in /plan. That special case caused confusion — a direct SPEC edit during a /plan read as off-script even to the designer. This batch makes SPEC a normal doc, changed only through a planned spec-edit build batch, like any other doc.

Dropping the read-only lock is safe because scope-lock already does the lock's real job. The lock existed to stop a build from editing the spec it builds against — grading its own homework. A feature build does not list SPEC.md in its Files, so scope-lock alone keeps it from touching SPEC. Spec changes get their own batch, separate from any feature build, so no build edits its own contract. The "decide in planning" split survives: authoring the spec-edit batch in /plan is the decision, and /next only does the typing. This sequences after [scope-anchor] because that batch hardens scope-lock's definition, and once the read-only lock is gone, scope-lock is SPEC's sole protector.

This batch creates the spec-edit mechanism but cannot use it on itself. Its build runs under the current host, where the read-only lock is still active until reinstall, so the build cannot edit SPEC.md. The one SPEC change this work implies — rewording SPEC's hooks description — is therefore deferred to the first spec-edit batch, authored after this ships and reinstalls.

Build:
- pre_tool_use.py: remove the SPEC.md read-only-during-builds rule; scope-lock alone governs SPEC. Make sure the empty-Files method-docs fallback does not let a build edit SPEC by default.
- plan.md: add spec-edit as a batch type in the Step 3 batch structure, alongside Build/Test/Audit (and Freeform once it ships). Add a /plan step that authors spec changes as a spec-edit batch.
- plugin-behaviour.md and plan.md pipeline wording: change "idea → SPEC.md → QUEUE.md" to "idea → decide in /plan → spec-edit batch → /next edits SPEC → feature batch".
- This project's CLAUDE.md: reword "Edit it only during /plan" to the new model.
- done.md / done-build.md: a spec-edit batch closes like any build.
- post_tool_use.py lint: add spec-edit to the allowed batch subheadings.

Test:
- Claude-run: pre_tool_use.py against a fixture — a build with an empty Files list cannot edit SPEC.md by default.
- Behavioural, host-side (after push + reinstall): a /next spec-edit batch edits SPEC.md without being blocked, and a normal feature build still cannot touch SPEC unless it is in scope. Needs the deferred-test discipline — flag at /done if it can't run.

**Generalize ask-when-unsure into plugin-behaviour.md** **[trickle-up-ask-when-unsure]**

next.md's "Unsure about an implementation choice? Ask. Don't guess and build wrong" is universal — /plan ordering calls, /setup scaffolding choices, /done routing decisions — but lives only in next.md, so every other skill runs without it. Trickle-up: the generalized rule belongs in plugin-behaviour.md Communication, adjacent to the web-search bullet so the two read as one decision rule with two branches — uncertain about an external fact → offer a search; uncertain about a choice the user owns → ask, don't guess and proceed. One deliberate addition beyond the capture as filed: a self-contained line in setup.md, because unadopted sessions get no behaviour-rules injection (confirmed in session_start.py this session) and /setup's scaffolding choices are a named use of the rule — setup.md carries its own copies by design. Same next.md rules area as [trickle-up-next-md-duplicates] touches; no ordering between them, placed adjacent for one-session convenience.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md Communication, next to the web-search bullet: add the generalized rule — when uncertain about a choice the user owns (implementation, scaffolding, routing), ask; don't guess and proceed.
- plugin/si-plugin/docs/next.md: remove the local copy (locate by rule text, not line ref).
- plugin/si-plugin/docs/setup.md: add one self-contained ask-when-unsure line where scaffolding choices are made.

Test:
- Grep the rule phrasing after the edit: present in plugin-behaviour.md and setup.md, gone from next.md.

**Queue-visible plan markers: write predictable planning moments into the queue** **[queue-plan-markers]**

Claude keeps recommending "run /plan first" at moments that feel unexpected to the user, but a subset of those moments is predictable when the queue is authored — an audit batch will file findings the next batch depends on; a batch's dependencies can only be estimated after a design decision a planning session has yet to make. Writing those moments into the queue converts a judgment-based session-end recommendation into a mechanical gate (weak-model friendly, the same bet as the push marker), makes the planning rhythm visible before it's hit, and carries the reason inline. Floor, not ceiling: planning must happen here at minimum, for the stated reason; ad-hoc /plan elsewhere stays unrestricted. Part of the autopilot prerequisite arc named in the cruise-control trigger. The FAQ entry for the marker is deliberately not in this batch — it rides with the FAQ-trigger capture's routing.

Build:
- plugin/si-plugin/docs/plan.md Step 3 (ordering/placement work): add the authoring rule — when placement puts an audit batch ahead of batches that depend on its findings, or queues a batch whose dependencies wait on an undecided design question, insert "--- Plan session here: <reason> ---" between batches at that spot. Name the two cases as illustrations, not a closed list.
- plugin/si-plugin/docs/plan.md Step 1: when the marker sits at the queue top, addressing its stated reason is part of this session's work; remove the marker once addressed.
- plugin/si-plugin/docs/next.md pre-flight: halt on a plan marker at the queue top, sibling to the push-marker halt — tell the user a planning session is needed and name the marker's reason.
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md and this project's CLAUDE.md (QUEUE.md format descriptions): document the marker line so it's recognizable in consumer projects.
- plugin/si-plugin/templates/faq-template.md (+ index line): FAQ entry explaining the plan-marker line a consumer may meet in their queue — what it means, what to do (run /plan).

Test:
- Self-verifying from doc text. Behavioural confirmation arrives naturally: the next /plan that authors an audit batch with dependent work should insert a marker; the next /next that meets one should halt and name the reason.

**FAQ entries become part of batch authoring** **[faq-authoring-trigger]**

The FAQ ships as faq-template.md, authored in this project and scaffolded to consumers at /setup — yet nothing routinely updates it: entries happen only when a batch explicitly includes one (observed once, [narrate-build-md-purpose]), and the pre-push sweep drift-checks existing answers without ever asking whether new concepts lack coverage. This is the FAQ twin of the spec-entry trigger, keyed at the same prospective moment — batch authoring. It's a host-project rule, not shipped plan.md: consumers never author FAQ entries, so the rule would misfire in their /plan sessions. The push-sweep coverage backstop was considered and held — the observed failure is no-trigger-at-all, not a leaking trigger; the sweep is already heavy; ship the rule and watch, add the backstop only if entries still slip through. The existing backlog is [faq-coverage-audit]'s job; already-queued batches introducing consumer-visible concepts ([queue-plan-markers], [deferred-tests-structural-home]) got FAQ entries added at routing time.

Build:
- This project's CLAUDE.md (host-only, does not propagate), with the self-hosting conventions: add the rule — when /plan authors a batch that introduces something a consumer would see or ask about (a new queue line, a new doc section, a new narration moment), the batch carries a faq-template.md entry (plus its index line) in its build list. The test mirrors the spec-entry trigger: would a non-coder meeting this change have a question the FAQ doesn't answer?

Test:
- Self-verifying from the rule text. Behavioural: the next /plan authoring a consumer-visible batch should include the FAQ entry without prompting.

**One-time FAQ coverage audit against the current plugin** **[faq-coverage-audit]**

[faq-authoring-trigger] only fixes the future. The FAQ's 13 Q&A pairs date from its original authoring; concepts shipped since have never been coverage-checked — the pre-push sweep only checks existing answers for drift. One sweep catches the backlog; findings route to Captures per the audit contract.

Audit:
- Target: plugin/si-plugin/templates/faq-template.md and faq-index-template.md, read against the consumer-visible concept surface of the current procedure docs (setup.md, plan.md, the next and done families, plugin-behaviour.md) and the scaffolded doc formats.
- Criteria: every shipped concept a non-coder consumer would meet and ask about, checked for an answer; and the reverse gap — existing answers naming concepts that no longer ship. For each finding: the concept, why a non-coder would ask, and whether the entry is missing or stale.

**No planning work in execution skills** **[no-planning-in-execution]**

The boundary between /plan and the execution skills rode on "no thinking work," which was the wrong axis — Claude thinks plenty while executing, and the audit auto-file direction deliberately leans on Claude's thinking. The real boundary is planning work: processing captures — routing, promoting, parking, deciding their fate — and the human decision-making that entails. Capture-making stays open to every session type (the never-restrict-ideation principle); capture-processing is /plan's monopoly. Observed leak: [output-tag-audit] seeded a reconciliation item whose resolution was a planning decision made mid-/next, its reasoning landing where no planning session looks. Part of the autopilot prerequisite arc named in the cruise-control trigger: unattended next→done→next is only safe if no decision the user must own can arise mid-run. plan.md's thinking-work ground rule stays as the /plan-side gate on what gets queued ([audit-definition] is rewriting it); this rule is its execution-side counterpart, living where execution sessions actually load rules.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md: add the rule, compliance-hardened from the start (why-clause, positive constraint, explicit scope, per resources/research/model-instruction-compliance.md): no planning work in any execution skill — planning work is processing captures (routing, promoting, parking, deciding their fate); making and approving captures is open to every session type; processing them happens only in /plan. Scope: all execution session types, including any added later. One clarifying line for test sessions: the user's involvement in running tests and judging outcomes is the work itself, not planning; filing those outcomes is capture-making.

Test:
- Self-verifying from the rule text. Behavioural: the next /next session that meets a routable discovery should append it to Captures and move on — no routing discussion mid-execution.

**Audit findings: one numbered set, bulk approval, contested items one at a time** **[audit-findings-bulk-approval]**

The per-finding capture-or-drop loop is the most interactive /next shape there is, and it duplicates /plan — every surviving finding judged twice. The original capture proposed removing approval entirely (mechanical auto-file); revised at routing: the [output-tag-audit] live preview validated bulk approval, not zero approval — findings 2–10 were batch-drafted and batch-approved in one pass, so the friction was the round-trips, and a session whose output the user never sees gives no reason to run it interactively. Bulk approval keeps the Captures always-show rule fully intact (no approval exemption needed — the caveat lands in the sequencing rule instead) and stays within [no-planning-in-execution]'s "making and approving captures." Full no-approval auto-file moves to cruise control's design scope: straight-to-Captures is autopilot behaviour. Double judgment still dies: one bulk ask in /next, full per-finding judgment once, in /plan. Absorbs the next-audit.md half of the [output-tag-audit] routing-loops tag finding — the new flow is authored with its tags correct from the start.

Build:
- plugin/si-plugin/docs/next-audit.md: replace the per-finding route-approved-findings loop with the bulk flow — compile all findings, present them as one numbered set in a single message, ask the user to approve the set or list the numbers they don't accept as-is, cover contested ones one at a time (reword or drop), append the approved set to Captures, report the filed count at close. Tag the bulk ask and the contested-item loop correctly from the start.
- plugin/si-plugin/docs/next-audit.md, same rewrite: the new close defines its review tail from birth — reviewing means re-examining what was already found, not raising new work; anything new routes through the existing paths (out-of-scope via scope management, thinking work via Captures). From a [close-out-audit] finding (e120f3d): the current "keep reviewing" tail is undefined, leaving open the new-work-smuggling risk next-build.md's tail was hardened against.
- plugin/si-plugin/docs/plugin-behaviour.md Communication, sequencing rule: add the bulk-approval inversion alongside the existing alternatives inversion, hardened (why-clause, positive constraint, explicit scope) — a deterministic result set produced by user-approved criteria is presented as one numbered message for bulk approval; the ask invites listing contested numbers; contested items then run one at a time. One-item-at-a-time stays the default everywhere else.
- plugin/si-plugin/docs/done-audit.md: the LOG entry records bulk-step outcomes — findings rejected or reworded at approval, with reasons — so nothing decided at audit time goes unrecorded.

Test:
- Self-verifying from doc text. Host-side behavioural (after push + reinstall): the next audit session presents one numbered set — [faq-coverage-audit] is queued as the natural first exercise. Needs the deferred-test discipline — flag at /done if it can't run.

**Tag application across the next and done families** **[next-done-tag-sweep]**

From [output-tag-audit], its headline finding. The procedure docs use response-shape tags to control when Claude speaks. In next-build.md and next-test.md, the whole Execute step — where Claude does the build work — is tagged [SILENT]. But that step contains moments that must speak: reporting a failure, asking before scope grows, handing a user-run test over. A literal-minded weak model gets two contradictory instructions at those moments. It either breaks the silence tag, or honours it by suppressing a failure report — the dangerous case. The fix has two parts. Each speaking moment gets its own tag, because a tag on the specific moment overrides the tag on the surrounding step. And Execute gets one clarifying line: silence covers routine bookkeeping when things go fine; failures, asks, and handoffs always speak. This was the only audit finding needing new wording — every other finding is plain tag placement. Sibling tag findings from the same audit fold into this batch as they route. Locate every edit by content, not by the audit's line numbers — the docs shift under other queued batches.

Build:
- plugin/si-plugin/docs/next-build.md and next-test.md, Execute step: add the clarifying line — silence governs success-path bookkeeping; failures, asks, and handoffs speak.
- Same two docs, inside Execute: tag the scope-expansion ask and the user-run test handoff [PROMPT]; tag failure noting [BRIEF].
- Same two docs, Scope management: tag the scope-growth asks [PROMPT]. In next-build.md, "Scope grows during the build" takes the tag at section level — both its paths ask and wait. In next-test.md, "Test surfaces unexpected scope" takes it on the minor-case ask only — the significant case notes for the queue and continues, so a section-level tag would force a wait that shouldn't happen. Restores symmetry with the already-tagged "User raises something out of scope" sibling.
- plugin/si-plugin/docs/next.md pre-flight: tag the push-marker halt [BRIEF]. Tag the blocker gate's surfacing moments [BRIEF]. Tag [PROMPT] where a user decision gates proceeding — the deferred-tests check and the capture-overlap recommendation. By the time this batch runs, [deferred-tests-structural-home] and [queue-plan-markers] may have reshaped this gate; tag the text as it stands then.
- done-build.md, done-test.md, done-audit.md: tag the route-to-Captures approval loops [PROMPT] — the close-out steps where leftover findings are drafted into Captures for the user's approval. The routing prose stays; only the tag is added. The matching next-audit.md loop is not in this batch — [audit-findings-bulk-approval] replaces it wholesale, tagged from birth.
- done.md and the three sub-docs, close-out moments: tag the unticked-entries ask (finish or close partial) [PROMPT] in done-build.md, done-test.md, done-audit.md. Give the staleness sweep in all three the path-split treatment next.md's pre-flight already models — [SILENT] when clean, [BRIEF] when flagging. Tag done.md's router [SILENT] to match its own "don't ask" prose. Tag the minor bookkeeping moments [SILENT]: the registry update in done-build.md, the _build.md deletion in all three.

Test:
- Self-verifying from doc text. Watch later /next sessions: failure reports and scope asks speak; success-path bookkeeping stays silent.

**Trim tag-definition restatements from plan.md** **[tag-restatement-trim]**

From [output-tag-audit]. Four spots in plan.md restate in prose what the response-shape tag definitions already say — "one item at a time" beside [SEQUENCE], "don't narrate the absence" beside [SILENT]. The audit flagged a tension: trimming prevents the copies drifting apart, but local restatement also props up weak models. Resolved at routing: the propping has already been paid for centrally — the hardened definitions carry their own why-clauses and constraints — so keeping the restatements buys the same insurance twice while leaving wording to drift. The line to apply: trim where the hardened definition fully covers the content; keep prose that adds step-specific substance. The audit also flagged next-audit.md's "Don't preview upcoming findings," but that line lives in the section [audit-findings-bulk-approval] replaces wholesale, so it dissolves on its own and stays out of this batch. setup.md is excluded entirely — its restatements are load-bearing because its sessions may never load the definitions (separate finding). Locate every spot by content, not the audit's line numbers. Folded in at the 2026-06-12 /plan, user-caught: the same Step 2 ordering line names the processing order "oldest first," but Claude-directed placement means file order and age order diverge — an item placed next to its relatives jumps the age queue by design, so the name promises an order the file no longer guarantees. The rename rides here because this batch already edits that line.

Build:
- plugin/si-plugin/docs/plan.md, four restatement spots: the ground-rules "One item at a time" line, Step 2's one-at-a-time/never-preview restatement (keep the ordering content — candidates first, file order, count scope — it's step-specific), the gap-noticing "One at a time," and "don't narrate the absence" after the Test-section [SILENT]. Apply the line above to each. Treat the ground-rules spot with care: no tag sits on the ground rules or Step 1, so the line may be covering territory the [SEQUENCE] definition doesn't reach there — if so, it stays.
- plugin/si-plugin/docs/plan.md Step 2, same ordering line: rename the processing order from "oldest first" to file order, top to bottom. Age order is only the append fallback at filing time (plugin-behaviour.md Captures placement); processing follows the file as placed. Sweep plan.md for other "oldest first" uses describing processing order and rename those too — filing-fallback uses ("oldest-first as the fallback") are correct and stay.

Test:
- Self-verifying from the doc text. Behavioural watch on later /plan sessions: one-at-a-time discipline holds without the trimmed prose; any leakage is a mandatory capture.

**Ship freeform: a fourth /next type for unqueued work** **[ship-freeform-next-type]**

Demand is observed, not speculative: twice in one day the work had no plugin path — an ad-hoc audit run with the plugin switched off, and a session that wanted captures surfaced without processing pressure — plus a general need for somewhere to discuss changes already made. Freeform is the fourth /next type for that work. Two forms ship together. Queue-driven: /plan scopes planned freeform work as a batch and /next picks it up. On-demand: `/next freeform` with no queued batch. Both pass the same gate first — could this be build, test, or audit? — with a one-line answer for why none fit; the gate runs in /plan for queue-driven and at session start for on-demand. Freeform is a refuge from ceremony, not from discipline. The scope lock holds, with files granted ask-by-ask by the user. Captures may be made but never processed — [no-planning-in-execution] already covers freeform through its written scope, no amendment needed. Freeform has no completion signal — nothing to tick — so it gets no Completion section: the session closes when the user runs /done, and the context-running-long nudge is the only close prompt Claude initiates. Expectation over time: recurring freeform shapes surface real new types, the way the audit type emerged. SPEC.md was updated at routing. Absorbs [freeform-on-demand]; both items leave Parked into this batch.

Build:
- plugin/si-plugin/docs/next.md router: add the freeform branch — a queued freeform batch at the top, or `/next freeform` with none. For on-demand, run the gate: ask whether the work could be build, test, or audit; require the one-line why-none-fit before proceeding.
- New doc plugin/si-plugin/docs/next-freeform.md: the procedure. Scope lock ask-by-ask — _build.md's Files list starts empty, and each file the work needs is requested and appended once the user grants it. The captures-append constraint: when the session yields captures, warn that /next can only append them, not process them, and offer the choice — move this to /plan now, or continue and process later. No Completion section. Authored with its response-shape tags correct from birth.
- plugin/si-plugin/docs/done.md router plus new done-freeform.md: record a freeform session — LOG entry describing what happened and what changed, registry check, commit. No batch to return, nothing to tick. Authored with tags from birth.
- plugin/si-plugin/docs/plan.md Step 3: the queue-driven shape — a Freeform subheading for planned freeform work, with the authoring-time gate (one line on why build, test, and audit don't fit).
- plugin/si-plugin/hooks/ lint hook (ships earlier in the queue): add Freeform to the allowed batch subheadings — its own batch notes this list must grow when new types ship.
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md: describe the freeform form in the workflow section.
- plugin/si-plugin/templates/faq-template.md (+ index line): FAQ entry — what a freeform session is, when to reach for it, and what it won't do (process captures).

Test:
- Self-verifying from the doc text for structure. Behavioural: the next real freeform need runs through `/next freeform` instead of switching the plugin off — the originally observed case is the natural live test. Host-side (after push + reinstall) — flag at /done if it can't run; needs the deferred-test discipline.

**Memory gets boundaries: enumerate what it must never hold, free the rest** **[memory-rule-boundaries]**

User direction, 2026-06-11. The route-observations rule's memory clause ("Not to memory, not discussed and dropped") is a blanket veto with no boundary, which makes it both too strong and too weak: it reads as forbidding memory entirely, while giving a weak model no list to check against. The tightened form enumerates what memory must never hold — project records that system docs own — and explicitly frees memory for everything else. Must-not-hold: behaviour observations and testing outcomes (Captures), design decisions and their reasoning (QUEUE, SPEC, LOG), project state and constraints (the method docs), procedure gaps noticed mid-session (Captures). Free: user preferences, working style, communication feedback, cross-project facts. Resolved at routing: consumers get their own version — their Claude has the same memory feature and a worse misroute risk, since memory is invisible to them, unversioned, and machine-local; a design decision saved there never reaches their project docs. Files over memory, in consumer clothes.

Build:
- This project's CLAUDE.md (host-only, does not propagate), the route-observations rule: replace the blanket "Not to memory" with the enumerated must-not-hold list and the explicit freed remainder, as above.
- plugin/si-plugin/docs/plugin-behaviour.md: add the consumer-facing version, compliance-hardened from the start (why-clause, positive constraint, explicit scope per resources/research/model-instruction-compliance.md) — project records belong in the project's docs, never in Claude's memory: ideas and discoveries to Captures, design decisions to QUEUE and SPEC, project state to the method docs. Memory stays free for what no project doc owns: user preferences, working style, communication feedback, cross-project facts. The why: memory doesn't travel with the project and the user can't read it; the method docs are the project's record.

Test:
- Self-verifying from the rule text. Behavioural watch: the next session where an observation or decision surfaces mid-work routes it to the docs, and memory use for preferences continues without hesitation.

**/done reads _build.md unconditionally; memory enriches, never substitutes** **[done-unconditional-read]**
Depends on: [scope-boundary-rule]

Raised by the user (2026-06-12): people may /clear between a skill's work and /done, even if advised not to. /clear can't be hooked before it happens, and blocking it isn't the design anyway — the files must suffice at that seam. The observed slip: the last /done skipped the mandated _build.md read, plausibly a judgment call because the whole build session was in memory. That call works same-session and breaks exactly when it matters — post-/clear and post-compaction, when the session feels remembered but the details are gone. A "read it if you don't remember the session" condition was considered and rejected: it hangs on Claude assessing its own memory, which fails in the post-compaction case. The decided form inverts it: the read is unconditional, and conversation memory enriches the record but never substitutes for the read. Side benefit: a same-session /done that reads the file while still remembering the build notices when ticks or Changes notes don't match what happened — the only routine check _build.md's quality ever gets before a fresh session needs it. The findings steps in all three sub-docs name "the conversation" as a source, which institutionalizes the memory dependence; they get reworded so files are the record. The dependency is real: [scope-boundary-rule] is what routes Claude-noticed discoveries to Captures at the moment of noticing, making "flagged items are already in files" true for the reworded findings steps.

Build:
- plugin/si-plugin/docs/done.md, the router's "_build.md exists → read it" line: harden into the canonical rule, compliance-hardened from the start (why-clause, positive constraint, explicit scope per resources/research/model-instruction-compliance.md) — the read is unconditional regardless of what the session remembers; conversation memory enriches the LOG entry (tradeoffs, learnings, colour) but never substitutes for the read; a memory-state condition fails post-compaction, when the session feels remembered but isn't. Stated once here; the sub-docs route through it.
- plugin/si-plugin/docs/done-build.md, verify-completion step: add the reconcile line — where the file and session memory disagree (work done but unticked, Changes notes missing something memory knows happened), the mismatch is itself a finding about build discipline and routes to Captures.
- plugin/si-plugin/docs/done-build.md findings step, done-test.md findings step, done-audit.md stragglers step: reword "Check _build.md and the conversation" — the record is _build.md's notes plus Captures already routed at noticing; conversation, when present, is a same-session bonus sweep, never a source the step depends on. Locate by content, not line numbers.
- plugin/si-plugin/templates/faq-template.md (+ index line): FAQ entry — "Is it safe to clear the conversation or start a new session between steps?" After /done, yes: everything is recorded and committed. Before /done, the plugin recovers from its working file, but closing with /done first is the clean habit.

Test:
- Self-verifying from doc text for the rewording. Grep "and the conversation" across the /done sub-docs after the edit — expect zero hits in findings steps.
- Behavioural, host-side (after push + reinstall): the next /done that runs in the same session as its build visibly reads _build.md before Phase 1. Needs the deferred-test discipline — flag at /done if it can't run.

**Commit messages derive from the LOG entry: two authored texts, four renditions** **[closeout-text-collapse]**
Depends on: [approval-display-blockquotes]

From a capture filed at the 2026-06-12 /done close. /done authors four renditions of the same session facts — index entry, LOG entry, commit title, commit body — and the user sits through each. The renditions correlate in pairs: the index entry and commit title are both one-liners; the LOG entry's rationale and the commit body are both the session story. The collapse makes each correlation literal. Two texts get authored: the one-liner (usually pre-existing — /next generates it as the index entry candidate) and the rationale prose. The one-liner serves as entry heading, index line, and commit title. The rationale serves as entry body and commit body. The user approves the LOG entry once; everything else derives mechanically with nothing new to read. The commit-time ask survives only for the real decision it carries — commit and push, or just commit. Weighed and rejected at routing: dropping the index in favour of reading git log — the index is curated (one line per session; history is full of push-ritual and bump commits), its line ends with the entry filename so retrieval is one hop, and post-collapse it costs nothing to keep, being a mechanical copy of approved text. Also rejected: backfilling old commit messages — rewriting a message changes that commit's hash and every descendant's, invalidating every hash the system has recorded, and needs a force-push the file-safety rules ban; unnecessary anyway, since LOG entries are committed files and the why-pipeline already lives in git as content. One correction recorded from the capture: git log -S searches diff content, not commit messages, so commit-title choice never affected the hash backfill — that consideration is neutral. Commit-title length conventions are already moot in this repo's history. The Depends on is file-collision ordering, not semantic: [approval-display-blockquotes] rewrites the commit core's presentation step (its confirmed offender is the fenced commit message), and this batch reshapes the same step after it. The post-close-captures capture still in Captures interacts — a single text finalizes earlier, widening that gap — and is deliberately left to its own routing, aware of this decision. Folded in from a capture at the plan-2026-06-12-4 /done (e51cf40): the collapse makes multiline commit bodies the norm, and the first such commit broke when passed inline. The capture's stated cause — "PowerShell 5.1 has no heredoc" — is wrong; PowerShell has here-strings (`@'...'@`), but their column-0 closing-token rule makes a generated multiline `-m` string brittle to produce correctly, and the session fell back to the Bash tool. The real lesson is broader than one shell: inline multiline strings are brittle to generate anywhere. The fix is therefore one unconditional mechanism, not a per-shell branch — write the message to a file and commit with `git commit -F`, which sidesteps quoting on every machine and matches the weak-model design target of no which-shell judgment. Folded in from a capture at the [audit-definition] /done (ef3220a), the first live run of the derived message: Claude presented the body as a description of the derivation ("the rationale as approved, plus one appended line…") rather than stating the identity plainly, and the user couldn't tell what had been done — a meta-description reads as a third text existing, defeating the nothing-new-to-read point. The presentation must state the identity in plain words and show only what is genuinely new.

Build:
- plugin/si-plugin/docs/done.md commit core: replace "Draft the commit message title and body" — the title derives from the entry's one-liner, the body from the entry's rationale prose; the entry approval already covered both, so the commit step asks only the commit-and-push question, never a fresh review. Present it by stating the identity plainly — the title is the index line's text verbatim, the body is the approved rationale verbatim — and showing only what is genuinely new, never a meta-description of the derivation. Allowance: when the commit stages extras beyond the session story (hash backfills, sweep edits, rolled-in user edits), the body appends one line naming them, and that appended line is the one genuinely-new text the presentation surfaces.
- plugin/si-plugin/docs/done.md commit core: state how the commit message is passed — write it to a file and commit with `git commit -F <path>`, then remove the file; one shell-agnostic mechanism, not inline `-m` with embedded newlines and not a heredoc branch. Flag for the build to verify: the message file must be writable at commit time despite _build.md's scope-lock — resolve by path choice, by timing (if _build.md is already deleted at the commit step), or by how the file is written.
- plugin/si-plugin/docs/done.md LOG entry files section: state the one-text identity once — the entry heading's one-liner, the index line's body, and the commit title are the same authored text in three positions.
- plugin/si-plugin/docs/done-build.md, done-test.md, done-audit.md, done-plan.md, entry-approval steps: one line each — this approval also covers the commit message, which derives from this text; points at the commit core's statement.

Test:
- Self-verifying from doc text. Behavioural, host-side (after push + reinstall): the next /done runs one entry approval, then a commit step showing a derived title and body with only the commit-and-push ask. Needs the deferred-test discipline — flag at /done if it can't run.

**Post-close captures update the entry's routed line as a working-tree edit** **[post-close-capture-record]**

From a capture raised at the [doc-crossrefs-by-name] /done close (2026-06-12). Captures filed in a session's post-commit tail have no session record: the LOG entry's "Routed to Captures:" line is approved and committed before they exist — that session's entry said "none" while two captures originated in its tail. The fix reuses an existing pattern. When a capture is filed after the commit, the same move that appends it to QUEUE.md also updates the just-written entry's "Routed to Captures:" line as a working-tree edit, with no separate commit — the edit rides into the next session's commit, exactly as hash-backfill edits do. The entry converges to truth and attribution stays with the session the capture came up in. Checked at routing: the hash backfill resolves the entry's commit from committed history, so the uncommitted edit doesn't disturb it. Weighed and rejected: recording tail captures in the next session's entry — cross-entry attribution relies on the next session noticing, a judgment step on the path weak sessions fumble, and the log records captures by when they came up; a dedicated follow-up commit per tail capture — truth-preserving but adds ceremony exactly where the session is winding down, and tail captures arrive in clusters; accepting the gap — the capture's inline origin makes QUEUE.md a sufficient record, but it leaves the session entry knowingly false on one line. Interaction accepted: with [closeout-text-collapse], the committed copy of the entry (and commit body) permanently says what was routed as of commit time, while the entry file — the canonical record — carries the correction; git shows the correction landing in the next commit. No dependency header: the design works whether or not the collapse has shipped — adjacency, not a gate.

Build:
- plugin/si-plugin/docs/done.md, beside the LOG entry files section: add the post-close captures rule — a capture filed after this session's commit also updates the just-written entry's "Routed to Captures:" line, as a working-tree edit with no separate commit; the edit rides into the next session's commit, same pattern as the hash backfill. Carry the why: the entry is the session's record, and captures belong to the session they came up in.

Test:
- Behavioural, host-side (after push + reinstall): the next post-close tail capture updates the entry's routed line uncommitted; the next session's commit carries both; the hash backfill still resolves the entry to its /done commit. Needs the deferred-test discipline — flag at /done if it can't run.

**Recommend-next states the scan result both ways: clean case codified, audit gap absorbed** **[done-recommend-next-both-ways]**

Raised by the user at the [doc-crossrefs-by-name] /done (2026-06-12): the close-out assessment has been landing well, but only half of it is codified. The recommend-next step in the /done sub-docs runs the unprocessed-Captures overlap scan and speaks only when something blocks — overlap found → recommend /plan and name it. The clean case (captures waiting, none touching the next batch, /next can proceed) has no instruction behind it: "the three waiting captures don't touch it, so nothing blocks it" was judgment, not procedure. That's the [short-session-design-target] gap class — behaviour the user values, carried by session finesse, which a fresh weak-model session may not reproduce. The fix states the scan's result in all three states: Captures empty (nothing waiting for /plan), waiting but clean (what's waiting, with the plain verdict that nothing blocks), overlap found (the existing rule). The clean-case line reads as plain assessment, not a hedge. Absorbed: [done-audit-overlap-scan], from a [close-out-audit] finding (e120f3d) — done-audit.md is the only sub-doc whose recommendation skips the scan entirely; the gap bites when an audit routes nothing, since pre-existing captures overlapping the top batch would go unflagged and the close would recommend /next, the exact case the scan exists to catch. Folding it here lands the scan and the both-ways rule in done-audit.md in one pass and keeps the wording identical across all four sub-docs.

Build:
- plugin/si-plugin/docs/done-build.md, done-test.md, done-plan.md, recommend-next steps: extend the overlap-scan instruction to state the result either way — what's waiting for /plan (empty, or the waiting items) and whether it blocks the next batch. The clean case is a plain assessment; include one good/bad example pair pinning the tone ("Three captures are waiting; none touches the next batch — nothing blocks it," not a hedge about overlap possibly being worth checking). Identical wording in all three. Locate by content, not line numbers.
- plugin/si-plugin/docs/done-audit.md Phase 3, nothing-routed branch: add the overlap scan with the same both-ways rule and wording — the scan and the result statement land together in one edit, absorbing [done-audit-overlap-scan].

Test:
- Self-verifying from doc text. Grep the scan phrasing across the four /done sub-docs after the edit — expect four identical statements including the both-ways result line.
- Behavioural, host-side (after push + reinstall): the next /done close states the waiting-captures verdict in the clean case without prompting. Needs the deferred-test discipline — flag at /done if it can't run.

**Define the staleness-flag fix path: pointer drift fixable at close, fate decisions to /plan** **[staleness-flag-fix-path]**

Observed at the [setup-preexisting-content-handling] /done close (dc4bfee): the staleness sweep flagged two drifted line references in [setup-project-agnosticism-sweep] — the build's new Case B section had pushed setup.md's line numbers down — and Claude offered to fix them in-session with approval, the edit riding into the commit. The flag is codified (done sub-docs' §2.2 sweep says "flag, don't edit without asking"; plugin-behaviour.md's staleness watch defines the review as drop/rewrite/keep). The fix path is not: nothing says whether a flagged item is fixed at /done with approval or waits for /plan, so the move was ad hoc judgment inside the "without asking" parenthetical. The resolving distinction is sharper than mechanical-vs-judgment: the drop/rewrite/keep review is a fate decision about whether the item is still valid, and fate decisions are /plan's, always. But a drifted pointer on an otherwise-valid item — a line or location reference whose target content is unchanged — is not a fate decision; it's maintenance, and may be fixed at the flagging moment with approval, riding the current commit, the same ride-along /done already does for hash backfills and rolled-in user edits. A content change in the referenced material (the quoted wording itself moved, signalling the item's premise may have shifted) is not mechanical and goes to /plan. The location-vs-content line is written in deliberately: leaving it out just relocates the ad-hoc judgment to the next quoted-string flag. Scope note: this fix-at-close path is for skills that commit (/done) and /plan; /next's pre-flight stale scan stays surface-and-recommend-/plan, since /next doesn't edit the queue's other batches. Sibling to [plan-resolves-by-default], which states the /plan-side resolve-now rule — complementary, neither gates the other.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md, Dependency ownership Staleness watch bullet: extend the canonical rule. The drop/rewrite/keep review is /plan's (a fate decision about the item's validity). A drifted pointer on an otherwise-valid item — a line or location reference whose target content is unchanged — is mechanical maintenance and may be corrected at the flagging moment with approval, riding the current commit, the same ride-along as hash backfills and rolled-in user edits; a content change in the referenced material is not mechanical and goes to /plan. Carry the why: the fate decision needs planning, a moved pointer doesn't.
- plugin/si-plugin/docs/done-build.md, done-test.md, done-audit.md, §2.2 staleness sweep ("If so, flag (don't edit without asking)"): align all three to the fix path — flag fate-decision staleness for /plan; offer to fix a drifted pointer here with approval. Point at the plugin-behaviour.md statement rather than restating it. Locate by content, not line numbers (the same line is also tagged by [next-done-tag-sweep]; no ordering between them — locate by content).

Test:
- Self-verifying from doc text. Grep the sweep wording across the three done sub-docs after the edit — expect three aligned statements.
- Behavioural, host-side (after push + reinstall): the next /done staleness flag of a pure pointer drift offers an in-session fix with approval; a fate-decision flag defers to /plan. Needs the deferred-test discipline — flag at /done if it can't run.

**State the single-summary rule in all four /done sub-docs** **[done-single-summary-line]**

From a [close-out-audit] finding (e120f3d). The single-summary rule is stated at five close-outs, but inside the /done sub-docs only done-plan.md carries it at the entry-writing step — done-build.md, done-test.md, and done-audit.md are silent on it. The pull the rule guards against lives exactly there: just after the commit, the natural move is to recap the session while recommending what's next, and a two-sentence recap satisfies the recommend-next [BRIEF] tag while still duplicating the entry. Grep-confirmed at routing: only done-plan.md has the line. The fix copies its exact wording so the rule reads identically everywhere it appears.

Build:
- plugin/si-plugin/docs/done-build.md, done-test.md, done-audit.md, entry-writing steps: add done-plan.md's line verbatim — "This entry is the session's summary — there is no separate chat recap." Locate each spot by content (the show-for-approval instruction in each entry step), not line numbers.

Test:
- Self-verifying. Grep "separate chat recap" across the /done sub-docs after the edit — expect four hits, identical wording.

**Fit the push offer to session shape and remote state** **[push-offer-fit]**

From a [close-out-audit] finding (e120f3d), plus one gap surfaced at routing. done.md's commit core asks "Commit and push, or just commit?" identically for every session shape. The dual ask fits build, test, and audit closes — work shipped or was verified, push is a real choice. It misfits planning closes: the staged paths are local planning state, so the standing offer treats planning work as a ship event. In the self-hosting host the cost is concrete — a push triggers the full push-and-rezip ritual off a commit that changed nothing in the plugin. A non-coder reads offered options as equally sensible defaults, so the ask teaches that pushing planning state is normal when the system reserves push for shipping. The routing-time gap: consumer repos may have no remote at all — nothing in setup or install creates one — so the ask can offer an option that errors when picked. The fix keeps the mechanics canonical in done.md and shapes the ask by context. The override is a default, not a prohibition — for consumers push is often just backup, and that stays available. Setup-shaped sessions inherit the override for free once [setup-closeout-redesign] routes them through done-plan.md.

Build:
- plugin/si-plugin/docs/done.md commit core: gate the push offer on a remote existing (one git remote check). No remote: ask about committing alone — don't offer what would error.
- plugin/si-plugin/docs/done.md commit core: add one line stating sub-docs may override the ask's default while the mechanics stay canonical here.
- plugin/si-plugin/docs/done-plan.md commit step: override the ask — planning sessions offer commit alone by default; push stays available when the user asks or is deliberately backing up. Carry the why: planning state is local bookkeeping, push is reserved for shipping, and in self-hosting projects a push triggers the full push-and-rezip ritual.

Test:
- Self-verifying from doc text. Behavioural, host-side (after push + reinstall): the next /done after a planning session asks commit-only; a /done after a build still offers the dual ask. Needs the deferred-test discipline — flag at /done if it can't run.

**Define next-test.md's completion review tail** **[next-test-review-tail]**

From a [close-out-audit] finding (e120f3d). The three /next-family completions share one shape — "Run /done to record this and commit, or X before closing" — but only next-build.md defines its X, and that definition exists deliberately to close a new-work-smuggling risk: an undefined tail can absorb fresh work past the batch's contract. next-test.md's "review what's already tested" carries no equivalent definition, so the same risk sits open there. The audit half of this finding rides in [audit-findings-bulk-approval], which rewrites next-audit.md's close; this batch covers the test half, mirroring next-build.md's wording so the rule reads the same in both places.

Build:
- plugin/si-plugin/docs/next-test.md Completion, after the "Run /done…" say-line: add the definition — reviewing means re-examining what was already tested, not raising new work; anything new routes through the existing paths (out-of-scope via Scope management, thinking work via Captures). Mirror next-build.md's tightening definition in structure and length.

Test:
- Self-verifying from the doc text. The two defined tails should read as the same rule in build and test clothing.

**Push marker: one hard direction, otherwise a ship-by aim** **[push-marker-hard-direction]**

The push-marker convention reads as a solid barrier, but it's only hard in one direction. Decided-but-unshipped standards already shape sessions before any push — in-repo sessions read the queue and the discussion, not just the installed plugin (observed 2026-06-12: blockquote displays, verbatim-first quoting, a why-pipeline judgment call, all applied pre-push). The genuinely hard case is host-side reads: work that reads installed state — an audit reading injected rules, a live test of hook behaviour — gets wrong results before push + reinstall, and the /next halt exists to protect exactly that. Left undistinguished, the risk is a session treating the line as solid and suspending decided reasoning ("not shipped yet"), which breaks the why-pipeline. Decided rationale never waits on a push.

Build:
- This project's CLAUDE.md (host-only, does not propagate), the push-marker convention in Self-hosting dependency ordering: state the distinction — the marker halts /next because batches past it read host-side state, the one hard direction; it does not suspend decided rules or reasoning in any session, and it is not a wall for planning work. The line marks when we aim to ship by. Decided rules and reasoning apply from the moment they're decided.

**Remove dash-stripping from the scope-lock parser: bare paths become the single truth** **[scope-lock-drop-dash-stripping]**

The scope-lock parser strips trailing annotations from Files: lines when a dash separator is used (" — ", " - ", " – "), but not parenthetical ones. The code is partially tolerant while the decided rule says bare paths, nothing else on the line. The split is the worst spot: a dash-annotated line works silently, so the annotating habit never gets corrected, then a parenthetical one breaks scope mid-build. The denial message shipped by [git-add-safety-hook-gap] teaches that any annotation breaks the match — the dash-stripping makes that false for one annotation style. Removing the stripping makes the rule, the denial message, and the parser agree. The teaching denial is the recovery path for anyone who annotates a line. Side benefit: a genuine path containing " - " no longer gets truncated by the stripper. _build.md is ephemeral — each build writes a fresh one — so nothing needs migrating.

Build:
- plugin/si-plugin/hooks/pre_tool_use.py: remove the dash-stripping loop from the Files: parser — entries are taken whole after the leading "- " marker. No other parser behaviour changes.
- Verify, no edits expected: the scope-lock denial text and next.md's _build.md format section already state the bare-path rule and stay accurate once the stripping is gone.

Test:
- Claude-run: pre_tool_use.py against a fixture _build.md — a dash-annotated Files: line is denied with the teaching message; a bare path still passes; an empty Files: section still locks to method docs.
- Host-side (after push + reinstall): a live denial on an annotated line. Needs the deferred-test discipline — flag at /done if it can't run.

**Audit narration volume at skill openings** **[opening-narration-audit]**
Depends on: [plan-step1-sequencing]

Raised 2026-06-14. Narration has been piling up at the start of skill sessions, and the cause looks structural: a skill's opening is where the most rules fire at once — the read-state step, the unpark and staleness scans, and several behaviour rules that each independently say "narrate" (narrate the ordering work, surface unpark candidates, flag staleness). Each was added for good reason, but nothing bounds the total, so they stack into a wall of opening narration. [output-tag-audit] already checked tag placement across all docs, and its fixes are the queued tag batches; this audit asks a different question it never measured — how much narration accumulates at one opening, and whether the fix is a tag or a rule. It depends on [plan-step1-sequencing] because that batch cleans /plan's opening, the flagship example, so auditing afterward reads the intended state instead of re-finding a queued fix.

Audit:
- Target: the opening sequences of all four skills as written in the procedure docs — setup.md's entry, plan.md Step 1, the next family's pre-flight opening, the done family's openings — plus the plugin-behaviour.md rules that drive opening narration (narrate the ordering work, the unpark watch, the staleness watch, dependency-ownership narration). If the same pile-up appears at any other high-rule-density moment while reading, report it too.
- Criteria: at each opening, separate narration the user genuinely needs (the entry question, a real unpark candidate, an actual ordering decision) from accumulated excess (scan and process narration, state restatement, over-explaining). For each excess moment, name the lever — a missing [SILENT] or [BRIEF] tag on the step, a tag that needs changing, or a behaviour rule that fires narration with nothing bounding the total when several stack on one opening. Flag especially where multiple rules pile onto the same opening — the aggregate problem per-step tagging can't catch. Where a queued fix already addresses an opening ([plan-step1-sequencing], [output-tag-audit]'s findings), note it as covered and don't re-file.

**Backfill the FAQ folder this project never scaffolded** **[faq-backfill]**

This project is missing its `FAQ/` folder — the `faq.md` and `index.md` that /setup scaffolds from templates. The cause: the FAQ scaffolding step was added to /setup after this project was first set up (commit `06c24e4`), and /setup was never re-run here, so the folder was never created. Nothing automatically re-scaffolds this project when the plugin gains new scaffolding, so the gap stayed silent.

This batch backfills the FAQ from the current templates, so the dev project has the FAQ that consumers get and can dogfood FAQ edits. It is placed late on purpose: several queued batches add FAQ entries to the templates, so running it after them captures a more current snapshot instead of one that is stale on arrival.

Two caveats are accepted, not solved here. This is a point-in-time copy, not a synced one — it will drift again as later FAQ-template edits land, and there is no detection because `.si-version` is deliberately left to the separate self-hosting design item. And once `FAQ/index.md` exists, the session-start hook injects it into every session start — small and by design, but the narration audit should treat that injection as in-scope here.

Build:
- Create the `FAQ/` folder in the project root.
- `FAQ/faq.md` — copy the current content of `plugin/si-plugin/templates/faq-template.md`.
- `FAQ/index.md` — copy the current content of `plugin/si-plugin/templates/faq-index-template.md`.

Test:
- Self-verifying: `FAQ/faq.md` and `FAQ/index.md` exist and match the current templates. The next session start will then inject `FAQ/index.md` — observable, minor.

### Parked

## Deferred tests

Planned tests that couldn't run in their own session (host-side, needs-user, external event). /done writes entries here when a test can't run in-session; /next's pre-flight gate re-presents every pending entry; the session that confirms one removes its line and records the confirmation in its LOG entry.

- [narrate-build-md-purpose] — verify the remaining unobserved narration moment: a one-line opener when a resume reads _build.md (scope-lock narration and rationale-carry confirmed live 2026-06-12). Confirmed by: the first /next that resumes an interrupted build.
- [next-pre-scope-lock-abort] — verify a /next that ends before a build is locked (push-marker halt, blocker-gate stop, or the user calling it off at "Ready?") routes any reshape direction to Captures and names /done, not /plan. Confirmed by: the first naturally-occurring pre-scope-lock end after push + reinstall.
- [drop-log-per-release-split] — verify a "why did we decide X" question targeting a pre-split entry in an old log-v*.md file is answered through the index plus the hash-or-title search fallback (pre-split entries have no per-entry file to open). Confirmed by: the first such why-question after push + reinstall, or a deliberate run any time after reinstall.
- [hash-backfill-as-hook] — verify the session-start hook runs the LOG hash backfill live: the first session opening after a /done that left an unfilled placeholder shows the hook's one-line housekeeping report, the placeholder is filled in the working tree, and archived prose mentioning the token survives. Confirmed by: observing that report and the filled hash in the first post-/done session after push + reinstall.
- [queue-format-lint-hook] — verify the lint hook fires live on a real QUEUE.md edit: advisory warnings appear next to the tool result after the edit lands (the four known dangling-dependency flags are expected on current content), and a clean edit elsewhere stays silent. Confirmed by: the first session editing QUEUE.md after push + reinstall.
- [git-add-safety-hook-gap] — verify a live denial on a deliberate git add -A in a scratch context, with the teaching message naming explicit staging and the patterns-as-data note. Confirmed by: the first such denial observed after push + reinstall.
- [narration-vocabulary] — verify user-facing narration stays free of background-only structural terms (loop, Step N, gate, slug names), with the Vocabulary list catching what the abstract rule missed. Confirmed by: narration observed clean against the list in the first /plan or /next session after push + reinstall.
- [setup-preexisting-content-handling] — verify a Case B /setup run peeks at pre-existing content before Q1 (framing clarifier, never a pre-answer) and leaves it untouched during scaffolding while naming it in the closing message. Confirmed by: the first /setup run in a folder with pre-existing content after push + reinstall.

## Captures

Captured outside /plan. Picked up and routed during the next /plan session. Processed captures (slug assigned, dependencies scanned) sit above the `---` divider; unprocessed raw captures collect below. See plan.md Capture and parking discipline.

**Retire REGISTRY.md: drop the write-only inventory doc** **[retire-registry]**

Decided 2026-06-13. Remove REGISTRY.md as a project doc. The architecture goes from four docs to three: SPEC, QUEUE, LOG.

Why: REGISTRY is write-only. Grep-confirmed — it's scaffolded at setup, updated at every /done, presence-checked at session start, and listed among the editable "method docs" for the scope-lock, but nothing ever reads its content to make a decision. No read-before-edit gate, no procedure step that opens it. The only justification was a human-facing map for a non-coder. The user — the non-coder it serves — never opens it, and never opened the richer old MANIFEST either. The replacement is better: a non-coder who wants to know what their app contains asks Claude in-session, which explores the live code — accurate, contextual, zero maintenance. This is the MANIFEST echo: REGISTRY kept the inventory after the mechanisms that made it load-bearing (the read-before-edit gate, serves-lines, rationale suffixes) were already dropped.

One nuance weighed and rejected: REGISTRY could in theory give Claude a fast orientation map in a large project. But nothing reads it today, and live search beats a hand-maintained list that drifts — so it doesn't save the doc.

Removal arc — what changes (the build does a full grep sweep so no reference is missed):
- setup.md: stop scaffolding REGISTRY — the template block, the Case B mention, the SKILL.md description line.
- session_start.py: remove the REGISTRY presence check and its method-doc detection.
- pre_tool_use.py, next.md, next-audit.md: remove REGISTRY from the "method docs" editable set wherever that set is listed.
- done.md: drop REGISTRY from staged paths; done-build.md: remove the "Update REGISTRY" step; done-plan.md: drop it from staged paths.
- next-build.md: remove the "REGISTRY.md is not build scope" line.
- plugin-behaviour.md: remove REGISTRY from the doc-routing line and the route-to-artifacts list. While editing the doc-routing line, also reword the SPEC.md description project-agnostic — "what/who/how/why the project exists," not "the product exists" — which carries the folded-in [plugin-behaviour-doc-routing-agnostic] decision (otherwise lost when [setup-registry-template-and-noun] is dropped).
- SPEC.md: remove REGISTRY from the four-docs description (a spec change — rides a spec-edit batch under [spec-edit-batch-type]).
- CLAUDE-TEMPLATE.md and this project's CLAUDE.md: drop REGISTRY from the architecture and doc descriptions.
- faq-template.md + faq-index-template.md: remove the "What is REGISTRY.md for?" entry.
- This project's REGISTRY.md: delete the file.
- Consumer migration: existing adopted projects (e.g. Taskflowapp) have a REGISTRY.md that becomes orphaned — the adopt/setup re-run path should retire it, not leave it dangling.

Queue interactions: moots [setup-registry-template-and-noun] (it reworked the REGISTRY template — now dropped, with its surviving SPEC-side doc-routing reword folded into this capture's plugin-behaviour.md step). [setup-project-agnosticism-sweep] is unaffected — it deliberately holds no REGISTRY item. Relates to [spec-edit-batch-type] (the SPEC portion rides a spec-edit batch).

**Keep this project's scaffolding in sync — it silently drifts from /setup** **[scaffolding-resync]**

Raised 2026-06-14, from the FAQ-absence finding. This project's own scaffolding drifts from what /setup now produces, and nothing detects or corrects it. Today's concrete gaps: the FAQ folder (being backfilled one-off by [faq-backfill]) and the missing `.si-version`. The real problem is the missing mechanism — nothing re-syncs this project when the plugin gains new scaffolding, and there's no `.si-version` baseline for the session-start hook to even flag the drift.

`.si-version` is not a simple backfill. This project bumps its version on every push, but only a few bumps add new scaffolding a project must absorb. A static `.si-version` would fire "re-run /setup" every session after the next bump — a false alarm most of the time, and new start-noise of exactly the kind we're trying to reduce.

A fix needs to decide three things:
- How this project (and any self-hoster) keeps its scaffolding current — re-run /setup on real scaffolding changes, a backfill check in the pre-push sweep or /done, or another mechanism.
- How `.si-version` is handled so drift is detected without constant false "re-run /setup" nags (auto-update it on push, or change what the mismatch check keys on).
- Whether the version-mismatch signal should distinguish scaffolding-changing releases from internal-only ones — the coarse-signal flaw behind the false alarms.

Relationships (citations, not blockers): overlaps [self-hosting-support-during-setup] and [self-hosting-notes-audit]. [faq-backfill] handles the immediate FAQ snapshot; this item is about keeping it and the rest current.

---

**Trickle four /next-only rules down out of the every-session injection** [audit finding: behaviour-doc-firing-map-audit]

From the firing-map audit (2026-06-13). Four rules live in plugin-behaviour.md — the doc injected into every session — but their triggers only exist during a /next build, so every /plan, /done, and setup session pays for words it can never use:
- "SPEC.md is read-only during builds" (plugin-behaviour.md:103)
- "One build at a time. Never start /next while _build.md exists" (plugin-behaviour.md:104)
- "At build completion, the only valid next-step recommendation is /done" (plugin-behaviour.md:105)
- "If context is long mid-build, suggest completing the current file and running /done" (plugin-behaviour.md:134)

Each keys to _build.md or build execution, which exist only inside /next — none can fire outside /next, and none fire in /plan, /done, or setup. Owning doc: next.md. Roughly 111 words would leave the injection (the build-completion bullet is ~75 of them).

This contradicts the trickle-up direction for these specific rules: that arc moved rules up on "cross-skill belongs in the injection," but single-skill rules don't earn it. Action for /plan: author a trickle-down batch moving these to next.md as canonical, each carrying its rationale per the why-pipeline.

Two interactions to handle when authoring:
- [trickle-up-next-md-duplicates] (queued) plans to DELETE next.md's copies of "SPEC read-only" and "one build at a time," leaving the injection as their sole home — the opposite of this finding. Amend that batch (or carve these two out of it) before it builds.
- [spec-edit-batch-type] (capture) would remove the "SPEC.md read-only during builds" rule entirely (SPEC becomes a normal doc governed by scope-lock). If it promotes, the SPEC-read-only trickle-down is mooted — sequence accordingly.

**Spec-entry pipeline rule is /plan-only — make plan.md canonical, drop the injection copy** [audit finding: behaviour-doc-firing-map-audit]

From the firing-map audit (2026-06-13). The spec-entry pipeline rule at plugin-behaviour.md:100 — "New features need a spec entry before a build entry. Pipeline: idea → question (if unclear) → SPEC.md → QUEUE.md. Threshold: if a user would see or experience the difference, update SPEC.md first" — fires only in /plan. The pipeline (idea→question→SPEC→QUEUE) is /plan's authoring sequence; a feature idea captured elsewhere just gets filed, and nothing runs the pipeline until /plan picks it up. It's already restated in plan.md:17, so the injection and plan.md carry two synced copies. ~33 words sit in the injection.

Single-skill (/plan). Owning doc: plan.md. Action for /plan: make plan.md the single canonical home and drop the behaviour.md copy, rather than maintaining two synced versions.

Two interactions to handle when authoring:
- [spec-entry-trigger-rethink] (queued) rewords BOTH copies to keep them aligned. If plan.md becomes canonical, that batch should target plan.md alone — fold this decision into it rather than letting it re-sync two copies.
- [spec-edit-batch-type] (capture) would rewrite the pipeline to "idea → decide in /plan → spec-edit batch → /next edits SPEC → feature batch," adding a /next stage and pushing the firing map from single-skill to two-skill (plan + next). If it promotes, the home question changes — decide after its disposition is known.

**Middle-band rules (2–3 skills) in plugin-behaviour.md — firing data for the restructure decision** [audit finding: behaviour-doc-firing-map-audit]

From the firing-map audit (2026-06-13). These rules fire in two or three skills but never outside a skill — so they don't earn the every-session injection on the "fires outside skills" test, but they aren't single-skill trickle-down candidates either. Recorded as data for the progressive-disclosure restructure, not moved (the audit proposes no move for this band).

The band:
- Index entries (plugin-behaviour.md:82-93) — 3 skills: /plan readiness gate (plan.md:105), /next pre-generate (next.md:29), /done writes it (all done sub-docs). The retrieve path reads the index but doesn't apply the authoring rule.
- Unpark watch (plugin-behaviour.md:112) — 3 skills; self-names its firing sites (/plan read-state + loop, /next pre-flight, /done close-out).
- Staleness watch (plugin-behaviour.md:113) — 3 skills, "same surfacing moments." [staleness-flag-fix-path] (queued) extends it — same band.
- Empty Batches → /plan (plugin-behaviour.md:106) — 2 skills (/next pre-flight, /done recommend-next).
- User owns scope (plugin-behaviour.md:118) — 2 skills (/plan promote-park-drop, /next whether-to-proceed). [scope-anchor] rewords it.
- Resume reads _build.md (plugin-behaviour.md:135) — 2 skills (/next resume, /done reads it).
- /plan-for-planning, /next-for-building (plugin-behaviour.md:99) — 2–3 skills; boundary rule.
- Borderline /plan-only authoring read cross-skill: Depends/Blocks headers (plugin-behaviour.md:115), stable slugs (plugin-behaviour.md:117) — authored in /plan, referenced when read elsewhere.

Why it matters: this band is what the restructure is for — compact core injected with the fuller doc loaded at skill time, or a shared sub-doc the relevant skills load, or canonical-in-one with a read-on-demand pointer. That decision is parked in [behaviour-doc-size-watch]; this record is the firing data it should be decided on, instead of a guess. No move now — fold into that item when it fires.

**Queued plugin-behaviour.md additions whose firing maps are narrower than every-session** [audit finding: behaviour-doc-firing-map-audit]

From the firing-map audit (2026-06-13). The audit checked every queued batch whose build entries add or reword rules in plugin-behaviour.md (the every-session injection). Most plan correct homes — their rules fire outside skills via capture-making, approval moments, or memory-routing ([red-flags-screen-rule], [approval-display-blockquotes], [approval-ask-after-draft], [human-readable-authoring], [memory-rule-boundaries], and the Dependency-ownership trio). Four plan injection homes for rules whose triggers are narrower:

- [scope-anchor] — the Scope statement (build scope = the active batch's entries' work; the Files: list is its mechanical approximation) fires in /plan (entries name files) and /next (scope-lock, expansion asks) = 2 skills, not outside any skill. Planned for the injection.
- [scope-boundary-rule] — the discovery decision rule (needed→ask/split; not needed→capture; premise broken→halt) is /next execution, planned canonical-in-injection with next-build/next-test pointers. It also rewrites the current "Don't fix things outside current scope" rule (plugin-behaviour.md:101), itself /next-execution — deepening an execution rule's injection footprint.
- [no-planning-in-execution] — mixed: the prohibition ("no capture-processing in execution skills") fires in /next; the permission ("capture-making is open to every session type") is genuinely universal. The prohibition half is narrower than every-session.
- [audit-findings-bulk-approval] — the bulk-approval inversion fires only in /next-audit, but is added to the universal sequencing rule as an exception. Borderline: an exception co-located with its universal parent has merit.

Action for /plan: weigh each home against the firing map before these batches build — not to override their own reasoning, but so the injection-vs-skill-doc choice is made deliberately. [scope-anchor] and [scope-boundary-rule] are the clear candidates to reconsider (plan+next / next-only); [no-planning-in-execution] and [audit-findings-bulk-approval] may justify injection anyway. This is the reason the audit was placed above the rule-adding batches.

**README: separate the four-commands intro line and add a best-practice usage cycle**

Observed by the user, 2026-06-14. Target is README.md at the repo root — the GitHub landing page, not a file inside the plugin package, so it's edited directly and doesn't propagate through reinstall.

Two changes wanted in the "What it does" section:
- Reword the intro so the claim and the list are separate sentences. "…walks you through it with four slash commands:" becomes "…walks you through it. It has four slash commands:".
- Add a best-practice usage section under the command list: /setup once only; then repeat the cycle of /plan → /done → /clear and /next → /done → /clear; with /plan → /done → /clear repeated as many times as needed for long-running planning.

Why it matters: a non-coder reads four one-line command descriptions but can't infer the rhythm. This cycle is how the user will present real-world use demos, and the README should teach the same pattern to anyone who isn't watching them — mirroring what the demos show. It also keeps the repo honest. The four commands look like something you can pick up and use freely, but a fair bit of invisible process sits on top — not a huge amount, but enough that skipping the rhythm gives you a bad time. The load-bearing habit is closing every session with /done before /clear: the design relies on each session being recorded before the context is cleared. Presenting the commands without the cycle oversells how freely they can be used and drifts from how the demos present it.

To settle when this is promoted: the paired-cycle layout can read as strict one-/plan-then-one-/next alternation. In practice /next repeats across many batches between planning sessions, so the final wording should make /next-repeats as visible as /plan-repeats.

**Self-install branch in the guided install: let Claude Code install SI via terminal**

Raised by the user, 2026-06-14, building on the existing guided install (INSTALL.md). For repo visitors who already have Claude Code, add a branch where Claude Code installs the SI plugin itself via the terminal, instead of the human doing the GUI zip-upload (Customise → Create a plugin).

Mechanism is confirmed (research: resources/research/claude-code-plugin-install-mechanisms.md). The desktop app's Code tab is Claude Code with an integrated terminal, and there is a non-interactive `claude plugin install <name>@<marketplace>` command the agent can run. So Claude Code can do the install in both the CLI and the desktop app.

Two things shape how this branch must be written:
- INSTALL.md is consumed by a claude.ai chat, which has no terminal — it can only instruct the human, not run the install. So this branch is a handoff: the already-has-Claude-Code user is routed to run the install through Claude Code itself, not through the claude.ai guide. This overlaps the experienced-user bypass queued in [install-separate-ai-instructions] and the app-identification check in [install-app-identification-check] — likely the same branch point.
- Prerequisite: the clean install command installs from a marketplace, and SI's repo has no marketplace manifest today. The repo must publish `.claude-plugin/marketplace.json` pointing at si-plugin before `claude plugin marketplace add FlintCraftTech/sovereign-implementer` + `claude plugin install` will work. The raw-local-zip alternative is the unreliable path (open upstream feature request). So this idea carries a prerequisite build: publish the marketplace manifest.

Ripple for /plan to weigh at promote time: publishing a marketplace manifest makes "add our marketplace and install" the standard, robust install flow, which could simplify or partly moot some queued INSTALL.md batches (all of which assume the GUI zip-upload). Decide the interaction with those batches when this is promoted.

**SI teaches the user the working rhythm in-product, not just in the README**

Raised by the user, 2026-06-14, sibling to the README usage-cycle capture above. That capture puts the /setup-once-then-cycle rhythm on the repo front page for visitors. This one is the in-product counterpart: SI itself should show the user the rhythm during use, so someone who installed SI without reading the README still learns it.

Same content as the README capture (the cycle: /setup once; then repeat /plan → /done → /clear and /next → /done → /clear, planning repeated as needed). Same why: the rhythm is load-bearing and not inferable from the four one-line command descriptions — every session closes with /done before /clear so it's recorded before the context is cleared. Different surface: in-product teaching, not a repo-front-page reference.

Candidate homes (to settle at promote time):
- The /setup close-out — the natural onboarding moment, right after scaffolding, when the user is about to start the cycle. This interacts directly with [setup-closeout-redesign], which is already rewriting that close to recommend /done; coordinate with or sequence after it.
- A FAQ entry (faq-template.md + index line) as the durable in-product reference the user can return to.
- Not session-start: the rhythm is onboarding teaching, and repeating it every session would be noise.

Authoring note: the setup close-out and FAQ are user-facing (external non-coder), so the rhythm must read in plain English with no internal terms, and the cycle wording should stay consistent across the README, the setup close-out, and the FAQ.

**Hook-count descriptions lag the QUEUE.md lint hook**

Found during the v1.12.0 pre-push consistency sweep, 2026-06-14. This project's CLAUDE.md Architecture section enumerates "2 hooks (session_start, pre_tool_use)," but post_tool_use.py — the QUEUE.md structure lint, shipped after v1.11.0 — makes three hook files. SPEC.md's "Two hooks enforce discipline mechanically" is arguably still accurate, because the lint hook advises rather than enforces. So this is a framing decision, not a clear error: update CLAUDE.md's enumeration to three, and decide whether SPEC should mention the advisory lint hook at all. Host-only / this-project docs; nothing consumer-facing was stale (CLAUDE-TEMPLATE.md and faq-template.md don't enumerate hooks).

### Parked

- **[narration-vs-menu-drift]** Observed during 1b7d359 /plan: Claude defaulted to menu-style options ("file as capture, drop it, or commit to the rule now?") when narrating a recommendation would have been more appropriate. Dependency ownership's narration rule ("narrate the ordering work" — exercise judgment, recommend) is supposed to catch this. The mechanism failed under exploratory back-and-forth tone — the pull toward "lay out the options" was stronger than the pull toward "state the recommendation, let user push back." Worth watching whether this generalizes: when the conversation gets exploratory, does Claude soften from recommendation-narration into menu-listing? If so, the narration rule needs tightening — possibly explicit text that menu-style enumeration of equally-weighted options is *not* narration when Claude actually has a preference, and the recommendation must come first with the menu as fallback.
  Blocked by: a second observed instance of menu-style enumeration where a recommendation was due — behavioural trigger, no slug; fires at the /plan that processes such a capture.

- **[parked]** Decide whether to add an inline marker for internal-only terms in procedure prose. The marker would let procedure docs flag internal terms inline so the translate-or-omit rule fires mechanically rather than relying on Claude matching against the vocabulary list each time.
  Blocked by: [narration-vocabulary] + observed leakage after it ships

- **[user-execution-batch-shape]** When the user is the executor of a batch (gather these receipts, identify the lender, call the ATO) rather than Claude, the existing build/test/audit shapes don't quite fit. Build batches assume Claude executes; test batches are about verification; audit batches are read-and-route. A user-execution batch sits closest to a test batch in mechanics (user runs steps, Claude facilitates), but it's not verification — it's the primary work. Observed during /setup on a tax-prep folder: queueing batches that were mostly user-action items felt weird, even though step-by-step communication rules in plugin-behaviour.md would handle the running well. Three possible landings: (a) new `User:` subheading alongside Build/Test/Audit, (b) covered by existing types + freeform once shipped, (c) framing-only — "build" means "user does it" in non-coder projects, no new structure. Decision premature without running several user-execution batches first.
  Blocked by: experience from 2–3 user-execution batches run in the tax project — external behavioural trigger, no slug; fires when that experience reaches a /plan session here.

- Add scenarios to reader-test-workflow.js — evaluate which scenarios are still undertested and worth adding. Known blind spots regardless of refresh outcome: /setup interview (untested), push-and-rezip sweep (untested — lives in this project's CLAUDE.md, not plugin docs, so coverage question is whether it should even be in scope for plugin reader-tests), mid-build resume from a real _build.md (current next.md sim covers fresh /next, not resume), /done plan-mode close-out (current sim only covers build close-out), empty-queue handling, audit-batch flow (planning-as-work). Promote as one or more build batches once scenarios are picked. The refresh itself shipped at 2356cb7 ([reader-test-refresh]), so only the run remains.
  Blocked by: refreshed workflow run once — behavioural trigger; the first refreshed run may surface blind spots not on this list, or may show that scenario count matters less than scenario specificity.

- Cruise control skill — a skill that runs build→commit→build→commit through a batch (or multiple batches) unattended, stopping only when it hits something requiring user input. Key design concerns: (1) wording that doesn't pressure Claude to push through uncertainty, (2) dependency management when Claude decides when to wrap a batch, (3) /done judgment steps can't get skipped for speed; (4) the red-flags gate — an open red flag in the active scope blocks the unattended run, only resolved or accepted flags let it proceed, and a user who leaves a flag open stays on hand to approve each step (the gate is a hook reading the three flag states defined by [red-flags-screen-rule]).
  Blocked by: the autopilot prerequisite arc shipping — the no-planning-in-execution rule ([no-planning-in-execution]), queue-visible plan markers ([queue-plan-markers]), and audit bulk approval ([audit-findings-bulk-approval]); fires when those have shipped and an unattended next→done→next run is plausible. Full no-approval auto-file of audit findings is in this item's own design scope — interactive audits keep bulk approval. Named as the end-goal in the thinking-work capture, 2026-06-10.

- **[self-hosting-support-during-setup]** Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping, **and the dependency-management discipline** (host-vs-target distinction as it governs batch ordering, the host-side-after-push-marker rule, the `--- Push required before continuing ---` queue convention, and the `(host-side)` annotation on `Depends on:`). All of this carries into the new project's CLAUDE.md. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
  Blocked by: a second self-hosting consumer appearing — a user reports building a plugin (or any project that ships itself) with the plugin, or Alex starts one; external behavioural trigger, no slug. The scoping decision (interview question vs skill vs template) waits for that real case to design against.

- **[done-spec-sync-check]** /done spec check at build close — when the session being closed was a /next build (not test or audit), /done reads SPEC.md against the just-landed changes and applies the spec-entry trigger test (post-[spec-entry-trigger-rethink] form: would these changes make SPEC.md's description wrong or incomplete?). If yes, /done files a mandatory capture naming the gap — it never edits SPEC.md directly; product-truth edits stay in /plan. Decided 2026-06-10: detect-and-file wins over sync-in-/done, keeping SPEC authorship in /plan while making the backstop mechanical. Evidence the backstop is needed: the prospective /plan gate leaked at [tag-definitions-compliance-rewrite] — no spec entry preceded the build, and the gap was caught only because the /done session noticed by judgment and filed a capture. This makes that lucky catch structural: prospective gate at /plan, mechanical detect-and-file at /done.
  Blocked by: [spec-entry-trigger-rethink] — the /done check applies the rewritten trigger wording, so it can't be authored until that wording has shipped.

- Threshold-based context management — if hooks ever gain token usage fields (e.g. `context_usage_pct`), the plugin could recommend `/compact` or `/clear` based on actual utilization instead of rule-based triggers. Research filed at resources/research/context-window-hook-access.md.
  Blocked by: Anthropic adding token data to hook event input — external trigger, no slug.

- **[lint-citation-refire]** Observed at [queue-format-lint-hook] build testing, 2026-06-12: the prose-citation check re-fires on every QUEUE.md edit for references it has already flagged. The check is stateless — it reads the whole file, not the edit — so a reference the user has judged "citation, fine" gets flagged again on every later edit, indefinitely. The build already cut the worst noise by flagging only references to slugs still defined in the file: a dry run showed references to shipped work were the bulk (~2.5KB of advisory text per edit), and a reference to shipped work can only be a citation. The residue is real: the first live run flagged ~21 batches, all naming pending items, and any judged-as-citation among them will keep re-firing. Candidate fixes if live use shows this as noise: an inline convention marking a reference as a deliberate citation, which the lint would skip (new format design, /plan's call); or accepting the re-fire as cheap advisory background. The hook is not yet in the installed host — it was built after the v1.11.0 push — so no live session has run with it yet.
  Blocked by: live experience with the lint hook — behavioural trigger; fires once a few /plan sessions have edited QUEUE.md with the hook installed and the re-fire can be judged noisy or tolerable.

- **[behaviour-doc-size-watch]** Filed at the 2026-06-13 /plan, from a doc-size review. plugin-behaviour.md is the largest doc by content (~3,074 words / 135 lines at counting time) and the most expensive position in the system: it is injected at every session start, and skill sessions pay it twice until [behaviour-doc-double-load] ships. Many queued batches add rules to it — the approval rules, authoring standards, scope anchor, memory boundaries, no-planning-in-execution — so it will grow before it settles. Decided at the review: no blanket terseness pass. The rationale-everywhere style is the compliance bet; stripping why-clauses to save tokens buys back the failure mode they were installed to fix. Duplication-targeted trims are already queued ([tag-restatement-trim], [trickle-up-next-md-duplicates], [trickle-up-ask-when-unsure], [behaviour-doc-double-load]). The remaining lever is the progressive-disclosure restructure — compact core injected, full doc loaded at skill time — already noted as a revisit in [behaviour-doc-double-load]'s rationale. This capture is the re-measure trigger: when it fires, re-count plugin-behaviour.md, compare against ~3,074 words, and weigh the restructure on real numbers instead of trimming mid-flux.
  Blocked by: the compliance arc's plugin-behaviour.md additions landing — behavioural trigger, no single slug; fires at the /plan after the queued rule-adding batches have shipped and the doc's contents have settled.

- **[full-tag-placement-recheck]** A fresh full placement re-check of response-shape tags across all procedure docs — setup.md, plan.md, the next and done families, plugin-behaviour.md — to grade the corrected state after [output-tag-audit]'s fixes ship, and to catch any tag drift since that audit (commit 0405315). Distinct from [opening-narration-audit], which measures narration volume at openings; this one re-checks per-step tag placement everywhere, the same lens [output-tag-audit] used, re-run on the post-fix docs. Deferred deliberately: running it before [output-tag-audit]'s findings build would mostly re-discover gaps already sitting in the queue.
  Blocked by: the queued tag-fix batches from the last full tag audit shipping — chiefly [next-done-tag-sweep], [plan-step1-sequencing], and [setup-self-contained-no-tags]; fires once those findings have landed, so the re-check grades corrected docs, not the pre-fix state.
