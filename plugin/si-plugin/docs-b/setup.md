---
name: setup
docset: B
note: >
  /setup procedure. Runs BEFORE a project is adopted, so the behaviour rules
  aren't loaded yet — this doc carries no response-shape tags and states its own
  plain-language guard.
---

# /setup procedure

You are setting up a project folder with the Sovereign Implementer method.

**This doc carries no response-shape tags** (the bracketed `[BRIEF]`-style
markers other procedure docs use). /setup runs before a project is adopted, so the
behaviour rules that define those tags aren't loaded yet — here the prose in each
step carries the behaviour directly. **Don't add tags back**; they'd be undefined
tokens in this doc.

**Plain-language guard.** Everything you say during /setup is read by a non-coder
who may be brand new to all of this. Keep internal terms out of what they see — no
hook filenames, no `_build.md`, no "scope-lock," "method docs," or "Case B"
labels. Say "your project's files," not "method docs"; say "I'll set this up as a
migration," not "this is Case B." This needs saying here because the
plain-language behaviour rule loads only once a project is adopted, and /setup runs
before that.

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

For Case C, check `.si-version`:

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
        ->  load ${CLAUDE_PLUGIN_ROOT}/docs/migrate-checklist.md and follow it,
            drafting the converted queue and getting approval before writing
already two-section (## Processed / ## Unprocessed)
        ->  skip
```

This is the one project doc that reliably falls behind as the method evolves; the
checklist encodes judgment a find-and-replace can't make.

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

**3. Update `.si-version`** to the current plugin version.

**4. Skip the interview** — the project is already described in SPEC.md.

**5. Close state-aware.**

```
a leftover _build.md is present  ->  an earlier build was interrupted: name it
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

**CLAUDE.md:**

```
no CLAUDE.md exists  ->  scaffold from
                         ${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE-TEMPLATE.md
one already exists   ->  APPEND the method block; never overwrite
```

The template carries an Editor field (`not recorded`), a Working mode field
(default `local`), a Model field, and a Repo visibility field; Step 4 fills them
from Q6, Q7, Q8 and the visibility detection.

**.si-version** — write the current plugin version (from
`${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`). session_start reads it to
detect when the plugin has been updated.

**Git repository** — if the folder isn't already one, run `git init`, silently and
mechanically like the rest of the scaffold. Without a repository there is nothing
for the close-out to commit to.

## Step 3: Interview (adaptive discovery + three settings)

The interview is an **adaptive discovery, not a fixed script.** Its job is to reach
a shared, buildable understanding — enough to fill SPEC's What / Who / How /
Principles and capture a first piece of work — by reading each answer and asking
the next question that actually matters.

**Ask one question per message and stop after each.** Never bundle two questions
into one message, even short ones.

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

```
verbatim user words     ->  yes
expansion               ->  no
illustrative examples   ->  no
parentheticals drawn    ->  no  # even parenthetical examples read as
from visible context            commitments the user agreed to
```

Scope decisions belong in /plan, which is where this item gets processed. If
examples would clarify scope, ask a follow-up rather than smuggling them in.

**The three settings questions are fixed, not adaptive** — they're project
settings, not discovery. Ask them the same way each time, one message each, after
discovery reaches its stopping point. All optional; the user can skip any.

**Q6 (optional). If you wanted to change something in one of these project docs
yourself, what would you open it in?**
→ Records the app you'd edit in. Claude's links open the file in Claude's own
viewer, which shows the text but won't let you change it — so this is only about
where you'd go to make an edit by hand. **Plenty of people never do, so skipping
this is completely normal** — say skip and nothing else changes: you still get
links, and Claude still does the writing. Named editor → record it; skipped →
write `not recorded` so the field is present but empty. Asked once, no nag.

**Q7 (optional). Will you usually be working from your computer, or driving Claude
from your phone?**
→ Sets your working mode. **local** = you're at your desktop, where an edited file
opens instantly, so Claude points you to text with a link. **remote** = you're on
your phone, where opening a file is awkward, so Claude pastes the text into chat.
Defaults to **local**. Switch anytime by telling Claude ("I'm remote today") — it
holds for that session and reverts. Asked once, no nag.

**Q8 (optional). Which Claude model do you mostly run — the newest generation, or
an older one?**
→ Claude works better with instructions written for the model actually running, so
the plugin keeps two sets and picks the one that fits. Name the current models
plainly and let the user pick; if they don't know or skip, say the safe default is
assumed and move on. Record the answer, not a preference about the plugin's
internals — the user should never meet the word for those two sets. Asked once, no
nag.

## Step 3b: Repo visibility, licensing, and publishing

Three things, in this order. The first is a **safety input**, not a preference,
and it applies to every project including one with no interest in publishing.

**1. Detect whether the repo is public — don't ask.** A recorded answer to this
goes stale silently, and silently is exactly how it hurts: one project's
visibility was set long ago and nobody knew what it was until it was checked
mid-session, six weeks into a live exposure. Detection costs one command and is
never out of date.

```
GitHub remote + gh available  ->  detect it (`gh repo view`), record what you found
no remote / no gh / not       ->  ask the user once, and record the answer AS a
GitHub                            stated fallback, marked as such
```

Record it in CLAUDE.md. What consumes it: the write-time rule about other people's
private information (plugin-behaviour.md) — a public repo makes that urgent rather
than theoretical, and a private one can be shared or made public later without
anything re-checking.

**2. Ask about the licence** [PROMPT] — in plain terms: does the user want others
free to use and build on this, or do they want to keep it to themselves? Write
their answer as a LICENSE file. Recommend one rather than asking cold.

**3. Offer public-repo setup, framed off the licence** [PROMPT] — "since you chose
this licence, would you like this on your GitHub? We can do it now, or note it for
a later planning session." **Offer, never push.** The note-it-for-later branch is
the graceful decline, and it's a real option, not a formality.

For a user who wants the most private posture available, offer to add every
project doc to `.gitignore` so none of it is ever committed.

## Step 4: Write the docs

Once discovery reaches a buildable understanding (or the user says "build from what
we have"), write the docs, then close in a sentence or two and **stop and wait**.

```
1.  fill SPEC.md from the interview answers
2.  write ONE work item in Unprocessed from the first-thing-to-build answer
    # the user's words, a [slug] at its end, a "captured by you" note.
    # Not multiple scoped entries.
2a. fill CLAUDE.md's Editor field from Q6         (or `not recorded`)
2b. fill CLAUDE.md's Working mode field from Q7   (or `local`)
2c. fill CLAUDE.md's Model field from Q8            (or leave the safe default)
2d. fill CLAUDE.md's Repo visibility field from the detection (or the stated
    fallback answer, marked as user-stated)
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

## Rules

- **One question per message. Do not bundle.**
- **Use the user's language** — don't rephrase into jargon.
- If an answer is vague, ask a follow-up — but honour the stopping rule and don't
  interrogate.
- **Don't create files until discovery has covered** what the project is, who it's
  for, its core, and a first thing to build. Principles and the free-form "anything
  else" are optional.
- **Unsure about a scaffolding choice the user owns** — which folder to adopt,
  whether existing content is a doc to leave alone, how to read an ambiguous answer?
  Ask before acting. The question costs one turn; a wrong guess makes the user undo
  a scaffold.
- The framing is **"adopt the folder"**: the method is being applied to their
  project, not the other way around.
