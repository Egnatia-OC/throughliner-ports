# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Audience anchor in this project's CLAUDE.md**
The plugin ships to external non-coders, not the person developing it. Without an audience anchor in this project's CLAUDE.md, skill docs drift — language meant for the developer leaks into chat output the user sees. Adding an Audience section makes the distinction visible to any session editing skill docs, so future skill-doc work writes for the right audience by default.

Build:
- This project's CLAUDE.md: add an Audience section establishing that the plugin's users are external non-coders (not the person developing the plugin), and that anything skills cause Claude to say to the user — chat narration, drafts, prompts, status lines — must read cleanly without referencing internal procedure terms.

**Split Plan close-out and remove all /compact recommendations**
The capture flagged Plan close-out's Step 4 as having the same bundled shape as Build close-out's old Phase 3 — push prompt + next-up + always-/clear in one breath. The V47 split fixed that anti-pattern in Build close-out by separating "what's queued" from "push and context"; Plan close-out deserves the same treatment so each decision lands as its own turn. Interview surfaced a related principle: /compact is being phased out as a recommendation. It was only ever hedging by maintaining daisy-chained context between builds, and /clear has proven stable. That collapses Build close-out Phase 4's asymmetric context advice (push → /clear, no push → /compact) into a single line — push or not, /clear is the right move. Same removal applies anywhere /compact is currently recommended (plan.md Step 4 close-out at minimum; setup.md and next.md need a scan). The rule is universal but stays skill-doc-local rather than going into behaviour.md, because it needs to be sequenced carefully against each skill's flow.

Build:
- done.md Build close-out Phase 4: remove the /compact branch. Becomes "Push to remote? (yes / not yet)" followed by "Either way, run /clear before the next skill."
- done.md Plan close-out: split current Step 4 ("Handoff") into Step 4 ("Recommend next") and Step 5 ("Push and context"). Step 4 mirrors Build Phase 3's shape with Plan-flavored branches — batches exist → "Next up is [batch]. Run /next when ready"; batches empty → "Queue is clear. Run /plan when you have more." Step 4 is its own turn; wait for user acknowledgment before Step 5. Step 5: push prompt, then /clear (no /compact branch).
- plan.md Step 4: drop "/compact or" from the context advice. Becomes "Run /done to record this and commit, or keep planning. Run /clear first to keep context clean."
- setup.md and next.md: scan for any /compact recommendations and remove. If found, replace with /clear-only advice mirroring the new convention.

Test:
- Grep across plugin/si-plugin/ for "/compact" — should return zero hits, or only legitimate non-recommendation references (flag any of those for review).
- Re-read done.md end to end. Build close-out should flow Phase 1 → 2 → 3 → 4 with Phase 4 collapsed to push + /clear. Plan close-out should flow Step 1 → 2 → 3 → 4 (Recommend next) → 5 (Push and context) with each turn standalone.

**Pull "one item at a time" rule into behaviour.md**
Alex's global CLAUDE.md carries a detailed rule about sequencing multi-part responses — one per message when the next action depends on the previous, count upfront, no preview, alternatives are the one exception. The plugin currently delegates this to the user's CLAUDE.md via the tag-precedence note in behaviour.md, which means it only governs unlabelled steps and free conversation when the user has it set. On any install without that rule, skills' close-outs and walkthroughs become bundle-prone. The [SEQUENCE] tag already covers procedure steps that explicitly carry it, but the broader principle — applying to any multi-part response across the session — needs to be plugin behaviour, not user preference. The Communication section is the right home.

Build:
- behaviour.md: add a "Sequencing multi-part responses" rule under Communication. Cover: one item per message when the user's next action depends on the prior one, state the count upfront, don't preview upcoming items, close-outs and walkthroughs are where the pull to bundle is strongest, the one inversion is alternatives the user is choosing between (because the choice requires seeing them together).

