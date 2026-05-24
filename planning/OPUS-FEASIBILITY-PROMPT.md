# Claude Code plugin feasibility check — prompt for Opus

*Paste into fresh Opus chat with web search. Bring the response back.*

---

I'm converting a structured workflow ("no-code method") into a Claude Code plugin. Need to confirm what's possible before committing to architecture. **Use web search** — current answers, not training-data guesses. Cite Anthropic docs. If unsure, say so.

## Context

No-code developer. Method currently governs Claude Code via markdown docs (NO-CODE-METHOD.md, DOC-STRUCTURE.md, CLAUDE.md). Plugin distributes rules across hooks/subagents/skills for **structural, not prompt-based** adherence.

## What the plugin needs to do

1. **Read-only enforcement.** Block Edit/Write on source-of-truth files (`UX.md`, etc.). Locked list in CLAUDE.md path block. Hook reads CLAUDE.md at decision time.
2. **Batch sequencing.** BACKLOG.md lists build batches. On turn end, detect next unticked batch and redirect.
3. **Isolated batch execution.** Fresh subagent context per batch; only declared files visible.
4. **Session-start orientation.** Read CLAUDE.md, resolve paths, detect state (template/filled-in/unfinished), route to right mode.
5. **Always-loaded behavioural rules.** Universal rules firing every turn, not on-demand.
6. **Multiple subagents:** planning, drift-checker (called by planning), before-build, batch-executor, after-build, new-project, migration.
7. **Slash commands** launching subagents (`/new-project`, `/migrate`, etc.).
8. **Bundled templates** (5 markdown files) scaffolded by slash command.
9. **Bundled docs** ("crash course") shipping with plugin, not loaded into context.

## Questions

### Hooks
1. **SessionStart.** Exists? Read project files + inject context?
2. **PreToolUse.** Exists? (a) block, (b) read files, (c) modify/redirect, (d) structured feedback?
3. **Stop.** Exists? (a) read files, (b) `{"decision":"block","reason":"..."}`, (c) inject continuation?
4. **Execution context.** Languages? Filesystem/network access?

### Subagents
5. Configuration — system prompt, tool restrictions, context isolation?
6. Can a subagent invoke another subagent?
7. File-restricted subagents possible?
8. Genuinely isolated contexts (no history carryover)?

### Skills
9. Always-loaded vs on-demand?
10. Cross-phase behavioural influence?

### Slash commands
11. Launch subagent? Arguments? Plugin-defined?

### Packaging
12. Canonical layout?
13. Manifest format?
14. Bundle templates for scaffolding?
15. Install methods — marketplace, local, both?

### Cross-cutting
16. Observe transcript for pattern detection?
17. Write to project CLAUDE.md?
18. Versioning/updates?
19. Opinionated patterns conflicting with this design?

### Design validation
20. **Fold-in mechanism.** Planning writes `[FOLD-IN PENDING]` to BACKLOG.md; PreToolUse intercepts UX.md writes. Realistic?
21. **Batch sequencer.** Stop hook reads BACKLOG.md, returns block+reason. Realistic?
22. **Path-block parsing.** PreToolUse reads CLAUDE.md, parses path block, decides lock. Realistic?

## Response format

- One paragraph: overall verdict.
- Numbered section per question + citation.
- **"What to revise"** — architecture changes the gaps require.
- **"Risks I'd flag"** — technically possible but concerning.

Don't hedge. If something doesn't work, say so.
