# Claude Code plugin feasibility — Opus answer

## Verdict

**Mostly feasible; three structural gaps.** (1) Subagents can't call subagents — drift-checker must be restructured. (2) No always-loaded skill body — universal rules belong in a `UserPromptSubmit` hook. (3) Per-file access is a `PreToolUse` hook job, not a subagent property. Fold-in, batch sequencer, and path-block parsing all work as designed. Citations: Anthropic docs unless noted.

---

## Hooks

**1. SessionStart.** Yes. Fires on startup/resume/clear/compact. Stdout injected as context Claude sees; or return JSON `additionalContext`. Full filesystem access — reading CLAUDE.md is trivial.

**2. PreToolUse.** Yes to all four.
- (a) **Block**: exit 2 or `permissionDecision: "deny"` + reason.
- (b) **Read files**: stdin JSON has `cwd`, `tool_name`, `tool_input`.
- (c) **Modify**: return `updatedInput` in JSON.
- (d) **Feedback**: `permissionDecisionReason` (deny) or stderr+exit 2.

**3. Stop.** Yes, with loop-control caveat.
- (a) **Read files**: yes.
- (b) **Block stop**: `{"decision": "block", "reason": "..."}` — reason goes to Claude as continuation.
- (c) **Loop prevention**: `stop_hook_active: true` in input after first redirect; convention: allow stop then. One redirect per user-turn is safe; chaining is fragile.

**4. Execution context.** Any shebanged language, HTTP, or sub-LLM. Full filesystem/network, no sandbox. 60s timeout (configurable). Plugin files via `${CLAUDE_PLUGIN_ROOT}`.

---

## Subagents

**5. Configuration.** Markdown + YAML frontmatter. Body = system prompt; `tools` = whitelist; `model` optional. Files in `agents/` at plugin root or `.claude/agents/` project-level.

**6. Subagent→subagent? No.** Biggest gap. Options: (a) inline drift logic into planning, (b) invoke from main thread, (c) PostToolUse hook.

**7. File-restricted? Not directly.** Config restricts tools, not paths. Per-file access is a PreToolUse hook job — hook reads the declared file list and blocks outside it.

**8. Context isolation? Yes.** Fresh conversation per subagent; only final message returns. Parent→subagent channel is the prompt string only. (Experimental "forked" subagents inherit context — not what you want.)

---

## Skills

**9. Always-loaded? No.** Skills are progressive-disclosure — frontmatter always in system prompt, body loads only when judged relevant. For always-on rules: **UserPromptSubmit hook** (fires every prompt, injects `additionalContext`), CLAUDE.md (always in context, outside plugin), or plugin `settings.json` with `agent: <name>` (most invasive).

**10. Cross-phase influence? No.** Body leaves context after use. Use hook mechanisms from Q9.

**Note:** Plugin skills can't define hooks, MCP servers, or permission modes (security). Hooks must be plugin-level.

---

## Slash commands

**11. Yes to all three.** Skills with `disable-model-invocation: true` + `user-invocable: true` become user-only slash commands. Frontmatter supports `agent`, `context: fork`, `argument-hint`, `$ARGUMENTS`. Namespaced in plugins: `/my-plugin:command`.

---

## Plugin packaging

**12. Layout.** `.claude-plugin/plugin.json` (required), `agents/`, `skills/`, `hooks/` (+ `hooks.json`), `scripts/`, `settings.json`, `.mcp.json`. `commands/` is legacy — prefer skills.

**13. Manifest.** `plugin.json`: name (required), version, description, author, license, keywords. Can inline hooks/MCP/settings — most use separate dirs.

**14. Bundled templates? Yes.** Pattern: templates under `skills/<name>/templates/`, script copies to cwd. Use `${CLAUDE_PLUGIN_ROOT}`. Caveat: installed plugins can't reference files outside their directory.

**15. Install.** Marketplace (`/plugin marketplace add` + `/plugin install`) and local (`--plugin-dir`). Marketplace = git repo with `marketplace.json`. Installed plugins cached to `~/.claude/plugins/cache`.

---

## Cross-cutting

**16. Transcript observation?** Partially. `UserPromptSubmit` receives prompt text (pattern-match + inject route). Most hooks receive `transcript_path` (JSONL) for cross-turn matching. "Detect test notes, auto-route" works via UserPromptSubmit.

**17. Write to project CLAUDE.md?** Yes — just a file. Nothing blocks it.

**18. Versioning.** Marketplace pins to commits/tags. Updates explicit (`/plugin update`), cached per-version (~7 days). Mid-session: stays on previous version until `/reload-plugins`. `${CLAUDE_PLUGIN_DATA}` persists across updates.

**19. Conflicting opinions.** (a) Skills are on-demand, not always-on — use a hook for universal rules. (b) Hooks are deterministic, subagents probabilistic — enforcement belongs in hooks. (c) Plugins are sandboxed copies — all refs must use `${CLAUDE_PLUGIN_ROOT}` or `${CLAUDE_PLUGIN_DATA}`.

---

## Validation of specific designs

**20. Fold-in mechanism?** Yes, clean fit. Planning writes to BACKLOG.md (unlocked). PreToolUse denies locked-file writes with redirect reason. Claude self-corrects.

**21. Batch sequencer?** Mechanically yes. **Caveat**: `stop_hook_active` gives one redirect per user turn, not N-batch chaining. For multi-batch: add UserPromptSubmit hook detecting "continue."

**22. Path-block parsing?** Yes. Fast (one file read), deterministic, decision-time resolution. Keep locked list in fenced YAML/JSON, not free-form bullets, for robust parsing.

---

## What to revise

1. **Drop drift-checker-called-by-planning.** Inline drift logic or invoke from main thread.
2. **Universal rules → UserPromptSubmit hook**, not skill.
3. **Batch file-list enforcement → PreToolUse hook**, not subagent config.
4. **Batch sequencer: single-step** (Stop hook). For N-batch chains, add UserPromptSubmit hook.
5. **CLAUDE.md path block → fenced YAML/JSON**, not free-form markdown.
6. **Deterministic → hooks. Probabilistic → subagents.** Don't put enforcement in prompts.

---

## Risks I'd flag

1. **Shell-profile contamination.** Startup output (nvm, welcome messages) breaks hook JSON parsing. Explicit shebang, no profile loading, errors to stderr.
2. **Stop-hook loops.** If sequencer ignores `stop_hook_active`, sessions hang. Test loop-exit path before shipping.
3. **CLAUDE.md read-per-call.** Fast at normal scale; a 5k-line CLAUDE.md adds cost per Edit.
4. **Skills can't define hooks.** All hook logic is plugin-level.
5. **Subagent prompt is the only channel in.** Everything the batch-executor needs must fit in the prompt — long prompts eat subagent context.
6. **Manual cache invalidation.** `/reload-plugins` required after updates.
7. **Non-coder install UX.** `--plugin-dir` is CLI muscle. Ship marketplace install path with screenshots.
8. **Encoding a moving target.** Each method change = plugin change. Plugins iterate slower than docs.
