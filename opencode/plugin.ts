/**
 * Throughliner plugin for OpenCode / Kilo Code.
 *
 * Translates the host's plugin hooks into the Claude Code hook contract that
 * the vendored Throughliner Python hooks speak (vendor/throughliner/hooks/).
 * The vendored files are pristine upstream content; this file is the entire
 * port surface.
 *
 * Mapping (host event -> vendored hook):
 *   tool.execute.before  -> pre_tool_use.py   (deny -> throw; ask -> trace+log, host gate decides)
 *   tool.execute.after   -> post_tool_use.py  (additionalContext appended to tool output)
 *   session.created      -> session_start.py  (context stashed, injected per
 *                                                            LLM call via system.transform)
 *   experimental.chat.system.transform -> output-styles/brevity.md (always-on)
 *
 * The five method skills (setup/plan/next/rescan/done) are materialized at
 * plugin init into the host's global skills directory, with
 * ${CLAUDE_PLUGIN_ROOT} rewritten to the vendored tree's absolute path.
 *
 * Everything fails open: any error here degrades to "no Throughliner", never
 * to a broken session.
 */
import { spawn } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import type { OpencodeClient } from "@opencode-ai/sdk";

// ---------------------------------------------------------------------------
// Port configuration: SKILLS_DIR is the one thing the Kilo port changes —
// it is env-configurable, so the port just sets THROUGHLINER_SKILLS_DIR.
// ---------------------------------------------------------------------------

function skillsDir(): string {
  if (process.env.THROUGHLINER_SKILLS_DIR) return process.env.THROUGHLINER_SKILLS_DIR;
  // OpenCode auto-loads skills from OPENCODE_CONFIG_DIR when it is set, so
  // materialize there rather than only in the default global dir.
  if (process.env.OPENCODE_CONFIG_DIR) return path.join(process.env.OPENCODE_CONFIG_DIR, "skills");
  return path.join(homedir(), ".config", "opencode", "skills");
}

const SKILLS_DIR = skillsDir();
const LOG_PREFIX = "[throughliner]";

// ---------------------------------------------------------------------------
// Root resolution: this file lives at <repo>/opencode/plugin.ts
// ---------------------------------------------------------------------------

function repoRoot(): string | null {
  let root: string | null = null;
  if (process.env.THROUGHLINER_ROOT) {
    root = process.env.THROUGHLINER_ROOT;
  } else {
    try {
      const here = path.dirname(fileURLToPath(import.meta.url));
      root = path.join(path.dirname(here), "vendor", "throughliner");
    } catch {
      return null;
    }
  }
  // A path that is not a usable vendor tree is the same as none: the plugin
  // disables itself instead of running inert hooks against missing files.
  try {
    if (!existsSync(path.join(root, "hooks", "pre_tool_use.py"))) return null;
  } catch {
    return null;
  }
  return root;
}

const VENDOR_ROOT = repoRoot();

function log(msg: string): void {
  try {
    console.error(LOG_PREFIX + " " + msg);
  } catch {
    // never throw from logging
  }
}

// .throughliner/ is per-project scratch (add it to the project's
// .gitignore). Disable the channel entirely: THROUGHLINER_TRACE=0.
const TRACE_ENABLED = process.env.THROUGHLINER_TRACE !== "0";

// Best-effort debug channel: one JSON line per hook fire, appended to
// <cwd>/.throughliner/.shim-<sessionID>.jsonl — the primary observation
// channel for live runs. Never throws.
function trace(cwd: string, sid: string | undefined, entry: Record<string, unknown>): void {
  try {
    if (!TRACE_ENABLED || !cwd || !sid) return;
    const dir = path.join(cwd, ".throughliner");
    mkdirSync(dir, { recursive: true });
    const line = JSON.stringify({ at: new Date().toISOString(), session: sid, ...entry });
    writeFileSync(path.join(dir, `.shim-${sid.slice(0, 40)}.jsonl`), line + "\n", { flag: "a" });
  } catch {
    // tracing must never affect the session
  }
}

// The vendored scope-lock matches per-session working-file names
// (_build-<id>.md / _freeform-<id>.md) against a LOWERCASE-ONLY shape —
// pre_tool_use.py: ^_(build|freeform)-[a-z0-9._-]+\.md$ — and decides
// "build vs planning" by whether the file named from the hook payload's
// session_id exists. Harness session ids on this host are mixed-case
// (opencode/kilo "ses_..." base62), so passing the raw id deadlocks /next's
// bootstrap: the first write — creating the session's own _build-<id>.md —
// is denied as planning mode, and the session can never reach build mode
// (observed live in a smoke run; the model read the hook source and filed a
// queue item about it). Every hook payload therefore carries the lowercased
// id, and the session-orientation note tells the model the same lowercased
// name. The harness's own client calls keep the raw id.
function hookSid(sid: string): string {
  return sid.toLowerCase();
}

