# Plan — V17 onwards

Session-by-session roadmap for the plugin migration. Companion to `INVENTORY.md` (this folder) and the Opus feasibility response (`claude-code-plugin-feasibility-response.md`, this folder).

## Versioning convention going forward

From V17 onwards, sessions are tracked as **git commits and tags** (`v17`, `v18`, ...) rather than version folders. One session = one commit (or set of commits) ending with a version tag. The version footer at the bottom of each method file (`*No-code method — Version N.*`) stays as a human-readable hint of which snapshot you're reading; it gets updated as part of the commit when the version changes.

Per-session scopes for V18 onwards live as `sessions/V18.md`, `V19.md`, etc. **The session files are PROVISIONAL.** If the plan changes mid-track — sessions reordered, merged, split, or skipped — the files should be renamed, deleted, or merged. A file existing isn't a commitment to do that session in that order.

When a future session runs, its plugin code (hook scripts, subagent definitions, skill bodies, slash command definitions) lands in a `plugin/` subfolder of the repo root (created when the first plugin code arrives in V18).

## The session list

| V# | Session | Output |
|---|---|---|
| V18 | Path block format + plugin scaffold + `SessionStart` hook (universal-behaviour rules) | `templates/CLAUDE-TEMPLATE.md` path block in fenced JSON; plugin skeleton; SessionStart hook installed (originally planned as UserPromptSubmit; pivoted to SessionStart due to anthropics/claude-code#10225) |
| V19 | Read-only PreToolUse hook + bundled templates + `/init-project` skill-command | Lock enforcement; templates scaffolded by slash command; tested on Taskflow |
| V20 | SessionStart hook — extend with foundational reads + routing | V18's SessionStart hook gains foundational reads (CLAUDE.md, path block, SoT docs), template-state detection, resume detection, and routing logic; tested |
| V21 | Planning subagent (drift logic inlined) + Serves-line PreToolUse hook | Planning loop end-to-end; tested |
| V22 | Before-build subagent + batch-executor + Stop hook + supporting PreToolUse hooks | Build orchestration core (the user's two main motivating examples); tested |
| V23 | After-build subagent | MANIFEST auto-update + build recap; tested |
| V24 | New-project + migration skill-commands and subagents | "Starting a project" flows; tested |
| V25 | `DOC-STRUCTURE.md` content migration + Crash course update | Schema content moved into plugin; Crash course brought current |
| V26 | `NO-CODE-METHOD.md` retirement / cleanup | Original method files retired or pointed at plugin |
| V27 | End-to-end Taskflow test | Refinement list; possibly more sessions |

10 sessions. Some will combine or split during execution; the count is a target, not a contract.

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
