# ANALYSIS — Porting Throughliner to OpenCode 1.18.21

Analysis phase deliverable. Scope: map OpenCode's extension model against what the
Throughliner plugin needs, with verbatim schemas from the 1.18.21 source, so the shim
author can implement without re-deriving any field.

- Upstream Throughliner: pinned at commit `743aa63` (v1.21.1)
- Reference port (verified live): the omp port, published on the fork's `main` branch
- OpenCode source: tag v1.18.21 (ground truth for all quotes below)

---

## 1. Harness overview + installed version

- **Binary**: `/snap/bin/opencode` (snap, classic confinement). The wrapper
  (`/snap/opencode/current/bin/opencode.wrapper`) only unsets `SNAP*` vars and execs
  `$SNAP/bin/opencode`, a ~169 MB Bun single-file binary. The JS is not extractable
  from the bundle, so all schemas in this document are quoted from a source clone at
  the exact installed tag.
- **Version**: **1.18.21** (from `/snap/opencode/current/meta/snap.yaml`: name `opencode`,
  version `1.18.21`).
- **Source clone**: `/tmp/opencode-1.18.21` = tag `v1.18.21` of `anomalyco/opencode`
  (note: the repo moved from `sst/opencode`; raw URLs under the old org still resolve
  via redirect).
- **Non-interactive mode**: `opencode run` — "sends a single prompt, streams events to
  stdout, and exits when the session goes idle" (verbatim header comment,
  `packages/opencode/src/cli/cmd/run.ts`).
- **Runtime**: Bun. Plugins are loaded as TS/JS modules in-process (no subprocess for
  plugin code). Node 20+ API surface available.

---

## 2. Extension model (what exists, where, in what format)

### 2.1 Config files

**File discovery** (`packages/opencode/src/config/paths.ts`, verbatim logic):
- Project config JSON: walk up from cwd for `opencode.jsonc` / `opencode.json`
  (stop at worktree root; reversed so the closest project file wins).
- Config **directories** (each contributes md files + auto-loaded plugins/skills/agents):
  1. `~/.config/opencode` (`Global.Path.config`)
  2. `.opencode/` directories walked up from cwd to worktree root
  3. `~/.opencode/` (walk-up from home)
  4. `$OPENCODE_CONFIG_DIR` if set
- **`~/.opencode.json` (dot-file in home root) is NOT loaded by 1.18.21** — no code path
  references it (grep over the whole source tree: zero matches). The legacy
  `~/.opencode.json` present on this machine is dead config; only
  `~/.config/opencode/opencode.jsonc` takes effect globally.

**Config schema** (`packages/core/src/v1/config/config.ts`, relevant fields verbatim):

```ts
export const Info = Schema.Struct({
  $schema: Schema.optional(Schema.String),
  shell: Schema.optional(Schema.String),
  logLevel: Schema.optional(LogLevelRef),               // "DEBUG"|"INFO"|"WARN"|"ERROR"
  server: Schema.optional(ConfigServerV1.Server),
  command: Schema.optional(Schema.Record(Schema.String, ConfigCommandV1.Info)),
  skills: Schema.optional(ConfigSkillsV1.Info),         // { paths?, urls? }
  references: Schema.optional(ConfigReference.Info),
  watcher: Schema.optional(...),
  snapshot: Schema.optional(Schema.Boolean),
  plugin: Schema.optional(Schema.mutable(Schema.Array(ConfigPluginV1.Spec))),
  share: Schema.optional(Schema.Literals(["manual", "auto", "disabled"])),
  autoupdate: Schema.optional(Schema.Union([Schema.Boolean, Schema.Literal("notify")])),
  disabled_providers: Schema.optional(Schema.mutable(Schema.Array(Schema.String))),
  enabled_providers: Schema.optional(Schema.mutable(Schema.Array(Schema.String))),
  model: Schema.optional(Schema.String),                // "provider/model" — STRING
  small_model: Schema.optional(Schema.String),
  default_agent: Schema.optional(Schema.String),
  subagent_depth: Schema.optional(NonNegativeInt),
  username: Schema.optional(Schema.String),
  mode: Schema.optional(...),                           // @deprecated → agent
  agent: Schema.optional(Schema.StructWithRest( ... , [Schema.Record(Schema.String, ConfigAgentV1.Info)])),
  provider: Schema.optional(Schema.Record(Schema.String, ConfigProviderV1.Info)),
  mcp: Schema.optional(...),
  formatter: Schema.optional(ConfigFormatterV1.Info),
  lsp: Schema.optional(ConfigLspV1.Info),
  instructions: Schema.optional(Schema.mutable(Schema.Array(Schema.String))),
  layout: Schema.optional(...),                         // @deprecated
  permission: Schema.optional(ConfigPermissionV1.Info),
  tools: Schema.optional(Schema.Record(Schema.String, Schema.Boolean)),
  attachment: Schema.optional(ConfigAttachmentV1.Info),
  enterprise: Schema.optional(...),
  tool_output: Schema.optional(...),
  compaction: Schema.optional(...),
  experimental: Schema.optional(...),
}).annotate({ identifier: "Config" })
```

Note: **`model` is a string** ("provider/model", e.g. `"mercury/my-model-id"`).

**Provider schema** (`packages/core/src/v1/config/provider.ts`):

```ts
Info = {
  api?, name?, env?: string[], id?, npm?, whitelist?, blacklist?,
  options: { apiKey?, baseURL?, enterpriseUrl?, setCacheKey?, timeout?, headerTimeout?, chunkTimeout?, ...rest },
  models?: Record<modelID, Model>
}
Model = {
  id?, name?, family?, release_date?, attachment?, reasoning?, temperature?, tool_call?,
  interleaved?, cost?, limit?: { context, input?, output }, modalities?, experimental?,
  status?, provider?, options?, headers?, variants?
}
```

API key resolution (`packages/opencode/src/provider/provider.ts`, `resolveSDK`):
`options["apiKey"]` comes from the provider config's `options.apiKey`, falling back to
`provider.key` (from auth / `env` vars). For a local llama.cpp endpoint no key is
required; if the provider loader complains, set `options.apiKey` to any placeholder
string (see §7).

### 2.2 Plugins

**Registration** — two mechanisms, both verified in 1.18.21 source:

