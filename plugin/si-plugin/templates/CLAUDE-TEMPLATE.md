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

## Model

Model: not recorded

<!-- Which Claude model you mostly run, from the optional /setup question. Claude follows instructions better when they're written for the model actually running, so the plugin keeps two sets of its own working instructions and uses this to pick. Left as `not recorded` if you skipped — the safe default is used. Change it by telling Claude. -->

## Repo visibility

Repo visibility: not checked

<!-- Whether this project's code repository is public or private. Detected at /setup rather than asked, because an answer typed once goes out of date without anyone noticing. It matters because a public repo means anything written into these docs is readable by anyone, permanently — so Claude holds a firmer line about never writing other people's names or private details into them. If it was recorded from your answer rather than detected, that's noted here. -->
<!-- If this repo's visibility changes, tell Claude so this gets re-checked. -->

<!-- ▲ PLUGIN-MANAGED — do not edit above this line. ▲ -->

## Project rules

<!-- Add your own rules, conventions, and context below. This section is yours — the plugin won't touch it.
     If your project has specific test procedures (how to run tests, what to check, environment setup),
     add them here or point to where they live — Claude will follow them during test entries and /done verification.

     If you regularly write things about this project for people outside it — posts to a community,
     a newsletter, updates to a client — Claude may offer to add a short section here recording:
       - where that work goes (the audience, the channel)
       - whether its full text is kept in the log, or only a description and a pointer to it
       - what later draws on it (release notes, a changelog, the next update)
     That's so it isn't re-decided every session. The offer is optional and declining it is fine. -->
