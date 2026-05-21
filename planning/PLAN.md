# Plan — V17 onwards

Session-by-session roadmap for the plugin migration. Companion to `INVENTORY.md` (this folder) and the Opus feasibility response (`claude-code-plugin-feasibility-response.md`, this folder).

## Versioning convention going forward

From V17 onwards, sessions are tracked as **git commits and tags** (`v17`, `v18`, ...) rather than version folders. One session = one commit (or set of commits) ending with a version tag.

**Session tag vs. method version** — these are two different things. The session tag increments per session; the `*No-code method — Version N.*` footer at the bottom of every method-side file (and `PLUGIN_METHOD_VERSION` in `session_start.py`, and `plugin.json` `version`) only bumps when the session **substantively changes the method or plugin**. Dev-internal-only sessions (BUILD-METHOD edits, BUILD-LOG entries, TEST-LOG appends, planning artefact reshuffles) ship with the footer unchanged. Full rule in `BUILD-METHOD.md` → *Session tag vs. method version*.

Per-session scopes for V18 onwards live as `sessions/V18.md`, `V19.md`, etc. **The session files are PROVISIONAL.** If the plan changes mid-track — sessions reordered, merged, split, or skipped — the files should be renamed, deleted, or merged. A file existing isn't a commitment to do that session in that order.

When a future session runs, its plugin code (hook scripts, subagent definitions, skill bodies, slash command definitions) lands in a `plugin/` subfolder of the repo root (created when the first plugin code arrives in V18).

## The session list

