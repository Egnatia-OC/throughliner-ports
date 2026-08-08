# /setup procedure

You are setting up a project folder with the Sovereign Implementer method.

This doc carries no response-shape tags (the bracketed `[BRIEF]`/`[SEQUENCE]`-style markers other procedure docs use). /setup runs before a project is adopted, so the behaviour rules that define those tags aren't loaded yet — here the prose in each step carries the behaviour directly: when to stop and wait for the user, when to keep output short, one question per message. Don't add tags back; they'd be undefined tokens in this doc.

**Plain-language guard.** Everything you say to the user during /setup is read by a non-coder who may be brand new to all of this. Use everyday words and keep internal or technical terms out of what they see — no hook filenames, no `_build.md` or `_plan.md`, no "scope-lock," "method docs," or "Case B" labels. Say "your project's files," not "method docs"; say "I'll set this up as a migration," not "this is Case B." Why this needs saying here when no other procedure doc repeats it: the plain-language behaviour rule loads only once a project is adopted, and /setup runs before that — so during a first-run /setup that rule isn't in context, and this reminder stands in for it.

## Step 1: Detect folder state

Before anything else, classify this folder:

- **Case A — No content:** The folder is empty or nearly so — none of the user's own files, no method docs. Fresh start.
- **Case B — Content exists, no method docs:** The folder already holds the user's own files (code, documents, notes, whatever the project is made of) but no SPEC.md/QUEUE.md. This can be a true fresh start, or a **migration** — a project already planned under another tool or an older version of this method, with its planning docs under other names. Don't assume blank-slate: if the existing files look like planning or spec documents, treat it as a possible migration and follow the Case B migration framing below. Recognise a migration by what the docs do, not by a fixed list of old names — the source could be anything.
- **Case C — Already set up:** SPEC.md exists.

For Case C, check `.si-version`:
- **Version matches current plugin:** Project is fully up to date. Tell the user in a sentence, offer to run /plan instead, then stop and wait for their answer — take no further action until they reply.
- **Version missing or outdated:** The plugin has been updated since this project was set up. Go to Step 2C (migration scaffolding).

## Case B: pre-existing content rules

Case B folders hold user content that predates the method. Two rules govern how /setup treats it:

1. **Peek before Q1.** Read the pre-existing content before asking the first interview question, and use what you learn to frame that question — a parenthetical clarifier where it helps — never to pre-answer it. The line: a clarifier invites the user's own answer ("I can see a tax brief in this folder — is that what this project is about, or something separate?"); pre-answering proposes the answer for confirmation ("From the brief, this is a tax-prep project for your 2025 return — right?"). The first frames the question; the second bundles an answer into it. Ask cold and you miss context the folder already gave you; pre-answer and the spec fills with your words instead of the user's.

2. **Leave it untouched; name it at close.** Pre-existing user content is not edited, moved, or reorganized during scaffolding — scaffolding only adds the method docs. In the closing message, explicitly name the pre-existing content as source material the user can refer back to.

## Case B: migration framing

When the Case B content is a migration — existing planning or spec docs from another tool or an older version of this method — /setup maps that content into SI's docs. The mapping is your judgment, not a fixed table; these guardrails keep it from importing the source's shape wholesale. (Detection stays generic: you recognised the migration by what the docs do, not by matching old names, so these apply to any source.)

- **State SPEC's purpose first.** Before mapping anything, say plainly what SPEC.md is for: it's product truth — what the app is, who it's for, how it works, and why it exists. It is not a UX spec or an implementation manual. Map the source's content into that frame; don't let the source decide what SPEC becomes.
- **Check role-fit before renaming — never blind-rename.** A source doc and the SI doc it seems to map to may not cover the same ground: the old one might be broader (a UX doc walking through every screen) or narrower than the SI doc. Before turning an old doc into an SI doc, check that their roles actually match. If they don't, say so plainly and let the user decide how to split or combine the content — don't silently rename one into the other.
- **Scrub the source's self-description from the content.** Renaming the file isn't enough — the old framing often hides inside the text. A line like an old UX doc's "this describes every functionality and UI element as the user experiences it" silently re-mandates the exhaustive detail SPEC is meant to leave out. When you map source content into SPEC, rewrite or drop any purpose, intro, or self-description sentence that re-asserts the source's role, so SPEC describes the product, not the old doc.
- **SI docs live at the project root.** SPEC.md, QUEUE.md, and the LOG/ folder sit directly in the project folder — there is no path setting and no doc-location config. If the source used a path block or pointed its docs elsewhere, that doesn't carry over; place the SI docs at the root regardless.

