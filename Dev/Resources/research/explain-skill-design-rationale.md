# Design rationale inventory — mined from build log

Phase 2 output: the "why" behind each of the 42 plugin features, extracted from build log entries.
Next step: use this to enrich crash course, reference manual, and UX.md, then build the /explain skill.

**Staleness key:** None = current. Low = concept current, minor details may have shifted. Medium = core idea current but implementation has evolved significantly. High = superseded.

---

## A. Workflow lifecycle

### 1. Session routing
**Why it exists:** Claude needs to know what kind of session the user is opening (setup, resume, test notes, bug report, etc.) so it can load the right procedure doc and skip irrelevant ceremony. Without routing, every session opens with generic preamble and the user must manually direct Claude.
**Key decisions:**
- UserPromptSubmit uses keyword-based first-prompt classification with conservative thresholds to avoid false positives
- Routing table is priority-ordered top-to-bottom, first matching row wins
- Bug reports route to `planning.md` (they produce BACKLOG items) rather than a dedicated procedure
- Three missing routes (bug reports, doc audits, method questions) added after a reader test showed a stranger-Claude wouldn't know what to do with them
- Output ordering: status summary → tripwire → routing (resolved competing "first output" claims)
**Staleness risk:** Low — v133 clarifications are very recent.
**Sources:** v57, v133

### 2. Phase detection
**Why it exists:** The plugin needs to flip editing permissions by phase — allowing doc edits during planning and locking them during build, and vice versa for source code. The original mechanism (parsing `Status: active` from BACKLOG) had a critical flaw: status is file-level state, so ALL concurrent sessions see the lock, not just the build session. This drove the redesign to file-existence detection (`_method/active-build.md` present = build phase).
**Key decisions:**
- MANIFEST stays writable during both phases (mirrors codebase state that changes during build)
- `research/` files exempt from planning-phase source lock (project docs, not source code)
- Read-before-edit gate and test-confirmation gate only fire during build (irrelevant when source code is already locked during planning)
**Staleness risk:** High for v78's original `Status: active` mechanism (superseded by file-existence). The *why* for phase detection itself is stable.
**Sources:** v78, v110

### 3. Editing surfaces (phase-aware locking)
**Why it exists:** Without phase-aware locking, Claude can edit anything at any time, leading to spec drift (editing source-of-truth docs during build without the proposed-edits protocol) or premature implementation (editing source code during planning before the spec is settled). PreToolUse enforces mechanically so docs don't need to carry the rule.
**Key decisions:**
- Planning-phase source lock and build-phase doc lock are two sides of the same coin, both in PreToolUse
- Footer exception allows version bumps on locked docs (metadata, not content)
- `[PROPOSED EDIT PENDING]` queues build-phase doc changes for user review rather than blocking entirely
**Staleness risk:** Low — concept stable; enforcement updated when phase detection shifted to file-existence.
**Sources:** v78, v110

### 4. Build snapshot
**Why it exists:** Extracting the active batch from BACKLOG into a separate file solves two problems: (1) unlocks BACKLOG for parallel sessions, (2) gives phase detection an unambiguous signal (file exists = build in progress) instead of parsing status fields.
**Key decisions:**
- `/sovbuild` extracts the batch; `/sovclose` deletes the snapshot (the build-log entry is the shipped record — v139 changed this from writing back)
- File existence is unambiguous phase detection, replacing `Status: active` parsing
- Snapshot shrinks after re-batching carve-outs
**Staleness risk:** Low — one detail stale: v112 said `/sovclose` writes back to BACKLOG, but v139 changed to delete-only.
**Sources:** v112

