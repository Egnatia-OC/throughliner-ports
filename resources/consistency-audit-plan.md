# Method consistency audit — reusable plan

> Reusable plan, sibling to `overnight-blitz-plan.md`. First full run 2026-08-07
> (report: `LOG/2026-08-07-pre-compression-doc-audit.md`; findings filed as the
> 15 `[audit-…]` captures). Amend in place after each future run.

Two modes, one pass list:

- **Differential** — the routine mode. Runs once per branch cycle, at **soak-end,
  immediately before the merge to main**, over the span `main...HEAD`. This is
  the pre-merge gate: main only ever receives a reconciled state. Usually cheap
  enough to run inline in one session.
- **Full corpus** — the occasional mode. Every doc, every pass, regardless of
  span. Reserved for big boundaries: before a compression pass, after a large
  redesign, or when differential runs keep finding things. Heavy — the first run
  took an eight-subagent fan-out.

**Where this sits in the branch cycle** (united with the overnight blitz,
decided 2026-08-07):

```
branch → blitz builds → soak → DIFFERENTIAL AUDIT over the whole branch
       → reconcile (one /plan + /next over the audit's repair captures)
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
- **Audit docset B only.** `docs/` is docset A — the frozen 4.8 fallback, NOT
  retired (retirement proposed and declined 2026-08-05). Never diff A against B.
  The one docs/-related check: report references resolving into `docs/` —
  EXCEPT the five `skills/*/SKILL.md` files, whose hardcoded `docs/` paths are
  the deliberate session-start redirect mechanism.
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

**Differential scoping:** from `git diff --name-only $(git merge-base main
HEAD)..HEAD`, list the rules/formats/names the span's commits touched; run
passes 1, 2, 3, 4, 6 over those rules' statement sites corpus-wide (a touched
rule's *other* sites are the point), pass 9 if hooks changed, pass 10 if the
span retired anything. Passes 5, 7, 8 are full-corpus concerns — skip unless
the span obviously implicates them.

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
- Differential mode: usually inline; fan out only if the span is unusually wide.
- Output: full report → a LOG entry file; findings → `[audit-…]` captures in
  Unprocessed (repairs grouped, design calls standalone); the reconcile
  /plan + /next clears the repairs before the merge is offered.