// ---------------------------------------------------------------------------
// Hook runner: spawn the vendored Python, feed Claude-protocol JSON, parse
// the JSON reply. Fail-open on every failure mode.
// ---------------------------------------------------------------------------

interface HookReply {
  decision?: string;
  reason?: string;
  hookSpecificOutput?: {
    hookEventName?: string;
    permissionDecision?: string;
    permissionDecisionReason?: string;
    additionalContext?: string;
  };
}

function runHook(script: string, payload: unknown, timeoutMs: number): Promise<HookReply | null> {
  const { promise, resolve } = Promise.withResolvers<HookReply | null>();
  if (!VENDOR_ROOT) {
    resolve(null);
    return promise;
  }
  const bin = process.env.THROUGHLINER_PYTHON ?? "python3";
  const hookPath = path.join(VENDOR_ROOT, "hooks", script);
  let child;
  try {
    child = spawn(bin, [hookPath], {
      cwd: (payload as { cwd?: string }).cwd || process.cwd(),
      env: { ...process.env, CLAUDE_PLUGIN_ROOT: VENDOR_ROOT },
      stdio: ["pipe", "pipe", "pipe"],
    });
  } catch (err) {
    log(`${script} spawn failed: ${String(err)}`);
    resolve(null);
    return promise;
  }
  let stdout = "";
  let stderr = "";
  let settled = false;
  const finish = (reply: HookReply | null) => {
    if (settled) return;
    settled = true;
    clearTimeout(timer);
    resolve(reply);
  };
  const timer = setTimeout(() => {
    try { child.kill("SIGKILL"); } catch { /* already dead */ }
    log(`${script} timed out after ${timeoutMs}ms — failing open`);
    finish(null);
  }, timeoutMs);
  child.stdout?.on("data", (d: Buffer) => { stdout += d.toString(); });
  child.stderr?.on("data", (d: Buffer) => { stderr += d.toString(); });
  child.on("error", (err) => {
    log(`${script} failed to start (${bin}): ${String(err)} — failing open`);
    finish(null);
  });
  child.on("close", (code) => {
    if (code !== 0 && !stdout) {
      log(`${script} exited ${code}: ${stderr.slice(0, 400)} — failing open`);
      finish(null);
      return;
    }
    const text = stdout.trim();
    if (!text) {
      finish(null);
      return;
    }
    try {
      finish(JSON.parse(text) as HookReply);
      return;
    } catch { /* fall through */ }
    const last = text.split("\n").filter((l) => l.trim()).pop();
    if (last) {
      try {
        finish(JSON.parse(last) as HookReply);
        return;
      } catch { /* fall through */ }
    }
    log(`${script} returned non-JSON output — failing open`);
    finish(null);
  });
  child.stdin?.on("error", () => { /* EPIPE on fast exit; close handler covers it */ });
  child.stdin?.write(JSON.stringify(payload));
  child.stdin?.end();
  return promise;
}

// ---------------------------------------------------------------------------
// Claude tool-name mapping
// ---------------------------------------------------------------------------

/** opencode tool name -> Claude hook tool_name, or null for tools Throughliner does not police. */
function claudeToolName(tool: string): string | null {
  switch (tool) {
    case "write":
      return "Write";
    case "edit":
      return "MultiEdit";
    case "bash":
      return "Bash";
    case "task":
      return "Task";
    case "skill":
      return "Skill";
    default:
      return null;
  }
}

/** Build the Claude tool_input from the host's tool args. The vendored hooks
 * read exactly: file_path (Edit/Write/MultiEdit), command (Bash/PowerShell),
 * skill (Skill). Relative paths are resolved against the session cwd — the
 * Claude protocol is absolute. */
function claudeToolInput(tool: string, args: Record<string, unknown>, cwd: string): Record<string, unknown> {
  const out: Record<string, unknown> = {};
  const filePath = args.filePath ?? args.file_path ?? args.path;
  if (typeof filePath === "string") {
    out.file_path = path.isAbsolute(filePath) ? filePath : path.resolve(cwd, filePath);
  }
  if (typeof args.command === "string") out.command = args.command;
  if (typeof args.name === "string" && tool === "skill") out.skill = args.name;
  if (typeof args.description === "string") out.description = args.description;
  return out;
}

// ---------------------------------------------------------------------------
// Skill materialization
// ---------------------------------------------------------------------------

const SKILL_NAMES = ["setup", "plan", "next", "rescan", "done"];

