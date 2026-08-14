---
name: setup
docset: B
note: >
  /setup procedure. Runs BEFORE a project is adopted, so the behaviour rules
  aren't loaded yet — this doc carries no response-shape tags and states its own
  plain-language guard.
---

# /setup procedure

You are setting up a project folder with the Throughliner method.

**This doc carries no response-shape tags** (the bracketed `[BRIEF]`-style
markers other procedure docs use). /setup runs before a project is adopted, so the
behaviour rules that define those tags aren't loaded yet — here the prose in each
step carries the behaviour directly. **Don't add tags back**; they'd be undefined
tokens in this doc.

**Plain-language guard.** Everything you say during /setup is read by a non-coder
who may be brand new to all of this. Keep internal terms out of what they see — no
hook filenames, no working-file names, no "scope-lock," "method docs," or "Case B"
labels. Say "your project's files," not "method docs"; say "I'll set this up as a
migration," not "this is Case B." This needs saying here because the
plain-language behaviour rule loads only once a project is adopted, and /setup runs
before that.

## Step 0: Is a build running right now?

Look for a file named `_build-<session-id>.md` in the project folder. That file
means a build is in progress — either in this chat or another one — and /setup
must not run alongside it.

**Say so plainly and stop.** /setup creates and rewrites a lot of the project's
files, and while a build is running the safety check refuses every write outside
that build's own list. Starting anyway would not be blocked cleanly at the door;
it would fail partway, file by file, leaving the setup half-finished. So:

> There's a build running in this project at the moment, and setting up while it
> runs would leave things half-changed. Finish it, or run /done to close it, and
> then start me again — I'll pick up from there.

Then stop. Don't begin the scaffolding, don't ask whether to continue anyway, and
don't try to work around the refusal. Making /setup runnable during a build would
mean the safety check yielding to the one command that changes the most files,
which is that guard's whole purpose inverted.

**A planning session is different — it is not refused.** There is no build file
there and nothing is blocked; writes outside the usual few files simply ask
first. What /setup owes that situation is a description rather than a refusal,
because the failure to avoid is silence, not permission. Say what is about to
happen and let the user choose:

> You've got a planning session going here. I can set up now — it'll ask before
> touching anything outside your usual files. Worth knowing that the planning
> work in this chat isn't saved yet; /done is what records it. Set up now, or
> close first?

Then wait for their answer, and do what they say.

## Step 1: Detect folder state

```
Case A  no content            the folder is empty or nearly so. Fresh start.
Case B  content, no SPEC.md   the user's own files exist but no method docs.
                              Either a true fresh start OR a MIGRATION.
Case C  already set up        SPEC.md exists.
```

**Don't assume blank-slate on Case B.** If the existing files look like planning or
spec documents, treat it as a possible migration and follow the migration framing
below. Recognise a migration **by what the docs do, not by a fixed list of old
names** — the source could be anything.

For Case C, check `.throughliner-version`:

```
version matches current plugin   ->  fully up to date. Say so in a sentence,
                                     offer /plan instead, then STOP and wait.
version missing or outdated      ->  Step 2C (migration scaffolding)
```

## Case B: pre-existing content rules

**1. Peek before Q1.** Read the pre-existing content before the first interview
question, and use what you learn to *frame* that question — never to *pre-answer*
it.

```
a clarifier INVITES the user's own answer:
    "I can see a tax brief in this folder — is that what this project is about,
     or something separate?"
pre-answering PROPOSES the answer for confirmation:
    "From the brief, this is a tax-prep project for your 2025 return — right?"
```

Ask cold and you miss context the folder already gave you; pre-answer and the spec
fills with your words instead of the user's.

**2. Leave it untouched; name it at close.** Pre-existing content is not edited,
moved, or reorganized during scaffolding — scaffolding only adds the method docs.
In the closing message, name that content explicitly as source material the user
can refer back to.

## Case B: migration framing

When the content is a migration, /setup maps it into SI's docs. The mapping is
your judgment, not a fixed table; these guardrails keep it from importing the
source's shape wholesale.

- **State SPEC's purpose first.** Before mapping anything, say plainly what SPEC.md
  is for: product truth — what the app is, who it's for, how it works, why it
  exists. **It is not a UX spec or an implementation manual.** Map the source into
  that frame; don't let the source decide what SPEC becomes.
- **Check role-fit before renaming — never blind-rename.** A source doc and the SI
  doc it seems to map to may not cover the same ground: the old one might be
  broader (a UX doc walking every screen) or narrower. If the roles don't match,
  say so plainly and let the user decide how to split or combine — don't silently
  rename one into the other.
