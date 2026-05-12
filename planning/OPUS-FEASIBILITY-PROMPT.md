# Claude Code plugin feasibility check — prompt for Opus

*Paste the content below into a fresh Opus chat (web search must be available). Bring the full response back to the No code method Cowork session.*

---

I'm planning to convert a structured workflow document (the "no-code method") into a Claude Code plugin. Before I commit to the architecture, I need you to confirm what's actually possible in Claude Code's plugin system. **Please use web search liberally** — I need accurate, current answers, not best-guesses from training data. Cite your sources (Anthropic docs preferred). Where a feature doesn't exist or you're uncertain, say so plainly.

## Context

I'm a no-code developer. The no-code method currently governs Claude Code's behaviour in user projects via a set of markdown docs (NO-CODE-METHOD.md, DOC-STRUCTURE.md, CLAUDE.md). The plugin will distribute those rules across plugin components so adherence is **structural, not just prompt-based**.

## What the plugin needs to do

1. **Read-only file enforcement.** Block Edit/Write on certain project files (`UX.md`, additional source-of-truth docs). The locked list lives in the project's `CLAUDE.md` "Where the docs live" path block (a markdown bullet list mapping doc names to paths). The hook must read CLAUDE.md at decision time to know what's locked.

2. **Build-batch sequencing.** The project's `BACKLOG.md` lists "build batches." When Claude finishes a turn, the plugin should detect the next unticked batch and redirect Claude into that batch — so Claude only ever sees the active batch, not the full backlog.

3. **Isolated batch execution.** Each batch runs in a fresh subagent context with only the batch's instructions and declared file list visible.

4. **Session-start orientation.** At session start, the plugin reads CLAUDE.md, resolves the path block, reads source-of-truth docs, detects project state (template vs filled-in), checks for unfinished batches, and routes to the right mode (planning / building / new-project / migration).

5. **Always-loaded behavioural skill.** A small skill containing universal behavioural rules (push back on user assumptions, surface security/privacy concerns, plain English) firing across every turn, not on-demand.

6. **Multiple specialised subagents:** planning, drift-checker (called BY planning), before-build, batch-executor (with isolated tool/file access), after-build, new-project, migration.

7. **Slash commands** that launch specific subagents (`/new-project`, `/migrate`, etc.).

8. **Bundled templates** (5 markdown files) that a slash command can scaffold into a user project.

9. **Bundled human-readable docs** (a "crash course" markdown file) that ships with the plugin but isn't loaded into Claude's context.

## Questions

### Hooks
1. **SessionStart hook.** Does it exist? Can it read project files (e.g. CLAUDE.md) and inject context into the session that Claude will see?
2. **PreToolUse hook.** Does it exist? Can it: (a) block a tool call before it executes, (b) read project files at decision time, (c) modify or redirect the tool call, (d) return a structured response Claude sees as feedback?
3. **Stop hook.** Does it exist? Can it: (a) read project files (BACKLOG.md) to determine next action, (b) return `{"decision": "block", "reason": "..."}` to redirect Claude, (c) inject a prompt that Claude treats as a continuation rather than an end-of-turn?
4. **Hook execution context.** What languages/runtimes? File system access? Network access?

### Subagents
5. How are subagents configured? System prompt? Tool restrictions? Context isolation?
6. Can a subagent invoke another subagent?
7. Can a subagent be configured to only access certain files (e.g., batch-executor only sees the batch's declared file list)?
8. Are subagent contexts genuinely isolated from the parent (no conversation-history carryover)?

### Skills
9. Is there a way to mark a skill as always-loaded vs on-demand?
10. Can a skill body include behavioural rules that influence Claude's responses across all phases (not just when the skill is explicitly invoked)?

### Slash commands
11. Can a slash command launch a specific subagent? Take arguments? Be defined inside a plugin?

### Plugin packaging
12. Canonical file layout? Where do hook scripts, subagent definitions, skill bodies, slash command definitions, and bundled files live?
13. Plugin manifest format? What does it declare?
14. Can a plugin bundle templates and docs that a slash command can scaffold into a user project?
15. How does a user install a plugin? Marketplace? Local install? Both?

### Cross-cutting
16. Can a plugin observe the conversation transcript (e.g. to detect "test notes pasted" patterns and auto-route)?
17. Can a plugin write to CLAUDE.md in the user's project (e.g. to update the path block on confirmed path mismatches)?
18. How is plugin versioning / updates handled?
19. Are there architectural patterns Claude Code is opinionated about that might conflict with this design?

### Validation of specific designs
20. **The fold-in mechanism.** When a planning batch resolves, the planning subagent appends a `[FOLD-IN PENDING]` block to BACKLOG.md instead of writing to UX.md (which is locked). A PreToolUse hook also intercepts any UX.md write attempt and redirects. **Realistic?**
21. **The batch sequencer.** Stop hook reads BACKLOG.md after each turn, finds the top unticked build batch, returns `decision: "block"` with the batch's instructions as the reason; Claude continues with that batch as the next task. **Realistic?**
22. **The PreToolUse hook reading CLAUDE.md path block.** When Claude tries to Edit/Write a file, the PreToolUse hook reads the project's CLAUDE.md, parses the path block, and decides whether the target file is locked. **Realistic?**

## Response format

Please structure your response as:

- One short paragraph stating the overall verdict: feasible / mostly feasible with these gaps / not feasible because X.
- A numbered section per question above with the answer plus source citation.
- A **"What to revise"** section listing any architecture changes the gaps require.
- A **"Risks I'd flag"** section for things that are technically possible but you have concerns about.

Do not hedge unnecessarily. If something doesn't work, say so plainly.
