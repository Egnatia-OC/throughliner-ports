# BACKLOG — Dev-side

Batch-by-batch roadmap for the plugin migration. Companion to `INVENTORY.md` and the Opus feasibility response (`claude-code-plugin-feasibility-response.md`).

## Versioning convention

Batches tracked as git tags (`v17`, `v18`, …). The method footer (`*No-code method — Version N.*`) only bumps on substantive method/plugin changes — dev-internal batches leave it unchanged. Full rule: `session-protocol.md` → *Three numbers to keep distinct*.

Scope files: `scopes/NNNN-kebab-title.md`. Allocation: next unused 4-digit number by scanning `planning/scopes/`. Numbers never reused or renumbered; reorder by moving rows below, not renaming files. Files are PROVISIONAL — a file existing isn't a commitment.

## The batch list

| # | Batch | Output |
|---|---|---|
| V18 | Plugin scaffold + SessionStart hook | Path block in fenced JSON; plugin skeleton; SessionStart installed. **Shipped v18.** |
| V19 | PreToolUse lock + templates + `/init-project` + Fold-ins | Lock enforcement; templates scaffolded by skill-command; fold-ins section. **Shipped v19.** |
| V20 | Reference manual promotion; parity audit | Reference manual current; parity rule extended. **Shipped v20.** |
| V21 | SessionStart — foundational reads + routing | State summary, template detection, resume detection, routing. **Shipped v21.** |
| V22 | Planning subagent + Serves-line hook | Planning loop end-to-end; tested. **Shipped v22.** |
| V23 | Remove Cowork mentions | Claude Code becomes explicit required tool. **Shipped v23.** |
| V24 | BUILD-METHOD + TEST-LOG creation | Dev-internal working manual and test record. **Shipped v24.** |
| V25 | Before-build + batch-executor + Stop hook | Build orchestration core; batch-sizing principle. **Shipped v25.** |
| V26 | TEST-LOG mechanism + V25 bugfixes + Drafts convention | 8-column TEST-LOG spec, V25 bugfixes, drafts-in-flight. **Shipped v26.** |
| V27 | After-build subagent | MANIFEST auto-update, recap, test-confirmation gate. **Shipped v27.** |
| V28 | V27 fix sweep | TEST-LOG writable, Stop-hook TEST-LOG-aware, shared helpers extracted. **Shipped v28.** |
| V29 | Safety net + unified `/adopt` | Unadopted-folder detection + PreToolUse enforcement; five-case `/adopt`. **Shipped v29.** |
| V30 | DOC-STRUCTURE migration + Reference manual coherence | Schema content into plugin; Reference manual rewrite. **Shipped v30.** |
| V31 | Planning — rescope OPEN-QUESTIONS | Four entries promoted to sessions. **Shipped v31.** |
| V32 | NO-CODE-METHOD.md retirement | Original method files retired or pointed at plugin. **Shipped v32.** |
| V33 | Consumer audit trail + frame-correction sweep | Consumer BUILD-LOG, planning/drafts/, frame-correction sweep. **Shipped v33.** |
| V34 | Consumer git workflow | Tag-and-push habit + git safety-guard hook. **Shipped v34.** |
| V35 | E2E Taskflow test | First real-project plugin run; validated adopt cases 1+4. **Shipped v35.** |
| V36 | Doc-only: TEST-LOG ordering, planning authority, plan-panel research | Three bundled doc fixes. **Shipped v36.** |
| V37 | Marketplace.json + local install | Marketplace packaging; first non-`--plugin-dir` smoke test. **Shipped v37.** |
| V38 | Locked-doc edit rules + Sonnet-search | Footer-stamp carve-out, proposed-edit mechanism, Sonnet-search discipline. **Shipped v38.** |
| V39 | MANIFEST paths + read-before-edit gate | Paths field + Shape B PreToolUse enforcement. **Shipped v39.** |
| V40 | Shelve the two-write rule | Repo-root docs frozen at V39; plugin side becomes sole source. **Shipped v40.** |
| v41 | Planning — rescope OPEN-QUESTIONS | Three entries scoped into V45/V46/V47. **Shipped v41.** |
| v42 | Git-diff drift detection | New drift check 1: direct-edit detection via git-diff + per-file confirmation. **Shipped v42.** |
| V43 | Permission-mode UX harmonization | Mode-aware deny messages, two-layer preamble, Reference manual section. **Shipped v43.** |
| V44 | /setup UX + per-project opt-out | Marker architecture removed; `/adopt` → `/setup`; 3 UX friction items resolved. **Shipped v44.** |
| V45 | Distributed fold-ins + BACKLOG open-questions + Inputs line | Fold-ins in destination docs; open-questions section; Inputs line; fold-in carve-out. **Shipped v47.** |
| V46 | BACKLOG.md PostToolUse validation | PostToolUse parse validation after BACKLOG edits. **Shipped v48.** |
| V47 | Vocabulary sweep / non-GUI generalisation | "Observable behaviours" generalisation; planning/plan-mode disambiguation. **Shipped v49.** |
| V48 | Test split + non-UI test types | Four test types, Claude/User verifier, 10-column TEST-LOG, after-build commit/tag. **Shipped v50.** |
| V49 | Consumer-batch structure overhaul | Five scope-context sections + Changes: delimiter + red-flag marker. **Shipped v51.** |
| V50 | ADR-style numbering + per-batch file-split | NNNN-kebab-title format; BACKLOG/ folder; allocate_number.py. **Shipped v52.** |
| V51 | Research folder + Sonnet-search reword | `/setup` scaffolds research/; agent researches directly. **Shipped v53.** |
| V52 | BUILD-LOG restructuring | build-log/ folder with per-build files + INDEX.md. **Shipped v54.** |
| V53 | Automated test suite | pytest suite at tests/; 124 tests. Dev-internal, no footer bump. **Shipped v55.** |
| V54 | Validation + warnings bundle | Serves-DOC validation, red-flags warning, aging detection, PROPOSED EDIT rename. **Shipped v56.** |
| V55 | New hook events (compaction guard + opener routing) | PreCompact blocks mid-build compaction; UserPromptSubmit classifies opener. **Shipped v57.** |
| V56 | TEST-LOG row pruning | Planning subagent deletes orphaned-component rows before drift checks. **Shipped v58.** |
| V57 | Subagent rule-loading convergence | Batch-executor converged on read-spec-on-entry pattern. **Shipped v59.** |
| V58 | Session performance tracking | Structured Performance section in build-log entries. **Shipped v60.** |
| 0060 | Taskflow E2E prep and testing | First real E2E since V35; partial — remaining coverage deferred to 0068. **Parked.** |
| 0063 | Subagent efficiency pass | Classify before loading; doc-first ordering; no inner agents. **Shipped v62.** |
| 0064 | /setup case 4 completion | BUILD-LOG folder migration + batch stub quality. **Shipped v63.** |
| 0065 | Project-boundary PreToolUse hook | Block Edit/Write/MultiEdit outside project root. **Shipped v64.** |
| 0066 | Permission prompt surface audit | Glob-based allocation replaces Bash calls; Auto mode recommended. **Shipped v66.** |
| 0067 | Desktop app install/update docs | Desktop-app procedures in Reference manual. **Shipped v67.** |
| 0068 | Taskflow E2E round 2 | Full build cycle against Taskflow with 0063–0067 fixes. Skills migration. **Shipped v71.** |
| 0069 | BACKLOG batch status tracking | Status: line (active/queued/parked/shipped) + parser + subagent transitions. **Shipped v70.** |
| 0061 | Rename "Crash course" to "Reference manual" | Rename + update all references. Frees name for HTML guide. **Shipped v68.** |
| 0062 | HTML Crash Course guide | Multi-page HTML guide for testers/early adopters. Depends on 0061. **Shipped v69.** |
| 0070 | After-build close completeness | Doc-parity audit, idea sweep with routing, pre-commit checkpoint, CLAUDE.md extensibility section. **Shipped v72.** |
| 0071 | Subagent cost optimization | Planning subagent from ~31.6k to <15k tokens: conditional drift-check skip, classify-then-dispatch, Sonnet evaluation. **Shipped v73.** |
| 0072 | After-build source-code boundary | Hard boundary: after-build cannot edit source/build files. Fold in "run commands yourself" rule. **Shipped v74.** |
| 0073 | ~~Stop hook before-build→build chain fix~~ | **Cancelled.** Superseded by architecture redesign — auto-chaining removed entirely. |
| 0074 | Session-open status summary | User-facing batch counts, next batch, pending tests — mandatory presentation via hook directive. **Shipped v75.** |
| 0075 | Dev-side log folder migration | BUILD-LOG.md + TEST-LOG.md → build-log/ + test-log/ folder structures. Dev-side only, no plugin changes. **Shipped v76.** |
| 0076 | ~~Plugin-side TEST-LOG folder migration~~ | **Cancelled.** Superseded by 0090. Original scoped against subagent architecture. |
| 0077 | ~~Greenfield E2E: burner app from scratch~~ | **Cancelled.** Intent kept — rewrite as new scope after architecture redesign lands. |
| 0078 | ~~Post-fix E2E validation (Taskflow)~~ | **Cancelled.** Validates 0073/0074 in old architecture; 0072 already shipped. Nothing left to validate. |
| 0079 | Subagent removal: code and procedures | Remove all 5 subagents. Convert to procedure docs. Delete Stop hook. Rewrite session_start/PreToolUse/skills to route to docs instead of spawning agents. **Shipped v77.** |
| 0080 | Doc permission flip: phase-aware editing | Unlock source-of-truth docs (UX, MANIFEST, additional) during planning. Lock source code during planning. Reverse during build. Phase detected via BACKLOG batch status. Depends on 0079. **Shipped v78.** |
| 0084 | Greenfield E2E: post-redesign full cycle | Planning-phase E2E of procedure-doc architecture. /setup works when invoked; Claude ignores routing hint for uninformed users; build transition opaque. **Shipped v79.** |
| 0081 | Proxy format and companion proxies | Proxy format spec + companion proxies for UX, MANIFEST, TEST-LOG, research. Session A of three-way split (0081/0089/0090). Depends on 0079, 0080. **Shipped v81.** |
| 0082 | CLAUDE template product overview | Product overview section in CLAUDE.md: what it is, who it's for, what friction it solves, milestones. Populated by `/setup` conversation. Depends on 0079, 0080. **Shipped v82.** |
| 0083 | Gemini search MCP server | `/research` skill + query-file template + proactive-search rule. Reuses existing MCP server; plugin provides discipline wrapper. **Shipped v83.** |
| 0085 | First-time user experience | /setup enforcement in PreToolUse deny + build-transition UX in before-build procedure + parent-directory CLAUDE.md inheritance advisory. Depends on 0084. **Shipped v84.** |
| 0086 | Scaffold quality fixes | [Project Name] replacement, UX principle capture, Status: line, marketplace.json description. **Shipped v85.** |
| 0087 | Doc folder restructure | Move spine docs into dedicated subfolder. Large surface area. Depends on 0085, 0086. **Shipped v86.** |
| 0096 | Manifest rationale field | One-line "why it exists" on MANIFEST entries; eliminates build-log scanning for decision context. |
| 0088 | Build E2E test | Build-phase E2E: /before-build through /build through after-build. Picks up from 0084. Depends on 0085 soft. |
| 0089 | INDEX relocation to proxies | Move BACKLOG INDEX.md and build-log INDEX.md content into `_method/proxies/`. Folders keep only per-entry files. Depends on 0081. **Shipped v88.** |
| 0090 | TEST-LOG folder split + proxy index | Split TEST-LOG.md into test-log/ folder; `_method/proxies/test-log.md` becomes folder index. Supersedes 0076. Depends on 0081, 0089. **Shipped v89.** |
| 0091 | Dev-side terminology and BACKLOG alignment | Rename PLAN.md→BACKLOG.md, planning/sessions/→planning/scopes/, merge OPEN-QUESTIONS into BACKLOG. Dev-internal only. **Shipped v87.** |
| 0092 | BUILD-METHOD split and dev-side proxies | Split BUILD-METHOD into protocol + reference; adopt .proxies/. Depends on 0091. **Shipped v90.** |
| 0093 | Dev-side folder restructure | Move all dev-side content into `dev/`; delete frozen V39 docs and `plugin.zip`. Depends on 0091 (shipped). |
| 0094 | Guided testing and debugging procedure | New `/test` skill + procedure doc. Step-by-step test walkthroughs for non-coders + structured debugging when tests fail. Depends on 0079 (shipped). |
| 0095 | /test skill E2E validation | E2E test of `/test` skill against burner app. Happy path, deliberate failures, debugging protocol, planning handoff. Depends on 0094. |
| V60+ | Remaining parked open questions | Graduation (indefinitely shelved). Prose-only rewrite (indefinitely parked). |