function materializeSkills(): void {
  for (const name of SKILL_NAMES) {
    try {
      const src = path.join(VENDOR_ROOT as string, "skills", name, "SKILL.md");
      const body = readFileSync(src, "utf8").replace(/\$\{CLAUDE_PLUGIN_ROOT\}/g, VENDOR_ROOT as string);
      const dir = path.join(SKILLS_DIR, name);
      mkdirSync(dir, { recursive: true });
      const dest = path.join(dir, "SKILL.md");
      let current = "";
      try { current = readFileSync(dest, "utf8"); } catch { /* first install */ }
      if (current !== body) writeFileSync(dest, body);
    } catch (err) {
      log(`skill materialization failed for ${name}: ${String(err)}`);
    }
  }
}

// ---------------------------------------------------------------------------
// Plugin
// ---------------------------------------------------------------------------

// The host passes the real @opencode-ai/sdk client. We type against the
// actual SDK (not a hand-rolled shape) so tsc catches API drift at build
// time — the earlier flat `{ sessionID, parts }` calls passed a hand-rolled
// type but 404 against the real `path`/`body` envelope.
interface PluginInputLike {
  client: OpencodeClient;
  directory?: string;
  [k: string]: unknown;
}

export default function throughlinerPlugin(input: PluginInputLike) {
  if (!VENDOR_ROOT) {
    log("vendored tree not found next to the plugin (expected vendor/throughliner/) — plugin disabled");
    return Promise.resolve({});
  }
  materializeSkills();

  const startContext = new Map<string, Promise<string | null>>();
  const stopBlocks = new Map<string, number>();

  function sessionStart(sid: string, cwd: string): Promise<string | null> {
    let p = startContext.get(sid);
    if (!p) {
      p = runHook("session_start.py", { cwd, session_id: hookSid(sid) }, 60_000).then((out) => {
        const ctx = out?.hookSpecificOutput?.additionalContext ?? null;
        if (!ctx) startContext.delete(sid);
        return ctx;
      }).catch((err) => {
        log(`session_start failed: ${String(err)}`);
        startContext.delete(sid);
        return null;
      });
      startContext.set(sid, p);
    }
    return p;
  }

  function cwdOf(): string {
    return input.directory || process.cwd();
  }

  async function onStopIdle(sid: string): Promise<void> {
    const cwd = cwdOf();
    let messages: Array<{ info?: { role?: string }; parts?: Array<{ type?: string; text?: string }> }> = [];
    try {
      const res = await input.client.session.messages({ path: { id: sid } });
      messages = (res?.data ?? []) as typeof messages;
    } catch (err) {
      log(`stop: message fetch failed: ${String(err)}`);
      return;
    }
    const assistant = messages.filter((m) => m.info?.role === "assistant");
    const last = assistant[assistant.length - 1];
    if (!last) return;
    const text = (last.parts ?? [])
      .filter((p) => p.type === "text" && typeof p.text === "string")
      .map((p) => p.text as string)
      .join("\n")
      .trim();
    if (!text) return;
    const out = await runHook("stop.py", { last_assistant_message: text, cwd, session_id: hookSid(sid) }, 30_000);
    if (out?.decision !== "block" || !out.reason) return;
    const count = (stopBlocks.get(sid) ?? 0) + 1;
    if (count > 2) {
      log(`stop-block cap (2) reached for ${sid} — stopping the loop`);
      return;
    }
    stopBlocks.set(sid, count);
    trace(cwd, sid, { hook: "stop", decision: "block", block: count });
    try {
      await input.client.session.prompt({ path: { id: sid }, body: { parts: [{ type: "text", text: out.reason }] } });
      log(`stop-block fired for ${sid} (block ${count}/2)`);
    } catch (err) {
      log(`stop-block re-prompt failed: ${String(err)}`);
    }
  }


  // Intentional denial from the vendored Python; must propagate even through fail-open catches.
  class ToolDenied extends Error {}

  return Promise.resolve({
    async "tool.execute.before"(
      _input: { tool: string; sessionID: string; callID: string; [k: string]: unknown },
      output: { args: Record<string, unknown> },
    ): Promise<void> {
      try {
        const claudeName = claudeToolName(_input.tool);
        if (!claudeName) return;
        const cwd = cwdOf();
        const payload = {
          cwd,
          session_id: hookSid(_input.sessionID),
          tool_name: claudeName,
          tool_input: claudeToolInput(_input.tool, output.args ?? {}, cwd),
        };
        const out = await runHook("pre_tool_use.py", payload, 30_000);
        const decision = out?.hookSpecificOutput?.permissionDecision;
        const reason = out?.hookSpecificOutput?.permissionDecisionReason ?? "blocked by Throughliner";
        if (decision === "deny") {
          trace(cwd, _input.sessionID, { hook: "pre_tool_use", tool: claudeName, decision: "deny", action: "throw" });
          throw new ToolDenied(reason);
        }
        if (decision === "ask") {
          // OpenCode 1.18.x gives plugins no way to raise a permission prompt:
          // the SDK client has no permission-create method, and the
          // `permission.ask` hook is declared but never triggered
          // (source-verified, ANALYSIS.md section 2.6). Record the cost
          // reason in the trace and let the host's own permission system
          // gate the call: default config asks in the TUI, headless
          // `opencode run` auto-rejects (approve with --auto), and
          // `permission.task` in opencode.json overrides.
          trace(cwd, _input.sessionID, { hook: "pre_tool_use", tool: claudeName, decision: "ask", action: "allow(native gate)", reason });
          log(`cost gate: ${reason} — no plugin prompt API on this host; OpenCode's native permission gate decides`);
        } else {
          trace(cwd, _input.sessionID, { hook: "pre_tool_use", tool: claudeName, decision: "none", action: "allow" });
        }
      } catch (err) {
        // Fail-open: the ONLY tool denial path is an explicit Python "deny" decision
        // (ToolDenied). Any unexpected shim error must not block the user's tools.
        if (err instanceof ToolDenied) throw err;
        log(`tool.execute.before error — allowing (fail-open): ${String(err)}`);
      }
    },

    // Trigger: ({ tool, sessionID, callID, args }, <tool result: { title, output, metadata, ... }>)
    // — args arrive on the INPUT; the result object is the mutable OUTPUT.
    async "tool.execute.after"(
      _input: { tool: string; sessionID: string; callID: string; args?: Record<string, unknown>; [k: string]: unknown },
      output: { output?: string; [k: string]: unknown },
    ): Promise<void> {
      try {
        const claudeName = claudeToolName(_input.tool);
        if (!claudeName) return;
        if (!["Write", "MultiEdit", "Bash"].includes(claudeName)) return;
        const cwd = cwdOf();
        const payload = {
          cwd,
          session_id: hookSid(_input.sessionID),
          tool_name: claudeName,
          tool_input: claudeToolInput(_input.tool, _input.args ?? {}, cwd),
        };
        const out = await runHook("post_tool_use.py", payload, 30_000);
        const ctx = out?.hookSpecificOutput?.additionalContext;
        if (!ctx) return;
        if (typeof output.output === "string") {
          output.output += `\n\n${ctx}`;
          trace(cwd, _input.sessionID, { hook: "post_tool_use", tool: claudeName, action: "context-appended" });
        }
      } catch (err) {
        log(`tool.execute.after error — ignoring (fail-open): ${String(err)}`);
      }
    },

    // The server dispatches as hook["event"]({ event: { id, type, properties: <bus data> } })
    // (opencode plugin/index.ts:259).
    async event(input: {
      event?: { type?: string; properties?: { sessionID?: string; [k: string]: unknown }; [k: string]: unknown };
    }): Promise<void> {
      const event = input.event;
      if (!event) return;
      const sid = event.properties?.sessionID;
      if (!sid) return;
      if (event.type === "session.created") {
        void sessionStart(sid, cwdOf());
      } else if (event.type === "session.deleted") {
        startContext.delete(sid);
        stopBlocks.delete(sid);
      } else if (event.type === "session.idle") {
        void onStopIdle(sid);
      }
    },

    async "experimental.chat.system.transform"(
      _input: { sessionID?: string; [k: string]: unknown },
      output: { system: string[] },
    ): Promise<void> {
      try {
        const brevity = readFileSync(path.join(VENDOR_ROOT as string, "output-styles", "brevity.md"), "utf8");
        output.system.push(`[Throughliner output style — always on]\n${brevity}`);
      } catch (err) {
        log(`brevity injection failed: ${String(err)}`);
      }
      if (!_input.sessionID) return;
      const ctx = await sessionStart(_input.sessionID, cwdOf());
      if (ctx) {
        // The vendored hooks name per-session working files _build-<id>.md
        // from the hook payload's session_id; Claude Code shows the model its
        // session id natively, this host does not, so the shim says it. The id
        // is lowercased (hookSid) to match the lowercase-only working-file
        // shape the vendored scope-lock accepts — see hookSid.
        const safeId = hookSid(_input.sessionID).replace(/[^a-z0-9._-]/g, "_");
        const idNote = `Session ID for this session: ${safeId} — per-session working files are named with it, exactly _build-${safeId}.md (and _freeform-${safeId}.md for freeform work).`;
        output.system.push(`[Throughliner session orientation — injected once per session by the session_start hook]\n${ctx}\n${idNote}`);
      }
    },
  });
}

export type { PluginInputLike };
