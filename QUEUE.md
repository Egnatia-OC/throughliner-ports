# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### Rename every occurrence of "session" that means a run, per the audit's classification [session-vocabulary-corrections]
Filed 2026-08-17 from the same settlement. **The corrections pass, which cannot start without the audit's line-by-line list.**

**What changes.** Each occurrence the audit classified as meaning a run is reworded to say run; each classified as the chat or as correct is left untouched. The stop-list is honoured rather than re-derived.

**Scope includes the code, which is a different case.** `session_id` names the chat and is the harness's own field, so it is not renameable; what is ours is the variable names, the comments and the `_build-<session_id>.md` filename — and that filename is parsed by `pre_tool_use.py`, so changing it is a hook-enforced-format change whose ripple is traced by grep first. The code is not the loose-usage case settled by [work-item-term-in-hook-and-script-code]: there the code used a term loosely for the same thing, here it uses the word for a different thing.

**Lifted 2026-08-21.** [session-occurrence-audit] shipped — `LOG/2026-08-21-session-occurrence-audit.md` carries the full line-by-line classification (941 matches, ~50 meaning a run, listed per file and line), so the corrections pass now has the list it waited for.

--- Build block ---
Changes: the run-meaning occurrences listed in `LOG/2026-08-21-session-occurrence-audit.md`
  are reworded to say "run" — across `plugin/throughliner/docs/` (next.md, plan.md,
  done.md, done-build.md, next-build.md, setup.md and the others the audit lists),
  `templates/faq-template.md` with `FAQ/faq.md` re-copied, and SPEC.md's listed lines.
  Occurrences the audit classified as the chat or as technical names are left untouched;
  the stop-list is honoured rather than re-derived. The `_build-<session_id>.md` filename
  and `session_id` are NOT renamed — harness fields, per the item's own prose.
Acceptance: every line the audit lists as run-meaning now reads "run" (or is recorded in
  the entry as deliberately left, with why); no stop-list occurrence changed; grep for
  the audit's listed lines confirms.
Refused: renaming `session_id` or the working-file name — harness-owned, and the
  filename is parsed by `pre_tool_use.py`.
--- End build block ---

#### Flavour-specific close material sits in the file every close reads, and the restyle passes will not move it [done-md-carries-other-flavours-material]
**Captured on your instruction 2026-08-21**, after you asked why a planning close ran to roughly 6,000 tokens. The measurement is in `resources/research/why-the-close-is-heavy.md`; this item is the one lever that research names as unqueued.

**The measurement, in one line.** That close read **10,297 words of procedure** — `done.md` 7,443 plus `done-plan.md` 2,854 — to write **3,603 words of record**, about 2.9:1 against the output. The record is the smaller half, so shortening session records does not reach this.

**`done.md` is a fixed toll on every close in every project**, whatever the session did, and it is the second-largest doc in the method after `plan.md`. The sub-docs exist to carry flavour deltas, and a large amount of flavour-specific material is not in them.

**What a planning close reads and discards**, none of it skippable, because knowing which parts apply requires having read them:

```
the completion-verification step        build and audit only
the record-a-routing-step-sweeps block  build and audit only
the entry template's build body fields  build only
the entry template's audit body fields  audit only
the audit approval-outcomes line        audit only
the red-flag lifecycle                  only where a flag cleared
the isolated-session branch             only in a worktree
```

**Why the two queued restyle items do not cover it.** [law-prose-restyle-heavy-docs] applies the wording standard and a subordination lens; [rationale-lens-after-the-build-view] relocates rationale out of operative statements. Both make the text shorter where it stands. **Neither asks whether the text is in the right file**, which is a distribution question — the third limb of the rule gate, and the one nothing in the queue currently exercises over the close docs.

**The precedent is this project's own.** A run used to read the whole queue to build a handful of items; the build view now gives it only what it is building. This is the same shape one layer out — a close reading the whole close manual to run one flavour — and the remedy was simply never applied here.

**What to settle at processing, and the sequencing question is real.** Which material moves and which is genuinely shared; whether the entry template splits per flavour or stays whole with the sub-docs pointing into it, since a split template is the thing most likely to drift into four divergent copies — that risk is the argument the shared file was built on and it has not been weighed against the measurement. **And whether this runs before or after the two restyle passes**: moving text first means the restyle rewrites each paragraph once in its final home, but a distribution pass over text about to be reworded may move sentences that are then merged away.

**One thing not claimed.** No figure here is a target, and a shorter close manual that drops a step is worse than a long one that works — `done.md`'s length is largely accumulated repairs to real failures, several of which it names in its own text. **This item moves text; it must not delete any.** A rule that leaves `done.md` still exists, and the acceptance test is that nothing is lost.

**Files (rough):** `plugin/throughliner/docs/done.md`, `done-plan.md`, `done-build.md`, `done-audit.md`. Shipped: every consumer pays the same toll at every close. Relates to [law-prose-restyle-heavy-docs] and [rationale-lens-after-the-build-view] (the same files, a different lever), and to [split-the-cleared-region-for-concurrent-sessions] (the precedent).

**This build also reverses the one sibling-axis dedup on record, settled 2026-08-22 on your instruction that docs are deduplicated only against parents and above.** The 2026-08-15 pass (`b4de5bf`, `LOG/2026-08-15-route-to-unprocessed-duplicated-across-close-subdocs.md`) compared done-build.md and done-audit.md against each other and hoisted their shared routing-step record block into done.md; moving that block back into the sub-docs, which the table above already lists, is the reversal. The same pass's justification deletion stands — it evicted against the always-loaded rule, a grandparent, which the axis rule permits. A capture for the reversal ([reverse-sibling-dedup]) was deleted as covered by this item.

**Kept 2026-08-21, all three questions settled.** What moves is the seven flavour-specific blocks the table above lists, each into the sub-doc for the flavour that uses it. The entry template stays whole in done.md with the sub-docs pointing into its per-flavour fields — a split template is the four-divergent-copies risk this item names, and pointers get most of the saving without it. It runs after the two freeform passes so each paragraph is rewritten once and then moved as final text, which is why it is held below the line behind them.

Rule gate: run — a distribution pass: rules move between files and none is authored, amended in substance, or evicted; the gate's distribution limb is the whole of what this exercises, and the acceptance test is that nothing is lost.

--- Build block ---
Changes: `plugin/throughliner/docs/done.md` — the seven flavour-specific blocks its
  own table lists (completion-verification, routing-step sweep, build body fields,
  audit body fields, audit approval-outcomes, red-flag lifecycle, isolated-session
  branch) move out; the entry template and genuinely shared material stay, with
  pointers where a sub-doc needs a template field. `done-plan.md`, `done-build.md`,
  `done-audit.md` — each receives the blocks for its flavour, placed where its
  entry-writing step reads.
Acceptance: every moved block is findable verbatim-or-tightened in exactly one
  sub-doc; nothing is deleted — a diff shows moves, not losses; a planning close's
  read no longer includes the build/audit-only blocks. Statement counts per file
  reconciled in the session record.
Refused: splitting the entry template per flavour — the divergent-copies risk the
  shared file was built against.
Refused: deleting any rule in passing — this item moves text and must not shorten
  by loss; shortening is the freeform passes' job, already done by the time this
  runs.
--- End build block ---

**Lifted 2026-08-21.** Both freeform passes it waited on are done by hand and recorded — `LOG/2026-08-21-cut-length-remaining-docs-2.md` and `LOG/2026-08-21-law-prose-remaining-thirteen-docs-2.md` — so every paragraph this item moves has been rewritten once in its final form, which is the ordering its keep decided.

#### Freeform sessions cannot edit the files their queue item names — the scope-lock's standing list denies them [freeform-blocked-by-standing-list]

Found 2026-08-21, mid-session, attempting the queued freeform item [cut-length-remaining-docs] by hand. The scope-lock (`pre_tool_use.py`, Rule 4) covers any session with no build working file under the planning standing list — QUEUE.md, SPEC.md, LOG/, FAQ/, research, scratchpad, INBOX — and denies everything else outright. A freeform session has no build working file by construction, so a `[freeform]` item whose work edits `plugin/throughliner/docs/` is undoable as designed: the deny message says to queue the work, but the work is already queued, as an item the queue says must be done by hand. The hook's own top docstring still says Rule 4 "asks, never deny", which the code no longer does — the docstring is stale against the deny decision recorded in `_is_plan_quiet_path`.

The workaround available in-session is hand-writing this session's build working file with the item's file list, so the scope-lock enforces an agreed list instead — a workaround, not a design. Design question for /plan: how does a freeform session declare its file scope? Options seen: a sanctioned freeform marker or working file the hook reads; or the deny becoming an ask when the top cleared item is `[freeform]` and names the path. Whatever is chosen, the stale "asks, never deny" docstring should be corrected in the same build.

**Kept 2026-08-21, shaped as the sanctioned declaration.** A freeform session opens by writing its own scope file — a freeform marker, not a borrowed build working file — listing the files from its queue item's build block; the hook reads it and scope becomes that list plus the standing list. The list still originates at planning, so nothing widens without an agreed item behind it. The declare-scope instruction lives in the always-loaded `[freeform]` flavour block, because a freeform session runs no skill and reads nothing else. SPEC's scope-lock paragraph gained its carve-out sentence at this keep. FAQ: not needed — the declaration is Claude's move, reported in one line; nothing a user does changes.

Rule gate: run — admitted as a subordinate clause on the `[freeform]` flavour block in skill-nonspecific-rules.md, its named parent; no freestanding rule, no slot beyond the clause, nothing evicted; enforcement is the hook's. Failure evidence is one live instance, the 2026-08-21 freeform sitting, worked around by hand on approval.

--- Build block ---
Changes: `plugin/throughliner/hooks/pre_tool_use.py` — Rule 4 accepts a freeform scope
  file (`_freeform-<session_id>.md`, same location as the build working file) whose
  listed paths extend the standing list for that session; the top docstring's stale
  "asks, never deny" is corrected to the deny decision. `plugin/throughliner/docs/
  skill-nonspecific-rules.md` — the [freeform] flavour block gains one clause: before
  the first edit, write the scope file from the item's build block and report it in
  one line. `resources/testing/` — assertions for allow-on-listed, deny-off-list, and
  unchanged behaviour when no scope file exists.
Acceptance: a session with a freeform scope file edits its listed files and is denied
  unlisted ones; a session without one behaves exactly as today; the hook suites pass;
  the docstring no longer says "asks, never deny".
Refused: deny-becomes-ask keyed on the top cleared item — the hook would parse queue
  prose per write, and per-file asking on agreed work is the friction the lock rejects.
Refused: reusing the build working file — the close and the one-build-at-a-time rule
  read that file as a build's.
--- End build block ---

#### The two-limb keep check pushes research into build items, beating the rule that says research is done in planning [research-packaged-as-build-work]
Captured by you 2026-08-14, from a live instance in another project minutes earlier: a planning session proposed splitting an item into "one build item where I do the research and write the findings into `resources/research/`" plus a slimmer `[user]` line. Your framing is the finding — research is never planned into work items, and if research can be done now in /plan then it is. **You also observed this is suddenly happening a lot, which is what the diagnosis below explains.**
**It happened three times in one day.** Twice in this session — research queued into [faq-entry-criteria], and research folded into [shipped-spec-maintenance-rules] — and once in the other project. Both of this session's instances were corrected on your instruction; the SPEC one needed no research at all, because `resources/research/spec-document-standards.md` already answered it.
**Nothing was deleted, and the rule is intact.** `plan.md` still carries "/plan resolves what it can in-session; capture is only for what it can't", with `research` listed first among what /plan resolves now. The defect is not a missing rule.
**Three things make it lose, and the third explains the timing.** It is not stated as a rule about research — it is one word inside a fenced list of six, so "research belongs in planning" must be inferred. It is hedged by the sentence immediately after, "A default, not an absolute", a standing licence to make the exception. And the keep-check pushes the other way with far more force.
**The mechanism, which is this capture's substance.** To keep an item, `plan.md` requires stating the build in both limbs — which files change, what changes inside them — and calls it blocking. When the answer isn't yet known, the cheapest way to pass both limbs is "research X, then change Y", which reads as a fully specified build. So the check that exists to keep undesigned work out of Processed is the same check that rewards packaging research as build work. It fires hardest exactly where the answer is unknown, which is where research is needed.
**The timing, confirmed from git rather than assumed.** The two-limb check was hardened 2026-08-10 in `f8b03ea`, which introduced "This is a blocking check, not a prompt to try harder", the instruction to state both limbs before recommending keep, and the warning that a bare file list is what undesigned work looks like. Before that it existed in a softer form; after it, a keep can be refused. Four days later the pattern is visible across projects. An earlier `git log -S` attributed the change to `989c38b` — a false positive, since `989c38b` is the rename that moved the whole package folder and shows every string as newly added. Recorded so the trace isn't run twice with the same wrong result.
**What this is not.** Not a case for weakening the keep check. It stopped undesigned work reaching Processed, a real failure with real instances. Two correct rules were put into conflict and the stronger won.
**The shape of the fix, to settle at processing.** The clause belongs on the keep check itself, where the pressure lands, not on the research bullet, which is already there and already ignored: an item that cannot state its build *because the answer is not known yet* routes to doing the research now, in this session, and only what /plan genuinely cannot resolve is captured. Weigh also whether "A default, not an absolute" should go — it is the sentence that licenses the exception, and by this project's standard a rule qualified into a default loses every contest.
**Files (rough):** `plugin/throughliner/docs/plan.md` — the keep-check sub-step, and the resolve-now block's hedge. Shipped, not host-only: this fires in every consumer's planning session, and the prompting instance was in another project.

**Skipped 2026-08-21, and what settles it is named: the [keep-step-accretes-from-five-items] audit, cleared the same day.** That audit writes out the whole keep-step as it now stands and judges each clause's site — and this item's fix is a further clause on that same step, so deciding it before the composite reading exists would be the decide-piecemeal failure the audit was filed against. Process this at the first planning session after that audit reports, with its findings in hand; the audit's build block already names this item as evidence it reads.

**Kept 2026-08-21, with the audit's findings in hand.** The audit judged every keep-step clause correctly sited, so adding this one at the check itself follows its reading rather than fighting it. The shape is the item's own: the clause rides the two-limb check, where the pressure lands; the research bullet is left alone, already present and already losing. The hedge goes — "A default, not an absolute" is the licence the mechanism exploits, and the sentence after it carries the genuine test, so the restatement loses nothing.