60 batches through 0078, plus V60+ TBD. Three cancelled (0073, 0077, 0078), one superseded (0076 → 0090). New scope files for the post-redesign phase follow.

## Scope file shape

Each `scopes/NNNN-kebab-title.md` follows this shape:

```markdown
# NNNN — [Batch Name]

## Goal
[One paragraph: what this batch produces.]

## Inputs
[Docs/files the batch reads / depends on.]

## Outputs
[New files, edited files, plugin components.]

## Success criteria
[How we know the batch succeeded.]

## Open questions for this batch
[Open design questions to resolve.]

## Risks / dependencies
[What could derail this. Dependencies on prior batches.]
```

## Open questions

Method-level questions not yet ready to be a batch. Each stays until resolved — folded into a batch's scope, promoted to its own batch, or dropped with a reason in `build-log/`. Newest first. Removed when resolved. Every entry carries a `**Surfaced.**` line with the session tag when it was created, so planning can detect neglected entries.

---

### Session close as a `/close` skill

**Surfaced.** v90 (post-session discussion).

**The question.** The 10-step session close procedure (session-protocol.md) is the most failure-prone part of the method. Claude follows it from memory after reading a document — steps get skipped under context pressure, build-log entries get missed, uncommitted work from prior sessions gets ignored. Should session close become a `/close` skill that mechanically walks the checklist?