| V# | Session | Output |
|---|---|---|
| V18 | Path block format + plugin scaffold + `SessionStart` hook (universal-behaviour rules) | `templates/CLAUDE-TEMPLATE.md` path block in fenced JSON; plugin skeleton; SessionStart hook installed (originally planned as UserPromptSubmit; pivoted to SessionStart due to anthropics/claude-code#10225). **Shipped.** |
| V19 | Read-only PreToolUse hook + bundled templates + `/init-project` skill-command + Fold-ins pending section | Lock enforcement; templates scaffolded by slash command; structural rewrite for Fold-ins pending section; tested on Taskflow. **Shipped.** |
| V20 | Crash course promoted to source-of-truth doc; parity audit; planning-list shifts | Crash course brought current; CLAUDE.md parity rule extended to Crash course; OPEN-QUESTIONS entry for the prose-only rewrite. **Shipped.** |
| V21 | SessionStart hook — extend with foundational reads + routing | V18's SessionStart hook gains foundational reads (CLAUDE.md, path block, SoT docs), template-state detection, resume detection, and routing logic; tested. **Shipped.** |
| V22 | Planning subagent (drift logic inlined) + Serves-line PreToolUse hook | Planning loop end-to-end; tested. **Shipped.** |
| V23 | **Remove Cowork mentions from method docs** | Method docs strip Cowork; Claude Code becomes the explicit required tool; this project's `CLAUDE.md` unspecifies dev location. **Shipped.** |
| V24 | **`BUILD-METHOD.md` + `TEST-LOG.md` — dev-internal working manual and test record** | `BUILD-METHOD.md` consolidates session structure / doc-code parity / testing semantics / artefact lifecycles (lifted out of old `CLAUDE.md`); `TEST-LOG.md` created with V18/V19/V21/V22 backfill; CLAUDE.md slimmed and ghost-reference corrected; session tag vs. method version decoupled going forward. **Shipped.** |
| V25 | Before-build subagent + batch-executor + Stop hook + supporting PreToolUse hooks; **batch-sizing principle** | Build orchestration core (the user's two main motivating examples); batch-sizing optimised for verification burden; tested |
| V26 | **TEST-LOG.md mechanism + protocol (consumer-side) + V25 carry-over bugfixes + Drafts in flight convention** | New operational tracking doc (TEST-LOG.md, 8-column spec), template + plugin-side copy, structural spec in DOC-STRUCTURE.md, five protocol rules placed across method phases (with Rule 2 relocated mid-session from *After every build* to *During planning* per Q4), fourth drift check. V25 carry-over bugfixes: parse_backlog.py placeholder detection, BACKLOG-TEMPLATE.md de-collision (both copies), before-build.md parser invocation fix + sweep-bonus fix to /build slash command. Session-open recovery: `BUILD-METHOD.md` *Drafts in flight* convention + `CLAUDE.md` session-open scan rule + `planning/drafts/` folder. scaffold.py extended to scaffold TEST-LOG.md as the fifth spine template. **Shipped.** |
| V27 | After-build subagent (enforces V26 test-confirmation gate) | MANIFEST auto-update + build recap + test-confirmation gate; tested |
| V28 | **V27 fix sweep — test-confirmation gate becomes functional** | Three V27 bugs from same-day Windows smoke testing: `WRITABLE_LOGICAL_NAMES` excluded TEST-LOG.md (after-build's row-open writes denied); Stop hook wasn't TEST-LOG-aware (derailed planning's read-back); gate visibility on Stop-hook-redirected Task calls uncertain. Shared helpers extracted to `plugin/scripts/project_state.py`. AB2 retest passes end-to-end via fresh g4 fixture; full chain — Stop hook → after-build → TEST-LOG.md row open → SessionStart tripwire → planning read-back → row close — confirmed working. Walkthrough-mode-for-non-UI-testing (this row's prior content) dropped: never had a matching `sessions/V28.md`, V27's after-build "What to test" covers the use case at narrative altitude. **Shipped.** |
| V29 | Safety net (unadopted-folder detection at session start + PreToolUse enforcement) + unified `/adopt` skill-command | Two-hook architecture (Path D): SessionStart extended with unadopted-folder detection emitting `systemMessage` + `additionalContext` advisory; PreToolUse extended with enforcement gate that denies Edit/Write/MultiEdit and Task → method-subagent calls from main Claude when folder is unadopted (mechanism replaces the originally-scoped `systemMessage` halt at SessionStart, which Claude Code's hook protocol doesn't support — anthropics/claude-code#10225 → #12151). `/init-project` (V19) + new-project + migration unified into `/adopt` with **five** case branches (empty / existing code no docs / existing code foreign docs / already method-managed / opted out via `.no-code-method-skip` marker); method-doc rewrites for the rename and for folding *New-project route* + *Existing-docs migration route* into `/adopt`'s case branches; live-tested via `claude --plugin-dir`. |
| V30 | `DOC-STRUCTURE.md` content migration + Crash course coherence pass | Schema content moved into plugin; final coherence read across Crash course before public release |
| V31 | **Planning — rescope OPEN-QUESTIONS into sessions** | Four promotion-ready entries from OPEN-QUESTIONS folded into V33/V34. V32–V35 numbering shifted accordingly. New `sessions/V33.md` + `V34.md` scope files; remaining OPEN-QUESTIONS entries retargeted V31+ → V36+. Dev-internal-only; no footer bump. |
| V32 | `NO-CODE-METHOD.md` retirement / cleanup | Original method files retired or pointed at plugin |
| V33 | **Consumer-side audit trail + frame-correction sweep** | Consumer `BUILD-LOG.md` (new spine doc + template); `planning/drafts/<topic>.md` pattern for consumer projects; frame-correction sweep at *After every build*. Combined because all three touch the same docs/components. |
| V34 | **Consumer-method git workflow** | *Recommended habits* line ("tag and push after every shipped build batch") + PreToolUse safety-guard hook against `git reset --hard` / `git push --force`. Stop-hook auto-commit deferred to a later opt-in session. Consumes `planning/drafts/git-integration-research.md`. Cowork drift cleanup (4 line-level fixes across 3 files). V36 scope created (OPEN-QUESTIONS doc-only bundle). **Shipped.** |
| V35 | End-to-end Taskflow test | First plugin run against real Taskflow (not synthetic fixture). Validated `/adopt` case 1 (cold-start adoption) and case 4 (refresh after real planning docs swapped in); planning subagent reached Q1 of 5 of a [SEQUENCE] before halting (questions clashed with decisions already settled in Alex's separate planning project). Build / before-build / after-build not exercised — folds into normal Taskflow use. Two new OPEN-QUESTIONS entries (`/adopt` permission-prompt UX; footer-stamp on locked docs). Marketplace path researched — surfaces V37. Dev-internal; no footer bump. **Shipped.** |
| V36 | **Doc-only: TEST-LOG ordering, planning's BACKLOG authority, plan-panel research** | Three small open-question resolutions bundled because they don't interact: flip TEST-LOG.md to newest-first (split from row pruning, which still needs Taskflow row-count data); one-line assertion of planning's structural authority over BACKLOG.md in *During planning*; web-search check on whether Claude Code's plan panel is programmatically writable (research half only — design half stays parked). Doc-only; no smoke test. |
| V37 | **Marketplace.json + local install** | Add `.claude-plugin/marketplace.json` at repo root with relative `source: "./plugin"` (works for both local and future public GitHub distribution per V35 research). Run `claude plugin validate .`. Install locally via `/plugin marketplace add ./sovereign-implementer` + `/plugin install no-code-method@<marketplace-name>`. Smoke-test that hooks/agents/commands all fire in a normal (non-`--plugin-dir`) Claude Code session against a scratch fixture. Plugin-side packaging change — warrants footer bump. Decisions to make in-session: marketplace `name`, `owner.name`, whether to add a top-level README, whether to ship a license. Consumes `research/plugin-marketplace-scoping.md`. |
| V38 | **Locked-doc edit rules + Sonnet-search discipline** | Footer-stamp carve-out on locked docs; `[PROPOSED EDIT]` mechanism for planning-time source-of-truth edits with no-coder permission; Sonnet-search discipline as a required behaviour in `universal-behaviour.md`. Three OPEN-QUESTIONS entries resolved. Touches PreToolUse locked-doc check, `DOC-STRUCTURE.md` (both sides), `adopt.md`, Crash course. |
| V39 | **MANIFEST paths field + shape B enforcement** | MANIFEST.md gains a paths field (decided). Shape B (inline deny-with-context) PreToolUse enforcement for read-before-edit rule (decided). Incremental migration for existing entries; one-time backfill via `/adopt` case 4. One OPEN-QUESTIONS entry resolved (MANIFEST schema gap). Split from original V39 — drift detection moves to V40. **Shipped.** |
| V40 | **Shelve the two-write rule for canonical docs** | Dev-internal. Repo-root docs-only set (`NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md`, `templates/`) frozen at method version V39; plugin side becomes sole operational source. Updates `BUILD-METHOD.md` (session-open reads, doc-code parity, footer-bump list, two-write section), the project root `CLAUDE.md`, `INVENTORY.md`, `OPEN-QUESTIONS.md` (one entry resolved), `PLAN.md`, `README.md`, and plugin-side prose references. Method version stays at V39 (no footer bump). |
| V41 | **Git-diff drift detection + direct-edit confirmation protocol** | (Renumbered from V40 in session v40.) Git-diff based detection of in-file content changes at planning-session start (decided). Per-change confirmation protocol: user confirms each flagged change, Claude checks for build-batch conflicts, accepts + doc catch-up if clean. Resolves remaining shapes from V22 partial fold-in. One OPEN-QUESTIONS entry resolved (direct-edit users — shapes #2/#3 deferred). Depends on V39 paths field. |
| V42 | **Vocabulary sweep / non-GUI generalisation** | (Renumbered from V41 in session v40.) Generalise "user-observable behaviours" for non-GUI projects; disambiguate method "planning" from Claude Code "plan mode." Single grep-and-rewrite pass across plugin-side canonical docs, subagent bodies, plugin templates, Crash course. Two OPEN-QUESTIONS entries resolved. **Note:** bundling rationale dissolved with v40's two-write shelving — the two questions may still ship together for surface-area reasons, or split. Decide at session start. |
| V43 | **/adopt UX + per-project opt-out** | (Renumbered from V42 in session v40.) End-to-end `/adopt` test via marketplace install on a fresh folder. Permission-prompt surface under marketplace install. Per-project opt-out UX — obvious off-ramp for users who don't want the method (`.no-code-method-skip` via `/adopt` leave-alone is non-obvious; may add `/skip` command). `/adopt` narration improvements. CLI vs. desktop-app input parity. |
| V44+ | Remaining parked open questions | Automated CI (parked — revisit on regression escape or surface growth); TEST-LOG row pruning (parked — needs real Taskflow row count); subagent rule-loading divergence (parked — targets shifted V32, same tension); Stop-hook 8-block cap (parked); AEX-style DEX/HEX (parked); restoration of two-write maintenance if a real audience for the prose-only set emerges (parked — shelved in v40); graduation of sovereign-implementer's own dev onto the method (parked — meta-entry in OPEN-QUESTIONS). Each becomes its own session row when promoted. |

26 sessions through V43, plus V44+ TBD. Some will combine or split during execution; the count is a target, not a contract.

## Session-scope file shape

Each `sessions/Vxx.md` follows this shape:

```markdown
# Vxx — [Session Name]

## Goal
[One paragraph: what this session aims to produce.]

## Inputs
[What docs/files the session reads / depends on.]

## Outputs
[What this session produces: new files, edited files, plugin components.]

## Success criteria
[How we know the session succeeded. Usually: thing built, tested in Taskflow, working.]

## Open questions for this session
[Any open design questions to resolve in this session.]

## Risks / dependencies
[What could derail this session. Dependencies on prior sessions.]
```
