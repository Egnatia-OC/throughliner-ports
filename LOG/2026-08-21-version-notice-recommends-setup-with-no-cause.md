# 746608f — the cry-wolf halt traced to the version check rather than the format epoch, and the notice scheduled for removal rather than rewording

The user reported that sessions keep halting on a stale-format warning even though the epoch marker is correct, that this happens on every plugin update, and that all her projects were held up by having to run /done, /setup and /plan again mid-session each time. She supplied two screenshots.

**The format check was not what fired, established from the code and from this session's own opening.** `session_start.py` halts only where the project's recorded epoch is below `FORMAT_EPOCH`. The project records 4 and the plugin declares 4, so it stayed silent in both screenshots and here — this session opened with "Project is set up."

**What fires is a separate version check, and it goes off on every release.** A flag compares `.throughliner-version` against the installed plugin and emits a notice saying an update has been installed, that /setup wants a session of its own, and to finish and close what is running first. It says nothing about the documents being wrong. **Both screenshots show Claude reading that notice and narrating it as a format emergency** — claiming the update changed the structure the documents are read in, and that conclusions from the queue could be confidently wrong. The hook never said either thing.

**Only /setup writes `.throughliner-version`, which is why it repeated every session rather than once per update.** Rezip, marker goes stale, every session opens telling her to close what she is running, she complies, the marker updates, the next rezip starts it again. She rezips at every run, so it was a per-run tax — and running /setup was the only thing that silenced it.

**A version change requires nothing.** /setup is called for by the format epoch being behind or by a document or setting missing, both checked separately and both already saying so. `CLAUDE.md` predicted this when it made the epoch deliberately separate from the version, on the ground that a version check would cry wolf and be learned past. The epoch was built to replace the version check; the version check was left running beside it.

**Removal rather than rewording, and the reason it costs nothing.** The installed version is already reported at every session opening unconditionally, so a factual "the version changed" line says what the opening has just said. A line that fires at every session until /setup runs is noise whatever its wording.

**The ripple reached a second site, found by grep rather than from the discussion.** `next.md`'s run-presentation guard fires on the project's recorded version being behind the installed one, so it rests on the same false equation. Its purpose survives and only its trigger was wrong; it is retargeted onto the signals that genuinely mean /setup is outstanding. Nothing else reads the flag — it is defined once and used once, checked rather than assumed.

**SPEC was corrected here**, ahead of the build: a version change now produces no notice and calls for nothing, and the /next guard is described as firing while *setup* is outstanding rather than while an update is.

**Placed first in the cleared region**, ahead of the restyle the user has been chasing, because it is small and it is the only item in the queue that unblocks work in her other projects. She was told the placement and the reason rather than having the order changed quietly, and also told plainly that building it does not silence anything until a rezip and restart carry it into the installed plugin.

**Queue changes:** [version-notice-recommends-setup-with-no-cause] written into Processed at the top of the cleared region; two SPEC sentences rewritten.

**Work processed:** kept — [version-notice-recommends-setup-with-no-cause].

**Routed to Captures:** none.

Rule gate: not needed — no rule is authored or amended in the method's own rule text. The change removes a hook's unfounded recommendation and retargets one procedure-doc trigger onto signals that already exist.

FAQ: updated — the item carries an FAQ entry in its build list, answering what a plugin update requires of the user and that a version change on its own requires nothing. It fires on the trigger's own test: today she closes a session and runs /setup on every update, and after this she does not.