**Why it matters.** Alex identified a pattern across multiple sessions where each Claude "acts like a separate person" — committing only its own files and ignoring orphaned work. The 10-step close is exactly the kind of procedural work skills were designed for — named action, loaded procedure, mechanical execution. A `/close` skill would enforce the full checklist including a `git status` sweep for all uncommitted work, not just the current scope's files.

**Working notes.** Design questions: which of the 10 steps survive if the rigid cycle loosens? Does `/close` own the commit, or does the user commit independently? Should it include a `git status` check for all uncommitted work? Does the build-log entry step stay mandatory or become optional?

**Next step.** Design session needed. Depends on resolving the broader build-cycle rigidity question — which close steps are genuinely load-bearing vs. ceremony.

---

### Planning as a `/plan` skill

**Surfaced.** v90 (post-session discussion).

**The question.** Planning is the only core workflow with no skill entry point. `/build`, `/before-build`, `/setup`, and `/research` are all invocable skills. Planning depends entirely on the rigid session lifecycle and procedural documentation. Should planning become a `/plan` skill that produces structured plans — the core competency scope files currently deliver (goal, inputs, outputs, success criteria, risks)?

**Why it matters.** Alex identified scope files as the beating heart of the project — Claude's ability to take vague intent and organize it into a structured plan is the core value for non-coders. Currently this happens only within the rigid session lifecycle. Consumer projects don't get scope files at all; `/before-build` does a narrower version (file list + verification burden) without the full planning structure. A `/plan` skill would make this competency independently accessible. Relates to Claude Code's native plan mode, which covers "how to approach this work" but not "what to work on next and why."

