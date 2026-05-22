# V51 — Research folder convention + Sonnet-search reword

> **Promoted from OPEN-QUESTIONS in session v47 (2026-05-22).**

## Goal

Two changes that address the same gap — the method currently tells the agent to "prompt the user to do a Sonnet search" (a Cowork-era workaround) and has no designated home for research findings:

1. **Research folder.** `/setup` scaffolds an empty `research/` folder at project root. When the agent hits uncertainty sufficient to research, it researches and writes findings to `research/<topic>.md` automatically — no user prompt needed, no size threshold. Research files are reference material: no MANIFEST tracking, no BACKLOG entries. Zero maintenance burden.

2. **Sonnet-search reword.** Replace "prompt the user to do a Sonnet search" language across method docs with "offer to conduct research on anything you're uncertain of" — shifting responsibility from user to agent. Claude Code has built-in web search; the agent should research directly.

## Inputs

- OPEN-QUESTIONS entry: "`research/` folder convention + automatic research persistence"
- `plugin/hooks/universal-behaviour.md` — contains the Sonnet-search language to reword
- All subagent bodies under `plugin/agents/` — any that reference Sonnet search or external research
- `Crash course.md` — Sonnet-search mentions
- `plugin/agents/setup.md` — `/setup` scaffolding logic; gains `research/` folder
- `plugin/scripts/scaffold.py` — if scaffolding is scripted
- This dev project's own `research/` folder — proven pattern to reference

## Outputs

- `/setup` scaffolds `research/` folder at project root (adopt subagent + scaffold script updated)
- Sonnet-search language reworded across universal-behaviour, all subagent bodies, Crash course
- `plugin/docs/DOC-STRUCTURE.md` updated — `research/` folder described as reference material, not a spine doc
- `plugin/docs/VOCABULARY.md` updated — "research file" defined
- OPEN-QUESTIONS entry removed
- All plugin-side method-version footers bumped

## Success criteria

- `/setup` on a fresh project creates a `research/` folder
- No remaining "Sonnet search" or "prompt the user to search" language in any plugin-side doc or subagent body
- Research files written by the agent during a build session land in `research/` without user prompting
- Build log entries can reference research files rather than embedding findings inline
- Smoke-testable in a desktop-app burner session with the plugin installed via local marketplace: run `/setup` on a scratch folder; verify `research/` exists; trigger a research-worthy question during planning; verify the agent writes to `research/`

## Open questions for this session

- **Research file naming convention.** `<topic>.md` (free-form, as in this dev project) or date-prefixed `YYYY-MM-DD-<topic>.md`? Leaning: free-form — dates add clutter and the file's own content carries the date context.
- **Should the agent announce when it's writing research?** Silent write (agent just does it) or a brief mention ("I'm saving these findings to `research/marketplace-options.md` for future reference")? Leaning: brief mention — aligns with "no stealth fixes" / transparency ethos.
- **Build-batch `Inputs:` line integration.** V45 ships the `Inputs:` line. Research files are the natural thing to list there. Should this session add guidance for referencing research files in `Inputs:`, or leave that to emerge naturally? Leaning: add one line to DOC-STRUCTURE explaining that research files are valid Inputs-line entries.

## Risks / dependencies

- **No hard dependencies.** Could ship in any order relative to V45–V50. Placed after V50 to avoid renumber churn.
- **Reword sweep surface.** Sonnet-search language may appear in more places than expected. Grep thoroughly before starting the rewrite.
- **Agent behaviour change.** Shifting from "prompt user to search" to "research directly" is a behavioural change, not just a language change. The universal-behaviour rule and subagent bodies must be clear enough that Claude actually does the research rather than asking permission.