- **Scrub the source's self-description from the content.** Renaming the file isn't
  enough — the old framing hides inside the text. A line like "this describes every
  functionality and UI element as the user experiences it" silently re-mandates the
  exhaustive detail SPEC is meant to leave out. Rewrite or drop any purpose, intro,
  or self-description sentence that re-asserts the source's role, so SPEC describes
  **the product**, not the old doc.
- **SI docs live at the project root.** No path setting, no doc-location config. If
  the source used a path block or pointed its docs elsewhere, that doesn't carry
  over.

## Step 2C: Migration scaffolding

The plugin version changed since this project was last set up. Re-scaffold without
overwriting user content. Run the checks and file creation **silently**; keep the
close to a sentence or two.

**1. Check each doc/folder** from the Step 2 scaffold list. Exists → skip. Missing
→ create from the standard scaffold (empty structure, not interview-filled).

**1a. Convert an old-format QUEUE.md.**

```
existing QUEUE.md uses an old multi-section shape
    (## Red flags · ## Batches · ### Parked · ## Deferred tests · ## Captures)
        ->  load ${CLAUDE_PLUGIN_ROOT}/docs-b/migrate-checklist.md and follow it,
            drafting the converted queue and getting approval before writing
already two-section (## Processed / ## Unprocessed)
        ->  skip
```

Showing the conversion before writing it is the general write-first test
applied, not an exception to it: a project being adopted or migrated may not be
a committed git repo, so its old queue may not be recoverable once overwritten.
The checklist states the reasoning where it is used.

This is the one project doc that reliably falls behind as the method evolves; the
checklist encodes judgment a find-and-replace can't make.

**1b. Reconcile the settings attached to the scaffold list.** Step 1 restores
missing *files*. It does not re-run the *decisions* attached to them, so a
migrated project can end up with a file and none of the setup that goes with it.
Check each, and make it so if it isn't:

```
INBOX/ present          ->  `.gitignore` carries an `INBOX/` line
.gitignore present      ->  it carries a `.throughliner/` line
```

Both are "exists → skip" cases under Step 1, which is exactly how they get
missed: an existing `.gitignore` counts as present however little it contains.

**Where the project has INBOX files already in git history, say so plainly.**
Adding an ignore line stops future commits; it does not untrack what is already
committed, and it cannot remove anything from history. Tell the user what is
there and that the line does not undo it. Don't write the line and leave the
impression the mail is now private.

**2. Retire REGISTRY.md if present.** No longer one of the method's docs, but
**don't delete it on sight** — the user may have written real notes there. Read it
first.

```
holds ONLY what the old setup put there
    (a # REGISTRY heading, the "Components that exist…" line, and either the
     empty placeholder or an auto-generated file list)
        ->  remove it quietly as part of the migration
holds anything the user clearly added
        ->  LEAVE it. Tell them plainly what's in it and ask where that content
            should live now (usually SPEC.md) before removing the file.
```

Where their own content goes is the user's call, not yours.

**3. Update `.throughliner-version`** to the current plugin version.

If the project instead carries the pre-rename marker `.si-version`, write the
new file and delete the old one — the method was called Sovereign Implementer
until epoch 3 and both marker files were named for it. Do the same for
`.si-format-epoch` in step 3a. Leaving the old file behind means every later
session reads a marker the plugin no longer writes to, so the two names drift
apart silently.

**3a. Write `.throughliner-format-epoch`** — the document-format number this migration
brings the project up to. Read it from `FORMAT_EPOCH` near the top of
`${CLAUDE_PLUGIN_ROOT}/hooks/session_start.py` and write that number, on its own,
into `.throughliner-format-epoch` at the project root.

Do this **last among the migration edits**, once the conversions above have
actually landed. It is what clears the session-start halt that sent the user
here, so writing it early would silence the warning while the project was still
on the old shape — and nothing else would ever raise it again.

**4. Skip the interview** — the project is already described in SPEC.md.

**5. Close state-aware.**

```
a leftover build working file    ->  an earlier build was interrupted: name it
    is present
                                     and recommend resuming with /next. The
                                     migration's new files get recorded when
                                     that build closes.
otherwise                        ->  tell the user what was created or updated
                                     and recommend /done
```

**Do NOT overwrite existing files.** The goal is to add what a newer plugin version
introduced, not to refresh content.

## Step 2: Scaffold the docs

Create these files (empty structure; content comes from the interview). **Don't
narrate each file as it's created** — the Step 4 close-out reports the full list.

**SPEC.md:**

````markdown
# SPEC — [Project Name]

## What this is
[filled by Q1]

