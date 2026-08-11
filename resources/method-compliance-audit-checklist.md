# Routine method-compliance audit checklist

The standing criteria for a periodic compliance audit of the method's own procedure docs — `skill-nonspecific-rules.md`, `setup.md`, `plan.md`, the `next*` family, the `done*` family, and any procedure doc added later.

**What this is for, and how it differs from the authoring gate.** [`self-authoring-rules.md`](self-authoring-rules.md) is a per-rule check run *once, at authoring time* — you run it over a rule before that rule ships. This checklist is the *corpus-wide periodic sweep*: you run it over docs that already shipped, to catch what drifted or was never checked. The un-hardened tool-use rule that slipped past for so long (the subagent-cost incident, 2026-06-24) is exactly the gap this exists to close — an authoring-time check never re-examines old rules, so without a periodic sweep, a rule authored before a standard existed never gets held to it.

It is a dev artifact. It audits the method's own docs, so it is host-only — not shipped in the plugin package, no FAQ, no SPEC entry — the same status as the gate it builds on.

**What triggers a sweep.** The rule-lifecycle board's **AUDITED** signal, which fires when the always-loaded rule-statement count computed by [`rule_signals.py`](rule_signals.py) is over the ceiling. Being over the ceiling *is* the reason to sweep — rules accumulated past what a session can hold are what these three lenses look for — so the trigger needs no machinery of its own and no number of its own.

The obvious alternative, a sweep every N sessions, was rejected twice over: N would be a bare number with no derivation, which the authoring gate now bans; and a periodic duty is the post-legislative-scrutiny shape the research condemns, which achieved 7.6% coverage of eligible Acts. Before this, the sweep had no trigger at all and ran only when a /plan happened to file an `[audit]` item, which is how the corpus reached ~218 before anyone counted.

**The gap this leaves, stated rather than discovered.** Below the ceiling no sweep ever fires, so drift that is *not growth* — a rule going stale, a prohibition that should have been an action — goes uncaught until the corpus grows across the line. That hole belongs to the board's MAINTAINED signal, which watches for near-duplicate rules independently of the count.

Run all three lenses over each doc in scope. One read of the doc serves all three. Findings route to Captures for a later /plan to scope — an audit produces findings, not edits to the docs it reads.

## The instruction count — run this first

The gate's binding limit is a **count of instructions**, not a word count, so a sweep that doesn't produce a number can only produce opinions: "evict what fails admission" has no target and no stopping rule without one. Count before disposing of anything.

**Scope the count to the always-loaded corpus.** That is `skill-nonspecific-rules.md` plus, in the dev project, `CLAUDE.md`. The skill docs (`plan.md`, `next.md`, `done.md`, `setup.md` and the flavor families) are excluded: they load only when their skill runs, and the ceiling is about what competes for attention in every session. Audit them under the three lenses below; don't count them against the ceiling.

**Counting rule.** One instruction per discrete directive Claude must follow — a bolded rule statement, a bullet, or a decision block. Descriptive prose, rationale and worked examples score zero. Count per section and record the section totals, not just the sum: the sum tells you whether there is a problem, and the section totals tell you where it is.

**Report the split by audience, not just the total.** A consumer loads only `skill-nonspecific-rules.md`; the dev project loads both. Those are two different numbers against the same ceiling, and collapsing them hides which one is actually over.

### Dispositions

Every rule the inventory touches gets one:

```
keep                    admissible today, correctly placed, correctly worded
recast                  amendments have accreted past legibility; repeal the
                        whole thing and replace with one new text
consolidate-and-repeal  merge the rules on a topic into one AND delete the
                        priors — the repeal is the essential half
evict                   delete outright: fails admission, or is stale
relocate-rationale      the rule stays; its why moves out (consumer-facing why
                        to the shipped FAQ, authoring decision to its LOG entry)
```

`relocate-rationale` saves no slot and is still worth doing: the ceiling counts instructions, but per-rule weight is the other half of what makes a corpus hard to follow.

**Redistribution is a disposition the gate deliberately does not list, and it needs its own justification each time.** Moving a rule to a fetched doc removes it from the count without removing it from the method, which is how bloat gets hidden rather than cut. It is legitimate only where the rule has a trigger a session cannot miss — a word the user says, a hook that surfaces something. Record that reasoning per rule, never once for a batch.

### Two things learned running this (2026-08-09, the first inventory)

- **The eviction list is the audit's output, and it goes into the queue as build work cleared to run — not as findings awaiting a later planning session.** An audit that reports and removes nothing reproduces the failure it exists to fix, but the fix is not cramming a corpus rewrite into a review pass. Approve the list item by item during the run.
- **An `[audit]` item that names a document to write into contradicts the audit contract and must be surfaced, not followed.** This checklist is named as the criteria home, which reads as a doc-write. The resolution that worked: the *findings* went to the queue, and only the *method* — this section — was written here.

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

Each procedure step carries the response-shape tag that fits what it does (`[SILENT]` / `[BRIEF]` / `[DISCUSS]` / `[PROMPT]` / `[SEQUENCE]`, defined in skill-nonspecific-rules.md). Check each step for three failure modes:

- **Missing** — a step that produces output (or withholds it, or waits, or sequences) but carries no tag, so its output behaviour is left to chance.
- **Wrong** — a tag that fights what the step does: `[SILENT]` on a step that must ask the user, `[DISCUSS]` on pure internal bookkeeping, `[BRIEF]` on a genuine decision point that needs room.
- **Prose where a tag belongs** — a step that describes its output behaviour in a sentence ("keep this short," "don't say much here," "stop and wait") instead of carrying the tag that encodes it. The tag is the mechanism; prose substitutes are what the tags exist to replace.

## Lens 3 — narration drift

Check what the doc causes Claude to *say to the user* against the communication rules in skill-nonspecific-rules.md. Three drift patterns:

- **Background vocabulary in user-facing narration** — a structural or bookkeeping term from skill-nonspecific-rules.md's Vocabulary list (loop, Step N, gate, pre-flight, slug, "processed/unprocessed captures," "staleness sweep," "hash backfill," and the rest) leaking into text the user reads. Background terms belong in the procedure prose Claude reads, never in narration to the user.
- **Menu where a recommendation was due** — the doc steering Claude to lay out flat options ("file it, drop it, or commit now?") at a moment it actually has a preference, instead of leading with the recommendation and offering the alternatives as fallback (skill-nonspecific-rules.md Dependency ownership narration; the spectrum-not-flat-list rule).
- **Multi-finding openings that should consolidate** — a doc that fires several scans, watches, or narrations at one skill opening (a /plan read-state, a /next pre-flight, a /done close-out) without consolidating them into one narration, against the consolidate-the-scans rule in skill-nonspecific-rules.md.

**Not a target: a purpose clause.** Where a sentence is welded into a rule's operative text because the rule cannot be applied correctly without it, that sentence *is* the rule, not rationale riding it. An eviction sweep must leave it alone. The test in reverse: delete it and read what remains — a complete instruction means it was rationale, an unfinished one means it was operative.

## Output

Findings to Captures, one per drifted spot — name the doc, the step or rule, the lens, and what drifted. No edits to the audited docs; the fixes get scoped in a later /plan that processes the findings.
