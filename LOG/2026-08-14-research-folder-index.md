# [HASH] — The research folder gains an index, 54 lines backfilled from each file's own opening

Captured by the user, in her own words: add an index to the research folder, like there is on LOG, so subject matter can be searched without opening files.

The evidence was a corpus with a write path and no read path. `resources/research/` held 54 files. `LOG/` has an index for exactly this reason — one line per entry carrying the artifact and the nature of the change, so a session decides what to open without reading prose. Research had the same shape and nothing.

**Why filenames are not enough, from a miss that had just happened.** A session searched the web for what Claude Code documents about session worktrees. `worktree-isolation-and-desktop-sessions.md` already answered it and would have been caught by a filename scan. But `remote-control-limitations.md` is in the same folder and may bear on the same question, and no scan for "worktree" reaches it. A filename only matches a question phrased the way the file was named; an index line describes what a finding *settles*.

The index is newest-first, one line per file, each carrying the subject it settles and enough of the finding to support an open-or-skip decision, ending in the filename — the same contract `LOG/index.md` states for itself, with the same no-length-cap reasoning, since a line too short to decide on fails at any length. Add dates came from `git log --diff-filter=A` rather than being guessed. Every line was written from the file's own opening rather than from its title, which is the bulk of the work and the whole point: a title-derived index reproduces the blindness it is meant to cure.

Three files carrying supersession or narrowing notes are flagged in their lines, so a session scanning the index meets the correction before it opens the file.

**The item's stated anomaly rested on a wrong premise, and resolving it changed nothing else.** It recorded that `scopelock-independent-implementation` carries no `.md` extension unlike the other 52, and asked whether to rename it. It is not a file at all — it is a **directory** of three (`README.md`, `AGENTS.scopelock.md`, `scopelock.ts`), holding someone else's independent implementation of the same scope-lock idea. So there was nothing to rename. It is indexed as a folder and its line says so. Corrected in the build rather than captured, because the item required only that the index build not silently skip it, and it did not.

The maintenance clause ships with it, or the index rots immediately: filing a finding now writes its index line in the same move. That ships rather than staying host-only, because the triage sends every consumer's research to that folder too, so a consumer's folder grows the same way with the same blindness.

Rule gate: run — admitted as an amendment to the research-filing rule, written as a subordinate clause of it, so no slot is spent. The index itself is an artifact, not a rule, and consumes nothing. Not hookable: nothing marks the moment a finding becomes worth filing.

**Files touched:** `resources/research/index.md` (new, 54 lines), `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (one clause on the research-filing rule).
**Routed to Captures:** none. Note for planning: `[check-existing-research-before-offering]` sits below the readiness line blocked by this item, and its clause must now say *read the index* rather than *list the folder and match filenames*. Lifting it is a planning decision and was left alone.