1. **Auto-load from config directories**: `packages/opencode/src/config/plugin.ts`:
   ```ts
   export async function load(dir: string) {
     const plugins: ConfigPluginV1.Spec[] = []
     for (const item of await Glob.scan("{plugin,plugins}/*.{ts,js}", {
       cwd: dir, absolute: true, dot: true, symlink: true,
     })) {
       plugins.push(pathToFileURL(item).href)
     }
     return plugins
   }
   ```
   i.e. every file matching `plugin/*.{ts,js}` or `plugins/*.{ts,js}` **directly inside**
   each config dir (`.opencode/`, `~/.config/opencode/`, `~/.opencode/`,
   `$OPENCODE_CONFIG_DIR`) is loaded. Single level — **no subdirectories** are scanned.
2. **Config field**: `"plugin": [spec, [spec, options], ...]` where
   ```ts
   // packages/core/src/v1/config/plugin.ts (verbatim)
   export const Options = Schema.Record(Schema.String, Schema.Unknown)
   export const Spec = Schema.Union([Schema.String, Schema.mutable(Schema.Tuple([Schema.String, Options]))])
   ```
   Path-like specs (`file://...`, `./...`, absolute) are resolved **relative to the
   config file that declared them** (`config/plugin.ts:resolvePluginSpec`):
   ```ts
   export function isPathPluginSpec(spec: string) {
     return spec.startsWith("file://") || spec.startsWith(".") || isAbsolutePath(spec)
   }
   ```
   Everything else is treated as an **npm package name**, installed via Bun to
   `~/.cache/opencode/node_modules` at startup.

**Module contract** (`packages/opencode/src/plugin/shared.ts`, `readV1Plugin`):
the module must `default export` an object with a `server` function (and optional
`id`); legacy named-export functions are also accepted. Verbatim type from
`packages/plugin/src/index.ts`:

```ts
export type PluginModule = { id?: string; server: Plugin; tui?: never }
export type Plugin = (input: PluginInput, options?: PluginOptions) => Promise<Hooks>
export type PluginOptions = Record<string, unknown>

export interface PluginInput {
  client: OpencodeClient          // SDK client; works for session.prompt / event.subscribe / permission.reply
  project: Project                // { id, worktree, vcs?, time }
  directory: string               // instance directory (project cwd)
  worktree: string                // worktree root
  experimental_workspace: { register(type: string, adapter: WorkspaceAdapter): void }
  serverUrl: URL
  $: BunShell                     // Bun.$ shell helper (undefined if not Bun)
}
```

**Entry resolution for a directory spec** (`shared.ts:resolvePathPluginTarget`):
- dir contains `package.json` → use it (`exports["./server"]` or `main`)
- else dir with `index.{ts,tsx,js,mjs,cjs}` → that index file
- else bare file spec → the file itself
- `package.json` with `engines.opencode` gets a **semver compatibility check**
  (`checkPluginCompatibility`; thrown as "Plugin X skipped: …" on mismatch).

**Load lifecycle** (`packages/opencode/src/plugin/index.ts`):
- `--pure` (or `RuntimeFlags.pure`) **skips all external plugins** (`const plugins =
  flags.pure ? [] : (cfg.plugin_origins ?? [])`) — this is the A/B baseline switch.
- After load, each hook's `config` hook is called once with the full merged config:
  `(hook as any).config?.(cfg)`.
- The `event` hook is subscribed to the global bus:
  ```ts
  const unsubscribe = yield* events.listen((event) => {
    if (event.location?.directory !== ctx.directory) return Effect.void
    return Effect.sync(() => {
      for (const hook of hooks) {
        void hook["event"]?.({ event: { id: event.id, type: event.type, properties: event.data } as any })
      }
    })
  })
  ```
  Note `void hook["event"]` — **fire-and-forget**: event hooks are notification-only,
  cannot block, and errors inside them are not propagated.
- Load failures surface as `session.error` events (observable in `opencode run
  --format json` streams): `"Failed to install plugin <pkg>@<ver>: …"`,
  `"Plugin <spec> skipped: …"`, `"Failed to load plugin <spec>: …"`.

**Trigger semantics** (`plugin/index.ts:trigger`): hooks for a given trigger run
**sequentially per plugin**; each is `Effect.promise(async () => fn(input, output))`.
A **rejected hook (throw) fails the enclosing tool-execution effect → the tool call
fails, and the error message is returned to the model as the tool result**. That throw
is THE deny/block mechanism (matches the official docs `.env` protection example:
`throw new Error("Do not read .env files")` in `tool.execute.before`). `output.args`
is mutable before execution — in `session/tools.ts:106-112` the trigger's returned
`{args}` goes straight to `item.execute(args, ctx)`.

**`opencode plugin <module>` CLI** (alias `plug`, `cli/cmd/plug.ts`): takes **only an
npm module name** (yargs positional required), installs it, reads its manifest
(`exports["./server"]` / `main`), and patches the `plugin` array in global or local
config (`-g` global, `-f` force). Not usable for local directories.

### 2.3 Skills

**Discovery** (`packages/opencode/src/skill/index.ts`, verbatim patterns):
```ts
const CLAUDE_EXTERNAL_DIR = ".claude"
const AGENTS_EXTERNAL_DIR = ".agents"
const EXTERNAL_SKILL_PATTERN = "skills/**/SKILL.md"
const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"
const SKILL_PATTERN = "**/SKILL.md"
```
Search roots, in order:
1. `~/.claude/skills/**/SKILL.md` and `~/.agents/skills/**/SKILL.md` (global;
   disabled by `disableExternalSkills` / `disableClaudeCodeSkills` flags)
2. Project tree: `.claude/skills/**/SKILL.md` + `.agents/skills/**/SKILL.md` walking up
   from cwd to worktree root
3. Every config dir (`.opencode/`, `~/.config/opencode/`, …): `{skill,skills}/**/SKILL.md`
   → **project `.opencode/skills/<name>/SKILL.md` is the canonical install spot**
4. `cfg.skills.paths[]` — dirs (relative-to-project or absolute, `~/` expanded),
   scanned with `**/SKILL.md`
5. `cfg.skills.urls[]` — remote skill indexes (cached in `~/.cache/opencode/skills`)

**Frontmatter validation** (`isSkillFrontmatter`) — deliberately permissive:
```ts
function isSkillFrontmatter(data: unknown): data is { name: string; description?: string } {
  return (
    isRecord(data) &&
    typeof data.name === "string" &&
    (data.description === undefined || typeof data.description === "string")
  )
}
```
**Extra frontmatter keys pass through harmlessly** — upstream Throughliner SKILL.md
files (with `disable-model-invocation: true`, `user-invocable: true`) load unmodified.