Rule gate: run — admitted as a subordinate clause on plan.md's two-limb keep check, its named parent. Evicted in the same move: the resolve-now block's "A default, not an absolute" sentence, with its test sentence kept. Failure evidence is three instances in one day across two projects, mechanism confirmed from git. FAQ: not needed — planning behaviour changes, nothing a user does.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — the two-limb keep check gains one clause:
  where a limb cannot be stated because the answer is not yet known, the route is doing
  the research now, in this session, under the resolve-now rule — and "research X, then
  change Y" is named at the check as a research item wearing a build's shape, which the
  check must not pass. The resolve-now block's "A default, not an absolute." sentence is
  deleted; the sentence carrying the test ("can /plan resolve this with what it has
  right now") stays.
Acceptance: the clause sits in the keep-check sub-step naming the disguise; grep finds
  no "A default, not an absolute" in plan.md; the test sentence survives.
Refused: weakening the two-limb check — it correctly stops undesigned work, and both
  colliding rules are right.
Refused: strengthening the research bullet instead — it is already stated there and
  already ignored; the clause belongs where the pressure lands.
--- End build block ---

#### Ship a brevity output style in the plugin — Opus 5 verbosity breaks the experience, and `force-for-plugin` would fix every consumer on install [ship-brevity-output-style]
Filed 2026-08-22 from INBOX mail sent by another of your projects, carrying your own request from that session: a fix consumers actually get, not one they must set up. The message reports, verified there against the official Claude Code output-styles docs (fetched 2026-08-21): plugins can ship output styles in an `output-styles/` directory; a style with `force-for-plugin: true` applies automatically whenever the plugin is enabled, overriding the user's own style choice; `keep-coding-instructions: true` keeps the built-in coding instructions; styles reach the main conversation only, and take effect only after /clear or a new session. A built-in "Concise" style exists as a comparison point. Per the handoff-provenance rule these are the other session's claims — re-verify against the docs before building.

**This reverses a recorded decision, and the record must be weighed rather than skipped.** SPEC: "The plugin no longer ships an output style" — removed 2026-08-14 because its rules were stated three times over and triplication degrades the rules around it; the style's three rules moved into skill-nonspecific-rules.md. What is new since that decision: the failure being addressed is Opus 5's default verbosity rather than rule duplication, `force-for-plugin` gives a style reach the old one may not have had, and the message's third request — move brevity rules UP to the style and remove the duplication below — is the opposite of the triplication that killed the old style, and could come out net-negative in duplication. The old removal reasoning is not refuted by this; it has to be answered by the design: whatever ships at style level must be evicted from the always-loaded rules in the same move, or the 2026-08-14 defect is rebuilt.

**Three requests in the message:** ship the style (likely `keep-coding-instructions: true` + `force-for-plugin: true`); a README note on the verbosity issue, shrinking to a mention if the style ships; review the shipped docs for brevity/communication rules a system-prompt-level style would carry better, and de-duplicate.

**To settle at processing:** whether `force-for-plugin` overriding a consumer's own chosen style is acceptable — the docs call it a deliberate design decision, and it is exactly the consumer-override the 2026-08-14 removal celebrated ending; which rules move up; and whether the rule gate treats a shipped output style as method rule text (it is always-loaded in the strongest sense — system-prompt level — so the gate's distribution limb plainly reaches it).

**Kept 2026-08-22, all three settled on your approval.** Force is on — your framing was a fix consumers actually get, and a selectable style is the must-set-up kind; the override of a consumer's own style is accepted knowingly and stated in the README. The claims were re-verified live against the official docs this session — `resources/research/output-styles-plugin-capability.md`, filed with its index line. SPEC's output-style paragraph was rewritten at this keep to the new truth, bare, with the 2026-08-14 removal history left to the record. The message's third request — moving rules up and de-duplicating below — is split out as [style-level-rule-dedup-audit], placed immediately after this build; without it the triplication that killed the old style would be rebuilt, so that audit is the eviction half of this gate. **Dedup axis, on your instruction this session: docs are deduplicated only against their parents and above — the style outranks the always-loaded rules, so evicting downward from it is parent-axis by construction; sibling-to-sibling dedup is barred.**

Rule gate: run — the style is method rule text at system-prompt level, the strongest always-loaded distribution there is; its content is authored in this build from rules that already exist rather than new ones, and the matching eviction is carried by [style-level-rule-dedup-audit] plus the SPEC paragraph replaced at this keep. FAQ: needed — a consumer's own chosen output style stops applying when the plugin is enabled, which changes what choosing a style does; the entry ships with this item.

**Superseded in part 2026-08-22, on your decision, overturning the force-for-plugin mechanism kept hours earlier.** What falls: `force-for-plugin: true` — a silent override of the user's own chosen style, applied with no conversation, which you judged the wrong consent shape once asked how users would experience it. What replaces it, your design with one improvement found in the docs: **project-level switch-or-keep at /setup**, opt-out with acceptance as the default. The `outputStyle` setting lives per-project in `.claude/settings.local.json`, so the style lands only where Throughliner runs and their other work keeps their chosen style — better than the global scope your instruction assumed, and you approved the substitution. /setup first checks whether an `outputStyle` is already set; if so it names it and flags contradictions with ours; it explains why acceptance is strongly preferable — verbose models like Opus 5 produce runaway verbosity in doc-heavy projects and weigh sessions down with unnecessary narrative — says the scope is this project, and invites discussion before setup continues. Existing projects get the offer via the top-up's missing-setting list. **Appending our rules to a user's own style file was proposed by you and reversed on Claude's recommendation with your agreement** — it edits a file the user authored, the case you had already called bad. **And session_start checks the setting at every opening, on your instruction: where the style is not enabled for the project, one very short line says so; where it is, silence.** The earlier force-for-plugin reasoning ("a fix consumers actually get") is answered, not discarded: the opt-out default plus the every-session line is what keeps the fix reaching consumers without the silent override.

--- Build block ---
Changes: `plugin/throughliner/output-styles/` (new) — one brevity style, frontmatter
  `keep-coding-instructions: true`, NO `force-for-plugin`; body carrying the method's
  brevity/communication-shape steering, drawn from rules already in
  `skill-nonspecific-rules.md` — placement, not new rules. `plugin/throughliner/docs/
  setup.md` — new scaffolding step, opt-out with acceptance default: check any
  existing `outputStyle` first, name it and its contradictions, give the verbosity
  rationale (runaway verbosity on verbose models in doc-heavy projects), state
  project scope, invite discussion before continuing; on acceptance write
  `outputStyle` into the project's `.claude/settings.local.json`; the top-up's
  missing-setting list gains the same offer for existing projects.
  `plugin/throughliner/hooks/session_start.py` — check the project's `outputStyle`
  at every opening: not the Throughliner style -> one short line saying the brevity
  style is not enabled; enabled -> nothing. Suites under `resources/testing/` cover
  both branches. `README.md` — the verbosity note, shrunk to a mention of the setup
  offer. `templates/faq-template.md` + `faq-index-template.md` — entry on the setup
  question and the session-start line; re-copy both into `FAQ/`.
Acceptance: the style file exists without `force-for-plugin`; a fresh /setup makes
  the opt-out offer and writes the setting on acceptance; a session opening in a
  project without the setting carries the one short line, and one with it carries
  nothing; hook suites pass; README and FAQ updated.
Refused: `force-for-plugin` — a silent global override of the user's chosen style
  with no consent moment; superseded by the user 2026-08-22.
Refused: appending our rules to the user's own style file — edits a file the user
  authored.
Refused: folding the doc-dedup review into this build — corpus-wide judgment, split
  to [style-level-rule-dedup-audit].
--- End build block ---

#### [audit] Which brevity and communication rules does the shipped output style now carry better — report per-rule, parent-axis only [style-level-rule-dedup-audit]
Filed 2026-08-22 at the keep of [ship-brevity-output-style], as the eviction half of that item's gate — the message's third request, split out because it is a corpus-wide judgment pass. Reads the shipped style against `skill-nonspecific-rules.md` and the skill docs, and reports, per rule: stated in the style and where else, whether the lower statement should be evicted, and what a session that never loads the style (a subagent) would lose. **Axis constraint, on your instruction 2026-08-22: a doc is deduplicated only against its parents and above — the style, then the always-loaded rules, then a skill's own doc. Sibling-to-sibling comparison is barred; see [audit-axis-is-parent-not-sibling].** An audit edits nothing; findings become captures and the evictions are their own later work.

--- Build block ---
Changes: none — an audit edits nothing. Reads `plugin/throughliner/output-styles/`,
  `skill-nonspecific-rules.md`, the skill docs; reports per-rule findings as captures.
Acceptance: every rule stated in the style has a finding naming every lower site that
  states it, with an evict-or-keep recommendation and the subagent caveat weighed;
  the axis constraint is honoured — no finding compares sibling docs.
Refused: editing in place — audit discipline; evictions are later captures.
--- End build block ---

#### Design the standing audit set that maintains the rule corpus once the cleanup is finished [standing-audit-programme]
**Captured by you 2026-08-14. Your instruction, rendered in Claude's words rather than quoted: design the routine audits that you will run in the future and maintain the full corpus once we're done.** The reasoning below came out of that discussion — your strategy is yours, the argument about what it can and cannot retire is Claude's, and you asked for it to be captured.

**Your strategy, recorded first because the design serves it.** Dedupe and de-contradict the corpus first, cutting the word count and therefore how much there is to process; then design the audits and edits that put the final finish on the method rules, converting them into the law-prose style; then, once the always-loaded self-authoring rules are doing their job, stop needing to run these audits at all.

**The sequencing is right and is not what is being questioned.** Deduping before restyling is correct: a restyle over a corpus holding four copies of one rule restyles it four times and creates four chances to diverge. Cutting first means each rule is rewritten once. The `done-plan.md` merge processed the same day is that shape in miniature — four items, one file, one judgment applied consistently, where deciding them apart would have answered the same question four times inconsistently.

**Where the strategy overreaches: the self-authoring rules govern ADMISSION, and audits catch DRIFT. Different jobs.** Admission asks whether a rule should exist, worded this way, in this file — it fires when someone is writing a rule. Drift is what happens to a correctly-admitted rule *afterwards*, when something changes around it and the rule is left describing a mechanism that no longer exists. **No admission gate can prevent drift, because the cause arrives after admission.** Three items in the queue at writing are pure drift and every one passed admission cleanly: [done-md-names-a-repealed-clear-step], [adopted-claude-md-describes-retired-structure], [docs-b-name-outlives-the-two-docset-model]. A perfect gate produces all three anyway.

**The harder evidence: correct wording does not make a rule fire.** The corpus documents at least four instances of an always-loaded, correctly-worded rule failing: the provenance rule, shipped and sharpened, still not holding ([invented-rationale-compounds-past-the-shipped-rule]); the file-the-blocker rule, unambiguous and explained by the user five to ten times in a month ([nothing-blocks-it-read-as-a-dead-end]); the INBOX-opening step skipped in the very session that authors it ([inbox-open-step-not-enforced]); and the subagent-cost rule broken hours after being read. The provenance item already draws the conclusion: "state the rule again, or state it harder" is no longer a candidate direction.

**A fifth instance, carried here 2026-08-19 from [build-wrote-its-own-gate-disposition] when that item was deleted as already decided, and it is the sharpest of the five because the rule that failed was the gate's own.** A build in the eighteen-item run found itself authoring a shipped rule with no disposition to transcribe. `CLAUDE.md` instructs exactly that build to halt and say so. It had the instruction, and instead ran the gate's four questions itself and recorded the result — a description of an admission decision, written by the party that had already done the work, which is the failure the /plan siting exists to prevent. The design gap the deleted item suspected turned out not to exist: [stated-open-design-question-passes-the-keep-step] shipped 2026-08-17 in `7e3c1c8` and now refuses at the keep-step any item whose prose schedules a design decision into its build. What was left was a correctly worded rule that did not fire.

**The rule board is this experiment already run.** Built on the theory that the rules could watch themselves, it reported clean while five real rule defects shipped in the same session — see [rule-board-measures-paperwork-not-health], settled the same day as keep-and-rename for that reason.

**What the strategy genuinely buys, which is substantial.** Fewer rules and no duplicates means fewer sites where drift can occur, and each future retirement ripples to fewer places. An audit over a deduped corpus costs a fraction of one over the corpus as it stands. The win is real; it is a change in cost, not in necessity.

**So the goal is reframed rather than abandoned: not eliminate the audits, but make them cheap enough to run routinely without dreading them.**

**The design test this item applies, and it is the actionable part.** What retires an audit class is a **mechanical check, never a prose rule.** The queue lint and the digest genuinely removed the need to eyeball queue structure, because code reads the whole file and cannot skim. So for each drift class, ask first whether it is mechanically detectable: if yes, build the check and retire the audit; if no, the audit stays and gets a trigger. The board's retired-terms check is an existing instance of the first kind.

**What this item must produce.** The standing set itself — which audits, what each reads, what triggers each one, and how the user runs it without needing to remember it exists. A siteless audit is the failure this project has now recorded five times.

**One risk to design around.** The law-prose restyle is itself a large authoring pass over the whole corpus, and every rewrite is a chance to reintroduce what was just cut. It should be the last big pass and should be audited *after* rather than trusted to verify itself — the party doing the restyling is the party that would certify it, which is [rule-admission-has-no-independent-approver].

**The finish line this set takes over from is already assembled**, in the session that captured this item: twenty-two remaining items in five groups plus [law-prose-restyle], with five stated finish conditions. It lives in that session's LOG entry rather than in a queue item, because it is a record to be read rather than work to be done.

**Two of the five finish conditions are already mechanically checkable** by `resources/rule_signals.py` as it stands — no live rule naming a retired term, and no near-duplicate rule pairs. That is this item's own design test paying off before the design starts: the standing set inherits two conditions it never has to audit by hand, and should look for more of the same before proposing any audit a script could do instead.

**The comparison axis is split out and settled — see [audit-axis-is-parent-not-sibling].** It was the one fully designed part of this item, so on 2026-08-15 it was split off and kept into Processed on its own: audits compare a doc against its parent rather than its sibling, and each finding names where both sites fire. That half needs nothing further from this item; the standing set inherits it as a constraint every audit it designs must satisfy.

**Not kept, 2026-08-15, and why — this is design progress rather than a rejection.** The item fails the keep check's second limb by construction: its file list is whatever its own design produces, so it can never clear to run and a build would stall on it. It also should not be designed yet on its own reasoning — the set is meant to follow the dedupe and the restyle, and audits designed against a corpus about to be rewritten are audits designed against a shape that will not exist. **The user's decision was to split rather than design it now.**

**What remains to be designed, so the next session starts here.** Which audits are in the set; what each one reads; what triggers each one, given that a siteless audit is the failure this project has recorded five times; and how the user runs the set without having to remember it exists. Each candidate audit is tested first against this item's own rule — is the drift class mechanically detectable? If yes, build the check and retire the audit rather than designing it. Two of the five finish conditions already pass that test using `resources/rule_signals.py` as it stands, and the design should look for more of the same before proposing any audit a script could do instead.

**Files: not yet derivable, which is the point of not keeping it.** Likely `resources/method-compliance-audit-checklist.md`, `resources/rule_signals.py`, and `CLAUDE.md` for whatever trigger the set gets. Host-only. Relates to [rule-admission-has-no-independent-approver] for the restyle-audits-itself risk.

