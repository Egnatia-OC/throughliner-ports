# Claude Code × Git: Research Findings for the Sovereign Implementer Plugin

_Researched May 2026. Sources: code.claude.com/docs, GitHub anthropics/claude-code issues._
_Provenance: Sonnet web-search response, returned during V30, 2026-05-20. Supports the OPEN-QUESTIONS entry "Consumer-method git workflow — tagging, commits, push discipline." Will be consumed by the V32+ session that promotes that question._

---

## Q1 — Does Claude Code expose git-specific hooks a plugin can pair with?

**Confidence: HIGH**

No dedicated git hooks exist (no `PreCommit`, `PostCommit`, `PrePush` etc.). What the system *does* offer that covers git operations:

| Hook event | How it intersects with git |
|---|---|
| `PreToolUse` + matcher `Bash` | Fires before any bash command — can intercept `git commit`, `git push`, `git tag` before they run. Can block (exit 2) or allow. |
| `PostToolUse` + matcher `Bash` | Fires after bash completes — can trigger your own git ops once a command succeeds. |
| `Stop` | Fires when Claude finishes a turn. The right place for end-of-session git ops (tag + push). |
| `SubagentStop` | Fires when a subagent finishes. Relevant if your plugin ever uses subagents for build batches. |
| `FileChanged` | Fires when a watched file changes on disk. Could be used to detect doc/manifest edits, not git state directly. |

**The full hook event list as of May 2026** (from the official reference): `SessionStart`, `Setup`, `UserPromptSubmit`, `UserPromptExpansion`, `PreToolUse`, `PermissionRequest`, `PermissionDenied`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `Notification`, `SubagentStart`, `SubagentStop`, `TaskCreated`, `TaskCompleted`, `Stop`, `StopFailure`, `TeammateIdle`, `InstructionsLoaded`, `ConfigChange`, `CwdChanged`, `FileChanged`, `WorktreeCreate`, `WorktreeRemove`, `PreCompact`, `PostCompact`, `Elicitation`, `ElicitationResult`.

No "PostCommit" or "PostPush" analogue. Git awareness happens by intercepting Bash or acting at Stop.

---

## Q2 — Plugin patterns or recommended conventions for git-workflow integration?

**Confidence: MEDIUM** (documented by pattern, not by a dedicated "git integration" section)

The official plugin docs treat hooks as a first-class plugin component — plugins can ship hooks alongside skills and agents in the same `.claude-plugin/plugin.json` manifest. There is no dedicated git-workflow plugin guide.

Observed patterns from official examples and community:

- **GitButler integration** ships as a three-hook set: `PreToolUse` (Edit/Write), `PostToolUse` (Edit/Write), and `Stop` — all delegating to an external CLI (`but claude ...`). The `Stop` hook commits and updates branches. This is the closest published prior art for your use case.
- **git-guardrails skill** (`mattpocock/skills`) ships a `PreToolUse` bash hook that blocks dangerous git commands (`reset --hard`, `push --force`, etc.). Useful as a safety layer you could bundle.
- The plugin dev skill in the official repo (`anthropics/claude-code` → `plugins/plugin-dev`) documents hook development explicitly and supports all four hook types: `Stop`, `SubagentStop`, `UserPromptSubmit`, `PreToolUse`.

**Recommendation for your plugin:** The plugin system supports bundling hooks. A git-workflow skill could ship as: a skill doc (instructions), plus optional hook entries that users opt into. That matches how GitButler and git-guardrails work.

---

## Q3 — How does the `claude` CLI handle git natively, without a plugin?

**Confidence: HIGH**

Claude Code has **no auto-commit behaviour by default**. It treats git as a tool it can call via Bash, not a managed subsystem. Specifically:

- Claude reads `git log`, `git status`, `git diff` for context-gathering (part of its standard project awareness at session start).
- It will commit when you ask it to, or when it decides a commit is appropriate — but this is LLM-driven, not deterministic.
- There are no CLI flags that change commit behaviour (no `--auto-commit`, no `--no-commit` etc.).
- Claude Code adds a `Co-authored-by: Claude` trailer to commits it writes.
- Checkpointing (`code.claude.com/docs/en/checkpointing`) is a separate feature — it creates git stash-based restore points before risky operations, not session tags.

**The background git activity to know about:** Claude Code runs background `git status` polling for its own context (repo state, dirty files). This is relevant to Q5.

---

## Q4 — Prior art: existing git-workflow plugins or community tools?

**Confidence: HIGH for existence; MEDIUM for current maintenance status**

