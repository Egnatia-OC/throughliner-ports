---
name: sovexplain
description: Answers questions about the method — what the project does, how to use a feature, or why something works the way it does. Routes to the right source based on question type. No arguments required.
user-invocable: true
---

# /sovexplain

The user has a question about the method or their project. Route to the right source based on what they're asking.

## Determine the topic

**If the user asked a specific question** — use it as-is.

**If the user invoked `/sovexplain` with no question** — look at the most recent interaction: the last hook denial, tool output, or skill step. Infer what they're asking about. When you answer, frame it clearly: "Based on [what just happened]: [explanation]." Then add: "If you had a different question, go ahead."

## Classify the question

Before looking anything up, classify what the user is asking:

- **"What"** — capability identification. "What does my project do?" "What have we built?" "What's in the project?" The user wants an overview of their project's current state.
- **"How"** — usage. "How do I close a build?" "How do I add a feature?" "How does planning work?" The user wants to know how to do something with the method.
- **"Why"** — design rationale. "Why does it block my edits?" "Why two phases?" "Why is close mandatory?" The user wants to understand the reasoning behind a method feature.

When ambiguous, default to "why" — it was the original and most common use case.

## Route and answer

### "What" route — capability identification

1. Read the MANIFEST proxy at `_method/proxies/manifest.md` (or legacy `.proxies/manifest.md`).
2. Read the `## Capabilities summary` section. If it exists and is populated, use it as the primary answer.
3. If the summary doesn't exist or is a placeholder, fall back to reading `_method/MANIFEST.md` and summarize the entries directly.
4. Answer in plain English. Frame around what the user's project does, not what MANIFEST contains.

### "How" route — usage

1. Identify the matching skill or procedure doc. Skills live at `${CLAUDE_PLUGIN_ROOT}/skills/<name>/SKILL.md`. Procedure docs live at `${CLAUDE_PLUGIN_ROOT}/docs/procedures/<name>.md`.
2. Common mappings:
   - Planning/batches/BACKLOG → `procedures/planning.md`
   - Starting a build → `procedures/before-build.md` (recap) then `procedures/build.md`
   - Closing a build → `procedures/close.md`
   - Testing → `procedures/testing.md`
   - Git operations → `procedures/git.md`
   - New ideas → `procedures/ideate.md`
   - Open questions → `procedures/deliberate.md`
   - Setup → `procedures/setup.md`
   - Reverting → `procedures/revert.md`
   - Doc compression → `procedures/tersify.md`
   - Research → `/sovresearch` skill
3. Read the matching doc. Summarize the key steps in plain English — don't dump the procedure verbatim.
4. End by naming the slash command that triggers the flow, if one exists.

### "Why" route — design rationale

1. Read the proxy at `${CLAUDE_PLUGIN_ROOT}/docs/explain-proxy.md`.
2. Match the user's question to the most relevant topic(s) in the proxy.
3. Read the indicated line range(s) from `${CLAUDE_PLUGIN_ROOT}/docs/explain-reference.md` using offset/limit.
4. If the proxy doesn't cover the question, read the full section heading that's closest. If nothing matches, say so — don't fabricate rationale.

## Answer style

- Plain English. No jargon the user hasn't used first.
- Lead with the direct answer, then supporting detail only if it helps understanding.
- Keep it short. A paragraph is usually enough. Two if the topic has layers.
- If the answer involves a doc the user has in their project (`_method/UX.md`, `_method/BACKLOG/`, etc.), mention it so they can look.
- If the answer connects to another feature, name it but don't explain it unprompted — let the user ask if they want to go deeper.

`[PROMPT]` — end with a brief signal that the user can ask another question or move on.
