# Routine method-compliance audit checklist

The standing criteria for a periodic compliance audit of the method's own procedure docs — `plugin-behaviour.md`, `setup.md`, `plan.md`, the `next*` family, the `done*` family, and any procedure doc added later.

**What this is for, and how it differs from the authoring heuristic.** [`authoring-heuristic.md`](authoring-heuristic.md) is a per-text check run *once, at authoring time* — you run it over a piece of text before that text ships. This checklist is the *corpus-wide periodic sweep*: you run it over docs that already shipped, to catch what drifted or was never checked. The un-hardened tool-use rule that slipped past for so long (the subagent-cost incident, 2026-06-24) is exactly the gap this exists to close — an authoring-time check never re-examines old rules, so without a periodic sweep, a rule authored before a standard existed never gets held to it.

It is a dev artifact. It audits the method's own docs, so it is host-only — not shipped in the plugin package, no FAQ, no SPEC entry — the same status as the authoring heuristic it builds on.

Run all three lenses over each doc in scope. One read of the doc serves all three. Findings route to Captures for a later /plan to scope — an audit produces findings, not edits to the docs it reads.

## Lens 1 — 4.8 authoring-compliance

Apply the seven points in the **4.8 — the authoring pass** section of [`authoring-heuristic.md`](authoring-heuristic.md) to each doc. They are the single source of truth — read them there, don't re-list them here, so the two never drift. In summary, they cover: quantified targets over adjectives, a positive exemplar of the wanted output, lead-with-the-decision, scope stated in words, the verbosity pattern named with its replacement, action-not-prohibition framing, and the guard against over-terseness.

The authoring heuristic is written for a single piece of text at authoring time. Reading it corpus-wide adds one question it doesn't ask: **is the rule held to its own standard consistently across docs?** A rule hardened in one doc but cited loosely in another, an exemplar present in one step and missing from its sibling — that inconsistency is a finding even when each instance reads fine alone.

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

Two reporting disciplines apply (canonical statement in `docs-b/next-audit.md`'s Compile findings): before reporting a rule as *missing*, search the corpus — "absent entirely" and "present elsewhere but unsignposted" are different findings with different fixes; and before reporting already-shipped work as *broken*, reconcile with the LOG's record of it being verified.
