# SPEC — Sovereign Implementer

## What this is

A Claude Code plugin for non-coders. It gives users a structured workflow for building apps with Claude Code without needing to know how to code.

## Who it's for

Non-coders who know what their app should do but need a framework to keep Claude aligned.

## How it works

Splits changes into a build queue that helps the user harness Claude's skills in dependency management, not just coding. The secondary core functionality is basic context window management.

Four skills drive the workflow:
- `/setup` — scaffold project docs and run the onboarding interview.
- `/plan` — manage the queue, add ideas, resolve questions, check for drift.
- `/next` — pick the top queue entry and execute it. A freeform form (`/next freeform`) runs unqueued work — discussion-first sessions, ad-hoc audits, wrapping up changes made by hand — under the same scope and capture discipline.
- `/done` — close the build, record what happened, commit.

Four project docs structure each project:
- `SPEC.md` — product truth. What the app is, who it's for, how it works.
- `QUEUE.md` — work batches, captured ideas, and red flags (security, privacy, and breach risks Claude has surfaced).
- `REGISTRY.md` — components list. What exists, where it lives.
- `LOG/` — per-session records of what was built, tested, and decided.

Two hooks enforce discipline mechanically, and a third advises:
- `session_start` — detect project state and load behaviour rules.
- `pre_tool_use` — SPEC.md read-only during builds, scope-lock to file list, git safety.
- `post_tool_use` — advisory QUEUE.md structure lint; flags format drift, never blocks.

One behaviour doc steers everything the hooks can't enforce:
- `plugin-behaviour.md` — loaded at every session start in adopted projects. Carries the cross-skill rules (communication, capture routing, dependency ownership, file safety) and five response-shape tags ([SILENT], [BRIEF], [DISCUSS], [PROMPT], [SEQUENCE]) that procedure docs place on individual steps to control verbosity and interaction. Rule and tag definitions are compliance-hardened: each carries a why-clause, quantified constraints, and an explicit scope statement so it holds against the helpfulness pull of current models.

One output style sets the communication default at system-prompt priority:
- A concise output style — shipped in the plugin and applied automatically when SI is enabled. It lifts the plugin's communication structure (lead with the decision, one item at a time, gate detail) to system-prompt priority, the level that holds when lower-priority instructions are skipped. It steers structure and plain English, not terseness — the goal is to not overwhelm the non-coder who reads and approves everything, never to cap length.

**Red flags.** Claude watches for anything that could expose the user's data or their users' data, or amount to a breach, and surfaces it as a red flag instead of quietly building past it. Red flags collect in a section at the top of QUEUE.md, so they're the first thing seen each session. Each flag carries a state — open, resolved, or accepted. An accepted flag records the user's decision in the LOG: what they were warned about, and that they chose to proceed anyway. Open flags are meant to gate the unattended build mode — a user who leaves a risk unaddressed stays on hand to approve each step rather than letting the build run on its own.

## Principles

- Never restrict ideation, just direct it. The user must be able to ideate at any point in the build cycle.
- Hooks enforce what must never happen; hardened rules and tags steer what should usually happen. Mechanical enforcement is cheap and unskippable; behavioural steering is written to survive priority conflicts on the models users actually run.
- Execution sessions trend toward pure execution. Ideas and discoveries can be captured anywhere, but deciding their fate is planning work and happens in planning sessions. The end state is an unattended build mode that works through the queue, stopping only for what genuinely needs the user.
- Surface risk in plain language; never bury it. Claude screens for data-exposure and breach risks and flags them where the user can't miss them. It doesn't silently ship past a security concern, and it doesn't let a risk be accepted without a recorded, informed choice.
- Readable output is a control requirement, not a style preference. The user keeps Claude aligned by reading and approving what it does, so output too long to get through breaks that control — an error the user can't read past is one they can't catch. "Be thorough" means surfacing every important thing the user must see and act on, never emitting every word: lead with the decision, then stop; gate detail behind an explicit request. This is anti-overwhelm, not terseness — the levers are sequencing and leading with the decision, never a word-count cap, and plain English for the non-coder is the standard the concision serves, not a cost it trades away.