## Who it's for
[filled by Q1]

## How it works
[filled by Q2]

## Project docs

Three project docs structure each project:
- `SPEC.md` — product truth. What the project is, who it's for, how it works.
- `QUEUE.md` — processed work (vetted, ready to build) and unprocessed work
  (captured ideas not yet fully processed).
- `LOG/` — per-session records of what was built, tested, and decided.

## Principles
[filled by Q3]
````

**QUEUE.md:**

````markdown
# QUEUE

## Processed

Vetted work, ready to build — worked top to bottom. Each piece of work is one
item: a `#### ` heading naming it, a `[slug]` at the end of that heading line, and
a short rationale beneath. A leading flavor tag names how it runs — none for a
build (Claude edits files), `[audit]` for a review pass, `[user]` for a step only
you can do. A security or privacy risk Claude surfaces lives here too, as a work
item carrying a `Red flag · State: cleared/uncleared` marker. The line below marks
how far down is cleared to build; anything below it is decided but not ready yet.

--- Cleared to run above this line ---

## Unprocessed

Captured ideas and tasks not yet fully processed. The next /plan session goes
through these with you and decides each one's fate — keep it (move it up to
Processed) or drop it. Each is filed as its own `#### ` heading, so the list shows
up in an editor's outline.

[filled by Q4]
````

**LOG/ folder** — create the directory with one file in it, `LOG/index.md`:

````markdown
# LOG Index

One-line summaries of each session. Newest first. Each line names the session's
full entry file in this folder.
````

Session entries are written by /done, each as its own file in LOG/ — nothing else
to scaffold.

**FAQ/ folder** — create the directory **first**, then copy the templates in (the
folder must exist before the copies, or they fail):

```
FAQ/faq.md    <-  ${CLAUDE_PLUGIN_ROOT}/templates/faq-template.md
FAQ/index.md  <-  ${CLAUDE_PLUGIN_ROOT}/templates/faq-index-template.md
```

**resources/research/ folder** — create it empty. It's the home for research notes
(`resources/research/<topic>.md`). Creating it at setup means research notes have a
place from day one rather than the folder being conjured on first use.

**INBOX/ folder** — create it empty, with an `INBOX/archive/` inside it. It's this
project's mailbox: another project you run can drop a message file in here, and
session_start surfaces anything waiting in one line. A project only ever reads its
own INBOX — it never goes looking through other projects for mail.

Add `INBOX/` to `.gitignore`, and say so in one line — that mail from other
projects stays out of the repository, and they can remove the line if they want it
committed. No question is asked.

Why it isn't asked: a message another project sends carries that project's content
into this one, and anything committed is published. A read message is *moved to
`INBOX/archive/`*, not deleted, so a mailbox that isn't ignored accumulates
another project's raw text in the repository forever — long after its useful
content has been carried into this project's queue in this project's own words.
Anything worth keeping leaves the mailbox by being processed, so the mailbox
itself is leftover comms. The safe outcome must not depend on a question being
asked, because a question is skippable.

**CLAUDE.md:**

```
no CLAUDE.md exists  ->  scaffold from
                         ${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE-TEMPLATE.md
one already exists   ->  APPEND the method block; never overwrite
```

The template carries no rendering settings — how doc-bound text is surfaced is a
default plus a session-opening offer, not a stored field (skill-nonspecific-rules.md,
view-in-doc rendering).

**.throughliner-version** — write the current plugin version (from
`${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`). session_start reads it to
detect when the plugin has been updated.

**.throughliner-format-epoch** — write the document-format number, read from `FORMAT_EPOCH`
near the top of `${CLAUDE_PLUGIN_ROOT}/hooks/session_start.py`. Separate from the
version on purpose: the version changes at every release, the format number only
when a change makes older projects' documents structurally wrong. session_start
compares the two and halts the session when the project is behind, so a project
on an old shape finds out instead of quietly running on stale scaffolding.

