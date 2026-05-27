# BACKLOG — Dev-side

Batch-by-batch roadmap for the plugin migration. Companion to `Dev/INVENTORY.md`.

## Versioning convention

Batches tracked as git tags (`v17`, `v18`, …). The method footer (`*No-code method — Version N.*`) only bumps on substantive method/plugin changes — dev-internal batches leave it unchanged. Full rule: `session-protocol.md` → *Three numbers to keep distinct*.

Queued batches live inline in the *Queued batches* section below the shipped-batch table. Each batch heading carries a 4-digit number (e.g. `### 0096 — Manifest rationale field`). Allocation: next unused number. Numbers never reused; reorder by moving sections, not renumbering.

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
| 0089 | INDEX relocation to proxies | Move BACKLOG INDEX.md and build-log INDEX.md content into `_method/proxies/`. Folders keep only per-entry files. Depends on 0081. **Shipped v88.** |
| 0090 | TEST-LOG folder split + proxy index | Split TEST-LOG.md into test-log/ folder; `_method/proxies/test-log.md` becomes folder index. Supersedes 0076. Depends on 0081, 0089. **Shipped v89.** |
| 0091 | Dev-side terminology and BACKLOG alignment | Rename PLAN.md→BACKLOG.md, planning/sessions/→planning/scopes/, merge OPEN-QUESTIONS into BACKLOG. Dev-internal only. **Shipped v87.** |
| 0092 | BUILD-METHOD split and dev-side proxies | Split BUILD-METHOD into protocol + reference; adopt .proxies/. Depends on 0091. **Shipped v90.** |
| 0093 | Dev-side folder restructure | All dev-side content into `Dev/`, product docs into `Guides/`. Manual execution with different design choices from spec. **Shipped v96.** |

| 0102 | Dev-side session-close convergence | Proxy regen close step + response-shape tags on session-protocol.md close steps. Dev-internal only. |
| 0101 | Structured-markdown validator | PostToolUse validation for TEST-LOG, build-log, scope-context, proxies. Warn on malformed shapes. |
| 0100 | Bash write-guard + skill escape guidance | Bash-matcher PreToolUse for file-write commands; escape guidance on all write-lock denies. |
| 0099 | /sovrecap + /sovbuild rename + lock-timing fix | Rename before-build→sovrecap, build→sovbuild; Status: active delayed to post-confirmation. **Shipped v95.** |
| 0096 | Manifest rationale field | Inline italic rationale suffix on MANIFEST entries; close procedure writes it; planning checks it before UX edits. **Shipped v97.** |
| 0098 | /sovplan skill + ordering principles + [SECURITY] marker | Planning skill wrapping planning.md; ordering principles; SessionStart top-3 summary; universal `[SECURITY]` marker. **Shipped v96.** |
| 0097 | /sovclose + /sovgit + after-build retirement | Close skill (dual-path), git skill, after-build.md absorbed. **Shipped v94.** |
| 0103 | /tersify skill for doc compression | Guided triage + audit for reducing token cost in SOT docs. Planning-phase only. **Shipped v98.** |
| 0102 | Dev-side session-close convergence | Proxy regen close step + response-shape tags on session-protocol.md close steps. Dev-internal only. **Shipped v99.** |
| 0094 | Guided testing and debugging procedure | `/test` skill + `testing.md` procedure doc. User-verified walkthrough, direct TEST-LOG recording, structured debugging. **Shipped v100.** |

Shipped/cancelled batches end here. Queued batches are below with full scope content — no separate scope files.

## Queued batches

Full scope for each queued batch lives inline here — no separate scope files. Read the whole section at session open; the batch you're working on has the context you need, and the other batches prevent you from duplicating or contradicting queued work.

---

### 0088 — Build E2E test

**Goal.** Test the build phase of the procedure-doc architecture. Picks up where 0084 left off — `/setup` and planning are validated, now test `/sovrecap` through `/sovbuild` through `/sovclose` in the Polite Fart Announcer burner app.

**Inputs.** `Dev/Resources/research/e2e-greenfield-post-redesign.md` ("What wasn't tested" section). Burner app at `C:\Users\Alex\Desktop\Polite Fart Announcer` (scaffolded from 0084).

