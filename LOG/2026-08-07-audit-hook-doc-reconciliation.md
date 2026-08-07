# [HASH] — The docs reconciled against the hooks: four undocumented behaviours written down, four understatements corrected, three stale names fixed

The reverse direction nobody looks for. The hooks stay as they are; the docs were wrong about them.

**Undocumented behaviours, now documented.**

- **The self-hosting mechanism** had no template field, no doc, no FAQ entry — `session_start.py` detects the plugin package inside the repo, asks once, records `Self-hosting:` in CLAUDE.md, and suppresses the version-drift report. `CLAUDE-TEMPLATE.md` gained the field and a comment explaining what it changes and why a recorded `no` is honoured permanently. The payload is suppression, which is the one thing detection can do that ambient prose cannot: prose cannot stop a program printing a line.
- **The scope-lock's fail-open tri-state** — no `Files:` section means no enforcement, present-but-empty means the always-editable set, entries mean those files. Written into `plugin-behaviour.md` as a table, with the design stated: it fails open deliberately so a malformed `_build.md` cannot brick a session, but it fails open **audibly**, via a once-per-build advisory, so an unscoped run is a thing you were told about.
- **Mechanical denial of scripted shell file-writes**, and **the `git commit -a/-am/--all` deny** — both absent from the File-safety block, which listed `git add -A` but not its twin. Both added, with the note that the listed items are *blocked*, not merely asked of you.

**Understatements corrected.** The planning gate's quiet-list omitted FAQ/ and the memory, research and scratchpad exemptions — `plan.md` now lists all of them, plus the deliberate exclusion of `templates/` and its reason. `plugin-behaviour.md` claimed "all three hooks parse" the work-item shape when two do. `migrate-checklist.md` said the lint "confirms" the queue is well-formed when it is a **deny-list** that passes novel structure silently — now stated as "a clean run means nothing it checks for went wrong, never that the queue is confirmed well-formed". And `next.md` claimed an insertion backstop that Write-based insertions bypass by design — now bounded honestly as a check that catches the common mistake, not a guarantee.

**Stale names.** `session_start.py`'s three "deferred-test roll" comments renamed to /plan's below-line revisit; `CLAUDE-TEMPLATE.md`'s claim to be "Updated on plugin reinstall" corrected, since nothing updates it then; `migrate-checklist.md`'s claim that session_start tops up CLAUDE.md corrected to /plan.

The empty-Files denial text also understated its own permitted set and routed findings to the retired "Captures" name; both fixed in the hook's message. That is a text change only — no behaviour moved.

Two limbs were split out at processing into their own items, because they needed code changes rather than documentation and one carried a privacy risk that would have been invisible inside a doc sweep: [session-start-writes-payload-sample-into-repo] and [editing-state-closing-marker-ignores-adoption].

Hook schema checks pass after the changes.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/docs-b/plan.md`, `plugin/si-plugin/docs-b/next.md`, `plugin/si-plugin/docs-b/migrate-checklist.md`, `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md`, `plugin/si-plugin/hooks/pre_tool_use.py` (denial text), `plugin/si-plugin/hooks/session_start.py` (comments)
**Routed to Captures:** none
