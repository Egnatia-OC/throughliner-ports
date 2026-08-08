# Method consistency audit — reusable plan

> Reusable plan, sibling to `overnight-blitz-plan.md`. First full run 2026-08-07
> (report: `LOG/2026-08-07-pre-compression-doc-audit.md`; findings filed as the
> 15 `[audit-…]` captures). Amend in place after each future run.

Two modes, one pass list:

- **Differential** — the routine mode. Runs once per branch cycle, at **soak-end,
  immediately before the merge to main**, over the span `main...HEAD`. This is
  the pre-merge gate: main only ever receives a reconciled state. **It runs as
  its own queued `[audit]` work item, never inline in a planning chat** — see
  *This audit's queue-item form* below.
- **Full corpus** — the occasional mode. Every doc, every pass, regardless of
  span. Reserved for big boundaries: before a compression pass, after a large
  redesign, or when differential runs keep finding things. Heavy — the first run
  took an eight-subagent fan-out.

**Where this sits in the branch cycle** (united with the overnight blitz,
decided 2026-08-07):

```
branch → blitz builds → soak → DIFFERENTIAL AUDIT — a queued [audit] item,
                                run through /next over the whole branch span
       → reconcile: /plan processes the audit's findings, /next builds the
                    repairs it cleared
       → merge → branch again
```

The audit runs at soak-end, not blitz-end, because soak-day work lands on the
branch after a blitz-night audit would have run — an audit the merge outruns is
muddied by construction. At soak-end the span covers blitz plus soak and nothing
lands after it but the merge. Leakage is tolerable by design: the differential
is span-based, so anything a merge lets through is covered by the next cycle's
span, with the authoring-time ripple-grep ([ripple-grep-for-rule-changes], once
built) as the first line. The rhythm shortens the distance between a divergence
and its detection; it does not promise to catch everything once.

## Ground rules (learned on the first run — the brief that seeded it had three
## wrong premises, each of which would have produced false findings)

- **Report findings only. Edit nothing.** Findings become captures in
  QUEUE.md's Unprocessed; the full report becomes a LOG entry. Repairs
  consolidate into grouped capture items; genuine design calls file standalone
  so they can be ordered or dropped on their own.
- **There is one docset, `docs-b/`, and it is the whole audit surface.** Docset A
  (`docs/`) was retired 2026-08-08 and its folder is gone, so the old
  "audit B only, never diff A against B" instruction has nothing left to
  exclude. What replaces it is a plain error check: **any reference resolving
  into `docs/` is now a finding**, with no exceptions — the `skills/*/SKILL.md`
  files used to be the deliberate exception, because a session-start directive
  rewrote their paths at runtime, and they now name `docs-b/` directly like
  everything else. A surviving `docs/` path points at nothing.
- **Verify the brief's premises against the repo before running**, whoever wrote
  it. Handoff-claim provenance applies to audit briefs too.
- **Verify before shipping:** every finding's cited lines are re-read by the
  compiling session; a finding that doesn't survive the re-read is dropped, not
  softened. Independent re-discovery by two auditors counts as corroboration.
- **Dedupe against the queue before filing** — findings already captured under
  an existing slug are referenced, not re-filed.
- **Compare, don't explain.** Whether two passages agree, never why either was
  written. "This looks wrong and I can't account for it" is an expected output.
- **No quotas.** A clean pass is the finding (the blitz plan's lesson holds
  here too).
- **Search before reporting something missing.** "Absent entirely" and "present
  elsewhere but unsignposted" are different findings with different fixes, and
  they are indistinguishable without the search.
- **Reconcile with the LOG before reporting already-shipped work as broken.**
  The LOG carries the record of it being verified; a finding that contradicts
  that record has to account for the contradiction rather than ignore it.

## The passes

Run one criterion across the whole in-scope set, then the next — never file by
file applying everything at once.

1. **Stale references.** Every named field, setting, marker, tag, or filename,
   checked against what setup.md scaffolds and the hooks parse. Both
   directions: referenced-but-never-defined, and defined-but-never-referenced.
2. **Cross-doc pointer integrity.** Resolve every "see X's Y-rule" style
   pointer; report targets that don't exist, were renamed, or no longer say
   what the pointer claims. Cited rule-*names* that grep to nothing are
   findings even when the content exists unnamed.
3. **Duplicate statements of one rule.** Divergence matters more than
   duplication; say which site reads as canonical.
4. **Multi-site rules.** Rules naming two or more firing sites — check every
   named site still exists and describes the same rule.
5. **Premise-bearing factual claims.** List claims about the app, harness,
   links, CLI, OS, or model behaviour that rules rest on. List for human
   verification — never verify in-audit.
6. **Direct contradictions.** Two rules incompatible at one concrete moment.
   Quote both sides; clear compatible readings rather than stretching.