**Outputs.** Updated research file with build-phase findings. New BACKLOG entries or open questions for any issues. Token cost baseline for procedure-doc architecture.

**Success criteria.** `/sovrecap` populates correctly (Files: and Tests: populated). `/sovbuild` sets Status: active and creates `index.html` — file exists and works in browser. `/sovclose` fires: MANIFEST updated, build-log entry written, TEST-LOG rows written. Phase-aware permissions work. Observations documented.

**Open questions.**
1. Can the existing burner session be reused, or does it need a fresh session?
2. If a fix session shipped between 0084 and this, re-test the fixed behaviour first.

**Risks / dependencies.** Soft dep on 0099 (skill names). Burner app may have stale state from 0084 testing (Status: active on a batch). May need status reset or fresh start.

---

### 0095 — /test skill E2E validation

**Goal.** End-to-end test of `/test` skill (shipped in 0094) against a real project. Validate the full flow: invoke after build, follow guided walkthrough, report failure, get debugging support.

**Inputs.** `/test` skill and `plugin/docs/procedures/testing.md` (from 0094). A burner app with pending TEST-LOG rows across multiple test types. `Dev/Resources/research/e2e-greenfield-post-redesign.md`.

**Outputs.** Research file `Dev/Resources/research/e2e-test-skill-validation.md`. New BACKLOG entries for issues. `/sovclose` handoff validation.

**Test plan.** Happy path: invoke `/test`, walk through Look-and-click and Run-and-read tests, report Pass, verify row updates. Failure path: report Fail, verify debugging protocol, verify routing to BACKLOG. Edge cases: no pending tests (graceful exit), mid-build invocation (rejected), partial progress on early stop. Handoff: confirm planning read-back handles rows `/test` already confirmed.

**Success criteria.** Non-coder completes full flow without independent knowledge. Debugging produces useful output on deliberate failure. TEST-LOG state after `/test` is consistent with planning expectations. No silent failures.

**Risks / dependencies.** Hard dep on 0094. Soft dep on 0088 (reuse app state). Risk: insufficient test-type variety in burner app.

---

### 0101 — Structured-markdown validator

**Goal.** Extend PostToolUse validation beyond BACKLOG to cover all structured method docs — TEST-LOG, build-log, scope-context sections, and proxies. Malformed docs cause silent downstream failures (hooks gate on wrong data, proxies become stale, TEST-LOG rows lose columns). A general validator catches shape violations at write time.

**Inputs.** `plugin/scripts/parse_backlog.py` (existing BACKLOG-specific parser — model for the pattern). `plugin/docs/DOC-STRUCTURE.md` (canonical shapes for all doc types). `plugin/hooks/post_tool_use.py` (current PostToolUse hook — BACKLOG validation only).

**Outputs.**
- `plugin/scripts/validate_docs.py` (or similar) — general-purpose validator covering: TEST-LOG column count (10 columns), build-log entry structure (required sections), scope-context section completeness (Goal/Outputs/Success criteria present), proxy format (HTML comment header, state summary, entries section). Callable from PostToolUse and as a standalone planning pre-flight.
- `plugin/hooks/post_tool_use.py` — updated to call the new validator after edits to TEST-LOG files, build-log files, BACKLOG batch files, and proxy files.
- Tests updated (validator unit tests, PostToolUse integration tests).

**Design decisions (v92).**
1. Separate script (`validate_docs.py`), not bolted onto `parse_backlog.py`. The BACKLOG parser is a data-extraction tool consumed by multiple hooks; the validator is a shape-checker. Different jobs.
2. PostToolUse is the primary trigger — validate at write time, same pattern as BACKLOG validation. Also usable as a planning pre-flight (standalone invocation).
3. Lenient on legacy formats — warn, don't block. Same philosophy as `parse_backlog.py`: malformed input produces a warning in `additionalContext`, not a hard deny. Claude sees the warning and can self-correct.
4. Validation rules derived from DOC-STRUCTURE.md — the spec is the source of truth for what "well-formed" means.

