# [HASH] — /setup run after an eight-version gap, and it converted nothing it should have

The `[freeform]` item [setup-outstanding-here] is closed. `session_start` had reported the plugin moving 1.12.0 → 1.20.0-test13 since this project was last set up, and the notice had been surfaced at every opening and acted on by nobody. The item was tagged `[freeform]` because /setup refuses outright while a build is in progress, so it cannot execute inside a run — the constraint was the session, not the capability.

**The run itself.** The session opened on a format halt: project documents on format 3 against the plugin's 4. Step 0 found no build working file. The scratchpad marker was written so the safety check would permit /setup's writes, and deleted at the end. Everything on the scaffold list was already present — the queue two-section, both folders, the FAQ, `resources/research/`, `INBOX/` with its archive, and a `.gitignore` already carrying both required lines. No REGISTRY file to retire. The retired-terms step found six occurrences of "batch" in this project's own `CLAUDE.md` and reported them without editing, which is what that step is for. Two markers were written: `.throughliner-version` to 1.20.0-test13 and `.throughliner-format-epoch` to 4.

**What went wrong, found later in the same chat and only because the user asked a question about something else.** Writing the epoch marker is what silences `session_start`'s migration halt, and this run wrote it having converted nothing. /setup's migration step loads `migrate-checklist.md` only when it finds a queue in the **old multi-section shape** — the Red flags / Batches / Parked / Deferred tests layout. This queue is two-section, so the checklist was skipped, and with it the checklist's own "Epoch 4 — build blocks on cleared work" section. Two-section is what every project has had since epoch 3, so that gate now tests for a shape no live project still has.

The close therefore reported a clean migration that had not happened. The project's marker asserts format 4 while its cleared items are on format 3's shape, and because the marker is what the halt reads, nothing will raise it.

**The diagnosis is [setup-migration-gate-is-epoch-3-shaped]** and the conversion this run owed is [convert-cleared-items-to-build-blocks]. Both were kept and cleared in the same chat.

**One thing not claimed:** the version top-up half of this run was correct and is not in question. The scaffold checks, the marker rename path, the retired-terms report and the `.gitignore` reconciliation all behaved as specified. What failed is a single condition deciding whether the epoch migrations run at all.

**Queue changes:** [setup-outstanding-here] removed from Processed as complete.
**Work processed:** closed — [setup-outstanding-here].
