# Build log

Running record of decisions, changes, and reasoning. Newest first. Written for a friend skimming — half a page per session, less when possible.

For format details, see `BUILD-METHOD.md` → *BUILD-LOG entry shape*.

---

## V28 — 2026-05-18 — V27 fix sweep: test-confirmation gate becomes functional

**What shipped.** Three V27 bugs found in same-day Windows smoke testing, all fixed and live-tested end-to-end.

- `plugin/hooks/pre_tool_use.py` — `WRITABLE_LOGICAL_NAMES` extended with `"TEST-LOG.md"` (the one-line fix that unblocks everything else). Check (a) docstring names TEST-LOG.md as a spine doc explicitly. After-build's `Write(TEST-LOG.md)` now succeeds; the V27 gate has rows to gate on. Duplicated helpers extracted (see next item) — file shrinks ~150 lines.
- `plugin/scripts/project_state.py` — new shared module (the V27 BUILD-LOG-named co-fix). Holds the helpers previously duplicated in `pre_tool_use.py` and `stop.py` (`safe_read_text`, `extract_path_block`, `resolve_path_block_entry`, `run_parser`, `parse_test_log_rows`, `is_row_confirmed`, `identify_previous_session`) plus new `get_unconfirmed_previous_session_rows` and `is_test_session_open` extracted from `check_test_confirmation_gate`.
- `plugin/hooks/stop.py` — imports from `project_state`. New V28 check: `if is_test_session_open(project_root): return emit_silent()` before `run_parser` — defers the batch-executor redirect when previous-session rows are unconfirmed. Docstring rewritten for four outcomes (was three).
- `planning/sessions/V28.md` (this session's scope) with V28→V29→V30→V31→V32 renumbering of pre-existing scope files (V28-prequel restructure — `/adopt` moves from V28.md to V29.md, etc.).
- `planning/OPEN-QUESTIONS.md` — V27 WRITABLE_LOGICAL_NAMES + Stop-hook-vs-tripwire entries removed (both resolved this session).
- `planning/PLAN.md` — V28 row replaced with the fix sweep. Walkthrough-mode-for-non-UI-testing (PLAN.md's prior V28) dropped: never had a matching `sessions/V28.md`, V27's after-build "What to test" covers the use case at narrative altitude.
- `TEST-LOG.md` — V28 section with rows #064–070. Implicitly flips #059 (AB1) and #060 (AB3) to Pass via the after-build flow; explicitly retests #057 (P1) post-refactor.

Smoke-tested live in `claude --plugin-dir` against a freshly rebuilt `v27-smoke-fixtures/g4` (V27 fixture was empty — rebuilt 7 files via the Write tool). Two-run sequence: after-build → row opened + MANIFEST update + recap; `/exit` + restart → SessionStart tripwire → planning read-back → "Pass" → test session closed + drift checks clean. All rows Pass; see TEST-LOG #064–070.

**Method-version footers NOT bumped this session.** V28 restores V27's *intended* behaviour — consumers reading the V27 footer get what V27 claimed to ship. Bumping would over-signal a structural change for a bug-fix sweep. (V28.md's open question on this resolved deliberately to no-bump.)

**Decisions taken and why.**

- **V28-prequel restructure over expanding V28's `/adopt` scope.** V27's bugs made the gate inert; shipping `/adopt`'s safety net on top of inert machinery would have buried the foundation issue. Renamed pre-existing scope files (V28→V29→V30→V31→V32) and inserted a new V28 for the fix sweep. Each session keeps one focus.
- **Shared helpers module: `plugin/scripts/project_state.py`.** Considered `shared_state.py` (vague), `test_log.py` (too narrow), `plugin/lib/state.py` (new directory). `project_state.py` describes what's inside (path-block reads, BACKLOG parser invocation, TEST-LOG parsing, BUILD-LOG session-narrowing). `plugin/scripts/` is the existing neighbour for `parse_backlog.py`; hooks add scripts/ to sys.path on import. No new directory needed.
- **Stop hook defers via silent exit, not redirect-to-planning.** Two viable shapes. Silent exit relies on the SessionStart tripwire (already shipped + confirmed working in V27 #056) to do the routing; redirect-to-planning duplicates intent. Critically, a redirect-to-planning during planning's read-back-turn-end would re-invoke planning and re-ask the same question — worse UX than the bug we're fixing.
- **Walkthrough-mode-for-non-UI-testing dropped, not deferred.** PLAN.md row never had a matching `sessions/V28.md`. V27's after-build recap already names "What to test" with one bullet per user-observable behaviour — at narrative altitude, the walkthrough need is covered. If a structured step-by-step format is missed in practice, it'll surface as an OPEN-QUESTIONS entry naturally.

**Pivots and surprises.**

- **Cowork parallel-session corruption hit at session open.** Working tree showed hundreds of spurious modifications (Archive folders, every method-side doc, both V30.md and V31.md scope files) plus a phantom `.git/index.lock` that bash couldn't delete. Recovery: Alex deleted the lock via Windows Explorer, `git reset --hard HEAD` in PowerShell restored the V27 commit state. All subsequent git operations went through PowerShell (file edits stayed in Cowork via Read/Edit/Write — those use the canonical Windows path).
- **V27 g4 fixture was empty.** Initial premise "fixture intact" was wrong; `ls` showed only `.` and `..`. Cause unknown — wasn't V27, `git reset` (fixture sits outside the git repo), or Alex's doc compaction (which she'd confirmed didn't touch this folder). Rebuilt 7 files (CLAUDE.md, UX.md, BACKLOG.md with fully-ticked batch, MANIFEST.md, TEST-LOG.md, BUILD-LOG.md, index.html) via Write tool in mtime-sensitive order so `BACKLOG.mtime > TEST-LOG.mtime` and the Stop hook's after-build trigger fired correctly.
- **Stop-hook V28 fix not uniquely distinguished from natural fallthrough in the live test.** Fixture batch was fully ticked, so `run_parser` would have returned empty even without V28's check — both paths yield silent exit. V28's check definitely fired (`is_test_session_open` returned True given the unconfirmed row), but the bug-trigger scenario (unticked batch + unconfirmed rows simultaneously) wasn't replicated. The one-line fix is mechanically straightforward; TEST-LOG #069 records the caveat. Uniquely-V28 verification owed if doubt arises (direct hook-script test).
- **Compacted planning docs landed with `(1)` suffixes.** Windows save-as artifact from Alex's mid-session doc compaction. `OPEN-QUESTIONS (1).md`, `INVENTORY (1).md`, `OPUS-FEASIBILITY-PROMPT (1).md`, `claude-code-plugin-feasibility-response-terse.md` — renamed back to canonical names in PowerShell.

- **Mid-session compaction pass folded into V28's commit.** While Claude worked on the code, Alex compacted the language in `BUILD-METHOD.md`, `Crash course.md`, `DOC-STRUCTURE.md`, `NO-CODE-METHOD.md`, `README.md`, and the four `planning/` docs (`INVENTORY.md`, `OPEN-QUESTIONS.md`, `OPUS-FEASIBILITY-PROMPT.md`, `claude-code-plugin-feasibility-response.md`). Language tightening only — no meaning, rules, paths, file names, or decisions changed. Folded into V28's commit as the natural session boundary; a separate compaction commit would have added churn without value.

**Carried forward.**

- **V27 Skipped TEST-LOG rows #061 (P2), #062 (L1), #063 (L2)** remain Skipped — each needs a narrower fixture (multiple unconfirmed rows for P2's push-back-on-bulk-confirmations; a planning session writing `[Requested]`/`[Suggested]` labels on BACKLOG.md change-list bullets for L1; a halt-C verification-burden split in before-build for L2). Slot into a future session if regression-risk warrants direct verification; otherwise let them retest opportunistically in real Taskflow work.
- **Stop-hook V28 unique-verification** (direct hook-script test against a fixture with unticked batch + unconfirmed rows simultaneous). Cheap; not blocking V28's ship.
- **PLAN.md ↔ scope-file numbering convention** to enforce going forward — drift caught at session-open this time (PLAN.md V28 named walkthrough-mode, V28.md held `/adopt`).

---

## V27 — 2026-05-17 — After-build subagent + test-confirmation gate hook + SessionStart TEST-LOG tripwire + [Requested]/[Suggested] labels in BACKLOG.md

**What shipped.** The V26 test-confirmation gate prose, now wired end-to-end.

- `plugin/agents/after-build.md` — new subagent owning *After every build*: silent MANIFEST update (Q2), recap with `[Requested]`/`[Suggested]` labels read from BACKLOG.md (Q3), test-session-open by appending blank-Status rows to TEST-LOG.md, prompts to refresh-test-and-return. Idempotent — exits with a brief note if TEST-LOG rows for the current session already exist (covers Stop-hook re-fires).
- `plugin/agents/batch-executor.md` — V25's *After every build* responsibilities stripped. Turn now ends with a brief completion note; Stop hook routes to after-build from there.
- `plugin/agents/planning.md` — two additions: per-row read-back of pending TEST-LOG rows as first sub-step of *During planning* (Rule 2, push-back-on-bulk-confirmations + Skipped-requires-reason); inline-label-writing on every change-list bullet (`- [Requested] Fix drag-to-postpone overshoot`).
- `plugin/agents/before-build.md` — label-preservation rule for halt-C splits: labels travel with their items; no re-classifying to `[Suggested]`.
- `plugin/hooks/pre_tool_use.py` — gained check (f): test-confirmation gate on Task → batch-executor. `hooks.json` PreToolUse matcher extended from `Edit|Write|MultiEdit` to `...|Task`; script dispatches on `tool_name`. Reads TEST-LOG, identifies previous batch's session from BUILD-LOG (path-block → project-root → strict fallback when BUILD-LOG missing OR unparseable — per Q4, the distinction is named in the deny message).
- `plugin/hooks/session_start.py` — TEST-LOG tripwire (Q5): when previous-batch rows have `Confirmed Explicitly: No`, `additionalContext` injects a routing override directing main Claude to planning regardless of opener, with row IDs and Test Descriptions inline. `SPINE_FILENAMES` extended for `TEST-LOG.md`; `PLUGIN_METHOD_VERSION` bumped to 27; comment rewritten for V20+ session-tag/method-version decoupling.
- `plugin/hooks/stop.py` — after-build routing path: when parser returns no top unticked batch but Build batches has a `- [x]` bullet, compare BACKLOG.mtime to TEST-LOG.mtime. If BACKLOG newer, redirect to after-build; otherwise silent.
- `plugin/commands/build.md` — updated for the batch-executor-completion-note vs. after-build-recap split.
- DOC-STRUCTURE.md → *Build batches* — new sub-section *Change list — `[Requested]`/`[Suggested]` labels*: the inline-prefix shape, planning/before-build/after-build chain, why labels attach to changes-not-files.
- NO-CODE-METHOD.md — new *Handoff to after-build* paragraph in *At session start* (also tightened batch-executor handoff to say "completion note"); *During planning* labels rule extended with BACKLOG.md-inline persistence + DOC-STRUCTURE cross-reference.
- Crash course.md — *After build* paragraph in *The session shape* attributes recap to after-build with labels-read-off-BACKLOG; *Four disciplines* test-confirmation-gate paragraph updated to describe both hooks.
- INVENTORY.md — full sweep: SessionStart gains TEST-LOG tripwire; PreToolUse (f) promoted from spec to Shipped V27; Stop hook gains after-build routing; planning, before-build, batch-executor, after-build entries updated; stale "NO-CODE-METHOD.md retired in V27" entry corrected (prose file stays).
- BACKLOG-TEMPLATE.md (×2) — examples show `[Requested]`/`[Suggested]` labels.
- BUILD-METHOD.md — *Footer bumps* list adds `after-build.md`.
- Version 26 → 27 across 19 files. `plugin.json` 0.26.0 → 0.27.0.
- Three V26 carry-forwards (SPINE_FILENAMES, PLUGIN_METHOD_VERSION comment, pre_tool_use.py docstring count) absorbed.

**No smoke tests run this session** — Windows integration via `claude --plugin-dir` owed to Alex post-commit. ~13 distinct checks the V27 design implies (5 around the gate, 3 after-build, 2 planning extension, 2 labels, 1 DOC-STRUCTURE) get logged to TEST-LOG when run.

**Decisions taken and why.**

- **Q3 placement correction: labels live on change-list items, not Files: sub-section.** V27.md's scope said "small label addition in *Files: sub-section* item shape" — pushed back at design-lock as a category error. `[Requested]`/`[Suggested]` describes the provenance of a *change*, not a file: one change touches many files; one file absorbs many changes. Files-level labels would force an arbitrary call when `[Requested]` and `[Suggested]` changes touch the same file. Moved up to change-list level; DOC-STRUCTURE got an explicit sub-section.

- **Mid-session scope expansion: fold the label work into V27 rather than a follow-up.** Q3's resolution implied three small touches beyond after-build (DOC-STRUCTURE, planning label-write, before-build label-preserve). Considered V27a/V27b split. Folded in: those files were already in scope for other reasons, so additional edits cost less than reopening them, and shipping after-build without labels would have meant a dead-code "fallback for missing labels" branch covering a state that should never exist.

- **Scope discovery: batch-executor must shed *After every build*.** V27.md listed after-build as a new subagent but didn't note that batch-executor's V25-era completion path *also* does MANIFEST + recap + prompts. Surfaced while designing after-build's prompt — leaving both would mean duplicate work. Added the scope-reduction edit.

- **Stop hook "after-build pending" heuristic: BACKLOG.mtime vs. TEST-LOG.mtime.** Considered state file, session-tag comparison, "no rows for today" check — each had same-day second-batch failure modes. Mtime comparison is simple, robust to same-day (planning advances BACKLOG when removing the completed batch; second batch advances it again; TEST-LOG stays at first batch's after-build write — BACKLOG > TEST-LOG when second batch completes), and lenient on stat failures.

- **TEST-LOG tripwire as `additionalContext` routing override, not just a status flag.** SessionStart's state summary *informs* main Claude's routing; the tripwire *overrides* it — "regardless of opener, spawn planning with this prompt." Necessary because a feature-request opener while pending rows exist would otherwise route to planning-as-feature-request, not read-back-first. Carries row IDs and Test Descriptions so the subagent can open with a specific row immediately.

**Pivots and surprises.**

- **Stale "NO-CODE-METHOD.md retired in V27" in INVENTORY.** Aspirational note from earlier sessions, not actual V27 scope. Updated: NO-CODE-METHOD.md is source-of-truth prose; subagents read it via read-spec-on-entry.
- **batch-executor's "Flags surfaced in your response" section needed restructuring.** Originally assumed batch-executor produces the recap. Post-V27 it doesn't, so flags need a different surface: red flags written to BACKLOG.md's Red flags section (where after-build picks them up); out-of-scope improvements need to be prominent in batch-executor's in-turn output (chat-only signal after-build can't see).
- **Crash course's "A hook is the load-bearing gate"** was aspirational at V26 (hook not yet shipped). True with V27. Tightened to name both hooks.

**Carried forward.**

- **Smoke testing in `claude --plugin-dir` on Windows** — Alex runs the 13-check sweep post-commit.
- **`planning/sessions/V27.md`** deleted in this commit per transient lifecycle.
- **OPEN-QUESTIONS.md entries** — none added; no existing entries named V27 as fold-in target.
- **Helper-code duplication across `pre_tool_use.py` and `session_start.py`.** Both carry near-identical `parse_test_log_rows`, `is_row_confirmed`, and BUILD-LOG identification logic. Extract to a shared module (same pattern as `parse_backlog.py`). Not pursued — duplication is mechanical, refactor deserves its own session. → future packaging/refactor session.
- **Q3 correction takeaway** — V27.md's category error wouldn't have been caught without the design-lock walk. Worth keeping the design-lock-first rhythm where the scope file calls a specific structural location.

---

## V26 — 2026-05-17 — TEST-LOG.md mechanism + Drafts in flight convention + V25 carry-over bugfixes

**What shipped.** New consumer-side TEST-LOG.md doc class (8 columns: # / Date / Session / Component / Test Description / Status / Confirmed Explicitly / User Notes; phase-based pruning), with templates in both `templates/` and `plugin/templates/`, and structural spec in DOC-STRUCTURE.md.

Five protocol rules placed across NO-CODE-METHOD.md phases:
- Rule 1 (Never infer completion) → *Required of Claude*
- Rule 2 (test-session-close read-back) → first sub-step of *During planning*
- Rule 3 (No new build until test session closed, hybrid hook+subagent) → *Prohibited of Claude*
- Rule 4 (Pass/Fail/Skipped definitions) → *Vocabulary*
- Rule 5 (Retest after change, judgement + reasoning trail) → fourth drift check in *During planning*

Phase edits: *After every build* gains test-session-open step; *During planning* gains test-session-close read-back. CLAUDE-TEMPLATE.md (×2) gains TEST-LOG.md in the JSON path block; scaffold.py extended for fifth spine template. Crash course updated (TEST-LOG bullet in *The files*; *Three disciplines* → *Four*). V27.md scope reframed into 3 components plus main-Claude session-open TEST-LOG tripwire.

**Three V25 carry-over bugfixes** absorbed: parse_backlog.py placeholder detection (#041); BACKLOG-TEMPLATE.md de-collision in both copies (#042); before-build.md parser invocation fix (#044). Sweep bonus: `plugin/commands/build.md` had the same parser-path bug — fixed inline.

**Session-open recovery:** dev-side `CLAUDE.md` (No-code-method project root, not part of this commit) gained *Vxx.md inputs must be in the repo* session-open scan rule; BUILD-METHOD.md gained *Drafts in flight* under *Planning artefacts* (close-time prevention); `planning/drafts/` folder created with V26 as inaugural example via `planning/drafts/test-log-mechanism.md` (consumed and deleted at session close).

Doc-code parity audit: 17 edits across 8 files closing gaps from TEST-LOG additions (doc-listing updated in NO-CODE-METHOD + Crash course; "three drift checks" → four; INVENTORY after-build entry rewritten for V27 revival; INVENTORY PreToolUse gains (f); pre-existing "5 templates" off-by-one in INVENTORY + SKILL.md fixed). Footer bumps V25→V26 across 21 files; BUILD-METHOD's *Footer bumps* list extended for the two new TEST-LOG-TEMPLATE files. No smoke tests — V26 is doc-only on the gate; real test runs when V27 ships.

**Decisions taken and why.**

- **Rule 2 relocation, mid-session.** V26.md put Rule 2 inside *After every build*. Mid-session realisation: *After every build* can't span the testing window — the user tests between sessions, after `/clear`. Relocated to first sub-step of *During planning* where test outcomes actually arrive. *After every build* keeps the open step; close happens next planning. Reshapes V27: after-build owns open, planning owns close, hook fires between.

- **Hybrid enforcement of Rule 3.** Pure subagent hits the ~30% drift rate (Crash course → Caveats). Pure hook is hostile without a walk-through. Hybrid: hook is the load-bearing gate (PreToolUse on Task → batch-executor); planning's first sub-step is the UX. Hook fallback when no BUILD-LOG: "any unconfirmed row blocks" — strict but safe.

- **Q2 punted to Claude's judgement + reasoning trail.** Rule 5's "substantially changed" could be mechanical (line threshold) or judgemental. Mechanical needs the MANIFEST schema extension parked in OPEN-QUESTIONS. Judgemental keeps V26 scoped — and the reasoning trail makes the call auditable. Real builds will force a schema decision later if needed.

- **Drafts in flight convention added mid-session as recovery.** V26.md cited "the Sonnet draft produced in V20 planning" as input; nothing in the repo, nothing on Alex's machine. Confirmed via prompt-to-previous-session that the draft was never committed. Root cause: scope files wrote "Alex has the file locally" without an integrity check. Fix: `planning/drafts/<topic>.md` (committed when "good enough to walk away from"; deleted in the consuming commit) + CLAUDE.md session-open scan rule (halt on out-of-repo references in `Vxx.md` *Inputs*). V26 itself is the inaugural example.

**Pivots and surprises.**

- **V20→V26 "lives locally" failure as session-opener.** Above. Convention written into BUILD-METHOD with the V20→V26 case as a worked example.
- **`/build` slash-command parser-path bug.** OPEN-QUESTIONS noted `/build` did "correctly" handle the parser; that was about BACKLOG.md path resolution, but the script path itself (`python plugin/scripts/parse_backlog.py`) was wrong (project-relative; plugin isn't in the project tree). Caught by the V25 carry-over sweep; fixed inline.
- **Pre-existing "5 templates" off-by-one.** INVENTORY and SKILL.md both said "5 templates" with 4 listed since at least V19. V26's TEST-LOG makes the count actually 5 — coincidental fix.
- **Parity audit surfaced more drift than expected** — 17 edits, 8 files. Pattern worth keeping: when a new doc class lands, sweep doc-listing prose + count-mentions across NO-CODE-METHOD, Crash course, INVENTORY, README, and subagent bodies.

**Carried forward.**

- **`SPINE_FILENAMES` in `session_start.py`** still lists three docs; should include TEST-LOG for detection consistency. Not a runtime bug. → V27.
- **`PLUGIN_METHOD_VERSION` comment** says "Bumped each session" — outdated since V20+ decoupling. → V27.
- **`pre_tool_use.py:5` docstring** says "Runs three checks" — INVENTORY lists 5 (a–e); V27 adds (f). → V27.
- **Three V25 carry-over OPEN-QUESTIONS entries** absorbed and resolved; removed from OPEN-QUESTIONS.md.
- **`planning/sessions/V26.md`** + **`planning/drafts/test-log-mechanism.md`** deleted per their lifecycles.

---

## V25 — 2026-05-17 — Build orchestration core: Stop hook + batch-executor + before-build + slash commands + spec rewrites

**What shipped.** The build orchestration core — two main motivating examples for the plugin.

- `plugin/scripts/parse_backlog.py` — new shared parser. Walks BACKLOG.md, finds top unticked build batch, emits JSON payload (heading, change_list, Files: with tick state, Serves lines). Lenient on malformed input (`{}` + exit 0). Three call sites: Stop hook redirect reason; `/build` manual invocation; PreToolUse edit-time Files: lookup.
- `plugin/hooks/stop.py` — build sequencer. After batch-executor finishes, parses BACKLOG, finds next batch, returns `{"decision": "block", "reason": "<payload>"}` redirecting into the next batch-executor. Respects `stop_hook_active` — one redirect per user turn (D1's explicit user gating).
- `plugin/hooks/pre_tool_use.py` — (c) batch file-list boundary: parses BACKLOG at edit-time, blocks Edit/Write/MultiEdit on any file not on the top batch's Files: list. Originally-scoped (d) MANIFEST/UX read-before-edit deferred — the MANIFEST.md path-mapping schema gap blocks it (logged in OPEN-QUESTIONS).
- `plugin/agents/batch-executor.md` — build-time subagent. Receives JSON via invocation prompt, reads unticked files in Files: order, makes changes, ticks BACKLOG per-file (partial-completion-safe), produces recap with `[Requested]`/`[Suggested]`/`[Prerequisite, not in plan]`/`[Re-batch, not in plan]` labels. Halt-and-confirm protocols cover the two exceptions under *Prohibited of Claude* (prerequisite carve-out, re-batching carve-out). Rules inlined — intentional divergence from planning.md's read-spec-on-entry.
- `plugin/agents/before-build.md` — pre-build subagent. Validates the top batch (parser parses; Serves UX.md names resolve), enumerates Files: into BACKLOG, estimates verification burden, halts-and-confirms if Batch-sizing requires a split. Rules read at runtime from NO-CODE-METHOD → *Before build*.
- `plugin/commands/before-build.md` and `plugin/commands/build.md` — first two slash-commands in the newer commands-directory pattern (`description:` + `allowed-tools:` frontmatter + prose body). `/before-build` spawns before-build via Task; `/build` reads path block, runs parser, embeds payload into batch-executor invocation, handles empty-backlog.

NO-CODE-METHOD.md substantive work: *Before build* rewritten from 8 chat-mediated steps to 8 subagent-aware (validate → enumerate Files: → review → verification burden → Batch-sizing → conflict flags → switch out of plan mode + `/build`); *After every build* rewritten from 5 to 5 with explicit carve-out-label + flag-taxonomy refs; *Batch-sizing principle* sub-section added (split-when-test-list-long, bundle-no-behaviour, never-fragment-arbitrarily); *Pre-build verification estimate* added to *Before build* step 4; *Mid-build re-batching carve-out* added to *Prohibited → Two exceptions*; four new Vocabulary entries (Files: sub-section, Batch-sizing principle, Pre-build verification estimate, Halt-and-confirm protocol); *At session start* gained two new handoff paragraphs (Handoff to before-build, Handoff to batch-executor) paralleling planning. DOC-STRUCTURE.md gained *Files: sub-section* spec; *Build batches* "unfinished portion" sentence tightened to reference tick state. Crash course got three paragraph rewrites in *The session shape*. Both BACKLOG-TEMPLATE.md copies got Files: sub-section examples (mirrors kept in sync).

INVENTORY.md: six restructure passes during doc-code parity audit (before-build and batch-executor entries expanded; after-build annotated "absorbed into batch-executor"; slash-commands restructured for both patterns with shipped-V annotations; /before-build + /build moved from "Pending V23" to "Shipped V25"; templates path corrected; parse_backlog.py added; Stop + PreToolUse (c) annotated "Shipped V25"). OPEN-QUESTIONS gained four entries; one resolved in-session.

Footer bumps V23 → V25 across 16 files. `plugin.json` 0.23.0 → 0.25.0; `PLUGIN_METHOD_VERSION` 23 → 25. `batch-executor.md` gained a V25 footer for consistency with sibling subagents. BUILD-METHOD's *Footer bumps* list adds `before-build.md` and `batch-executor.md`. Pre-validation smoke tests via Cowork bash (15/15 parser, 8/8 Stop, 9/9 PreToolUse boundary + V19/V22 regression); see TEST-LOG #031–033. Windows integration in `claude --plugin-dir` owed to Alex post-commit.

**Decisions taken and why.**

- **Doc-code parity audit escape-clause override: NO-CODE-METHOD's *Before build* / *After every build* rewrites landed in-session.** BUILD-METHOD's escape clause recommends deferring spec rewrites that would dominate. Default lean was defer. Override: the spec gap was load-bearing for V25's shipped subagents — before-build's read-spec-on-entry *depends on* *Before build* being operationally correct; batch-executor's recap references *After every build* labels. Leaving V22-era wording would have shipped agents reading a spec that didn't match what they do.

- **before-build subagent: validate-only first move + read-spec-on-entry.** Original design had a "reorganise pass" matching the spec's steps 1–2 verbatim. Validation review (fresh Sonnet reading the actual files) caught: planning has full BACKLOG edit authority since V22, making reorganise dead weight in ~99% of cases and silently absorbing the only realistic case (out-of-band manual edits) where flagging would matter. Changed to validate-only; reorganise survives only as response to verification-burden split. Rule-loading: original draft proposed inline (matching batch-executor on "mechanical not branching"). Validation reframed as "stable vs. fresh rules" — batch-executor inlined rules stable since V18; before-build's load-bearing rules were V25-introduced and likely to churn. Read-spec-on-entry kills doc-code parity drift on freshest rules.

- **`/build` argument-less per V25 Q3.** Out-of-order batches handled by reordering BACKLOG during planning, not by a build-time chooser. Single mental model with Stop-hook auto-continuation: both entry points always pick top unticked batch.

- **Ideation-session edits bundled into V25's commit, not separated at staging.** Previous uncommitted ideation left rule edits in `universal-behaviour.md`, NO-CODE-METHOD, Crash course, PLAN.md. V25's parity audit added edits to two of those. Plan was `git add -p` for separate tags. At commit time, procedural cost (`git add -p` is new to Alex; unpacking would be the most friction-heavy close-out step) outweighed clean-tag value — BUILD-LOG carries both narratives. Ideation work folded in this commit: wording sharpen on "push back rather than agree" → "push back rather than simply agreeing"; new "Walkthroughs one step at a time; alternatives all at once" rule in *Required of Claude*; `[SEQUENCE]` tag definition expanded with no-previewing clause + cross-ref; new fourth load-bearing example in Crash course's *What's editable, what's not* (counter changed three → four); new V28 row in PLAN.md ("Walkthrough-mode for non-UI testing"; previous V28–V31 shifted to V29–V32). No own session number.

**Pivots and surprises.**

- **Validation-via-sister-Sonnet-session was the right intervention.** When before-build hit the three open questions (halt scenarios, reorganise scope, inline vs. read-spec), spinning up a separate Claude Code session with a self-contained validation prompt produced sharper pushback than continuing in Cowork. Two recommendations flipped, one halt scenario dropped (stale Files: detection — over-engineered), one missing scenario surfaced (verification-burden-triggered split). Pattern worth keeping for design questions with real downside risk.

- **"after-build subagent" was a ghost reference in INVENTORY.** V17's architecture listed a separate after-build. V25's batch-executor design absorbed those responsibilities on the principle that the recap is most accurate in-context with the build. INVENTORY hadn't been updated; audit caught it.

- **Slash-commands convention changed mid-roadmap.** INVENTORY described slash commands as skills with `disable-model-invocation: true` etc. — the older pattern. V25's `/before-build` and `/build` landed in the newer `plugin/commands/<name>.md` pattern. Both patterns coexist now (init-project still uses old; new commands use new). INVENTORY restructured with shipped-V annotations.

- **parse_backlog.py is lenient on failure (always exit 0, `{}` on malformed) — `/build`'s first draft misread it.** Initial draft told main Claude to detect empty via "exit non-zero or empty payload." Re-read of the docstring caught it: detection has to be on output content (`{}` or empty), not exit code. Corrected before the Edit went through.

- **Cowork bash-mount staleness recurred — pre_tool_use.py + BACKLOG.md.** Same phantom-state issue as V22. Worked around by running CLI smoke tests against `outputs/` copies, then validating canonical state via file tools. Memory entry already exists (`reference_cowork_git_mount_phantoms.md`).

- **Edit tool's "must Read first" requirement bit on every Grep'd file.** Footer bumps required reading 8 templates I'd only Grep'd. Two-pass workaround: parallel Reads, then parallel Edits. A Read with offset/limit doesn't cover editing outside the read range — fresh Read needed. Tool affordance to remember.

**Carried forward.**

- **Windows integration smoke test in `claude --plugin-dir`** — run 2026-05-17 against pre-populated `v25-scratch`. TEST-LOG #034–050. End-to-end works; three bugs logged as OPEN-QUESTIONS for V26: Stop-hook template-placeholder misfire (#041), BACKLOG-TEMPLATE `[FOLD-IN PENDING]` ambiguity (#042), before-build parser-path spec (#044).
- **Subagent rule-loading pattern divergence** — OPEN-QUESTIONS. Defer convergence until V26–V31 ship and NO-CODE-METHOD change rate settles. Revisit if parity audit flags drift in batch-executor.
- **MANIFEST.md path-mapping schema gap** — OPEN-QUESTIONS. Blocks PreToolUse (d) read-before-edit; (d) deferred from V25 as a result. Five candidate shapes in the entry; promote to a planning session when MANIFEST schema work fits naturally.
- **Stop-hook 8-block cap** — OPEN-QUESTIONS. Parked — current design respects `stop_hook_active` so chain length is always 1; cap can't trigger.
- **`/plan` slash command** — still pending; auto-route remains the only planning invocation.
- **Slash-command footer convention** — not pursued. SessionStart footer-tripwire reads spine docs and subagent bodies, not slash-commands. Set when a hook or audit needs the fingerprint.

---

## V24 — 2026-05-16 — BUILD-METHOD.md and TEST-LOG.md added; session-tag and method-version decoupled

**What shipped.** Two new dev-internal docs and a slim of the project-root `CLAUDE.md`.

- `sovereign-implementer/BUILD-METHOD.md` consolidates the working manual — session structure (open, three middle shapes, close), doc-code parity audit (now with sixth item, *Ghost references*), testing semantics (corrected), BUILD-LOG / OPEN-QUESTIONS / new TEST-LOG entry shapes, footer-bump rules, planning artefact lifecycle. Lifted out of the old CLAUDE.md and expanded where the old version was thin or wrong.
- `sovereign-implementer/TEST-LOG.md` is new — 30 backfilled rows from V18 (3), V19 (11), V21 (10), V22 (6), one Fail (V22 INVENTORY ghost-command catch + separate row for its in-session retest as Pass), three Skipped with reasons. V20 and V23 had no testable code.
- Project-root `CLAUDE.md` slimmed 240 → 100 lines — orientation, environment, file ops, terminology cheat sheet, Taskflowapp lock-down, command-prompt experience level only. Everything procedural moved to BUILD-METHOD.
- PLAN.md table renumbered: V24 is this session; old V24–V30 shifted to V25–V31 (V20 precedent). Session-scope files renamed, headings bumped, internal cross-refs shifted. OPEN-QUESTIONS entries 1–3 had forward-looking refs shifted; entry 4's dated historical notes intact. INVENTORY got mechanical V## shifts on 6 forward refs.

**No method-version footer bumps anywhere** — `plugin.json` stays 0.23.0, `PLUGIN_METHOD_VERSION` stays 23, all footers stay V23. First session under the new dev-internal-doesn't-bump rule.

**Decisions taken and why.**

- **BUILD-METHOD.md as a new file, not a CLAUDE.md restructure (option a, not b).** The dev project's working manual deserves its own home, separate from CLAUDE.md's orientation / environment / personal-collab material. Lets CLAUDE.md be terse and gives the manual room to grow (TEST-LOG entry shape, ghost-references audit, footer-bumps list — none of which fit cleanly in the old CLAUDE.md). Option b would have preserved single-file convenience but lost the conceptual separation.

- **Session tag and method-version footer decoupled going forward.** Old convention bumped footers every session regardless. V20 (Crash course promotion) and V23 (Cowork mentions strip) both bumped despite arguably-doc-only scopes — recording an interpretive mismatch. New rule: footer + `plugin.json` + `PLUGIN_METHOD_VERSION` only bump when the session substantively changes method or plugin. Session tag still increments per session. V21 footer-mismatch tripwire stays silent because `PLUGIN_METHOD_VERSION` moves in tandem. V18–V23 numbers stay as-is.

- **TEST-LOG.md created this session, not deferred to V26's consumer-side ship.** Alex pushed back on a draft proposing defer. The failure mode this session diagnosed (CLAUDE.md asserting "plugin never installed" while V18/V19/V21/V22 BUILD-LOG entries all describe smoke tests) is precisely what TEST-LOG fixes — making outcomes queryable rather than buried in prose. Backfill was ~30 min.

**Pivots and surprises.**

- **Initial framing wasted a round-trip on "live install + back-test."** I opened proposing live-install + back-test as next session before doing the read-pass, citing CLAUDE.md's *Plugin install status* "never installed" paragraph. Alex's pushback: (1) V23 was a terminology sweep with nothing testable, (2) tests have happened — BUILD-LOG records them — the recording isn't visible to future sessions, (3) the proposed session has no current pathway since the plugin isn't packaged for global install. Saved as `feedback_dont_propose_live_install_session.md`. Root fix is BUILD-METHOD's corrected *Testing* section, not just the memory.

- **The old footer-bump convention had quietly drifted across V20 and V23.** When I drafted BUILD-METHOD I treated "every session bumps" as the rule. Alex called it out: the rule itself was the problem for doc-only sessions. Decoupled-numbering is partly retroactive acknowledgement; history stays as-shipped with *Historical note* in BUILD-METHOD recording the discontinuity.

- **INVENTORY.md's forward-pointers are semantically stale.** During renumber, several refs (Crash course "Updated in V25", DOC-STRUCTURE "deferred to V25", `/new-project` "Pending — V26") look misaligned even pre-renumber. Mechanical +1 shift applied only. Content audit deferred.

- **Renumber surfaced V28.md and V31.md bodies still reference a "live-install session" deferred from V27/V28.** Superseded by this session's BUILD-METHOD *Testing*. Natural fix is V28's planning session.

- **BUILD-LOG header pointer updated mid-entry.** Said "see CLAUDE.md → *Build log*" — section moved to BUILD-METHOD this session.

**Carried forward.**

- **V23 carry-forwards remain valid.** Soft-discipline risk for mid-build SoT edits; OPEN-QUESTIONS cross-version entry still has Cowork-first vocabulary; V22's smoke-test items (a) and (e) not in TEST-LOG because BUILD-LOG didn't explicitly attest them.
- **INVENTORY.md forward-pointers** — semantic audit deferred.
- **`sessions/V24.md` hand-delete** — not applicable. This session was directed live without a scope file; step 7 of session close is a no-op. Precedent: live-directed sessions skip step 7.
- **V28.md and V31.md body's "live-install session" references** — superseded; address during V28's planning.

---

## V23 — 2026-05-17 — Remove Cowork mentions from method docs; Claude Code becomes explicitly required

**What shipped.** Cowork-removal sweep across method spec docs, templates, and plugin component bodies.

- `NO-CODE-METHOD.md` — explicit "the method requires Claude Code" at the top; "Claude-Code fallback" framing removed from new-project route; *Detect template state* tripwire simplified to recommend new-project route directly; every "in Cowork" / "during their next Cowork session" → "by hand during planning sessions" (the fold-in mechanism is unchanged — user edits by hand, Claude Code agent doesn't — only the location moves).
- `DOC-STRUCTURE.md` — two-line equivalents in *Fold-ins pending* and *Planning batches*.
- `Crash course.md` — bigger rewrite: "Where each tool fits" reframed from two tools to two phases (planning, build); "Day one" walkthrough rewrote around new-project route; editing-surfaces table collapsed from two columns to one ("Claude (the agent) edit access").
- Templates: `ADDITIONAL-DOC-TEMPLATE.md` and `BACKLOG-TEMPLATE.md` in both locations got Cowork mentions replaced.
- Plugin components: `plugin/agents/planning.md`, `pre_tool_use.py` deny message, `session_start.py` template-state recommendation, `init-project/SKILL.md` all stripped.
- This project's outside-the-repo `CLAUDE.md` stripped its "work happens in Cowork by default" specification per user direction — left unspecified (not replaced with Claude Code) to preserve flexibility during Alex's personal migration.
- `OPEN-QUESTIONS.md` prose-only-rewrite entry got a V23 note recording the framing shift: target audience moves from "Cowork novices" to "people using the method outside the plugin."
- PLAN.md renumbered during V23 prep: V23 (new) is Cowork-removal; old V23–V29 → V24–V30. Footers V22 → V23 across method-side files (3 spec docs + 5 templates × 2 + INVENTORY + planning.md). `plugin.json` 0.22.0 → 0.23.0; `PLUGIN_METHOD_VERSION` 22 → 23.

**Decisions taken and why.**

- **Claude Code is required, not recommended.** The user's direction was unambiguous: the method ships as a Claude Code plugin and can't run anywhere else, so the docs make it mandatory. Stronger than V17's "Cowork-first, Claude Code for builds." The prose-only rewrite (parked in OPEN-QUESTIONS) is the carve-out for users who want the planning/build disciplines without the plugin.

- **Replacement wording: "during planning sessions" + "by hand."** The Cowork mentions weren't pure mentions — they were the *location* of fold-ins. Stripping without replacement would break sentences. The replacement keeps the mechanism (user does the editing, not Claude) and updates only the location. "By hand" makes the user-vs-agent distinction explicit: user opens file in editor and types; Claude Code agent can't write to SoT docs (PreToolUse enforced).

- **This project's own `CLAUDE.md` is unspecified, not Claude-Code-prescribed.** Alex is mid-personal-migration from Cowork to Claude Code with no fixed timeline. Pinning the dev location would force a date she doesn't have. Solution: strip the specification, leave to discretion.

- **Internal planning artefacts deliberately left alone.** PLAN.md, V27.md, OPEN-QUESTIONS' cross-version reconciliation entry retain Cowork refs. V23 scope was strict mentions-strip on user-facing content. Each resolves naturally when its session runs. `Archive/` and BUILD-LOG are historical record.

**Pivots and surprises.**

- **Crash course rewrite was bigger than a mentions-strip.** "Where each tool fits" was load-bearing structural framing — two tools used in sequence — and "Day one" described starting in Cowork and switching. Both framings wrong post-V23, so both got rewritten. Within scope per V23.md's anticipated "minor rephrasing," but Crash course's narrative voice changed measurably.

- **"Edit by hand during planning sessions" implies a soft discipline that didn't exist in the Cowork-tool era.** Under the original method, SoT docs were edited in Cowork (no file editor in builds), so the user *physically couldn't* edit `UX.md` during a build. Under V23, the user has a file editor available throughout — the discipline of "don't edit UX.md mid-build" is now *soft* (not hook-enforced; only Claude's edits blocked). Small new drift risk: a user editing UX.md mid-build would silently violate build-scope-locked. Not addressed in V23 (mentions-strip, not redesign); recorded for future.

- **Cowork session corruption from parallel sessions** during V23 prep (yesterday). Linux mount vs. Windows filesystem fight produced CRLF mangling across many files and silent truncation of `Archive/Version 10/NO-CODE-METHOD.md`. Recovered via `git restore .` after closing parallel sessions. Logged as memory (`reference_cowork_parallel_sessions_corrupt.md`). Not directly V23, but worth recording.

- **"Instructions" vocabulary miss.** Mid-session, I repeatedly failed to recognise that "the instructions" in Alex's vocabulary is Cowork's UI label for `CLAUDE.md`. Screenshot disambiguated. Logged as feedback memory.

**Carried forward.**

- **Live install + back-test of V18–V23** per existing OPEN-QUESTIONS entry. V23's changes — especially the rewritten `pre_tool_use.py` deny message and `session_start.py` recommendation — should be exercised in a real Claude Code session. Pre-install era's script-level validation isn't enough for user-facing prompt strings.

- **Soft-discipline risk for mid-build SoT edits** — above. If real use surfaces failure, consider a soft-warning hook (PostToolUse on manual SoT edit) or document the discipline in NO-CODE-METHOD → *Method contract*. Not pursued.

- **OPEN-QUESTIONS' Cowork-first cross-version reconciliation entry** still uses Cowork-first vocabulary. Substance (tripwire half folded in V21, worker half pending in V27) still valid; framing stale. Sweep when V27 ships.

- **`planning/sessions/V23.md` hand-delete** per CLAUDE.md and V21/V22 precedent — Alex deletes via Windows Explorer; Cowork bash mount can't delete due to ACLs.

- **Personal migration from Cowork to Claude Code** (Alex's workflow). Not encoded as method recommendation but informs this project's CLAUDE.md (now dev-tool-unspecified). Decoupled from any session.

---

## V22 — 2026-05-14 — Planning subagent + Serves-line PreToolUse hook

**What shipped.** Two plugin components landed and four method-side docs caught up.

- `plugin/agents/planning.md` is the plugin's first subagent. System prompt covers: inputs (the `primary_intent` line main Claude passes), always-on first action (read CLAUDE.md, path block, BACKLOG/MANIFEST/UX, plus NO-CODE-METHOD → *During planning* and DOC-STRUCTURE → *BACKLOG.md structure*), the three planning flows (test notes / feature request / scope question), mixed-input secondary sort that catches "by the way, can we add dark mode?" even when primary is test notes, always-run drift checks, BACKLOG editing protocol with Q3 Serves-line caveat, Discoveries → planning batches promotion, recap contract. Tools: `Read, Edit, Write, Glob, Grep` — no Bash (no scripts), no Task (subagents can't spawn subagents per V17).
- `plugin/hooks/pre_tool_use.py` gained the Q3 Serves-line check: parses every `Serves UX.md: <names>.` line in proposed new content, matches each name against UX.md's `## Functionalities` → `### ` entries with case-insensitive exact match after whitespace-trim, denies with redirect message listing unmatched names + sample of known entries. `Serves <ADDITIONAL>.md:` lines for additional SoT docs out of scope, pass through.
- NO-CODE-METHOD → *At session start* gained "Handoff to the planning subagent" defining four `primary_intent` values (`test notes`, `feature request`, `scope question`, `mixed (primary: ...)`) and the rule that main Claude relays the subagent's recap. *During planning*'s drift-check skip clause tightened to "always run; only skip case is 'nothing has been built yet'" (Q2 explicit). Crash course got a one-paragraph mention of the subagent split. DOC-STRUCTURE gained a Serves-line matching note.
- INVENTORY's planning-subagent and PreToolUse entries filled in with V22 state, D3 structurally corrected (SessionStart hooks inject context — they can't launch subagents; main Claude is the launcher). OPEN-QUESTIONS' direct-edit-users entry got a V22 note: shape #1 partially folded — file-level manual edits caught by drift check 2 now that it runs every session; in-file changes inside still-tracked files remain uncovered.
- Footer V21 → V22 across 15 files. `plugin.json` 0.21.0 → 0.22.0; `PLUGIN_METHOD_VERSION` 21 → 22.

**Decisions taken and why.**

- **Q1 — main Claude classifies primary intent at handoff; subagent still does mixed-input sort.** Classification is cheap and main Claude has to read the opener anyway. Doing it once in main Claude keeps the subagent prompt tight. Mixed-input openers still require the subagent to look at the opener a second time during the sort, so option (a)'s "classify once" doesn't eliminate the subagent's own scan — it just hints which flow to start in. Option (b) (subagent classifies itself) would unify location at the cost of a longer prompt. (a) wins on clarity-per-token.

- **Q2 — drift checks run every planning session; only skip is "nothing has been built yet."** A "skip when nothing built since last planning" rule would need a reliable signal for "since last planning," and there isn't one. More important: drift check 2 (MANIFEST.md ↔ codebase) is exactly the diff that surfaces manual code edits outside Claude's awareness — the direct-edit-user case in OPEN-QUESTIONS. A skip rule would defeat that. Cost when no diff is low (subagent reads, finds nothing); cost when a diff is missed is silent compounding drift. Asymmetric in favour of always-running.

- **Q3 — case-insensitive exact match after whitespace-trim; no fuzzy.** The hook's job is to catch "Claude proposed a build batch with no matching UX entry," which usually means Claude skipped the planning-batch → fold-in step. Fuzzy would let that slip whenever the made-up name *resembles* a real entry. Strict-enough-to-fail-fast. Case-insensitive-after-trim handles the only harmless variation (capitalisation in headers) without opening the door to ambiguous matches. Real typos by Claude are rare; deny message gives a one-round-trip fix.

- **Slash command `/plan` not shipped.** V22.md's success criteria require the auto-route path (paste test notes → main Claude classifies → planning fires). User-facing `/plan` listed in INVENTORY but not in V22 scope; can land later if auto-route proves insufficient, or stay deferred.

**Pivots and surprises.**

- **Web-search mid-build for the subagent file format.** Started V22 not knowing the YAML frontmatter shape, whether `subagent_type` was bare or plugin-namespaced, or whether `agents/` files auto-register. Wrote structured prompt for Alex to paste into Sonnet; she paste-backed `plugin-subagent-reference.md`. Key facts: `subagent_type` is `<plugin-name>:<agent-name>` (so `no-code-method:planning`); `description` drives auto-delegation; `hooks`, `mcpServers`, `permissionMode` silently ignored in plugin subagents; `agents/*.md` auto-register. Guessing wrong would have wasted a smoke-test cycle.

- **D3 in INVENTORY described a mechanism that doesn't exist.** V17 said "SessionStart auto-launches the planning subagent." Hooks inject context — they can't launch subagents. V21's actual implementation was correct (hook surfaces state; main Claude decides), but INVENTORY hadn't been updated.

- **Cowork bash mount stuck on pre-edit snapshot of pre_tool_use.py.** Bash saw 174 lines / May 13 timestamp; Read saw current 455. Same phantom-state issue as the existing memory note. Couldn't run `python -c "ast.parse(...)"` to verify syntax in-session. Eyeball review used; smoke test is the real validation.

- **Planning subagent's prompt deliberately delegates rule detail to NO-CODE-METHOD rather than restating.** Saved against Opus risk #5 (long subagent prompts eat their own context). Names doc sections to read first, lists only V22-specific clarifications + behavioural protocol. Tightness vs. self-containment is a real tension; preferring tightness for V22.

- **INVENTORY's slash-commands list described unshipped commands as if they existed — caught mid-smoke-test.** When the smoke test opened Claude Code in Taskflow, the planning subagent confidently recommended `/migrate`. `/migrate` doesn't ship until V26, but INVENTORY listed it (and five other future slash commands) without "pending" annotation. Fold-in fix in the same V22 commit: every entry now carries "**Shipped Vxx**" or "*Pending — Vxx*"; top-of-section preface states only `/init-project` is shipped. Audit missed this in first sweep; smoke test caught it. Same precedent as V21's plugin/templates footer catch.

- **The smoke test's auto-route check (Check 2) couldn't run in Taskflow.** Taskflow is tier 2 — its `CLAUDE.md` path block uses the pre-V18 bullet-list format and its spine docs lack the method-aware footer. SessionStart correctly classified tier 2; main Claude correctly declined to auto-route. All working, but Checks 2–4 (auto-route, Serves deny, case-insensitive accept) can't be exercised in Taskflow. Plan was to pivot to `v22-scratch` via `/init-project`; actual setup hit multiple side-quests (Alex ran `/init-project` from Taskflow's session; Claude recommended non-existent `/migrate`; loop-detection menu appeared third invocation). Resolved by closing Taskflow's session and starting fresh.

**Carried forward.**

- **Smoke test for V22** — for Alex post-commit. Suggested: (a) after `/reload-plugins`, confirm `plugin/agents/planning.md` in `/agents`; (b) in Taskflow, paste short test notes — verify main Claude classifies, spawns planning, recap returns; (c) ask Claude to add a build batch with a broken `Serves UX.md: NonExistentEntry.` — verify PreToolUse denies with redirect; (d) verify `Serves UX.md: <real entry, different case>` succeeds; (e) confirm V21's SessionStart still fires in a tier-3 project.

- **`planning/sessions/V22.md` hand-delete** per CLAUDE.md and V21 precedent.

- **`/plan` slash command** — not pursued. Future session can add it (one skill file in `plugin/skills/plan/`) if auto-route proves insufficient.

- **Cowork bash-mount staleness on pre_tool_use.py** — reproducible. No action; smoke test validates syntax-in-flight.

- **Direct-edit-users OPEN-QUESTIONS entry** — V22 partially folded shape #1. Shape #2 (developer-mode entry point), shape #3 ("Who this is for" doc section), and residual gap (in-file changes inside still-tracked files) remain.

---

## V21 — 2026-05-14 — SessionStart hook extension: three-tier detection + foundational reads + footer tripwire

**What shipped.** `plugin/hooks/session_start.py` extended from ~60 lines (V18's universal-rules emitter) to ~280 lines, now doing the full V21 scope. The hook reads project root from stdin JSON `cwd` field — not from `$CLAUDE_PROJECT_DIR`, which is broken for plugin hooks (anthropics/claude-code#9447); resolves CLAUDE.md; parses its fenced JSON path block; reads spine + any additional SoT docs; detects template state (`[Project Name]` placeholder); detects unfinished top build batch in BACKLOG (filtering template-placeholder titles); runs a version-footer mismatch tripwire — for every loaded SoT doc, compare `*No-code method — Version N.*` footer against `PLUGIN_METHOD_VERSION = 21`.

**Three-tier behaviour:**
- **Tier 1** (non-method folder — no CLAUDE.md and no method-footer spine docs): emits *nothing*, exits 0. Plugin invisible.
- **Tier 2** (partial method shape — four sub-cases between missing-CLAUDE.md-with-spine-docs and present-CLAUDE.md-with-unparseable-path-block): universal rules + single-paragraph gap flag naming the missing piece and pointing at `/init-project` or `/migrate`.
- **Tier 3** (complete method project): universal rules + full state summary, including a routing reminder that the hook does not classify the user's opener — Claude does.

Footer V20 → V21 across 8 method-side files. `plugin.json` 0.19.0 → 0.21.0 (V20 missed it). INVENTORY updated for new SessionStart shape; stale "added in V20" → V21. Project's outside-the-repo CLAUDE.md gained three rules: Cowork-first lean ("stay in Cowork; switch to Claude Code only when something needs a real session to be tested"), test-run guidance (Claude must explain plugin enabling and treat Alex's Claude Code inexperience as default), "Which CLAUDE.md is which" sub-section distinguishing the three (dev project, template, consumer).

Smoke-tested on Windows in `~\v21-scratch`: plugin loaded, both hooks registered, empty-folder verified tier 1 (silent), `/init-project` scaffolded cleanly, fresh session against the scaffold fired tier 3 — Claude reported 3 of 3 path entries resolved, template state in all four spine docs, routing reminder, version-footer mismatch tripwire (which surfaced the missed `plugin/templates/` footer bumps; see *Pivots*). Tier 2 in Taskflow not pursued — the mid-smoke tripwire catch already exercised the structural-mismatch code path; revisit only if real-world tier-2 misfires surface.

**Decisions taken and why.**

- **Tier 1 emits nothing — behaviour change from V18.** V18 injected universal-behaviour rules in *every* Claude Code session regardless of project. V21 narrows to method projects only. The argument for preserving V18 was "soft visibility never hurts"; for invisibility (won): the plugin should respect folders it has no claim on. If installed globally but working in 20 unrelated folders, those shouldn't get method-shaped noise.
- **Route signal is prose, not a structured marker.** Hook describes structural state; Claude classifies the opener. Only consumer is Claude. A structured marker (`ROUTE: planning`) was considered but later hooks would re-derive route from state anyway, and SessionStart can only *recommend* — Claude makes the final call after seeing the opener.
- **Tier-2 detection tightened via method-footer check.** V21.md flagged the false-positive risk: a non-method folder with an unrelated BACKLOG.md would trip tier 2. Fix: a spine doc counts only if it carries `*No-code method — Version N.*` footer.
- **Tripwire half of cross-version reconciliation folded into V21, worker half stays in V26.** Per OPEN-QUESTIONS' plan (which referenced V20 / V24 in pre-V20-renumbering terms; corrected to V21 / V26). Tripwire is a SessionStart-time read with no auto-fix; worker (diff-and-propose) lives in `/migrate`.
- **Method response to direct-edit users — not folded into V21.** Per OPEN-QUESTIONS' own logic. V21 adds reads + tiers + routing; none catch manual code edits. Natural home for "tighten drift detection" is V22 (drift logic inlined into planning); developer-mode and "Who this is for" shapes would warrant own sessions.
- **`plugin.json` bumped 0.19.0 → 0.21.0, skipping 0.20.0.** V20 was doc-only and didn't bump. Aligning plugin version with method version is more useful than walking every integer.

**Pivots and surprises.**

- **Workflow misframed early.** Initially described V21's implementation as happening in Claude Code, with this Cowork session as planning prep. Alex corrected: she builds the method itself in Cowork; Claude Code only enters for smoke-testing. Triggered the project-CLAUDE.md edits (Cowork-first lean, "Which CLAUDE.md is which"). The tagging question collapsed accordingly — this *is* V21.

- **"Which CLAUDE.md is which" confusion was real and worth pinning.** When discussing project-root detection, I used "the project's CLAUDE.md" without naming which — Alex's, the template, or Taskflow's. Plain confusion, fixed in the project's CLAUDE.md. Also surfaced that V19's `/init-project` skill (which she'd forgotten she'd shipped) already automates the template-copy-and-rename.

- **Sonnet's hook-environment summary was confident but unsourced.** Alex pasted it; I asked whether Sonnet had web-searched; she confirmed it hadn't. Direct fetch of source URLs confirmed: stdin `cwd` is documented hook input contract; `CLAUDE_PROJECT_DIR` is broken for plugins per #9447; sibling bug #11649 (`CLAUDE_ENV_FILE` empty in plugins) marked "Fixed in next release" — implies #9447 likely fixed similarly, but stdin is the correct path regardless.

- **`planning/sessions/V21.md` couldn't be deleted via Cowork's bash mount.** Permission denied per the existing memory. Hand-deletion via Windows Explorer baked into push instructions.

- **The version-footer tripwire caught a real oversight mid-smoke-test.** The session-close footer-bump pass covered `sovereign-implementer/templates/*.md` but missed `plugin/templates/*.md` copies — the templates `/init-project` actually scaffolds from. Tier 3 flagged the scaffolded docs as Version 20 while plugin reported Version 21. Fixed in the same commit. The two-directory template sync (V19 rule) is easy to miss because CLAUDE.md → *Session close* says "every template" without naming both directories. **The smoke test paid for itself with this catch alone.**

**Carried forward.**

- **Tier-2 detection rule may need tightening.** If real-world use surfaces false positives or negatives, revisit. For V21 ship, method-footer-in-spine-doc is the tightest signal available without parsing internal doc structure.
- **Method response to direct-edit users** — remains in OPEN-QUESTIONS, V21-vs-V20 reference corrected. Revisit during V22 planning at earliest.

**Build-log housekeeping (post-tag patch — V18 precedent).** Initial V21 entry was drafted partway through the session and listed the smoke test and V21.md hand-delete under *Carried forward* — items completed before the v21 tag. Smoke-test outcome folded into *What shipped*; V21.md hand-delete bullet removed; *Carried forward* now lists only items genuinely outstanding past V21.

---

## V20 — 2026-05-14 — Crash course promoted to source-of-truth doc; planning shifts

**What shipped.** Crash course.md became a parity-tracked source-of-truth doc — CLAUDE.md's doc-code-parity audit checklist gained a fifth item naming Crash course alongside spec docs, templates, INVENTORY. To earn that status the doc got a drift audit: `[FOLD-IN PENDING]` mechanism paragraph rewritten to describe the dedicated *Fold-ins pending* section (was still describing pre-V19 in-batch marker); three-sections-of-BACKLOG rationale block updated to four; prerequisite carve-out added to *Why batch scope is locked*; UX-principle-conflict surfacing added to *How a test note becomes a feature*; Method contract Required/Prohibited named in *What's editable*; *Where the actual files live* corrected (Taskflow repo → sovereign-implementer repo, version folders → git tags); user's locking-rationale phrasing landed at top of *Editing surfaces*.

Planning shifts: existing `V20.md`–`V27.md` renamed to `V21.md`–`V29.md` (this housekeeping became V20); new `V24.md` for TEST-LOG mechanism + protocol; `V23.md` (formerly V22, Before-build subagent) absorbed batch-sizing into scope. PLAN.md rewritten. New OPEN-QUESTIONS entry: *Cowork-friendly prose-only rewrite (post-plugin-build)*. Footer V19 → V20 across 15 files.

**Decisions taken and why.**

- **Crash course earns SoT status, but not by retrofitting unshipped work.** Initial proposal bundled two things: promote (yes) and pre-populate with V20–V27 scope file contents (no — those are explicitly provisional; writing them in would turn plans into authoritative prose). Promotion stands; fold-ins land session-by-session.
- **Cowork-first stays in the spec for now; de-Cowork-ification is a future deliverable.** Mid-session reconsideration. Current plugin-based method IS Claude-Code-specific — hooks, slash commands, `[FOLD-IN PENDING]` all need Claude Code primitives that don't exist in Cowork. Spec correctly documents reality. Cowork-friendly prose-only rewrite is a separate substantial deliverable, parked pending V29.
- **TEST-LOG.md is operational, sibling of MANIFEST.md.** Sonnet's V20 draft handed a clean shape. Re-categorised as operational (Claude updates during builds), dropped inside-doc "Version: 0.1" in favour of footer convention, distributed five protocol rules across NO-CODE-METHOD's existing phases rather than as one new section. V25's After-build will enforce the gate; V24 ships the prose.
- **Batch-sizing principle folds into V23, not its own session.** Small paragraph in *Before build* plus mid-build re-batching carve-out — bundling with V23 (Before-build subagent) keeps doc-code parity clean.

**Pivots and surprises.**

- **Stale `.git/index.lock` blocked session-file renames.** Zero-byte lock existed only on Linux mount's view (Windows reported no such file). `rm -f` failed with "Operation not permitted." `git mv` recreated its own lock. Workaround: plain `mv`, let git detect renames as 100% content matches at commit. Memory note if it reproduces.
- **Read-required-before-Edit caught the renames.** First batch of post-rename header bumps on V21.md and V23.md failed because they were Read pre-rename under old paths. Re-Read after rename, edits landed.
- **"Cross-version template reconciliation" OPEN-QUESTIONS framing weakened.** Pre-commits to "Cowork-first is now the recommended path"; the new Cowork-friendly-rewrite entry partially supersedes. Both stay; cross-version wording adjusts when the rewrite question resolves.

**Carried forward.**

- **Cowork-friendly prose-only rewrite of the method** — OPEN-QUESTIONS. Parked until V29; promote sooner if public release approaches.
- **TEST-LOG.md mechanism + protocol** — `sessions/V24.md`. Five rules, new operational doc class, new template, structural spec, fourth drift check.
- **Batch-sizing principle** — folded into `sessions/V23.md`. Three sub-rules + verification-burden recap + mid-build re-batching carve-out + Crash course parity item.
- **V27 scope reframed** — was "DOC-STRUCTURE migration + Crash course update"; now "DOC-STRUCTURE migration + Crash course coherence pass" since Crash course is parity-tracked. May need further tightening when V27 plans.

---

## V19 — 2026-05-13 — PreToolUse hook + bundled templates + /init-project + Fold-ins pending section

**What shipped.** The plugin now blocks edits to locked source-of-truth docs and gives Claude an unambiguous place to record the proposed change instead.

- `plugin/hooks/pre_tool_use.py` PreToolUse hook intercepts `Edit`, `Write`, `MultiEdit` against UX.md and any additional SoT doc declared in the project's CLAUDE.md path block. Returns deny decision telling Claude to add a `[FOLD-IN PENDING]` block to the new *Fold-ins pending* section of BACKLOG.md. Registered in `hooks.json` with `Edit|Write|MultiEdit` matcher.
- 5 templates bundled inside the plugin at `plugin/templates/` (copy of repo-root, both kept in sync via session-close footer-bump rule).
- New `/init-project` skill at `plugin/skills/init-project/` (`disable-model-invocation: true`, `user-invocable: true`) — Python scaffold script recursively scans `cwd` for the four destination filenames before writing, echoes target path for confirmation, refuses (pointing at `/migrate`) on conflicts.
- Structural rewrites for fold-ins pending: BACKLOG-TEMPLATE.md (×2), DOC-STRUCTURE.md BACKLOG.md section, NO-CODE-METHOD.md Editing surfaces + Fold-in vocabulary + per-route mentions.

Smoke-tested on Windows in a scratch dir: plugin loaded, both hooks registered, `/init-project` scaffolded cleanly and refused on non-empty, PreToolUse blocked an `Edit(UX.md)` attempt with deny visible, Claude pivoted to add the `[FOLD-IN PENDING]` block, the BACKLOG edit proceeded unblocked.

**Decisions taken and why.**

- **Templates at `plugin/templates/`, not nested inside `skills/init-project/`.** Originally drafted as `skills/init-project/templates/` (one consumer), revised after recognising templates also serve `/migrate` (V24) as reference structure to diff user-authored docs against. With multiple consumers, plugin-root is the right semantic home.
- **`/init-project` refuses on non-empty target, doesn't merge.** Recursive scan checks any of the four destination filenames anywhere under `cwd`. Cowork-first authoring is the expected path, so "user arrives with pre-drafted docs" is *normal* — and belongs to `/migrate`, not `/init-project`. Half-scaffolding would silently mix template-source and user-source. Refusal is louder and safer.
- **Hook denies with a redirect message rather than silently rewriting.** PreToolUse can technically rewrite an Edit's target via `updatedInput`, but doing so would silently transform UX.md writes into BACKLOG.md writes — magical, brittle (the hook would have to synthesize a `[FOLD-IN PENDING]` block from the raw edit), and against the method's "be told what's wrong, don't be silently rerouted" principle. Hard-block + reason keeps Claude in the loop.
- **`[FOLD-IN PENDING]` gets its own top-level section in BACKLOG**, between Red flags and Planning batches. Pre-V19 nested fold-ins inside the originating planning batch, but only the planning-batch-resolution route has a preceding batch — new-project, migration, and now the PreToolUse intercept all produce orphan blocks. Own section means one clear "things waiting for fold-in" location regardless of origin. Bigger rewrite to DOC-STRUCTURE and NO-CODE-METHOD than V19 scope said, but the alternative (hook deny referring to a section that doesn't exist in the template) was worse.

**Pivots and surprises.**

- **`${CLAUDE_PLUGIN_ROOT}` does expand inside skill bodies.** Flagged as real uncertainty in V19 plan ("may differ from hooks"); smoke test resolved on first try — `python "${CLAUDE_PLUGIN_ROOT}/skills/init-project/scripts/scaffold.py" check` expanded to full Windows path correctly.
- **Skill frontmatter shape works.** `disable-model-invocation: true` + `user-invocable: true` produced a working `/init-project` (visible as `/no-code-method:init-project`). No `agent:` key needed for skills that just run a script.
- **V18's universal-behaviour rules visibly self-policed on first hook test.** Asked to add a placeholder to UX.md, Claude refused before PreToolUse fired — citing UX.md "no placeholder entries" and offering three alternatives. The hook is a backstop, not the only line of defence. Forced the hook test with explicit "stress-testing, please attempt the edit anyway" — confirmed both layers work.
- **A Discovery surfaced mid-smoke-test.** Claude's first attempt at writing the fold-in block flagged that BACKLOG-TEMPLATE.md had no designated section for `[FOLD-IN PENDING]` — placed it at top of Planning batches with "this is my guess at the canonical location." That note made the structural rewrite (originally pushed to OPEN-QUESTIONS) part of V19's shipped work. Taking the user's "let's do it in V19 anyway" call was right.
- **Hook permission gates appeared at every Python invocation.** Claude Code's "approve commands" workflow: each `python ...` (the `check` call, then the `write` call) triggered its own dialog. Bothersome on a 4-step skill but correct — blanket approval would have been over-permissive. Note for Crash course in V25.
- **Test scratch dir lived outside the mounted workspace.** Alex created `~/v19-scratch` on Windows; smoke-test work happened in a Claude Code session pointing there, but I couldn't delete it myself (path outside mount). Handed back PowerShell `Remove-Item -Recurse -Force`. Confirmation that smoke-test directories don't need to be in mounted workspace folders.

**Carried forward.**

- **Cross-version template reconciliation** raised as OPEN-QUESTIONS entry — fold into V20 (tripwire in SessionStart) + V24 (worker in `/migrate`); entry removed when both folds confirmed.
- **Step 8 (subfolder-conflict test on Windows) not pursued:** recursive scan was verified in sandbox during V19 (`/tmp/scaffold_test2/docs/UX.md` caught as `docs/UX.md`, write refused with exit code 2). `pathlib`'s `rglob` and `name` matching are platform-agnostic; Windows path separators aren't a different code path. Skipping the live Windows test saved usage with negligible information loss.
- **V25 Crash course note:** document per-command Claude Code approval gate so first-time users know to expect dialogs at each Python invocation.

---

## V18 — 2026-05-12 — Plugin scaffold + SessionStart hook + JSON path block

**What shipped.** The plugin's bones now on disk at `plugin/`. Minimal `.claude-plugin/plugin.json`, `hooks/hooks.json` declaring a `SessionStart` hook, Python script (`session_start.py`) emitting the eight universal behavioural rules — push back, plain English, no stealth fixes, red-flag surfacing, the rest — as `additionalContext` at every session start. Rules text lives in `hooks/universal-behaviour.md` (copied from NO-CODE-METHOD → Method contract → Required of Claude; becomes canonical when NO-CODE-METHOD retires in V26). CLAUDE-TEMPLATE.md's path block changed from markdown bullets to fenced JSON so V19+ hooks can parse paths deterministically without grepping prose. Smoke-tested on Windows: `claude --plugin-dir <path>` loaded, `/hooks` showed `SessionStart` registered, Claude recited all eight rules verbatim.

**Decisions taken and why.**

- **Plugin lives inside the same repo (`sovereign-implementer/plugin/`), not a separate repo.** Method docs and plugin code co-evolve through V27 — every change touches both. One history beats threading version tags across two repos. Going one-repo to two later is cheap; the reverse is expensive.
- **Hook script language is Python, not bash or Node.** Bash has the shell-profile contamination risk Opus flagged in V17 and needs Git Bash on Windows. Node isn't bundled with Claude Code on Windows. Python is cross-platform, robust at parsing, and most readable for a non-coder debugging a hook.
- **Path block is JSON, not YAML.** Both parse from Python; JSON wins because it needs zero external deps (`json` is stdlib; `pyyaml` would be a plugin install dep), fails loudly on syntax errors, no quoting gotchas. Edited rarely — reliability beats prettiness.

**Pivots and surprises.**

- **`UserPromptSubmit` hooks in plugins don't execute** — GitHub `anthropics/claude-code#10225`. V18 was scoped to install one; pivoted to `SessionStart` (works in plugins, functionally equivalent given the method's `/clear`-after-every-build discipline). Saved to memory.
- **`${CLAUDE_PLUGIN_ROOT}` doesn't quote paths with spaces.** Smoke test failed silently first time because expanded path (`C:\Users\Alex\Desktop\Taskflow Planning\...`) got truncated at the first space — Python tried `C:\Users\Alex\Desktop\Taskflow` and gave up. Fix: wrap script path in escaped quotes in `hooks.json`. Future hook commands must follow this pattern; saved to memory.
- **Claude Code CLI wasn't installed on this machine.** Smoke testing required installing it via Anthropic's native PowerShell installer — adds ~30 min but overdue work (Claude Code CLI is Alex's stated Priority 1).
- **Two working-with-me rules added to project CLAUDE.md mid-session**, saved as feedback memories: (1) when uncertain about external facts, ask Alex to web-search rather than guessing; (2) format web-search requests as paste-able prompts for Sonnet, not questions to Alex.

**Carried forward.**

- V19+ hook commands all need the escaped-quote pattern from the start (memory + V19.md note).
- Crash course (V25) needs install instructions covering Python prerequisite, Claude Code CLI install, and the `where claude` diagnostic for the native+npm hook bug (memory in V17 work).
- `BUILD-LOG.md` itself added post-tag as a working-process improvement — separate small commit after the V18 tag.

---

## V17 — 2026-05-11 — Plugin-migration architecture decided

**What shipped.** Migration path from "method as markdown docs" to "method as a Claude Code plugin" scoped end-to-end. Produced `planning/INVENTORY.md` (final plugin component list — hooks, subagents, slash commands, bundled artefacts), `planning/PLAN.md` (session-by-session roadmap V18→V27), `planning/claude-code-plugin-feasibility-response.md` (Opus run grounding design in actual Claude Code capabilities). Created `planning/sessions/V18.md` through `V27.md` as provisional scopes. Switched versioning from numbered folders (`Version 3/` through `Version 16/` in `Archive/`) to git commits and tags (`v17`, `v18`, ...) — folders archived, going forward each session ships as one tagged commit.

**Decisions taken and why.**

- **Plugin layout = two-layer split.** Per-project SoT content (UX.md, BACKLOG.md, MANIFEST.md, CLAUDE.md, additional SoT docs) stays per-project. The mechanical method itself (process, schemas, behaviour contract) becomes the plugin. This split is the whole bet: discipline becomes structural (hooks deny) rather than prompt-based (Claude is asked to behave).
- **Stop hook proposes, user gates** (D1). Build sequencer single-steps one batch per user prompt rather than auto-chaining. `stop_hook_active` naturally prevents loops; explicit user gating matches the method's `/clear`-after-build discipline.
- **Drift checks inlined into planning subagent** (revision vs walkthrough). Subagents can't spawn subagents — Opus confirmed. Drift logic moves from a would-be `drift-checker` subagent into planning's instructions.

**Pivots and surprises.**

- **"Always-loaded core skill" idea collapsed under Opus's check.** Skill bodies are progressive-disclosure — never always-loaded. Universal behavioural rules had to move to a hook (V17 chose `UserPromptSubmit`; V18 pivoted to `SessionStart` after the plugin bug).
- **Slash commands and skills merged in Claude Code v2.1.101.** Slash commands now defined as skills with `disable-model-invocation: true` + `user-invocable: true` + `agent: <subagent>`. Roadmap depends on v2.1.101+ from V19 onwards.
- **V18 nearly became a research session.** Opus did the research live during V17, so V18 was promoted to the first real build session.

**Carried forward.**

- All plugin construction work — distributed across `V18.md` through `V27.md`.
- Risk of method instability during migration: explicitly accepted at V17 close. The plugin's per-component context isolation is the testability fix, not a freeze of an unstable method.
