---
name: setup
description: Bring a folder under the no-code-method's discipline. Detects which of four cases applies (empty / existing code no docs / existing code foreign docs / already adopted) and runs the matching dialogue. V29: unified the previously-planned /new-project, /migrate, and /init-project commands.
disable-model-invocation: true
user-invocable: true
---

# /setup

Resolves the method's unadopted-folder state — by scaffolding, migrating, or refreshing. Users who don't want the method here: `/plugin` → Installed → toggle off.

Entry point only. The actual work happens in the `no-code-method:setup` subagent.

## Steps

1. **Invoke the subagent:** `Task(subagent_type="no-code-method:setup", prompt="User invoked /setup. Detect the case and run the matching dialogue per agents/setup.md.")`

2. **Wait for recap.** Subagent will have scaffolded, migrated, refreshed, or cancelled.

3. **Surface recap verbatim.** Don't re-summarise.

## Why a subagent

`/setup` can run many turns across four cases. Running in main Claude would pollute context with adoption internals irrelevant to subsequent project work.