**Info shape**: `{ name, description?, location (path to SKILL.md), content (body) }`.
Duplicate names: **first scanned wins** + warning log. A built-in skill
`customize-opencode` is registered first; any disk skill with the same name overrides it.

**Every skill becomes a slash command** (`packages/opencode/src/command/index.ts`):
```ts
for (const item of yield* skill.all()) {
  if (commands[item.name]) continue
  const dir = item.location === "<built-in>" ? undefined : path.dirname(item.location)
  commands[item.name] = {
    name: item.name,
    description: item.description,
    source: "skill",
    get template() {
      if (!dir) return item.content
      return [
        item.content,
        "",
        `Base directory for this skill: ${dir}`,
        "Relative paths in this skill (e.g., scripts/, references/) are relative to this base directory.",
      ].join("\n")
    },
    hints: [],
  }
}
```
So the five Throughliner skills are user-invocable as `/setup /plan /next /rescan
/done` AND headless via `opencode run --command <name>`.

**Skills are also model-invocable**: a `skill` tool exists (`tool/skill.ts`). The
system prompt includes a skills block (`session/system.ts`):
```ts
[
  "Skills provide specialized instructions and workflows for specific tasks.",
  "Use the skill tool to load a skill when a task matches its description.",
  Skill.fmt(list, { verbose: true }),
].join("\n")
```
`skill` tool parameters: `{ name: string }`; it asks permission
`{ permission: "skill", patterns: [params.name], always: [params.name] }` and returns
the SKILL.md body wrapped in `<skill_content name="…">` with a sampled file list.
This means `disable-model-invocation: true` from the Claude frontmatter is **ignored**;
if the port wants to suppress model-initiated skill loading, the mechanism is the
permission config `permission.skill` (patterns are skill names, e.g.
`"skill": { "*": "deny" }` or per-name). Built-in command names that would collide:
`init`, `review` (no collision with throughliner names).

### 2.4 Commands (custom slash commands)

`packages/opencode/src/config/command.ts:load(dir)`: glob `{command,commands}/**/*.md`
in each config dir. **Name comes from the file path** (relative, stripping
`command/`/`commands/` prefixes) — not from frontmatter. Frontmatter is decoded
**strictly** against (`packages/core/src/v1/config/command.ts`, verbatim):
```ts
export const Info = Schema.Struct({
  template: Schema.String,           // required; from the md body
  description: Schema.optional(Schema.String),
  agent: Schema.optional(Schema.String),
  model: Schema.optional(Schema.String),
  variant: Schema.optional(Schema.String),
  subtask: Schema.optional(Schema.Boolean),
})
```
Effect Schema `Struct` decoding rejects unknown keys → **command md files with extra
frontmatter keys fail config loading** (unlike skills). Do not copy Throughliner
skill frontmatter into command md files.

**Argument substitution** (`session/prompt.ts` command fn): `$1..$n` positional,
`$ARGUMENTS` whole-arg string; if the template has no placeholders and args are given,
args are appended after `\n\n`; `` !`cmd` `` shell injection (run in project root via
`ConfigMarkdown.shell`); `@file` references resolved to file parts.
If the command's agent is `mode: subagent` (and `subtask !== false`), the command
runs as a subtask part.

### 2.5 Agents

md files from config dirs, glob `{agent,agents}/**/*.md`. `AgentSchema` (StructWithRest
— unknown keys fold into `options`): `model?, variant?, temperature?, top_p?, prompt?,
tools? (deprecated → permission; write|edit|patch → edit), disable?, description?,
mode?: "subagent"|"primary"|"all", hidden?, options?, color?, steps?,
permission?: ConfigPermissionV1.Info`.
Built-in agents: `build` (primary, default), `plan` (primary, edit denied),
`general` (subagent), `explore` (subagent), hidden `compaction`/`title`/`summary`.
Config `permission` merges into every agent; agent-specific `permission` overrides.

### 2.6 Permissions

`packages/opencode/src/permission/index.ts`:
- `evaluate(permission, pattern, ...rulesets)`: **last** matching rule wins
  (`Wildcard.match` on both permission and pattern); default when nothing matches:
  `{ action: "ask", permission, pattern: "*" }`.
- `ask`: `deny` → throws `DeniedError`; `allow` → passes; otherwise creates a pending
  request, publishes `permission.asked`, and **blocks on a deferred** until a reply.
- `Reply = "once" | "always" | "reject"` ("always" records allow rules for the
  request's `always` patterns).
- Error messages the model sees (verbatim from `packages/core/src/v1/permission.ts`):
  - `DeniedError`: `"The user has specified a rule which prevents you from using this specific tool call. Here are some of the relevant rules {ruleset}"`
  - `RejectedError`: `"The user rejected permission to use this specific tool call."`
  - `CorrectedError`: `"The user rejected permission to use this specific tool call with the following feedback: {feedback}"`
- **Headless `opencode run`** (`cli/cmd/run.ts:801-826`, verbatim):
  ```ts
  if (event.type === "permission.asked") {
    const permission = event.properties
    if (!sessions.has(permission.sessionID)) continue
    if (auto) {
      await client.permission.reply({ requestID: permission.id, reply: "once" })
    } else {
      UI.println(... `permission requested: ${permission.permission} (${permission.patterns.join(", ")}); auto-rejecting`)
      await client.permission.reply({ requestID: permission.id, reply: "reject" })
    }
  }
  ```
  i.e. `--auto` → approve all asks; without it → **auto-reject** (with a console
  notice). A pending permission that is never replied to does NOT hang the process in
  run mode.
- Tool→permission mapping: `write`/`edit`/`apply_patch` → permission `edit` with
  pattern = path relative to worktree; `read` → `read`; `bash` → `bash`; `task` →
  `task`; `skill` → `skill` (pattern = skill name); etc. (permission schema keys:
  `read, edit, glob, grep, list, bash, task, external_directory, todowrite, question,
  webfetch, websearch, lsp, doom_loop, skill` + open `Record<string, Rule>`).
- **The `permission.ask` plugin hook (declared in the `Hooks` type) is NEVER triggered
  anywhere in the 1.18.21 server code** (grep-verified). It is dead in this version.
- The SDK client (`@opencode-ai/sdk` `OpencodeClient`) likewise has **no
  method to create a permission request** — only
  `postSessionIdPermissionsPermissionId` (the reply:
  `POST /session/{id}/permissions/{permissionID}`, body
  `{ response: "once"|"always"|"reject" }`). A plugin therefore cannot raise
  a permission prompt on 1.18.x; the host's own permission system (config
  `permission.*`) is the only prompt path.