**Skipped again 2026-08-21, and what settles it is now two named cleared items.** The corpus rewrite it must follow is carried by the freeform pair [cut-length-remaining-docs] and [law-prose-remaining-thirteen-docs], both kept and cleared today. Process this at the first planning session after those two passes are done — the design question is unchanged, and the second limb still fails by construction, so it stays a capture.

**Designed and kept 2026-08-22, both passes done.** The set, by the item's own test — mechanical where detectable, audit only where judgment is irreducible. Retired-term naming and near-duplicates stay mechanical (existing checks; two finish conditions never audited by hand). **One new mechanical check, audit-lag, is the whole trigger design:** `rule_signals.py` reads git for commits touching the gate's staged-path set since the most recent compliance-audit LOG entry, and files one `[audit]` capture scoped to those changed files — satisfied while one is open, riding the existing run-at-rule-bearing-close site, so no audit in the set depends on anyone remembering. Its trigger is a fact (rule text changed since last audited), not a number. The accepted cost: one standing audit capture usually cycling in the queue — which is the routinely-cheap goal realized as delta-scoped audits rather than dreaded sweeps. **One audit class**, run by /next as ordinary `[audit]` work, criteria in `resources/method-compliance-audit-checklist.md`: delta scope, **parent-axis only** (your rule), four lenses — self-authoring compliance, mechanism-accuracy (does the rule describe what the code actually does), tag-placement/narration drift, and **disguised rationale**. **The fourth lens is yours, 2026-08-22:** history — text describing what the rules or product used to be, or how they came to be so — is rationale that does not read as rationale, which is why earlier why-clause audits missed it (the SPEC output-style paragraph found today is the instance); and the wider class is any unmarked why-form — precedent stories, reassurances, comparisons — caught by the existing delete-and-read test rather than by markers like "because". First instance filed as [post-restyle-compliance-audit], immediately after this build: the restyle audited by a party other than the restyler, with the history lens run over the whole corpus including SPEC, once, before anything is baked in.

Rule gate: run — two amendments and one eviction, dispositions here for the build to transcribe. (1) CLAUDE.md's "Rationale lives outside the operative rule" gains the history clause as a subordinate unit of that named parent: history is rationale and belongs to the record, detected by the existing delete-and-read test, no "because" required. Failure evidence: the SPEC output-style paragraph, found and rewritten 2026-08-22, having survived every earlier audit. (2) CLAUDE.md's rule_signals description updates its counts. Evicted: the "is a corpus sweep due" measurement in `rule_signals.py` — it lost its trigger when the ceiling was repealed and can never fire; audit-lag supersedes it, so it is deleted in the same build rather than left as a measurement nobody reads. FAQ: not needed — host-only, consumers never author method rules. SPEC: no sentence goes wrong — SPEC does not describe the dev-side rule machinery.

--- Build block ---
Changes: `resources/rule_signals.py` — new firing check, audit-lag: commits touching
  the gate's staged-path set (`plugin/throughliner/docs/`, `resources/self-authoring-
  rules.md`, `resources/rule-maintenance.md`, `resources/method-compliance-audit-
  checklist.md`, `CLAUDE.md`) since the most recent compliance-audit LOG entry file
  one [audit] capture scoped to the changed files, satisfied while one is open; the
  sweep-due measurement is deleted; header counts become five firing checks and one
  measurement. `resources/method-compliance-audit-checklist.md` — criteria restated:
  delta scope, parent-axis only, the four lenses named above with the delete-and-read
  test as the disguised-rationale detector. `CLAUDE.md` — the rule_signals section's
  counts updated (four→five firing, two→one measuring, sweep-due removed); the
  "Rationale lives outside the operative rule" passage gains the history clause,
  typed out from the disposition above.
Acceptance: on a repo whose rule paths have commits after the last compliance-audit
  entry, the check files exactly one capture and stays quiet while it is open; the
  sweep-due measurement is gone from code, output and CLAUDE.md's description; the
  checklist states axis, scope and all four lenses; the history clause reads as a
  subordinate unit of its parent rule.
Refused: any time- or count-based audit trigger — a bare number with no derivation.
Refused: the corpus sweep as the standing shape — delta scope is the routine form;
  the one full pass is the first instance, filed separately.
Refused: notifying or escalating on a standing audit capture — the work sits in the
  queue where ignoring it is visible, per the checks' existing posture.
--- End build block ---

**Skipped again 2026-08-17, and the blocker it waits on now exists as work.** It was presented by the ladder as the longest entry in the section. Rather than skipping it silently a second time, the decision it was actually waiting on was put to you: whether the restyle stops at the one file it covered this morning. **You decided it continues to the rest of the corpus**, so this set still follows a rewrite that has not happened — and audits designed against a corpus about to be rewritten are designed against a shape that will not exist. It follows [law-prose-restyle-heavy-docs] and then [law-prose-restyle-remaining-docs]; the ordering is written into those entries too. [law-prose-restyle] is consumed and no longer names anything in the queue, which is why it is no longer cited above. The second limb still fails by construction, so this stays a capture rather than being held below the line.

#### A rule-holding file sits outside the gate's trigger, so editing it summons no gate at all [gate-trigger-misses-the-audit-checklist]
Filed 2026-08-15 by Claude while writing a gate disposition, and raised with the user before writing.

**What is wrong.** The rule gate's trigger is mechanical and reads staged paths: a commit touching `plugin/throughliner/docs/`, `resources/self-authoring-rules.md`, `resources/rule-maintenance.md`, or `CLAUDE.md`. `resources/method-compliance-audit-checklist.md` is not in that set, and its entire content is rules — the standing criteria every method compliance audit runs against. A session adding a criterion to it authors a rule, and nothing asks it to run the gate.

**How it surfaced.** [audit-axis-is-parent-not-sibling] adds two requirements to that checklist. Its gate ran because the session happened to notice; it would not have fired from the trigger. That is the failure this gate's design is against — a check depending on someone remembering is the shape the mechanical trigger replaced, and `CLAUDE.md` says so when it contrasts this trigger with FAQ-sync's undetectable one.

**To settle at processing, because the obvious fix may be wrong.** Adding the one path is a two-word change and closes this instance. The prior question is whether the trigger set should be a list of paths at all, given that a rule-holding file added later lands outside it again by default and nobody notices — exactly as this one did. A rule about which files hold rules has the same maintenance problem as the rules themselves. Whether there is a shape that fails safe rather than silent is the design question; if not, add the path and say so.

**A second instance, 2026-08-19, and it widens the question rather than repeating it.** A planning session amended a genuine rule — the no-write instruction about Taskflow, which gained an INBOX exception — living in a folder-level `CLAUDE.md` above this project. No gate was summoned, correctly by the trigger and wrongly by the subject. So the trigger misses rules held *outside the repository* as well as rules held in unlisted files inside it, and a path list cannot be extended to cover a file the repository does not contain. See [parent-claude-md-taskflow-no-write-stale].

**Also worth checking in the same pass:** whether any other file under `resources/` holds operative rules and sits outside the trigger. `retired-terms.md` and `rule_signals.py` are the obvious candidates, and both may turn out to be data and code rather than rules.

**Kept 2026-08-22, the prior question answered by the item's own fallback.** No fail-safe shape exists that does not guess at what "holds rules" means, so the path is added and the limit said. The grep found the set stated in exactly three places — CLAUDE.md's gate trigger, CLAUDE.md's close-step rule, `rule_signals.py`'s path constant — and `retired-terms.md` checked clean (zero rule-shaped lines: data, not rules), so the checklist is the only unlisted rule-holder. The out-of-repo instance gets the honest-limit treatment: the trigger reaches files in this repository only, and a rule living elsewhere gets no gate — stated where the trigger is described rather than left to be discovered again. [standing-audit-programme]'s build touches the same constant for audit-lag; the two are consistent (its set already names the checklist) and either build order works.

Rule gate: run — amends the gate's own trigger set, its named parent, as a widening of the existing list plus one honest-limit clause; no freestanding rule, nothing evicted. Failure evidence: two instances on the item, one in-repo and one out. FAQ: not needed — host-only, consumers never author method rules.

--- Build block ---
Changes: `CLAUDE.md` — `resources/method-compliance-audit-checklist.md` added to the
  staged-path set at both sites (the gate trigger and the close-step rule), and the
  trigger sentence gains the limit clause: it reaches files in this repository only,
  so a rule living outside it — a folder-level CLAUDE.md above the project — gets no
  gate, said plainly. `resources/rule_signals.py` — the same path added to the path
  constant (around line 160).
Acceptance: grep finds the checklist path at all three sites; the limit clause reads
  in the trigger's description; a commit touching only the checklist now counts as
  rule-bearing to both the gate and the script.
Refused: a fail-safe trigger shape (detecting rule-holding files by content) — it
  guesses, and a heuristic that misses is worse than a list that states its limit.
--- End build block ---

#### [audit] First compliance audit of the rewritten corpus — restyle audited independently, with the one-time history sweep over everything including SPEC [post-restyle-compliance-audit]
Filed 2026-08-22 at the keep of [standing-audit-programme], as the standing set's first instance. Scope: every rule-corpus change since the last full audit (`LOG/2026-08-10-prohibition-and-subordination-audit.md`), which contains both freeform rewrite passes — so this is the restyle audited by a party other than the restyler, the risk [standing-audit-programme] required designing around. Criteria: `resources/method-compliance-audit-checklist.md` as the build ahead of this updates it — parent-axis only, four lenses. **The disguised-rationale lens runs over the whole corpus including SPEC this once, on your instruction 2026-08-22** — history and other unmarked why-forms, judged by the delete-and-read test — so none get baked in; later delta audits carry the lens at delta scope. An audit edits nothing; findings become captures.

--- Build block ---
Changes: none — an audit edits nothing. Reads the rule-corpus diff since the
  2026-08-10 audit, the updated checklist, and — for the history lens only — the
  whole corpus plus SPEC.md; files findings as captures.
Acceptance: every changed rule file has been read against all four lenses at
  parent-axis; the history lens has covered the full corpus and SPEC; each finding
  names its file, its parent site, and which lens caught it; a clean lens says so
  per file rather than staying silent.
Refused: auditing sibling against sibling — barred by the axis rule.
Refused: fixing findings in place — audit discipline; evictions are later work.
--- End build block ---
Placed immediately after [standing-audit-programme] rather than held below the line: the checklist and check it depends on are dev artifacts, live the moment the build writes them, so one run can build the set and then run this — the tool-then-audit placement rule.

#### The build working file's Changes section falls behind its ticks, and only the ticks are enforced [changes-section-falls-behind-the-ticks]
Filed 2026-08-17 by Claude at its own close, from the reconcile against memory that `done-build.md` requires.

**What happened.** Across a twenty-six-item run, every item was ticked with a depth field and an index-entry candidate at the moment it completed — those three are named at the per-item completion step and all three held. The `Changes:` section did not: it carries per-file notes for roughly the first three items and the end-of-run summary, and almost nothing for the twenty in between. The gap was found by the close's reconcile, not by anything mechanical.

**Why the two behave differently.** The tick, the depth field and the index candidate are enumerated as a numbered set at one step, and the close reads each of them — a missing depth field is explicitly called a discipline slip. `Changes:` is described in `next-build.md` under "accumulate close notes as you go", with no step that reads it back and nothing that notices when it is thin. It is the one part of the working file whose absence costs nothing at the moment it is skipped.

**What it costs.** `done-build.md` sources each entry's `Files touched:` line from this section. With it thin, the close reconstructs the file list from memory of the run — which works in a chat that still remembers, and is exactly what fails in the fresh short session this method designs for. A crash mid-run would have left a working file that understates what was done.

**What to weigh at processing.** Whether `Changes:` joins the per-item completion set as a fourth required write, which is the shape that already works for the other three; or whether the close should read it against the ticks and flag a mismatch, which catches it later but costs nothing during the run. The first is more writes in the run, the second is a check at the one moment the information is already being reconstructed.

**One thing not claimed:** nothing was lost this time. The entries were written from a chat that still held the run, so the record is accurate — this is a defect in what the file would carry for someone else, found because the reconcile asked.

**Kept 2026-08-22, the first fix chosen.** `Changes:` joins the per-item completion set as the fourth required write, because the close-side alternative only detects the gap at the moment a fresh or crashed session can no longer fill it — the design-target session is the one it fails in. The per-item write is the shape the other three already prove, and the close's existing reconcile stays as the backstop that found this. The cost, accepted: one more write per built item during the run.

Rule gate: run — amends next-build.md's per-item completion set, its named parent, from three required writes to four; subordinate to the existing enumeration, nothing evicted. Failure evidence: the twenty-item gap the 2026-08-17 reconcile found. FAQ: not needed — run bookkeeping; nothing a user does changes.

--- Build block ---
Changes: `plugin/throughliner/docs/next-build.md` — the per-item completion step's
  enumerated set (tick, depth field, index-entry candidate) gains a fourth member:
  the item's `Changes:` entry, files touched with one line each, written at the same
  moment as the tick; the separate "accumulate close notes as you go" description is
  repointed at the enumerated set rather than left as a second, unenforced statement.
Acceptance: the completion step enumerates four writes; no other site describes the
  Changes section as accumulate-as-you-go; done-build.md's sourcing of `Files
  touched:` from the section is unchanged and now fed per-item.
Refused: the close-side mismatch check as the fix — detection without repair, in the
  session shape least able to repair.
--- End build block ---

#### Checkpoint question invites a fate answer before the interview — "Worth doing?" reworded to an engagement question [checkpoint-question-invites-a-fate-answer]
**Raised by you 2026-08-22, processed in the same session on your instruction.** Your report: "worth doing" is supposed to mean worth *processing*, not worth building — your yes meant you were open to looking at the item, and it has been slipping for a couple of sessions. The live evidence is this session's own: two items were kept-and-cleared on a "yes" that, by your meaning, only opened them (both offered back for reversal; you let them stand).

**The diagnosis: plan.md contradicts itself.** The fold rule already states that the checkpoint's "continue" answers *which item comes next*, never a disposition of that item — and the checkpoint specimen three paragraphs away ends "**Worth doing?**", a fate question. The fate question's home is the recommend step, after the interview. The fix is alignment, not new design. Grep found one specimen site plus its describing line; no template, FAQ or SPEC site carries the phrase.

Rule gate: run — amends the checkpoint's message-order block to agree with the existing continue-is-not-a-disposition rule, its named parent; evicts the "is it worth doing" phrasing from the block and the specimen. Failure evidence: your report, the multi-session slippage, and this session's two premature folds. FAQ: not needed — the user answers the same routing choice, better worded.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — the checkpoint message-order block's
  question line becomes: one bold question inviting the user into that item ("Take
  this one next?"), never a fate question, which waits for the recommend step after
  the interview; the specimen's "**Worth doing?**" becomes "**Take this one next?**".
Acceptance: grep finds no "Worth doing" in plan.md; the block and the fold rule no
  longer disagree; the specimen shows the new question.
Refused: adding a separate "ready to dig in?" turn — plan.md already bars it; the
  checkpoint question IS that invitation, which is why its wording carries the load.
--- End build block ---

#### The dispositions listing was run at a planning opening and never surfaced to the user [dispositions-listing-run-not-surfaced]
Filed 2026-08-19 by Claude at its own close, as a testing outcome from using the plugin to build the plugin.

**What happened.** `CLAUDE.md` requires the rule-gate dispositions listing to be surfaced at a /plan opening, alongside the digest and the held work. The session ran `rule_signals.py --dispositions`, read its output, and then folded nothing from it into the opening narration. The user never saw it.

**Why the omission matters more than the content did.** The listing exists because a refused rule proposal leaves one sentence inside one entry and nothing scannable — the user's own recorded question is *"how would I even know to demand it?"*. A listing that is run and not reported reproduces exactly the condition it was built to remove, and does so invisibly, since running it leaves no trace either.

**This is the siteless-check failure with a site.** The obligation has a stated moment and was still skipped, which is the harder case: the corpus already records four instances of a correctly worded rule failing to fire, and this is a fifth in a rule whose whole subject is making things visible.

**To settle at processing.** Whether the fix is wording, placement, or a required artifact — the last being the shape that has proven teeth here, as FAQ-sync and the gate line both show. Weigh against the cost: a line at every planning opening saying "nothing refused since the last planning session" is noise on most sessions, which is the objection that kept this a prose obligation in the first place. Relates to [gate-trigger-misses-the-audit-checklist] and to [standing-audit-programme]'s record of correctly worded rules that do not fire.

**Kept 2026-08-22, merged with [dispositions-listing-window-not-bounded] — two accounts of one broken surface, and the merge is what came out shorter.** That capture's observation, carried in: the listing printed "176 on record (since the last planning session)" at two consecutive openings against a stated bound of one session's window; deliberately undiagnosed — the header may be mislabelled, the window computed wrongly, or the planning-entry finder broken by the per-entry LOG split — **read the code before fixing; the acceptance is behavioural, not a guessed cause.** The settled design, three parts: the window bound is fixed so the listing genuinely covers only since the most recent planning session; the opening narration carries one short line **only where that window holds a refusal** — refusals being the thing the user cannot otherwise know to demand — and silence otherwise, the same quiet-when-fine shape as the output-style check; and the required artifact with teeth sits in the planning close's LOG entry — one line, refusals surfaced or none since last session — so a skipped surfacing is visible afterwards instead of indistinguishable from a quiet one.

Rule gate: run — amends CLAUDE.md's surface-the-listing-at-a-/plan-opening rule, its named parent: the always-surface instruction is narrowed to refusals-only-with-silence-otherwise (that narrowing is the eviction), and the close-entry line is added as a subordinate required-artifact clause in the FAQ-sync shape. Failure evidence: the 2026-08-19 non-surfacing instance plus the unusable 176-entry listing at two openings. FAQ: not needed — host-only, the listing does not ship. SPEC: no sentence goes wrong — SPEC does not describe the dev-side listing.

--- Build block ---
Changes: `resources/rule_signals.py` — the `--dispositions` window fixed to entries
  since the most recent planning LOG entry, cause established by reading the code
  (the planning-entry finder under the per-entry split is the suspect, not the
  conclusion); `--dispositions-all` unchanged. `CLAUDE.md` — the dispositions-listing
  passage amended: the /plan opening carries one short line only where the window
  holds a refused proposal, silence otherwise; a planning close's LOG entry carries
  one required line — refusals surfaced, or none since last session; the listing's
  description updated to match.
Acceptance: the listing's header count equals the entries since the last planning
  LOG entry (spot-check against the index: far fewer than 176); a window holding a
  refusal produces the opening line and an empty one produces nothing; the close-line
  requirement reads in CLAUDE.md beside the existing close obligations.
Refused: surfacing the full listing at every opening — the recorded noise objection.
Refused: a notification mechanism — already refused in the record; mail is
  fire-and-forget and a notice moves the problem.
--- End build block ---

#### The scaffolded "Project docs" section in every consumer SPEC describes the method's own machinery, and goes stale in a way no migration repairs [spec-scaffold-describes-method-docs]
Filed 2026-08-15 by Claude, from INBOX mail sent by a consumer project running this method running 1.20.0-test7. Their user noticed it unprompted while reading her own SPEC and asked why SPEC described the workflow's files rather than her product; they filed it without proposing a fix and said no reply was needed.

**The admission point.** `setup.md`'s SPEC scaffold writes a `## Project docs` section into every new SPEC.md, listing what SPEC, QUEUE and LOG each hold. plan.md's SPEC admission rule says a sentence describing how a mechanism is implemented belongs in the doc that owns it, and that SPEC names the behaviour instead. So the scaffold writes into every consumer's SPEC exactly the kind of sentence the rule governing SPEC edits forbids. Whether that section earns its place is the question; the sender proposed no answer.

