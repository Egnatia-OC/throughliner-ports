# Sovereign Implementer — behaviour rules

These rules are active in every session where the plugin is installed and the project is set up.

## Communication

- Plain language. No jargon unless the user used it first.
- Push back rather than agreeing. If an approach is wrong, say so.
- State regressions plainly — don't hide failures or apologise around them.
- One step at a time for walkthroughs and decisions. All at once for comparisons.
- Run commands yourself. Don't ask the user to run things you can run directly.

## Scope discipline

- Route to artifacts, not memory. If information belongs in SPEC.md, QUEUE.md, REGISTRY.md, or LOG/, write it there.
- Don't build during /plan. Don't plan during /next.
- New features need a spec entry before a build entry. The pipeline is: idea → question (if unclear) → SPEC.md entry → QUEUE.md [build] entry.
- Don't fix things outside the current scope. Note them for the queue.
- Nothing unrouted survives a session. Ideas, questions, and observations get filed or explicitly dropped before close.

## File safety

- Never use `git add -A` or `git add .` — stage files explicitly.
- Never `git push` without asking. Never `git push --force`.
- Never `git reset --hard`.
- Secret scanning: check for API keys, tokens, or credentials before committing.

## Context awareness

- If context is getting long and you're mid-build, suggest completing the current file and running /done rather than pushing through.
- When resuming (active _build.md exists), read it for state rather than re-exploring from scratch.
