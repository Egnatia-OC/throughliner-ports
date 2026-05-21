# Claude Code Plan Panel — Programmatic Write Surface Research

## Bottom line

The plan panel is **not writable from outside Claude itself** — no hook output field, MCP surface, file convention, CLI flag, or env var populates it. It is exclusively driven by Claude calling `ExitPlanMode`, which reads a plan file Claude wrote during native Plan Mode.

---

## Evidence

**How the panel actually works** — Armin Ronacher reverse-engineered the mechanism in December 2025: a plan in Claude Code is a Markdown file written into Claude's plans folder by Claude in plan mode. When exiting plan mode it reads the plan file that it wrote to disk, then starts working off that. So the path towards spec in the prompt always goes via the file system. The `ExitPlanMode` tool description confirms this: the tool does NOT take the plan content as a parameter — it reads the plan from the file Claude wrote. The tool simply signals that Claude is done planning and ready for the user to review and approve.
- Source: https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/

**What hooks can and cannot do** — The full hooks reference documents every stdout JSON field and every `hookSpecificOutput` shape. None of them target the plan panel. The `ExitPlanMode` hook input does expose `plan` and `planFilePath` (so a `PreToolUse` hook can *read* the plan Claude wrote), but there is no inverse: no hook output field that *injects* content into the panel. `additionalContext` puts text into Claude's context window, not the plan panel.
- Source: https://docs.claude.com/en/docs/claude-code/hooks

**A plugin author hit this exact wall, April 2026** — The `superpowers` issue #1260 describes the problem precisely: the `writing-plans` skill writes a structured implementation plan and hands it off for review, but never enters native Plan Mode and never calls `ExitPlanMode`. As a result, the Plan side panel in the desktop app stays empty ("No plan yet…") even though a thorough plan is actively being written in the chat. The proposed workarounds are all Claude-mediated — have Claude enter plan mode and call `ExitPlanMode` after writing the file — not direct writes from outside.
- Source: https://github.com/obra/superpowers/issues/1260

**The only viable indirect path** — Two options were proposed in the superpowers issue, neither of which is a direct write surface:
- **Option A:** After the plan file is written, instruct the agent to enter Plan Mode, have it read/summarise the plan from disk into the plan-mode plan file, then call `ExitPlanMode`.
- **Option B:** Write the plan to both the skill's output location *and* the active plan-mode plan file — though this requires verifying whether writing to that file without entering Plan Mode actually populates the panel.

Both require Claude to execute the native flow.

---

## What I checked that came back empty

- Full hooks reference (`/en/hooks`): no `hookSpecificOutput` field targets the plan panel.
- Settings reference (`/en/settings`): no key seeds plan panel state; plan-related settings only govern model and permission behaviour.
- GitHub `anthropics/claude-code` plugins README: plan panel not mentioned.
- Web search for "plan panel programmatic write hook plugin": returned the superpowers issue and community workarounds, none of which describe a direct write surface.
- No `.claude/plan.json` or equivalent file convention appears anywhere in the docs or community discussion.

---

## Caveats

- The `ExitPlanMode` `PreToolUse` hook can *modify* `tool_input` (which includes `plan` and `planFilePath`) before Claude Code reads it. That means a hook could theoretically intercept Claude's own `ExitPlanMode` call and swap in different plan content — but only if Claude is already running through a native plan-mode session. It does not let a plugin initiate the panel fill from scratch.
- The desktop app's Plan panel was redesigned on April 14, 2026. The docs have not been updated to describe its internals, so it is possible a write surface exists but is simply undocumented. The superpowers issue, filed in late April 2026, shows that no such surface was obvious to an experienced Claude Code plugin author actively looking for one.
- Anthropic could add a `planContent` field to some hook's `hookSpecificOutput` in a future release. Nothing in the current docs or public signals suggests this is planned.
