---
name: setup
description: Bring a folder under the no-code-method's discipline. Detects which of four cases applies (empty / existing code no docs / existing code foreign docs / already adopted) and runs the matching dialogue. Resolves the unadopted-folder state that the SessionStart advisory and PreToolUse enforcement gate are protecting. V29: unifies the previously-planned /new-project, /migrate, and /init-project (V19) commands.
disable-model-invocation: true
user-invocable: true
---

# /setup

The user runs `/setup` to resolve the no-code-method's unadopted-folder state — by scaffolding the method's spine docs (new project), migrating existing docs to method spec, or refreshing an already-adopted folder. Users who don't want the method in a folder should disable the plugin for that project via `/plugin` → Installed → toggle off.

This skill is the entry point. The actual dialogue and per-case work happens inside the `no-code-method:setup` subagent — invoke it once and let it run.

## Steps

1. **Invoke the subagent.** Use the Task tool:

   ```
   Task(subagent_type="no-code-method:setup", prompt="User invoked /setup. Detect the case and run the matching dialogue per agents/setup.md.")
   ```

   No detection or case-branching from main Claude — that's the subagent's first action.

2. **Wait for the subagent's recap.** When it returns, the subagent has either:
   - Scaffolded the spine docs (case 1 or 2 → folder is now adopted),
   - Migrated or overwritten foreign docs (case 3 → folder is now adopted),
   - Refreshed templates against an already-adopted folder (case 4 → folder stays adopted, version footers may have bumped), or
   - Cancelled without changes.

3. **Surface the subagent's recap to the user verbatim.** Don't re-summarise — the subagent's wording is intentional and the user needs to see what state the folder is in now.

## Why a subagent and not inline

`/setup`'s dialogue can run many turns across all four cases, and case 3's migrate flow walks the user through a foreign `CLAUDE.md` section-by-section. Running this in main Claude's context would pollute it with adoption-flow internals that aren't relevant to the actual project work that follows. The subagent keeps the dialogue self-contained and returns a clean recap.
