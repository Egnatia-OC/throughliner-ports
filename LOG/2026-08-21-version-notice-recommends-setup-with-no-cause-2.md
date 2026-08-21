# [HASH] — The version-change notice is deleted, and /next's guard retargeted onto the signals that actually mean /setup is outstanding

Build entry. The planning entry that processed this item is
`2026-08-21-version-notice-recommends-setup-with-no-cause.md`.

**Why this was worth doing.** The user raised it with two screenshots of sessions
halting after a test12 → test13 update, and the report that all her projects were
at halt — she was running /done, /setup and /plan again midway through sessions on
every update. The diagnosis was Claude's, read from the code: the format check was
never what fired. `session_start.py` halts on a stale epoch only where the recorded
number is below `FORMAT_EPOCH`, and this project records 4 against a declared 4, so
it was silent throughout. What fired was a separate flag comparing
`.throughliner-version` against the installed plugin, emitting a notice that an
update had been installed and that /setup wanted a session of its own. Only /setup
writes that marker, so the notice repeated at every session opening until /setup
ran — and since she rezips at every run, it was a per-run tax. `CLAUDE.md` had
predicted exactly this when it made the epoch deliberately separate from the
version, on the ground that a version check would cry wolf and be learned past. The
epoch was built to replace the version check; the version check was left running
beside it.

**What was built.** The notice block and its `version_mismatch` flag are deleted
outright from `session_start.py`. The comment in their place says no version
comparison is made and names what does mean /setup is outstanding — a stale epoch,
or a document or setting reported missing. The installed version is still reported
at every opening, which is why deleting the notice costs nothing: a factual "the
version changed" line told the user what the opening had already told them.

The ripple reached one further site, traced by grep at processing rather than
discovered here. `next.md`'s run-presentation guard fired on the same false
equation — version-behind means /setup-outstanding — so it is retargeted onto the
epoch and missing-document signals. Its second condition (an item in this run names
a file /setup rewrites from a template) and its drop-from-this-run-only behaviour
are untouched.

**Rewording the notice was refused** rather than merely not chosen: a line that
fires every session until /setup runs is noise whatever it says, and the repetition
was the defect. **Removing the guard along with the notice was refused too** — its
purpose is sound and only its trigger was wrong.

**Verification.** A new suite, `resources/testing/test_session_start_version_notice.py`,
pins both halves: a version-only difference with the epoch current and nothing
missing produces no notice and no /setup line, AND a stale epoch still halts while a
missing document is still reported. That matched pair matters — a repeal that also
silenced the real checks would be the worse defect. Five tests, all passing. The
suite reads `FORMAT_EPOCH` from the hook rather than hardcoding it, so it will not
go stale silently the first time a build bumps the epoch.

`grep version_mismatch` in `session_start.py` returns nothing. `FAQ/faq.md` and
`FAQ/index.md` are byte-identical to their templates.

**Files touched:** `plugin/throughliner/hooks/session_start.py`,
`plugin/throughliner/docs/next.md`,
`resources/testing/test_session_start_version_notice.py` (new),
`plugin/throughliner/templates/faq-template.md`,
`plugin/throughliner/templates/faq-index-template.md`, `FAQ/faq.md`, `FAQ/index.md`.

**Routed to Captures:** none from this item.

**FAQ: updated** — new entry, "The plugin updated to a new version. Do I need to do
anything?", naming the three things that genuinely ask for /setup and recording that
the old behaviour fired on any version difference at all. It fires on its own test:
what the user *does* changes, from closing a session and running /setup on every
update to doing nothing.

Rule gate: not needed — no rule is authored or amended in the method's own rule text. The change removes a hook's unfounded recommendation and retargets one procedure-doc trigger onto signals that already exist.

Depth: short. Built and confirmed.
