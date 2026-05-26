# Claude Code Plan Panel — Programmatic Write Surface Research

## Bottom line

The plan panel is **not writable from outside Claude itself.** No hook output field, MCP surface, file convention, or CLI flag populates it. It is exclusively driven by Claude calling `ExitPlanMode`, which reads a plan file Claude wrote during native Plan Mode.

---

## Evidence

**How it works** — A plan is a Markdown file Claude writes to disk in plan mode. `ExitPlanMode` reads that file; it does not take plan content as a parameter. (Source: Armin Ronacher, Dec 2025.)

**Hooks can read but not write** — `ExitPlanMode` PreToolUse input exposes `plan` and `planFilePath`, but no hook output field injects into the panel. `additionalContext` goes into Claude's context, not the panel.

**A plugin author hit this wall (Apr 2026)** — superpowers issue #1260: a skill writes a structured plan but never enters Plan Mode, so the panel stays empty. Proposed workarounds all require Claude to enter plan mode and call `ExitPlanMode`.

---

## What I checked (empty)

- Full hooks reference: no `hookSpecificOutput` targets the panel.
- Settings reference: no key seeds panel state.
- GitHub plugins README: plan panel not mentioned.
- Web search: only the superpowers issue; no direct write surface.

---

## Caveats

- A PreToolUse hook could intercept Claude's own `ExitPlanMode` call and swap plan content — but only during an existing plan-mode session, not from scratch.
- Desktop app panel redesigned Apr 14 2026; undocumented internals may contain a hidden write surface, but an experienced plugin author couldn't find one (superpowers #1260, filed late Apr 2026).
- Anthropic could add a `planContent` hook output field in a future release; nothing suggests this is planned.
