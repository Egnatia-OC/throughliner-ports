# Claude Code plugin feasibility — Opus answer

## Verdict

**Mostly feasible; three structural gaps change the architecture.** (1) Subagents can't call subagents, so "drift-checker called BY planning" must be restructured. (2) No "always-loaded skill body" — skills are progressive-disclosure, so universal behavioural rules belong in a `UserPromptSubmit` hook (or CLAUDE.md, or a default-agent override), not a skill. (3) Per-file access isn't a subagent property — it's a `PreToolUse` hook job. Fold-in mechanism, batch sequencer, and CLAUDE.md-reading PreToolUse hook all work as described. Citations are to Anthropic docs unless noted.

---

## Hooks

**1. SessionStart hook.** Yes. Fires on startup, resume, clear, and compact; resume passes `source: "resume"`. Stdout is injected as context Claude can see; or return JSON `hookSpecificOutput.additionalContext` explicitly. Runs as a shell command in the project cwd with full filesystem access — reading CLAUDE.md and source-of-truth docs is trivial.

**2. PreToolUse hook.** Yes to all four.
- (a) **Block**: exit code 2 (stderr → Claude) or `{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "..."}}`.
- (b) **Read project files at decision time**: yes; stdin JSON includes `cwd`, `tool_name`, `tool_input`.
- (c) **Modify the tool call**: return `updatedInput`. Full pattern: `{ "hookSpecificOutput": { "hookEventName": "PreToolUse", "permissionDecision": "allow", "permissionDecisionReason": "...", "updatedInput": { ... }, "additionalContext": "..." } }`.
- (d) **Structured feedback Claude sees**: `permissionDecisionReason` (on deny) or stderr+exit 2.

**3. Stop hook.** Yes, with a loop-control caveat.
- (a) **Read project files**: yes.
- (b) **Return `{"decision": "block", "reason": "..."}`**: canonical pattern. Blocks stop; `reason` is required and goes to Claude as a continuation instruction.
- (c) **Inject continuation prompt**: that's exactly what `reason` does. **But** input includes `stop_hook_active: true` once Claude is in a forced continuation; convention is to allow stop at that point to avoid infinite loops. So: one redirect per user-turn-cycle is safe; chaining many batches off a single prompt is fragile. See risks below.

**4. Hook execution context.** Shell commands (any shebanged language), HTTP endpoints, or sub-LLM prompts. Full filesystem and network, full user permissions, no sandbox. 60s default timeout, configurable. Plugin-bundled hooks reference plugin files via `${CLAUDE_PLUGIN_ROOT}`.

---

## Subagents

**5. Subagent configuration.** Markdown + YAML frontmatter:

```yaml
---
name: subagent-name
description: When this agent should be invoked
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---
You are a [role description and expertise areas]...
```

Body is the system prompt; `tools` is the whitelist; `model` is optional (`sonnet|opus|haiku`). Files in `agents/` at plugin root, or `.claude/agents/` for project-level.

**6. Can a subagent invoke another subagent? No.** Biggest gap in your design. Per docs: subagents can't spawn subagents; for nested delegation use Skills or chain from the main conversation. Your `drift-checker` called BY `planning` won't work. Options: (a) inline drift logic into the planning subagent, (b) invoke from the main thread before/after planning, (c) implement as a `PostToolUse` hook on Edits to BACKLOG.md.

**7. Subagent restricted to certain files? Not directly.** Subagent config restricts tools, not paths. `tools: Read, Edit` lets the subagent touch anything the parent could. Per-file access is a `PreToolUse` hook job — the hook reads the subagent's declared file list (passed via prompt or context file) and blocks edits outside it. Design works; enforcement is a hook, not the subagent.

**8. Subagent context isolation? Yes.** Each subagent runs in a fresh conversation; intermediate calls/results stay inside; only the final message returns to the parent. The only parent→subagent channel is the prompt string via the Agent (Task) tool. (Exception: experimental "forked subagents" inherit parent context — not what you want.)

---

## Skills

**9. Always-loaded vs on-demand.** Skills are progressive-disclosure. Frontmatter (name + description) is always in the system prompt; SKILL.md body loads only when Claude judges it relevant. Body is *never* always-loaded. No `always-load: true`. Closest options for always-on behavioural rules:
- **UserPromptSubmit hook with `additionalContext`** — fires every prompt, injects whatever you want. The right tool for design point 5.
- **CLAUDE.md at project level** — always in context, but lives outside the plugin.
- **Plugin `settings.json` with `agent: <name>`** — replaces default Claude Code behaviour with your agent. Most powerful, most invasive.