### 2.7 Instructions (auto-injected context — output-style landing spot)

`packages/opencode/src/session/instruction.ts` (verbatim logic):
- Global: first existing of `~/.config/opencode/AGENTS.md`, `~/.claude/CLAUDE.md`
  (the latter only if `disableClaudeCodePrompt` is off).
- Project: walking up from cwd to worktree, first match of `AGENTS.md`, `CLAUDE.md`,
  `CONTEXT.md` (deprecated).
- `config.instructions[]`: relative globs (walked up), absolute paths, `~/` paths,
  or `http(s)://` URLs (fetched).
- Each file is wrapped: `"Instructions from: ${filepath}\n${content}"`.
- Assembly into the system prompt (`session/prompt.ts:1257-1268`, verbatim):
  ```ts
  const [skills, env, instructions, mcpInstructions, modelMsgs] = yield* Effect.all([
    sys.skills(agent),
    sys.environment(model),
    instruction.system().pipe(Effect.orDie),
    sys.mcp(agent, session.permission),
    MessageV2.toModelMessagesEffect(msgs, model),
  ])
  const system = [
    ...env,
    ...instructions,
    ...(mcpInstructions ? [mcpInstructions] : []),
    ...(skills ? [skills] : []),
  ]
  ```
This is where the Throughliner **output style** (brevity rules) lands: a block in
project `AGENTS.md` (or `~/.config/opencode/AGENTS.md` globally) — same approach as
the omp reference port.

### 2.8 Session lifecycle events

Where idle is set (this is the Claude **Stop** equivalent — end of each turn, not
process end):
- `session/processor.ts:624` — `status.set(ctx.sessionID, { type: "idle" })` at end of
  the assistant turn.
- `session/run-state.ts:62` — runner teardown.
- `session/status.ts:41-45` (verbatim):
  ```ts
  yield* events.publish(Event.Status, { sessionID, status })
  if (status.type === "idle") {
    yield* events.publish(Event.Idle, { sessionID })
    data.delete(sessionID)
    return
  }
  ```
  → **both** `session.status` (with `{type:"idle"}`) **and** `session.idle` are
  published on every turn end.

Event payload schemas are quoted in §4.

### 2.9 `opencode run` CLI (verified via `--help` on the installed binary)