**Success criteria.** A TEST-LOG edit that drops a column triggers a PostToolUse warning. A build-log entry missing the Performance section triggers a warning. A proxy with a malformed HTML comment header triggers a warning. No false positives on well-formed docs. Existing `parse_backlog.py` validation unchanged.

**Risks / dependencies.** Scope creep — "validate all docs" can expand indefinitely. Cap at the four doc types above (TEST-LOG, build-log, scope-context, proxies). BACKLOG validation stays in `parse_backlog.py`. No hard dependencies; benefits from proxy layer (shipped) and folder structures (shipped).

---

### 0100 — Bash write-guard + skill escape guidance

**Goal.** Close the Bash bypass hole in PreToolUse enforcement. Currently `Edit`/`Write`/`MultiEdit` are gated by project-boundary and phase-aware locks, but Bash commands (`sed -i`, `> file`, `Set-Content`, etc.) bypass all of them. Add a Bash-matcher PreToolUse check that catches file-write patterns and applies the same rules. Separately, add escape guidance to every skill that induces write locks — so Claude tells users how to change phase via the correct skill instead of leaving them to reason around the lock.

**Outputs.**
- `plugin/hooks/pre_tool_use.py` — new Bash-matcher logic. On `Bash`/`PowerShell` tool calls, scan the command for file-write patterns. If the target path would be denied by existing rules (outside project root, or locked file in current phase), deny with the same `[No-code method]` message format and `What to do:` line.
- Deny messages for Bash write-guard include skill escape guidance: "To edit this file, invoke `/sovplan` to switch to planning phase" (or whichever skill unlocks the target).
- Skill escape guidance added to existing deny messages on `Edit`/`Write`/`MultiEdit` locks — not just Bash. Every deny that blocks a phase-aware edit names the skill that would unlock it.
- Tests updated (Bash-matcher unit tests, false-positive regression tests for legitimate in-project Bash use).