**10. Can a skill body influence Claude across phases? No.** Once Claude moves on the body leaves context. Skills are "Claude invokes me, reads body, does task". For cross-phase rules use answer 9's mechanisms.

**Critical**: Plugin skills can't use hooks. For security, plugin-provided skills can't define hooks, MCP servers, or permission modes. Hooks must be plugin-level (`hooks/hooks.json`). Doesn't break your design — but you can't scope hooks per skill.

---

## Slash commands

**11. Slash command launching a subagent, taking arguments, defined in a plugin? Yes to all three.** As of Claude Code v2.1.101 (April 2026), custom slash commands have merged into skills. A skill with `disable-model-invocation: true` and `user-invocable: true` becomes user-only. Frontmatter supports `agent: <subagent-name>`, `context: fork`, `argument-hint`, and `$ARGUMENTS` / `$1` / `$2` in the body:

```yaml
---
name: deploy
description: Deploy the application to production
disable-model-invocation: true
user-invocable: true
argument-hint: [environment]
allowed-tools: Bash, Read, Write
model: opus
context: fork
agent: general-purpose
---
```

In plugins, commands are namespaced — `/my-plugin:new-project`.

---

## Plugin packaging

**12. Canonical file layout.**

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # required manifest
├── commands/                # legacy; prefer skills/
├── agents/                  # subagent definitions
├── skills/                  # skills (and skill-as-command)
│   └── my-skill/
│       └── SKILL.md
├── hooks/
│   └── hooks.json           # hook config; scripts can live here too
├── scripts/                 # hook scripts, utilities
├── settings.json            # default settings (agent, subagentStatusLine)
├── .mcp.json                # MCP servers (optional)
└── README.md
```

**13. Manifest format.** `plugin.json` declares name (required), version, description, author, license, keywords. Can inline `hooks`, `mcpServers`, `lspServers`, `settings`, `monitors` — most plugins use separate directories instead.

**14. Bundled templates scaffolded by a slash command into the user's project.** Yes; Wiki Builder is the precedent. Pattern: templates under `skills/<name>/templates/`, a bash script under `skills/<name>/scripts/` copying to cwd, SKILL.md instructs Claude to run it (or a slash command does). Use `${CLAUDE_PLUGIN_ROOT}` for source paths. Caveat: installed plugins can't reference files outside their directory — `../shared-utils` won't work post-install, those files aren't copied to the cache.

**15. Installation.** Marketplace and local both supported. Marketplace: `/plugin marketplace add <owner/repo>` then `/plugin install <name>@<marketplace>`. A marketplace is just a git repo with `.claude-plugin/marketplace.json`. Local dev: `claude --plugin-dir ./my-plugin`. Installed plugins are copied to `~/.claude/plugins/cache`.

---

## Cross-cutting

**16. Plugin observing the transcript to detect patterns (e.g. test notes pasted)?** Partially. Hooks see event-specific data, not the full transcript. But:
- `UserPromptSubmit` receives the user's prompt text — pattern-match there and inject a route via `additionalContext` or block with a redirect.
- Most hooks receive `transcript_path` to a JSONL of the conversation; a hook can read it for cross-turn matching.

The "detect test notes pasted, auto-route" idea works via UserPromptSubmit.

**17. Plugin writing to CLAUDE.md in the user's project?** Yes — it's just a file. Edit tool or a hook script writes it. Nothing structural blocks this.

**18. Plugin versioning/updates.** Marketplace plugins pin to commits/tags. Updates are explicit (`/plugin update`). Each version is its own cache directory; old versions kept ~7 days. Mid-session updates keep using the previous version until `/reload-plugins`. `${CLAUDE_PLUGIN_DATA}` is a persistent dir across updates — use it for carry-forward state.

**19. Architectural opinions that conflict with this design.** Three:
- **Skills are meant to be discoverable and on-demand**, not always-on rule books. Your "universal behavioural rules" fights this. Use a hook.
- **Hooks are deterministic; subagents are probabilistic.** Anything enforced (read-only files, batch sequencing, drift checks) belongs in hooks. Subagents will sometimes ignore instructions; hooks won't.
- **Plugins are sandboxed copies** — state, file refs, runtime deps must live under `${CLAUDE_PLUGIN_ROOT}` or `${CLAUDE_PLUGIN_DATA}`. No `../sibling-folder`.

---

## Validation of specific designs

**20. The fold-in mechanism — realistic?** Yes, clean fit. The planning subagent writes `[FOLD-IN PENDING]` to BACKLOG.md (allowed; BACKLOG.md isn't locked). The PreToolUse hook intercepts Edit/Write where `tool_input.file_path` is locked, returns `permissionDecision: "deny"` with reason "UX.md is locked; queue this change as a FOLD-IN block in BACKLOG.md instead." Claude reads the reason and redirects on its own.

**21. The batch sequencer — realistic, with a caveat.** Mechanically yes: Stop hook reads BACKLOG.md, finds top unticked batch, returns `{"decision": "block", "reason": "<batch instructions>"}`. **Caveat**: `stop_hook_active` loop-prevention means this reliably gives **one redirect per user turn**, not auto-chaining of N batches from a single prompt. After batch A redirects to batch B, the hook should allow stop or risk a loop. That's probably what you want — explicit user gating between batches — but it's not infinite chaining. For multi-batch chains per prompt, add a `UserPromptSubmit` hook that detects "continue" and injects the next batch as additionalContext.

**22. PreToolUse hook reading CLAUDE.md path block — realistic?** Yes. Shell script reads `$cwd/CLAUDE.md`, parses the path block, checks `tool_input.file_path` against the locked list, returns deny+reason if locked. Fast (one file read, no API call), deterministic, decision-time path resolution so CLAUDE.md changes take effect immediately. Watch: parse robustly. Keep the locked list in a fenced YAML/JSON code block, not free-form markdown bullets, so parsing is trivial.

---

## What to revise

1. **Drop "drift-checker called BY planning subagent."** Subagents can't spawn subagents. Options: (a) inline drift logic into the planning prompt, (b) call drift-checker from the main thread post-planning, (c) `PostToolUse` hook on Edits to planning-relevant files.

2. **Reframe "always-loaded behavioural skill" as a `UserPromptSubmit` hook.** Fires every prompt, injects `additionalContext` Claude sees before responding. Plugin skills can't have hooks, but the plugin can (`hooks/hooks.json`).

3. **Move "batch-executor only sees the batch's declared file list" from subagent config to a `PreToolUse` hook.** Pass the allowed list to the subagent via prompt; the hook enforces on every Edit/Write.

4. **Decide: batch sequencer auto-chains, or single-steps.** Pure Stop-hook redirect = one batch per prompt. For N-batch chains, add a `UserPromptSubmit` hook recognising "continue"/"next" and injecting the next batch.

5. **Structure CLAUDE.md's locked-files block as YAML/JSON in a fenced code block**, not free-form markdown. Trivial parser, no brittle prose dependency.

6. **Keep hooks deterministic; keep subagents probabilistic.** Guaranteed behaviour (locks, sequencing, drift detection) → hook. Judgement (planning, drift-checking) → subagent. Don't put enforcement in subagent prompts.

---

## Risks I'd flag

1. **Hook fragility around shell environments.** Shell-profile startup output (welcome messages, nvm updates) mixes with hook JSON and breaks parsing. Scripts need explicit shebang, no profile contamination, errors to stderr. For non-coder users this is a real failure mode. Test on a clean shell.

2. **Stop-hook infinite loops are easy to trigger, hard to debug.** If the batch sequencer doesn't respect `stop_hook_active`, sessions get stuck. Test the loop-exit path before shipping.

3. **PreToolUse hook reading CLAUDE.md is read-at-call-time, not cached.** Fast in practice, but a 5,000-line CLAUDE.md adds measurable cost per Edit. Probably fine at your scale; worth noting.

4. **Plugin skills can't define hooks** (security). All hook logic plugin-level. Not a blocker, but constrains file organisation.

5. **Subagent context isolation is real; the prompt is the only channel in.** Anything the batch-executor needs (file list, batch spec, current state) must be packed into the prompt from the parent. Long prompts eat the subagent's own context budget.

6. **Cache invalidation on plugin update is manual** — `/reload-plugins` required. Frequent dev updates won't reach users on long sessions until reload. Mention in install docs.

7. **The "vibe coder distributing a plugin" UX gap.** Marketplace install is easy. Local install for testing needs `--plugin-dir`, a CLI muscle your users may not have. Ship an install script in the marketplace repo doing the `/plugin marketplace add` + `/plugin install` dance, with screenshots for first run.

8. **You're building enforcement infrastructure for a workflow still being refined.** Each method change means a plugin change. Plugins are harder to iterate than markdown docs. Worth honestly asking whether the method has stabilised enough to encode structurally — your stated priority order puts the no-code method ahead of Taskflow, which suggests the method is still the thing moving most.
