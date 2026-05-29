---
name: sovexplain
description: Explain why a method feature works the way it does. Answers "why" questions about the plugin — from hook denials to design decisions. No arguments required.
user-invocable: true
---

# /sovexplain

The user wants to understand *why* something in the method works the way it does. This might be a hook denial they just hit, a procedure step that surprised them, a term they don't recognise, or a general question about how the pieces fit together.

## Determine the topic

**If the user asked a specific question** — use it as-is.

**If the user invoked `/sovexplain` with no question** — look at the most recent interaction: the last hook denial, tool output, or skill step. Infer what they're asking about. When you answer, frame it clearly: "Based on [what just happened]: [explanation]." Then add: "If you had a different question, go ahead."

## Look up the answer

1. Read the proxy at `${CLAUDE_PLUGIN_ROOT}/docs/explain-proxy.md`.
2. Match the user's question to the most relevant topic(s) in the proxy.
3. Read the indicated line range(s) from `${CLAUDE_PLUGIN_ROOT}/docs/explain-reference.md` using offset/limit.
4. If the proxy doesn't cover the question, read the full section heading that's closest. If nothing matches, say so — don't fabricate rationale.

## Answer

- Plain English. No jargon the user hasn't used first.
- Lead with the "why" — the design reason, not the mechanism. Follow with the mechanism only if it helps understanding.
- Keep it short. A paragraph is usually enough. Two if the topic has layers (e.g. phase detection involves both the "why two phases" rationale and the "why file-existence" implementation choice).
- If the answer involves a doc the user has in their project (`_method/UX.md`, `_method/BACKLOG/`, etc.), mention it so they can look.
- If the answer connects to another feature, name it but don't explain it unprompted — let the user ask if they want to go deeper.

`[PROMPT]` — end with a brief signal that the user can ask another question or move on.