**The staleness point, which the sender judged sharper and which is invisible from here.** That section copies how QUEUE.md is structured, and QUEUE.md's structure is what changes between format epochs. Theirs read "work batches and captured ideas" — the pre-recut shape — and had since the two-section change. They ran the format 2→3 migration and it correctly did not touch the line, because migration adds missing files rather than refreshing existing content. So the stale description survives every migration by design, in every consumer project, in the one document sessions are told to read as product truth. Theirs is now corrected by hand.

**Why it needs planning rather than an obvious patch.** Three candidate answers, not equivalent: drop the section from the scaffold; keep it but reduce it to behaviour rather than structure; or give the migration a refresh path for scaffolded content, which is a new capability rather than a wording fix. The first two are cheap and the third is not.

**A related check when this is processed:** whether anything else the scaffold writes has the same shape — content copied from the method into a consumer document, where the method can change and the copy cannot be reached.

**Kept 2026-08-22, the first candidate chosen, and what shipped since filing is what settled it.** [managed-claude-md-block-never-refreshed] built the refresh capability — but for CLAUDE.md's plugin-managed block, method-owned and marked; that is the right home for what the three docs hold, while SPEC can never get a managed region, because method-owned text inside the user's product-truth document is what this item exists to remove. The section also fails SPEC's own admission rule. So: the scaffold stops writing it; the template's managed block is verified to carry the description (confirmed by the build, not assumed); existing projects learn through the migration's report-only retired-terms step, which gains one detection and still edits nothing; and the scaffold sweep for the same shape rides the build, findings filed as captures.

Rule gate: run — amends setup.md's SPEC scaffold and the migration's retired-terms report step, their named parents; the eviction is the scaffolded "Project docs" section itself; no always-loaded rule touched. Failure evidence: the consumer's reported stale section, surviving migration by design. FAQ: not needed — the migration report moment already exists; nothing a user does changes. SPEC (ours): no sentence goes wrong.

--- Build block ---
Changes: `plugin/throughliner/docs/setup.md` — the SPEC scaffold's "Project docs"
  section removed; the migration's retired-terms detection gains one entry: a
  "Project docs" section in a consumer SPEC is reported as method-machinery
  description, naming the managed CLAUDE.md block as where it now lives, edited
  never. `plugin/throughliner/templates/CLAUDE-TEMPLATE.md` — verified (and if
  absent, added) that the managed block describes what SPEC, QUEUE and LOG hold.
  Sweep the rest of the scaffold for method content copied into consumer docs;
  findings filed as captures, not fixed in this build.
Acceptance: a fresh /setup writes a SPEC with no "Project docs" section; the
  migration report names the section when present in an existing SPEC; the managed
  block carries the three-doc description; the sweep's findings (or a clean result)
  are in the session record.
Refused: a managed region inside SPEC — method-owned text in the user's product
  truth, the defect itself.
Refused: reducing the section to behaviour — still method description in the wrong
  document, and still unreachable by any refresh.
--- End build block ---

#### A build read queue items through a grep window shorter than the items, and reasoned from the truncated read twice [build-reads-item-through-a-truncated-window]

The 2026-08-21 run had to transcribe each built item's `Rule gate:` disposition, which
the build view does not carry (see [build-view-strips-the-gate-disposition]). It went
to QUEUE.md for them and read each item through a `sed`/`grep` window of about 36
lines. All three items run past 50. Both the labelled `Rule gate:` line and the
item's FAQ disposition sit below where the window stopped.

**Two wrong outputs came out of that one read, and neither announced itself.**

First, a capture was filed asserting that [advisory-step-does-not-fire] carried its
gate reasoning as unlabelled prose with no `Rule gate:` line. The item carries a
properly labelled line. That capture was deleted at the close on the same day it was
filed.

Second — and this is the one that reached the user — the close concluded the FAQ gate
fired on that item, put the question to her, and got approval to add four FAQ files
and write an entry. The item had already dispositioned it: *"**No FAQ entry**, on the
FAQ trigger's own test: a consumer sees one more line in their session record and does
nothing different."* Planning had considered the identical question and answered it
the other way. The entry was written, then reverted on her instruction once the
recorded decision was found.

**The rule that would have caught it is already shipped and was not followed.**
`skill-nonspecific-rules.md`: page the whole file before any queue-wide reasoning, and
name a read that stopped short rather than reasoning from it quietly — with the reason
stated in the rule itself, that a truncated read looks like a complete one to whatever
reasons over it. That is exactly what happened, and it is why nothing downstream
flagged either error.

**So this is a rule-does-not-fire instance, not a missing rule**, and it joins the
class this corpus already tracks — the provenance rule, the file-the-blocker rule, the
INBOX-opening step, the subagent-cost rule, the gate's own halt instruction, and the
advisory step this very run was built to fix. The corpus's recorded conclusion about
that class applies: stating the rule again, or harder, is not a candidate direction.

**What is arguably new here is the shape of the trigger.** The paging rule reads as
being about *whole-file* reasoning — the queue digest, a queue-wide reorder — and a
build fetching one item's disposition does not feel like queue-wide reasoning. It is
still reasoning over a unit read short. Whether that is a wording gap in the rule or
simply an instance of it is the question for the keep-step.

**Two candidate directions, neither designed:** the build view could carry the gate
disposition and the FAQ disposition, which removes the need to read QUEUE.md at all
and is what [build-view-strips-the-gate-disposition] already proposes for half of it;
or the close's fetch could be specified as read-the-whole-item-block, keyed on the
`####` heading and the next one, rather than left to a hand-written window.

**A third thing this exposes, worth stating separately: a close overrode a recorded
disposition and the user could not have known.** She was asked a well-formed question
and answered it. Nothing in the ask told her a decision already existed, because the
session asking had not read it. Whatever else changes, an ask that re-opens a
dispositioned question should say that it is doing so.

Filed at the close of 2026-08-21; commit at filing time is the tip of main at
`461c999`.

**Kept 2026-08-22.** Half shipped the day it was filed — [build-view-strips-the-gate-disposition] puts gate and FAQ dispositions into the view, removing the errand that produced the windows in their most common case. What this build does is the general half: the close's per-item lookup specified as a whole-block read, and the re-opening clause. The paging-rule wording question is answered no — one item's block is already a unit the rule covers; this was the rule not firing, joining the recorded class, and the fix makes the fetch mechanical so the rule stops being load-bearing there.

Rule gate: run — two amendments to existing done-build.md provisions: the record-writing step's fetch gains the whole-block form, and the prior-decisions rule gains its close-site clause (an ask that re-opens a dispositioned question names the recorded decision). Subordinate on both counts, nothing evicted. Failure evidence: two wrong outputs from one windowed read, one reaching the user. FAQ: not needed — close mechanics; nothing a user does changes.

--- Build block ---
Changes: `plugin/throughliner/docs/done-build.md` — the per-item record-writing
  step specifies the fetch: read the built item's whole block, from its `####`
  heading to the next heading (or section end), from the pre-run QUEUE.md in git;
  a hand-sized grep or line window is named as the form that produced two wrong
  outputs and is not used. Same step gains one clause: where the close is about to
  put a question to the user that the fetched item's own text already dispositions,
  transcribe the disposition instead — and an ask that deliberately re-opens one
  names the recorded decision it re-opens.
Acceptance: the fetch instruction names the heading-to-heading form; the re-opening
  clause reads beside the step that asks; no other close doc contradicts either.
Refused: widening the always-loaded paging rule's wording — the rule already covers
  any unit the reasoning depends on; restating it harder is the direction the record
  rules out.
--- End build block ---

#### You cannot name the parts of the method you want changed, so you cannot ask for changes to them [user-has-no-handle-on-the-methods-own-parts]

**Raised by you 2026-08-21, in your own words:** *"I have also lost control because I
don't know what the place were we explain this is called. I have some vague idea it's
in skill-nonspecific-behaviours but I wouldn't have a clude how to refer to it and
actually ask for improvements on it that yield better outcomes."*

**The near-miss is the evidence.** The file is `skill-nonspecific-rules.md` and the
section is "The work cycle". You were close enough to be clearly reaching for the right
thing and not close enough to name it — and naming it is what a request has to survive
in order to reach the right place.

**This is the cost side of a rule that is otherwise working.** The vocabulary rule
keeps internal terms out of what Claude says to you: procedure-doc filenames, step
numbers, tag names are translated or omitted. That is right for a consumer building an
app, who never needs them. It has a different effect here, where the method **is** the
product: the parts you most need to direct are the ones you are never told the names
of. This project is the unusual case the audience note in CLAUDE.md already describes,
and this is a consequence of it that nobody had written down.

**Two directions, and they are not exclusive.**

The first is Claude's side and costs you nothing: **a request that describes a behaviour
should be enough**, and Claude should locate the file. *"When you hand me a prompt to
paste, never put a command inside it"* is complete and actionable as it stands. Needing
a filename to make a request land is itself the defect. Whether anything needs writing
for that, or whether it already follows from rules in place, wants checking rather than
assuming.

The second is a **map you can hold** — one short list naming the parts and what each
governs, in your language rather than the corpus's: the always-loaded rules and what
kinds of behaviour live there, the one doc per command, this project's own CLAUDE.md,
SPEC. Where it lives is an open question. This project's CLAUDE.md is the obvious home
and is also already long; the FAQ is consumer-facing and this is not a consumer's
problem.

**Not designed, and deliberately so.** The right shape depends on which of the two
actually restores the control you lost, and that is your judgment rather than Claude's.

**One thing worth not losing:** you said you had lost control, not that you were
confused. Those are different complaints and the second is easier to answer than the
first. A fix that leaves you able to follow what Claude is doing but still unable to
direct it has answered the wrong one.

Filed 2026-08-21 from a chat outside any skill; commit at filing time is `ae84933`.