### 5. Close procedure (mandatory)
**Why it exists:** Without mandatory close, builds finish but leave orphaned state — active-build snapshots, unbumped footers, missing build-log entries, uncommitted work. Advisory close steps get skipped under context-window pressure. Making close mandatory and mechanically enforced prevents orphaned snapshots that block all future builds.
**Key decisions:**
- Dual-path: post-build (full 14-step quality gates) vs planning/general (lighter — idea sweep, proxy regen, git nudge)
- Skill-to-skill transitions use `[PROMPT]` nudges, never auto-handoff
- PreToolUse commit guard blocks `git commit` when all Files: ticked and close hasn't run; mid-build commits still allowed
- Commit-guard regex `\bgit\s+(?:-\S+\s+)*commit\b` chosen over simpler patterns to reduce false positives
- v139: lighter close expanded from 4 to 7 steps; `Status: shipped` removed; build-log entry is the shipped record
**Staleness risk:** Low — v139 is very recent and represents current state.
**Sources:** v62, v94, v132, v139

### 6. Session handoff
**Why it exists:** Claude has no visibility into its own context-window usage. During long builds, compaction can silently drop critical context. PreCompact blocks compaction during active builds and surfaces a handoff prompt instead, so the user can start a fresh session with full context.
**Key decisions:**
- PreCompact reframed from context-preservation to block+handoff (platform can't inject `additionalContext` from PreCompact)
- Three proxy signals for context pressure: pre-build sizing (8+ files AND open decisions), mid-session compact nudge (15+ exchanges), skill-handoff compact nudge
- Compound trigger (8+ files AND open decisions) — high file count with resolved decisions is normal; deliberation-heavy builds blow out
- Mid-session nudge placed in universal-behaviour.md (cross-cutting) not individual procedure docs
**Staleness risk:** Low.
**Sources:** v57, v116

---

## B. Planning & scoping

### 7. Planning procedure (`/sovplan`)
**Why it exists:** Planning needs to detect manual edits, catch drift between BACKLOG intent and file state, and provide ordering principles for batch sequencing. Drift checks run every session because skipping them would defeat manual-edit detection — the core threat is fold-ins silently left unapplied and direct edits going unnoticed.
**Key decisions:**
- Drift checks always run; no threshold or bulk-confirm (bulk-confirm is the failure mode that lets things slip through)
- Git-diff drift detection uses `git diff <last-tag>...HEAD`; files from previous batch pass silently, others trigger per-file confirmation walk
- Per-file walk is mandatory — no threshold
- Serves-line matching is case-insensitive exact, no fuzzy
- Three OQs combined into one batch when they touch the same doc section
**Staleness risk:** Low — drift-check logic migrated from subagent to procedure doc but rationale is current. The subagent itself was retired in v66.
**Sources:** v22, v31, v42

### 8. Before-build recap (`/sovrecap`)
**Why it exists:** A pre-build checkpoint that validates the upcoming batch before the user commits. The core insight: BACKLOG must remain editable during the recap so users can adjust file lists, test plans, and split proposals — locking it prematurely blocks productive conversation.
**Key decisions:**
- Before-build is validate-only (reorganise dropped — planning owns BACKLOG since V22)
- `/build` is argument-less — out-of-order execution handled by reordering BACKLOG, not passing batch IDs
- Lock timing: `Status: active` moved from recap to build's first action, keeping BACKLOG editable during discussion
- Procedure doc filenames kept as `before-build.md` despite skill rename to `/sovrecap` — renaming would break conventions for no user-facing benefit
**Staleness risk:** None.
**Sources:** v25, v95

### 9. Open-question deliberation (`/sovdeliberate`)
**Why it exists:** Open questions have a different lifecycle from build batches — non-blocking parking for things that need deliberation but shouldn't stall the build pipeline. The deliberation skill provides structured resolution: promote to batches, fold into existing batches, drop, or keep parked.
**Key decisions:**
- OQs coexist with batches but have different lifecycles (non-blocking vs blocking)
- Planning scans OQs every session for promotion triggers
- Batch lifecycle on completion: delete from BACKLOG at close, don't write back as "shipped" — nothing queries shipped status; build-log is the shipped signal
**Staleness risk:** Low — the OQ-as-parking rationale and disposition model are current.
**Sources:** v47, v91, v135

### 10. Ideation (`/sovideate`)
**Why it exists:** Ideation generates new batches and surfaces open questions from observation. A separate mode from planning (which sequences existing work) and building (which executes). Captures architectural ideas and triages them into the batch pipeline.
**Key decisions:**
- Build-snapshot architecture emerged from ideation (v110) — unlocking BACKLOG for parallel sessions
- BACKLOG renamed to BUILD-PLAN because "backlog" contains "log" as substring, causing persistent confusion with "build log"
- Git conventions: planning mode close steps commit directly (no tag, no push); push reserved for builds only
**Staleness risk:** Low — BACKLOG-to-BUILD-PLAN rename was scoped; check current file names.
**Sources:** v103, v110

---

## C. Build mechanics

### 11. Build procedure (`/sovbuild`)
**Why it exists:** Ensures Claude works through one batch at a time in BACKLOG order, with a mechanical boundary preventing edits outside the batch's file list. Without it, Claude drifts across multiple batches or edits files not in scope.
**Key decisions:**
- Shared `parse_backlog.py` parser extracts top unticked batch as JSON; lenient (exit 0, empty JSON on malformed) to avoid blocking on formatting errors
- `/build` is argument-less — out-of-order selection handled by reordering BACKLOG in planning
- PreToolUse enforces batch file-list boundary mechanically
- Lock timing fixed in v95: lock moved from before-build to build's first action
**Staleness risk:** Low — one stale detail: v25 references `Status: active` as lock mechanism; later shifted to build-snapshot architecture. Principle of one-batch-at-a-time is current.
**Sources:** v25, v95

### 12. Test-confirmation gate
**Why it exists:** After a build, the user must verify test results before Claude can start the next batch. Without a gate, Claude would proceed on its own judgment, potentially building on top of a broken change. The gate ensures the user has seen and confirmed each test outcome.
**Key decisions:**
- PreToolUse blocks build-phase file edits when unconfirmed rows exist
- Labels (`[Requested]`/`[Suggested]`) live on change-list items, not Files: entries
- `TEST-LOG.md` added to `WRITABLE_LOGICAL_NAMES` (v28 one-line fix that was blocking the entire gate)
- Shared `project_state.py` extracted to eliminate hook helper-code duplication
**Staleness risk:** Medium — core gate concept current, but implementation evolved: now operates within build-snapshot architecture (not `Status: active`), stop hook retired, TEST-LOG format changed to 10 columns with per-row verifier split.
**Sources:** v27, v28

### 13. Testing walkthrough (`/sovtest`)
**Why it exists:** Non-coders need guided step-by-step test execution rather than a dump of all test rows. The method distinguishes four test types and splits verification between Claude-automated and user-verified, so Claude handles structural checks while the user reviews judgment calls.
**Key decisions:**
- Tests live in after-build (not batch-executor) to keep build/test boundary clean
- Verifier is per-row (not per-type) — same test type can be Claude-verified or user-verified
- 10-column TEST-LOG format with Type + Verifier columns
- Two-section recap ("Claude verified" / "Please check")
- Volunteered results accepted as alternative to guided walkthrough (specific per-row results with component name or row number + explicit status)
- One row per message during guided walkthrough; cowboy tests exempt
- Volunteered-results rule placed as subsection within walkthrough section (exception, not parallel mechanism)
**Staleness risk:** Low — v140 is very recent and refines v50 architecture.
**Sources:** v50, v140

### 14. Revert procedure (`/sovrevert`)
**Why it exists:** Non-coders need a guided walkthrough for rollback rather than being told to "run git commands." Makes rollback transparent and confirmable.
**Key decisions:**
- Uses `git checkout -- .` + `git clean -fd` rather than `git stash` or `git reset --hard` — most transparent for non-coders
- Untracked file removal is a separate confirmation step (user might want to keep build-created files)
- No prior commit → explain-and-stop rather than confusing error
**Staleness risk:** None — standalone procedure with no moving parts.
**Sources:** v108

---

## D. Doc infrastructure

### 15. Proxy files (`_method/proxies/`)
**Why it exists:** Large spine docs burn context window when Claude reads them in full. Proxies provide a lightweight index layer with line-number references so Claude can target-read specific sections via offset/limit.
**Key decisions:**
- Terse markdown over JSON — Claude reads markdown natively, humans can inspect
- Proxies regenerated by Claude (not a parser script) — format simple enough that a dedicated parser would be over-engineering
- TEST-LOG proxy only lists unconfirmed rows — confirmed rows represented by summary counts
- BACKLOG and build-log proxies are "proxy-as-index" (directly edited, operationally authoritative); UX/MANIFEST/test-log proxies are regenerated summaries
- Proxy-as-index keeps `proxies/` as single canonical "where to find indexes" location
**Staleness risk:** Low.
**Sources:** v80, v81, v88

### 16. MANIFEST.md
**Why it exists:** Tracks what features exist and where their files live, serving as source of truth for the read-before-edit gate. The rationale field records *why* each feature exists so future planning can check before rewriting or removing things.
**Key decisions:**
- Transcript-as-state for read-before-edit gate — half the implementation of a state file, same guarantee
- Paths are optional — no flag-day migration; three shapes cover single/list/directory
- Rationale uses inline italic suffix — preserves one-entry-one-line invariant
- Rationale stays out of MANIFEST proxy — keeps proxy lightweight
- Session tag in rationale — cheap pointer to build-log for deeper context
- Planning procedure checks rationale before UX rewrites
**Staleness risk:** None.
**Sources:** v39, v97

### 17. UX.md
**Why it exists:** No dedicated build-log entry found for UX.md's creation — it predates the build log. UX.md serves as the user-experience specification, separate from the backlog (which is a work plan) and MANIFEST (which is a component registry). It's locked during builds to prevent spec changes while implementation is in progress; the `[PROPOSED EDIT PENDING]` mechanism queues changes for user review.
**Staleness risk:** None — foundational doc.
**Sources:** No explicit entry.

### 18. BACKLOG.md / BUILD-PLAN
**Why it exists:** Work needs to be organized into discrete, scoped batches rather than a flat task list. Batch structure gives Claude and the user a shared contract for what a build includes (Goal, Outputs, Success criteria, Decisions, Dependencies) separated from the operational file list by a `Changes:` delimiter.
**Key decisions:**
- `Changes:` delimiter (not a scope-context fence) — cheaper, robust, backwards-compatible
- Red flags auto-detected as conditional section
- HTML-comment format specs in template instead of example batches (no diff noise)
- 4-digit zero-padded numbering following ADR convention
- `Status:` at top of batch body (easy to spot and parse); absent = queued for backwards compatibility
**Staleness risk:** Low — BACKLOG proxy-as-index (v88) superseded INDEX.md from v52, but batch structure and status tracking remain current.
**Sources:** v51, v52, v60

### 19. Build log
**Why it exists:** Replaced monolithic `BUILD-LOG.md` with per-entry files matching the BACKLOG folder pattern. A single growing file becomes unwieldy and burns context; per-entry files let Claude read only relevant history.
**Key decisions:**
- 3-digit entry numbers (fewer builds expected than BACKLOG batches)
- Bullet list format for index, matching BACKLOG
- Dev-side migration was script-based (74 files too error-prone by hand)
**Staleness risk:** Low — INDEX.md later relocated to `proxies/build-log.md`, but folder structure is current.
**Sources:** v54, v76

### 20. TEST-LOG
**Why it exists:** Tracks smoke-test results per session. Row pruning keeps it from growing unboundedly. Folder split (matching BACKLOG and build-log) moves to per-session files so Claude doesn't load entire test history.
**Key decisions:**
- Component-based pruning — cleanest signal for row relevance
- Deleted outright, no archive (git history preserves removed rows)
- Pruning placed at planning step 2c (planning already reads MANIFEST)
- Per-session file naming mirrors build-log
- Index line includes row count and unconfirmed count for at-a-glance status
- Row IDs globally unique across files (not per-file)
- Proxy-as-index (same pattern as BACKLOG and build-log)
**Staleness risk:** None — completes three-doc convergence on proxy-as-index.
**Sources:** v58, v89

---

## E. Safety & quality

### 21. Adoption gate
**Why it exists:** Prevents Claude from accidentally editing files in folders that haven't adopted the method. Two-hook design: advisory at session open (soft), enforcement at edit time (hard).
**Key decisions:**
- Three-tier SessionStart: Tier 1 (non-method folder) emits nothing — plugin invisible; Tier 2 (partial) emits universal rules + gap flag; Tier 3 (complete) emits full state summary
- Tier 1 silence is deliberate — plugin should not inject itself into unrelated folders
- Tier-2 detection tightened via method-footer check (prevents false positives from unrelated BACKLOG.md files)
- PreToolUse gate covers Edit/Write/MultiEdit only — Bash bypasses by design (threat model is accidental edits)
- `/adopt` calls pass through; gate self-clears on adoption
**Staleness risk:** Low — architecture current. Bash gap later closed by bash write-guard (v102).
**Sources:** v21, v29

### 22. Git safety guard
**Why it exists:** Prevents destructive git operations (`git reset --hard`, `git push --force`) that could lose work. Mechanical backstop — Claude can't override a hook.
**Key decisions:**
- Separate file (not extending `pre_tool_use.py`) — different matcher, different concern domain
- `--force-with-lease` explicitly allowed (it's the safe alternative)
- `\b` word-boundary regex bug caught pre-ship
**Staleness risk:** None — stable, narrow scope.
**Sources:** v34

### 23. Bash write guard
**Why it exists:** Closes the gap where shell commands could bypass Edit/Write/MultiEdit guards. Scans for file-write patterns and applies the same rules as edit hooks.
**Key decisions:**
- Added to existing `pre_tool_use.py` (shares state with existing check functions)
- Two-stage: quick keyword regex first (fast path for 99% of Bash calls), expensive path extraction only when write patterns detected
- Null targets (`/dev/null`, `$null`, `NUL`) treated as non-writes
- BACKLOG/MANIFEST exempted (always writable, same as edit flow)
- Skill escape guidance added to all phase-lock deny messages
**Staleness risk:** None.
**Sources:** v102

### 24. Read-before-edit gate
**Why it exists:** Ensures Claude has context about a feature before editing its files. Hook denies the first edit on a MANIFEST-covered file with inline context, then allows retries via transcript-scan marker.
**Key decisions:**
- Transcript-as-state over state file — half the implementation, same guarantee
- Paths optional on MANIFEST entries (no flag-day migration)
- Three path shapes: single, list, directory
- Spine docs exempt (don't need MANIFEST lookup)
- After-build populates paths on touch (incremental migration)
**Staleness risk:** None — stable, narrow scope.
**Sources:** v39

### 25. PostToolUse validation
**Why it exists:** Catches structural mistakes in method docs at write time, before they propagate. Started as BACKLOG-only validation and grew to cover five doc types.
**Key decisions:**
- Separate script (`validate_docs.py`) — validators are shape-checkers, distinct from parser's data-extraction role
- PostToolUse as trigger (same write-time pattern as BACKLOG check); also usable standalone via CLI
- Lenient warnings via `additionalContext`, not blocks — Claude sees and self-corrects
- Operational proxies exempt from header validation (directly edited indexes with different format rules)
- Scope-context check requires ≥3 non-heading lines to fire (avoids false positives on drafts)
- Build-log entry check requires a heading to fire (empty files and stubs aren't false positives)
**Staleness risk:** None.
**Sources:** v56, v101

### 26. Unclosed-build commit guard
**Why it exists:** Prevents orphaned snapshots that block all future builds. When all Files: entries are ticked but `/sovclose` never ran, committing would create a state where the build appears done but close outputs are missing.
**Key decisions:**
- Detection uses `Status: active` + all files ticked (sufficient because `/sovclose` always transitions status)
- Warning in both system message and user-facing status block
- Commit guard regex reduces false positives on non-commit git commands
- Mid-build commits (some files unticked) explicitly allowed
- Detection keyed on `_method/active-build.md` existence
**Staleness risk:** None — among the most recently shipped features.
**Sources:** v107, v132

---

## F. Behavioural rules

### 27. "Push back rather than agreeing"
**Why it exists:** One of the original eight V18 rules. Originates from the user's personal collaboration preference. Load-bearing for drift checks and red-flag surfacing — if Claude agrees rather than questioning, problems pass silently into source-of-truth docs.
**Key decisions:** No specific design decisions in the build log. Part of the foundational set from day one.
**Staleness risk:** None — foundational principle.
**Sources:** v18 (original rule, no dedicated rationale entry)

### 28. "Plain language over jargon"
**Why it exists:** Original V18 rule. The method targets non-coders explicitly. Load-bearing for the build recap, which assumes plain-language output so the user can verify what was built without reading code.
**Key decisions:** v106 reinforced — the `_method/` orientation section in CLAUDE-TEMPLATE.md was "written for non-coders — no jargon, no implementation details."
**Staleness risk:** None — core design constraint.
**Sources:** v18, v106

### 29. "Language: field support"
**Why it exists:** Shipped in V117. Non-English users must receive output in their language, but hook regex patterns match English control tokens. The design splits: human-facing output follows the `Language:` field; control tokens and procedure docs stay English so hooks don't break.
**Key decisions:**
- `Language:` field set during `/sovsetup` Q5
- Procedure docs stay English (Claude reads internally, paraphrases in target language)
- BOM hardening (`utf-8-sig` encoding) bundled for Windows byte-order marks
- `core.quotepath false` git setting for non-ASCII paths
**Staleness risk:** Low — stable but not yet E2E tested with a real multi-language project.
**Sources:** v117

### 30. "No stealth fixes"
**Why it exists:** Original V18 rule. When Claude silently fixes a regression, the build recap becomes inaccurate — it records what shipped but omits the break-then-fix cycle. The rule requires explicit disclosure.
**Key decisions:** Deliberately kept as prose, not mechanized. v103 considered and parked a PostToolUseFailure hook — "the 'no stealth fixes' prose rule covers the general case" and a logging hook "would generate noise on innocent failures without proportional value."
**Staleness risk:** None — deliberately kept as prose.
**Sources:** v18, v103, v136

### 31. "Flag out-of-scope improvements"
**Why it exists:** Original V18 rule. Supports the flag taxonomy table — out-of-scope improvements go "end of response, in chat; becomes a Discovery in next planning recap if actioned." Prevents scope creep during builds without losing observations.
**Key decisions:** Flag taxonomy table (V32) formalized three routing destinations when universal-behaviour.md absorbed cross-cutting orphans from retired NO-CODE-METHOD.md.
**Staleness risk:** None — foundational to build-batch boundary enforcement.
**Sources:** v18, v32

### 32. "Red flags — screen and surface"
**Why it exists:** Original V18 rule, later expanded. Security/privacy/safety concerns are never silently swallowed — three explicit outcomes: address now, attach to planned feature, or defer with BACKLOG Red flags entry.
**Key decisions:**
- `[SECURITY]` marker is informational, not hook-enforced (v96: "hooks add complexity and false-positive risk for a marker that's primarily a prioritization input")
- Red flags have a dedicated BACKLOG section with specific entry format
- Dev-side adaptation routes to `[SECURITY]`-marked batches or OQs (dev BACKLOG has no separate Red flags section)
**Staleness risk:** None — actively expanding (most recently v129, v136).
**Sources:** v18, v51, v96, v129, v136

### 33. "Verify external facts, don't guess"
**Why it exists:** Introduced V38. Prevents wrong facts from entering source-of-truth docs when Claude guesses rather than verifying. `[UNVERIFIED: <what>]` markers serve as fallback when search tools aren't available.
**Key decisions:**
- v38: `[UNVERIFIED]` as fallback, not hard block ("user can't always run searches")
- v53: All "prompt user for Sonnet search" language replaced with "research directly" — Claude now has its own search tools
- Filing became mandatory (was advisory)
- Proactive research (watching for decisions that need external information) added as companion rule
**Staleness risk:** None — actively refined (v53).
**Sources:** v38, v53

### 34. "Route information to artifacts, not memory"
**Why it exists:** Introduced V65. Memory writes bypass PreToolUse entirely (Claude Code issue #44820, closed "not planned"), making prose rules the only viable enforcement. Test: "if you can name the destination, write it there." Memory is for cross-session context with no project-level home.
**Key decisions:**
- Mechanical enforcement investigated first — dead end (memory writes don't use the Write tool)
- Prose rule is the fallback, not the first choice
- Research-filing made mandatory in same session
**Staleness risk:** None — platform limitation unchanged.
**Sources:** v65, v136

### 35. "Session-length awareness" (compact nudges)
**Why it exists:** Introduced V116. Claude has no visibility into its own context window usage (discovered v110). ~20% of sessions blow out when file-touch count is high and deliberation extends mid-build. Compact nudges give recovery points.
**Key decisions:**
- Mid-session nudge: 15+ exchanges since `/sovbuild` without reaching `/sovclose`
- Invocation-prompt nudge: every skill handoff `[PROMPT]` recommends `/compact`
- Compound trigger (8+ files AND open decisions) — deliberation-heavy builds blow out, not high file count alone
- Placed in universal-behaviour.md (cross-cutting rule)
**Staleness risk:** None — recently shipped, addresses persistent problem.
**Sources:** v110, v114, v116, v124

### 36. "Walkthroughs one step at a time"
**Why it exists:** Original V18 rule, reflecting user's collaboration preference. Companion inversion: alternatives for choosing between go all at once. Load-bearing for `[SEQUENCE]`-tagged routes and ad-hoc walkthroughs for non-coders.
**Key decisions:**
- v140: Test-specific pacing rule kept separate from generic rule because it adds cowboy-test exemption
- Volunteered-results rule placed as subsection (exception to flow, not parallel mechanism)
**Staleness risk:** None — recently refined in v140.
**Sources:** v18, v140

### 37. "Never infer completion"
**Why it exists:** Protects TEST-LOG integrity and the test-confirmation gate. Without it, Claude could mark rows confirmed based on absence of complaints or bulk statements like "all others good," bypassing the gate without actual per-row verification.
**Key decisions:** No dedicated build-log entry — added organically as the test-confirmation gate matured. The companion hook (gate blocking builds) was shipped v27-v28 with full mechanical enforcement. The prose rule fills the gap hooks can't cover: Claude's judgment about whether a user statement constitutes confirmation.
**Staleness risk:** None — integral to test integrity.
**Sources:** v27, v28, v135, v140 (no explicit entry for the prose rule itself)

### 38. "Response-shape tags"
**Why it exists:** Tags were part of the original method (pre-plugin) and absorbed into universal-behaviour.md during V32 when NO-CODE-METHOD.md was retired. They solve a verbosity-control problem: procedure docs need to specify not just what Claude does but how much it says.
**Key decisions:**
- Tags "compose freely" and "genuine tension is a doc bug — flag it"
- v99: Tags reproduced in dev-side session-reference.md rather than cross-referenced ("dev-side sessions don't routinely load plugin docs")
- `[PROMPT]` used as turn boundary marker in two-turn close procedure (v124)
**Staleness risk:** None — actively used across both plugin-side and dev-side.
**Sources:** v32, v99, v124

---

## G. Setup & onboarding

### 39. Setup procedure (`/sovsetup`)
**Why it exists:** Prevents accidental edits in unadopted projects and handles four folder-state branches to bring any project into the method. The core threat model is accidental edits, not malicious actors.
**Key decisions:**
- Two-hook safety net: SessionStart advisory (soft) + PreToolUse enforcement (hard)
- PreToolUse gate covers Edit/Write/MultiEdit only — Bash bypasses by design (accidental-edit threat model)
- `.no-code-method-skip` removed from public plugin; opt-out via `/plugin` toggle
- Renamed `/adopt` to `/setup` (less jargon, more accessible to non-coders)
- Case 4 non-blocking placeholder wording over omitting scope sections (before-build benefits from knowing what's missing)
- Scaffold drift detection via pytest registry (a separate version registry would have the same manual-maintenance risk)
- First-time UX: unadopted empty folders get "run `/setup` first" instead of referencing docs that don't exist yet
- Parent-directory advisory fires unconditionally (detecting "different project" is unreliable, warning is cheap)
- Method infra whitelist checks both `_method/` and root-level layouts for backwards compatibility
**Staleness risk:** None — all four cases actively maintained.
**Sources:** v29, v46, v63, v84, v109, v113

### 40. Research workflow (`/sovresearch`)
**Why it exists:** Replaces old pattern of prompting user to run a Sonnet search. The plugin's value is the discipline wrapper (skill + template + rule), not the API call itself.
**Key decisions:**
- Free-form kebab-case naming for research files (reference material, not sequential — no allocator needed)
- Date+slug naming for search query files (temporal visibility without allocator)
- `[UNVERIFIED: <what>]` fallback when search tools unavailable
- Reuse existing MCP server — plugin ships only the discipline wrapper; eliminated plan to build custom MCP server
- Proactive-search guidance in universal-behaviour.md (mechanism-agnostic)
**Staleness risk:** Low — discipline-wrapper rationale current; specific MCP server reference may have changed.
**Sources:** v53, v83

### 41. Tersify procedure (`/sovtersify`)
**Why it exists:** Non-coders accumulate verbose documentation that fills context windows and degrades Claude's performance. Directly addresses the core tension: heavy docs burn context, leaving less room for actual work.
**Key decisions:**
- Phase gate in procedure doc, not hook (source-of-truth docs already phase-gated by PreToolUse; procedure-level check gives clearer deny message)
- Compact gate between triage and audit (triage analysis fills context that isn't needed during editing)
- Adherence-drop diagnostic in universal-behaviour.md (Claude surfaces `/sovtersify` as one diagnostic option alongside others)
- Three issue categories: wrong-home content, structural problems, verbose prose
- Two-phase flow: triage then audit, with user approval gates on each target
**Staleness risk:** None — addresses ongoing structural concern.
**Sources:** v98

### 42. Git workflow (`/sovgit`)
**Why it exists:** Non-coders need plain-English narration of git operations, and destructive git commands need mechanical prevention.
**Key decisions:**
- Git safety-guard hook in separate file (different matcher, different concern domain)
- Denies `git reset --hard` and `git push --force`; allows `--force-with-lease`
- "Tag and push after every build" as recommended habit
- First-use solo/team detection, writes Git workflow section to CLAUDE.md
- Planning/general close path skips build-log entry (lightweight)
- All skill-to-skill transitions use `[PROMPT]` nudges, never auto-handoff
**Staleness risk:** Low.
**Sources:** v34, v94

---

## Summary: gaps and observations

### Features with no build-log rationale
- **Feature 17 (UX.md)** — predates the build log. The "why" needs to be written fresh.

### Features with stale rationale
- **Feature 2 (Phase detection)** — original `Status: active` mechanism superseded by file-existence. The *why* is stable but the *how* is outdated.
- **Feature 12 (Test-confirmation gate)** — core concept current but implementation evolved significantly (stop hook retired, 10-column format, build-snapshot architecture).

### Features where rationale is purely prose (no hook enforcement)
- **Features 27, 28, 30, 31, 34, 36, 37** — these rules exist only as prose in universal-behaviour.md. Some (27, 28, 30, 36) predate the build log. Their "why" may need to be written fresh for consumer-facing docs since the build log doesn't explain the original incidents.

### Richest rationale sources
- **Feature 5 (Close procedure)** — four build-log entries, well-documented evolution
- **Feature 39 (Setup)** — six build-log entries, thoroughly documented
- **Feature 32 (Red flags)** — five build-log entries, progressive expansion
