# Claude Code plugin feasibility check — prompt for Opus

*Paste into a fresh Opus chat with web search. Bring the response back to the No-code method Cowork session.*

---

I'm converting a structured workflow (the "no-code method") into a Claude Code plugin and need to confirm what's actually possible before committing to the architecture. **Use web search liberally** — I need current answers, not training-data guesses. Cite sources (Anthropic docs preferred). Where a feature doesn't exist or you're unsure, say so plainly.

## Context

I'm a no-code developer. The method currently governs Claude Code via markdown docs (NO-CODE-METHOD.md, DOC-STRUCTURE.md, CLAUDE.md). The plugin will distribute those rules across plugin components so adherence is **structural, not just prompt-based**.

## What the plugin needs to do

1. **Read-only file enforcement.** Block Edit/Write on certain project files (`UX.md`, other source-of-truth docs). The locked list lives in the project's CLAUDE.md "Where the docs live" path block (markdown bullets mapping doc names to paths). The hook must read CLAUDE.md at decision time.

2. **Build-batch sequencing.** The project's BACKLOG.md lists "build batches." When Claude finishes a turn, the plugin detects the next unticked batch and redirects Claude into it — so Claude only ever sees the active batch.

3. **Isolated batch execution.** Each batch runs in a fresh subagent context with only the batch's instructions and declared file list visible.

4. **Session-start orientation.** At session start: read CLAUDE.md, resolve the path block, read source-of-truth docs, detect project state (template vs filled-in), check for unfinished batches, route to the right mode (planning / building / new-project / migration).

5. **Always-loaded behavioural skill.** A small skill of universal rules (push back on assumptions, surface security/privacy concerns, plain English) firing every turn, not on-demand.

6. **Multiple specialised subagents:** planning, drift-checker (called by planning), before-build, batch-executor (isolated tool/file access), after-build, new-project, migration.

7. **Slash commands** launching specific subagents (`/new-project`, `/migrate`, etc.).

8. **Bundled templates** (5 markdown files) that a slash command scaffolds into a user project.

9. **Bundled human-readable docs** (a "crash course" markdown file) shipping with the plugin but not loaded into Claude's context.

## Questions

### Hooks
1. **SessionStart hook.** Exists? Can it read project files (e.g. CLAUDE.md) and inject context Claude will see?
2. **PreToolUse hook.** Exists? Can it: (a) block a tool call before execution, (b) read project files at decision time, (c) modify/redirect the call, (d) return a structured response Claude sees as feedback?
3. **Stop hook.** Exists? Can it: (a) read project files (BACKLOG.md) to determine next action, (b) return `{"decision": "block", "reason": "..."}` to redirect Claude, (c) inject a prompt Claude treats as continuation rather than end-of-turn?
4. **Hook execution context.** Languages/runtimes? File system access? Network access?

### Subagents
5. How configured? System prompt? Tool restrictions? Context isolation?
6. Can a subagent invoke another subagent?
7. Can a subagent be restricted to certain files (e.g. batch-executor seeing only the batch's declared files)?
8. Are subagent contexts genuinely isolated from the parent (no conversation-history carryover)?

### Skills
9. Any way to mark a skill as always-loaded vs on-demand?
10. Can a skill body include behavioural rules influencing Claude across all phases, not just when explicitly invoked?

### Slash commands
11. Can a slash command launch a specific subagent? Take arguments? Be defined inside a plugin?

### Plugin packaging
12. Canonical file layout? Where do hook scripts, subagent definitions, skill bodies, slash commands, and bundled files live?
13. Plugin manifest format and declarations?
14. Can a plugin bundle templates/docs that a slash command scaffolds into a user project?
15. Install methods — marketplace, local, both?

### Cross-cutting
16. Can a plugin observe the conversation transcript (e.g. to detect "test notes pasted" patterns and auto-route)?
17. Can a plugin write to CLAUDE.md in the user's project (e.g. update the path block on confirmed path mismatches)?
18. How is plugin versioning / updates handled?
19. Architectural patterns Claude Code is opinionated about that might conflict with this design?

### Validation of specific designs
20. **Fold-in mechanism.** When a planning batch resolves, the planning subagent appends a `[FOLD-IN PENDING]` block to BACKLOG.md instead of writing to UX.md (locked). A PreToolUse hook also intercepts any UX.md write attempt and redirects. **Realistic?**
21. **Batch sequencer.** Stop hook reads BACKLOG.md after each turn, finds the top unticked batch, returns `decision: "block"` with the batch's instructions as the reason; Claude continues with that batch. **Realistic?**
22. **PreToolUse hook reading CLAUDE.md path block.** On Edit/Write, the hook reads CLAUDE.md, parses the path block, decides whether the target is locked. **Realistic?**

## Response format

- One short paragraph: overall verdict (feasible / mostly feasible with these gaps / not feasible because X).
- A numbered section per question with answer + source citation.
- **"What to revise"** — architecture changes the gaps require.
- **"Risks I'd flag"** — technically possible but concerning.

Don't hedge unnecessarily. If something doesn't work, say so.
