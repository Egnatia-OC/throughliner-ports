# Claude Code plugin feasibility — Opus answer

## Verdict

**Mostly feasible, with three structural gaps that change the architecture.** The hook system, subagent system, plugin packaging, and slash-command-to-subagent wiring all support what you're describing. The gaps: (1) subagents cannot call other subagents, so "drift-checker called BY planning" must be restructured; (2) there is no "always-loaded skill body" — skills are progressive-disclosure by design, so your universal behavioural rules need to live in a `UserPromptSubmit` hook (or `CLAUDE.md`, or a default-agent override), not a skill; (3) per-file access control isn't a subagent property — it's a `PreToolUse` hook job. Your fold-in mechanism, batch sequencer, and CLAUDE.md-reading PreToolUse hook are all realistic as described. Citations below are to Anthropic's docs unless noted.

---

## Hooks

**1. SessionStart hook.** Yes. It fires once per session (on startup, resume, clear, and compact) and runs again on resume with `source: "resume"`. Per the Anthropic hooks reference, SessionStart hooks run again on resume so they can refresh their context. Stdout from SessionStart is special: it is added as context that Claude can see and act on. The hook can also return JSON with `hookSpecificOutput.additionalContext` to inject context explicitly. The hook is a shell command — it runs in your project's working directory and has full filesystem access, so reading CLAUDE.md and any source-of-truth docs is trivial. (Anthropic hooks reference, code.claude.com/docs/en/hooks)

**2. PreToolUse hook.** Yes to all four sub-questions.
- (a) **Block before execution**: yes, via exit code 2 (stderr fed back to Claude) or via `{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "..."}}`.
- (b) **Read project files at decision time**: yes — it's a shell script with arbitrary filesystem access, and the JSON payload on stdin includes `cwd`, `tool_name`, and `tool_input`.
- (c) **Modify the tool call**: yes — return `updatedInput` in the JSON to rewrite the tool arguments. The full payload pattern is `{ "hookSpecificOutput": { "hookEventName": "PreToolUse", "permissionDecision": "allow", "permissionDecisionReason": "...", "updatedInput": { ... }, "additionalContext": "..." } }`.
- (d) **Structured feedback Claude sees**: yes, via `permissionDecisionReason` (when denying) or stderr+exit 2 (the text goes back to Claude as feedback).

**3. Stop hook.** Yes, with one caveat about loop control.
- (a) **Read project files**: yes — same shell-script model as other hooks.
- (b) **Return `{"decision": "block", "reason": "..."}`**: yes — this is the canonical pattern. `"decision": "block"` prevents Claude from stopping; the `reason` field is required and is fed to Claude as a continuation instruction.
- (c) **Inject a prompt Claude treats as continuation**: that's exactly what `reason` does. **But** — the hook input includes `stop_hook_active: true` if Claude is already in a forced continuation, and convention is to allow stopping at that point to prevent infinite loops. When a Stop hook keeps blocking, Claude continues working, which can cause infinite loops; the `stop_hook_active` check is how you prevent this. In practice this means one redirect per user-turn-cycle is safe; chaining many batches off a single user prompt is fragile. See "Risks I'd flag" below.

**4. Hook execution context.** Shell commands (any language with a shebang — bash, Python, Node, etc.) or HTTP endpoints or prompts evaluated by a sub-LLM. Full filesystem and network access. Hooks run with your full user permissions; there is no sandbox. Default timeout 60s, configurable. Hooks bundled in a plugin can reference plugin files via the `${CLAUDE_PLUGIN_ROOT}` environment variable. (Anthropic hooks reference; plugins reference)

---

## Subagents

**5. Subagent configuration.** Markdown file with YAML frontmatter:

```yaml
---
name: subagent-name
description: When this agent should be invoked
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---
You are a [role description and expertise areas]...
```

The frontmatter declares system prompt (the markdown body), tool whitelist (`tools`), and optional model (`model: sonnet|opus|haiku`). Files live in `agents/` at plugin root or `.claude/agents/` for project-level.

