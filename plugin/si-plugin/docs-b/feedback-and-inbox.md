---
name: feedback-and-inbox
docset: B
note: >
  Fetched on demand from plugin-behaviour.md's pointers. Full procedures for
  the consumer feedback channel and the cross-project INBOX. The always-loaded
  rules keep only the discriminator and the never-send-unseen guarantee.
---

# Feedback channel and cross-project INBOX — full procedures

## Consumer feedback channel

A problem with the *method itself* (a skill misbehaving, a hook misfiring, a
rule producing a bad outcome) or with **Claude Code itself** is not work on the
user's app; each routes to its own destination. Never use Claude Code's
built-in `/bug` for a method problem — that reports Claude Code problems to
Anthropic, not third-party plugin issues to this plugin's author.

```
the discriminator:  which thing is misbehaving?
    my app       ->  an ordinary capture in my QUEUE
    the method   ->  flintcraft.tech/report
    Claude Code  ->  a GitHub issue on anthropics/claude-code
        (the harness: the app itself, its viewer, links,
         hooks machinery, sidebar — not this plugin's rules)
    unsure       ->  ask the user; don't guess between the three
```

```
user-raised     ->  always fine to draft a report
Claude-noticed  ->  offer ONCE. Drop it if they decline.
```

### The method report (flintcraft.tech/report)

- **One free-form block, not labelled fields** — the report page is a single
  text box. The block carries, as prose: what the plugin did versus what was
  expected, which skill and step, the method version, and generic repro steps.
- **Scrubbed by construction.** Include no app names, file contents, secrets,
  QUEUE/SPEC content, or project specifics beyond describing the issue. A
  report is *about* sensitive content more often than it contains some —
  describe the sensitivity ("a project name that shouldn't appear on a shared
  screen") without demonstrating it.
- **Claude drafts, the user sends.** Show the paste-ready block; the user
  reviews and pastes it themselves. The web form is the user's to submit, and
  their review is the required backstop on the scrubbing.
- **Red flag territory:** a submitted report can become a public GitHub issue
  downstream, so a leak of app details or secrets into one is a privacy breach.

### The Claude Code report (GitHub issue)

- **Offer to file it directly** when `gh` is installed and authenticated:
  draft the issue, show the exact text, post only on an explicit yes. When
  `gh` is absent or unauthenticated, draft text for the user to paste on
  GitHub themselves — the offer never just fails.
- **Approval-before-post is non-negotiable.** A GitHub issue is public and
  permanent under the user's identity. Show the full text; post on an explicit
  yes.
- **Duplicate-check first — it shapes the report.** Search existing issues
  before drafting; a match may turn the report into a strengthening comment
  plus a smaller new issue for the genuinely novel half.
- Apply the same scrub-by-construction standard as the method report.

**The two posting rules differ deliberately.** The method report is pasted by
the user because the report page is a web form Claude can't submit. The Claude
Code report is posted by Claude, after explicit approval, because `gh` can
post it and a non-coder shouldn't be sent to a GitHub form. Both keep the same
guarantee — nothing leaves without the user seeing the exact text and saying
yes — and only the mechanics differ.

## Cross-project INBOX

Each project has an `INBOX/` folder, scaffolded at /setup. It's how two
projects the same user runs send each other messages directly, instead of the
user carrying them between chats by hand.

**Inbound.** session_start surfaces what's waiting, in one line. Opening a
message routes it through the three-way triage in the behaviour rules — work
to do becomes a capture in Unprocessed, a finding goes to the LOG, evidence to
re-read goes under `resources/`. Then move the file to `INBOX/archive/`, so it
isn't surfaced again every session. A project reads only its own INBOX; it
never goes looking through other projects for mail.

**Outbound — never auto-send.** A message is written straight into the
recipient project's `INBOX/`, but only after the user has seen the exact
wording and approved it. Sending is outward-facing and both mailboxes may sit
in repositories that get published, so draft, show, wait — the same guarantee
the feedback reports keep.

Not to be confused with the editing-state signal: `.throughliner/` markers are
live session state a companion app reads. INBOX is for messages. They stay
separate.
