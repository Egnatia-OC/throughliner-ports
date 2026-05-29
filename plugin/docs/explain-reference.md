# Explain reference — design rationale

Why each part of the method works the way it does. Read by `/sovexplain` via targeted offset/limit reads using the proxy at `explain-proxy.md`. Not a procedure doc — no instructions to follow.

---

## Session & phase management

### Session routing
The plugin detects project state and classifies the user's first prompt to load the right procedure doc. Without routing, every session opens with generic preamble and the user must manually direct Claude to the right workflow.

The routing table is priority-ordered — first matching row wins. Bug reports route to the planning procedure (they produce BACKLOG items). The classification is conservative to avoid false positives.

### Phase detection
Two phases — planning and build — with different editing permissions. Planning: source-of-truth docs editable, source code locked. Build: source code editable (on the file list), source-of-truth docs locked.

Phase detection uses file existence: `_method/active-build.md` present = build phase, absent = planning phase. This replaced an earlier mechanism that parsed status fields from BACKLOG, which had a flaw: all concurrent sessions saw the lock, not just the build session.

**Why two phases?** Without the split, Claude can edit anything at any time. This leads to spec drift (editing UX.md during a build without proper deliberation) or premature implementation (editing source code before the spec is settled). The phase boundary forces design decisions into planning and implementation into builds.

### Editing surfaces
Phase-aware permissions are enforced mechanically by PreToolUse hooks — Claude can't override them.

- **Planning phase:** source-of-truth docs (UX.md, additional declared docs) are read/write. Source code is locked.
- **Build phase:** source code on the batch file list is editable. Source-of-truth docs are locked. BACKLOG and MANIFEST stay writable in both phases.
- **Footer exception:** version-bump footer edits are metadata, not content — allowed on locked docs.
- **`[PROPOSED EDIT PENDING]`:** during builds, Claude sometimes spots a needed doc change while implementing. Rather than blocking entirely, this mechanism queues the change in a dedicated section. The user reviews it next planning session — observations aren't lost, but design changes still get proper deliberation.

### Build snapshot
When `/sovbuild` starts, it extracts the active batch from BACKLOG into a separate file (`_method/active-build.md`). Two purposes: (1) gives phase detection an unambiguous signal (file exists = build in progress), and (2) unlocks BACKLOG for parallel planning, deliberation, or ideation in other sessions.

When `/sovclose` finishes, the snapshot is deleted. The build-log entry is the shipped record.

### Close procedure
After a build, `/sovclose` runs quality gates: MANIFEST updates, test rows, build-log entry, doc-parity sweeps, proxy regeneration. Then `/sovgit` walks through commit, tag, and push.

**Why is close mandatory?** Skipping it leaves an orphaned snapshot (`_method/active-build.md`) that blocks all future builds. It also means missing build-log entries, unbumped footers, and uncommitted work. A PreToolUse guard blocks `git commit` when all batch files are ticked but close hasn't run.

**Why two turns?** The judgment pass (MANIFEST, tests, recap) fills context. A `/compact` between turns clears room for the mechanical pass (footers, proxies, checkpoint).

### Session handoff
Claude has no visibility into its own context-window usage. During long builds, compaction can silently drop critical context. PreCompact blocks `/compact` during active builds and surfaces a handoff prompt instead, so the user can start a fresh session.

Compact nudges fire at three points: pre-build sizing (8+ files AND open decisions), mid-session (15+ exchanges since `/sovbuild`), and between skill invocations. The triggers are advisory — skip if you prefer, but compacting preserves context for close steps.

---

## Planning skills

### /sovplan — structural planning
Confirms test results from the last build, runs five drift checks, and edits BACKLOG. Drift checks run every session because skipping them defeats manual-edit detection — direct edits going unnoticed is the core threat.

**Five drift checks, not one:** each catches a different kind of desynchronisation (file-temporal, feature-to-feature, name-to-name, purpose-level, per-row code-touch). Bundling them produces noise; separate passes catch what each is designed for.

### /sovrecap — before-build recap
Validates the upcoming batch before the user commits: checks the Serves line, populates file lists, proposes splits if the batch is too large. BACKLOG stays editable during the recap so the user can discuss and adjust — locking it prematurely blocks productive conversation.

### /sovdeliberate — open-question deliberation
Walks through accumulated open questions: promote to a batch, fold into an existing batch, drop, or keep parked.