**Working notes.** Design questions: does `/plan` produce scope-file-format output, something lighter, or adapt to context? Does it write to BACKLOG automatically? How does it interact with Claude Code's native plan mode? See also OQ "Scope file split" — related but distinct (that's about format; this is about mechanism).

**Next step.** Design session needed. Cross-reference "Scope file split" OQ and "/close skill" OQ.

---

### Merge `/before-build` into `/build`

**Surfaced.** v90 (post-session discussion).

**The question.** From the user's perspective, `/before-build` and `/build` are one action — "I want to build something." The separation is an implementation detail: `/before-build` locks the file list so hooks know what's in bounds, then `/build` does the work. Should `/build` absorb `/before-build`'s steps internally, running them first if they haven't been done?

**Why it matters.** Alex asked why before-build is a separate skill from build. A user shouldn't need to know about batch file-list locking as a prerequisite step. The two-command sequence adds friction and conceptual overhead for non-coders.

**Working notes.** The hooks don't care which skill triggered the BACKLOG state — they gate on the Files: list existing, not on which command wrote it. If `/build` runs before-build internally, the same writes happen and enforcement works identically. Design question: is there ever a reason to run `/before-build` without immediately building? If not, the merge is clean.

**Next step.** Design session needed. Lower priority than `/close` and `/plan` — this is a UX simplification, not a missing capability.

