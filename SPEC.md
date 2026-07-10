# SPEC — Sovereign Implementer

## What this is

A Claude Code plugin for non-coders. It gives users a structured workflow for building apps with Claude Code without needing to know how to code.

## Who it's for

Non-coders who know what their app should do but need a framework to keep Claude aligned.

## How it works

Splits changes into a build queue that helps the user harness Claude's skills in dependency management, not just coding. The secondary core functionality is basic context window management.

Five skills drive the workflow:
- `/setup` — scaffold project docs and run the onboarding interview.
- `/plan` — manage the queue, add ideas, resolve questions, check for drift.
- `/next` — pick the top queue entry and execute it. A freeform form (`/next freeform`) runs unqueued work — discussion-first sessions, ad-hoc audits, wrapping up changes made by hand — under the same scope and capture discipline.
- `/cruise` — the autonomous multi-line runner: works the cleared queue top-down, build → commit → build → commit, without stopping to confirm each line, and finishes at the readiness line. The "do many" version of /next (see Cruise control below).
- `/done` — close the build, record what happened, commit.

Three project docs structure each project:
- `SPEC.md` — product truth. What the app is, who it's for, how it works.
- `QUEUE.md` — processed and unprocessed work. Processed work is vetted and ready to build; unprocessed work is captured ideas and tasks not yet discussed. One line per piece of work.
- `LOG/` — per-session records of what was built, tested, and decided.

Two hooks enforce discipline mechanically, and a third advises:
- `session_start` — detect project state and load behaviour rules.
- `pre_tool_use` — enforces the scope-lock (which governs SPEC.md like any other file) and git safety, and asks for your approval before Claude spawns a subagent (a cost guard that asks, never blocks).
- `post_tool_use` — advisory QUEUE.md structure lint; flags format drift, never blocks.

One behaviour doc steers everything the hooks can't enforce:
- `plugin-behaviour.md` — loaded at every session start in adopted projects. Carries the cross-skill rules (communication, capture routing, dependency ownership, file safety) and five response-shape tags ([SILENT], [BRIEF], [DISCUSS], [PROMPT], [SEQUENCE]) that procedure docs place on individual steps to control verbosity and interaction. Rule and tag definitions are compliance-hardened: each carries a why-clause, quantified constraints, and an explicit scope statement so it holds against the helpfulness pull of current models.

One output style sets the communication default at system-prompt priority:
- A concise output style — shipped in the plugin and applied automatically when SI is enabled. It lifts the plugin's communication structure (lead with the decision, one item at a time, gate detail) to system-prompt priority, the level that holds when lower-priority instructions are skipped. It steers structure and plain English, not terseness — the goal is to not overwhelm the non-coder who reads and approves everything, never to cap length.

**Readiness line.** /plan maintains a line in the queue — rendered `--- Cleared to run above this line ---` — that marks which work is vetted and safe to build (above it) from work that still needs planning (below it). /plan positions it at every close and narrates where it sits whenever the line moves — confirming silently when its placement is unchanged — so the user never has to work out by hand how much of the queue is safe to run next without being told the same boundary twice. Cruise control inherits it as its run bound — a clean finish at the line rather than running into unvetted work.

**Cruise control.** `/cruise` is the autonomous multi-line runner — the "do many" version of /next. Invoked when the user wants several cleared pieces of work built back-to-back without confirming each one, it works the cleared region of the queue top-down, building each line scope-locked and closing it to its own commit (build → commit → build → commit), so an interrupted run loses nothing. It reuses the same per-line build and close machinery /next and /done use; what it adds is the loop plus the autonomy needed to run unattended: a **red-flags gate** (any open risk blocks the run — only resolved or accepted flags let it proceed, and a risk raised mid-run halts it), a **response spine** (routine discoveries and user-run checks are filed and the run continues; only a genuine blocker — an open red flag, a needed SPEC change, or a decision only the user can make — halts it), and **hard-stops** (an iteration ceiling, no-progress detection, and a per-run budget ceiling that bound a runaway run). It finishes cleanly at the readiness line, and its per-line close never offers an outward push — a cruise run publishes nothing. This is the unattended build mode the Principles name.

**Keeping projects current.** The plugin keeps improving while projects sit set up, so a project can fall behind what the current method scaffolds. At the start of a working session, before /plan or /next, `session_start` catches this two ways: it flags whole docs or folders the project is missing (offering /setup to add them), and it tops up an existing doc that's missing a newer *setting* the method has since added. The top-up is add-only — it never rewrites or clobbers anything the user has written; where a setting needs an answer (like which editor they work in), Claude opens with a one-line question and writes the answer, and settings needing no answer are added silently with a note. The missing-setting check is a list, so new settings join it over time. The riskier case — reconciling content whose template wording changed — is deliberately out of scope for now.

## Principles

- Never restrict ideation, just direct it. The user must be able to ideate at any point in the build cycle.
- Hooks enforce what must never happen; hardened rules and tags steer what should usually happen. Mechanical enforcement is cheap and unskippable; behavioural steering is written to survive priority conflicts on the models users actually run.
- Execution sessions trend toward pure execution. Ideas and discoveries can be captured anywhere, but deciding their fate is planning work and happens in planning sessions. This end state is realized as cruise control (`/cruise`) — an unattended build mode that works the cleared queue, stopping only for what genuinely needs the user.
- Surface risk in plain language; never bury it. Claude screens for data-exposure and breach risks and flags them where the user can't miss them. It doesn't silently ship past a security concern, and it doesn't let a risk be accepted without a recorded, informed choice.
- Readable output is a control requirement, not a style preference. The user keeps Claude aligned by reading and approving what it does, so output too long to get through breaks that control — an error the user can't read past is one they can't catch. "Be thorough" means surfacing every important thing the user must see and act on, never emitting every word: lead with the decision, then stop; gate detail behind an explicit request. This is anti-overwhelm, not terseness — the levers are sequencing and leading with the decision, never a word-count cap, and plain English for the non-coder is the standard the concision serves, not a cost it trades away.