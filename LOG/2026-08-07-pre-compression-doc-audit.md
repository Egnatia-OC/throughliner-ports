# 2026-08-07 — Pre-compression consistency audit of the doc corpus

A ten-pass consistency audit of the plugin's instruction corpus (docset B, skills,
templates, hooks, scripts, output-styles, plus this repo as the representative
project), run ahead of the planned compression pass, from a user-supplied brief
whose premises were verified and corrected before running. Executed as an
eight-subagent fan-out on Fable 5; every finding cited below was either
independently found by two or more auditors or had its cited lines re-read and
confirmed by the compiling session. No file was edited by the audit itself.

**Brief corrections established before the run** (the brief was authored outside
this session and treated as unverified): docs/ is NOT retired — it is frozen
docset A, whose retirement was proposed and declined 2026-08-05; the five
SKILL.md `docs/` paths are the deliberate session-start redirect mechanism;
skills/cruise/ is an empty untracked remnant (files deleted at 5e62c1c), not a
live entry point; resources/authoring-heuristic.md IS referenced (CLAUDE.md +
method-compliance-audit-checklist.md) and CLAUDE.md's Model target section
exists — only its "current target is Opus 4.8" line is stale.

**Already queued before this audit, found again independently (not re-filed):**
[show-then-write-survives-at-step-level] (the write-first vs approve-before-write
split, finding A2 below), [skip-step-hardcodes-dev-repo-script-path] (plan.md:770,
finding C2), [faq-backfill] (the project FAQ fossil, finding D4).

---

## A. Direct contradictions — two live texts incompatible at one moment