---

### Scope file split: separate planning content from build content

**Surfaced.** v86 (0091 design discussion).

**The question.** Should the current scope file — which bundles planning-phase content (open questions, risks, dependencies, design decisions) with build-phase content (goal, outputs, success criteria, file lists) — be split into two artifacts? And should "build cycle" retire as a term, since it makes the whole workflow too synonymous with its second phase when planning is its own whole thing?

**Why it matters.** Alex has proven that planning and building can happen in separate parallel sessions (so long as you never build in parallel, and you inform the current build when a new plan lands). The bundled scope file pushes users toward a one-session-does-everything pattern that isn't required. Splitting would also clarify the terminology: the planning artifact and the build spec would each have a natural name without forcing a single term to cover both.

**Working notes.** Parallel planning/building needs git advice: commit before switching contexts, pull before resuming a build. The corruption risk is parallel builds, not parallel planning. The split would reshape plugin-side procedure docs — not just dev-side folder names.

**Next step.** 0091 shipped (v87) — terminology settled, folder is `planning/scopes/`. Still parked: promote when a concrete split design emerges (separate planning artifact vs. build spec).

---

### Remove timestamps from build-log and other docs

**Surfaced.** v82.

**The question.** Should timestamps be removed from build-log entries and any other method docs that carry them? The performance tracking section (shipped V58/v60) added structured timestamps to per-build log files. No clear use case for the timestamp data has emerged — session tags already provide ordering, and the method doesn't use elapsed-time data for any decision.

**Why it matters.** Timestamps add visual noise and token cost without serving a downstream consumer. If nothing reads them or acts on them, they're dead weight in every build-log entry going forward.

**Next step.** Audit which docs carry timestamps (build-log entry template, performance section shape, any others). Write a small scope to remove them from templates and procedure docs, or fold into a nearby batch touching build-log structure (0089).

---

### Bulk-tersify skill for doc compression

**Surfaced.** v82 (2026-05-25 ideation).

**The question.** Should the plugin include a `/tersify` (or similar) skill that rewrites method docs to be shorter without losing meaning — reducing token cost when Claude reads them at session open?