**Kept 2026-08-22, both directions, shaped by your answer to the one design question.** Asked where you actually look things up, you said: asking Claude in chat. So the map is a file — `resources/method-map.md` — because the session you ask is a fresh one, and a file is what makes its answer consistent instead of improvised; the trigger is you asking, the surface you already use, so it is never siteless for you. Direction 1 is confirmed working (this session's checkpoint fix landed from a pure behaviour description) and gains its clause: a request describing a behaviour is complete, and the answer names the part it found in passing — so each request teaches you one name as a side effect. Control, not comprehension, is the target: the map lists what you can direct, in your language.

Rule gate: run — one clause admitted on this CLAUDE.md's Audience section, its named parent (this project being the method-is-the-product case is what creates the problem); subordinate, host-only, a slot spent and said so; nothing evicted. Failure evidence: your recorded near-miss ("skill-nonspecific-behaviours"), and the shipped name-the-parts rule reaching only sessions where you already know what to ask about. FAQ: not needed — host-only; consumers get the shipped vocabulary rule. SPEC: no sentence changes.

--- Build block ---
Changes: `resources/method-map.md` (new) — one short list, in plain language, of the
  parts you can direct: the always-loaded rules and what kinds of behaviour live
  there, the one procedure doc per command, this project's CLAUDE.md, SPEC, the
  hooks — each with what it governs and one example request that would reach it.
  `CLAUDE.md` — the Audience section gains one clause: a request describing a
  behaviour is complete with no filename; locate the part, name it in the answer;
  when the user asks about the method's parts or where something is decided, read
  `resources/method-map.md` and answer from it.
Acceptance: the map exists, fits on one screen, and names every part with an example
  request; the clause reads in the Audience section; a fresh session asked "what are
  the parts of the method" would reach the map by the clause.
Refused: the map inside CLAUDE.md — always-loaded length for a fetch-on-ask artifact.
Refused: the map in the FAQ — consumer-facing surface for a host-only problem.
--- End build block ---

#### The rationale lens covered done.md whole and plan.md only in part, so plan.md's acceptance test is unmet [rationale-lens-plan-md-coverage-incomplete]

[rationale-lens-after-the-build-view] required every paragraph of `done.md` and
`plan.md` to go through the delete-and-reread test, with each removal recorded
against its destination. The build on 2026-08-21 met that for `done.md` and did
not meet it for `plan.md`.

**What was actually done.** `done.md` was read end to end across four reads and
worked section by section, so every paragraph was seen and judged: 959 lines
down to 794, statement count 244 to 235. `plan.md` is 1,594 lines, and the pass
there worked from targeted identification — grepping for the signatures of
history paragraphs ("Why both", "recorded because", "was rejected", "used to",
"weighed and lost") and reading around each hit. Roughly 40% of the file was
read. Eight sites were reduced; 1,594 lines down to 1,549, statement count 318 to
322.

**Why the count ROSE while the file shrank**, recorded because it looks wrong: a
paragraph carrying an operative rule buried in prose was, in several places,
restated as a bold-led sentence. That is what the pass is supposed to do — an
operative rule belongs in a countable shape — but it means the statement count is
not a proxy for how much history came out. Line count is the better signal here.

**What is left.** The unread ~60% of `plan.md`, which is not a list anyone holds:
the identification was signature-based, so a rationale paragraph phrased without
one of those openings was never looked at. That is the same class of miss as
[law-prose-pass-missed-mid-sentence-prohibitions], found the same day, by the
same shortcut.

**What a build would need to settle.** Whether the remaining pass reads the file
straight through — the only method that can honestly claim the acceptance test —
or whether the acceptance test itself should be restated as something a build can
actually discharge and evidence. The second is worth weighing: "every paragraph
has been through the test" is unfalsifiable from the artifacts, since a paragraph
correctly judged operative and left alone looks identical to one never read.
That is the same defect the required-artifact rules elsewhere in this project
exist to fix, and it is arguably the more valuable half of this item.

**Kept 2026-08-22, both halves settled.** The gap is confirmed still open — yesterday's freeform passes covered the thirteen remaining docs, which exclude plan.md. And the acceptance test is restated in the dischargeable form the item asked for: a **coverage ledger** — the build reads plan.md straight through and the session record lists every section heading with its outcome, removals named or "judged operative, kept clean". A missing section is then a visible gap, since headings are grep-enumerable; a silent skip stops being indistinguishable from a clean judgment. No general rule is authored — the ledger rides this item, and the wider unspecified-artifact family stays grouped for [rezip-supplies-no-verification-prompt]'s processing, as its filing intended.

Rule gate: run — a transcribed continuation of the rationale lens already admitted at [rationale-lens-after-the-build-view]; rationale paragraphs removed to the record, no new rule, nothing evicted beyond what the lens itself removes. FAQ: not needed — Claude-facing rule text behind unchanged behaviour. SPEC: no sentence changes.

--- Build block ---
Changes: `plugin/throughliner/docs/plan.md` — the rationale lens applied over the
  whole file in one straight-through read, every paragraph through the
  delete-and-reread test, removals relocated to the session record with their
  destinations named — the same method the done.md pass used.
Acceptance: the session record carries the coverage ledger — every `##`/`###`
  heading in plan.md listed with removals or "judged operative, kept clean" — and
  the heading list matches a grep of the file; line and statement counts reported
  before and after.
Refused: another signature-based pass — it is the shortcut that produced this gap
  and [law-prose-pass-missed-mid-sentence-prohibitions] alike.
Refused: leaving the acceptance test as "every paragraph has been through the
  test" — unfalsifiable from the artifacts, per the item's own analysis.
--- End build block ---

#### The rezip ritual names a verification but supplies no words for it, so Claude re-invents the prompt every time and got it wrong today [rezip-supplies-no-verification-prompt]

**Raised by you 2026-08-21**, immediately after a rezip: you are tired of having to get
Claude to redesign this prompt on every rezip, and want it supplied ready-made.

**The gap.** `resources/release-ritual.md` step 9 says to prove the hooks are alive by
asking a fresh session what the session-start hook actually reported to it, and explains
correctly why that step exists — a hook that is well-formed, installed and silently
dropped looks exactly like a working one from the source side, so only a session saying
what it received distinguishes them. **It supplies no prompt.** So the words are composed
fresh at every rezip, at the end of a long ritual, by whichever session is running.

**The failure is today's instance, observed end to end.** Claude told you to check what
the next session's opening line said. You relayed it as *"please tell me what its
session-start line says"*. The fresh session replied that it was not sure what "its"
pointed at — correctly, because it has no memory of the chat the instruction came from.
The verification did not happen, and the only reason it was not simply skipped is that
you came back and said so.

**Why the fresh-composition is the defect rather than that one wording.** This prompt has
an unusual authoring constraint: it is pasted into a session with **zero context**, so
every referring word has to resolve inside the prompt itself. A prompt composed by a
session that has been immersed in the work for hours is exactly the wrong author for that
— pronouns that are obvious here resolve to nothing there. The method already knows this
failure shape: it is the same reason `done.md` fixes the compaction caveat as a verbatim
sentence rather than an instruction to explain the limit honestly, and records that
inviting improvement is what went wrong.

**What a build would supply**, sketched from the version that worked today rather than
designed from scratch. A verbatim fenced block at step 9, plus two things around it:

- **Where to paste it** — any project in the state that reproduces the bug: **version
  marker stale, epoch current, nothing missing.** Name the state rather than a project.
  Claude's first attempt at this said "a project that was actually exhibiting the
  symptom, not this one", which was wrong twice over: it sent the user hunting for the
  right project when the dev project was already in the reproducing state, and a project
  picked that way may halt for a *legitimate* stale-epoch reason, which muddies the
  result rather than confirming anything.
- **How to read the answer** — which reply means the fix landed, which means a real and
  correct halt, and which means the app did not fully restart. Without that the report
  comes back and still needs interpreting.

The four questions the working version asked: quote the `[Throughliner]` block verbatim;
does it mention `/setup` and for which of the three reasons; does it tell you to stop or
close what is running; what version and build stamp does it report. Plus one instruction
that carries most of the value — **if the block did not arrive at all, say so plainly
rather than reconstructing it from the project's files**, which is the one answer that
distinguishes a delivered hook from a dropped one and is exactly what step 9 exists for.

**Host-only, and it goes in `resources/release-ritual.md`.** Consumers never rezip, so
this reaches no shipped doc.

**One thing to settle at processing.** Whether the block is fixed text that must be pasted
as written — the `done.md` compaction-caveat precedent, which exists because improving it
is what broke it — or a template a session may adapt per rezip. The failure recorded above
is an argument for the first, and the first is also cheaper.

**The prompt was then run and it worked, so a build starts from something proven rather
than from a sketch.** The reply came back as a straight paste of the whole
`[Throughliner]` block, and that single instruction — quote it verbatim — answered all
four questions on its own without the reader working through them one by one. So the
verbatim quote is the load-bearing part and the four questions are the fallback for a
session that paraphrases instead. **Design the block that way round.**

**What the run confirmed, recorded because it is also the worked example a build can put
in the ritual.** The dev project recorded `1.20.0-test13` against an installed
`1.20.0-test14`, with epoch 4 against a declared 4 and nothing missing — exactly the
state that produced the halt reported that morning. A fresh session opened in that state
and its block mentioned `/setup` nowhere. That is what a passing result looks like, and
it is worth showing rather than describing.

**One piece of expected noise the ritual should warn about**, or the next reader files it
as a finding: the returned block carries the INBOX line flagging `INBOX/sent.md`, which
is the outbound register rather than waiting mail. Already known as
`[sent-record-surfaced-as-waiting-mail]`. A verification step that returns a block
containing a known false positive needs to say so, or it manufactures work.

**Relates to** `[close-cost-scales-with-run-size]`,
`[law-prose-pass-missed-mid-sentence-prohibitions]` and
`[rationale-lens-plan-md-coverage-incomplete]`, all filed the same day. All four are the
same family: **a step that names a check and leaves its artifact unspecified**, so
whether it was really performed cannot be told afterwards. That family is worth processing
together rather than four separate repairs.

**Kept 2026-08-22, fixed text chosen, and [rezip-liveness-same-chat] merged in — two changes to the same ritual step, settled as one rewrite.** Fixed over template on the item's own evidence: the failure is fresh composition, and the compaction-caveat precedent exists because inviting improvement is what broke it. The merged-in half is your -test15 observation: the restarted app re-fires the session-start payload into the chat that ran the rezip, so the step's primary proof becomes that re-fired payload read in place, with the fixed fresh-session prompt kept as the fallback — one observed instance, so the fallback stays rather than being deleted. The merged capture is deleted; its content is this paragraph.

Rule gate: not needed — a host ritual doc outside the rule corpus gains a verbatim block; no method rule is authored or amended. FAQ: not needed — host-only; consumers never rezip. SPEC: no sentence changes.

--- Build block ---
Changes: `resources/release-ritual.md` — the liveness step rewritten whole: (1) the
  primary proof is the re-fired `[Throughliner]` session-start payload arriving in
  the rezip chat itself after the full restart — read it there, no fresh chat; (2)
  where none re-fires, the fallback is a fixed, verbatim fenced prompt block pasted
  into a fresh session in a project whose state reproduces the check — version
  marker stale, epoch current, nothing missing — leading with "quote the
  [Throughliner] block verbatim; if it did not arrive, say so plainly rather than
  reconstructing it", with the four questions as fallback for a paraphrasing
  session; (3) a how-to-read-the-answer guide — which reply means the fix landed,
  which a real halt, which an incomplete restart; (4) the warning that the returned
  block carries the sent.md waiting-mail false positive, already known, so it is
  not filed as a finding; (5) the worked -test13/-test14 example as the shown pass.
Acceptance: the step carries the fenced block as fixed text with no
  adapt-per-rezip licence; the same-chat payload is stated as the primary proof
  and the prompt as fallback; the interpretation guide and false-positive warning
  read beside it.
Refused: a template a session may adapt — fresh composition is the recorded
  failure, and fixed is also cheaper.
Refused: deleting the fresh-chat fallback — one observed instance of the same-chat
  payload is not enough to retire the path that always works.
--- End build block ---

#### Heading word-order rule did not fire on a fresh capture, and the user could not find it in her outline [heading-rule-did-not-fire-on-a-fresh-capture]

Filed 2026-08-21 by Claude at its own close, from an instance minutes earlier.

A capture was filed with the heading "The brevity work went to narration…" into
an outline where eleven consecutive headings already began with "The". The user
scrolled the outline, could not find it, and had to ask for it by name. The
shipped rule — put a heading's distinguishing words first, because the outline
truncates mid-phrase — is always-loaded, was in context, and did not fire; the
heading was corrected only after the user reported the failure.

Joins the class this corpus records as correctly-worded rules with a stated site
not firing (ninth instance). Per that record, stating it harder is not a
candidate direction. What may be mechanical here where the others are not: a
heading's first word is text a lint can read, and "starts with The/A/An" is
checkable at zero judgment — though that catches only the article case, not a
generically front-loaded heading, and the limit would need stating wherever it
reports.

**Files (rough):** `plugin/throughliner/hooks/post_tool_use.py` and
`resources/testing/` if the lint arm is taken; nothing if judged below the bar —
one instance, which the gate treats as insufficient for a rule, though this
would be a lint check rather than a rule.

**Kept 2026-08-22, the lint arm taken.** The one-instance bar guards rules, which cost attention every session; a lint check is mechanical and free, and the gate's own fourth question exists to escalate a repeating slip to a hook — the record's ninth instance of this class having already ruled out sharper wording. Two facts make it clean: an article at heading start is always wrong under the word-order rule, so there is no legitimate case to false-positive on; and the lint already separates pre-existing flags from newly introduced ones, so existing headings stay quiet and only a fresh capture is flagged, at the moment it is cheapest to fix.

Rule gate: not needed — hook code gains an advisory check; no method rule is authored or amended, and the always-loaded heading rule stands unchanged. FAQ: not needed — the lint's advisory moment already exists; this is one more check inside it. SPEC: no sentence goes wrong — the lint is already described as structure lint.

--- Build block ---
Changes: `plugin/throughliner/hooks/post_tool_use.py` — the queue lint gains one
  advisory check: a `#### ` heading whose first word is The, A or An is flagged,
  with the message naming the word-order rule and stating the limit — the article
  case only, not a generically front-loaded heading. Fires only on headings the
  change introduced, per the lint's existing new-versus-pre-existing split.
  `resources/testing/` — assertions: article heading flagged, non-article heading
  passed, pre-existing article heading not re-flagged.
Acceptance: suites pass; a fresh capture headed "The …" draws the advisory flag
  with the stated limit; existing headings draw nothing new.
Refused: restating the heading rule harder — the recorded dead direction.
Refused: detecting generic front-loading — needs judgment a lint cannot have; the
  stated-limit line is the honest form.
--- End build block ---

#### A slug built earlier in the same run is in neither the queue nor the log, so the filing-claim hook can still fire on it [stop-hook-blind-between-tick-and-close]

Filed 2026-08-21 by Claude, noticed while building [stop-hook-fires-on-cited-slugs] and testing the fix against this project's own state.

**The gap.** That item's fix suppresses the block where a slug absent from QUEUE.md has a session record in `LOG/`, on the reasoning that a record means the slug names shipped work rather than a failed filing. It closes the case it was filed for — citing work built in an earlier session.

**What it does not reach is the same run's own work.** A build removes each item from QUEUE.md at the moment it is ticked, and its LOG entry is not written until the close. Between those two events the slug is in neither file, so a message citing an item this run has just built looks exactly like a report of a write that never happened. Confirmed live: at the moment of writing, [cut-length-everywhere] had been ticked and removed and had no LOG entry, so a citation of it would still have blocked.

**Why it is not urgent.** The block downgrades after one fire per claim, so it cannot trap a chat, and the run's own narration names built items constantly without the hook seeing most of them. It is a false block in the one window where the session is most confident it is right.

**What would close it, undesigned.** The build working file already carries a Progress tick per built item, and it is per-session and readable from the hook's cwd. Reading ticked slugs out of it would cover the window exactly. Whether a hook should read that file at all is the open question — nothing else does, and it is deleted at the close.

Relates to [stop-hook-fires-on-cited-slugs], whose fix this extends, and to [changes-section-falls-behind-the-ticks], which is about the same file's reliability.

**Kept 2026-08-22, the open question dissolved by the record.** "Nothing else reads that file" is false: `pre_tool_use.py` already reads this session's build working file — the scope-lock's file list comes from it, and plan-versus-build is decided from its absence — so the stop hook reading ticked slugs from the same per-session file is precedented, cheap and correctly scoped, and the window closes itself when the close deletes the file. Kept despite the item's own not-urgent note because the false block fires exactly when the session is most confidently right, which is how a guard teaches sessions to distrust it. SPEC's stop-hook sentence, incomplete since the LOG suppression shipped, was amended at this keep to cover both suppressions.

Rule gate: not needed — a hook fix plus its tests; no method rule changes. FAQ: not needed — hook behaviour a user never steers.

--- Build block ---
Changes: the stop hook under `plugin/throughliner/hooks/` — the filing-claim check
  gains one suppression source: slugs ticked in this session's build working file
  are treated as finished work being cited, alongside the existing LOG-record
  suppression; a missing or unparseable working file changes nothing. `resources/
  testing/` — assertions: ticked-slug citation passes, unticked absent slug still
  blocks, no working file behaves as today.
Acceptance: suites pass; a citation of an item ticked this run draws no block in
  the tick-to-close window; the existing once-per-claim downgrade is untouched.
Refused: leaving it on the not-urgent ground — a guard that false-fires at the
  moment of highest confidence erodes trust in every real fire.
--- End build block ---

#### [user] Write the article comparing Throughliner to memory-system approaches, finishing with what shipped [competition-comparison-article]
**Captured by you 2026-08-15**, from a discussion prompted by Discord talk about "Obsidian memory systems" and "dreaming". **Your framing and your decision: the analysis reads as an article starter for the Throughliner site, and rather than sending it now it should be captured and finished with our shipped solutions, with the announcement doubling as a Discord post.**

**This is your own shipped-only rule applied correctly, and you reached it independently.** `CLAUDE.md` says a post announces only what has shipped, and that where a post describes work designed but not built, it waits for the build and is filed as a queue item naming what it waits on. That is exactly this.

**Your stance on the article's framing, recorded 2026-08-17 and NOT generalised into a rule.** Claude proposed turning it into a standing rule about all writing describing Throughliner, and you refused: it *truly depends what we are writing, and the tone required*. Claude had also flattened the position itself — writing "no stake in persuading anyone that one approach beats another" where **your actual position is that you have a stake, just not in being seen as the best thing since sliced bread.**

**Your assessment of the draft, which is the live problem with this item.** It swung from hard marketing to substantially explaining why the competition is better. You sent it to the other project for polishing rather than continuing here, because you wanted to move on — so the draft is out of this project's hands and the item covers what comes back.

**The queue-read weakness is NOT answered, corrected 2026-08-19, and this must be right before the article goes out.** It once read that the article's weak points — manual curation and a 56,000-token queue read — were answered by [digest-reports-computed-fields-not-summaries]. That became false on 2026-08-17, when the digest was expressly stopped from replacing the read: a planning session now runs the digest **and** reads the whole file, because the digest computes facts and the file carries the reasoning. So the full read is still paid, deliberately.

**What actually addresses it is unbuilt.** [split-the-cleared-region-for-concurrent-sessions] gives a build a derived view and stops it reading the queue at all. **Under the shipped-only rule the article cannot claim that until it ships**, and the honest line if it goes out sooner is that planning still reads everything and the reason is that reasoning across items is what planning is for.

**Read this paragraph before drafting.** A `[user]` item sitting cleared to run, producing public text, is exactly how [discord-post-context-adjacency] was nearly posted about a mechanism that no longer existed.

**The substance, drafted in discussion and to be rewritten rather than pasted.** *Stronger:* typed documents with defined roles versus an undifferentiated note graph, so product truth, pending work and history each have a home; memory coupled to execution, since /next builds from the queue rather than merely reading it; the throughline carrying *why* rather than only what; deletion as a user-approved fate decision rather than an automatic prune; and everything as plain markdown in git, reversible and auditable. *Weaker:* curation is manual, which is dreaming's entire job — sixty unprocessed items with duplicates accumulated over weeks, seven merges by hand, six items found behind already-shipped blockers; scale, where graph retrieval never needs to read everything; and one-way links, where backlinks are derived for free.

**The verification step runs BEFORE drafting, and is not optional.** `resources/research/auto-memory-staleness.md` is dated 2026-06-09 and names AutoDream as Anthropic's own consolidation sub-agent — two months old, and what the Discord means by "Obsidian memory systems" may be a specific community project rather than the general vault-as-memory pattern. **Publishing a wrong description of someone else's system under your name is worse than publishing nothing**, and unlike everything else this project writes, it is a claim about a third party. Search first, update the research file, then draft.

**Two artifacts, not one text, settled at capture.** The article is the full piece and may be long, may discuss competitors, and may say where Throughliner is weaker. The Discord post is capped at 2,000 characters, takes the shipped fix as its subject with the comparison only as framing, and points at the article. One text serving both would either saddle the announcement with a comparison it doesn't need or truncate the article into a changelog.

**The Discord post is this item's final step rather than a separate item — the user's decision.** Order: verify, draft the article, ship the digest work, finish the article with what actually shipped, then write the post. **Nothing is published without the user seeing the exact text and giving an explicit yes**, and Claude has no route to Discord or to the site — the user posts both.

**One thing to resolve at drafting.** The site is another project, so the article is drafted here and delivered rather than written into that repository. Whether that delivery is an INBOX message or the user carrying it across is a question for the moment it is ready.

**The blocker has shipped and the `Blocked by:` line is dropped, 2026-08-15.** [digest-reports-computed-fields-not-summaries] has a LOG entry, so the digest work the article was waiting to describe now exists.

**Verification done 2026-08-15, in the /plan session that processed this — and it changed the argument rather than confirming it.** `resources/research/auto-memory-staleness.md` was re-checked and partly corrected; its index line carries the correction too. Two material findings:

- **AutoDream is live.** It consolidates memory between sessions — merging facts, deleting contradicted notes, converting relative dates to absolute, trimming the index — triggering automatically after roughly 24 hours plus five sessions, and **a manual `/dream` command is available to everyone** regardless of rollout state. The research file's claim that it is not running was two months stale. **This sharpens the weakness the draft already admits:** automatic curation is no longer something only competitors have, it is in the base tool this plugin runs on. An article treating manual curation as a fair trade must say so, and the honest framing is why typed documents and user-approved deletion are worth the manual cost — not that the alternative is unavailable.
- **"Obsidian memory systems" is a category, not a project.** Several independent implementations exist, some with semantic search, self-rewriting notes and scheduled maintenance agents, plus Obsidian's own official Agent Skills for Claude Code from January 2026. So the article names the specific project it compares against, or says plainly it is describing the general vault-as-memory pattern. Describing "the Obsidian memory system" as one thing is the wrong-about-a-third-party failure this item was right to guard against.

**Tagged `[user]` at processing 2026-08-15**, matching the other post items rather than inventing a shape: Claude drafts the article and the post, the user publishes both.

**Only the final step yields to the one-a-day chain.** Three posts are queued ahead of it, and the pacing rule applies to the post rather than to the writing — so the item is cleared and the article can be drafted whenever. Carried as prose today because there is no way to write a date; once [not-before-date-field] ships, this becomes a `Not before:` line.

**Files:** none in this project — the artifacts are an article for the Throughliner site and a Discord post. Relates to [digest-reports-computed-fields-not-summaries] (shipped) and `resources/research/auto-memory-staleness.md` (verified and corrected).

#### [user] Discord post: the ordering ladder cut from six rungs to three, and every rung now costs no judgment [discord-post-context-adjacency]
Captured by you 2026-08-12; the angle is yours — the ladder and how much it improves the workflow. **Subject replaced 2026-08-15 — see the correction below. The slug is unchanged because slugs are immutable.**

**The subject this post had was deleted before it was ever posted, and that is the correction.** It was written to announce the cheap-to-settle rung — "/plan offers you the work closest to what this session has already read". Commit `0e62afe` on 2026-08-15 cut the ladder from six rungs to three and deleted that rung, the rung-6 offer and the decay rung with it. The item was sitting **cleared to run** when found, so a /next run reaching it would have walked you through drafting and posting a public claim about a mechanism that no longer exists. Caught by reading the item during processing; the digest's placement check matches a fixed set of known phrases and does not reach this shape, which it says of itself.

**The replacement subject is the deletion, and it is the better post.** Six rungs became three: an uncleared red flag, then unblock-potential by citation count, then longest-first by line count. **Every surviving rung either reads a field the digest already computes or subtracts two line numbers**, so ordering costs no judgment at all. Longest-first was also re-grounded — on cost-of-reading rather than on length predicting how finished an item is, because the settling session's own data contradicted the latter.

**What makes it worth saying rather than a changelog line.** The honest version is about subtraction: three rungs asked Claude to weigh something, and weighing is where a mechanism quietly stops being reproducible. The tool got simpler and more predictable in the same move — a harder and more interesting claim than "we added a feature".

**A judgment for you at drafting time.** The before-picture is that some deleted rungs were things this project built, used, then decided were not carrying their weight. Whether that goes public is your call; it is what makes the change legible rather than arbitrary.

**Verify before posting, not merely before drafting.** Every claim must be true of the *installed* plugin at the moment it goes out. Compare the installed host's build stamp against the target's before you post, since the cut is committed but a host that has not been reinstalled still runs six rungs.
**Walkthrough.** 1. Feature ships. 2. Claude drafts inside 2,000 characters. 3. You say what to change. 4. You post. 5. You confirm, and this line closes.
**Unblocked 2026-08-13.** [ladder-rung-for-context-adjacent-items] shipped and has since been refined once — the offer now leads with a recommendation rather than a flat menu (`LOG/2026-08-12-context-adjacency-offer-is-a-flat-menu.md`, `e5d169b`). Draft against the refined behaviour. Sat blocked unnoticed; the fix is the slug-resolution field in [digest-reports-computed-fields-not-summaries], which absorbed the item recording this.

**Paced 2026-08-14 on the user's decision: head of a one-post-per-day chain.** Her reason, rendered in Claude's words rather than quoted: one a day, don't drown out the server. Nothing here is unready — pacing alone held it. **The framing was repaired 2026-08-18** — it read "Her words:" over a paraphrase, which is a quote claim the text cannot support, and the three sibling post items carry the hedged form. Found by the tersification write-up's own §7, which predicted exactly this upgrade.

**Correction, 2026-08-15, in the user's own words: no post went out on 2026-08-14, "because it wasn't presented to me in next."** This item's earlier claim that she had already posted that day was wrong, and so is the same claim in [announcement-cadence-clear-to-resume]. What happened is worse than a delay: holding the item below the line made it invisible to /next, so the pacing did not slow the post down, it stopped it happening at all. That is the failure [held-items-invisible-during-normal-use] describes, observed live.

**Lifted 2026-08-15.** The holding fact — a day has passed since the last announcement — is true regardless of whether one went out on the 14th, and more clearly true if none did.

**Held again 2026-08-19, on your instruction, and its subject has now been overtaken a second time.** The post announces a ladder of three rungs where every rung costs no judgment. [decay-rung-unreachable-in-practice] was settled the same day and replaces that ladder with four rungs — an intersection rung and an alternating one — so the claim survives only until that work ships. **Posting it first would have announced a mechanism this project had already decided to replace**, which is [repeal-falsifies-a-posted-claim] happening rather than being guarded against. [discord-post-cycle-awareness] took the head of the chain instead.

**Waiting improves the post rather than merely deferring it.** The honest subject becomes the whole sequence: six rungs cut to three, then the bottom rung found to be unreachable in practice and the ladder rebuilt so it cannot starve. A mechanism got wrong twice and corrected in public is the register that has worked here before. **Rewrite the subject when this lifts — it will be the third.**

**Blocker repointed 2026-08-21, and the old one is resolved rather than merely replaced.** [decay-rung-unreachable-in-practice] has shipped and been confirmed, so the fact it named is gone — but the post is still held, by the one-a-day pacing chain, and [discord-post-cycle-awareness] sits at its head unposted. The field named a fact that had resolved instead of the fact actually holding the work, so every below-the-line revisit read this item as ready to lift and every one of them was wrong. Repointed at the item that genuinely holds it: the post now lifts by itself when the one ahead of it goes out, and no session has to remember today's reasoning. Claude's decision, deferred to by you. The subject rewrite is unaffected and stays required — see the paragraph above.

**Lifted 2026-08-21.** [discord-post-cycle-awareness] was posted and closed — `INBOX/sent.md` records the send on 2026-08-21, for completion, with the posted text in that item's LOG entry — so the head of the pacing chain is done and nothing holds this item. Under the one-a-day pacing this post goes out no earlier than 2026-08-22; the walkthrough's drafting step is where the required third subject rewrite happens.

--- Cleared to run above this line ---

#### [user] Discord post: how much stronger a session is from its start once /plan opens by reading recent LOG index lines [discord-post-session-start-strength]
Captured by you 2026-08-11. Your point, rendered in Claude's words rather than quoted: before, it felt shaky for the first few items; starting with log-awareness plus some maybe-relevant context massively boosts the start of sessions. The angle is yours; the correction below is Claude's.
**It cannot be written yet, which is why this is a queue item rather than a draft.** You asked believing the feature was live. It wasn't: `plan.md`'s Step 1 reads QUEUE.md and SPEC.md only, and its three `LOG/index.md` mentions are targeted lookups — has this been decided — not an orientation read. The feature is [plan-reads-recent-log-index], held below the line behind [index-line-length-proportional-cap].
**Your experience was real; the mechanism you credited was wrong.** What steadied that session was the below-line revisit reading LOG to check two blockers, plus the previous session's forward advisory naming where to start. Both live; neither is the five-recent-lines read. Worth carrying into the post — "the thing that helped wasn't the thing I thought" is the better story.
**The post's content, to draft when it ships.** The shaky-first-items problem and its cause; what the orientation read changes; and the honest scope — it doesn't carry all necessary context, it sets upcoming work against past work. Include the cost bound, since it's why the feature waited: five index lines is an unbounded read until index lines are capped, which [index-line-length-proportional-cap] fixes.
**Constraints:** 2000 characters, the Discord limit. Not posted until *everything* the post describes has shipped — standing rule in `CLAUDE.md`, adopted 2026-08-11.
**Walkthrough.** 1. Feature ships. 2. Claude drafts inside the limit. 3. You say what to change. 4. You post — Claude has no route to Discord. 5. You confirm, and the line closes.
**Unblocked 2026-08-13.** [plan-reads-recent-log-index] shipped — `LOG/2026-08-12-plan-reads-recent-log-index.md`; /plan's read-state step now opens with the five newest index lines. Ordinary ready work. Fourth item found sitting behind a shipped blocker; the fix is the slug-resolution field in [digest-reports-computed-fields-not-summaries].

**Paced 2026-08-14 on the user's decision: third in a one-post-per-day chain.** Her reason, rendered in Claude's words rather than quoted: one a day, don't drown out the server. Pacing alone holds it.
**Blocker repointed 2026-08-21.** [discord-post-cycle-awareness] was posted and closed on 2026-08-21 (`INBOX/sent.md`), so the old blocker had resolved and this item read as liftable while the pacing chain still held it. Repointed at [discord-post-context-adjacency], the post now ahead of it in the chain — it lifts by itself when that one goes out and closes. Same repair, same reasoning, as the repointing recorded on that item.
Blocked by: [discord-post-context-adjacency]

#### [user] Correct and post the announcement about rationale moving out of operative rules — the draft tells readers the why lives in session logs they can't reach [announcement-rationale-split-correction]
Captured by you 2026-08-09 — split out of [rationale-relocation-invisible-to-consumers] when that capture was deleted as otherwise satisfied. The 2026-08-09 Discord draft says the reasoning "lives in the session logs where you can go and read it." False for every reader not developing the method: the plugin package ships neither `LOG/` nor `resources/`. Posting it as written points users at something they cannot access.
**Why this is the user's line:** Claude can draft the correction; only the user can post. Under the capability test, drafting is Claude-work and posting is not.
**Walkthrough:**
1. Claude drafts the corrected announcement, replacing the session-logs claim with the actual split: why the method behaves a certain way is in the shipped FAQ; why a rule is worded as it is stays in the development log.
2. The user says what to change.
3. The user posts it.
4. The user confirms; it's recorded and the line removed.
Rough draft, to sharpen at step 1 — the announcement's other content wasn't reviewed, so check the whole thing, not only the false sentence. Also decide at step 1 whether it's still worth announcing, given the week that has passed.
**Paced 2026-08-14 on the user's decision: last in a one-post-per-day chain.** Her reason, rendered in Claude's words rather than quoted: one a day, don't drown out the server. Last because it corrects an already-posted announcement rather than being news, so it yields to the three new posts. It lifts when [discord-post-session-start-strength] is posted and closed.
Blocked by: [discord-post-session-start-strength]

**Files:** none — the artifact is a Discord post. Relates to [self-authoring-rules].

## Unprocessed

#### Show-first approval moments produce their text twice [approval-flow-token-doubling-simplification]
Captured by you (2026-08-01) while reviewing your Claude Code feature request anthropics/claude-code#77134. Rescoped at your direction 2026-08-13 from a larger item about approval-time doubling generally.
**The cost, narrowed to where it still exists.** Showing text in chat and writing it to a file are both the model producing those tokens, so text doing both is produced twice. That used to hit every approval moment; it no longer does — write-first shipped, and the post-write report is one line naming what landed, never a re-paste.
**What remains is the show-first set only** — the moments write-first deliberately keeps showing first, because the previous version isn't recoverable without the user: a commit message, anything leaving the machine, a wholesale conversion of a document the user already owns. There the text is composed in chat, approved, then produced again to be used.
**Why it is not buildable yet.** The saving needs the harness to surface an already-produced Write's content verbatim with no second model pass — issue #77134, which hasn't landed. Until it does there's no build to describe. Re-examine when the issue ships.
**Two things settled, not to be re-opened here.** The write-first ordering flip is decided and shipped. The convergence note about view-in-doc machinery is spent — working-mode field, Editor field and line-anchored-link promise all retired 2026-08-09.
External dependency: anthropics/claude-code#77134.

**Checked 2026-08-19 and still open** — filed 2026-07-13, labelled `enhancement`, `area:cost`, `area:tools`, `area:core`, no maintainer response and no close date. The disposition is unchanged: nothing to build, re-examine when it ships. **What the check buys is that the next session reads a date rather than re-running the lookup**, which is the whole reason it is written here.

**Two things in the discussion are worth having when this does become buildable.** A comment dated 2026-08-01 sets out the mirror direction — author-in-chat, approve, then write — and argues it needs no second primitive, because a workflow that can show a Write's content verbatim can adopt write-first ordering and get the same saving so long as rejection reverts. That is this project's shipped model described from the outside. **It looks like yours, on the date and the reasoning, but nothing in the record here says so — worth confirming rather than assuming.** A later comment proposes generalising the primitive to `show_file(path, range?)`, which would also let Claude surface parts of *existing* files without re-emitting them — that reaches the view-in-doc pointer and the inline-text offer, not just the three show-first cases, so it would widen this item rather than merely unblocking it.

**Surfaced 2026-08-19 by the decay rung, on its first firing since the interleave was adopted.** It had been the oldest entry in the queue at 17 days and nothing in the ladder had ever reached it.

**Dated 2026-08-21 with your approval — the field's first use, as this item predicted.** It waits on `anthropics/claude-code#77134`, which nothing in this queue can resolve; five weeks open with no maintainer movement, so a month out is when there is plausibly news. Not offered again before then.
Not before: 2026-09-21

**Skipped again 2026-08-19, and it is the item that produced the fix for its own condition.** Presented, found unchanged, and in being presented it made the pattern visible: three entries in one session waiting on something outside this project, none able to name a blocker, all re-offered every session. That is [not-before-reaches-unprocessed], kept and cleared in the same session. **This is its first candidate** — once `anthropics/claude-code#77134` ships, or a date is worth guessing at, the field goes here and the re-offering stops. Until the field is built there is nothing to write, so the skip stands.

#### A reversibility claim settled at processing was never checked against the world, and the build hit the exception [processing-asserts-reversibility-without-checking]
Filed 2026-08-14 by Claude at its own /done close, as a testing outcome from using the plugin to build the plugin. Host-only in its example, general in its shape.
**What happened.** [delete-codex-port-from-history] was settled at processing with a careful paragraph choosing the cheap operation over a history rewrite, recording that the cheap one "is also the reversible one" because dropped commits stay recoverable from the reflog until garbage collection. True of commits. The worktree being deleted held 722 lines of uncommitted work across 24 files plus two untracked files, none of which is a commit and none of which the reflog holds. The build halted, surfaced it, and the user chose to discard the work after being told plainly it couldn't be recovered.
**Why the processing session could not have known, and why that is the point.** Nothing in the keep-step asks a session to look at the thing it is about to destroy. The two-limb test asks whether the item says what changes inside the files it names — which this item did, precisely. A reversibility claim is a claim about the *world*, not about the item's specification, and the method has no check that reaches it.
**The shape it shares with other findings here.** [runs-alone-premise-never-tested], built in the same run, is the same failure one layer up: a plausible sentence about what git would or wouldn't recover, written at processing, quoted forward for days, refuted the moment anyone tested it. Two instances now, both about git recoverability.
**To settle at processing, and the obvious fix may be too broad.** A rule requiring every destructive item to inspect its target before clearing would fire on a great deal of work that destroys nothing. Weigh a narrower trigger: an item whose own prose *asserts* that an operation is reversible or recoverable earns a check of that assertion before it clears. That keys on something visible in the text rather than on judging what counts as destructive.
**Do not read the build's halt as the system working.** It worked because the build happened to run `git status` in the worktree before removing it, which no step required.

#### SPEC does not say how many commits a close makes, now that the answer is exactly one [spec-silent-on-one-commit-per-close]
Filed 2026-08-14 by Claude during the build of [close-produces-multiple-commits-every-time], as adjacent work rather than folded in.

**What the build settled.** A session makes exactly one commit — the close — and the post-commit tail commits nothing, riding into the next close. The accepted cost is that the working tree is dirty between one close and the next, always, which is what makes that dirt legible rather than noise.

**Why this is a capture and not part of that build.** Nothing in SPEC becomes false: its close paragraph says the close records and commits, and says the append offer exists, without claiming a commit count or a clean tree. So there is no contradiction to halt on and no stale sentence to correct — only an addition. The build's file list named `done.md` and the session-start hook, and adding product truth is the route that asks first, which would have stopped an unattended run for a sentence nobody is blocked on.

**What a keep would decide.** Whether the commit count and the expected-dirty-tree are product truth a consumer should read in SPEC — they will see the "uncommitted changes from a previous session" line at every session opening, and SPEC is where they would look to find out whether that is normal — or whether it is implementation detail belonging only in the close procedure. Relates to [close-produces-multiple-commits-every-time], [post-close-tail-state] and [close-cost-scales-with-run-size]. [done-delta-close] was deleted 2026-08-17 as already decided against in `done.md`, so it is no longer a relative; [rescan-appends-post-close-work] is the surviving piece of that subject.

#### A processed item carried its `Rule gate:` line twice, the second a truncated copy of the first [duplicate-gate-line-on-a-processed-item]
Filed 2026-08-15 by Claude at the close of the eighteen-item run, noticed while transcribing.

**What was found.** [move-section-does-not-report-line-crossings] carried two consecutive `Rule gate:` lines. The first read "not needed — this extends an existing report to a second code path and adds a refusal branch"; the second, the same without the refusal clause — evidently an earlier draft left in place when the item was revised. The build transcribed the fuller one once.

**Why it is worth a line.** The disposition is what two of the corpus checks read, and both take the line as authored. Two lines disagreeing about what the build does is a small inconsistency now and a wrong reading later — the truncated copy describes a narrower change than the item specified. It also suggests revision passes over a processed item append rather than replace, which would produce this again.

**What a keep would decide.** Whether anything mechanical should notice a duplicated disposition — the queue lint is the natural site and already parses work-item structure — or whether one instance is below the bar and this is a note about revising items in place. The bar question is real: one occurrence, which this project's own gate treats as insufficient for a freestanding rule.

#### A personal bridge pushing `[user]` items into Taskflow as tasks, and reading completions back [taskflow-personal-bridge]
**Raised by you 2026-08-19**, from executing in another of your projects where the work is mostly `[user]` items. Your framing: Throughliner becomes an executive layer over projects Claude only half-implements, and sometimes you do not want to complete things in conversation — you want the to-do list. **The mapping is yours: a `[user]` item is a task, and its steps are subtasks.** The assessment below and the decomposition are Claude's.

**Your mapping is Taskflow's own model rather than an approximation, which is what makes the completion half work.** Taskflow's subtasks inherit their parent's Project, date and placement, and a parent has no checkmark of its own — it is complete only when every subtask is, and un-checking any child pulls the parent back out of the completed tray. So completion arrives as one derived signal per item, and a half-done item cannot read as done.

**Two decisions of yours, in your own words.** Route: *"design this against the file-based route now, with MCP as the later transport."* Scope: *"agreed, personal bridge to start."* So this is host-only tooling in this project, assuming your own Drive setup, and it ships nothing to consumers; promoting it to a shipped feature is a later decision this does not pre-empt.

**Why file-first rather than MCP.** Taskflow's paid tier already designs the channel — Claude reaching Taskflow through a remote MCP server — so Throughliner would be a client of a route Taskflow intends rather than an integration Taskflow's local-first principle forbids. But `[0020-remote-mcp-server]` and `[0019-ai-choice-flow-and-mcp-setup]` are unbuilt over there and cloud sync is their precondition. The same reasoning is already on their queue in `[strategy-doc-preview]`, in your words there: *"We're just here, so we don't need the MCP."*

**Two hazards found by reading their SPEC rather than assumed.** Taskflow runs on the phone against a local Room database, so a file route means producing a file that is carried onto the device, not writing where Taskflow reads. And their existing `[0014-json-export-and-import]` is a whole-database export and restore — pushing tasks through it would replace every other task in the app. What this needs is an **additive** import, which Taskflow has neither built nor designed.

**Not designable here yet, and that is why this is a capture.** The file contract, which Taskflow Project a pushed item lands in, and when a push happens all depend on what Taskflow agrees to build — so the second limb cannot be stated. It waits on [taskflow-bridge-request].

**Dated 2026-08-21 with your approval.** It waits on Taskflow's reply to the three questions mailed 2026-08-20, which nothing in this queue can produce; a week is when there is plausibly news, since Taskflow is your own project. Not offered again before then.
Not before: 2026-08-28

**One thing to settle at processing regardless of their answer:** a `[user]` item's text can name real people or client details, so what crosses the boundary needs the scrub the queue already gets, and a pushed task is leaving this project's records.

#### Every procedure doc ends on a terminal step, and none can tell finished from interrupted [procedure-docs-cannot-tell-finished-from-interrupted]
**Split from [rescan-does-not-hand-back] on 2026-08-21, on your decision**, once that item's three-file fix turned out to be fully specified while this half was not. The observation that started it is yours; the design question below is Claude's.

**What prompted it.** Claude Code's documentation says an invoked skill's content enters the conversation once and is never re-read, so *"write guidance that should apply throughout a task as standing instructions rather than one-time steps"* — see `resources/research/skill-content-lifecycle.md`. All five of this method's procedure docs are numbered marches ending in a final step, which is the shape that instruction warns against. /rescan is the confirmed instance: its terminal step reads as the end of the conversation's work.

**Your evidence, and it is what makes this a design question rather than a rewrite.** Asked whether the same property affects /plan and /next, you said it is a problem sometimes: **sometimes the session ends when planning or building is done, and that is correct**; and sometimes the skills need to be alternately run depending on the conditions — not normally, but sometimes.

**So the naive fix is refused before it is proposed.** "Stop ending" is wrong, because a terminal step is right in the common case. Rewriting five docs to end conditionally, with nothing able to read the condition, replaces a doc that always ends with a doc that guesses — and a guess reads as a decision, which is worse than a consistent ending someone can learn to work around.

**The actual question: can a procedure doc tell which case it is in?** Three candidate signals, none weighed yet. What the user last asked for, which is in the conversation and is what /rescan already reads to do its job at all. Project file state, which is what the scope-lock already uses — `pre_tool_use.py` decides a session is a planning one purely from the absence of this session's build working file, so file state is a proven readable condition. Or nothing, in which case the honest outcome is that each doc's ending states plainly what it does and does not know, which is the honest-limit route this project has chosen repeatedly over a check that over-claims.

**Why it cannot be kept yet.** The file list is the audit's own output, which fails the keep check's second limb by construction. What changes inside each doc depends on which signal survives, and no signal has been tested. **Do not schedule the design into the build** — an item whose prose defers a decision to the start of a run fails the same limb.

**What would settle it, and who owns each part.** Whether a doc can read its own situation is a fact to be established by reading `pre_tool_use.py`, `rescan.md` and the conversation-reading `rescan.md` already does — Claude's to find. Whether an honest "I don't know whether you were mid-something" ending is acceptable output is yours, since it is a decision about what the tool says to a user rather than about what it can do.

**Skipped 2026-08-21, settler named: process after [rescan-does-not-hand-back]'s fix has shipped**, since that build establishes what a corrected ending looks like and this design is cheaper read against a worked example. No date and no blocker line — it stays a capture because its file list is its own design's output.

**Runs behind [rescan-does-not-hand-back]**, which fixes the one confirmed instance. Placement carries that and this sentence carries the reason: no `Blocked by:` is written, because this could be designed independently — it is only cheaper afterwards, since that build establishes what a corrected ending actually looks like.

**Files (rough): not yet derivable, which is the point of not keeping it.** Likely `plugin/throughliner/docs/` across the procedure docs, and possibly nothing at all if the answer is that no signal exists. Shipped in effect: every consumer runs these docs. Relates to [plan-does-not-build-keeps-being-relitigated] and [standing-audit-programme], both of which record a doc's own wording teaching a later session the wrong thing.

#### The autonomous keep-step kept two rule-amending items without writing the gate disposition, and the next build halted on it [keep-step-skipped-gate-disposition]
Filed 2026-08-21 by Claude, on the user's report of the halt. The 2026-08-21 autonomous planning run kept [cut-length-everywhere] and [sent-record-surfaced-as-waiting-mail] — both amend the method's own rules — and wrote no `Rule gate:` line on either. The following /next run halted before locking scope, correctly, and the user had to intervene: the gate was then run in conversation and the two dispositions written onto the items. The halt worked; the keep-step did not. The question a /plan should weigh: whether the keep-step's gate obligation needs a mechanical backstop for autonomous runs — e.g. the disposition-presence check running at the plan close over items kept that session, not only at rule-bearing commits — or sharper wording at the keep-step itself. Relates to [rule-gate-dispositions-missing] (the check's hash timing) and [build-view-strips-the-gate-disposition] (the view not carrying the line).

