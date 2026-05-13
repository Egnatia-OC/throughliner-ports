---
name: init-project
description: Scaffold the 5 no-code-method template files (CLAUDE.md, UX.md, BACKLOG.md, MANIFEST.md) into a fresh project. Refuses on a non-empty target; points the user at /migrate instead.
disable-model-invocation: true
user-invocable: true
---

# /init-project

Scaffolds the no-code-method spine docs into the user's current working directory (`cwd`) from the plugin's bundled templates.

## When to use

The user runs `/init-project` when they want to **start a fresh no-code-method project from scratch** — no method docs in the project yet.

If the user already has hand-authored docs from earlier drafting (for example, drafted in Cowork before installing the plugin), they should run `/migrate` instead. `/init-project` will refuse to overwrite existing method files.

`ADDITIONAL-DOC-TEMPLATE.md` is not scaffolded here. It's added per-project via `/add-sot-doc <name>` when the project decides it needs an additional source-of-truth doc.

## Steps

1. **Check.** Run:

   ```
   python "${CLAUDE_PLUGIN_ROOT}/skills/init-project/scripts/scaffold.py" check
   ```

   The script writes JSON to stdout: `{"target_path": "...", "conflicts": [...], "ready": true|false}`.

2. **Decide what to say to the user.**

   - **If `ready` is true (no conflicts).** Echo the target path back to the user in plain English and ask for confirmation: "About to scaffold the no-code-method templates into `<target_path>`. Proceed?" If the target path looks like an obviously wrong location (Desktop, home folder, system temp), point that out gently before they confirm so they have a chance to `cd` somewhere correct.

   - **If `ready` is false (conflicts found).** Do **not** ask for confirmation. Tell the user plainly which method files already exist in their project (the `conflicts` list, with paths), and suggest running `/migrate` instead. `/migrate` is built for the case where docs already exist and need to be brought up to spec. Stop. Do not run the write step.

3. **Write (only after user confirmation).** Run:

   ```
   python "${CLAUDE_PLUGIN_ROOT}/skills/init-project/scripts/scaffold.py" write
   ```

   The script writes JSON to stdout: `{"written": true, "files": [...], "target_path": "..."}` on success, or `{"written": false, "reason": "...", ...}` on failure.

4. **Report.** On success, tell the user which files were written, in plain English. On failure, surface the `reason` plainly. Do not retry silently.

## Notes

- The script does its own recursive existence scan in step 1, so files in subdirectories (e.g. an existing `docs/UX.md`) are caught even though the scaffold itself writes to `cwd` root.
- After scaffolding, the user is free to move the docs into any folder structure that suits the project, as long as they update the path block in `CLAUDE.md` to match. The plugin's hooks read the path block to locate the docs.