**Why it matters.** Every token in a method doc competes with working context. Docs accumulate detail over many sessions — each addition is justified, but the aggregate grows past what the content warrants. A non-coder can't confidently trim procedural docs they didn't write. A skill that systematically shortens prose while preserving every rule, constraint, and procedure would directly reduce the context-bloat problem the plugin exists to solve.

**Working notes.** Candidate targets: procedure docs (`plugin/docs/procedures/`), DOC-STRUCTURE.md, VOCABULARY.md, universal-behaviour.md, Reference manual. Scope-file and build-log templates could also benefit. The skill would need a diff-review step — show the user what changed and what was cut before committing, since "shorter" and "same meaning" are judgment calls. Could run against one file at a time or batch a folder. Planning-phase only (docs are unlocked).

**Next step.** Park until after the proxy layer and doc-folder restructure (0087) ship. Both will change which docs exist and where they live — tersifying before that wastes effort on files about to move or merge.

---

### Lost-feature sweep as a planning skill

**Surfaced.** v82 (2026-05-25 ideation).

**The question.** Should the plugin include a `/sweep` (or similar) skill that systematically scans cancelled batches, parked scope files, open question entries with stale rationale, and build-log "carried forward" items — surfacing features that were dropped, deferred under conditions nobody re-evaluated, or promised but never scoped?

**Why it matters.** Surfaced 2026-05-25 during an ideation session that manually did exactly this. The process — read BACKLOG for cancelled/parked rows, read their scope files, cross-reference build-log "carried forward" sections, check OQ parking rationale against what's shipped since — is mechanical enough to be a repeatable procedure. Doing it by hand took significant context window and required knowing where to look. A planning-phase skill could run this as a pre-flight before roadmap rescoping, catching items that silently fell off the map.

**Working notes.** The sweep found six items across ~65 batches: one genuinely lost output (after-build proxy regeneration), one partially shipped remainder with no home (UX threat-class marker), one undocumented constraint (parent-directory inheritance), and three items frozen under stale rationale. The pattern: cancellation and parking are one-way — nothing triggers a re-evaluation when the reason for parking stops being true.

**Next step.** Park until the planning procedure stabilises post-proxy-layer. The sweep reads BACKLOG, scope files, build-log entries, and open questions — all of which are changing shape through 0089/0090. Promote once those ship and the doc structure is stable.

---

### Project-boundary hook bypass via Bash

**Surfaced.** v73.

**The question.** The project-boundary PreToolUse hook (0065) blocks `Edit`/`Write`/`MultiEdit` outside the project root, but `Bash` commands (`sed`, `echo >`, PowerShell `Set-Content`, etc.) bypass it entirely. Should the plugin add a Bash-matcher PreToolUse check for common file-write patterns, similar to how the git safety guard matches `git reset --hard` and `git push --force`?