#### The shell-write guard sees neither the target nor the computation when a write's path is built by a call [shell-guard-blind-to-call-built-paths]

Filed 2026-08-21 by Claude, found while reproducing [shell-write-guard-blocks-the-scratchpad].

**The hole.** `open(os.path.join(d, 'x.md'), 'w').write(...)` passes the guard entirely. `structured_write_targets` returns nothing, so there is no target to check, and `has_computed_write_target` returns False, so it is not denied as unreadable either. The command runs.

**Why both halves miss it.** `PY_OPEN_WRITE_ANY` matches `open(` followed by `[^,()]+?` up to the mode argument. A path built by a call contains both a comma and parentheses, so the pattern does not match at all — and the computed check only fires on arguments it matched. The result is a shape that is neither literal nor computed as far as this code is concerned.

**Why it matters.** This is the exact failure the guard was written for. Its own docstring records that "a computed target slipped past an earlier version of this check and silently corrupted QUEUE.md, and the only difference from the version that was correctly blocked was one variable assignment." `open(p, 'w')` with a bare variable is correctly denied today; wrapping the same path in `os.path.join(...)` is not.

**Verified, not inferred.** Driven directly against the target hook: `targets=[] computed=False` for the join form, against `targets=[] computed=True` for the bare-variable form.

