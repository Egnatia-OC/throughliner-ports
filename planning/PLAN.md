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
| V31 | `NO-CODE-METHOD.md` retirement / cleanup | Original method files retired or pointed at plugin |
| V32 | End-to-end Taskflow test | Refinement list; possibly more sessions |

15 sessions. Some will combine or split during execution; the count is a target, not a contract.

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
