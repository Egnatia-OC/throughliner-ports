# Feature inventory for /explain skill — "why" questions

Phase 1 output: what exists now and what "why" questions each feature raises.
Next step: mine build log for the answers, then enrich consumer docs.

---

## A. Workflow lifecycle

### 1. Session routing (SessionStart + UserPromptSubmit + universal-behaviour.md routing table)
- Detects project state (unadopted, template-state, build-in-progress, idle)
- Classifies the user's first prompt into a routing category
- Routes to the correct procedure doc
- **Why questions:** Why does it route automatically? Why can't I just start working? Why does it care about my first message?

### 2. Phase detection (planning phase vs build phase)
- Planning = no `_method/active-build.md`; build = file exists
- Legacy fallback: `Status: active` on top batch
- **Why questions:** Why are there two phases? Why can't I edit code during planning? Why can't I edit UX.md during a build?

### 3. Editing surfaces (phase-aware doc locking)
- Planning: source-of-truth docs editable, source code locked
- Build: source code on file list editable, source-of-truth docs locked
- Footer exception for version bumps
- `[PROPOSED EDIT PENDING]` mechanism for build-phase doc changes
- **Why questions:** Why does it block my edits? Why can't Claude just edit everything? What is `[PROPOSED EDIT PENDING]`?

### 4. Build snapshot (`_method/active-build.md`)
- `/sovbuild` extracts active batch into snapshot, freeing BACKLOG for parallel sessions
- Phase detection shifts to file existence
- Snapshot shrinks after re-batching carve-outs
- **Why questions:** Why does it copy the batch to a separate file? Why not just work from BACKLOG directly?

### 5. Close procedure (mandatory, not advisory)
- Post-build: MANIFEST update, TEST-LOG rows, build recap, build-log entry, snapshot deletion, doc-parity/staleness/frame-correction sweeps
- Planning/general: lighter close with idea sweep, build-log, proxy regen
- PreToolUse enforces: `git commit` blocked when all Files: ticked and close hasn't run
- **Why questions:** Why can't I just commit? Why is the close so long? What happens if I skip it?

### 6. Session handoff (PreCompact blocks compaction during builds)
- PreCompact blocks `/compact` during active build
- Recommends preparing a handoff before fresh session
- **Why questions:** Why can't I compact during a build? Why not just continue?

---

## B. Planning & scoping

### 7. Planning procedure (`/sovplan`)
- Test-result close, drift checks, BACKLOG edits
- Five drift checks: direct-edit, UX-build, MANIFEST-codebase, MANIFEST-UX, TEST-LOG-code-touch
- **Why questions:** Why does planning start with test results? What are drift checks? Why five?

### 8. Before-build recap (`/sovrecap`)
- Validates top batch, blocker gate (OQs, unconfirmed tests), file-list enumeration, batch sizing
- **Why questions:** Why can't I just build? What's a blocker gate? Why does it check test results from last time?

### 9. Open-question deliberation (`/sovdeliberate`)
- Walk-through of OQs: promote, drop, re-park
- **Why questions:** Why are open questions separate from batches? Why walk through one at a time?

### 10. Ideation (`/sovideate`)
- Explores ideas, checks overlap, routes to OQ/batch/Ideas/drop
- **Why questions:** Why not just add it to the backlog? Why the routing step?

---

## C. Build mechanics

### 11. Build procedure (`/sovbuild`)
- One batch at a time, ticks files in snapshot
- Carve-out mechanisms (prerequisite, re-batching)
- **Why questions:** Why only one batch? What if I want to change scope mid-build?

### 12. Test-confirmation gate (PreToolUse)
- Blocks new build when previous batch has unconfirmed TEST-LOG rows
- **Why questions:** Why can't I start the next build? Why do tests have to be confirmed?

### 13. Testing walkthrough (`/sovtest`)
- One row at a time, type-specific guidance, no fixing inside testing
- Cowboy test exemption for volunteered results
- **Why questions:** Why one at a time? Why can't Claude just fix what failed? What's a cowboy test?

### 14. Revert procedure (`/sovrevert`)
- Plain-English walkthrough to undo a failed build
- **Why questions:** Why can't Claude just undo it? Why the confirmation step?

---

## D. Doc infrastructure

### 15. Proxy files (`_method/proxies/`)
- Lightweight summaries with line numbers for targeted reads
- **Why questions:** Why not just read the whole file? What's a proxy?

