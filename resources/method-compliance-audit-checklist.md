# Routine method-compliance audit checklist

The standing criteria for a periodic compliance audit of the method's own procedure docs — `plugin-behaviour.md`, `setup.md`, `plan.md`, the `next*` family, the `done*` family, and any procedure doc added later.

**What this is for, and how it differs from the authoring gate.** [`self-authoring-rules.md`](self-authoring-rules.md) is a per-rule check run *once, at authoring time* — you run it over a rule before that rule ships. This checklist is the *corpus-wide periodic sweep*: you run it over docs that already shipped, to catch what drifted or was never checked. The un-hardened tool-use rule that slipped past for so long (the subagent-cost incident, 2026-06-24) is exactly the gap this exists to close — an authoring-time check never re-examines old rules, so without a periodic sweep, a rule authored before a standard existed never gets held to it.

It is a dev artifact. It audits the method's own docs, so it is host-only — not shipped in the plugin package, no FAQ, no SPEC entry — the same status as the gate it builds on.

Run all three lenses over each doc in scope. One read of the doc serves all three. Findings route to Captures for a later /plan to scope — an audit produces findings, not edits to the docs it reads.

## Lens 1 — self-authoring compliance

Apply the four parts of [`self-authoring-rules.md`](self-authoring-rules.md) — admission, eviction, distribution, wording — to each doc. That document is the single source of truth; read the tests there rather than re-listing them here, so the two never drift.

Read corpus-wide, the gate asks things it can't ask one rule at a time:

- **Admission, retroactively.** Which rules here would not be admitted today? A rule with no pointed-to failure, one Claude follows unprompted, one that applies to only some sessions but is always loaded.
- **Eviction debt.** Where does a rule sit alongside the earlier version it was meant to supersede? Consolidation that never repealed its priors is the signature.
- **Distribution.** Which always-loaded rules are reference material that could be fetched on demand — and, the reverse error, which fetched material is a standing behavioural rule a session would never know to look for?
- **Rationale placement.** Which operative statements still carry their why inline, and where should it go — the shipped FAQ if a consumer would want it, the deciding LOG entry if it's an authoring decision? When moving one, check the clause isn't *stating* a rule while arguing for it.
- **Consistency.** Is a rule held to its own standard across docs? Hardened in one doc but cited loosely in another is a finding even when each instance reads fine alone.

**Eviction has to happen in the run, not as a follow-up.** An audit that reports and removes nothing reproduces the failure it exists to fix.

## Lens 2 — tag placement

Each procedure step carries the response-shape tag that fits what it does (`[SILENT]` / `[BRIEF]` / `[DISCUSS]` / `[PROMPT]` / `[SEQUENCE]`, defined in plugin-behaviour.md). Check each step for three failure modes:

- **Missing** — a step that produces output (or withholds it, or waits, or sequences) but carries no tag, so its output behaviour is left to chance.
- **Wrong** — a tag that fights what the step does: `[SILENT]` on a step that must ask the user, `[DISCUSS]` on pure internal bookkeeping, `[BRIEF]` on a genuine decision point that needs room.
- **Prose where a tag belongs** — a step that describes its output behaviour in a sentence ("keep this short," "don't say much here," "stop and wait") instead of carrying the tag that encodes it. The tag is the mechanism; prose substitutes are what the tags exist to replace.

## Lens 3 — narration drift

Check what the doc causes Claude to *say to the user* against the communication rules in plugin-behaviour.md. Three drift patterns:

- **Background vocabulary in user-facing narration** — a structural or bookkeeping term from plugin-behaviour.md's Vocabulary list (loop, Step N, gate, pre-flight, slug, "processed/unprocessed captures," "staleness sweep," "hash backfill," and the rest) leaking into text the user reads. Background terms belong in the procedure prose Claude reads, never in narration to the user.
- **Menu where a recommendation was due** — the doc steering Claude to lay out flat options ("file it, drop it, or commit now?") at a moment it actually has a preference, instead of leading with the recommendation and offering the alternatives as fallback (plugin-behaviour.md Dependency ownership narration; the spectrum-not-flat-list rule).
- **Multi-finding openings that should consolidate** — a doc that fires several scans, watches, or narrations at one skill opening (a /plan read-state, a /next pre-flight, a /done close-out) without consolidating them into one narration, against the consolidate-the-scans rule in plugin-behaviour.md.

## Output

Findings to Captures, one per drifted spot — name the doc, the step or rule, the lens, and what drifted. No edits to the audited docs; the fixes get scoped in a later /plan that processes the findings.
