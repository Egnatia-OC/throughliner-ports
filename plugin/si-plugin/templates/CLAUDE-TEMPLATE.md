# CLAUDE.md

<!-- ▼ PLUGIN-MANAGED — do not edit between these markers. Updated on /setup and plugin reinstall. ▼ -->

This project uses the Sovereign Implementer method.

## Project docs

- **SPEC.md** — product truth. What it is, who it's for, how it works.
- **QUEUE.md** — your work, in two sections. **Processed** work is vetted and ready to build, worked top-to-bottom; a `--- Cleared to run above this line ---` line marks how far down is greenlit (below it is decided but not ready yet). **Unprocessed** work is captured ideas and tasks not yet fully processed. Each piece of work is one line: a `#### ` heading naming the work, with a `[slug]` at the end of that heading line and a short rationale beneath it, plus a `captured by you` credit on items you personally raised (anything else is unmarked — Claude is the default author). A work item can carry a leading flavor tag: none means a build (Claude edits files), `[audit]` a review pass (Claude reads and reports), `[user]` a step only you can run. A security or privacy risk Claude surfaces becomes a work item carrying a `Red flag · State: cleared/uncleared` marker — surfaced first each session while uncleared, until it's cleared (either designed out, or you're told the risk plainly and choose to accept it).
- **LOG/** — session records: what was built, tested, decided. One file per session entry, plus index.md one-line summaries naming each entry file.
- **FAQ/** — workflow FAQ. Index loaded at session start; details in FAQ/faq.md.

## Workflow

- `/setup` — scaffold project docs (done if you're reading this).
- `/plan` — queue management, captures, design questions.
- `/next` — execute the top piece of ready work (a build or an audit, by its flavor tag). It can work several cleared pieces of work back-to-back, top-down, stopping at the readiness line or when something genuinely needs you.
- `/done` — record, update docs, commit.

## Rules for Claude

- SPEC.md is a normal doc — it changes during planning or a build, always with your approval, and there's no separate spec-edit step. A planning decision that changes what SPEC says edits SPEC in that /plan session; a build that needs a SPEC change asks you and adds SPEC.md to its file list. The safety check still blocks a build from editing SPEC unless that build lists it in its files, so a spec change never rides in silently. Note spec issues for /plan as they come up.
- Only touch files listed in the active build scope. Halt and ask if you need more.
- One build at a time. Never start a second build while _build.md exists — finish and /done before starting another. (A planning session in a separate chat alongside a build is allowed.)
- State problems plainly. Don't hide them or silently fix unrelated things.
- Route discoveries to QUEUE.md's Unprocessed section rather than acting on them immediately — a later /plan decides their fate.

## Language

Language: English

## Editor

Editor: not recorded

<!-- The `.md` editor you work in, from the optional /setup question. When it names an editor, Claude points you to your open docs with a link instead of re-pasting their text into chat, saving tokens. Left as `not recorded` if you skipped the question — Claude then quotes the text inline as usual. -->

## Working mode

Working mode: local

<!-- Where you work from, set at /setup. `local` = at your desktop, where an edited file opens instantly, so Claude points you to text in your docs with a link. `remote` = driving Claude from your phone, where opening an edited file is awkward, so Claude pastes the text straight into chat instead. Flip it for one session just by telling Claude ("I'm remote today"); it reverts next session. -->

<!-- ▲ PLUGIN-MANAGED — do not edit above this line. ▲ -->

## Project rules

<!-- Add your own rules, conventions, and context below. This section is yours — the plugin won't touch it.
     If your project has specific test procedures (how to run tests, what to check, environment setup),
     add them here or point to where they live — Claude will follow them during test entries and /done verification. -->
