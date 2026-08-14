---
name: feedback-and-inbox
docset: B
note: >
  Fetched on demand from skill-nonspecific-rules.md's pointers. Full procedures for
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

**When mail is opened.** Any session may open it whenever the user asks —
opening and routing is filing, and filing is open to every session. There are
two *guaranteed* moments: **/plan's Step 1 read-state**, before the session
skims and orders its queue, and **/next's pre-flight**, before the run is
presented. Without a guaranteed moment, mail was surfaced every session and
could be opened in none of them.

At /next the read is deliberately partial — open, file, and defer. Anything a
message raises becomes a capture; where it bears on an item in the cleared
region, /next names it and recommends dropping that item from **that run only**,
leaving the queue untouched. Deciding an item's fate stays /plan's.

Once routed, a message's contents are ordinary captures and rank by the existing
ladder. There is no priority rung for mail — the missing piece was the opening,
not the ranking.

**Mail arriving mid-session waits for the next session start.** The mailbox is
scanned at session start only. That bound is stated rather than engineered
around, matching the INBOX design's existing promise that delivery is not
guaranteed.

**Outbound — never auto-send.** A message is written straight into the
recipient project's `INBOX/`, but only after the user has seen the exact
wording and approved it. Sending is outward-facing and both mailboxes may sit
in repositories that get published, so draft, show, wait — the same guarantee
the feedback reports keep.

**Name the sending project twice: in the message's filename, and in its opening
line.** The filename carries it as `<date>-from-<sending project>-<subject>.md`;
the body opens by saying which project is writing.

```
INBOX/2026-08-14-from-hexboard-trailing-slash-command.md

    # <subject>
    From <sending project>, running Throughliner <version>.
```

Both, because they fail differently. The filename is readable without opening
anything, which is what makes a mailbox triageable — and it is the half any
move, archive or rename can drop. The body line survives every rename and is
invisible until the message is opened. Written at the send, which is the only
moment the sender is known for certain: a receiving-side check can see the field
is missing and can never recover it. One message arrived without either, and
identifying who sent it took five checks and a screenshot before it was settled.

**Check the recipient's `INBOX/` exists before writing, and say plainly when one
has to be created.** A project whose installed method predates INBOX scaffolding
has nothing at its session start that surfaces waiting mail, so a message
delivered into a folder this project just made can sit unread indefinitely with
nothing on this side ever knowing. That has happened.

**And confirm the recipient's `INBOX/` is covered by that project's
`.gitignore`. Where it is not, say so plainly and do not send until the user
says go.** One more limb on the check that already runs, not a new mechanism.
A reply is written into the recipient's own folder, so a file from this project
appears inside a repository whose ignore rules this project does not control —
and where those rules do not cover the mailbox, the message gets committed
there. Sending with a warning instead was rejected: a warning at the moment of
sending is the kind that gets clicked past, and the cost of being wrong lands in
a repository neither party can see.

**What sending guarantees, stated honestly because it is easy to assume more.**
It places a file in the recipient's mailbox. Nothing confirms it was read. A
completed round trip has happened — a message was read, answered, and a factual
error corrected at its source — but that worked because the other project
happened to read its mailbox and chose to reply. A good outcome, not a
guarantee, and the docs must not let it read as one.

An automatic read-receipt written back into the sender's mailbox is **rejected,
not merely unbuilt.** Nothing leaves the machine without the user seeing the
exact text and giving an explicit yes, and that rule names outbound INBOX
messages. A receipt is an automatic send: it would either break that guarantee
or stop to ask the user to approve a receipt for a message they never wrote.

**The address book — `INBOX/.address-book.md`, correspondent name to absolute
folder path.** Outbound needs a filesystem path and inbound needs none, so every
reply used to be a fresh lookup the user performed by hand, however long the
correspondence had run: a reply once stalled after four exchanges because
nothing anywhere recorded where the other project was. Write an entry the first
time the user supplies a path, so the cost is paid once per correspondent
instead of once per reply.

```
lives INSIDE INBOX/    ->  `.gitignore` ignores that folder and everything
                           beneath it, so the file is never committed. This is
                           load-bearing: the entries are absolute paths that
                           identify a person, and a later change moving the
                           file BESIDE INBOX/ loses the protection silently.
records what the user  ->  never a filesystem scan for other projects. The
    gave                   standing rule is to work on the folder the session
                           opened in and never go looking for others.
```

Putting the sender's path inside the message instead was rejected on the same
ground: that writes a path from this machine into another project's repository,
which may be committed and may be public.

**The address book is write-and-send only.** A session may pass a recorded path
to a send. It may never quote the path, never name a correspondent in any
document, and never carry either into chat. Some projects are private in a way
that goes past "not published" — the folder name alone can identify a real
person and a sensitive matter — and the gitignore protects against publication
and nothing else. The exposure this closes is a session reading the address book
and copying a name into QUEUE.md or a LOG entry, which are committed.

Not to be confused with the editing-state signal: `.throughliner/` markers are
live session state a companion app reads. INBOX is for messages. They stay
separate.