**Design decisions (v92).**
1. Advisory deny, not silent block — same `[No-code method]` format as existing denies. Claude sees the deny and the escape route.
2. Two threat surfaces: cross-project writes (Bash targeting paths outside project root) and phase-lock bypass (Bash editing locked files within project). Same matcher, same deny logic.
3. Pattern matching targets common file-write commands: `sed -i`, `>`, `>>`, `tee`, `Set-Content`, `Out-File`, `Add-Content`, `cp`, `mv`. Path extraction is best-effort — not hermetic, but catches the normal drift patterns.
4. False-positive mitigation: only fire when the extracted path would actually be denied by existing rules. Legitimate in-project Bash (e.g. `sed` on a file in the batch's Files: list during build) passes through.
5. Skill escape guidance on all write-lock denies (not just Bash): the deny message names which skill to invoke to change phase. This covers the case where Claude or the user tries to reason around a lock instead of using the method's own phase transitions.

**Success criteria.** `sed -i` targeting a file outside the project root is denied. `Set-Content` targeting a locked UX.md during build is denied. Legitimate in-project Bash during build passes. Every phase-lock deny message names the skill that would unlock the target. No false positives on standard build-time Bash (running dev servers, test commands, git operations).

**Risks / dependencies.** Bash command parsing is inherently fuzzy — complex piped commands, variable expansion, and heredocs may evade or false-positive the matcher. The git safety guard (0065) already demonstrates the pattern works for a constrained command set; file-write patterns are broader. Regression test suite essential. No hard dependencies on other queued batches, but benefits from 0097/0098/0099 shipping first (skill names in deny messages need to match).

---

## Open questions

Method-level questions not yet ready to be a batch. Each stays until resolved — folded into a batch's scope, promoted to its own batch, or dropped with a reason in `Dev/Planning/build-log/`. Newest first. Removed when resolved. Every entry carries a `**Surfaced.**` line with the session tag when it was created, so planning can detect neglected entries.

---

### Language setting for multi-language plugin support

**Surfaced.** v97 (2026-05-27 ideation).

**The question.** Should the plugin support a `language` setting in the consumer project's CLAUDE.md that tells skills, hooks, and procedure docs to work in the user's language instead of English?

**Why it matters.** The plugin targets non-coders, many of whom may not read English fluently. Claude already speaks dozens of languages — a lightweight setting (e.g. `Language: French` in CLAUDE.md) could instruct all skill/hook output to use that language without translating any plugin docs. The alternative — full locale folders with parallel doc trees — gives a polished experience but doubles maintenance per language. The design space includes: which layer reads the setting (skills only, hooks too, procedure docs?), whether templates scaffold in the target language, and whether the setting affects doc content or only Claude's responses.

**Next step.** Park until the plugin is stable enough for external testers. Likely surfaces naturally when a non-English-speaking tester tries the plugin.

**Design constraints surfaced (v97 ideation, 2026-05-27).** Robustness audit of the hook layer against non-English consumer projects. Two hard constraints identified:

1. **Git `core.quotepath` for non-ASCII filenames.** Drift check 1 (`planning.md` § direct-edit detection) tells Claude to run `git diff` and match output paths against the batch file list. Git's default escapes non-ASCII characters with octal notation (`créer` → `cr\303\251er`). That match happens in Claude's context window, not in Python hooks — `Path.resolve()` can't normalise it. Fix: `/setup` or `SessionStart` sets `git config --local core.quotepath false`. Without it, Claude would hit mangled paths and fire unnecessary confirmation prompts. Hooks themselves are safe — they resolve paths through `pathlib`, not git output. Path slash normalisation (forward vs. backslash) is also already handled via `Path.resolve()` on both sides of every comparison.

2. **Control tokens are English-only.** `Status:`, `Changes:`, `Serves UX.md:`, `Confirmed Explicitly:`, `[SECURITY]`, and every other metadata keyword the hooks regex-match must remain in English regardless of content language. A user translating `Status: active` to `Estado: activo` silently breaks phase enforcement — the parser returns empty, and the hook treats an active batch as nonexistent. The language setting (if built) must document this constraint explicitly, and `/setup` scaffolding should note it in the consumer CLAUDE.md.

**Source.** `Dev/Resources/research/ResearchFindingsMult (1).md` (§§ 3.1–3.3, 4.2). Hook audit confirmed path normalisation and encoding are handled; quotepath and control-token immutability are the two real gaps for internationalisation.

---

### UTF-8 BOM hardening for hook file reads

**Surfaced.** v97 (2026-05-27 ideation).

**The question.** Should the four `open()` / `read_text()` call sites in hooks switch from `encoding="utf-8"` to `encoding="utf-8-sig"` to strip Windows BOM bytes?

**Why it matters.** `safe_read_text()` in `project_state.py:323` and `session_start.py:216` uses `utf-8`. Two direct `open()` calls in `user_prompt_submit.py:82` and `pre_tool_use.py:820` also use `utf-8`. If a user hand-edits a spine file in a Windows editor that prepends a UTF-8 BOM (`\xef\xbb\xbf`), the BOM lands before the first character of line 1. Any regex matching `^Status:` or `^# ` on the first line fails silently — the hook sees `﻿Status:` instead. Claude Code itself writes BOM-free UTF-8, so the risk is only manual edits. Low probability but a one-line fix per site.

**Next step.** Low priority. Could fold into any batch touching hook file I/O, or ship as a standalone micro-batch.

---

### Pre-commit checkpoint as explicit checklist

**Surfaced.** v93 (2026-05-26 ideation).

**The question.** Should the dev-side pre-commit checkpoint (session-protocol.md step 6) name each artifact explicitly — like plugin-side close.md step 13 — instead of the current "verify steps 1–5 all done"?

**Why it matters.** The vague step is the one most likely skipped under context pressure. Plugin-side names each artifact (MANIFEST updated, TEST-LOG rows written, build-log entry written, idea sweep done, proxies regenerated, doc-parity done). Dev-side could name its equivalents (doc-parity done, frame-correction done, footers bumped if applicable, build-log entry written, idea sweep done, proxies regenerated).

**Next step.** Could fold into 0102 if it hasn't shipped, or a follow-on dev-side protocol polish batch.

---

### Idea sweep with explicit routing destinations

**Surfaced.** v93 (2026-05-26 ideation).

**The question.** Should the dev-side idea sweep (session-protocol.md step 5) enforce the plugin's three-way triage — every idea routed to exactly one of: BACKLOG batch, build-log "not pursued, reason: ...", or open question — instead of the current loose "sweep ideas raised but not implemented"?

**Why it matters.** Plugin-side close.md step 10 requires explicit routing so ideas don't slip through unrecorded. Dev-side step 5 has the same risk — ideas mentioned in chat but never routed to a durable location disappear at session end.

**Next step.** Could fold into 0102 if it hasn't shipped, or a follow-on dev-side protocol polish batch.

---

### Opener routing table for dev sessions

**Surfaced.** v93 (2026-05-26 ideation).

**The question.** Should session-protocol.md include a routing table mapping dev-session openers (planning, build, doc-only, ideation, E2E test) to what to load and what to skip — similar to plugin-side universal-behaviour.md § Routing openers?

**Why it matters.** Currently every dev session loads the same docs regardless of shape. An ideation session doesn't need full BACKLOG parsing; a doc-only session doesn't need test-log state. A routing table would reduce session-open token cost and give Claude clearer per-shape instructions.

**Next step.** Park until session-protocol stabilises after 0102 and 0093 ship. Both will change what's in the protocol and where it lives.

---

### Performance section in dev build-log entries

**Surfaced.** v93 (2026-05-26 ideation).

**The question.** Should dev build-log entries adopt the Performance section from plugin-side close.md (batch completion status, file count, carve-outs, test counts) — or is it unnecessary overhead for the dev project?

**Why it matters.** Consumer build-log entries track session efficiency. Dev sessions are less standardised but could still benefit from tracking token costs and session patterns over time, especially as the project approaches dogfooding.

**Next step.** Low priority. Park until dogfooding is closer or token-cost visibility becomes a pain point.

---

### Lost-feature sweep as a planning skill

**Surfaced.** v82 (2026-05-25 ideation).

**The question.** Should the plugin include a `/sweep` (or similar) skill that systematically scans cancelled batches, parked batches, open question entries with stale rationale, and build-log "carried forward" items — surfacing features that were dropped, deferred under conditions nobody re-evaluated, or promised but never scoped?

**Why it matters.** Surfaced 2026-05-25 during an ideation session that manually did exactly this. The process — read BACKLOG for cancelled/parked rows, read their scope files, cross-reference build-log "carried forward" sections, check OQ parking rationale against what's shipped since — is mechanical enough to be a repeatable procedure. Doing it by hand took significant context window and required knowing where to look. A planning-phase skill could run this as a pre-flight before roadmap rescoping, catching items that silently fell off the map.

**Working notes.** The sweep found six items across ~65 batches: one genuinely lost output (after-build proxy regeneration), one partially shipped remainder with no home (UX threat-class marker), one undocumented constraint (parent-directory inheritance), and three items frozen under stale rationale. The pattern: cancellation and parking are one-way — nothing triggers a re-evaluation when the reason for parking stops being true.

**Next step.** Park until the planning procedure stabilises. The sweep reads BACKLOG batches, build-log entries, and open questions. Promote once the doc structure is stable.

---

### Plugin testing framework beyond bespoke pytest

**Surfaced.** v71 (0068 E2E round 2).

**The question.** Should the project invest in a reusable plugin testing framework — run a hook against synthetic input and assert on output shape/content, without a full Claude Code session — or is the current bespoke pytest suite sufficient?

**Why it matters.** Surfaced 2026-05-24 during E2E testing research. The pytest suite at `Dev/Resources/tests/` covers hook subprocess tests and unit tests, but it's custom-built for this project. A framework could make it easier to add tests for new hooks, validate prompts, and regression-test deny/allow paths. Counter-argument: the bespoke suite works, runs in under 5 seconds, and covers 184 tests — a framework might add abstraction without proportional value.

**Next step.** Park. Revisit if test maintenance burden grows or if other plugin projects would benefit from the same patterns.


---

