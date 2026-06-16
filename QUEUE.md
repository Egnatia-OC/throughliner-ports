# QUEUE

## Red flags

Security, privacy, and data-exposure risks Claude has surfaced — kept at the top so they're the first thing seen each session. Each carries a state: open, resolved, or accepted. Empty until a risk comes up.

## Batches

Worked top to bottom. Each batch of changes or tests is one /next session of either type:

- build session where changes are applied, then claude runs all tests it is able to do itself
- test session where the user runs any testing only they can do

**Audit the Taskflow first-spec-edit transcript** **[audit-taskflow-first-spec-edit]**

The first real-world spec-edit in Taskflowapp, flowing from the /setup session that [audit-taskflow-setup-transcript] covers — the first live exercise of the spec-edit mechanism. Captured at `resources/captures/2026-06-16-taskflow-first-spec-edit-session.jsonl` (146 records). Audit how spec-editing actually behaved and route findings to Captures. Sibling to the /setup audit — process their findings together in /plan. Host may be behind target, so check each finding against current target before filing.

Audit:
- Target: `resources/captures/2026-06-16-taskflow-first-spec-edit-session.jsonl`.
- Criteria (a lens, not a closed list — file anything else noteworthy to Captures too): (1) spec-edit mechanism in practice — did /next route the Spec-edit batch, did the scope-lock allow SPEC.md because the batch listed it, did SPEC edit without being blocked (first live test of [spec-edit-batch-type]); (2) host-vs-target reality — how SPEC actually got edited under whatever host ran this, and whether it matches current target intent (if the host predates the mechanism, that's the finding); (3) procedure adherence — batch picked/executed, /done closed it like a build; (4) communication quality; (5) friction & confusion; (6) output correctness — SPEC got the intended change, nothing unintended touched; (7) gaps the docs should have prevented, + red-flag screening.
- Before filing each finding, check against current target; if already fixed, note it and don't re-file.
- Output: findings to Captures only — no direct doc edits.

--- Plan session here: process the two Taskflow audit findings before building the /setup- and SPEC-related batches; findings may reshape them ---

**Retire REGISTRY.md — remove the write-only inventory doc** **[retire-registry]**
Blocks: the consolidated spec-edit batch (carries the SPEC.md four-docs sentence; slug assigned when authored at items 12–13)

Decided 2026-06-13. REGISTRY is write-only — grep-confirmed scaffolded at setup, updated at every /done, presence-checked at session start, and listed in the scope-lock's editable "method docs," but nothing ever reads its content to make a decision. Its only justification was a human-facing map, and the non-coder it serves never opens it (nor the richer old MANIFEST). The better replacement: a user who wants to know what their app contains asks Claude in-session, which explores the live code — accurate, contextual, zero maintenance. Architecture goes from four docs to three: SPEC, QUEUE, LOG. One nuance rejected: REGISTRY could be a fast orientation map in a large project, but nothing reads it today and live search beats a hand-maintained list that drifts. The SPEC.md sentence is deliberately excluded here — it rides the consolidated spec-edit batch.

Build:
- setup.md: stop scaffolding REGISTRY (template block, Case B mention, SKILL.md description line); and make the migration / adopt re-run path retire an existing REGISTRY.md in an already-adopted project rather than leaving it orphaned.
- session_start.py: remove the REGISTRY presence check and its method-doc detection.
- pre_tool_use.py, next.md, next-audit.md: remove REGISTRY from the "method docs" editable set wherever listed.
- done.md: drop REGISTRY from staged paths; done-build.md: remove the "Update REGISTRY" step; done-plan.md: drop it from staged paths.
- next-build.md: remove the "REGISTRY.md is not build scope" line.
- plugin-behaviour.md: remove REGISTRY from the doc-routing line and the route-to-artifacts list; while there, reword the SPEC.md description project-agnostic ("what/who/how/why the project exists," not "the product exists") — folding in the [plugin-behaviour-doc-routing-agnostic] decision.
- CLAUDE-TEMPLATE.md and this project's CLAUDE.md: drop REGISTRY from the architecture and doc descriptions.
- faq-template.md + faq-index-template.md: remove the "What is REGISTRY.md for?" entry.
- Delete this project's REGISTRY.md.
- Full grep sweep across the repo to catch any remaining REGISTRY reference.

Test:
- Claude-runnable (at build): grep the whole repo for "REGISTRY" and confirm no dangling references remain (LOG history excepted).
- Host-side (deferred): the first /setup after push + reinstall scaffolds three docs (SPEC/QUEUE/LOG), not four, and session start no longer flags a missing REGISTRY.

**Spec-edit: sync SPEC.md after REGISTRY retirement and the read-only-rule removal** **[spec-sync-registry-and-lock]**
Depends on: [retire-registry]

Two SPEC.md sentences went stale and both are carved-out SPEC changes from earlier decisions. [retire-registry] removes REGISTRY as a doc (architecture → three docs), and [spec-edit-batch-type] removed the "SPEC read-only during builds" rule — but neither could touch SPEC.md in its own build (SPEC is out of a feature build's scope; the scope-lock only allows a batch that lists SPEC.md). This spec-edit batch makes both edits. Depends on [retire-registry] for ordering — sync SPEC after the removal lands so the two don't briefly contradict.

Spec-edit (Files: SPEC.md):
- "How it works": change "Four project docs structure each project:" → "Three project docs structure each project:", and remove the `REGISTRY.md — components list` bullet. (Leaves SPEC, QUEUE, LOG.)
- The hooks list: reword `pre_tool_use` from "SPEC.md read-only during builds, scope-lock to file list, git safety" to drop the read-only clause — state it enforces the scope-lock (which governs SPEC.md like any other file) and git safety.

(No test — self-evident from reading SPEC.md after the edit.)

**Update the consumer-facing SPEC model in the templates** **[consumer-spec-model-sync]**

Spotted building [queue-plan-markers] (2026-06-16). [spec-edit-batch-type] made SPEC a normal doc changed only through a spec-edit batch and removed "SPEC read-only during builds," but only updated this project's host-only CLAUDE.md. Two consumer-facing surfaces still teach the old model. Reword both to match, in plain English for a non-coder.

Build:
- CLAUDE-TEMPLATE.md "Rules for Claude": replace "SPEC.md is read-only during builds. Edit it only during /plan" with the new model — SPEC is a normal doc, changed only through a planned spec-edit batch that /next runs; a feature build can't touch SPEC because the scope-lock denies any file the batch doesn't list.
- faq-template.md: reword the "Can I edit SPEC.md while doing a build?" answer (currently "No. SPEC.md is read-only during builds…") to the new model. If the question wording changes, update the matching faq-index-template.md line; if only the answer changes, the index stays.

(No test — self-evident from reading the templates after the edit.)

**README: split the four-commands intro and add the usage-cycle section** **[readme-usage-cycle]**

Observed by the user 2026-06-14. README.md is the repo-root landing page — edited directly, doesn't propagate through reinstall. A non-coder reads four one-line command descriptions but can't infer the rhythm, and the four commands look more pick-up-and-use than they are; the load-bearing habit is closing every session with /done before /clear so it's recorded before context resets. This batch establishes the canonical cycle wording that the in-product teaching and FAQ captures will reuse, so the rhythm reads identically everywhere.

Build:
- README.md "What it does": split the intro so claim and list are separate sentences — "…walks you through it. It has four slash commands:".
- README.md: add a "How to use it" section under the command list, with this canonical cycle wording (final phrasing tunable at build time, but it must keep both repeats visible — planning repeats for long stretches, building repeats across many batches — so it never reads as strict one-/plan-then-one-/next alternation):
  > Run **/setup** once, when you first set up a project. After that you work in sessions, and every session ends the same way: **/done** to record what happened, then **/clear** to start fresh.
  > - **/plan** — think and organise: manage the queue, add ideas, resolve questions. Run it as often as planning needs; a long planning stretch is just /plan → /done → /clear, repeated.
  > - **/next** — build: it picks the top item and does it. You'll run /next many times, once per item, working down the queue.
  >
  > The habit that matters: always /done before /clear, so each session is saved before the context resets.

**Teach the working rhythm in-product — /setup close-out + FAQ** **[in-product-rhythm-teaching]**
Depends on: [readme-usage-cycle]

Raised by the user 2026-06-14, the in-product counterpart to [readme-usage-cycle]. The working rhythm is load-bearing but not inferable from the four command descriptions — and someone who installed SI without reading the README never sees it. This teaches it inside the product at the natural onboarding moment, and gives a durable reference to return to. Reuses the canonical cycle wording from [readme-usage-cycle] so the rhythm reads identically across the README, the setup close-out, and the FAQ.

Build:
- setup.md: at the close-out (already reshaped by [setup-closeout-redesign] to recommend /done), add a brief plain-English teaching of the rhythm — /setup once; then /plan and /next sessions, each closed by /done then /clear; planning repeats as needed, building repeats across batches. Reuse the canonical wording.
- faq-template.md + faq-index-template.md: add TWO adjacent, consistent FAQ entries (each with its index line): (1) how the four commands work together day-to-day (the working cycle); (2) what /setup does — it adopts the folder, scaffolds the method docs, and interviews five questions to seed SPEC.md; it runs once per project; re-running it later only backfills missing scaffold files and does NOT overwrite content already written (this backfill-not-overwrite line must match item 17's drift-signal FAQ).
- Not session-start — repeating the rhythm every session would be noise.

Test:
- Host-side (deferred): the first /setup close-out after push + reinstall shows the rhythm teaching in plain English. The FAQ entry's presence is verifiable at build by reading the file.

**Publish the marketplace manifest so `claude plugin install` works** **[publish-marketplace-manifest]**
Blocks: [install-self-install-branch]

Raised by the user 2026-06-14. The clean, robust install path is `claude plugin marketplace add FlintCraftTech/sovereign-implementer` then `claude plugin install` — but that needs a `.claude-plugin/marketplace.json` at the repo root pointing at the plugin, and SI has none today, so the command can't work. Publishing it enables marketplace install for everyone and is the prerequisite for the self-install branch. Mechanism confirmed in resources/research/claude-code-plugin-install-mechanisms.md.

Build:
- Create `.claude-plugin/marketplace.json` at the repo root, registering the si-plugin plugin (name, source path `plugin/si-plugin`, description). Confirm the current marketplace.json schema against Claude Code's plugin docs or the research file before writing — the format is external and may have shifted.

Test:
- Deferred (needs remote): after the manifest is pushed, `claude plugin marketplace add FlintCraftTech/sovereign-implementer` then `claude plugin install` succeed from a terminal. (Claude-runnable / user-run in a terminal session after push.)

**INSTALL.md: add a terminal self-install branch for users who already have Claude Code** **[install-self-install-branch]**
Depends on: [publish-marketplace-manifest]

Raised by the user 2026-06-14. For repo visitors who already have Claude Code, the GUI zip-upload (Branch B) is the slow path — Claude Code can install the plugin itself via the non-interactive `claude plugin install` command. INSTALL.md is read by a claude.ai chat with no terminal, so this branch is a handoff: the experienced user is routed to run the install inside Claude Code, not through the claude.ai guide. Additive — it doesn't replace the GUI-upload flow, which still serves users without Claude Code. Mechanism confirmed in resources/research/claude-code-plugin-install-mechanisms.md.

Build:
- INSTALL.md: add a terminal install option (alternative to Branch B's GUI zip-upload) for users who already have Claude Code. It hands off — the guide tells the user to run, inside Claude Code, `claude plugin marketplace add FlintCraftTech/sovereign-implementer` then `claude plugin install <plugin>@<marketplace>` (confirm the exact command and marketplace name against [publish-marketplace-manifest]'s manifest and the research file). Either they type these in Claude Code's integrated terminal or ask the Claude Code agent to run them.
- Update the "Already have Claude Code and a paid plan?" note and the Branch B intro to offer this terminal option as the faster path for experienced users, keeping the GUI zip-upload as the no-terminal fallback.
- This branch may name terminal commands (its audience is terminal-comfortable), but it still hands off — it never pretends the claude.ai chat can run the install itself.

Test:
- Deferred (needs remote + the manifest pushed): the terminal commands install SI in a real Claude Code session. (user-run, after push.)

**Fix the deferred-test seams: reframe the section, fix the roll, add the prompt** **[deferred-test-seams-fix]**

From items 6 + 7 (2026-06-16). Decision: keep both the deferred-tests section and test batches — they aren't redundant. Deferred tests are a staging pen for verification that can't run yet (host-side until reinstall, or waiting on an external event); test batches are the execution home for user-run verification that can run now; the roll mechanism is the bridge. The user's confusion is real but driven by self-hosting inflation (almost everything here is host-side, so the section looks like a parallel test queue; a consumer's would be near-empty). The fix is to clarify the framing and close two seams: the roll scan keys on a runnability tag the lines don't carry, and nothing actively offers the roll, so runnable tests can quietly accumulate.

Build:
- done.md: when writing a deferred-test line, record two axes — the deferral reason (host-side / needs-user / external) and the runnability the test will have once unblocked (Claude-runnable / user-run) — so a later session knows what kind of check each line becomes.
- plan.md: turn the silent roll scan into an active surface-and-ask. Each /plan reads the Deferred tests section, asks the user which deferrals have cleared (host-side: has a push + reinstall happened since? external: did the event occur?), and for the cleared lines, offers to roll the user-run ones into a test batch while noting the passive/Claude-runnable ones will be confirmed by observation. Don't silently skip lines tagged host-side.
- Reframe the Deferred tests section's purpose text — in setup.md's scaffolded QUEUE template and this project's QUEUE.md — to read as "verification waiting on an event," not a parallel test queue, and document the two-axis tagging. Grep for the canonical lifecycle statement (done.md / plan.md) and update it to match.

Test:
- Host-side (deferred): the first /plan after a push + reinstall actively surfaces the now-runnable host-side deferred tests and offers to roll the user-run ones into a test batch, rather than silently producing nothing.

**Shipped-slug cross-check at close** **[close-shipped-slug-crosscheck]**
Blocks: [formalize-goal-session]

From the /goal fork (item 9, 2026-06-16). A multi-batch close removes many batches in a manual loop with no mechanical check that each shipped slug actually left the queue — the prior goal session recorded shipping 14 batches but left [user-edits-rollup-on-commit] in QUEUE.md (genuinely built, only the removal missed), so it re-presented next session as unbuilt and wasted the first move rediscovering it was done. This adds the safety net, and ships it into done.md so cruise control inherits it.

Build:
- done.md: add a close step — after the LOG entry is written (it names the shipped batch slugs) and before the commit, cross-check each named slug against QUEUE.md's Batches section and confirm it's been removed. If any remain, surface them and remove (or halt and ask) before committing. Trivial for a one-batch close; the net is for multi-batch / goal / cruise-control closes.

Test:
- Host-side (deferred): the first multi-batch close after push + reinstall cross-checks the shipped slugs against QUEUE.md and catches any not removed. (One-batch closes pass self-evidently.)

**Formalize the goal-session shape** **[formalize-goal-session]**
Depends on: [close-shipped-slug-crosscheck]

From the /goal fork (item 9, 2026-06-16). `/goal` works in practice but the method has no defined goal-session shape — it assumes one batch per session, so the run improvised an aggregate `_build.md`, a multi-thread LOG entry, and one commit. This formalizes the shape in this project's CLAUDE.md (it stays the dev workflow; cruise control is the consumer-facing version), so it's defined rather than re-improvised each time. Step 1 of the cruise-control arc.

Build:
- CLAUDE.md "Goal sessions (plugin off)": rewrite from interim to defined. Specify: (1) a goal session runs several build batches back-to-back in one chat, plugin off, Claude autonomous; (2) it uses a single aggregate `_build.md` listing the batches it will work through, purely as a working-state / resume record — with the plugin off the scope-lock is inactive, so `_build.md` here is for state, not enforcement; (3) the close is one multi-thread LOG entry (one thread per batch) with its index line, and a single commit; (4) the manual /done uses the shipped-slug cross-check from [close-shipped-slug-crosscheck]; (5) the deferred-test and staleness sweeps run once across all the batches at close, not per-batch. Keep the existing handoff-claim provenance rule; note the claim-marking format decision belongs to the cruise-control build.

Test:
- Deferred (next goal session, observed): the first goal session run after this lands follows the defined shape — aggregate `_build.md`, multi-thread LOG entry, cross-checked close.

**Note the new-batch-type touch-points in CLAUDE.md** **[new-batch-type-touchpoints]**

From item 14 (2026-06-16). When a batch introduces a new batch type it must wire four places or ship half-working — [spec-edit-batch-type] omitted next.md's router and was half-wired until a goal session caught it. Encode the touch-points as a working-conventions reminder. Host-only: consumers never add batch types, so this goes in this project's CLAUDE.md, not shipped plan.md.

Build:
- CLAUDE.md "Working conventions": add a short reminder that adding a new batch type touches four places — next.md (execution routing), done.md (close routing), post_tool_use.py's `ALLOWED_SUBHEADINGS` (the lint), and plan.md's Step 3 batch structure — and that it's a host-only concern (consumers don't author batch types).

(No test — self-evident from reading CLAUDE.md after the edit.)

**FAQ coverage backfill: commit-and-push ask + drift signal** **[faq-coverage-backfill]**

From [faq-coverage-audit] (items 16 + 17, 2026-06-16). Two consumer-facing moments have no FAQ answer. Both source batches have landed, so the wording can match them now.

Build:
- faq-template.md + faq-index-template.md: add a FAQ entry on the commit-and-push ask — committing saves a snapshot locally; pushing also sends it to a remote backup (e.g. GitHub) if the project has one; with no remote, just commit. Match what [push-offer-fit] settled (commit-only default for planning closes; the dual ask after a build; never offered a push when there's no remote).
- faq-template.md + faq-index-template.md: add a FAQ entry on the "project out of date / run /setup" drift signal — what it means (the plugin gained scaffolding this project doesn't have yet) and what running /setup will and won't do (backfills missing files; does NOT reconcile or overwrite existing content). Match [make-drift-visible]'s catch-up message so the two agree; this is where item 8's overpromise warning lands — don't sell /setup as a cure-all.

(No test — entries verifiable at build by reading the templates.)

**Bound aggregate opening narration** **[bound-opening-narration-aggregate]**

From [opening-narration-audit] (item 18, 2026-06-16). Per-step tags bound each surfacing, but nothing bounds the total when several scans, watches, or ordering-narration rules fire at one skill opening — the /next pre-flight gate (five scans) and the dependency-ownership narration rules both pile up. The fix is a rule that bounds the aggregate, which per-step tagging can't reach.

Build:
- plugin-behaviour.md: add an aggregate-narration rule — when multiple scans / watches / ordering-narration rules fire at a single skill opening (/plan read-state, /next pre-flight, /done close-out), consolidate them into ONE combined narration ("here's what came up: …") rather than bullet-by-bullet or rule-by-rule. State that it governs the dependency-ownership narration rules ("narrate the ordering work," the Unpark watch, the Staleness watch), which each independently instruct narration at the same moments. Carry the why: per-step tags bound each surfacing but can't see the stack.
- next.md: at the pre-flight blocker gate, apply the rule — consolidate whatever the scans turn up into one combined surfacing instead of emitting each brief one back to back.

Test:
- Host-side (deferred): the first /next pre-flight (or /plan read-state) that trips multiple scans emits one consolidated narration, not several back-to-back.

**Add a screenshot of the plugin upload screen to INSTALL.md** **[install-upload-path-clarity]**

The prose half of this batch landed in a goal session (2026-06-15): INSTALL.md now states the confirmed upload path (Customise top left → + icon on the left → "Create a plugin" → browse and select the .zip), drops the hedge "usually in the top menu or settings area," and adds a heads-up that the "Create a plugin" label is the install path despite sounding like an authoring tool. Only the screenshot remains, and a goal session can't produce it — it needs a real capture of the desktop app's Plugins screen.

Build:
- INSTALL.md: add a screenshot of the Plugins screen showing the + icon and the "Create a plugin" option, so users can visually confirm they're in the right place. (User-only — needs a real desktop-app screen capture; a placeholder pointer sits in INSTALL.md's smoke-test step until the image lands.)

### Parked

## Deferred tests

Planned tests that couldn't run in their own session (host-side, needs-user, external event), one line each: source batch slug, what to verify, and what confirms it with a runnability tail (Claude-runnable, user-run, or external). The section holds only verification for shipped work — failures and new test needs route to Captures. Lifecycle: /done writes entries here; /plan reads the section each session and rolls the Claude-runnable and user-run lines into a test batch (external-event lines wait for their event); /done's close-out backstops by removing any line whose confirming event this session's own activity produced. The session that confirms a test removes its line and records the confirmation in its LOG entry.

- [narrate-build-md-purpose] — verify the remaining unobserved narration moment: a one-line opener when a resume reads _build.md (scope-lock narration and rationale-carry confirmed live 2026-06-12). Confirmed by: the first /next that resumes an interrupted build.
- [next-pre-scope-lock-abort] — verify a /next that ends before a build is locked (push-marker halt, blocker-gate stop, or the user calling it off at "Ready?") routes any reshape direction to Captures and names /done, not /plan. Confirmed by: the first naturally-occurring pre-scope-lock end after push + reinstall.
- [drop-log-per-release-split] — verify a "why did we decide X" question targeting a pre-split entry in an old log-v*.md file is answered through the index plus the hash-or-title search fallback (pre-split entries have no per-entry file to open). Confirmed by: the first such why-question after push + reinstall, or a deliberate run any time after reinstall.
- [hash-backfill-as-hook] — verify the session-start hook runs the LOG hash backfill live: the first session opening after a /done that left an unfilled placeholder shows the hook's one-line housekeeping report, the placeholder is filled in the working tree, and archived prose mentioning the token survives. Confirmed by: observing that report and the filled hash in the first post-/done session after push + reinstall.
- [git-add-safety-hook-gap] — verify a live denial on a deliberate git add -A in a scratch context, with the teaching message naming explicit staging and the patterns-as-data note. Confirmed by: the first such denial observed after push + reinstall.
- [narration-vocabulary] — verify user-facing narration stays free of background-only structural terms (loop, Step N, gate, slug names), with the Vocabulary list catching what the abstract rule missed. Confirmed by: narration observed clean against the list in the first /plan or /next session after push + reinstall.
- [setup-preexisting-content-handling] — verify a Case B /setup run peeks at pre-existing content before Q1 (framing clarifier, never a pre-answer) and leaves it untouched during scaffolding while naming it in the closing message. Confirmed by: the first /setup run in a folder with pre-existing content after push + reinstall.
- [red-flags-screen-rule] — verify a genuine data-exposure risk in later work draws a plain-English red flag rather than silence; any miss is a mandatory capture. Confirmed by: the first session where a real data-exposure risk surfaces after push + reinstall.
- [red-flags-structure] — verify a red flag Claude raises lands in QUEUE.md's Red flags section with a state, and an accepted flag's decision appears in the session LOG. Confirmed by: the first red flag raised, and the first flag accepted, after push + reinstall.
- [allow-parallel-sessions] — verify opening a /plan chat while a build is active is no longer refused (the active-build session-start message naming planning-alongside was confirmed in-session against a fixture). Confirmed by: the first time a /plan session is opened alongside an active build after push + reinstall.
- [make-drift-visible] — verify a session in a drifted project (missing a scaffolded file/folder) opens with Claude plainly flagging what's out of date and offering /setup, while a current project on a higher plugin version stays silent (the presence-based logic and no-false-alarm were confirmed in-session against fixtures). Confirmed by: the first session in a drifted project after push + reinstall.
- [setup-closeout-redesign] — verify a real /setup run in a fresh folder creates the git repository silently, the close-out names /done, and /done writes a setup-shaped LOG entry and commits the scaffold; a Case C migration close with a leftover _build.md recommends resuming /next instead. Confirmed by: the first /setup run in a fresh folder after push + reinstall. (host-side)
- [approval-display-blockquotes] — verify the next /plan or /done approval draft (LOG entry, capture, or batch) arrives as a labelled blockquote that wraps, not a fence. Confirmed by: the first /plan or /done approval draft after push + reinstall. (host-side) [Commit-step clause dropped 2026-06-16: superseded by [closeout-text-collapse], whose own deferred test now covers the collapsed commit step.]
- [show-before-write] — verify a later /plan writes nothing to QUEUE.md without the verbatim entry in the immediately preceding message; the case to watch is late-session, after compaction. Confirmed by: the first /plan batch write in a long/compacted session after push + reinstall. (host-side)
- [session-start-dirty-tree-check] — verify the live one-liner at session start with known dirt and no _build.md (the fixture test — dirty-without-build warns, dirty-with-build silent, clean silent — passed in-session this goal session). Confirmed by: the first session opened with a dirty tree and no active build after push + reinstall. (host-side)
- [plan-state-artifact] — verify the live resume offer: interrupt a /plan mid-processing, open a new session, watch for the "INTERRUPTED PLANNING SESSION" report (the fixture test — _plan.md detected, dirty-warning suppressed with _plan.md present, silent when absent — passed in-session this goal session). Confirmed by: the first interrupted /plan reopened after push + reinstall. (host-side)
- [capture-verbatim-first] — verify that /plan's present-and-interview sends the one-line preamble plus the verbatim item before any analysis (with the post-quote re-read separator), and /next's pre-flight sends the top batch verbatim before the blocker-gate findings. Confirmed by: the first /plan capture turn and the first /next pre-flight after push + reinstall. (host-side)
- [closeout-text-collapse] — verify the next /done runs one entry approval, then a commit step that states the title/body are the approved entry verbatim (only the commit-and-push ask, no fresh review) and commits via git commit -F. Confirmed by: the first /done after push + reinstall. (host-side)
- [tag-definition-redesign] — verify later sessions lead with the decision and the brevity tags hold against the wall-of-text pull. Confirmed by: the first /plan or /next session after push + reinstall. (host-side)
- [verbosity-output-style] — verify sessions visibly lead with the decision and chunk one item at a time while staying plain English (not terser/jargon-y), and the concise output style shows as forced-active (which also confirms plugin output-styles/ auto-discovery). Confirmed by: the first session after push + reinstall. (host-side)
- [deferred-test-lifecycle] — verify the first session after the update shows the hook deferred-tests line; the next /plan proposes rolling the runnable backlog into a test batch; a later /next pre-flight shows no deferred-tests listing. Confirmed by: the first session + /plan + /next after push + reinstall. (host-side)
- [dependency-scan-reference-roles] — verify the next /plan over a citation-bearing capture routes the evidence citation without false parking and names the classification at recommend time. Confirmed by: the first /plan over a citation-bearing capture after push + reinstall. (host-side)
- [scope-boundary-rule] — verify the next /next session that meets a Claude-noticed discovery routes it to Captures at the moment of noticing (draft, show, "anything else?", resume), not "for the queue" at an undefined later. Confirmed by: the first /next that meets a Claude-noticed discovery after push + reinstall. (host-side)
- [spec-edit-batch-type] — verify a /next spec-edit batch edits SPEC.md without being blocked, and a normal feature build still cannot touch SPEC unless it lists SPEC.md in Files. Confirmed by: the first /next spec-edit batch run after push + reinstall. (host-side)
- [queue-plan-markers] — verify the next /plan that authors an audit batch with dependent work inserts a "--- Plan session here: <reason> ---" marker, and the next /next that meets one halts and names the reason. Confirmed by: the first such /plan and /next after push + reinstall. (host-side)
- [ship-freeform-next-type] — verify the next real freeform need runs through `/next freeform` (or a queued Freeform batch): the gate asks build/test/audit-first and requires a why-none-fit; scope grows ask-by-ask; captures are filed but a warning offers /plan; /done routes to done-freeform.md. Confirmed by: the first freeform session after push + reinstall. (host-side)
- [done-unconditional-read] — verify the next /done in the same session as its build visibly reads _build.md in full before Phase 1, regardless of session memory. Confirmed by: the first same-session /done after push + reinstall. (host-side)
- [post-close-capture-record] — verify the next post-close tail capture updates the entry's Routed-to-Captures line uncommitted; the next session's commit carries both; the hash backfill still resolves the entry to its /done commit. Confirmed by: the first post-close tail capture after push + reinstall. (host-side)
- [done-recommend-next-both-ways] — verify the next /done close states the waiting-captures verdict in the clean case without prompting (not only when something blocks). Confirmed by: the first /done close with captures waiting but none overlapping, after push + reinstall. (host-side)
- [staleness-flag-fix-path] — verify the next /done staleness flag of a pure pointer drift offers an in-session fix with approval; a fate-decision flag defers to /plan. Confirmed by: the first /done staleness flag after push + reinstall. (host-side)
- [push-offer-fit] — verify the next /done after a planning session asks commit-only by default; a /done after a build still offers the dual ask; a repo with no remote is never offered a push. Confirmed by: the first planning-session /done and the first no-remote /done after push + reinstall. (host-side)
- [scope-lock-drop-dash-stripping] — verify a live denial on a dash-annotated Files: line in the installed host (the parser change was Claude-tested in-session via module import; the live hook path defers). Confirmed by: the first such denial after push + reinstall. (host-side)
- [done-spec-sync-check] — verify a build that lands a spec-affecting change without a prior /plan spec entry draws a filed capture at /done close; a build with no spec impact stays silent. Confirmed by: the first spec-affecting build /done after push + reinstall. (host-side)
- [verbatim-first-rationale] — verify a later /plan capture turn lands the verbatim item first without bundling or forced-wait (ties to the existing [capture-verbatim-first] line). Confirmed by: the first /plan capture turn after push + reinstall. (host-side)

## Captures

Captured outside /plan. Picked up and routed during the next /plan session. Processed captures (slug assigned, dependencies scanned) sit above the `---` divider; unprocessed raw captures collect below. See plan.md Capture and parking discipline.

---

**Self-hosting notes inventory — findings from [self-hosting-notes-audit]**

> Routing consciously deferred at the 2026-06-16 /plan to a dedicated session. Reason: this is a 34-finding distribution arc needing per-finding home decisions — too judgment-heavy for the tail of a long session. Most findings are (b) stay-in-CLAUDE.md (no work) or (c) funnel into the parked, blocked [self-hosting-support-during-setup] (premature). Only the ~7 (a) generalize-and-ship findings are genuine relocation work, and several of those are already shipped (pure CLAUDE.md cleanup). Process this in a focused /plan.

Audit run 2026-06-15 (goal session). The complete inventory of every self-hosting rule, convention, and judgment in the project, with where each lives, a candidate home, and whether its rationale is written. This is the committed inventory the [self-hosting-notes-audit] design called for: the next /plan authors the follow-on relocation batches from these findings (relocation, never copying — the new home lands and the CLAUDE.md source comes out in the same batch). Candidate homes are candidates only; the decision is /plan's. Homes: (a) shipped-generalized, (b) this project's CLAUDE.md, (c) the parked [self-hosting-support-during-setup] /setup-scaffolding scope.

1. **Note:** The plugin exists as "host" (installed, governs the live session) and "target" (editable source at `plugin/si-plugin/`). Target edits do nothing until packaged and reinstalled. **Lives:** CLAUDE.md "Host and target". **Candidate home:** (c) — host/target is the defining self-hosting concept any plugin-building consumer needs. **Rationale written:** yes.

2. **Note:** Ambiguous references to "the plugin / the hooks / the procedures" must specify host or target; default is target. **Lives:** CLAUDE.md "Host and target". **Candidate home:** (b) — local disambiguation convention for the developer's chat. **Rationale written:** yes (also MEMORY.md).

3. **Note:** Most target changes become host changes on reinstall, but changes outside the plugin package (project doc structure, this CLAUDE.md) don't propagate and need manual updates. **Lives:** CLAUDE.md "Host and target". **Candidate home:** (b) — concerns this repo's own non-propagating files. **Rationale written:** yes.

4. **Note:** Batch ordering assumes the next batch sees the previous batch's effects — true for target-side edits (readable at author time), false for host-side changes (hooks, loaded skill docs, plugin-behaviour.md) that only refresh after push + reinstall. **Lives:** CLAUDE.md "Self-hosting dependency ordering". **Candidate home:** (c) — [self-hosting-support-during-setup] lists this discipline. **Rationale written:** yes (worked example).

5. **Note:** When a batch depends on a previous batch's host-side effects, /plan must place it after a push marker and annotate its `Depends on:` line as `(host-side)`. **Lives:** CLAUDE.md "Self-hosting dependency ordering". **Candidate home:** (a) — /plan authoring behaviour; shipped plan.md has never heard of push markers. **Rationale written:** yes.

6. **Note:** The line `--- Push required before continuing ---` halts /next until the user has pushed and reinstalled. **Lives:** split — convention/authoring side in CLAUDE.md "Push-marker convention"; the halt ships in next.md pre-flight. **Candidate home:** (a) — the /next halt already ships; the authoring half should join it. This split-across-homes is the audit's named trigger case. **Rationale written:** yes.

7. **Note:** The push marker is hard in only one direction — it halts /next because batches past it read host-side state; it does NOT suspend decided rules/reasoning, and is not a wall for planning work. It marks a ship-by aim. **Lives:** queued batch [push-marker-hard-direction], not yet written into CLAUDE.md. **Candidate home:** (b) — the batch routes it to this project's CLAUDE.md. **Rationale written:** yes.

8. **Note:** Rezip and Push are distinct. Rezip builds a fresh zip for private dogfooding (no bump, commit, or remote). Push is the full release ritual that publishes. **Lives:** CLAUDE.md "Rezip and Push". **Candidate home:** (c) — [self-hosting-support-during-setup] lists "push-and-rezip steps". **Rationale written:** yes.

9. **Note:** Rezip procedure: delete `__pycache__` under `plugin/si-plugin/`, repackage overwriting the zip (zip the folder so internal paths start with `si-plugin/`), verify no `__pycache__` entries, tell Alex nothing was published. **Lives:** CLAUDE.md "Rezip" steps. **Candidate home:** (b) — exact commands/paths are this-machine specific; the concept (clean bytecode before zipping) is the scaffolding-level note. **Rationale written:** yes.

10. **Note:** Push ritual: backfill LOG hashes, bump version (patch vs minor), run the two-pass pre-push sweep, archive the old zip, prune to three, clean `__pycache__`, repackage+verify, stage paths+zip+archive+plugin.json+LOG, commit "Bump to v… and repackage", push, tell Alex to reinstall. **Lives:** CLAUDE.md "Push" steps 1–10. **Candidate home:** (b) — full ritual with literal commands is local; the high-level shape is the scaffolding abstraction. **Rationale written:** yes.

11. **Note:** Version bumping lives on push, never rezip — bumping on every test build would make Alex's own projects nag "re-run /setup". **Lives:** CLAUDE.md Push step 2. **Candidate home:** (c) — [self-hosting-support-during-setup] lists "version bumping". **Rationale written:** yes.

12. **Note:** Pre-push consistency sweep — two passes: gather unpushed commits and their LOG entries, then check target internal consistency (templates vs docs), project docs, and CLAUDE.md for staleness. **Lives:** CLAUDE.md Push step 3. **Candidate home:** (c) — [self-hosting-support-during-setup] lists "pre-push consistency sweep". **Rationale written:** yes.

13. **Note:** Zip-archive mechanics — archive the previous zip as `si-plugin-v<OLD>.zip`, prune to three; git history is the authoritative record, so a test-build overwrite in the archive is cosmetic. **Lives:** CLAUDE.md Push steps 4–5 + "Archive accuracy". **Candidate home:** (b) — specific to this repo's packaging layout. **Rationale written:** yes.

14. **Note:** Clean `__pycache__` before any zip so Python bytecode never ships. **Lives:** CLAUDE.md Rezip step 1 + Push step 6. **Candidate home:** (b) — tied to this plugin shipping Python hooks; literal command is local. **Rationale written:** yes.

15. **Note:** At session start with no `_build.md`, run `git status --porcelain plugin/si-plugin/`; if dirty, warn and list paths (possible orphaned sweep edits). **Lives:** CLAUDE.md "Session-start dirty-tree check". **Candidate home:** (a) — queued [session-start-dirty-tree-check] moves this into session_start.py for every consumer and removes the manual section. **Rationale written:** yes.

16. **Note:** A "goal session" runs with the plugin off so Claude works autonomously through several build batches in one chat, closed by manual /done. **Lives:** CLAUDE.md "Goal sessions (plugin off)". **Candidate home:** (b) — the developer's own autonomous-dev workflow; its formalization is an open fork (/goal vs cruise control). **Rationale written:** yes.

17. **Note:** In a goal session the session-start hook never fires, so its LOG-hash backfill doesn't run; manual /done must backfill by hand (oldest-`git log -S` rule), folding the edit into the commit. **Lives:** CLAUDE.md "Goal sessions (plugin off)". **Candidate home:** (b) — interim handling tied to the not-yet-supported /goal mode. **Rationale written:** yes (labelled interim; thin — no permanent home yet).

18. **Note:** The session's own behaviour is the thing under test — all use of the plugin to develop the plugin is testing it; any observed Claude behaviour routes to Captures, not memory. **Lives:** CLAUDE.md "Rules for Claude". **Candidate home:** (b) — defining self-hosting judgment, specific to the developer dogfooding. **Rationale written:** yes.

19. **Note:** Host-side deferred tests (confirmable only after push + reinstall) are the dominant deferred-test flavor in self-hosting; nearly every change here defers, making the section look far larger than a consumer's would. **Lives:** QUEUE.md Deferred tests + [deferred-test-lifecycle] + "Deferred tests vs test batches" capture. **Candidate home:** (a) for the lifecycle / (b) for the "self-hosting inflates the count" observation. **Rationale written:** yes.

20. **Note:** The /done close-out backstop ("did this session's own activity confirm a pending deferred line?") pays mainly in self-hosting but stays universal because no mechanical self-hosting flag exists to condition on. **Lives:** QUEUE.md [deferred-test-lifecycle]. **Candidate home:** (a) — ships into done.md universally, self-hosting reasoning travels as rationale. **Rationale written:** yes.

21. **Note:** `.si-version` records which plugin version set a project up; the hook compares it to the installed version only for the "an update just happened" signal — drift warnings are presence-based, not version-based (version bumps every release, would cry wolf). **Lives:** session_start.py + setup.md; [scaffolding-resync] / dev-project capture. **Candidate home:** (a) — shipped behaviour; the self-hosting friction (missing `.si-version`/`FAQ/`) is a (b) local capture. **Rationale written:** yes.

22. **Note:** The dev project drifts because nothing re-scaffolds it when the plugin gains new scaffolding — `.si-version` and `FAQ/` were missing because /setup was never re-run here. **Lives:** QUEUE.md [faq-backfill] + dev-project capture. **Candidate home:** (b) — self-hosting maintenance gap specific to this repo. **Rationale written:** yes.

23. **Note:** /setup is consumer-framed and fits awkwardly on the dev project — the host/target oddity isn't acknowledged, and migration scaffolding would create fresh drift. **Lives:** QUEUE.md "/setup on the dev project" capture. **Candidate home:** (c) — the capture proposes a self-hosting branch in /setup. **Rationale written:** yes.

24. **Note:** Telling the user "run /setup to bring everything up to standard" is an overpromise — migration only backfills missing files and stamps `.si-version`; it does nothing about content drift. **Lives:** QUEUE.md "/setup on the dev project" Outcome 2. **Candidate home:** (a) — bears on what the [make-drift-visible] / [scaffolding-resync] catch-up message promises any consumer. **Rationale written:** yes.

25. **Note:** [self-hosting-support-during-setup] — if a user builds a plugin with the plugin, /setup should scaffold the self-hosting workflow into their CLAUDE.md (push-and-rezip, host/target, pre-push sweep, version bumping, dependency-management discipline). **Lives:** QUEUE.md Parked. **Candidate home:** (c) — this *is* that scope; the destination for most consumer-facing notes here. **Rationale written:** yes.

26. **Note:** The first /goal session exposed that the method has no explicit goal-session shape — it assumes one batch per session, so a multi-batch run improvised an aggregate `_build.md`, multi-thread LOG entry, and single commit. **Lives:** QUEUE.md "First autonomous /goal" capture + LOG 018152a. **Candidate home:** (b) — developer's autonomous-mode workflow, not yet shipped. **Rationale written:** yes.

27. **Note:** Pushing planning state in self-hosting is costly — a push off a no-plugin-change commit triggers the full push-and-rezip ritual, so /done's push offer should default to commit-only for planning closes. **Lives:** QUEUE.md [push-offer-fit]. **Candidate home:** (a) — ships the commit-only default into done-plan.md; self-hosting is the sharpest motivating case. **Rationale written:** yes.

28. **Note:** Cross-doc references in `plugin/si-plugin/` docs name their target ("the blocker gate in next.md's pre-flight"), never a step number, because step numbers silently retarget on renumbering. **Lives:** CLAUDE.md "Working conventions" + LOG 9f1b80b. **Candidate home:** (b) — host-only authoring rule for editing the plugin's own source. **Rationale written:** yes.

29. **Note:** post_tool_use.py's `ALLOWED_SUBHEADINGS` must grow when new batch types ship — a maintenance coupling between the lint hook and the queue format the plugin defines for itself. **Lives:** post_tool_use.py docstring + denial text; echoed in [spec-edit-batch-type], [ship-freeform-next-type]. **Candidate home:** (b) — code-maintenance note for whoever edits this hook. **Rationale written:** yes (only as code comment — thin; not a stated convention).

30. **Note:** git-safety denials match command text, not intent, so a denial can fire on a command that carries the pattern only as data; the note tells Claude to assemble such strings at runtime. **Lives:** pre_tool_use.py `PATTERN_AS_DATA_NOTE` + LOG 61bfd2f. **Candidate home:** (a) — shipped in the hook; the surfacing case (writing the pattern as a test string) is a plugin-dev scenario. **Rationale written:** yes.

31. **Note:** This project's "Where things live" tree and Architecture enumerations describe the self-hosting repo layout (plugin/, zip-archive/, target source) that no consumer has. **Lives:** CLAUDE.md "Where things live" + "Architecture". **Candidate home:** (b) — describes this repo's dev layout. **Rationale written:** n/a (descriptive). Note: stale counts already captured separately ("2 hooks" vs three, "Target v1.11.0" vs 1.12.0).

32. **Note:** Taskflowapp is the E2E test consumer; Alex runs E2E in a separate session and observations come back as queue items — the self-hosting project uses a real external consumer to test what it can't test on itself. **Lives:** CLAUDE.md "E2E testing". **Candidate home:** (b) — names a specific external project and cross-session workflow. **Rationale written:** yes.

33. **Note:** Reading QUEUE.md as audit target means decided-but-unshipped notes enter the inventory without waiting to land — the queue itself is treated as authoritative target state. **Lives:** QUEUE.md [self-hosting-notes-audit] rationale. **Candidate home:** (b) — meta-judgment about this audit/distribution arc. **Rationale written:** yes.

34. **Note:** Distribution discipline — each relocated note lands in its new home AND its CLAUDE.md source comes out in the same batch (relocation, never copying), so no danglers survive; the arc ends with a CLAUDE.md sweep for stragglers. **Lives:** QUEUE.md [self-hosting-notes-audit] rationale. **Candidate home:** (b) — process discipline for this arc. **Rationale written:** yes.

Coverage note: the shipped procedure docs and templates carry essentially no self-hosting content — the single exception is next.md's push-marker halt (finding 6). That absence is the audit's thesis: self-hosting knowledge lives in CLAUDE.md and session judgment, not in the method. Two rationales are thin: finding 29 (lives only as a code comment) and finding 17 (labelled interim, no permanent home). Factual confirmation, not new findings: CLAUDE.md still reads "Target v1.11.0" and "2 hooks" while plugin.json/`.si-version` are 1.12.0 and three hook files exist — both already captured.

**Present-and-interview forced-wait: analysis must follow the verbatim quote in the same flow, not after a user reply**

Observed 2026-06-16 processing [retire-registry]. Claude quoted the capture verbatim, then stopped and asked "anything to add first?" before giving any analysis. This defeats verbatim-first: the quote exists so the user can read while Claude composes the analysis, so the analysis should arrive right behind the quote in the same flow. Stopping after the quote makes the user wait twice — once for the quote, then again after they reply — cancelling the benefit. plan.md's present-and-interview rule already names this exact failure mode ("forced-wait — stopping after the quote and gating the analysis behind the user's reply") and says the correct shape is quote-first, analysis-in-the-same-flow. So this is the rule not holding in practice, not a missing rule. For /plan to weigh: whether the rule needs strengthening despite being clearly written — a sharper tag, or a worked exemplar at the step — or whether this is a one-off to note. Relates to [capture-verbatim-first] and [verbatim-first-rationale].

**Pull test-session transcripts from the raw .jsonl session logs (self-hosting workflow)**

Raised by the user 2026-06-16. Claude Code keeps a raw log of every session as a `.jsonl` file (one record per line, can include thinking steps), stored under the `.claude` projects folder (per project: `.claude/projects/<project-slug>/`). This is the authoritative, unedited session record. In future, self-hosting testing should pull a testing session's transcript from this location rather than asking Claude to regenerate or recall it. Why: a Claude-generated transcript is a reconstruction — lossy, and it hits the handoff-provenance problem (Claude-authored content treated as fact), whereas the raw `.jsonl` is the real evidence. Applies to E2E sessions in the consumer project (Taskflowapp) and to goal/dev sessions here — when an audit or review needs a session transcript, source it from the `.jsonl` log. Relates to the self-hosting testing workflow and [self-hosting-support-during-setup]. Filed while scoping the Taskflow /setup audit, which needs exactly this transcript.

**plugin.json description says "two hooks" — should be three**

Noticed 2026-06-16 while applying the CLAUDE.md version close-fix. `plugin/si-plugin/.claude-plugin/plugin.json`'s description reads "Four skills (/setup, /plan, /next, /done) and two hooks for scope enforcement," but there are three hooks (session_start + pre_tool_use enforcing, post_tool_use advisory). It's consumer-facing (shows in the marketplace / install screen). Fix the count to three and ideally note two enforce, one advises. Low priority.

**Findings from [audit-taskflow-setup-transcript] — the Taskflow /setup re-run audit (2026-06-16)**

Routing note: F1–F4 below cluster into a "migration path for /setup" theme that has no existing home. The parked [self-hosting-support-during-setup] is about self-hosting workflow scaffolding, not migrating an older-vocabulary or foreign source — so it is a related but different scope. Per the QUEUE plan-marker above the retire-registry batches, process these together with the [audit-taskflow-first-spec-edit] findings in one /plan. Each finding was checked against current target state; none were already fixed. Transcript: `resources/captures/2026-06-16-taskflow-setup-session.jsonl` (record numbers cited).

**/setup has no migration path for an older-vocabulary or foreign source system**

Observed auditing the Taskflow /setup re-run. The live host (1.12.0-test4) met a project already fully set up under the method's older doc vocabulary — UX.md, BACKLOG/, MANIFEST.md, build-log/ — with no SPEC.md and no .si-version. setup.md's Step 1 keys "already set up" (Case C) on SPEC.md existing. With no SPEC.md the project was classified as Case B (content, no method docs), which steers toward scaffolding a fresh parallel doc set. Claude recognised the truth — set up, just on older names — and overrode the procedure by hand, inventing the whole old-to-new mapping (records 23, 54, 70, 852). Checked against current target: still present. Step 1 Case C still keys on SPEC.md, and Step 2C migration scaffolding is only reachable from Case C, so an old-vocab or foreign source is never detected as a migration. Why it matters: migrating from a foreign or older system is a real adoption path. Without detection, /setup actively misleads ("not set up yet") and leaves Claude to improvise the entire source-to-SI mapping with zero guidance, which is error-prone for any source that is not already old-SI. Relates to F2/F4 below.

**The session-start hook reinforces the /setup misdetection**

Observed in the same audit. For a folder with content but no SPEC.md, session_start.py's State 1 says "files but no SPEC.md — it hasn't been set up." That message pointed the wrong way for an old-vocab project that WAS set up under other names (records 2, 852 point 1). Checked against current target: still present (the `if not has_spec:` branch). Why it matters: the hook is the first orientation the user and Claude see, so the misread started before /setup even ran. Same root as the migration-path finding: detection is blind to method-shaped docs under non-current names. A migration-aware check could spot old-vocabulary docs (UX.md / BACKLOG / MANIFEST / build-log) or the old CLAUDE.md path-block and ask "looks like an older-vocabulary project — migrate?" instead of "fresh start."

**A 1:1 doc rename (UX.md to SPEC.md) imported a role mismatch the user then had to schedule cleanup for**

Observed in the same audit. The migration renamed the deliberately-exhaustive old UX.md straight to SPEC.md. But SPEC is meant to be product truth — what the product is, who it is for, how it works, why — not an exhaustive UX manual. The result was a knowingly-bad SPEC. The user caught it, and a SPEC-trim audit batch had to be queued to fix it later (records 745, 747, 852 point 4). Checked against current target: not fixed, because no migration path exists at all. Why it matters: renaming a doc by position without checking whether its old role matches its new role silently imports debt. A migration-aware /setup should flag a role mismatch — old doc broader or narrower than its SI counterpart — at migration time, so the user decides up front rather than discovering it in a later planning pass.

**The dead CLAUDE.md path-block caused a mid-migration reversal**

Observed in the same audit. Claude first planned to keep the docs inside no-code-method/ using CLAUDE.md's old path-block, then read the hooks, found they hardcode project-root paths (the path-block is a dead feature in this version), and reversed the plan in front of the user (records 58, 70, 852 point 3). Checked against current target: docs are still resolved at the project root and the path-block is still dead. Why it matters: a load-bearing migration constraint — docs must live at the project root, there is no path indirection — was discovered by trial mid-flight. Stating it up front in any migration guidance prevents the detour. Relates to F1/F2.

**/setup narration leaked internal and technical terms an external non-coder would not follow (mild)**

Observed in the same audit. Setup narration used hook filenames (session_start.py, pre_tool_use.py), "_build.md," "scope-lock," "method docs," and "Case-B" framing (records 70, 75). setup.md deliberately carries no response-shape tags and runs before the behaviour rules — and their plain-language Vocabulary translate-or-omit rule — load, so nothing guards the audience rule during /setup. Checked against current target: still no plain-language guard for /setup narration. Why it matters: the plugin's audience is external non-coders, and a real foreign-system migration would surface the same terms. Lowest-confidence of the set: this was the developer's own migration and the content was genuinely technical, which softens it. It may be acceptable for migration specifically — flagged for /plan to judge rather than asserted as a defect.

### Parked

- **[narration-vs-menu-drift]** Observed during 1b7d359 /plan: Claude defaulted to menu-style options ("file as capture, drop it, or commit to the rule now?") when narrating a recommendation would have been more appropriate. Dependency ownership's narration rule ("narrate the ordering work" — exercise judgment, recommend) is supposed to catch this. The mechanism failed under exploratory back-and-forth tone — the pull toward "lay out the options" was stronger than the pull toward "state the recommendation, let user push back." Worth watching whether this generalizes: when the conversation gets exploratory, does Claude soften from recommendation-narration into menu-listing? If so, the narration rule needs tightening — possibly explicit text that menu-style enumeration of equally-weighted options is *not* narration when Claude actually has a preference, and the recommendation must come first with the menu as fallback.
  Blocked by: a second observed instance of menu-style enumeration where a recommendation was due — behavioural trigger, no slug; fires at the /plan that processes such a capture.

- **[sweep-include-canonical-doc]** Observed at the 2026-06-15 goal session, building [deferred-test-lifecycle]: that batch's lifecycle-description sweep entry named four downstream places to update but omitted done.md's own Deferred tests section — the canonical statement the other four describe — which carried the same stale wording. It was fixed in-session only because the same batch happened to rewrite that section for other reasons, so the omission did not bite. The pattern: a build entry shaped as "update these N places," derived from a canonical doc, can leave the canonical doc itself off the list because the author is focused on the downstream copies. Candidate fix if it recurs: a one-line reminder in plan.md's batch-authoring guidance to include the source/canonical doc in any such sweep. Low priority — no harm this time.
  Blocked by: a second observed instance of a sweep entry omitting its canonical source doc — behavioural trigger, no slug; fires at the /plan that processes such a capture.

- **[inline-internal-term-marker]** Decide whether to add an inline marker for internal-only terms in procedure prose. The marker would let procedure docs flag internal terms inline so the translate-or-omit rule fires mechanically rather than relying on Claude matching against the vocabulary list each time.
  Blocked by: [narration-vocabulary] + observed leakage after it ships

- **[user-execution-batch-shape]** When the user is the executor of a batch (gather these receipts, identify the lender, call the ATO) rather than Claude, the existing build/test/audit shapes don't quite fit. Build batches assume Claude executes; test batches are about verification; audit batches are read-and-route. A user-execution batch sits closest to a test batch in mechanics (user runs steps, Claude facilitates), but it's not verification — it's the primary work. Observed during /setup on a tax-prep folder: queueing batches that were mostly user-action items felt weird, even though step-by-step communication rules in plugin-behaviour.md would handle the running well. Three possible landings: (a) new `User:` subheading alongside Build/Test/Audit, (b) covered by existing types + freeform once shipped, (c) framing-only — "build" means "user does it" in non-coder projects, no new structure. Decision premature without running several user-execution batches first.
  Blocked by: experience from 2–3 user-execution batches run in the tax project — external behavioural trigger, no slug; fires when that experience reaches a /plan session here.

- Add scenarios to reader-test-workflow.js — evaluate which scenarios are still undertested and worth adding. Known blind spots regardless of refresh outcome: /setup interview (untested), push-and-rezip sweep (untested — lives in this project's CLAUDE.md, not plugin docs, so coverage question is whether it should even be in scope for plugin reader-tests), mid-build resume from a real _build.md (current next.md sim covers fresh /next, not resume), /done plan-mode close-out (current sim only covers build close-out), empty-queue handling, audit-batch flow (planning-as-work). Promote as one or more build batches once scenarios are picked. The refresh itself shipped at 2356cb7 ([reader-test-refresh]), so only the run remains.
  Blocked by: refreshed workflow run once — behavioural trigger; the first refreshed run may surface blind spots not on this list, or may show that scenario count matters less than scenario specificity.

- Cruise control skill — the consumer-facing end-goal: a skill that runs build→commit→build→commit through a batch (or multiple batches) unattended, stopping only when it hits something requiring user input. The /goal-formalization arc ([close-shipped-slug-crosscheck] + [formalize-goal-session]) is step 1 of this — it builds the multi-batch close mechanics (shipped-slug cross-check, multi-thread LOG) that cruise control inherits, while a human still bookends the run; cruise control then adds the autonomy, the gate, and the unskippable judgment on top. Key design concerns: (1) wording that doesn't pressure Claude to push through uncertainty, (2) dependency management when Claude decides when to wrap a batch, (3) /done judgment steps can't get skipped for speed; (4) the red-flags gate — an open red flag in the active scope blocks the unattended run, only resolved or accepted flags let it proceed, and a user who leaves a flag open stays on hand to approve each step (the gate is a hook reading the three flag states defined by [red-flags-screen-rule]); (5) the handoff-claim-marking format — whether a handoff / context prompt marks which claims are user-vouched versus Claude-authored, or whether the standing "Claude-authored handoff content is unverified until the user confirms it" rule (already in CLAUDE.md) suffices (folded in from the /goal fork, item 9, 2026-06-16).
  Blocked by: the /goal-formalization arc landing ([close-shipped-slug-crosscheck] + [formalize-goal-session]) AND a few formalized goal sessions run, so the multi-batch close mechanics are proven before the human is removed from the loop — behavioural trigger. The original autopilot prerequisites ([no-planning-in-execution], [queue-plan-markers], [audit-findings-bulk-approval]) have all shipped. Full no-approval auto-file of audit findings is in this item's own design scope — interactive audits keep bulk approval. Named as the end-goal in the thinking-work capture, 2026-06-10.

- **[self-hosting-support-during-setup]** Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping, **and the dependency-management discipline** (host-vs-target distinction as it governs batch ordering, the host-side-after-push-marker rule, the `--- Push required before continuing ---` queue convention, and the `(host-side)` annotation on `Depends on:`). All of this carries into the new project's CLAUDE.md. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
  Evidence (folded in from the "/setup on the dev project" capture, 2026-06-14): running /setup on this self-hosting dev project surfaced the consumer-framing friction directly — the host/target oddity isn't acknowledged in the flow, and migration would scaffold a `FAQ/` folder this project never adopted (fresh drift). This strengthens the case for a self-hosting branch in /setup (e.g. the "are you building a plugin?" question), and adds an open sub-question: do self-hosting dev projects adopt consumer scaffolding like `FAQ/` at all, or opt out? Full session record: resources/captures/2026-06-14-setup-on-dev-project-session.md. Still parked — the design waits for the trigger below.
  Blocked by: a second self-hosting consumer appearing — a user reports building a plugin (or any project that ships itself) with the plugin, or Alex starts one; external behavioural trigger, no slug. The scoping decision (interview question vs skill vs template) waits for that real case to design against.

- Threshold-based context management — if hooks ever gain token usage fields (e.g. `context_usage_pct`), the plugin could recommend `/compact` or `/clear` based on actual utilization instead of rule-based triggers. Research filed at resources/research/context-window-hook-access.md.
  Blocked by: Anthropic adding token data to hook event input — external trigger, no slug.

- **[lint-citation-refire]** Observed at [queue-format-lint-hook] build testing, 2026-06-12: the prose-citation check re-fires on every QUEUE.md edit for references it has already flagged. The check is stateless — it reads the whole file, not the edit — so a reference the user has judged "citation, fine" gets flagged again on every later edit, indefinitely. The build already cut the worst noise by flagging only references to slugs still defined in the file: a dry run showed references to shipped work were the bulk (~2.5KB of advisory text per edit), and a reference to shipped work can only be a citation. The residue is real: the first live run flagged ~21 batches, all naming pending items, and any judged-as-citation among them will keep re-firing. Candidate fixes if live use shows this as noise: an inline convention marking a reference as a deliberate citation, which the lint would skip (new format design, /plan's call); or accepting the re-fire as cheap advisory background. The hook is not yet in the installed host — it was built after the v1.11.0 push — so no live session has run with it yet.
  Blocked by: live experience with the lint hook — behavioural trigger; fires once a few /plan sessions have edited QUEUE.md with the hook installed and the re-fire can be judged noisy or tolerable.

- **[behaviour-doc-size-watch]** Filed at the 2026-06-13 /plan, from a doc-size review. plugin-behaviour.md is the largest doc by content (~3,074 words / 135 lines at counting time) and the most expensive position in the system: it is injected at every session start, and skill sessions pay it twice until [behaviour-doc-double-load] ships. Many queued batches add rules to it — the approval rules, authoring standards, scope anchor, memory boundaries, no-planning-in-execution — so it will grow before it settles. Decided at the review: no blanket terseness pass. The rationale-everywhere style is the compliance bet; stripping why-clauses to save tokens buys back the failure mode they were installed to fix. Duplication-targeted trims are already queued ([tag-restatement-trim], [trickle-up-next-md-duplicates], [trickle-up-ask-when-unsure], [behaviour-doc-double-load]). The remaining lever is the progressive-disclosure restructure — compact core injected, full doc loaded at skill time — already noted as a revisit in [behaviour-doc-double-load]'s rationale. This capture is the re-measure trigger: when it fires, re-count plugin-behaviour.md, compare against ~3,074 words, and weigh the restructure on real numbers instead of trimming mid-flux.
  Blocked by: the compliance arc's plugin-behaviour.md additions landing — behavioural trigger, no single slug; fires at the /plan after the queued rule-adding batches have shipped and the doc's contents have settled.

- **[firing-map-middle-band]** Firing data for the progressive-disclosure restructure, from the firing-map audit (2026-06-13). These rules fire in two or three skills but never outside a skill — so they don't earn the every-session injection on the "fires outside skills" test, but they aren't single-skill trickle-down candidates either. The band (skill counts as of 2026-06-13): Index entries (3 skills — /plan readiness gate, /next pre-generate, /done writes it; the retrieve path reads the index but doesn't apply the authoring rule); Unpark watch (3 — /plan read-state + loop, /next pre-flight, /done close-out); Staleness watch (3, same surfacing moments — [staleness-flag-fix-path] extends it); Empty Batches → /plan (2 — /next pre-flight, /done recommend-next); User owns scope (2 — /plan promote-park-drop, /next whether-to-proceed; [scope-anchor] rewords it); Resume reads _build.md (2 — /next resume, /done reads it); /plan-for-planning vs /next-for-building (2–3, boundary rule); and borderline cross-skill reads — Depends/Blocks headers and stable slugs, authored in /plan but referenced elsewhere. Why it matters: this band is what the restructure is for — compact core injected with the fuller doc loaded at skill time, or a shared sub-doc the relevant skills load, or canonical-in-one with a read-on-demand pointer. This record is the firing data the decision should rest on, instead of a guess. Queued additions weighed 2026-06-16: [scope-anchor], [scope-boundary-rule], [no-planning-in-execution], and [audit-findings-bulk-approval] were all kept in the injection for now (scope discipline already lives there; the no-planning permission half and the bulk-approval exception are genuinely injection-shaped) — reconsider localizing the two scope rules ([scope-anchor], [scope-boundary-rule]) into next.md/plan.md as part of this restructure.
  Blocked by: [behaviour-doc-size-watch] — surfaces when the progressive-disclosure restructure is taken up; fold this in then. The line numbers and band membership are a 2026-06-13 snapshot to re-derive at that point, not apply (the band shifts as [scope-anchor], the trickle batches, and the compliance-arc additions land).

- **[full-tag-placement-recheck]** A fresh full placement re-check of response-shape tags across all procedure docs — setup.md, plan.md, the next and done families, plugin-behaviour.md — to grade the corrected state after [output-tag-audit]'s fixes ship, and to catch any tag drift since that audit (commit 0405315). Distinct from [opening-narration-audit], which measures narration volume at openings; this one re-checks per-step tag placement everywhere, the same lens [output-tag-audit] used, re-run on the post-fix docs. Deferred deliberately: running it before [output-tag-audit]'s findings build would mostly re-discover gaps already sitting in the queue.
  Blocked by: this 2026-06-16 /plan round's tag/narration batches shipping — behavioural trigger, no slug. The original blockers ([next-done-tag-sweep], [plan-step1-sequencing], [setup-self-contained-no-tags]) have landed, but the 2026-06-16 /plan adds further tag/narration work (e.g. the bound-aggregate-opening-narration finding), so promoting the re-check now would grade docs still in flux. Fires once this round's tag/narration batches have shipped, so the re-check grades settled docs — same deliberate-deferral logic that parked it originally.

- **[scaffolding-resync]** Content-level scaffold drift: when a scaffolded file already exists but its template changed later (e.g. a doc template gains a new section), a project that has the file won't pick up the change. [make-drift-visible] catches *missing* files and folders, but not this content-level drift, because the file is present. Open question: how to detect that a present file is behind its template, without a full /setup re-run that would overwrite user content. The drift is general, not self-hosting (Taskflowapp, a plain consumer project, had the same missing file); the version-bump false-alarm worry is mooted by [make-drift-visible]'s presence-based check. Lower priority — the missing-file case (the one that actually hurt) is handled by [make-drift-visible].
  Blocked by: first observed instance of content-level scaffold drift biting — a present scaffolded file falls behind its template and causes a problem; behavioural trigger, no slug; fires at the /plan that processes such a report.

- **[plan-md-offload-reframe]** Add an explicit instruction that Claude may record the rest of a multi-step plan in _plan.md (or _build.md) and release only the next item — turning the working file into a deliberate pressure-release against the pull to dump everything for completeness. Filed as a candidate, not a redirect: this session's analysis concluded bundling is mostly a disposition problem, not memory-capacity (within a session Claude has the whole transcript; the research attributes bundling to trained thoroughness / "task completion over process compliance"), so the highest-leverage fix is priority (the output style) plus structure (lead-with-decision, one-item chunking). The reframe might still add a humane "the rest is safely recorded, release just the next item" that lowers completeness anxiety — speculative, and possibly redundant once [verbosity-output-style] is live. Relates to [tag-definition-redesign] and [verbosity-output-style].
  Blocked by: observing whether [verbosity-output-style] (shipped, awaiting reinstall) closes the bundling pull on its own — behavioural trigger, no slug; fires at the /plan after the output style has been live long enough to judge whether bundling persists. If it persists, the reframe earns its words; if not, it's redundant.