| Tool | What it does | Relevance |
|---|---|---|
| **GitButler CC hooks** (`docs.gitbutler.com`) | Pre/PostToolUse + Stop hooks that auto-commit into virtual branches per session. Shipped as copy-paste hook config + a note to tell Claude not to commit itself. | Closest to what you're describing. Read before designing. |
| **git-guardrails skill** (`aihero.dev`) | PreToolUse skill that blocks dangerous git commands. Ships via `npx skills add`. | Good safety layer to bundle or reference. |
| **claude-auto-commit** (GitHub `0xkaz`) | Agent SDK tool: analyses diffs, generates commit messages, commits + pushes. | Separate tool, not a plugin — but shows the pattern. |
| **claude-commit** (GitHub `JohannLai`) | Similar: Agent SDK + CC CLI for AI-written commit messages. | Same category. |
| **Checkpointing** (built-in) | Creates stash-based restore points before risky Bash. Not tagging, not pushing. | Probably already firing in your sessions. |

**Note:** There is no official Anthropic-published git-workflow plugin. The space is active but fragmented.

---

## Q5 — Windows-specific gotchas for plugins doing git ops

**Confidence: HIGH** (multiple open/closed GitHub issues confirming this)

**The `.git/index.lock` problem — confirmed worse on Windows**

Claude Code runs background git commands (`git status --porcelain`) for context. These acquire the index lock. On Windows, file handle semantics are stricter than Linux/macOS — if CC's background git process hasn't fully released the handle when your hook or a manual git command runs, you get:

```
fatal: Unable to create '.git/index.lock': File exists.
```

This is a known open issue (`anthropics/claude-code` #28546, escalated from #11005). Anthropic closed the original as `NOT_PLANNED`. A later issue (#47721) proposes `--no-optional-locks` for all internal CC git operations; status unknown.

**Practical mitigation for your plugin hooks:**
- Add `|| true` or retry logic to git commands in hooks so a lock failure doesn't abort the hook entirely.
- If writing a shell script hook, test for the lock file and wait/remove before operating: `while [ -f .git/index.lock ]; do sleep 0.5; done`.
- Do **not** use `git status --porcelain` in any hook that runs frequently (e.g. PostToolUse on every write) — this is the main contention source.

**Google Drive sync interaction**

An open issue (#22049) confirms that running Claude Code in a directory on Google Drive File Stream can cause an indefinite freeze during startup (the "Gitifying…" hang at 100% CPU). This occurs when the working directory is on Drive but contains a git repo in a subdirectory.

**Your specific setup note:** Your Taskflow project repo is presumably on a local drive, not inside a Google Drive-synced folder. If it is inside a synced folder, move it. Git repos and Drive sync do not mix reliably on any platform, and worse on Windows.

**Other Windows-specific notes:**
- Hook commands run in the shell Claude Code uses for Bash — on Windows this is typically `cmd.exe` or PowerShell depending on your setup. Shell scripts (`.sh`) won't run directly; use `.ps1` or `python` scripts for Windows-compatible hooks, or call `git` directly as the command.
- Path separators in hook `command` strings: use forward slashes or escaped backslashes. `$CLAUDE_FILE_PATH` env var format on Windows may differ from docs examples (which assume Unix).

---

## Design decision: Recommended habit vs hook-enforced behaviour

This is outside the research scope but worth flagging before you design:

**The one user who tested hook-driven auto-commits at scale explicitly rolled it back** (the OpenAIToolsHub article, six months of daily use). Quoted reason: "hook-driven auto-commits" were in the "looked productive but cost more than they returned" category.

GitButler's approach (the only mature published example of Stop-hook git automation) works because GitButler is the git backend — it has full session context. A standalone plugin lacks that context and has to infer "did a build batch just complete?" from heuristics.

The safer initial position is probably: **recommended habit with a skill doc**, plus a `PreToolUse` guard that blocks `git reset --hard` and `git push --force`. Add a `Stop` hook as an opt-in variant once you've tested it yourself in Taskflow sessions.

---

## Items to verify before designing

1. **Lock behaviour on your actual machine.** Run a CC session, then immediately run `git status` manually. Does it block? How long? This determines how aggressive your hook's retry logic needs to be.
2. **GitButler hooks in practice.** Fetch `docs.gitbutler.com/features/ai-integration/claude-code-hooks` and read the full implementation — the `but claude stop` command is doing non-trivial branch management you'd need to replicate.
3. **`--no-optional-locks` status.** Check whether issue #47721 has been actioned in the current CC version before writing any `git status` calls into hook scripts.
4. **Plugin hook packaging.** Confirm that hooks defined inside a plugin's `plugin.json` are actually installed into `settings.json` on `plugin install`, versus requiring the user to copy them manually. The docs imply yes; verify with the plugin dev skill or by testing.