### 16. MANIFEST.md (feature registry with rationale)
- Entry format includes inline rationale suffix with session tag
- Serves-line links features to UX entries
- PreToolUse requires reading MANIFEST entry before editing a MANIFEST-pathed file
- **Why questions:** Why do features need rationale? Why does it make me read MANIFEST before editing?

### 17. UX.md (user-experience spec)
- Source of truth for what the product should do
- **Why questions:** Why is UX separate from the backlog? Why is it locked during builds?

### 18. BACKLOG.md / BUILD-PLAN (batch-structured work plan)
- Six sections: Red flags, Queued batches, Open questions, Ideas, Parked, Archive
- Batch structure with scope-context and build-operations regions
- **Why questions:** Why batches instead of a flat list? Why six sections? What's the difference between an OQ and an Idea?

### 19. Build log (`_method/build-log/`)
- Per-session record: what shipped, decisions, pivots, carried forward
- **Why questions:** Why keep a build log? Why per-session?

### 20. TEST-LOG (`_method/test-log/`)
- 10-column format, per-session files
- Explicit confirmation required
- **Why questions:** Why 10 columns? Why explicit confirmation? Why per-session?

---

## E. Safety & quality

### 21. Adoption gate (SessionStart + PreToolUse)
- Blocks edits in unadopted folders, recommends `/sovsetup`
- **Why questions:** Why can't Claude just start working? What does "adopted" mean?

### 22. Git safety guard (pre_tool_use_git_guard.py)
- Blocks `git reset --hard` and `git push --force` via Bash
- **Why questions:** Why block these? Can't I decide for myself?

### 23. Bash write guard
- Blocks file-write patterns targeting denied paths via Bash/PowerShell
- **Why questions:** Why can't I use Bash to write files? Why the restriction?

### 24. Read-before-edit gate (PreToolUse)
- First edit on a MANIFEST-pathed file denied with entries inlined; retry succeeds
- **Why questions:** Why does it block my first edit? Why show me MANIFEST?

### 25. PostToolUse validation
- Validates structured doc format after edits (BACKLOG parse, TEST-LOG columns, build-log sections, proxy headers)
- **Why questions:** Why does it check my formatting? What if I want a different format?

### 26. Unclosed-build commit guard (PreToolUse)
- Blocks `git commit` when all Files: ticked but `/sovclose` hasn't run
- **Why questions:** (Same as close procedure #5)

---

## F. Behavioural rules (universal-behaviour.md)

### 27. Push back rather than agreeing
- **Why:** Drift checks and red-flag surfacing depend on it

### 28. Plain language over jargon
- **Why:** Build recaps assume plain-language output; user is a non-coder

### 29. Language: field support
- **Why:** Non-English users; control tokens stay English for hook regex

### 30. No stealth fixes
- **Why:** Build recaps assume regressions are stated

### 31. Flag out-of-scope improvements
- **Why:** Flag taxonomy relies on flagging, not fixing

### 32. Red flags — screen and surface
- **Why:** Security/privacy/safety concerns need structured routing

### 33. Verify external facts, don't guess
- **Why:** Wrong facts contaminate source-of-truth docs

### 34. Route information to artifacts, not memory
- **Why:** Memory is invisible to the structured workflow

### 35. Session-length awareness (compact nudges)
- **Why:** ~20% of sessions blow out; nudges give recovery points

### 36. Walkthroughs one step at a time
- **Why:** Non-coder user; bundled procedures cause confusion

### 37. Never infer completion
- **Why:** Test-confirmation gate integrity

### 38. Response-shape tags ([SILENT], [BRIEF], [SEQUENCE], [DISCUSS], [PROMPT])
- **Why questions:** What do these tags mean? Why does Claude sometimes give short answers?

---

## G. Setup & onboarding

### 39. Setup procedure (`/sovsetup`)
- Four cases: empty folder, existing code no docs, foreign docs, already adopted
- Case 4: template refresh, structural migrations, footer bumps
- **Why questions:** Why four cases? What does setup actually create? Can I undo it?

### 40. Research workflow (`/sovresearch`)
- Drafts search queries, files results to `_method/research/`
- **Why questions:** Why file research? Why not just answer from memory?

### 41. Tersify procedure (`/sovtersify`)
- Doc compression: triage then audit
- **Why questions:** Why compress docs? Why planning phase only?

### 42. Git workflow (`/sovgit`)
- Plain-English walkthrough, detects first use, writes Git workflow to CLAUDE.md
- **Why questions:** Why the walkthrough? Why write the workflow to CLAUDE.md?

---

**Total: 42 features/mechanisms that could generate "why" questions.**
