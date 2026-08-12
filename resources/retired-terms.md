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
- `CEILING` — the 200-statement rule-corpus ceiling in `resources/rule_signals.py`, retired 2026-08-12; the 150–200 instruction figure it derived from was re-validated against the 5-series and found roughly an order of magnitude too tight, so the board reports growth with no threshold and no verdict
- `Completed [user]-item close (in done.md)` — a section of `done.md`, retired 2026-08-12; the close still exists but lives in `done-plan.md`, which now carries every no-build shape
- `Standalone handmade-work close (in done.md)` — a section of `done.md`, retired 2026-08-12; same relocation to `done-plan.md`
