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

## Principles
[filled by Q3]
```

**QUEUE.md:**
```markdown
# QUEUE

Entries are worked top-to-bottom. Each entry has a type marker and a clear scope.

## Next up

[filled by Q4]

## Parked

[empty]
```

**REGISTRY.md:**
```markdown
# REGISTRY

Components that exist in this project. Updated after each build.

[empty until first build completes]
```

**LOG/ folder:** Create the directory. It stays empty until the first /done.

**CLAUDE.md:** If no CLAUDE.md exists, scaffold one from the template at `${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE-TEMPLATE.md`. If one already exists (Case B), append the method block to it rather than overwriting.

## Step 3: Interview (5 questions, one at a time)

Ask these questions one per message. Wait for the answer before asking the next. Use the answers to fill SPEC.md and QUEUE.md.

**Q1. What are you building and who is it for?**
→ Fills "What this is" and "Who it's for" in SPEC.md.

**Q2. Describe the core functionality — what does it actually do?**
→ Fills "How it works" in SPEC.md.

**Q3. Any principles or constraints? (e.g., "must work offline", "no accounts", "mobile-first")**
→ Fills "Principles" in SPEC.md. If the user says "none" or isn't sure, leave this section with a note that it can be added later.

**Q4. What's the first thing to build? What would you want working by the end of today?**
→ Creates the first entry in QUEUE.md under "Next up." Mark it as `[build]`.

**Q5. Anything else I should know before we start?**
→ Free-form. Route to SPEC.md if it's product info, to QUEUE.md if it's a task, or acknowledge and move on.

## Step 4: Write the docs

After all 5 answers:
1. Fill SPEC.md with the interview answers.
2. Write the first QUEUE.md entry from Q4.
3. Show the user what was created (file list + one-line summary of each).
4. Tell them: "Run /next to start building, or /plan to adjust the queue first."

## Rules

- One question per message. Do not bundle.
- Use the user's language — don't rephrase into jargon.
- If the user gives a vague answer, ask one follow-up for clarity. Don't interrogate.
- Don't create files until you have at least Q1-Q4 answered (Q5 is optional if skipped).
- The "adopt the folder" framing: the method is being applied to their project, not the other way around.