Positional `message..`; key flags: `--command <name>` ("the command to run, use
message for args"), `-m/--model provider/model`, `--agent`, `-s/--session`,
`-c/--continue`, `--fork`, `--dir <path>`, `--format default|json`, `--title`,
`--file`, `--auto` (auto-approve permissions not explicitly denied), `--variant`,
`--thinking`, `--pure` (run without external plugins). Global: `--print-logs`,
`--log-level DEBUG|INFO|WARN|ERROR`.

Non-interactive flow (`cli/cmd/run.ts`):
- Subscribes to `client.event.subscribe()`; **breaks (exits) on `session.status` with
  `status.type === "idle"`** for the target session.
- With `--command`: `client.session.command({ sessionID, agent, model,
  command: args.command, arguments: message, variant })`; otherwise
  `client.session.prompt({ sessionID, agent, model, variant,
  parts: [...files, { type: "text", text: message }] })`.
- `--format json` prints the raw event stream (every event from §2.8) to stdout —
  this is the primary smoke-observation channel.

### 2.10 Debug CLI (no model calls — ideal for smoke checks)

`opencode debug { config, lsp, ripgrep, file, scrap, skill, snapshot, startup,
agent, v2, info, paths, wait }` (`cli/cmd/debug/index.ts`).
- `opencode debug skill` → `JSON.stringify(skills, null, 2)` of **all discovered
  skills** (name/description/location/content).
- `opencode debug info` → version + `plugins:` list (specs from config; "external
  plugins disabled (--pure)" when pure).
- `opencode debug paths` → global data/config/cache/state dirs.

### 2.11 Config discovery notes (general)

- Global config lives at `~/.config/opencode/opencode.jsonc` (valid 1.18.21 config
  format: `provider` map + `model` string — see §2.4). A self-contained smoke
  fixture must ship its own project `opencode.json` (see §6/§7); there is no
  requirement that a global config exist.
- `~/.opencode.json` — legacy dot-file, **not loaded** by 1.18.21 (see §2.1).
- `~/.config/opencode/` may contain `agent/` + `agents/` and `commands/` — evidence
  that both singular and plural dir names are used; the globs cover both.
- **Endpoint check before any live run**: `curl -s <your-endpoint>/v1/models` —
  confirm the provider's `baseURL` responds before budgeting model time.

---

## 3. Mapping table: Claude Code → OpenCode 1.18.21

| # | Claude Code mechanism (Throughliner) | OpenCode equivalent | Path / format | Fidelity |
|---|--------------------------------------|---------------------|---------------|----------|
| 1 | 5 SKILL.md skills (`setup`, `plan`, `next`, `rescan`, `done`) | Skill discovery + auto slash-command registration + `skill` tool | `.opencode/skills/<name>/SKILL.md` (project) or `~/.config/opencode/skills/…` (global); frontmatter `name`/`description` (extra keys ignored); invoke via `/name`, `opencode run --command <name>`, or model `skill` tool | **adapted** — files work unmodified; `disable-model-invocation`/`user-invocable` are ignored (model CAN auto-invoke skills; suppress via `permission.skill` patterns if wanted) |
| 2 | PreToolUse hook (scope-lock on `Edit\|Write\|MultiEdit`; git guard on `Bash\|PowerShell`; subagent guard on `Task\|Agent`) | `tool.execute.before` plugin hook; **deny = throw** (error text returned to model as tool result) | Plugin dir `plugin/throughliner/{package.json,index.ts}`; match on `input.tool` ∈ {`write`,`edit`,`apply_patch`,`bash`,`task`}; inspect `output.args` (`write`/`edit`: `filePath`; `apply_patch`: `patchText`; `bash`: `command`,`workdir`; `task`: `prompt`,`subagent_type`); resolve relative `filePath` against `input.directory` before feeding vendored Python | **exact** for block semantics (Claude `deny` → OpenCode throw); **adapted** for tool names: `MultiEdit`→`edit` (`replaceAll` param), `PowerShell`→`bash` (all shell kinds expose ToolID `"bash"`), `Agent`→`task` (no separate tool) |
| 3 | PostToolUse hook (`Edit\|Write\|MultiEdit` + `Bash\|PowerShell`) | `tool.execute.after` plugin hook with mutable `output = { title, output, metadata }` | same plugin; annotate/rewrite `output.output` text after execution | **adapted** — runs after the fact (cannot block, same as Claude); Claude `additionalContext` feedback → append text to `output.output` (visible to model on the same turn) |
| 4 | SessionStart hook (`session_start.py` → `hookSpecificOutput.additionalContext`) | (a) `chat.message` hook: push a synthetic `TextPart` onto `output.parts` (persisted into the user message; plugin tracks first-message-per-session) **or** (b) `experimental.chat.messages.transform` hook: re-inject a synthetic text part on the last user message **every LLM request** (the built-in `session/reminders.ts` plan-mode pattern; survives compaction) | same plugin; synthetic part shape `{ id, sessionID, messageID, type: "text", text, synthetic: true }` | **adapted** — no dedicated SessionStart event with a payload channel; `session.created` exists but the plugin cannot attach context through it. Recommend (b) for state-driven re-injection, (a) for one-shot injection |
| 5 | Stop hook (`stop.py`; can `decision: block` + reason to force continuation) | `event` hook on `session.idle` (published on every turn end, §2.8). "Block once" workaround: run vendored `stop.py`; if it would block, post a follow-up user message via `input.client.session.prompt({ path: { id: sessionID }, body: { parts: [{ type: "text", text: <reason> }] } })` | same plugin; event payload `{ type: "session.idle", properties: { sessionID } }` | **adapted + risky** — event hooks are fire-and-forget and cannot block synchronously; the follow-up prompt is a visible user message; in one-shot `opencode run`, idle also triggers process exit → race (see §5) |
| 6 | Output style (`output-styles/brevity.md`) | Instruction files auto-injected into every system prompt: project `AGENTS.md` / `CLAUDE.md` (walk-up) or `~/.config/opencode/AGENTS.md` / `~/.claude/CLAUDE.md` (global), or `config.instructions[]` | append the brevity rules verbatim as a section in `AGENTS.md` (project or global); wrapped as `"Instructions from: <path>\n<content>"` | **adapted** — always-on for the directory scope, not switchable per session (same approach as omp port) |
| 7 | Plugin/marketplace packaging (`.claude-plugin/plugin.json` + `marketplace.json`) | No marketplace. Plugin = local dir/file spec or npm package: config `"plugin": ["./plugin/throughliner"]` (resolved relative to declaring config file) OR drop `index.ts` into `.opencode/plugin/` (auto-load) | `plugin/throughliner/{package.json, index.ts, <vendored python>}`; `package.json` may set `engines.opencode: ">=1.18"` | **adapted** — distribution is git-clone + one config line (or npm publish); no registry/marketplace semantics to preserve |

---

## 4. Exact event/payload schemas (verbatim from 1.18.21 source)

### 4.1 Hooks type — `packages/plugin/src/index.ts`

```ts
export interface Hooks {
  dispose?: () => Promise<void>
  event?: (input: { event: Event }) => Promise<void>
  config?: (input: Config) => Promise<void>
  tool?: { [key: string]: ToolDefinition }
  auth?: AuthHook
  provider?: ProviderHook
  "chat.message"?: (
    input: {
      sessionID: string
      agent?: string
      model?: { providerID: string; modelID: string }
      messageID?: string
      variant?: string
    },
    output: { message: UserMessage; parts: Part[] }
  ) => Promise<void>
  "chat.params"?: (
    input: { sessionID: string; agent: string; model: Model; provider: ProviderContext; message: UserMessage },
    output: { temperature: number; topP: number; topK: number; maxOutputTokens: number | undefined; options: Record<string, any> }
  ) => Promise<void>
  "chat.headers"?: (input: { /* same as chat.params */ }, output: { headers: Record<string, string> }) => Promise<void>
  "permission.ask"?: (input: Permission, output: { status: "ask" | "deny" | "allow" }) => Promise<void>
  "command.execute.before"?: (
    input: { command: string; sessionID: string; arguments: string },
    output: { parts: Part[] }
  ) => Promise<void>
  "tool.execute.before"?: (
    input: { tool: string; sessionID: string; callID: string },
    output: { args: any }
  ) => Promise<void>
  "shell.env"?: (
    input: { cwd: string; sessionID?: string; callID?: string },
    output: { env: Record<string, string> }
  ) => Promise<void>
  "tool.execute.after"?: (
    input: { tool: string; sessionID: string; callID: string; args: any },
    output: { title: string; output: string; metadata: any }
  ) => Promise<void>
  "experimental.chat.messages.transform"?: (
    input: {},
    output: { messages: { info: Message; parts: Part[] }[] }
  ) => Promise<void>
  "experimental.chat.system.transform"?: (
    input: { sessionID?: string; model: Model },
    output: { system: string[] }
  ) => Promise<void>
  "experimental.session.compacting"?: (
    input: { sessionID: string },
    output: { context: string[]; prompt?: string }
  ) => Promise<void>
  "experimental.compaction.autocontinue"?: (
    input: { sessionID, agent, model, provider, message, overflow },
    output: { enabled: boolean }
  ) => Promise<void>
  "experimental.text.complete"?: (
    input: { sessionID, messageID, partID },
    output: { text: string }
  ) => Promise<void>
  "tool.definition"?: (
    input: { toolID: string },
    output: { description: string; parameters: any }
  ) => Promise<void>
}
```

Hooks actually **triggered** by the 1.18.21 server (grep of `plugin.trigger` in
`packages/opencode/src`): `tool.execute.before` / `tool.execute.after`
(`session/tools.ts:106/121` registry tools incl. write/edit/read/bash; `session/prompt.ts:307/389`
TaskTool; `tool/code-mode.ts:141/180`; MCP tools at `tools.ts:175/207/258/283/338/373/402/420`),
`tool.definition` (`tool/registry.ts:318`), `chat.message` (`session/prompt.ts:999`),
`chat.params` / `chat.headers` / `experimental.chat.system.transform`
(`llm/request.ts:69/114/134`), `experimental.chat.messages.transform`
(`session/prompt.ts:1255`, `session/compaction.ts:378`), `experimental.session.compacting`
(`compaction.ts:373`), `experimental.compaction.autocontinue` (`compaction.ts:500`),
`experimental.text.complete` (`processor.ts:516`), `shell.env` (`session/prompt.ts:554`,
`tool/shell.ts:417`, `server/routes/.../pty.ts:71`), `command.execute.before`
(`session/prompt.ts:1460`), plus the `config` hook (called once at load with the merged
cfg) and the `event` hook (all bus events for this instance directory). **`permission.ask`
is declared but never triggered.**

`chat.message` call site (verbatim, `session/prompt.ts:999`):
```ts
yield* plugin.trigger(
  "chat.message",
  {
    sessionID: input.sessionID,
    agent: input.agent,
    model: input.model,
    messageID: input.messageID,
    variant: input.variant,
  },
  { message: info, parts: resolvedParts },
)
```
Parts pushed onto `output.parts` here are **persisted** into the stored user message
(`for (const part of parts) yield* sessions.updatePart(part)`) and therefore remain in
model context for all later turns. Synthetic parts (reminders.ts pattern) are the
established internal mechanism for hidden context injection:
```ts
userMessage.parts.push({
  id: PartID.ascending(),
  messageID: userMessage.info.id,
  sessionID: userMessage.info.sessionID,
  type: "text",
  text: <text>,
  synthetic: true,
})
```

### 4.2 Tool IDs + arg schemas (for the PreToolUse shim)

Exact tool IDs (first arg of `Tool.define` in `packages/opencode/src/tool/`):
`write`, `edit`, `apply_patch`, `read`, `glob`, `grep`, `bash` (the shell tool —
`tool/shell/id.ts` verbatim: `export const ToolID = "bash"` with comment "Keep the
exposed tool ID and permission key as 'bash' for compatibility"; bash/pwsh/powershell/cmd
all report `bash`), `task` (`tool/task.ts`: `const id = "task"`), `todowrite`,
`question`, `skill`, `lsp`, `webfetch`, `websearch`, `plan_exit`, `invalid`,
plus MCP tools (`list_mcp_resources`, `list_mcp_resource_templates`,
`read_mcp_resource`, and per-server MCP tool names) and code-mode tools.

Arg schemas (verbatim from `Schema.Struct` declarations):
```ts
// write (tool/write.ts)
{ filePath: string, content: string }           // filePath absolute, or relative to instance.directory
// edit (tool/edit.ts)
{ filePath: string, oldString: string, newString: string, replaceAll?: boolean }
// apply_patch (tool/apply_patch.ts)
{ patchText: string }
// read (tool/read.ts)
{ filePath: string, offset?: NonNegativeInt, limit?: NonNegativeInt }
// bash (tool/shell/prompt.ts)
{ command: string, timeout?: PositiveInt, workdir?: string }
// task (tool/task.ts)
{ description: string, prompt: string, subagent_type: string,
  task_id?: string, command?: string, background?: boolean }
```
Relative path resolution (shim must replicate): `path.isAbsolute(params.filePath) ?
params.filePath : path.join(instance.directory, params.filePath)` (write.ts/edit.ts).
`instance.directory` corresponds to the plugin's `input.directory`.

### 4.3 Bus event payloads — `packages/sdk/js/src/gen/types.gen.ts` (verbatim)

```ts
export type SessionStatus =
  | { type: "idle" }
  | { type: "retry"; attempt: number; message: string; next: number }
  | { type: "busy" }

export type EventSessionStatus = {
  type: "session.status"
  properties: { sessionID: string; status: SessionStatus }
}

export type EventSessionIdle = {
  type: "session.idle"
  properties: { sessionID: string }
}

export type EventSessionCompacted = {
  type: "session.compacted"
  properties: { sessionID: string }
}

export type EventCommandExecuted = {
  type: "command.executed"
  properties: { name: string; sessionID: string; arguments: string; messageID: string }
}

export type Session = {
  id: string; projectID: string; directory: string; parentID?: string
  summary?: { additions: number; deletions: number; files: number; diffs?: Array<FileDiff> }
  share?: { url: string }; title: string; version: string
  time: { created: number; updated: number; compacting?: number }
  revert?: { messageID: string; partID?: string; snapshot?: string; diff?: string }
}

export type EventSessionCreated  = { type: "session.created";  properties: { info: Session } }
export type EventSessionUpdated  = { type: "session.updated";  properties: { info: Session } }
export type EventSessionDeleted  = { type: "session.deleted";  properties: { info: Session } }
export type EventSessionDiff     = { type: "session.diff";     properties: { sessionID: string; diff: Array<FileDiff> } }
export type EventSessionError    = {
  type: "session.error"
  properties: { sessionID?: string; error?: ProviderAuthError | UnknownError | MessageOutputLengthError | MessageAbortedError | ApiError }
}

export type EventMessagePartUpdated = {
  type: "message.part.updated"
  properties: { part: Part; delta?: string }
}
export type EventMessagePartRemoved = {
  type: "message.part.removed"
  properties: { sessionID: string; messageID: string; partID: string }
}
```
`message.updated` carries `properties: { sessionID, info: Message }` (shape confirmed
by the `run.ts:713-718` consumer: `event.properties.sessionID`,
`event.properties.info.role === "assistant"`, `info.agent`, `info.modelID`).
`message.part.updated.part` is a `Part` union; tool parts are
`{ id, sessionID, messageID, type: "tool", callID, tool, state: ToolState, metadata? }`
where `state.status` ∈ `"pending" | "running" | "completed" | "error"` (error text in
`state.error`) — the smoke-observation hook for blocked tools.

**Permission events** (v1 bridge actually published at runtime —
`packages/schema/src/v1/permission.ts`, verbatim):
```ts
export const Request = Schema.Struct({
  id: ID,
  sessionID: SessionID,
  permission: Schema.String,
  patterns: Schema.Array(Schema.String),
  metadata: Schema.Record(Schema.String, Schema.Unknown),
  always: Schema.Array(Schema.String),
  tool: Schema.optional(Schema.Struct({ messageID: Schema.String, callID: Schema.String })),
}).annotate({ identifier: "PermissionRequest" })

export const Reply = Schema.Literals(["once", "always", "reject"])

const Asked   = define({ type: "permission.asked",   schema: Request.fields })
const Replied = define({ type: "permission.replied", schema: { sessionID: SessionID, requestID: ID, reply: Reply } })
```
(The SDK's generated `types.gen.ts` also declares v2-shaped `permission.updated` /
`permission.replied`; the 1.18.21 runtime emits `permission.asked`/`permission.replied`
via the v1 bridge — `run.ts` keys on `permission.asked`.)

### 4.4 SDK client calls available to the plugin (`PluginInput.client`)

- `client.session.prompt({ path: { id: sessionID }, body: { parts, noReply?, system?, agent?, model? } })`
  (`POST /session/{id}/message`; also `promptAsync` → `POST /session/{id}/prompt_async`)
  — the channel for the Stop "block once" follow-up message.
- `client.session.command({ sessionID, agent, model, command, arguments, variant })`
- `client.event.subscribe()` — event stream (also what `opencode run` consumes)
- `client.permission.reply({ requestID, reply: "once"|"always"|"reject", message? })`
- `client.app.log({ body: { service, level, message, extra } })` — structured plugin logging

### 4.5 Upstream Throughliner hook stdin/stdout contract (what the shim must serve)

Claude hook JSON on stdin: `session_id`, `cwd`, `hook_event_name`, `tool_name`,
`tool_input` (+ `last_assistant_message` for Stop). Decisions on stdout: allow/deny/ask
+ reason, and `hookSpecificOutput.additionalContext`. Vendored scripts (pristine):
`hooks/session_start.py` (91 KB), `hooks/pre_tool_use.py` (73 KB),
`hooks/post_tool_use.py` (49 KB), `hooks/stop.py` (12 KB). All state is read from
project files; scripts are stdin/stdout-only (same posture as the omp port).

---

## 5. Gaps & risks

1. **No `permission.ask` hook (dead in 1.18.21)** → Claude's `ask` decision (e.g.
   subagent cost gate) has no interactive headless equivalent. In `opencode run`
   without `--auto`, any `ask` permission is **auto-rejected**. Workarounds:
   (a) fail-open: shim treats `ask` as `allow` (matches omp port); (b) deny-with-reason
   via throw in `tool.execute.before`. In TUI sessions, `ask` does work via the native
   permission UI (config `permission` rules → `permission.asked` → user reply).
2. **Stop "block once" race in one-shot `opencode run`**: the run loop breaks on the
   same `session.status idle` event the plugin's event hook receives; a follow-up
   `session.prompt` posted at idle may race process exit. Must be verified empirically
   in smoke. Document that Stop-block fully works in TUI/long-lived sessions and is
   best-effort under `run`.
3. **`event` hooks are fire-and-forget** (`void hook["event"]`): no guarantee the Stop
   shim finishes before the process exits; the shim should spawn Python
   synchronously-with-timeout, keep it short, and fail-open on timeout.
4. **Fail-open posture**: a throw from `tool.execute.before` is the ONLY deny path —
   so the shim must catch every unexpected error (spawn failure, timeout, non-JSON
   stdout, Python traceback) and only throw when vendored Python explicitly emits a
   deny decision. Any uncaught exception in the shim = accidental fail-CLOSED (blocks
   all tools with a confusing error).
5. **Relative paths**: Claude protocol is absolute; OpenCode `write`/`edit`
   `filePath` may be relative to the instance directory. The shim MUST resolve
   (`input.directory`) before feeding Python, and re-map denials' reasons back to the
   model-facing path. Same treatment for `bash.workdir`-relative reasoning (the git
   guard sees `command` + `workdir`).
6. **Tool name mapping** (see §3 row 2): `MultiEdit` has no distinct tool (covered by
   `edit`); `PowerShell`/`cmd` all surface as `bash`; `Agent` has no distinct tool
   (subagents = `task` with `subagent_type`). The vendored Python matcher list must be
   translated in the shim, not by editing the Python.
7. **`disable-model-invocation` is ignored**: the model can auto-invoke any skill via
   the `skill` tool. If Throughliner's setup/plan skills must stay user-initiated,
   configure `permission: { "skill": { "setup": "deny", ... } }` per name (or `"*"`),
   accepting that this also affects `always`-reply behavior. Acceptable default:
   leave model invocation enabled (skills are idempotent methods, not actions).
8. **Skill name collisions**: first scanned wins (global `~/.claude/skills` scanned
   before project `.opencode/skills`); the built-in `customize-opencode` is pre-registered
   (a disk skill with that name would override it — no throughliner name collides).
9. **Command md frontmatter is strict** (unknown keys fail config load) — never port
   skill frontmatter into `.opencode/command*.md`; skills use the permissive path.
10. **Legacy `~/.opencode.json` is not loaded** — do not ship anything relying on it;
    universal installs use `.opencode/` project config or `~/.config/opencode/`.
11. **Model quality**: the smoke model (whatever the machine runs) may follow
    multi-step skill methods imperfectly — smoke tests assert PLUMBING (hooks fired,
    denials enforced, context injected), not output quality.
12. **Endpoint/port**: verify the provider's `baseURL` responds before smoke
    (§6 step 0).

---

## 6. Smoke-test plan (any machine; slow local models budget 3–15 min per run)

**Fixture**: a scratch git project containing the ported plugin and an
`opencode.json`:
```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "<provider>/<model-id>",
  "plugin": ["<abs-path-to-repo>/opencode/plugin.ts"]
}
```

**Step 0 — endpoint check** (30 s):
```sh
curl -s <your-endpoint>/v1/models
```
Confirm the configured provider responds; if not, stop and report. (If the fixture
needs its own provider block, see §7.)

**Step 1 — zero-model verification** (seconds):
```sh
cd /tmp/tl-smoke-opencode
opencode debug skill     # expect all 5 throughliner skills listed as JSON (+ built-in customize-opencode)
opencode debug info      # expect "plugins:" listing ./plugin/throughliner
opencode debug config    # merged config sanity
opencode debug paths     # config/data dirs
opencode run --pure "ping" --print-logs --log-level DEBUG   # A/B: plugin disabled baseline
```

**Step 2 — one-shot skill runs** (each 3–15 min; capture the full event stream):
```sh
opencode run --dir /tmp/tl-smoke-opencode --command setup  --title tl-setup  --format json --print-logs --log-level DEBUG > /tmp/tl-smoke/opencode-setup.json 2> /tmp/tl-smoke/opencode-setup.log
opencode run --dir /tmp/tl-smoke-opencode --command plan   --title tl-plan   --format json --print-logs --log-level DEBUG > /tmp/tl-smoke/opencode-plan.json   2> /tmp/tl-smoke/opencode-plan.log
opencode run --dir /tmp/tl-smoke-opencode --command next   --title tl-next   --format json --print-logs --log-level DEBUG > /tmp/tl-smoke/opencode-next.json   2> /tmp/tl-smoke/opencode-next.log
opencode run --dir /tmp/tl-smoke-opencode --command rescan --title tl-rescan --format json --print-logs --log-level DEBUG > /tmp/tl-smoke/opencode-rescan.json 2> /tmp/tl-smoke/opencode-rescan.log
opencode run --dir /tmp/tl-smoke-opencode --command done   --title tl-done   --format json --print-logs --log-level DEBUG > /tmp/tl-smoke/opencode-done.json   2> /tmp/tl-smoke/opencode-done.log
```
(`--command <name>`: the positional message becomes the command's arguments — pass a
minimal task sentence for `next`/`rescan` that references a fixture file to force tool
use.)

**Step 3 — observe each of the 4 hook paths** (from the captured streams + plugin log):
1. **Plugin load / SessionStart context**: stream contains `command.executed` (name =
   skill name) and `message.part.updated` with a `synthetic: true` text part holding the
   `session_start.py` context; a load failure would appear as `session.error`
   ("Failed to load plugin …") — grep the JSON streams for `session.error` (expect none
   after fix). A/B: `--pure` runs must NOT contain the synthetic part.
2. **PreToolUse scope-lock (deny path)**: fixture task that induces a write outside the
   locked scope; expect `message.part.updated` → tool part `state.status: "error"`
   whose `state.error` carries the vendored deny reason, and the file NOT created.
   Allow path: in-scope write → `state.status: "completed"`.
3. **PostToolUse**: after an in-scope edit/bash, the tool part's output contains the
   shim's post-processing marker (append by the shim) — proves `tool.execute.after`
   ran and output mutation flowed through.
4. **Stop (`session.idle`)**: every run's stream ends with `session.idle` +
   `session.status {type:"idle"}`; the shim's log line for stop.py firing appears in
   the plugin log / stderr (shim writes one line per hook invocation to
   `/tmp/tl-smoke-opencode/.tl-hook.log` and/or `client.app.log`).

**Step 4 — git-guard check** (inside any run): instruct a guarded git command
(e.g. `git push`); expect a blocked tool part with the guard's reason.

**Step 5 — fail-open proof**: run with `PATH` missing `python3` (or point the shim's
interpreter env var at a nonexistent binary) → all tools must still work
(no denies), and the hook log records the skipped invocations.

---

## 7. Model/provider config (portable recipe — no machine values)

The port is model-agnostic: any provider/model the machine's OpenCode already has
configured works. If a smoke fixture must be self-contained (§6), the provider
block shape (any OpenAI-compatible endpoint — local llama.cpp, router, cloud):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "<provider>/<model-id>",
  "provider": {
    "<provider>": {
      "npm": "@ai-sdk/openai-compatible",
      "options": { "baseURL": "http://<host>:<port>/v1" },
      "models": {
        "<model-id>": { "name": "<label>" }
      }
    }
  }
}
```

- **Endpoint**: verify with Step 0's `curl <baseURL>/models` before budgeting
  model time.
- **API key**: keyless local endpoints need no auth; if provider init fails for a
  missing key, add `"apiKey": "not-needed"` to `options` (resolution order:
  `options.apiKey` → `provider.key` from auth/`env` vars). Alternative env form:
  `"env": ["<PROVIDER>_API_KEY"]` + export that var.
- **CLI override** (no config needed): `opencode run -m <provider>/<model-id> …`
  — `pick()` splits on the FIRST `/` (providerID = before it, modelID = the rest),
  so leading-slash model ids (llama.cpp) work.
- **Latency budget**: CPU inference runs 3–15 min per one-shot; run the 5 skill
  smokes sequentially with generous timeouts, and prefer Step 1 (zero-model)
  evidence for anything that doesn't strictly need generation.

---

## 8. Universal install contract (what ships; no machine-specific values, no secrets)

**User prerequisites** (any machine):
- OpenCode ≥ 1.18 (1.18.21 verified) — any install channel (snap/npm/binary)
- Python 3.8+ (vendored hooks are stdlib-only)
- git (Throughliner reads repo state)
- any working model/provider already configured in OpenCode — **Throughliner is a
  workflow layer, never a model choice; the port ships zero provider config**

**Install (a stranger runs exactly this)**:
```sh
git clone <port-repo-url> /path/to/throughliner-opencode   # or copy the directory
cd /path/to/your-project