**6. Can a subagent invoke another subagent? No.** This is the single biggest gap in your design. From the docs: "Subagents cannot spawn other subagents. If your workflow requires nested delegation, use Skills or chain subagents from the main conversation." Your `drift-checker` called BY `planning` won't work. The drift check has to be either (a) inlined into the planning subagent's instructions, (b) invoked from the main thread before/after planning, or (c) implemented as a `PostToolUse` hook that runs when the planning subagent writes to BACKLOG.md.

**7. Can a subagent be restricted to certain files?** Not directly — subagent config restricts tools, not file paths. A subagent's `tools: Read, Edit` lets it touch any file the parent could. Per-file access is a `PreToolUse` hook job: the hook reads the subagent's "declared file list" (passed in via the prompt or a context file) and blocks edits outside it. So design point 7 works, but the enforcement layer is a hook, not the subagent.

**8. Are subagent contexts genuinely isolated?** Yes. Each subagent runs in its own fresh conversation; intermediate tool calls and results stay inside the subagent, and only its final message returns to the parent. The only channel from parent to subagent is the prompt string passed via the Agent (Task) tool — no conversation history carryover. (One exception: experimental "forked subagents" inherit parent context; that's not what you want here.)

---

## Skills

**9. Always-loaded vs on-demand.** Skills are progressive-disclosure by design. The YAML frontmatter (name + description) is always loaded in Claude's system prompt; the SKILL.md body is loaded only when Claude thinks the skill is relevant to the current task. The body is *never* always-loaded. There's no `always-load: true` switch. The closest options for your "always-on behavioural rules":
- **UserPromptSubmit hook with `additionalContext`** — fires on every user prompt, injects whatever text you want. This is the right tool for what you described in design point 5.
- **CLAUDE.md at project level** — always in context, but lives outside the plugin.
- **Plugin `settings.json` with `agent: <name>`** — activates one of your custom agents as the main thread, replacing default Claude Code behaviour. Most powerful but most invasive.

**10. Can a skill body influence Claude across all phases?** No — once Claude moves on, the skill body isn't held in context. Skills are designed for "Claude invokes me, reads body, does task". For cross-phase behavioural rules, use one of the three mechanisms in answer 9.

**Also critical**: Plugin skills can't use hooks. For security reasons, plugin-provided skills cannot define hooks, MCP servers, or permission modes. Hooks must be defined at plugin level (`hooks/hooks.json`), not inside individual skills. This doesn't break your design — but if you'd been planning to scope hooks to specific skills, you can't.

---

## Slash commands

**11. Can a slash command launch a specific subagent? Take arguments? Be defined in a plugin?** Yes to all three. As of Claude Code v2.1.101 (April 2026), custom slash commands have been merged into skills. A skill with `disable-model-invocation: true` (so Claude can't auto-invoke it) and `user-invocable: true` becomes a user-only slash command. The frontmatter supports `agent: <subagent-name>` to delegate to a specific subagent, `context: fork` to run in a fresh subagent context, `argument-hint`, and `$ARGUMENTS` / `$1` / `$2` placeholders in the body:

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

In plugins, commands are namespaced — `/my-plugin:new-project` — to avoid collisions.

---

## Plugin packaging

**12. Canonical file layout.** From the official docs:

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

**13. Manifest format.** `plugin.json` declares name (required), version, description, author, license, keywords. It can also inline `hooks`, `mcpServers`, `lspServers`, `settings` (for default agent), and `monitors` if you don't want separate config files. Most plugins keep these in their own directories rather than inlining.

**14. Bundled templates that a slash command scaffolds into a user project.** Yes, and there's a clean precedent: the Wiki Builder plugin does exactly this. The pattern: bundle templates under `skills/<name>/templates/`, write a bash script under `skills/<name>/scripts/` that copies templates into the user's cwd, and have the SKILL.md instruct Claude to run that script (or run it via a slash command). Use `${CLAUDE_PLUGIN_ROOT}` for the source path. Important caveat: installed plugins cannot reference files outside their directory. Paths that traverse outside the plugin root (such as `../shared-utils`) will not work after installation because those external files are not copied to the cache.

**15. Installation.** Both marketplace and local. Marketplace: user runs `/plugin marketplace add <owner/repo>` then `/plugin install <name>@<marketplace>`. The marketplace is just a git repo with a `.claude-plugin/marketplace.json` listing plugins. Local development: `claude --plugin-dir ./my-plugin`. Plugins are copied to `~/.claude/plugins/cache` on install.

---

## Cross-cutting

**16. Can a plugin observe the transcript to detect patterns (e.g. test notes pasted)?** Partially. Hooks see event-specific data, not the full ongoing transcript. But:
- `UserPromptSubmit` hook receives the user's prompt text — pattern-match there for "test notes pasted" and inject a route via `additionalContext` or block with a redirect.
- Most hooks receive `transcript_path` pointing to a JSONL file of the conversation, which a hook can read if it really needs cross-turn pattern matching.

So the "detect test notes pasted, auto-route" idea is feasible via UserPromptSubmit.

**17. Can a plugin write to CLAUDE.md in the user's project?** Yes — it's just a file. Either Claude uses the Edit tool (no special privilege needed), or a hook script writes it directly. Nothing structural blocks this.

**18. Plugin versioning/updates.** Marketplace plugins are pinned to commits/tags. Updates are explicit (`/plugin update`). Each installed version lives as its own directory in the cache; old versions are kept for ~7 days. When a plugin updates mid-session, hooks, MCP servers, and LSP servers keep using the previous version's path until `/reload-plugins` is run. `${CLAUDE_PLUGIN_DATA}` is a persistent dir that survives updates — use it for any state you want to carry forward.

**19. Architectural opinions of Claude Code that conflict with this design.** Three to flag:
- **The system expects skills to be discoverable and on-demand**, not always-on rule books. Your "universal behavioural rules" is fighting this. Use a hook.
- **Hooks are deterministic; subagents are probabilistic.** Anything you want enforced (read-only files, batch sequencing, drift checks) belongs in hooks, not in subagent instructions. Subagents will sometimes ignore their instructions; hooks won't.
- **Plugins are sandboxed copies**, so any state, file references, or runtime dependencies must live under `${CLAUDE_PLUGIN_ROOT}` or `${CLAUDE_PLUGIN_DATA}`. No `../sibling-folder` references.

---

## Validation of specific designs

**20. The fold-in mechanism — realistic?** Yes, clean fit. The planning subagent writes `[FOLD-IN PENDING]` to BACKLOG.md (allowed because BACKLOG.md isn't locked). The PreToolUse hook intercepts any Edit/Write whose `tool_input.file_path` is in the locked list (UX.md and friends) and returns `permissionDecision: "deny"` with a `permissionDecisionReason` like "UX.md is locked; queue this change as a FOLD-IN block in BACKLOG.md instead." That reason text goes back to Claude as feedback, and Claude redirects on its own. Both pieces work.

**21. The batch sequencer — realistic, with a caveat.** Mechanically yes. Stop hook reads BACKLOG.md, finds top unticked build batch, returns `{"decision": "block", "reason": "<batch instructions>"}`. Claude continues with that as its next task. **Caveat**: because of `stop_hook_active` loop-prevention, this reliably gives you **one redirect per user turn**, not auto-chaining of N batches from a single prompt. If the user types "go", Claude finishes batch A, the hook redirects to batch B, Claude finishes batch B, the hook should allow stop (otherwise loop risk). That's actually probably what you want — explicit user gating between batches — but be aware it's not infinite auto-chaining. If you do want multi-batch chains per prompt, consider also using a `UserPromptSubmit` hook that detects "continue" prompts and injects the next batch as additionalContext instead.

**22. PreToolUse hook reading CLAUDE.md path block — realistic?** Yes, completely. The hook is a shell script that reads `$cwd/CLAUDE.md`, parses the path block (grep/awk/jq depending on whether you keep it as a bullet list or a fenced code block), checks `tool_input.file_path` against the locked list, returns deny+reason if locked. Fast (single file read, no API call), deterministic, and the path resolution happens at decision time so changes to CLAUDE.md take effect immediately. The only thing to watch: parsing CLAUDE.md robustly. I'd recommend keeping the locked list in a structured fenced code block (YAML or JSON inside ```) rather than a free-form markdown bullet list, so the parser is trivial.

---

## What to revise

1. **Drop "drift-checker called BY planning subagent."** Subagents can't spawn subagents. Options: (a) inline the drift logic into the planning subagent's prompt, (b) call drift-checker from the main thread after planning returns, (c) implement drift detection as a `PostToolUse` hook that fires on Edits to planning-relevant files.

2. **Reframe the "always-loaded behavioural skill" as a `UserPromptSubmit` hook.** This hook fires on every prompt and can inject `additionalContext` text Claude sees before responding. That's what you actually want. Plugin skills can't have hooks, but the plugin itself can (in `hooks/hooks.json`).

3. **Move "batch-executor only sees the batch's declared file list" from subagent config to a `PreToolUse` hook.** Pass the allowed file list into the subagent via its prompt; the hook enforces the boundary on every Edit/Write attempt.

4. **Decide whether the batch sequencer auto-chains or single-steps.** Pure Stop-hook redirect reliably gives one batch per user prompt. If you want N-batch chains, add a `UserPromptSubmit` hook that recognises "continue" / "next" prompts and injects the next batch as additionalContext.

5. **Structure CLAUDE.md's locked-files block as parseable YAML/JSON inside a fenced code block**, not free-form markdown. Makes the PreToolUse parser trivial and removes a brittle dependency on prose layout.

6. **Keep hooks deterministic; keep subagents probabilistic.** Anything you want guaranteed (locks, sequencing, drift detection) goes in a hook. Anything that needs judgement (planning, drift-checking) goes in a subagent. Don't put enforcement in subagent prompts.

---

## Risks I'd flag

1. **Hook fragility around shell environments.** If your shell profile prints anything at startup (welcome messages, nvm updates, etc.), that text mixes with your hook's JSON output and Claude Code can't parse it. Your hook scripts need to be defensive — explicit shebang, no shell-profile contamination, all errors to stderr not stdout. For a plugin distributed to non-coder users, this is a real failure mode. Test on a clean shell.

2. **Stop-hook infinite loops are easy to trigger and hard to debug.** If your batch sequencer doesn't respect `stop_hook_active`, you'll get stuck sessions. Test the loop-exit path before shipping.

3. **The PreToolUse hook reading CLAUDE.md is read-at-call-time, not cached.** Fast in practice, but if a user has a 5,000-line CLAUDE.md it's a measurable cost on every Edit. Probably fine for your scale, but worth noting.

4. **Plugin skills can't define hooks** (security). All hook logic must be plugin-level. This isn't a blocker but constrains how you organise files.

5. **Subagent context isolation is real but the prompt is the only channel in.** Anything the batch-executor needs to know (file list, batch spec, current state) has to be packed into the prompt string from the parent. Long prompts eat the subagent's own context budget.

6. **Cache invalidation on plugin update is manual** — `/reload-plugins` is required. If you push frequent updates during development, users on long sessions won't see them until they reload. Mention this in your install docs.

7. **The "vibe coder distributing a plugin" UX gap.** Marketplace install is easy. Local install for testing requires the `--plugin-dir` flag, which is a CLI muscle your users may not have. Consider shipping an install script in the marketplace repo that does the `/plugin marketplace add` + `/plugin install` dance, with screenshots for the first run.

8. **You're building enforcement infrastructure for a workflow that's still being refined.** Each time you change the method, you change the plugin. The plugin is harder to iterate than markdown docs. Worth being honest about whether the method has stabilised enough to encode structurally yet — particularly given your stated priority order has the no-code method ahead of Taskflow, which suggests the method is the thing still moving the most.
