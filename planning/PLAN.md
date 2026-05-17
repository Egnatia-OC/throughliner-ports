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
| V26 | **TEST-LOG.md mechanism + protocol (consumer-side)** | New operational tracking doc, template, structural spec, five protocol rules placed across method phases, fourth drift check (for projects that use the method — distinct from this project's TEST-LOG.md shipped in V24) |
| V27 | After-build subagent (enforces V26 test-confirmation gate) | MANIFEST auto-update + build recap + test-confirmation gate; tested |
| V28 | **Walkthrough-mode for non-UI testing** | Build batch declares its test mode (UI-testable vs. needs-walkthrough); Before-build captures the declaration; the After-build subagent (V27) branches — producing plain-English recap or step-by-step `[SEQUENCE]`-tagged smoke-test walkthrough; tested |
| V29 | Safety net (untrusted-folder detection at session start) + unified `/adopt` skill-command | SessionStart hook extended with untrusted-folder halt via `systemMessage`; `/init-project` (V19) + new-project + migration unified into `/adopt` with four case branches (empty / existing code no docs / existing code foreign docs / already method-managed); method-doc rewrites for the rename and for folding *New-project route* + *Existing-docs migration route* into `/adopt`'s case branches; script-validated only (live-install deferred) |
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