**Not fixed in that item's build,** because its described work was the disagreement between the guard and its own message — a raw-string literal being read as computed — and this is a different defect in a different function. Widening `PY_OPEN_WRITE_ANY` to tolerate nested calls needs its own design: the obvious `.+?` risks matching across unrelated arguments, which is the fragile general-parsing this module deliberately rejects.

Relates to [shell-write-guard-blocks-the-scratchpad], whose reproduction found it.

#### An item whose described work is queue CONTENT can be cleared but never built, and nothing at the keep-step catches it [queue-content-items-are-unbuildable-by-a-run]

Filed 2026-08-21 by Claude, from a build run that met one.

**What happened.** [cut-length-everywhere] listed QUEUE.md among its files — "every item cut to its build block plus a short rationale". The scope-lock refuses a build any direct Edit or Write on QUEUE.md, by design: a build reads the generated view, and the only queue writes a run makes are the mover's per-item removal and an appended capture. So that limb of the item was unbuildable from the moment it cleared, and nothing said so until the run was already scope-locked. [lint-flags-its-own-scaffolding] had the same shape in its local half.

**Why the keep-step misses it.** The two-limb buildability check asks whether the item names its files and says what changes inside them. Both items passed: the files were named and the changes were described. The limb that does not exist is whether the named files are ones a build is *permitted* to write.