7. **Orphan rules and orphan files.** For standing behavioural rules,
   "no doc points at it" is NOT orphanhood (they're resident by design) — a
   rule is orphaned only if it governs a moment no procedure reaches.
8. **Terminology drift.** Two internal names for one thing, unanchored.
   Plain-language substitutions declared by the vocabulary rules and
   migrate-checklist are intentional, not findings.
9. **Hook behaviour vs docs — both directions.** Read the scripts in full.
   Implemented-but-undocumented is the direction nobody looks for.
10. **Retirement completeness.** LOG-driven: extract what each removal entry
    says went, grep the tree for survivors, verdict COMPLETE/INCOMPLETE, rank
    survivors live vs inert. Also the reverse: looks-retired with no LOG entry.

**Passes 11 and 12 are FULL-CORPUS ONLY.** Passes 1–10 ask whether the documents
agree with each other and with the code; these two ask whether the documents are
*well-made*. That is a quality sweep over standing text, not a question a span
can scope, so a differential run skips them. Both were folded in from the retired
`method-compliance-audit-checklist.md` on 2026-08-08.

11. **Response-shape tag placement.** Each procedure step should carry the tag
    that fits what it does (`[SILENT]` / `[BRIEF]` / `[DISCUSS]` / `[PROMPT]` /
    `[SEQUENCE]`, defined in plugin-behaviour.md). Three failure modes:
    **missing** — a step that produces output, withholds it, waits, or sequences
    but carries no tag, so its output behaviour is left to chance; **wrong** — a
    tag fighting what the step does, `[SILENT]` on a step that must ask,
    `[DISCUSS]` on pure bookkeeping, `[BRIEF]` on a decision point needing room;
    **prose where a tag belongs** — a step describing its output behaviour in a
    sentence ("keep this short", "stop and wait") instead of carrying the tag
    that encodes it. The tag is the mechanism; prose substitutes are what the
    tags exist to replace.
12. **Narration drift.** Check what each doc causes Claude to *say to the user*
    against plugin-behaviour.md's communication rules. Three patterns:
    **background vocabulary leaking into user-facing narration** — a structural
    or bookkeeping term (loop, Step N, gate, pre-flight, slug, hash backfill and
    the rest) appearing in text the user reads, when it belongs only in the
    procedure prose Claude reads; **menu where a recommendation was due** — the
    doc steering Claude to lay out flat options at a moment it actually has a
    preference, instead of leading with the recommendation and offering the
    alternatives as fallback; **unconsolidated openings** — a doc firing several
    scans or narrations at one skill opening without consolidating them into one,
    against the consolidate-the-scans rule.

**A third lens returns here when it has something to point at.** The retired
checklist's Lens 1 applied the authoring heuristic's per-model pass corpus-wide.
That pass was deleted when docset A retired
([authoring-heuristic-has-no-live-model-pass]), so the lens has nothing to check
against. If a 5-series authoring pass is ever written, it comes back as pass 13,
asking the corpus-wide question the per-text check cannot: **is the rule held to
its own standard consistently across docs?** — a rule hardened in one doc but
cited loosely in another is a finding even when each instance reads fine alone.

**Differential scoping:** from `git diff --name-only $(git merge-base main
HEAD)..HEAD`, list the rules/formats/names the span's commits touched; run
passes 1, 2, 3, 4, 6 over those rules' statement sites corpus-wide (a touched
rule's *other* sites are the point), pass 9 if hooks changed, pass 10 if the
span retired anything. Passes 5, 7, 8 are full-corpus concerns — skip unless
the span obviously implicates them. Passes 11 and 12 are full-corpus only and
are always skipped here.

## Scope

The target at `plugin/si-plugin/` — docs-b/, skills/, templates/, hooks/
(hooks.json + three scripts), scripts/, output-styles/, .claude-plugin/ — plus
this repo as the representative project (CLAUDE.md, QUEUE.md, SPEC.md,
resources/, FAQ/). LOG/ is the retirement record, not an audit target.
Taskflowapp excluded (frozen old plugin; write-locked).

## Execution and reporting

- Full mode: subagent fan-out (one auditor per pass or pair, ~8 agents) with
  the corrected premises baked into every prompt; the main session verifies and
  compiles. Ask before spawning, per the behaviour rules.
- Differential mode: run through /next as its own `[audit]` work item, in one
  session, reading the changed files in full; fan out only if the span is
  unusually wide, and ask first.
- Output: full report → a LOG entry file; findings → `[audit-…]` captures in
  Unprocessed (repairs grouped, design calls standalone); the reconcile
  /plan + /next clears the repairs before the merge is offered.

## This audit's queue-item form

**The differential audit is a queued `[audit]` work item, run through /next. It
is never run inline inside a planning chat.** /plan's role is to seed the item at
rebranch, clear it at soak-end, and then process the findings the run brings
home — not to be the run.

Seeded below the readiness line at rebranch (CLAUDE.md's soak-end sequence, the
"branch again" step), lifted at soak-end:

```
#### [audit] Differential consistency audit over this branch's span [differential-audit-<cycle>]
Seeded at rebranch. Runs `resources/consistency-audit-plan.md` in differential
mode over `main...HEAD`. Below the line until soak-end; lift-condition: the
branch has stopped taking new work and the merge is the next thing due.
This is the pre-merge gate — main only ever receives a reconciled state.
```

**Why it must be a run and not a chat, from the failure that settled it.** A
differential audit was run inline in a /plan session on 2026-08-08 and the user's
verdict on the result was *"there was no audit of any shape, just one small thing
was built."* Two things went wrong and the second is the deeper one. **Invisible:**
an inline run produces no `[audit]` item, no LOG entry at the time, and no sense
that the cycle's gate fired — the user approved "keep and clear it" believing the
*audit* was being queued, when what was queued was only its repair. **Shallow:**
the inline run never read the three changed hooks in full (pass 9 as written) and
skimmed the pointer and duplicate passes. "Cheap enough to run inline" licensed a
light check to wear the audit's name; compression of effort followed compression
of form.
