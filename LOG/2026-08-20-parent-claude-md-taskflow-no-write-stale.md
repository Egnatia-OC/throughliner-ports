# b485ee3 — The parent-folder Taskflow rule: one owner, the right path, and the INBOX exception written in

Three faults sat in one paragraph, found by reading both copies rather than the version pasted into a session. The rule — "Read Taskflowapp freely from here to answer questions or check state. Do not write to it" — lived word for word in `My Drive/CLAUDE.md` and in `Taskflow Planning/CLAUDE.md`, and both load into every session opened in this project. It needed the user's INBOX exception written into it, or every future session would read a flat prohibition and stop exactly where this one did. Both copies named a path that is not this machine's — one a `C:\Users\Alex\Desktop\...` layout, the other a `G:` drive. And two copies of one rule with no declared relationship means an edit to either can silently diverge.

Measured at processing, the duplication turned out to be total rather than confined to that paragraph: both files were 17 lines and byte-identical apart from the path string. The Drive-root copy describes folders three levels beneath it, so it was misfiled as well as duplicated — orientation for the Taskflow Planning folder, sitting at the top of the whole Drive. That is what settled the fix as one canonical owner rather than a pointer.

Neither file is under version control — My Drive is not a git repository — so write-first's own test returns no, and every edit here was shown before it happened, including the deletion. The two files were diffed first, and differed only at the two lines being corrected, which is what made the deletion safe to recommend. Nothing is orphaned by it: `Desktop/CLAUDE.md` already orients anything opened above this project.

**Also worth recording:** the user asked mid-build whether deleting the Drive-root copy owed a message to the Claude memory project, which owns the global instruction layers. Checked rather than assumed, and the answer was no — that project owns `~/.claude/CLAUDE.md` and the ranked priority list, neither of which this file is, and a grep of its own documents returns no reference to it. So no message was sent and no /setup was run there.

**Files touched:** `Taskflow Planning/CLAUDE.md` (line 11 path corrected to this machine's, line 13 gained the INBOX exception); `My Drive/CLAUDE.md` (deleted). Both outside the repository and outside git.

**Routed to Captures:** [parent-claude-md-version-claim-stale] — the surviving file still calls this project v37 at plugin version 0.37.0, and still uses the pre-rename name. Noticed while editing, filed rather than folded in, since it is a different staleness with a different cause.

Rule gate: not needed — a rule is genuinely amended, and it is not in the method's own text. These are folder-level instructions for one machine, so nothing under `docs-b/`, this project's `CLAUDE.md`, `self-authoring-rules.md` or `rule-maintenance.md` is touched and the mechanical trigger never fires. **That silence is itself a second instance of [gate-trigger-misses-the-audit-checklist]**, noted on that item rather than treated as new here.

Tick: done, confirmed.
