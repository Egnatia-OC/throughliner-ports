# 4f5e167 — A stale document format now halts the session at start and points at /setup, with a format epoch kept deliberately separate from the plugin version

The migration machinery already existed — /setup re-scaffolds on drift and loads `migrate-checklist.md`, and the SA consumer project validated that it works. What was missing was any way for a project to *find out* it needed migrating. Migration happened only if the user thought to run /setup, and Alex's reason for changing that stands: a project silently on an old format wastes every /plan and /next reasoning over stale scaffolding, and the person least able to spot the drift is the non-coder the method is for.

The signal is a **format epoch**, and its separation from the plugin version is the whole design rather than a detail. The version bumps at every release and most releases change no format, so a version check cries wolf — which is exactly why the user-facing "your project is behind" warning had already been moved off it and onto presence-of-scaffolding. The epoch says something a version cannot: not "something shipped" but "your files are on an older shape". Detection by inspecting the documents' structure was rejected for the opposite reason — it guesses, about files users legitimately hand-edit.

The halt sits **above the red-flag scan** in the payload, and that ordering is deliberate rather than a ranking of importance. Every scan below it reads the project's documents, and a stale project's documents are in a shape those readers were not written for; a red-flag scan that cannot parse its input reports nothing, which is indistinguishable from "no risks found". The user can override and carry on — it is their project — and is told once that results may be unreliable until the migration runs.

Two smaller decisions worth recording. An adopted project with no epoch marker is treated as epoch 1 rather than as an error, because no migration ever reaches every project and an unreadable file must never be the thing that decides a project is fine. And the epoch is declared as a constant in `session_start.py` rather than as a key in the plugin manifest: whether the manifest tolerates unknown keys is an external fact that could not be confirmed in-session, and the epoch has exactly one reader, so declaring it where it is read avoids the question entirely.

/setup writes the marker **last** among its migration edits, once the conversions have landed. Writing it early would clear the warning while the project was still on the old shape, and nothing would ever raise it again.

The self-hosting half is the piece that makes the whole thing live: a build that changes the document format must bump the epoch, or the halt never fires and every consumer project keeps running on the old shape. That rule now sits alongside the README-sync and SPEC-sync triggers, and it carries an instruction to extend the epoch's history comment — a bare number nobody can date is a number nobody dares change.

Verified before closing: an epoch-1 project halts, the halt is the first line of the payload, and writing the marker clears it.

**Files touched:** `plugin/si-plugin/hooks/session_start.py` (`FORMAT_EPOCH`, `FORMAT_EPOCH_FILE`, the halt, the missing-scaffold entry suppressed while the halt fires); `plugin/si-plugin/docs-b/setup.md` (migration step 3a and a scaffold-file entry); `CLAUDE.md` (the epoch-bump rule); `SPEC.md`; `README.md`; `plugin/si-plugin/templates/faq-template.md` and `faq-index-template.md`; `.si-format-epoch` (new, scope addition approved mid-build).

**Routed to Captures:** none from this item.

FAQ: updated — new consumer entry "A session stopped and said my project's files are on an 'older format'. What is that, and is my work at risk?", plus its index line.