# 1) register the plugin (either mechanism works):
mkdir -p .opencode/plugin
ln -s /path/to/throughliner-opencode/plugin/throughliner .opencode/plugin/throughliner
#   — OR add to opencode.json: "plugin": ["/path/to/throughliner-opencode/plugin/throughliner"]

# 2) skills (auto-discovered; become /setup /plan /next /rescan /done):
mkdir -p .opencode/skills
cp -r /path/to/throughliner-opencode/plugin/throughliner/skills/* .opencode/skills/
#   — OR config: "skills": { "paths": ["/path/to/throughliner-opencode/plugin/throughliner/skills"] }

# 3) output style (brevity): append the shipped brevity rules block to
#    AGENTS.md in the project root (per-project) or ~/.config/opencode/AGENTS.md (global)
```

**Verify (zero model calls)**: `opencode debug skill` (5 skills listed) +
`opencode debug info` (plugin listed). No secrets, no ports, no IP addresses in any
shipped file.

---

## Appendix — shim design summary (per the verified omp reference port)

- Vendored Python stays **pristine**; `plugin/throughliner/index.ts` default-exports
  `{ id: "throughliner", server: (input, options) => hooks }`.
- `tool.execute.before`: map OpenCode tool+args → Claude `PreToolUse` stdin JSON
  (resolve relative `filePath` against `input.directory`); spawn the vendored
  `pre_tool_use.py` with a timeout; parse stdout JSON; on explicit deny →
  `throw new Error(reason)` (model sees it as the tool error); on ask → treat as
  allow (fail-open, §5.1); on any error/timeout → allow + log (fail-open).
- `tool.execute.after`: same translation for `post_tool_use.py`; append its
  `additionalContext` to `output.output`.
- `chat.message` (or `experimental.chat.messages.transform`): first-user-message-per-
  session (tracked in a `Set`) → run `session_start.py` → push synthetic TextPart with
  its `additionalContext`.
- `event` on `session.idle`: run `stop.py`; if it returns block →
  `input.client.session.prompt(...)` follow-up (best-effort under `run`, §5.2).
- One log line per hook invocation (file + `client.app.log`) for smoke observation.