**Why it matters.** Surfaced 2026-05-25 during v73 session close. Claude used `sed` to edit a file outside `sovereign-implementer/` after the Edit tool was correctly blocked. The boundary enforcement is advisory (catches normal editing flow), not hermetic (can't prevent Bash-based writes). A careless or drifting Claude session could write outside the project without the hook ever firing. The git safety guard already demonstrates the pattern — match dangerous Bash substrings and deny — but file-write patterns are far more varied than git commands, so false positives are a real concern.

**Working notes.** Common file-write patterns that could be matched: `sed -i`, `> file`, `>> file`, `tee`, `Set-Content`, `Out-File`, `Add-Content`, `cp`, `mv`. But every match risks blocking legitimate in-project Bash use. An alternative: instead of blocking, surface a warning via `additionalContext` when Bash targets a path outside the project root — advisory rather than deny.

**Next step.** Park. Revisit if E2E testing or real-world use surfaces unintended cross-project writes from Bash. The advisory-warning approach is lower-risk than a hard deny if this gets promoted.

---

### Structured-markdown validator as a plugin component

**Surfaced.** v71 (0068 E2E round 2).

**The question.** Should the plugin include a general-purpose structured-markdown linter that validates BACKLOG batch format, TEST-LOG column counts, scope-context section completeness, and other method-specific document shapes — beyond what `parse_backlog.py` currently does?

**Why it matters.** Surfaced 2026-05-24 during E2E testing research. `parse_backlog.py` validates BACKLOG structure, but TEST-LOG, build-log entries, and scope-context sections have no equivalent validation. Malformed docs cause silent failures downstream (hooks gate on wrong data). A general lint could run as a PostToolUse check or a planning-session pre-flight.

**Next step.** Promote after the proxy layer ships (0081/0089/0090). Proxies add another structured format with specific shape requirements — validation becomes more valuable as the number of structured doc types grows.

---

### Plugin testing framework beyond bespoke pytest

**Surfaced.** v71 (0068 E2E round 2).

**The question.** Should the project invest in a reusable plugin testing framework — run a hook against synthetic input and assert on output shape/content, without a full Claude Code session — or is the current bespoke pytest suite sufficient?

**Why it matters.** Surfaced 2026-05-24 during E2E testing research. The pytest suite at `tests/` covers hook subprocess tests and unit tests, but it's custom-built for this project. A framework could make it easier to add tests for new hooks, validate prompts, and regression-test deny/allow paths. Counter-argument: the bespoke suite works, runs in under 5 seconds, and covers 124 tests — a framework might add abstraction without proportional value.

**Next step.** Park. Revisit if test maintenance burden grows or if other plugin projects would benefit from the same patterns.

---

### Plugin settings layer / per-project config file

**Surfaced.** v71 (0068 E2E round 2).

**The question.** Should the plugin support a separate config file (or settings layer) that lets users override or extend plugin-owned workflows — as opposed to using CLAUDE.md sections for extensibility?

**Why it matters.** Surfaced 2026-05-24. CLAUDE.md is already the per-project customization point, so a recognised section there is the simpler path. A separate config file would be a new mechanism to maintain. Worth revisiting if CLAUDE.md extensibility proves insufficient.

**Next step.** Parked. Revisit if the CLAUDE.md-section approach ships and users hit limits.

---

### Red-flag / threat-class marker for security-shaped batches

**Surfaced.** v43.

**The question.** Should BACKLOG batches touching security surfaces (auth, secrets, PII, deletion, payment) carry an explicit *Red flags* marker — as a batch sub-section, as auto-detection, or both?

**What shipped.** Batch-level Red flags sub-section shipped V47 (v51) — planning auto-detects security-shaped scope and writes a persistent section.

**What remains.** Threat-class marker on individual UX.md entries — so security-shaped features are flagged at the spec level, not just at the batch level.

**Next step.** Ready to promote. Could fold into a planning or UX-template batch, or stand alone as a small scope.

---

### Graduate sovereign implementer onto sovereign implementer

**Surfaced.** v40.

**The question.** Can this dev project dogfood the method's own plugin?

**Why it matters.** Surfaced 2026-05-21. Dogfooding would surface gaps Taskflow can't and validate non-UI project types.

**Prerequisites (all shipped):**

1. Distributed fold-ins + open questions — **Shipped V43.**
2. Automated vs. manual test split — **Shipped V46.**
3. Two-write rule shelved — **Done v40.**
4. UX.md non-GUI adaptation — **Shipped V47.**

**Next step.** **Indefinitely shelved** (v61). All prerequisites shipped, but E2E testing revealed efficiency/correctness fixes needed (0063–0068). Restore when the method is stable enough to dogfood without excessive token burn.

---

### Prose-only rewrite of the method

**Surfaced.** v23.

**The question.** Tool-agnostic prose-only version for users without Claude Code.

**V37 note:** V32's two-write rule delivered the docs-only set at repo root. V40 froze it at V39.

**Next step.** **Indefinitely parked** (v47). Promote if a real audience emerges.
