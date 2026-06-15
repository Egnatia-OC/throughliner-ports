# /setup procedure

You are setting up a project folder with the Sovereign Implementer method.

This doc carries no response-shape tags (the bracketed `[BRIEF]`/`[SEQUENCE]`-style markers other procedure docs use). /setup runs before a project is adopted, so the behaviour rules that define those tags aren't loaded yet — here the prose in each step carries the behaviour directly: when to stop and wait for the user, when to keep output short, one question per message. Don't add tags back; they'd be undefined tokens in this doc.

## Step 1: Detect folder state

Before anything else, classify this folder:

- **Case A — No content:** The folder is empty or nearly so — none of the user's own files, no method docs. Fresh start.
- **Case B — Content exists, no method docs:** The folder already holds the user's own files (code, documents, notes, whatever the project is made of) but no SPEC.md/QUEUE.md/REGISTRY.md.
- **Case C — Already set up:** SPEC.md exists.

For Case C, check `.si-version`:
- **Version matches current plugin:** Project is fully up to date. Tell the user in a sentence, offer to run /plan instead, then stop and wait for their answer — take no further action until they reply.
- **Version missing or outdated:** The plugin has been updated since this project was set up. Go to Step 2C (migration scaffolding).

## Case B: pre-existing content rules

Case B folders hold user content that predates the method. Two rules govern how /setup treats it:

1. **Peek before Q1.** Read the pre-existing content before asking the first interview question, and use what you learn to frame that question — a parenthetical clarifier where it helps — never to pre-answer it. The line: a clarifier invites the user's own answer ("I can see a tax brief in this folder — is that what this project is about, or something separate?"); pre-answering proposes the answer for confirmation ("From the brief, this is a tax-prep project for your 2025 return — right?"). The first frames the question; the second bundles an answer into it. Ask cold and you miss context the folder already gave you; pre-answer and the spec fills with your words instead of the user's.

2. **Leave it untouched; name it at close.** Pre-existing user content is not edited, moved, or reorganized during scaffolding — scaffolding only adds the method docs. In the closing message, explicitly name the pre-existing content as source material the user can refer back to.

## Step 2C: Migration scaffolding

The plugin version has changed since this project was last set up. Re-scaffold without overwriting user content. Run the checks and file creation silently; keep the close (item 4) to a sentence or two:

1. **Check each doc/folder** from the Step 2 scaffold list. If it exists, skip it. If not, create it from the standard scaffold (empty structure, not interview-filled).
2. **Update .si-version** to the current plugin version.
3. **Skip the interview** — the project is already described in SPEC.md.
4. **Close state-aware.** If a leftover `_build.md` is present, an earlier build was interrupted: name it and recommend resuming it with /next — the migration's new files get recorded when that build closes. Otherwise, tell the user what was created or updated and recommend /done to record and commit the migration, matching Step 4.

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

Four project docs structure each project:
- `SPEC.md` — product truth. What the project is, who it's for, how it works.
- `QUEUE.md` — work batches and captured ideas.
- `REGISTRY.md` — components list. What exists, where it lives.
- `LOG/` — per-session records of what was built, tested, and decided.

## Principles
[filled by Q3]
```

**QUEUE.md:**
```markdown
# QUEUE

## Red flags

Security, privacy, and data-exposure risks Claude has surfaced — kept at the top so they're the first thing seen each session. Each carries a state: open, resolved, or accepted. Empty until a risk comes up.

## Batches

Worked top to bottom. Each batch is one /next session. Subheadings name the kind of work (Build, Test, Audit).

[filled by Q4]

### Parked

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

### Parked
```

**REGISTRY.md:**
```markdown
# REGISTRY

Components that exist in this project. Updated after each build.

[empty until first build completes]
```

**LOG/ folder:** Create the directory with one file:

**LOG/index.md:**
```markdown
# LOG Index

One-line summaries of each session. Newest first. Each line names the session's full entry file in this folder.
```

Session entries are written by /done, each as its own file in LOG/ — nothing else to scaffold.

**FAQ/ folder:** Create the directory with two files scaffolded from templates:
- `FAQ/faq.md` — from `${CLAUDE_PLUGIN_ROOT}/templates/faq-template.md`
- `FAQ/index.md` — from `${CLAUDE_PLUGIN_ROOT}/templates/faq-index-template.md`

**CLAUDE.md:** If no CLAUDE.md exists, scaffold one from the template at `${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE-TEMPLATE.md`. If one already exists (Case B), append the method block rather than overwriting.

**.si-version:** Write the current plugin version (from `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`) to a file called `.si-version` in the project root. session_start reads it to detect when the plugin has been updated and the project needs re-scaffolding.

**Git repository:** If the folder is not already a git repository, run `git init` so the project has version history from the first session. Do this silently and mechanically, like the rest of the scaffold — no narration. This is what lets the close-out commit the new files: without a repository there is nothing to commit to.

## Step 3: Interview (5 questions, one at a time)

Ask these one per message, and stop after each — wait for the user's answer before asking the next. Never bundle two questions into one message, even short ones. Use the answers to fill SPEC.md and QUEUE.md.

**Q1. What is this project, and who is it for?**
→ Fills "What this is" and "Who it's for" in SPEC.md.

**Q2. What's the core of it — the main thing it produces, organises, or does?**
→ Fills "How it works" in SPEC.md.

**Q3. Any principles or constraints? (e.g., "must work offline", "no accounts", "everything in plain text", "must follow the 2025 tax rules")**
→ Fills "Principles" in SPEC.md. If the user says "none" or isn't sure, leave the section with a note that it can be added later.

**Q4. What's the first thing to build or do? What would you want to have working or made progress on by the end of today?**
→ Creates one rough build entry in QUEUE.md under a Build subheading. Use the user's words verbatim. No expansion, no illustrative examples, no parentheticals drawn from visible context — even examples in parentheses read as commitments the user agreed to. Scope decisions belong in /plan. If examples would clarify what's in scope, ask a Q4 follow-up instead of smuggling them into the entry — the one-follow-up-max rule for vague answers (see Rules) already covers that case.

**Q5. Anything else I should know before we start?**
→ Free-form. Route to SPEC.md if it's product info, to QUEUE.md if it's a task, or acknowledge and move on.

## Step 4: Write the docs

After all 5 answers, write the docs, then close in a sentence or two — show what was created and recommend /done, then stop and wait for the user:
1. Fill SPEC.md with the interview answers.
2. Write one build entry in QUEUE.md from Q4 — under a Build subheading, in the user's words, not multiple scoped entries.
3. Show the user what was created (file list + one-line summary of each).
4. Recommend /done to record this setup and commit the new files. The file list above shows what appeared in the folder; the session's single summary — what was set up and why — is the LOG entry /done writes at close.

## Rules

- One question per message. Do not bundle.
- Use the user's language — don't rephrase into jargon.
- If an answer is vague, ask one follow-up for clarity. Don't interrogate.
- Don't create files until you have at least Q1–Q4 answered (Q5 is optional if skipped).
- Unsure about a scaffolding choice the user owns — which folder to adopt, whether existing content is a doc to leave alone, how to read an ambiguous answer? Ask before acting; don't guess and scaffold wrong. The question costs one turn; a wrong guess makes the user undo a scaffold.
- The "adopt the folder" framing: the method is being applied to their project, not the other way around.
