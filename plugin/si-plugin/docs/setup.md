# /setup procedure

You are setting up a project folder with the Sovereign Implementer method.

## Step 1: Detect folder state

Before anything else, classify this folder:

- **Case A — Empty/near-empty:** No source code, no docs. Fresh start.
- **Case B — Existing code, no method docs:** Source files exist but no SPEC.md/QUEUE.md/REGISTRY.md.
- **Case C — Already set up:** SPEC.md exists.

For Case C, check `.si-version`:
- **Version matches current plugin:** Project is fully up to date. Tell the user, offer to run /plan instead, and stop here.
- **Version missing or outdated:** The plugin has been updated since this project was set up. Go to Step 2C (migration scaffolding).

## Case B: pre-existing content rules

Case B folders hold user content that predates the method. Two rules govern how /setup treats it:

1. **Peek before Q1.** Read the pre-existing content before asking the first interview question, and use what you learn to frame that question — a parenthetical clarifier where it helps — never to pre-answer it. The line: a clarifier invites the user's own answer ("I can see a tax brief in this folder — is that what this project is about, or something separate?"); pre-answering proposes the answer for confirmation ("From the brief, this is a tax-prep project for your 2025 return — right?"). The first frames the question; the second bundles an answer into it. Ask cold and you miss context the folder already gave you; pre-answer and the spec fills with your words instead of the user's.

2. **Leave it untouched; name it at close.** Pre-existing user content is not edited, moved, or reorganized during scaffolding — scaffolding only adds the method docs. In the closing message, explicitly name the pre-existing content as source material the user can refer back to.

## Step 2C: Migration scaffolding [BRIEF]

The plugin version has changed since this project was last set up. Re-scaffold without overwriting user content:

1. **Check each doc/folder** from the Step 2 scaffold list. If it exists, skip it. If not, create it from the standard scaffold (empty structure, not interview-filled).
2. **Update .si-version** to the current plugin version.
3. **Skip the interview** — the project is already described in SPEC.md.
4. **Tell the user** what was created or updated, and that they're ready for /plan or /next.

Do NOT overwrite existing files. The goal is to add what a newer plugin version introduced, not to refresh content.

## Step 2: Scaffold the docs

Create these files (empty structure, content comes from the interview):

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
- `SPEC.md` — product truth. What the app is, who it's for, how it works.
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

Worked top to bottom. Each batch is one /next session — builds first, then tests.

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

## Step 3: Interview (5 questions, one at a time) [SEQUENCE, PROMPT]

Ask these one per message. Wait for the answer before the next. Use the answers to fill SPEC.md and QUEUE.md.

**Q1. What are you building and who is it for?**
→ Fills "What this is" and "Who it's for" in SPEC.md.

**Q2. Describe the core functionality — what does it actually do?**
→ Fills "How it works" in SPEC.md.

**Q3. Any principles or constraints? (e.g., "must work offline", "no accounts", "mobile-first")**
→ Fills "Principles" in SPEC.md. If the user says "none" or isn't sure, leave the section with a note that it can be added later.

**Q4. What's the first thing to build? What would you want working by the end of today?**
→ Creates one rough build entry in QUEUE.md under a Build subheading. Use the user's words verbatim. No expansion, no illustrative examples, no parentheticals drawn from visible context — even examples in parentheses read as commitments the user agreed to. Scope decisions belong in /plan. If examples would clarify what's in scope, ask a Q4 follow-up instead of smuggling them into the entry — the one-follow-up-max rule for vague answers (see Rules) already covers that case.

**Q5. Anything else I should know before we start?**
→ Free-form. Route to SPEC.md if it's product info, to QUEUE.md if it's a task, or acknowledge and move on.

## Step 4: Write the docs [BRIEF, PROMPT]

After all 5 answers:
1. Fill SPEC.md with the interview answers.
2. Write one build entry in QUEUE.md from Q4 — under a Build subheading, in the user's words, not multiple scoped entries.
3. Show the user what was created (file list + one-line summary of each).
4. Tell them: "Run /plan to scope your first batch, or /next if you're ready to build."

## Rules

- One question per message. Do not bundle.
- Use the user's language — don't rephrase into jargon.
- If an answer is vague, ask one follow-up for clarity. Don't interrogate.
- Don't create files until you have at least Q1–Q4 answered (Q5 is optional if skipped).
- The "adopt the folder" framing: the method is being applied to their project, not the other way around.