**Why are OQs separate from batches?** Different lifecycle. OQs are non-blocking parking for things that need deliberation but shouldn't stall the build pipeline. A batch is a commitment to build; an OQ is a question that needs answering before it can become a batch (or get dropped).

### /sovideate — new ideas
Explores a fresh concept, checks overlap with existing work, and routes it to an OQ, batch, Ideas entry, or drop.

**Why not just add it to the backlog?** Ideas need triage. Some are OQs (need deliberation), some are batches (ready to scope), some overlap with existing work (fold in), some aren't worth pursuing (drop). The routing step prevents the backlog from accumulating unvetted entries.

---

## Build & testing

### /sovbuild — build execution
Locks the batch and works through the file list. PreToolUse enforces the file-list boundary mechanically — Claude can only edit files listed in the batch.

**Why only one batch at a time?** Without the boundary, Claude drifts across multiple batches or edits files not in scope. Scope creep during a build makes testing unpredictable and breaks the planning-gate filter.

### Test-confirmation gate
After a build, the user must confirm test results before the next build can start. PreToolUse blocks build-phase file edits when unconfirmed test rows exist.

**Why can't Claude just proceed?** Building on top of a broken change is worse than waiting. The gate ensures the user has seen and confirmed each test outcome rather than Claude proceeding on its own judgment.

### /sovtest — testing walkthrough
Guides the user through pending tests one row at a time, with type-specific instructions. Four test types: Look and click, Run and read, Trigger and observe, Generate and inspect.

**Why one at a time?** Bulk confirmations ("all tests passed") silently flip rows the user didn't actually verify. Row-by-row read-back means every confirmation is deliberate.

**Volunteered results:** if the user has already tested and brings specific per-row results, those are accepted without the guided walkthrough.

**No fixing inside testing:** if a test fails, Claude reports it and routes it to the next planning session rather than fixing it inline. Testing and building are separate phases.

### /sovrevert — rollback
Walks the user through undoing a failed build in plain English — no git knowledge required. Untracked file removal is a separate confirmation step (the user might want to keep build-created files).

---

## Method documents

### Proxy files
Large spine docs burn context window when Claude reads them whole, leaving less room for actual work. Proxies give Claude a lightweight index with line-number references so it can target-read specific sections instead.

Two kinds: **regenerated summaries** (UX, MANIFEST, test-log — Claude rebuilds from the source doc) and **proxy-as-index** (BACKLOG, build-log — directly edited, operationally authoritative).

### MANIFEST.md
Flat glossary of every named thing in the codebase: name, file path, description, and a one-line rationale (why it exists, with a session tag pointing to the build log for deeper context).

**Read-before-edit gate:** the first time Claude tries to edit a MANIFEST-covered file in a session, PreToolUse denies the edit and shows the MANIFEST entry inline. This forces Claude to have context about the feature before changing it. The retry succeeds — it's a one-time context injection, not a permanent block.

### UX.md
The app from the user's perspective. Every entry is something experienceable, with a rationale. Source of truth for what the product should do — separate from the backlog (work plan) and MANIFEST (component registry).

**Locked during builds** so design changes get proper deliberation in planning sessions. The `[PROPOSED EDIT PENDING]` mechanism (see Editing surfaces above) captures observations without blocking.

### BACKLOG
Work organized into discrete batches rather than a flat task list. Each batch has scope-context (Goal, Outputs, Success criteria, Decisions, Dependencies) separated from operational file lists by a `Changes:` delimiter.

Six sections: Red flags, Queued batches, Open questions, Ideas, Parked, Archive. Batch numbering uses 4-digit zero-padded IDs.

### Build log
Per-session record of what shipped, decisions made, pivots, and items carried forward. Per-entry files rather than a single growing file — Claude reads only relevant history, not the entire log.

### Test log
Per-session test files with 10 columns per row. Explicit confirmation required — Claude cannot infer completion from silence or bulk statements. Verified rows stay until component-based pruning removes them in the next planning session.

---

## Safety mechanisms

### Adoption gate
Prevents edits in folders that haven't adopted the method. Two layers: SessionStart advisory (soft, tells the user to run `/sovsetup`) and PreToolUse enforcement (hard, blocks Edit/Write/MultiEdit). The gate self-clears when `/sovsetup` completes.

**Why block edits?** The method's docs are the guardrails. Without them, Claude has no spec, no backlog, no test log — edits would be unguided and untracked.

### Git safety guard
Blocks `git reset --hard` and `git push --force` — the two commands most likely to destroy uncommitted work or overwrite remote history. `--force-with-lease` is allowed as the safe alternative. Mechanical backstop — Claude can't override a hook.