- **A1 — CONFIRMED (the brief's named suspect).** plugin-behaviour.md:139-142 and
  :1670-1675 both forbid closing a Claude-raised capture with "anything else?";
  next-build.md:219 ("Claude discovers user-runnable testing is needed", step 2)
  instructs exactly that loop. The user-raised sibling at next-build.md:139-147
  is consistent; only the Claude-raised procedure collides. High confidence.
- **A2 — Write-first vs approve-before-write** (already queued as
  [show-then-write-survives-at-step-level]). Write-first: plugin-behaviour.md:199-201,
  :826-830; plan.md:29-36. Show-first: done-build.md:49-50, done-audit.md:29-30,
  next-audit.md:81-110, done.md:521-524, plan.md:854-857 — and plan.md
  contradicts itself (line 31 vs line 619 "Don't write until approved"). High.
- **A3 — done.md self-contradiction, scan order.** :259 and :503-509 say the
  wind-down re-scan precedes the LOG entry; the [user]-item close (:121→:131) and
  handmade close (:168→:173) order entry-then-scan. Verified. High.
- **A4 — done.md self-contradiction, approval frame.** :348 "identical for every
  flavor — write the entry to its LOG file, then put the wording in front of the
  user" vs :168-169 (handmade close) "show them for approval before writing".
  Verified. High.
- **A5 — Push-offer collision at a combined close.** done.md:90-91 supports a
  /plan close that also closes a completed [user] item; done.md:135-136 then says
  offer push, done-plan.md:297-301 says a planning close never offers push. No
  carve-out either side. Medium-high.
- **A6 — The shipped QUEUE scaffold contradicts the red-flag lifecycle.**
  setup.md:206-207 scaffolds Processed-header text saying red-flagged items live
  there with "State: cleared/uncleared"; plugin-behaviour.md:1154-1167 says
  uncleared NEVER sits in Processed. Every consumer receives the contradicting
  text. migrate-checklist.md:52-54, 82-85 also omits the constraint. Verified. High.
- **A7 — FAQ vs procedure on readiness-line narration.** faq-template.md:281
  promises Claude "tells you where it sits" every planning session;
  done-plan.md:140-142 mandates narrating only on a move, silence otherwise.
  Verified verbatim. High.
- **A8 — FAQ states the retired advisory-clear trigger.** faq-template.md:321
  ("once you and Claude have agreed on the order, the note is deleted") is the
  exact trigger done-plan.md:250-254 names as the failure it replaced. High.
- **A9 — Two FAQ entries give two firing moments for the missing-setting
  catch-up.** faq-template.md:222-224 (session start) vs faq-template.md:419-429
  + plan.md:141-160 (/plan Step 1). High.
- **A10 — Two FAQ entries contradict each other on model detection.**
  faq-template.md:339-345 ("works out which to use… There's no setting for it")
  vs faq-template.md:41-47 + setup.md Q6 + CLAUDE-TEMPLATE.md:33-37 (detection
  unavailable in the desktop app, so a recorded setting exists). High.

## B. Documented-but-not-implemented / implemented-but-undocumented

- **B1 — The `--- Plan session here: <reason> ---` halt marker has no
  implementation in docset B.** Found independently by four auditors. Documented:
  faq-template.md:267-269, faq-index-template.md:54, host CLAUDE.md ("the only
  in-queue halt marker"), post_tool_use.py:111-112 (lint exemption). Implemented:
  nowhere — next.md:33-34 says the cleared-to-run marker "is the only thing that
  bounds a run", :148-150 denies other gates; plan.md never places or removes
  one. Same shape as the retired push marker (documented, honoured by nothing),
  which docs-b itself recounts at plugin-behaviour.md:1069-1076. The audit's
  highest-priority finding. Design call: implement or retire.
- **B2 — Subagent ask-gate wired to one tool name.** pre_tool_use.py:552 matches
  ("Task", "Agent") and comments that both occur across harness builds;
  hooks.json:31-38 registers only a Task matcher, so an Agent-named payload never
  reaches the hook. High on divergence; impact depends on current harness
  matcher semantics.
- **B3 — Red-flag /next backstop absent from the /next family.**
  plugin-behaviour.md:1175-1180 ("if /next meets one it stops"); grep across
  next.md / next-build.md / next-audit.md: zero red-flag text. done-side backstop
  exists (done.md:493-498, done-build.md:96-102). Whether resident-doc-only is
  sufficient is a design call.
- **B4 — Abort/requeue assumes the replaced queue model.** next-build.md:266-269,
  :280-281 direct "return it to Processed"; under next.md:229-250 items never
  leave the queue until ticked, so there is nothing to return — and an insertion
  is what next.md says the lint flags. Medium-high; incompatible models, unclear
  which text is stale.
- **B5 — Self-hosting mechanism implemented, documented nowhere.**
  session_start.py:442-489, :895-926 (ask-once, `Self-hosting:` CLAUDE.md line,
  report suppression); no template field, no docs-b or FAQ mention. Verified by
  grep. High.
- **B6 — session_start silently writes into the consumer's repo.**
  `_record_payload_once` (session_start.py:259-277) drops
  resources/research/session-start-payload-sample.json when that folder exists.
  Undocumented. High.
- **B7 — Editing-state signal asymmetry + unadopted-folder litter.**
  pre_tool_use writes the active marker only in adopted projects (SPEC gate
  first); post_tool_use.py:481 writes the closing marker BEFORE its SPEC gate
  (:486) — an unadopted folder accumulates `.throughliner/` markers never
  opened, with no .gitignore covering them. Verified order. Auditor's verdict:
  looks wrong, can't be accounted for from the corpus. High on the code path.
- **B8 — Scope-lock fail-open tri-state and once-per-build "unscoped build"
  advisory** (pre_tool_use.py:17-21, :684-731) documented only in the script's
  own header. High.
- **B9 — Mechanical denial of scripted file-writes** (Python open(...,'w') etc.,
  pre_tool_use.py:81-122, :621-662) enforced; no doc says so (plan.md:710-712
  only alludes). High.
- **B10 — `git commit -a/-am/--all` denied by the hook** (pre_tool_use.py:72,
  :611-619); plugin-behaviour.md's File-safety block (:1821-1826) doesn't list
  it. High.
- **B11 — FAQ/ passes the planning gate silently; every doc statement omits it.**
  pre_tool_use.py:405-436 (verified: FAQ/, memory, research, scratchpad all
  quiet) vs plan.md:20-21 and the hook's own ask text (:796-810). High.
- **B12 — Nested-SI surfacing narrower than documented.** Runs only in the
  not-adopted branch (session_start.py:669-722); plugin-behaviour.md:368-370
  doesn't state the limit. Medium-high.
- **B13 — Two docs overstate the queue lint.** migrate-checklist.md:37-39 ("the
  lint confirms the new queue is well-formed") vs the deny-list advisory design
  (post_tool_use.py:59-64, novel structure passes silently); next.md:250-252
  ("a heading inserted under Processed gets flagged") vs Write-based insertions
  passing by design (:386-390). Medium-high.
- **B14 — "This exact shape is what all three hooks parse" — it's two.**
  plugin-behaviour.md:831-833; pre_tool_use never parses the work-item shape.
  Secondary: "with no error surfaced" is not always true (orphaned-prose check,
  post_tool_use.py:344-380). High.
- **B15 — Minor undocumented emissions:** hourly stale-marker sweep
  (session_start.py:537-568), dirty-tree state line (:964-975), backfill-anomaly
  note (:130-146). Low stakes.
- **B16 — CLAUDE-TEMPLATE.md:3 claims "Updated on /setup and plugin reinstall";
  nothing updates it on reinstall.** The hook only reads it. Medium.
- **B17 — migrate-checklist.md:18-19 says CLAUDE.md "is topped up by
  session_start"** — that moved to /plan's opening read (plan.md:141-154). High.

## C. Stale references and broken pointers

- **C1 — The hook's own denial text routes to a retired section name.**
  pre_tool_use.py:750 "route findings to Captures in QUEUE.md" (verified) and
  faq-template.md:112 — the live section is Unprocessed; `## Captures` is what
  the migration converts away from. High.
- **C2 — plan.md:770 hardcodes the dev repo's mover path.** Already queued as
  [skip-step-hardcodes-dev-repo-script-path]; three auditors re-found it. High.
- **C3 — next.md:130 cites plugin-behaviour's "Context awareness" for the
  don't-size-the-run trigger; that section is one sentence about resuming from
  _build.md** (:1866-1868). The rule actually lives at plugin-behaviour.md:180-186
  and next-build.md:284-296. Verified. High.
- **C4 — "stop self-sufficiency" cited three times (done.md:357, :527, :570);
  the name appears nowhere in plugin-behaviour.md.** The rule exists unnamed at
  :55-77; content matches, the cited name greps to nothing. High.
- **C5 — More cited-name misses:** "the Captures placement rule" (four docs:
  next-build.md:142, next-audit.md:111, done-build.md:60, done-audit.md:42) → an
  unnamed "**Placement.**" paragraph (plugin-behaviour.md ~:930); "the coherence
  rules" (next-build.md:150-154) → no such named criteria anywhere; "the
  diagnosis-order rule" (plan.md:444) → ambiguous between two plugin-behaviour
  rules (:627 and :1536-1547); next-audit.md:87 canonises "the bulk-approval
  inversion", a name the target never uses (its own names: result-set inversion,
  destination rule); "spec-entry trigger test" (done.md:206-208) → plan.md's
  unnamed "the test:" parenthetical (:39-41), quote-by-name fragile. Medium.
- **C6 — setup.md's scaffolds reference a retired interview.** `[filled by Q1]`
  …`[filled by Q4]` (:175, :178, :181, :192, :219, verified) and "Peek before
  Q1" (:62) — Step 3 is now adaptive with only Q6 numbered; Q5 exists nowhere;
  the Step 3 heading promises "three settings" (:307), the body carries one. High.
- **C7 — CLAUDE-TEMPLATE's `Language:` field (:29-31) is scaffolded but nothing
  fills or reads it.** Verified. Medium-high.
- **C8 — resources/testing/ is a sanctioned destination setup never scaffolds**
  (setup.md:272-275 creates only resources/research/, with a rationale that
  argues for scaffolding testing/ too). Medium.
- **C9 — plugin-behaviour.md:444 names "the deep-research skill"; no such skill
  exists anywhere in the tree.** Medium.
- **C10 — docs-b/setup.md:121 points into docs/** for migrate-checklist — the
  one docs-b→docs/ reference outside the SKILL.md redirect; directive coverage
  rests on a generous reading of "wherever a skill names a procedure doc". Medium.

## D. Retirement completeness (LOG-driven)

- **D1 — LIVE: host CLAUDE.md's "A new batch type touches four places" rule
  describes retired machinery.** Names ALLOWED_SUBHEADINGS (grep: exists only in
  CLAUDE.md:118 itself), the Build/Test/Freeform types (Test and Freeform
  retired), and routes wiring to docs/ paths. High.
- **D2 — LIVE, one word: plan.md:171 "the user-only batch"** — retired noun in a
  doc every docset-B /plan loads. Verified. Also host-side: CLAUDE.md still uses
  "method docs" as a live heading (:319, :242, :342) and "batch" as its unit
  noun, both retired terms; whether host CLAUDE.md was in either sweep's scope
  is unrecorded. Medium-high / medium.
- **D3 — session_start.py comments (:160, :811, :826) name "the deferred-test
  roll"** — a retired mechanism name nothing defines; the live consumer is
  plan.md's below-line revisit. Verified. Inert (comments). High.
- **D4 — FAQ/faq.md (project copy) is a fossil across ~8 retirements** — known,
  queued as [faq-backfill]; this audit confirms the inventory (headings at faq.md
  :9, :17, :21, :33, :45, :61, :69, :73; index.md:8, :10). High.
- **D5 — FABLE-BRIEF.md sits spent at project root, no disposition logged.**
  Describes cruise/Parked/the deleted sibling folder as current; referenced by
  nothing outside LOG. High on staleness.
- **D6 — resources/reader-test-workflow.js asserts the pre-redesign model as its
  expected test criteria** (Batches, Parked, spec-edit-only SPEC — the inverse of
  the current rule); untouched since 2026-06-21; no retirement entry. The
  strongest looks-retired-but-unlogged candidate. High on staleness.
- **D7 — resources/queue-two-section-migration-recipe.md plausibly superseded by
  the shipped migrate-checklist.md**; no recorded relationship. Low-medium.
- **D8 — Thirteen retirements verified COMPLETE:** REGISTRY.md, cruise text,
  freeform, multi-spec, push marker, "work line", handover→walk-through, old
  red-flag states, goal sessions, hook "batch" vocabulary, IDEAS.md, spectrum
  offers, test flavor. Calibration set behaves as documented: skills/cruise/ is
  an empty untracked remnant (inert); Working mode / Completion mode / Editor
  are the deliberate, correctly-handled incomplete retirements.

## E. Orphans

- **E1 — resources/captures/ exists; plugin-behaviour.md:765 says resources/
  "holds two things only" (research/, testing/).** One artifact is wrong; design
  call. High on the mismatch.
- **E2 — resources/testing/test_reorder_queue.py is unreachable** — no ritual,
  queue item, or doc runs it; CLAUDE.md's rituals name only
  hook_schema_check.py. Medium.
- **E3 — scrub_sweep.py is invoked by description in three docs
  (plugin-behaviour.md:1241, faq-template.md:63, SPEC.md:83) but its path is
  named nowhere** — unlike reorder_queue.py, whose invocations give the full
  path. Medium.
- **E4 — Low notes:** the filing-time commit-stamp convention
  (plugin-behaviour.md:841-854) has no procedure that reaches it;
  authoring-heuristic.md:6 still says "current target is Opus 4.8" against the
  two-docset Model target; four research files have zero inbound references
  (batch-sizing-research, codex-port-postmortem, context-window-hook-access,
  live-queue-preview — sanctioned home, likely fine); overnight-blitz-plan.md is
  live but discoverable only via LOG.

## F. Terminology drift

- **F1 — The run boundary carries five internal names** — "cleared-to-run
  marker", "cleared-to-run line", "readiness line", "readiness marker", bare
  "the marker"/"the line" — and the "readiness" family is never anchored to the
  literal `--- Cleared to run above this line ---` (done.md:772 defines it only
  functionally). A compression pass could collapse them wrongly. High that the
  synonymy is unanchored.
- **F2 — "walk-through" vs "walkthrough"** split fairly consistently between the
  live drive and the recorded steps, but the convention is stated nowhere — reads
  as drift to any editor. Medium.
- **F3 — Lesser variants, all recoverable but unanchored:** the session working
  file ("own notes", "working notes", "working state" vs _plan.md/_build.md by
  name); the planning gate (four surface forms across done.md, plan.md,
  plugin-behaviour.md, pre_tool_use.py); "the queue mover" at
  plugin-behaviour.md:1833 with no local anchor to reorder_queue.py. Low-medium.

## G. Premise-bearing factual claims — inventory for human verification

Fifty claims catalogued (none verified by the audit, per the brief). The ten the
compression pass most needs checked first, because multiple rules rest on each:

1. `.md` links with `:N` line suffixes are dead in the desktop app; plain `.md`
   links open at the top; code files honour anchors (plugin-behaviour.md:247-249;
   next.md:100-102; next-build.md:42-44; faq-template.md:23).
2. Reply suggestions are harness-generated, unreliable, absent on remote control
   (plugin-behaviour.md:56-66; done.md:526-530; faq-template.md:355-361) — the
   stop-self-sufficiency rule rests on this.
3. The session-start docset directive actually substitutes docs-b/ wherever a
   skill names docs/ (SKILL.md files + plugin-behaviour.md:375-379) — the whole
   corpus's reachability rests on this.
4. The "file modified on disk" warning fires as described and the mover reliably
   trips it (plugin-behaviour.md:1830-1838; plan.md:635-654; done-plan.md:109-117).
5. The MSIX/AF_UNIX sandbox mechanism blocking Gradle, incl. `gradlew --version`
   being the undetecting command and the three external references
   (plugin-behaviour.md:520-530, :720-723; faq-template.md:491-503) — dated,
   could be fixed upstream, would invert the FAQ's advice.
6. The desktop app omits the `model` field in the session_start payload
   (faq-template.md:43-47; the basis of the recorded-Model setting) — plus the
   internal FAQ contradiction A10.
7. reorder_queue.py's behaviour contract (byte-exact, refuses-not-guesses,
   non-zero-means-nothing-written, marker kept in place) as stated at five doc
   sites — many rules rest on the script being exactly this.
8. The marketplace install path (`FlintcraftTech/throughliner` →
   `sovereign-implementer@flintcraft`, faq-template.md:128) — post-rename, the
   old-path redirect is unverified per CLAUDE.md.
9. Run buttons attach to shell-tagged fences; fences don't wrap in the app
   (plugin-behaviour.md:145-151, :172-173) — the fencing rules rest on these.
10. migrate-checklist.md:122-131's "passed cleanly" validation stamp cites host
    1.15.0-test6, two-plus release lines old.

The remaining forty, condensed by domain: **App UI** — copy-selects-text
(self-corrected, retained as history, plugin-behaviour.md:147-151); viewer
code-mode flip + stale snapshots (:255-257); Editor field unread (:293-295,
faq-template.md:27); Claude Code's own `plan` command owning the bare name
(faq-template.md:365-373); usage bar visible to user not Claude
(faq-template.md:154); commit-msg permission popup was the method's own gate
(done.md:710-715). **Harness mechanics** — read tool caps large files
(plugin-behaviour.md:452-459; plan.md:125-128); PowerShell here-string
column-0 constraint → `git commit -F` (done.md:700-704);
`${CLAUDE_PLUGIN_ROOT}` runtime resolution (all SKILL.mds, hooks.json,
setup.md); queue-lint parse surface and what it ignores
(plugin-behaviour.md:832-836 — see B14); scope-lock exact-path matching
(next.md:219-226 — see B11/finding sets); planning gate ask-never-deny
(plan.md:18-24; faq-template.md:255-263); _build.md self-editability citing the
hook's denial text (next-build.md:176-183); Processed-insert lint backstop
(next.md:251-253 — see B13); subagent gate prompts (hooks.json:2 — see B2);
hash backfill at next session start, mechanical token match (done.md:276-279,
:404-410, :631-635); Blocked-by lint (plugin-behaviour.md:1090-1091;
faq-template.md:75); .si-version update detection (setup.md:287-289); build
stamp exists but no docs-b doc consumes it (faq-template.md:140-142); leftover
working-file resume detection (faq-template.md:146, :208, :212); the
"developing the method itself?" question's landing place unconfirmed in scope
(faq-template.md:379-385 — see B5); shell-write detection honest-limits
(faq-template.md:467-477); `.throughliner/` editing-state contract incl. ~30s
staleness, absolute paths, safe deletion (setup.md:296-301;
faq-template.md:525-533) — a third-party contract other software consumes;
catch-up moved to /plan (faq-template.md:419-429; plan.md:147-154).
**Git/GitHub/CLI** — Watch→Releases notification flow (faq-template.md:130-132);
`gh repo view` visibility detection (setup.md:389-395; CLAUDE-TEMPLATE.md:64);
author-email stamping + noreply + history-rewrite-only fix (setup.md:400-410;
faq-template.md:55); commits forever despite deletion
(plugin-behaviour.md:1184-1186, :1250-1254; faq-template.md:53, :65, :349);
gitignore vs already-tracked files, `git rm --cached` (setup.md:258-265); /bug
routes to Anthropic; flintcraft.tech/report is a single text box; gh can post
issues (plugin-behaviour.md:1703-1743; faq-template.md:309-315). **Model
behaviour** — newer models want less spelled out (faq-template.md:43-47);
intent-recovery confabulation (plugin-behaviour.md:1505-1514;
done-build.md:78-88); short affirmatives bind to the most recent ask
(plugin-behaviour.md:100-108); Claude models are shelf-happy
(plugin-behaviour.md:1339-1340). **External tools** — the standard-generator
list (plugin-behaviour.md:549-557; plan.md:587-591); sandbox diagnosis's three
external URLs (faq-template.md:503).

---

**Method note.** Passes: (1) stale references, (2) cross-doc pointer integrity
(~52 pointers clean, 11 flagged), (3) duplicate statements, (4) multi-site
rules, (5) premise-bearing claims, (6) direct contradictions, (7) orphan
rules/files, (8) terminology drift, (9) hooks vs docs (both directions), (10)
retirement completeness. Healthy patterns worth noting from the clean side: the
[user] lifecycle is the best-maintained multi-site rule in the corpus; the
set-aside marker, downstream-action test, CLI-before-GUI pair, and dependency
two-routes rule are consistent at every site; the queue lint, scope-lock
permitted set, docset layering, and hash-backfill rules all match their code.
