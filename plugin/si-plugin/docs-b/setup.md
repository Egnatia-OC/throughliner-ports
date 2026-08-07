---
name: setup
docset: B
note: >
  /setup procedure. The behaviour rules ARE read here, like any other session's;
  this doc carries no response-shape tags and states its own plain-language
  guard.
---

# /setup procedure

You are setting up a project folder with the Sovereign Implementer method.

**The behaviour rules govern this skill too, and are read like any other
session's.** The session-start hook points an unadopted folder at
`plugin-behaviour.md` exactly as it does an adopted one — that file ships with
the plugin, so it is readable whether or not anything has been set up yet. (An
earlier version of this doc said the rules "aren't loaded yet". That described a
delivery model the method no longer uses and was simply untrue.)

**This doc still carries no response-shape tags** (the bracketed `[BRIEF]`-style
markers other procedure docs use) — the prose in each step carries the behaviour
directly instead. **Don't add tags back.**

**/setup's own local rules stay, and are not made redundant by inheriting the
behaviour rules.** Leave the user's content untouched, never overwrite, never
blind-rename, use the user's words verbatim. They are specific to adopting a
stranger's folder, and belt-and-braces is the right posture at the
highest-consequence moment in the method — the one where files get created, and
the only one a brand-new user ever sees.

**Plain-language guard.** Everything you say during /setup is read by a non-coder
who may be brand new to all of this. Keep internal terms out of what they see — no
hook filenames, no `_build.md`, no "scope-lock," "method docs," or "Case B"
labels. Say "your project's files," not "method docs"; say "I'll set this up as a
migration," not "this is Case B."

## Step 1: Detect folder state

```
Case A  no content            the folder is empty or nearly so. Fresh start.
Case B  content, no SPEC.md   the user's own files exist but no project docs.
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
moved, or reorganized during scaffolding — scaffolding only adds the project docs.
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

**The FAQ is a LOCAL COPY of something that ships with the plugin — not a
document in the user's project.** That framing decides two things together, and
shipping either half alone is a regression:

```
never committed  ->  add `FAQ/` to the project's .gitignore (create the file if
                     absent; don't duplicate an existing entry). These files
                     explain how the METHOD works — they are not part of what
                     the user is building, and they read as clutter in the
                     user's own repository.

always restored  ->  restore FAQ/faq.md and FAQ/index.md from the shipped
                     templates WHENEVER THEY ARE MISSING, not only at first
                     adoption. Without this the ignore rule is a regression: a
                     fresh clone on another machine would have no FAQ at all,
                     and the FAQ is what session_start points every session at.
```

**An already-tracked FAQ needs an action, not a rule.** Adding a `.gitignore`
entry does nothing to files git is already tracking. Detect that case and
**offer** the untracking — `git rm --cached FAQ/`, which removes it from
tracking while leaving the files on disk — explaining in plain English what it
does and does not change. It alters what is in the user's repository, so it is
theirs to approve, not something to do silently or leave half-done.

**Scope: this reaches the FAQ and nothing else.** SPEC.md, QUEUE.md and LOG/ are
the user's own record and belong in their history; their CLAUDE.md is theirs
too. The FAQ is the only scaffolded artifact that is purely an explanation of
somebody else's tool, so there is no slope here to slide down.

**resources/research/ folder** — create it empty. It's the home for research notes
(`resources/research/<topic>.md`). Creating it at setup means research notes have a
place from day one rather than the folder being conjured on first use.

**CLAUDE.md:**

```
no CLAUDE.md exists  ->  scaffold from
                         ${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE-TEMPLATE.md
one already exists   ->  APPEND the method block; never overwrite
```

The template carries a Model field and a Repo visibility field; Step 4 fills
them from Q6 and the visibility detection.

**.si-version** — write the current plugin version (from
`${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`). session_start reads it to
detect when the plugin has been updated.

**.gitignore** — create it if absent, and make sure it carries entries for
`.throughliner/` and `FAQ/` (don't duplicate ones already there).

`FAQ/` is covered above: it is a local copy of the plugin's own help, restored
whenever missing, so it never belongs in the user's history.

That folder holds the editing-state signal: while Claude is writing a file, the
hooks drop a small file in there saying so, so a Markdown reader or editor open
on the same document can hold off rather than the two of you typing over each
other. It is transient state about the session running right now, and it carries
absolute paths from this machine, so it must never be committed.

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

**The settings question is fixed, not adaptive** — it's a project setting, not
discovery. Ask it the same way each time, in its own message, after discovery
reaches its stopping point. Optional; the user can skip it.

**Q6 (optional). Which Claude model do you mostly run — the newest generation, or
an older one?**
→ Claude works better with instructions written for the model actually running, so
the plugin keeps two sets and picks the one that fits. Name the current models
plainly and let the user pick; if they don't know or skip, say the safe default is
assumed and move on. Record the answer, not a preference about the plugin's
internals — the user should never meet the word for those two sets. Asked once, no
nag.

## Step 3b: Repo visibility, licensing, and publishing

Four things, in this order. The first two are **safety inputs**, not preferences,
and they apply to every project including one with no interest in publishing.

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

**2. Name the commit identity, before the first commit exists** [BRIEF; PROMPT
only if the user wants the change]. Run `git config user.email` and tell the user
in one line what address every commit will carry — and that GitHub offers a
`noreply` address if they'd rather not publish a real one. This runs on **every**
branch, not just the public ones: a private repo can go public later and nothing
re-checks its history. The timing is the whole point — before this session's
close makes the first commit, fixing this is one `git config` line; after it,
it's a full history rewrite, because commit metadata can't be edited out of the
files. If the user wants the `noreply` address, set it now (`git config
user.email <their-noreply>`); if they're happy as-is, say nothing more and move
on.

**3. Ask about the licence** [PROMPT] — in plain terms: does the user want others
free to use and build on this, or do they want to keep it to themselves? Write
their answer as a LICENSE file. Recommend one rather than asking cold.

**4. Offer public-repo setup, framed off the licence** [PROMPT] — "since you chose
this licence, would you like this on your GitHub? We can do it now, or note it for
a later planning session." **Offer, never push.** The note-it-for-later branch is
the graceful decline, and it's a real option, not a formality.

**State what publishing actually shows, in one sentence, when making that offer:**
most of what a visitor to the repo will find is the planning record itself — the
spec, the queue and the session log, which carry every decision, the rejected
alternatives and why they lost, and the fact that the project is built with an AI
method. Not a leak — some projects publish exactly that deliberately — but a
decision worth making consciously, and without that sentence it gets made by
default.

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
2a. fill CLAUDE.md's Model field from Q6            (or leave the safe default)
2b. fill CLAUDE.md's Repo visibility field from the detection (or the stated
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
