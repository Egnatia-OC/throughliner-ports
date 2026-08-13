# CLAUDE.md

<!-- ▼ PLUGIN-MANAGED — do not edit between these markers. Updated on /setup and plugin reinstall. ▼ -->

This project uses the Throughliner method.

## Project docs

- **SPEC.md** — product truth. What it is, who it's for, how it works.
- **QUEUE.md** — your work, in two sections. **Processed** work is vetted and ready to build, worked top-to-bottom; a `--- Cleared to run above this line ---` line marks how far down is greenlit (below it is decided but not ready yet). **Unprocessed** work is captured ideas and tasks not yet fully processed. Each piece of work is one line: a `#### ` heading naming the work, with a `[slug]` at the end of that heading line and a short rationale beneath it, plus a `captured by you` credit on items you personally raised (anything else is unmarked — Claude is the default author). A work item can carry a leading flavor tag: none means a build (Claude edits files), `[audit]` a review pass (Claude reads and reports), `[user]` a step only you can run. A security or privacy risk Claude surfaces becomes a work item carrying a `Red flag · State: cleared/uncleared` marker — surfaced first each session while uncleared, until it's cleared (either designed out, or you're told the risk plainly and choose to accept it).
- **LOG/** — session records: what was built, tested, decided. One file per session entry, plus index.md one-line summaries naming each entry file.
- **FAQ/** — workflow FAQ. Index loaded at session start; details in FAQ/faq.md.
- **INBOX/** — messages from other projects you run. Anything waiting is mentioned at session start; handled messages move to `INBOX/archive/`. A message going out to another project is always shown to you for approval first.

## Workflow

- `/setup` — scaffold project docs (done if you're reading this).
- `/plan` — queue management, captures, design questions.
- `/next` — execute the top piece of ready work (a build or an audit, by its flavor tag). It can work several cleared pieces of work back-to-back, top-down, stopping at the readiness line or when something genuinely needs you.
- `/done` — record, update docs, commit.

## Rules for Claude

- SPEC.md is a normal doc — it changes during planning or a build, always with your approval, and there's no separate spec-edit step. A planning decision that changes what SPEC says edits SPEC in that /plan session; a build that needs a SPEC change asks you and adds SPEC.md to its file list. The safety check still blocks a build from editing SPEC unless that build lists it in its files, so a spec change never rides in silently. Note spec issues for /plan as they come up.

## Language

Language: English

<!-- ▲ PLUGIN-MANAGED — do not edit above this line. ▲ -->

## Project rules

<!-- Add your own rules, conventions, and context below. This section is yours — the plugin won't touch it.
     If your project has specific ways of checking that things work — how to run its tests, what to look at,
     any setup needed first — add them here or point to where they live. Claude follows them as part of
     building, and where a check is one only you can make, it becomes a step in your queue for you to run. -->