### Bash write guard
Shell commands could bypass the Edit/Write/MultiEdit guards. The bash write guard scans shell commands for file-write patterns (redirects, tee, etc.) and applies the same phase-aware rules. Null targets (`/dev/null`, `$null`, `NUL`) are treated as non-writes.

### PostToolUse validation
After Claude edits a method doc, a hook checks the result for structural correctness — parse errors, wrong column counts, missing sections. Warnings are advisory (not blocking) — Claude sees and self-corrects. Catching mistakes at write time prevents them from propagating into docs that other hooks depend on.

### Unclosed-build commit guard
Blocks `git commit` when all batch files are ticked but `/sovclose` hasn't run. Without it, committing would create a state where the build appears done but close outputs (build-log, MANIFEST, tests) are missing, and the orphaned snapshot blocks future builds.

---

## Behavioural rules

Rules in `universal-behaviour.md` that Claude follows as prose guidance. These are deliberately not mechanized — they govern judgment calls that hooks can't evaluate.

### Push back rather than agreeing
Drift checks and red-flag surfacing assume Claude will question things that look wrong. If Claude defaults to agreement, those safety nets are disabled in practice even though the code still runs.

### Plain language over jargon
The method targets non-coders. Build recaps assume plain-language output so the user can verify what was built without reading code.

### No stealth fixes
When Claude silently fixes a regression, the build recap becomes inaccurate — it records what shipped but omits the break-then-fix cycle. The rule requires explicit disclosure so the user has full visibility.

### Flag out-of-scope improvements
Prevents scope creep during builds without losing observations. Out-of-scope improvements get flagged at the end of the response and become discoveries in the next planning session.

### Red flags — screen and surface
Security, privacy, and safety concerns are never silently swallowed. Three outcomes: address now, attach to a planned feature, or defer with a BACKLOG Red flags entry.

### Verify external facts
Prevents wrong facts from entering source-of-truth docs when Claude guesses rather than verifying. `[UNVERIFIED: <what>]` markers serve as fallback when search tools aren't available.

### Route to artifacts, not memory
Memory writes bypass all plugin enforcement. Information that belongs in a structured artifact (BACKLOG, build log, research file) should be written there — memory is for cross-session context with no project-level home.

### Session-length awareness
Claude has no visibility into its own context-window usage. Compact nudges at three proxy signals give recovery points before context degrades.

### Walkthroughs one step at a time
Non-coders need sequential delivery. Bundled procedures cause confusion. The companion inversion: alternatives for choosing between go all at once (comparisons need everything visible).

### Never infer completion
Protects test-log integrity. Claude cannot mark rows confirmed based on absence of complaints or bulk statements. Every confirmation must be deliberate and per-row.

### Response-shape tags
Tags like `[SILENT]`, `[BRIEF]`, `[SEQUENCE]`, `[DISCUSS]`, and `[PROMPT]` let procedure docs specify not just what Claude does but how much it says. `[SEQUENCE]` means one step at a time. `[PROMPT]` means end with a clear next-action for the user.

---

## Setup & utilities

### /sovsetup — project setup
Detects four folder states and runs the right dialogue: empty folder, existing code without method docs, foreign docs present, already adopted. Nothing destructive without confirmation; every destructive option backs up first.

**Why four cases?** Each starting state needs different handling. An empty folder gets full scaffolding. Existing code needs analysis before docs are generated. Foreign docs need conflict resolution. Already-adopted projects need template refresh and migration.

### /sovresearch — research workflow
Identifies gaps where external information would improve a decision, drafts search queries, executes searches, and files results to `_method/research/`. Filing is mandatory — unfiled research is lost at session end.

**Why the discipline wrapper?** The value isn't the search itself — it's the structure: identifying what decision the research informs, filing results where future sessions can find them, and ensuring Claude researches rather than guesses.

### /sovtersify — doc compression
Triages source-of-truth docs by context-window cost, then audits and compresses user-selected targets. Planning phase only — source-of-truth docs are already locked during builds, and the triage analysis fills context that isn't needed during editing.

**Why compress?** Non-coders accumulate verbose documentation. Heavy docs burn context window, leaving less room for actual work. This directly addresses the method's core tension.

### /sovgit — git workflow
Plain-English walkthrough of commit, tag, and push. Detects first-time use and writes the project's git workflow to CLAUDE.md. The git safety guard (see Safety mechanisms) provides the mechanical backstop.

---

*No-code method — Version 103.*