**Add "thinking work isn't a batch" rule to plan.md**
The current Ground rules section says "Never build during /plan" but has no inverse — nothing stops planning work from being queued as a batch. Surfaced twice this session: I framed both the trickle-up audit and the output tag overhaul as candidate batches when both are planning work whose output is decisions, not changed files. Without a structural rule, this becomes a judgment call each time and defaults to whatever shape the previous capture took. Naming the recurring shapes (audits, reviews, reconciliations/drift checks, design exploration) gives the routing decision a clear test.

Build:
- plan.md Ground rules: add a rule pairing the existing "Never build during /plan" — never queue thinking work as a batch. Name the four shapes (audits, reviews, reconciliations/drift checks, design exploration), include the test (if the main work is figuring something out rather than executing on a decision, it's planning work), and state that thinking work runs inside /plan and spawns batches as output. Place it right after "Never build during /plan."

**Brief batch display at /next start**
Step 1.4 of /next currently dumps the full batch text — title plus every entry — when starting a build. That re-renders content the user just wrote in QUEUE.md and can open anytime. A brief summary serves the user better: title (which batch), one-line gist synthesized from the rationale (what it's about), and entry counts (how big). The full text lives in _build.md the moment the user confirms; QUEUE.md has it before then.

Build:
- next.md Step 1.4: replace the "Batch title and all entry text from QUEUE.md" bullet with an instruction to display the batch title, a one-line gist drawn from the rationale, and entry counts (build / test).

**Verbatim-copy strings in fenced blocks; combine commit approval**
In the desktop app, Ctrl+C copies the whole assistant message, so strings the user needs to lift verbatim (commit message, commit body, paste-ready prompts) only work as copy targets when each one sits in its own fenced code block. Commit message and body are the most frequent case — every /done. Currently they're presented and approved as separate steps, which is redundant; they can be displayed together as two adjacent copyable blocks and approved in one go. A general rule in behaviour.md keeps this from drifting back as other copy-need cases surface.

Build:
- behaviour.md: add a rule that strings the user is meant to copy verbatim must be presented in fenced code blocks. Cover the why (desktop app Ctrl+C copies the whole message, so only fenced blocks give a clean copy affordance). Examples: commit messages, commit bodies, paste-ready prompts.
- done.md Build close-out Section 2.4 (commit step): rewrite to present the commit message title and commit body each in its own fenced code block in the same message, then ask for a single approval covering both.
- done.md Plan close-out Section 3 (commit step): same change.

**Tag the no-test-section decision as [SILENT]**
When /plan drafts a batch without a Test section, the absence currently gets narrated ("No Test section because the change is verifiable..."). That narration is noise — the user wrote the rationale and knows what kind of change it is. The existing tag system covers this case; using `[SILENT]` rather than prose keeps the procedure doc consistent with how output behaviour is described elsewhere.

Build:
- plan.md Step 3 Test section: tag the omission case as `[SILENT]` so the decision to skip a test section doesn't get narrated to the user. Use the tag, not a prose substitute.

**Backfill LOG hashes at the start of /plan and /next**
The current /done flow writes LOG with `[HASH]` placeholder, commits, runs `rev-parse` to fill in the hash, then amends — but the amend changes the hash, so the recorded value is stale (13c4612 / 44ab617 this session). Move the infill out of /done entirely: /done leaves the placeholder committed. The next /plan or /next session, at start, finds any `[HASH]` placeholders in LOG/log.md and LOG/index.md and fills them with the hash of the commit that introduced the entry. The infill is just a working-tree edit; whatever commit that session later makes folds it in — no separate commit, no amend, no two-commit flow.

Build:
- done.md Section 2.4 (Build close-out commit step): drop steps 5–7 (rev-parse, replace placeholder, amend). The committed LOG entry keeps the `[HASH]` placeholder. Section ends after the commit.
- done.md Plan close-out Section 3 (commit step): same simplification.
- next.md Step 1 pre-flight: add a sub-step at the very start `[BRIEF]` — scan LOG/log.md and LOG/index.md for `[HASH]` placeholders. For each, find the hash of the commit that introduced that entry (e.g. `git log --diff-filter=A --pretty=%h -- LOG/log.md` walked top-down, or blame-based) and replace in place. No new commit; the infill is uncommitted working-tree state that the session's next commit picks up.
- plan.md Step 1: add the same backfill sub-step at the very start, before the captures/discussion question.

**Promote recommendation must name concrete outputs**
The current /plan procedure asks for promote/park/drop before the batch entry is drafted, so the user approves a direction without seeing what would actually get built. This session that gap was bridged by Claude's style — concrete outputs got named at recommendation time organically. Style isn't a guarantee; a different model could recommend promote in abstract terms, leaving the user to approve blind. Codifying it structurally — promote must describe what would actually get built, in terms the user can recognize as the work product — closes the hole regardless of model. If the interview hasn't yielded enough to describe it concretely, the recommendation isn't ready; keep interviewing.

Build:
- plan.md Step 2 sub-step 2 (Recommend): change the Promote bullet so it requires describing what would actually get built — in terms the user can recognize as the work product. Add a forcing-function clause: if sub-step 1's interview hasn't yielded enough to describe it concretely, the recommendation isn't ready — keep interviewing. Park and Drop bullets unchanged.

**Tighten Why-pipeline preserve and retrieve rules**
behaviour.md's Why-pipeline section already covers preserving rationale as prose and retrieving it from LOG when a user asks why-questions. Two gaps blunt the rule. Preserve doesn't call out the common collapse-shapes (one-line summaries, dedicated why-fields, typed taxonomies) that look reasonable to a future doc or skill designer but lose meaning silently — without naming them, the same mistake gets remade. Retrieve doesn't mention LOG/index.md — so a why-search reads the full log files when the one-line-per-entry index would point to candidates first, faster and more accurately. Both edits serve the same end: when the user asks "why is the app like this?", the answer needs to exist as preserved prose AND be findable.

Build:
- behaviour.md Why-pipeline > Preserve: expand the existing rule to explicitly name the three collapse-shapes — one-line summaries, dedicated why-fields, typed taxonomies (e.g. "UX reason / functionality reason"). The expansion must include its own why woven in as inline prose (not a labelled field) so the rule models what it asks for: each shape loses meaning differently — a line truncates the reasoning behind a decision; a taxonomy is never complete and forces nuance into the closest pre-defined slot.
- behaviour.md Why-pipeline > Retrieve: update the search instruction to use LOG/index.md first (the one-line-per-entry summary) to find candidate entries, then read the full prose in LOG/log.md or LOG/log-v*.md. The Prior decisions section already references this rule and inherits the change.

**Stage sweep edits at push; warn on dirty plugin tree at session start**
push-and-rezip step 8 stages a fixed list (zip, archive, plugin.json, LOG/) that doesn't include whatever the pre-push sweep modified. Sweep edits — prose tightening in plugin/si-plugin/ to keep templates and skill docs aligned with the procedure changes being pushed — fall out of the commit and sit orphaned in the working tree across sessions. The next /next can then layer build edits on top of orphaned sweep changes, mixing unrelated work into one commit. Two complementary fixes addressing the two failure modes: at push, stage every dirty path in plugin/si-plugin/ rather than a named list (catches sweep edits automatically); at session start, when no build is in progress, warn if plugin/si-plugin/ has uncommitted state (catches existing orphans before a new build layers on top). Both edits land in this project's CLAUDE.md — the push-and-rezip workflow lives there, not in the shipped plugin.

Build:
- CLAUDE.md push-and-rezip step 8: replace the fixed stage list ("zip, archive changes, plugin.json, LOG/ changes") with an instruction to stage every dirty path in `plugin/si-plugin/` (via `git status --porcelain plugin/si-plugin/`) plus the zip in `plugin/`, archive changes in `plugin/zip-archive/`, and LOG/ changes. Sweep edits get caught automatically.
- CLAUDE.md (this project's, root): add a session-start dirty-tree check. When a session starts with no `_build.md` present in the project root, run `git status --porcelain plugin/si-plugin/` and warn the user if non-empty, listing the dirty paths. Surfaces orphaned sweep edits before /next layers build changes on top.

**Mirror response shape tags into CLAUDE.md and template**
The response shape tags (`[SILENT]`, `[BRIEF]`, `[PROMPT]`, `[DISCUSS]`, `[SEQUENCE]`) live in behaviour.md, which only loads on-demand. So at session start, Claude doesn't have the tags in immediate context — when /plan drafts changes to procedure docs, it tends to write prose describing output behaviour instead of reaching for an existing tag. Mirroring the tag names and one-line meanings into CLAUDE.md puts the system in front of Claude from the start, making tag use the default move when authoring. The same mirroring into CLAUDE-TEMPLATE.md propagates to consumer projects via /setup. Drift risk between the two copies is low — the tag set is stable.

Build:
- this project's CLAUDE.md: add a brief "Response shape tags" section mirroring the five tag bullets from behaviour.md (names + one-line meanings only). The sub-sections in behaviour.md (Unlabelled steps, Tag precedence) stay there as elaboration; CLAUDE.md surfaces just the at-a-glance reference.
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md: add the same mirrored section so consumer projects get it on /setup.

### Parked

- Sizing gates rework — research filed at resources/research/batch-sizing-research.md. Three changes slated: (1) reframe "name concrete outputs" as the readiness gate (what differentiates batch-ready from still-a-capture), (2) remove the 5-test verification-burden rule, (3) replace with coherence test ("can Claude explain the batch in one sentence without multiple 'and's"). Further research needed on session-length as a mid-build split indicator — scroll bar length correlates with quality drop / auto-compact; is this because higher communication quality makes session length mirror cognitive load? Could a simple metric (word count, turn count) work as a split yardstick both mid-build and at planning time when actual session length isn't yet known?

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.


- Trickle-up audit: review all procedure docs (setup.md, plan.md, next.md, done.md) for rules that are repeated across multiple docs or aren't skill-specific. Move them to behaviour.md so they're stated once and apply everywhere.

- Output tag overhaul audit: review all procedure docs (setup.md, plan.md, next.md, done.md) for prose that describes output behaviour where a tag ([SILENT], [BRIEF], [PROMPT], [DISCUSS], [SEQUENCE]) should be used instead. Includes: _build.md entry ticking in next.md should be [SILENT] (crash-recovery bookkeeping, not a status report).


### Parked

- Batch cohesion ordering heuristic — the build log as decision log creates pressure for discrete builds, and batch ceremony is friction for users. Queue ordering rule: builds touching an area with no related batches yet should sink (absent urgency or dependency), giving time for more captures to accumulate and make the batch worthwhile. Batching also touches context window management, not just coherent logging — Claude needs to think about one area of related concerns at a time. Needs design work to sharpen "no friends" and "related" into a mechanical rule. (The companion /next-time check — recommend switching to /plan if related captures exist for the top batch — shipped as the next.md blocker-gate capture scan.)
- Cruise control skill — a skill that runs build→commit→build→commit through a batch (or multiple batches) unattended, stopping only when it hits something requiring user input. Key design concerns: (1) wording that doesn't pressure Claude to push through uncertainty, (2) dependency management when Claude decides when to wrap a batch, (3) /done judgment steps can't get skipped for speed. Parked: depends on stabilizing the skills it would chain.
- Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
- /done spec check — after writing the **Why:** field, Claude checks whether any reasoning constitutes a product decision that should update SPEC.md. Retrospective check (at decision time) vs the current /plan pipeline gate (prospective, at planning time). Both mechanisms need more real usage before deciding how they relate.
- Threshold-based context management — if hooks ever gain token usage fields (e.g. `context_usage_pct`), the plugin could recommend `/compact` or `/clear` based on actual utilization instead of rule-based triggers. Research filed at resources/research/context-window-hook-access.md. Parked: depends on Anthropic adding token data to hook event input.
- Pre-push sweep could be lighter if /done flagged host-side impacts at build time — accumulate a manifest of "this change affects X in project docs" during /done while context is fresh, then the push sweep checks flagged spots instead of re-reading everything. Sweep stays as safety net but gets cheaper. Design question: cross-build staleness (build 3 invalidates something build 1 touched) still needs the sweep to catch it.
