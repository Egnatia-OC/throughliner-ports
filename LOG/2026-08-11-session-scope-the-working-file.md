# 7c9922a — Working files are per session, so a second session stops inheriting another's scope-lock [session-scope-the-working-file]

Split out of [isolation-model-is-not-ours-to-choose] at the user's instruction. The finding was recorded on 2026-08-10 as Finding 2 of [concurrent-session-support]; the separability argument is Claude's.

**The defect, live under every isolation model.** `_build.md` and `_plan.md` sat in the project root, making them project-level rather than session-level. The behaviour rules explicitly permit a planning session in one chat alongside a build in another — so the planning session saw `_build.md` present, concluded it was inside a build, and `pre_tool_use.py`'s scope-lock applied the *build's* file list to writes that session never agreed to. Every check keying on the file's existence was asking "is there a build" when it meant "is there a build **for this session**".

**Why it was split from the isolation question rather than waiting on it**, which is the decision worth preserving: the isolation design had reversed direction twice and was genuinely unsettled, and this fix is correct whichever way it lands, because the question it repairs is about *this session* and never about the tree. Splitting meant one clearly-right build landed regardless.

**Both build-time questions were answered by following existing convention rather than inventing.** The name is `_build-<session-id>.md`, reusing the editing marker's `<name>-<safe id>` shape and its sanitiser verbatim — a second convention for the same job is how two things that must agree drift apart — and it stays in the project root, because that is where the docs and the FAQ already tell users to look. A per-session directory would have moved it for no gain.

**The leftover question got the better answer, and testing is what surfaced why it mattered.** Project-level working files were at least self-evidently stale; a per-session one is invisible to every session but its own. So a leftover is surfaced at session start and never deleted, because it can hold the only record of what a crashed session did — which is exactly why /next writes progress to it.

**A migration gap found by testing and closed without a format-epoch bump.** With only the new names recognised, an existing project's legacy `_build.md` would have become invisible to every session at once — orphaned rather than merely stale, which is worse than the problem being fixed. The leftover scan now recognises the two old names, so no migration is needed. Verified: a session with a different id reports "Ready" instead of inheriting the build, and surfaces the legacy file as a leftover.

The ripple was traced by grep before building, as the hook-enforced-format rule requires: 18 files, 90-plus references, all reworded to "the build/planning working file" with the name pattern stated once per doc. `SPEC.md` was checked and is genuinely absent from the list — it names neither file. The FAQ *does*, so its two entries were rewritten rather than dispositioned away.

**Files touched:** `plugin/si-plugin/hooks/pre_tool_use.py`, `session_start.py`, `post_tool_use.py`; `plugin/si-plugin/docs-b/` (next, next-build, next-audit, done, done-build, done-audit, done-plan, plan, setup, skill-nonspecific-rules); `plugin/si-plugin/templates/faq-template.md`, `faq-index-template.md`; `FAQ/faq.md`, `FAQ/index.md`; `CLAUDE.md`
**Routed to Captures:** none from this item
