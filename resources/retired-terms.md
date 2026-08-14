# Retired terms

Mechanisms, settings and vocabulary the method has retired. Host-only.

**What this file is for.** Retiring a mechanism automatically puts every rule
that still mentions it into question. This list is what makes that mechanical:
`rule_signals.py`'s REPEALED signal reads it and reports live references, so
leaving a stale reference standing produces a visible signal rather than
silence. That is the sunset principle transferred — the default state does the
work — without a calendar, which does not transfer here.

**It is source data, not derived state.** A retirement is an event, recorded
once at the close that retires it. That is why storing it does not contradict
the rule that the board itself is always computed: derived state is computed,
recorded events are stored.

**How a term gets added.** The close that retires something appends a line
here, as part of the same disposition line the rule gate already requires. One
line, one place, carrying both what the gate decided and what was retired.

**Format** — the parser reads exactly this shape, so keep it:

```
- `term` — what it was, and when it was retired
```

**A term is removed from this list only when no live reference remains** and
the retirement is old enough that nobody will reintroduce it. Removing it
early turns the signal off while the problem stands.

## The list

- `plugin-behaviour.md` — the old always-loaded behaviour document, split into skill-nonspecific-rules.md and the per-skill docs on 2026-08-10
- `docset A` — the heavier per-model docset, retired 2026-08-09; the method runs one docset
- `Working mode:` — a project CLAUDE.md field recording how much text to paste inline, retired 2026-08-09
- `Completion mode:` — a project CLAUDE.md field toggling a planning-time sweep for finished user work, retired 2026-08-09
- `Editor:` — a project CLAUDE.md field naming an editor, retired 2026-08-09; the desktop app opens .md in its own viewer regardless
- `authoring-heuristic.md` — the predecessor to the self-authoring gate, retired when that gate replaced it
- `spec-edit batch` — a batch type for SPEC changes, retired; SPEC is a normal doc any batch can list
- `test flavor` — a work-item flavor for test entries, retired; a check Claude can run is part of building and a check only the user can run is a `[user]` item
- `merge cycle` — branch/blitz/soak/differential-audit/reconcile/merge, retired after failing persistently
- `--- Push required before continuing ---` — a positional queue marker, retired with the old readiness model
- `--- Plan session here: ` — a positional queue marker, retired with the old readiness model
- `Blocks:` — a queue field, retired in favour of `Blocked by:` on the held item
- `Depends on:` — a queue field, retired in favour of `Blocked by:` on the held item
- `session-break line` — a manual run bound, retired 2026-08-11; the readiness line is the run bound
- `Wind-down re-scan (/plan's)` — /plan's own full re-scan, retired 2026-08-12; done.md's file-only version runs at every close whatever the session type
- `Step 3: Close out` — /plan's close-out phase, retired 2026-08-12; /done is the only close, and the work-cycle block at plan.md's opening is what now names it
- `Spec-sync gate (build close)` — the build close's sync obligation, retired 2026-08-12; it became a check-against, and the /plan close carries the only sync gate
- `ceiling of 200` — the rule-corpus ceiling in `resources/rule_signals.py`, retired 2026-08-12; the 150–200 instruction figure it derived from was re-validated against the 5-series and found roughly an order of magnitude too tight, so the board reports growth with no threshold and no verdict. **Listed by the phrase naming the number, not as the bare word `CEILING`, which was tried first and fired on the ordinary English word — `plan.md` uses "this ceiling" about an unrelated queue guard. A term that matches correct writing is the cry-wolf failure this list exists to avoid.** The live prose references to the old figure are tracked as [gate-still-declares-the-old-ceiling] rather than by this entry.
- `Completed [user]-item close (in done.md)` — a section of `done.md`, retired 2026-08-12; the close still exists but lives in `done-plan.md`, which now carries every no-build shape
- `Standalone handmade-work close (in done.md)` — a section of `done.md`, retired 2026-08-12; same relocation to `done-plan.md`
- `Planning state:` — a required line in a planning session's LOG entry naming its working file, retired 2026-08-14 with the file itself; the close reads `git diff HEAD -- QUEUE.md` instead
- `close-out phase` — a phase of /plan, retired 2026-08-12 and listed 2026-08-14; /done owns that work and always did, so a user-facing sentence offering to "close out" offers something they cannot do. Every internal use — the build close-out, the audit close-out, the sub-doc headings in `done.md` and its family — is procedure-internal vocabulary and correctly named, so this term is the two-word phrase and never the bare word `close-out`.
- `why-pipeline` — the name of the rationale-carrying mechanism, retired 2026-08-13; it is now **the throughline**, and the plugin is named for it. The mechanism is unchanged; only the name moved, so a live doc still saying `why-pipeline` is stale rather than wrong.

**The identity strings retired on the same day — `sovereign-implementer`, `si-plugin`, `.si-version`, `.si-format-epoch` — are deliberately NOT listed here, and the reason is this list's own cry-wolf rule.** Every one of them has a correct, permanent live use: the marketplace `renames` map must carry the old slug forever or consumers' settings stop migrating, and `session_start.py` and `setup.md` name both old marker files on purpose, as the fallback that recognises a pre-rename project. Listing them would make REPEALED fire on machinery that is working exactly as designed — the same failure the bare word `CEILING` produced. `throughliner` is now the only correct name in new writing; that is enforced by reading, not by this list.