## Step 2C: Migration scaffolding

The plugin version has changed since this project was last set up. Re-scaffold without overwriting user content. Run the checks and file creation silently; keep the close (item 5) to a sentence or two:

1. **Check each doc/folder** from the Step 2 scaffold list. If it exists, skip it. If not, create it from the standard scaffold (empty structure, not interview-filled).
1a. **Convert an old-format QUEUE.md.** If the project's existing `QUEUE.md` uses an old multi-section shape (a `## Red flags`, `## Batches`, `### Parked`, `## Deferred tests`, or `## Captures` section) rather than the current `## Processed` / `## Unprocessed` model, load `${CLAUDE_PLUGIN_ROOT}/docs/migrate-checklist.md` and follow it to convert the queue — drafting the converted queue and getting the user's approval before writing. If the queue is already two-section, skip this. (This is the one project doc that reliably falls behind when the method evolves; the checklist encodes the judgment rules a find-and-replace can't make.)
2. **Retire REGISTRY.md if present.** REGISTRY.md is no longer one of the method's docs — older versions created it, so a project set up under one of those may still have a REGISTRY.md in it. Don't delete it on sight: the user may have written real notes there. Read it first. If it holds only what the old setup put there — a `# REGISTRY` heading with the "Components that exist…" line and either the empty placeholder or an auto-generated file list — remove it quietly as part of the migration. If it holds anything the user clearly added themselves, leave it in place, tell them plainly what's in it, and ask where that content should live now (usually SPEC.md) before removing the file. Where their own content goes is the user's call, not yours.
3. **Update .si-version** to the current plugin version.
4. **Skip the interview** — the project is already described in SPEC.md.
5. **Close state-aware.** If a leftover `_build.md` is present, an earlier build was interrupted: name it and recommend resuming it with /next — the migration's new files get recorded when that build closes. Otherwise, tell the user what was created or updated and recommend /done to record and commit the migration, matching Step 4.

Do NOT overwrite existing files. The goal is to add what a newer plugin version introduced, not to refresh content.

## Step 2: Scaffold the docs

Create these files (empty structure, content comes from the interview). Do this without narrating each file as it's created — the Step 4 close-out reports the full list, so nothing is lost by working quietly here:

**SPEC.md:**
```markdown
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
- `QUEUE.md` — processed work (vetted, ready to build) and unprocessed work (captured ideas not yet fully processed).
- `LOG/` — per-session records of what was built, tested, and decided.

## Principles
[filled by Q3]
```

**QUEUE.md:**
```markdown
# QUEUE

## Processed

Vetted work, ready to build — worked top to bottom. Each piece of work is one item: a `#### ` heading naming it, a `[slug]` at the end of that heading line, and a short rationale beneath. A leading flavor tag names how it runs — none for a build (Claude edits files), `[audit]` for a review pass, `[user]` for a step only you can do. A security or privacy risk Claude surfaces lives here too, as a work item carrying a `Red flag · State: cleared/uncleared` marker. The line below marks how far down is cleared to build; anything below it is decided but not ready yet.

--- Cleared to run above this line ---

## Unprocessed

Captured ideas and tasks not yet fully processed. The next /plan session goes through these with you and decides each one's fate — keep it (move it up to Processed) or drop it. Each is filed as its own `#### ` heading, so the list shows up in an editor's outline.

[filled by Q4]
```

**LOG/ folder:** Create the directory with one file:

**LOG/index.md:**
```markdown
# LOG Index

One-line summaries of each session. Newest first. Each line names the session's full entry file in this folder.
```

Session entries are written by /done, each as its own file in LOG/ — nothing else to scaffold.

**FAQ/ folder:** Create the `FAQ/` directory first, then copy the two template files into it — the folder must exist before the copies, or they fail:
- `FAQ/faq.md` — from `${CLAUDE_PLUGIN_ROOT}/templates/faq-template.md`
- `FAQ/index.md` — from `${CLAUDE_PLUGIN_ROOT}/templates/faq-index-template.md`

**resources/research/ folder:** Create the `resources/research/` directory (empty — no files). It's the home for research notes: when a web search or external lookup yields a finding worth keeping, Claude files it here as `resources/research/<topic>.md`. Creating it at setup means research notes have a place from day one rather than the folder being conjured on first use.

**CLAUDE.md:** If no CLAUDE.md exists, scaffold one from the template at `${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE-TEMPLATE.md`. If one already exists (Case B), append the method block rather than overwriting. The template carries an Editor field left as `not recorded`, a Working mode field defaulting to `local`, and a Completion mode field defaulting to `in-/next`; Step 4 fills them from Q6, Q7, and Q8.

**.si-version:** Write the current plugin version (from `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`) to a file called `.si-version` in the project root. session_start reads it to detect when the plugin has been updated and the project needs re-scaffolding.

**Git repository:** If the folder is not already a git repository, run `git init` so the project has version history from the first session. Do this silently and mechanically, like the rest of the scaffold — no narration. This is what lets the close-out commit the new files: without a repository there is nothing to commit to.

## Step 3: Interview (adaptive discovery, one question at a time, plus three optional settings)

The interview is an **adaptive discovery**, not a fixed script. Its job is to reach a shared, buildable understanding of the project — enough to fill SPEC.md's What / Who / How / Principles and capture a first piece of work — by reading each answer and asking the next question that actually matters, rather than marching through a set list. Ask **one question per message** and stop after each — wait for the answer before asking the next. Never bundle two questions into one message, even short ones.

**How the adaptive interview runs:**

- **Read each answer, then reason about what's still unclear** before choosing the next question. Walk the design one branch at a time — resolve what an answer opens up before moving to a new topic, rather than reading questions off a list. The next question is generated from what's still missing, not from a fixed position in a script.
- **Recommend an answer to each question.** Don't just ask cold — offer a plausible answer the user can accept, correct, or replace ("My guess is this is for personal use rather than a team — is that right?"). This composes with the method's one-at-a-time and recommend-an-answer rules; a non-coder finds it far easier to react to a proposal than to fill a blank.
- **Cover these topics** (this is a bank to draw on, not a checklist to recite): what the project is and who it's for (fills What this is / Who it's for); the core of it — the main thing it produces, organises, or does (fills How it works); any principles or constraints, e.g. "must work offline", "no accounts", "everything in plain text", "must follow the 2025 tax rules" (fills Principles); the first thing to build or make progress on today (becomes the first work item); and anything else worth knowing before starting. Draw on whichever of these the project still needs — skip what an earlier answer or the existing content already settled, and probe deeper wherever the picture is still thin.
- **Explore whatever already exists first.** A non-coder is often starting from scratch, but not always — there may be an old doc, a sketch, a rough notes file, or a running app. Read whatever material the folder already holds (Case B) and use it to inform your questions, rather than asking the user things the existing content already answers. Where there's genuinely nothing yet, that's fine — just interview from a blank slate.

**The stopping rule (the anti-overwhelm guard).** Keep probing only until there's a shared, buildable understanding — the point where the answers bottom out into something concrete enough to build from (the "5 Whys" idea: you're done when the Whys are answered, not when every possible branch is exhausted). Don't turn discovery into an interrogation. And tell the user plainly, early on, that they can end the interview any time by saying **"build from what we have"** — at which point you stop asking and write the docs from whatever's been gathered. Depth is the goal; a slog is not.

**The first work item** — whichever answer names the first thing to build — creates one rough work item in QUEUE.md's Unprocessed section: a `#### ` heading in the user's words, with a kebab-case `[slug]` at the end of that heading line and a "captured by you" note beneath it. Use the user's words verbatim. No expansion, no illustrative examples, no parentheticals drawn from visible context — even examples in parentheses read as commitments the user agreed to. Scope decisions belong in /plan (which is where this item gets processed). If examples would clarify what's in scope, ask a follow-up instead of smuggling them into the entry.

**The three settings questions (Q6, Q7, Q8) are fixed, not adaptive** — they're project settings, not discovery, so ask them the same way each time, one message of its own, after the discovery has reached its stopping point. They're optional; the user can skip any.

**Q6 (optional). When you open a `.md` file — like these project docs — what do you usually open it in?**
→ Identifies your default `.md` app. Knowing it lets Claude point you to one of your project docs with a link that opens in that app — but the link is only useful if you keep a default `.md` reader open alongside Claude. If you'd rather not set this, just say skip — that's a plain option for anyone, not only "if you're unsure." The trade-off of skipping: when Claude needs to show you a doc, it writes the doc's text out into the chat instead, which costs tokens each time and adds up over a project's life. (Doc links also aren't much use while Claude is driving your screen remotely — a minor caveat, not a reason to skip.) Fills the Editor field in the generated CLAUDE.md. Asked once, no nag, never again. If the user names an editor, record it in CLAUDE.md's Editor field; if they skip, write `not recorded` there so the field is present but empty.

**Q7 (optional). Will you usually be working from your computer, or driving Claude from your phone?**
→ Sets your working mode. Two options, explained once here: **local** means you're at your desktop, where an edited file opens instantly — so Claude points you to text in your docs with a link. **remote** means you're driving Claude from your phone, where opening an edited file is awkward — so Claude pastes the text straight into chat instead. Defaults to **local** if you skip. Fills the Working mode field in the generated CLAUDE.md, and you can switch anytime just by telling Claude ("I'm remote today") — it holds for that session and reverts after. Asked once, no nag.

**Q8 (optional). When there's a step only you can do — like sending something or checking a screen — do you prefer to do it together with Claude as it comes up, or handle those on your own between sessions?**
→ Sets your completion mode. Two options, explained once here: **in-/next** (the default) means you let Claude walk you through each such step when it reaches it while building — the relaxed way, nothing to remember or chase. **async** means you often do these on your own, between sessions. The only thing it changes: in async mode, planning sessions ask up front whether you've already done any of these steps (so they get recorded); in the default in-/next mode they don't ask — you're doing those steps in /next anyway, so being asked each planning session would just nag. Defaults to **in-/next** if you skip. Fills the Completion mode field in the generated CLAUDE.md; switch anytime by re-running /setup or just telling Claude. Asked once, no nag.

## Step 4: Write the docs

Once discovery has reached a buildable understanding (or the user says "build from what we have"), write the docs, then close in a sentence or two — show what was created and recommend /done, then stop and wait for the user:
1. Fill SPEC.md with the interview answers.
2. Write one work item in QUEUE.md's Unprocessed section from the first-thing-to-build answer — a `#### ` heading in the user's words with a `[slug]` at its end and a "captured by you" note, not multiple scoped entries.
2a. Fill the Editor field in CLAUDE.md from Q6 — the named editor, or `not recorded` if it was skipped.
2b. Fill the Working mode field in CLAUDE.md from Q7 — `local` or `remote` as answered, or `local` if it was skipped.
2c. Fill the Completion mode field in CLAUDE.md from Q8 — `in-/next` or `async` as answered, or `in-/next` if it was skipped.
3. Show the user what was created (file list + one-line summary of each).
4. Recommend /done to record this setup and commit the new files. The file list above shows what appeared in the folder; the session's single summary — what was set up and why — is the LOG entry /done writes at close.
5. Teach the working rhythm in plain words — a few short sentences so the user knows how sessions go from here:
   - **/setup** you've now run once; you won't run it again for this project.
   - From here, two commands carry the work: **/plan** to think and organise (manage the queue, add ideas, resolve questions), and **/next** to build the next thing on the list. Run /plan whenever planning is needed, and /next once per item as you work down the queue — planning repeats for long stretches, building repeats across many items.
   - However a session goes, end it the same way: **/done** to record what happened, then **/clear** to start fresh. The habit that matters: always /done before /clear, so each session is saved before the context resets.

## Rules

- One question per message. Do not bundle.
- Use the user's language — don't rephrase into jargon.
- If an answer is vague, ask a follow-up for clarity — but honour the stopping rule and don't interrogate. Probe until the picture is buildable, then stop.
- Don't create files until discovery has covered at least what the project is, who it's for, its core, and a first thing to build — enough to fill SPEC's What / Who / How and one work item. Principles and the free-form "anything else" are optional if the user has nothing to add.
- Unsure about a scaffolding choice the user owns — which folder to adopt, whether existing content is a doc to leave alone, how to read an ambiguous answer? Ask before acting; don't guess and scaffold wrong. The question costs one turn; a wrong guess makes the user undo a scaffold.
- The "adopt the folder" framing: the method is being applied to their project, not the other way around.