**.gitignore** — create it if absent, and make sure it carries an entry for
`.throughliner/` (don't duplicate one already there).

That folder holds the editing-state signal: while Claude is writing a file, the
hooks drop a small file in there saying so, so a Markdown reader or editor open
on the same document can hold off rather than the two of you typing over each
other. It is transient state about the session running right now, so it must
never be committed.

**Git repository** — if the folder isn't already one, run `git init`, silently and
mechanically like the rest of the scaffold. Without a repository there is nothing
for the close-out to commit to.

## Step 3: Interview (adaptive discovery + two settings)

The interview is an **adaptive discovery, not a fixed script.** Its job is to reach
a shared, buildable understanding — enough to fill SPEC's What / Who / How /
Principles and capture a first piece of work — by reading each answer and asking
the next question that actually matters.

**Write the project's files once discovery has covered** what the project is, who
it's for, its core, and a first thing to build. Principles and the free-form
"anything else" are optional and don't hold the writing up.

**Where a scaffolding choice is the user's — which folder to adopt, whether
existing content is a doc to leave alone, how to read an ambiguous answer — ask
before acting.** The question costs one turn; a wrong guess makes the user undo a
scaffold.

**The framing throughout is "adopt the folder":** the method is being applied to
their project, not their project reorganised to suit the method.

**Ask one question per message and stop after each.** Never bundle two questions
into one message, even short ones.

- **Use the user's own language.** Ask in their words and record their answers in
  their words, rather than rephrasing into the method's vocabulary.
- **Where an answer is vague, ask a follow-up** — subject to the stopping rule
  below, which bounds how far probing goes.
- **Read each answer, then reason about what's still unclear** before choosing the
  next question. Walk the design one branch at a time. The next question is
  generated from what's missing, not from a fixed position in a script.
- **Recommend an answer to each question.** Don't ask cold — offer a plausible
  answer the user can accept, correct, or replace ("My guess is this is for
  personal use rather than a team — is that right?"). A non-coder finds it far
  easier to react to a proposal than to fill a blank.
- **Cover these topics** — a bank to draw on, not a checklist to recite:

```
what the project is, and who it's for   ->  What this is / Who it's for
the core — the main thing it produces,  ->  How it works
    organises, or does
principles or constraints               ->  Principles
    ("must work offline", "no accounts", "everything in plain text")
the first thing to build today          ->  becomes the first work item
anything else worth knowing
```

  Skip what an earlier answer or the existing content already settled; probe deeper
  wherever the picture is thin.
- **Explore whatever already exists first.** There may be an old doc, a sketch, a
  notes file, or a running app. Use it to inform your questions rather than asking
  things the existing content already answers. Where there's genuinely nothing,
  interview from a blank slate.

**The stopping rule (the anti-overwhelm guard).** Keep probing only until the
answers bottom out into something concrete enough to build from — you're done when
the Whys are answered, not when every branch is exhausted. **Don't turn discovery
into an interrogation.** Tell the user plainly, early on, that they can end it any
time by saying **"build from what we have"**, at which point you stop asking and
write the docs from whatever's been gathered.

**The first work item** — whichever answer names the first thing to build — creates
**one rough work item** in Unprocessed: a `#### ` heading **in the user's words**,
with a kebab-case `[slug]` at the end and a "captured by you" note beneath.

**Write the heading in the user's own words, and stop there.** Their words are
the whole content of the item — anything added is Claude's scope decision wearing
the user's voice, and the tempting case is a parenthetical example drawn from
what they said, which reads as a commitment they agreed to.

Scope decisions belong in /plan, which is where this item gets processed. If
examples would clarify scope, ask a follow-up rather than smuggling them in.

**There is no settings question at all, here or anywhere.** The last one —
whether INBOX messages were committed — was dropped in favour of ignoring
`INBOX/` on both paths, because the safe outcome must not depend on a question
being asked. Discovery ends where it ends; there is no settings round after it.

The editor and working-mode questions that used to sit here are **gone**. Neither
was doing a job: the desktop app opens `.md` in its own viewer whatever editor is
named, and the location question measured how much text the user wanted pasted
rather than where they were sitting. Both are replaced by one default — point at
the doc — plus a one-line offer in the session's opening narration to paste text
inline instead.

## Step 4: Write the docs

Once discovery reaches a buildable understanding (or the user says "build from what
we have"), write the docs, then close in a sentence or two and **stop and wait**.

```
1.  fill SPEC.md from the interview answers
2.  write ONE work item in Unprocessed from the first-thing-to-build answer
    # the user's words, a [slug] at its end, a "captured by you" note.
    # Not multiple scoped entries.
3.  show the user what was created (file list + one line each)
4.  recommend /done to record this setup and commit the new files
5.  teach the working rhythm (below)
```

The file list shows what appeared in the folder; the session's single summary is
the LOG entry /done writes at close.

**Teach the working rhythm in plain words** — a few short sentences:

- **/setup** you've now run once; you won't run it again for this project.
- From here, two commands carry the work: **/plan** to think and organise, and
  **/next** to build the next thing on the list. Run /plan whenever planning is
  needed, and /next once per item as you work down the queue.
- However a session goes, end it the same way: **/done** to record what happened,
  then **/clear** to start fresh. The habit that matters: **always /done before
  /clear**, so each session is saved before the context resets.