**The mechanical form, which is what makes this cheap.** The scope-lock's own refusal list is short and known — QUEUE.md is the only project doc a build cannot edit at all. An item naming QUEUE.md in its Files line is either a queue-content rewrite, which is planning work, or a mistake. Either way it should not clear to run.

**Worth checking whether the answer is a keep-step limb or a lint rule.** The queue lint already parses each item's build block, so a cleared item naming QUEUE.md could be flagged with no judgment at all — which would fire before a run ever locks scope. That is the cheaper site if it works.

**Not urgent.** The failure is visible and recoverable: the run halted, said so, and the user redirected. Nothing was silently skipped.

Relates to [cut-length-remaining-docs], whose remaining work includes the same queue limb, and to [keep-step-accretes-from-five-items] — which is a reason to weigh this against the keep-step's existing load rather than adding a sixth clause without looking.

#### Should /plan write CLAUDE.md, making planning the session that authors the method's rules [plan-as-rule-author]
**Your proposal, 2026-08-21**, split out of [build-view-strips-the-gate-disposition] at processing on 2026-08-21 so the buildable repair there did not decide this by momentum. It changes who authors the method's rules and deserves its own discussion, not the tail of a processing run.

**The proposal.** Lift the planning bar on `CLAUDE.md` so /plan writes rule text at the keep-step, where the gate already runs and the user is present — rather than a build typing it later from a disposition.

**Two arguments for it, the second previously nowhere in the record.** A build that writes rules is the party that did the work writing the text saying the work was right — the SPEC-symmetry argument. And /plan is the session the user is in: a rule the user is meant to read and approve would be written where she can see the words, where today every method rule's wording is produced in a run that is unattended in practice.

**Two costs, the first the user's own objection from elsewhere in this queue.** [plan-does-not-build-keeps-being-relitigated] records her words — *"I don't know why this is even a question. Plan does not build."* — and letting /plan write rule text moves that boundary; a candidate answer is that writing a document is not building, since /plan already writes SPEC, but that is what needs settling rather than assuming. Second, load: a planning session admitting fifteen rules would then write fifteen rules, on top of already being the heavy session.

**Context that changed since the prior refusal.** `LOG/2026-08-17-scope-lock-denies-claude-md-2.md` (`7e3c1c8`) refused a permission change on the ground that deciding is not writing — an answer that assumed the disposition travels to the build, which had failed. [build-view-strips-the-gate-disposition]'s kept repair makes the disposition travel again, so the current model works as designed; this proposal is now a choice between two working models, not a fix.

**What stays refused regardless, carried from the parent item:** barring the build from CLAUDE.md *without* lifting the planning bar — the two bars together would make the method's rules unwritable.

#### done-build.md's reply step still carries the broad changed-work trigger the reply rule just dropped [done-build-reply-trigger-stale]
The reply obligation was narrowed to question-asking messages ([inbound-replies-not-drafted]): feedback-and-inbox.md's triage and the always-loaded rule now both say a question is owed a reply and a defect report is owed nothing. done-build.md's step 1.5 ("Reply to mail the run opened") still fires on "a message that changed work here" — the broad trigger the amendment evicted elsewhere. That file was outside the item's described work, so the build filed this rather than folding it in. The fix is one wording change aligning 1.5's trigger with the question form.

#### SPEC and README rest the throughline on total amnesia, which current Claude Code no longer has [throughline-claim-overstates-amnesia]
Finding from [claims-need-a-claude-code-delta-test], approved 2026-08-21. SPEC ("Claude's memory resets each session") and the README claim a fresh session carries nothing forward — current Claude Code ships an auto memory directory and context summarization that carries work across windows, so the delta test fails the claim on its own terms. The throughline's real delta is structured, user-vouched product truth versus Claude's private notes; restate the claim on that ground. Files a /plan should weigh: SPEC.md, README.md, faq-template.md (the "Why does the method record the reasoning" entry leans on the same premise).

#### INBOX framing predates Claude Code's live session messaging [inbox-claim-predates-live-messaging]
Finding from [claims-need-a-claude-code-delta-test], approved 2026-08-21. "Projects message each other instead of you carrying notes between chats" reads as if no channel exists at all; Claude Code can now message live sessions on one machine. The INBOX's delta — durable, offline, approval-gated mail between projects — is real and currently implicit. One clause where the feature is described (SPEC's INBOX paragraph, README line, feedback-and-inbox.md's opening) keeps the claim honest.

#### The keep-step's research-index check restates the always-loaded Research rule at a second site [keep-step-index-check-restated]
Finding from [keep-step-accretes-from-five-items], approved 2026-08-21. plan.md's shelf question ("check resources/research/index.md for an entry covering this item's subject") restates the always-loaded rule "before offering a search, read resources/research/index.md" — two rules on one subject at two sites, the shape the law-prose pass hunts. A cross-reference from the keep-step to the always-loaded rule could replace the restatement. The audit judged every other keep-step clause correctly sited; this is the only merger candidate.

#### [user] walkthroughs do not travel into the build view, so a run cannot drive them [user-walkthrough-missing-from-view]
Finding from this run, approved 2026-08-21. The view prints "No build block — the run halts on it as underspecified" for a [user] item, and the run may not read QUEUE.md — but next.md's walk-through branch says to drive the steps "the item records", which live only in queue prose. This run reached [competition-comparison-article] and [discord-post-context-adjacency] with no steps available to drive. Either the view carries a [user] item's walkthrough (as it now carries dispositions), or the walk-through branch names where the steps legitimately come from.

#### An audit directed at queue prose cannot reach it from inside a run [audit-cannot-read-queue-prose]
Finding from [keep-step-accretes-from-five-items], approved 2026-08-21. The audit was directed to read [research-packaged-as-build-work]'s pressure argument — Unprocessed prose, which the view strips and the run's rules bar reading. It went unread and the entry says so. Any future audit naming queue prose hits the same wall; the keep-step could refuse to point an audit at queue prose, or the view could carry named excerpts for audit items the way it carries build blocks.

#### SPEC's advisory paragraph owes the replace-branch sentence [spec-owes-advisory-replace-sentence]
Filed by the build close, 2026-08-21. [advisory-step-collides-with-a-spent-note] shipped: a close meeting a spent advisory in the reserved slot now replaces it — deletes the spent note and files its own, saying it replaced one. SPEC's forward-recommendation paragraph still says clearing happens only at the next /plan's read. The sentence SPEC owes, for the next planning session to write with the user present: a close filing its own advisory over a spent one replaces it, and the read-clears-it rule covers only notes a close is not replacing. The FAQ's "Last session advises…" entry has the same one-clause lag.

#### SPEC's keeping-current paragraph owes the managed-block carve-out sentence [spec-owes-managed-block-sentence]
Filed by the build close, 2026-08-21. [managed-claude-md-block-never-refreshed] shipped: /setup's migration now refreshes the PLUGIN-MANAGED region of a project's CLAUDE.md, reporting what it replaces and moving user-authored lines below the end marker. SPEC's "Keeping projects current" paragraph still says the top-up "never rewrites or clobbers anything the user has written" and that reconciling template-worded content "stays deliberately out of scope" — true of user text, now false of the managed region, which is method-owned. The sentence SPEC owes: the plugin-managed CLAUDE.md block is the one region migration refreshes, with user text moved below the marker rather than overwritten.

#### CLAUDE.md's folder-rename note says "renamed from `docs/` to `docs/`" — the old name is missing [claude-md-rename-note-lost-old-name]
Filed 2026-08-21 by Claude at a freeform close's wind-down, noticed while reading CLAUDE.md in full for the length cut. The Model target section's note about the 2026-08-21 folder rename gives the same path twice, so the sentence no longer says what the folder used to be called — the old name (`docs-b/`, per the installed plugin cache's layout) was presumably lost in an earlier edit. One-line fix to this project's CLAUDE.md, but it edits the sentence that explains why old records legitimately carry the old path, so the fix should restore the old name rather than delete the note.

#### The ordering ladder's fixed-at-opening medians were re-derived mid-session by the session that knows the rule [ladder-medians-re-derived-mid-session]
Filed 2026-08-22 by Claude at its own close, from the wind-down re-scan. Mid-session this planning run briefly ranked Unprocessed against a re-computed median (11 lines, from a re-run digest) instead of the medians fixed at the opening (10 lines), skipping two qualifying 10-line entries for a few picks before self-correcting. plan.md states the rule and its reason — a recomputed median lets the group stop shrinking — and the rule was in context and did not govern the pick. Joins the correctly-worded-rule-not-firing class (tenth instance); per that record, stating it harder is not a candidate direction. What may be mechanical: the digest prints the medians, so a session could be required to quote the opening medians in the floor narration, making a re-derived figure visible as a mismatch — weigh against the noise cost. Filed while the queue is otherwise clear so the instance is not lost.

#### Whether the already-decided check actually fires in consumer sessions is untested, and the user is unsure it does [already-decided-check-untested-in-consumers]
Filed 2026-08-22 by Claude at its own close, from the wind-down re-scan. Mid-session the user questioned whether dispositions routed to LOG will actually be found by later sessions — "that's not the case with throughliner running on any session other than this one" — and, asked whether she had seen a consumer session re-propose something its LOG had settled, answered unsure. The machinery ships (per-item entries, index lines, plan.md's check-LOG-before-keeping/deleting), but no evidence exists either way about it firing in consumer projects, and the honest answer given in-session was "findable, with a shipped check that usually fires", not "always found". What would settle it: a real instance from a consumer project (watch for one), or a deliberate test — seed a consumer project's LOG with a decided item and observe whether a later /plan re-proposes it. Until then this records that the assumption is unverified, so a future session does not read the design as proven.

