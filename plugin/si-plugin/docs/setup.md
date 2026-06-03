# /setup procedure

You are setting up a project folder with the Sovereign Implementer method.

## Step 1: Detect folder state

Before anything else, classify this folder:

- **Case A — Empty/near-empty:** No source code, no docs. Fresh start.
- **Case B — Existing code, no method docs:** Source files exist but no SPEC.md/QUEUE.md/REGISTRY.md.
- **Case C — Already set up:** SPEC.md exists. This is a refresh/version-migration.

For Case C: tell the user the project is already set up and offer to run /plan instead. Stop here.

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

**LOG/ folder:** Create the directory with two files:

**LOG/index.md:**
```markdown
# LOG Index

One-line summaries of each session. Newest first.
```

**LOG/log.md:**
```markdown
# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).
```

**FAQ/ folder:** Create the directory with two files scaffolded from templates:
- `FAQ/faq.md` — from `${CLAUDE_PLUGIN_ROOT}/templates/faq-template.md`
- `FAQ/index.md` — from `${CLAUDE_PLUGIN_ROOT}/templates/faq-index-template.md`

**CLAUDE.md:** If no CLAUDE.md exists, scaffold one from the template at `${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE-TEMPLATE.md`. If one already exists (Case B), append the method block to it rather than overwriting.

## Step 3: Interview (5 questions, one at a time) [SEQUENCE, PROMPT]

Ask these questions one per message. Wait for the answer before asking the next. Use the answers to fill SPEC.md and QUEUE.md.

**Q1. What are you building and who is it for?**
→ Fills "What this is" and "Who it's for" in SPEC.md.

**Q2. Describe the core functionality — what does it actually do?**
→ Fills "How it works" in SPEC.md.

**Q3. Any principles or constraints? (e.g., "must work offline", "no accounts", "mobile-first")**
→ Fills "Principles" in SPEC.md. If the user says "none" or isn't sure, leave this section with a note that it can be added later.

**Q4. What's the first thing to build? What would you want working by the end of today?**
→ Creates one rough build entry in QUEUE.md under a Build subheading. Use the user's words, don't expand or split — scope decisions belong in /plan.

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
- If the user gives a vague answer, ask one follow-up for clarity. Don't interrogate.
- Don't create files until you have at least Q1-Q4 answered (Q5 is optional if skipped).
- The "adopt the folder" framing: the method is being applied to their project, not the other way around.
