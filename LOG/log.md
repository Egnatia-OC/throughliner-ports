# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## [HASH] — /plan: 3 batches promoted from audit captures + close-out incongruence flagged

Processed all 12 unprocessed captures — the 11 fac25ab audit findings plus a LOG hash backfill optimization. 8 of the audit findings were mechanical-or-near-mechanical setup.md rewords (Q1-Q4, Step 4 close-out, Step 1 case wording, SPEC and QUEUE templates) and aggregated into one sweep batch; promoting each as its own one-line-edit batch would have been ceremony. 3 findings were held as processed captures because they're more than rewords: REGISTRY.md noun choice carries a Q3.5 interview-question proposal, the spec-entry-trigger threshold needs work on audience (external user vs owner-only — pronoun shifts "someone" → "you"), and plugin-behaviour.md doc-routing inherits the registry noun decision (Blocked by [setup-registry-template-and-noun]). A new audit batch [close-out-audit] was promoted to survey close-out recommendations across all four skills before [next-done-recommendation] is built — that batch addresses one observed incongruence (Step 4 setup.md close-out unconditionally offers /next even when Q4 may have produced nothing); the audit may shrink, expand, or absorb the batch, so it's now Blocked by [close-out-audit]. The hash backfill capture promoted as [log-hash-backfill-in-done]: move the work to /done where the hash is known seconds after commit, use `git commit --amend --no-edit` (safe-case exception to the prefer-new-commits rule — unpushed, seconds-old, local), eliminating /next Step 1.1 entirely. Unpark candidate [ship-freeform-next-type] flagged at session start (blocker shipped in fac25ab) — left deferred to next /plan.

**Queue changes:**
- Promoted: [close-out-audit] (placed before [next-done-recommendation], blocks it), [log-hash-backfill-in-done] (placed after [drop-log-per-release-split]), [setup-project-agnosticism-sweep] (placed after [setup-q4-no-expansion], absorbs 8 captures).
- Modified: [next-done-recommendation] now carries `Blocked by: [close-out-audit]`.

**Captures routed:** 8 promoted (into [setup-project-agnosticism-sweep]); 3 held as processed captures for own later promotion ([setup-registry-template-and-noun], [spec-entry-trigger-rethink], [plugin-behaviour-doc-routing-agnostic] with Blocked by); 1 promoted standalone ([log-hash-backfill-in-done]); 1 promoted as new batch from mid-session split ([close-out-audit]).

## fac25ab — behaviour-agnosticism audit: 11 findings routed to Captures

plugin-behaviour.md is the universal rule layer and setup.md is the on-ramp every project enters through, so app-building assumptions in either doc leak straight into how SI treats non-app projects (records-keeping, research, writing, tax-prep). The audit read both pass-by-pass against the criterion "what assumes the project is an app being built with Claude Code." 2 findings in plugin-behaviour.md (doc-routing line uses "product"/"components"; spec-entry pipeline uses "features" and external "user"). 9 in setup.md, spread across the Step 1 case wording ("source code"/"source files"), the three scaffolded doc templates (SPEC.md "the app is", QUEUE.md "builds first, then tests" missing Audit and freeform, REGISTRY.md "components"/"after each build"), all five interview questions and examples, and the Step 4 close-out. Two findings surfaced second-order issues worth flagging: REGISTRY.md may want a Q3.5-style interview prompt so the user supplies their own noun for project parts; the Step 4 close-out shouldn't unconditionally offer /next when Q4 may not have produced a usable first batch. Q4 itself got an inclusive-wording approach (keep "build/working" for app projects, add "do/made progress on" for non-app) rather than replacement — dropping "build" would alienate non-coders building with a codebase. All 11 findings live in unprocessed Captures for /plan to decide each (reword project-agnostic / demote per-type / keep with load-bearing reason).

**Files touched:**
- QUEUE.md: removed [behaviour-agnosticism-audit] batch from Batches; appended 11 captures (one per finding) to unprocessed Captures.
- _build.md: created at audit start, deleted at close.
- LOG/log.md and LOG/index.md: HASH backfill for the prior commit (777b4c3) folded in.

**Routed to Captures:** 11 findings (see prose above and QUEUE.md captures from this session).

## 777b4c3 — self-hosting dependency-management discipline: target-vs-host distinction, push-marker queue convention, /next halt

Batch ordering in QUEUE.md implicitly assumed the next batch sees the previous batch's effects — true for target-side edits Claude can read at author time, false for host-side effects (hooks, loaded skill procedures, plugin-behaviour.md rules) that only refresh after push + uninstall/reinstall. The recent bite: [capture-parking-discipline] placed before [behaviour-agnosticism-audit] on the assumption the new parking discipline would govern audit capture routing, but it wouldn't have unless a push happened between them. Fixed in two parts: a discipline rule in this project's CLAUDE.md Working conventions distinguishing target-side from host-side, and a structural form — a `--- Push required before continuing ---` queue line paired with a `(host-side)` annotation on `Depends on:`. /next halts at the marker until the user has pushed and reinstalled. The marker check sits in next.md (skill-level, so it works for any self-hosting fork), the discipline rule sits in this project's CLAUDE.md (host-only, doesn't propagate via plugin update). The parked [self-hosting-support-during-setup] capture was extended so the scaffolding template, whenever it ships, carries all of this — target/host distinction, ordering rule, marker convention, annotation — into forking projects' CLAUDE.md.

**Files touched:**
- CLAUDE.md: new "Self-hosting dependency ordering" subsection under Working conventions
- plugin/si-plugin/docs/next.md: push-marker halt added at Step 1.3
- QUEUE.md: [self-hosting-support-during-setup] parked capture extended; missing slug marker added

**Routed to Captures:** none new this build (one capture filed pre-build: LOG hash backfill optimization — move into /done via amend)

## dedb34a — /plan session: tax-folder /setup test surfaced 3 new batches + structural form for self-hosting dependency

A real /setup run in a tax-prep folder (separate, non-SI project) surfaced gaps in setup.md that ride on Claude's judgement rather than written rules: handling of pre-existing user content in Case B, and Q4's tolerance for parenthesised illustrative examples that bend "in user's words." Promoted [setup-preexisting-content-handling] to make peek-but-don't-pre-answer and leave-untouched explicit, and [setup-q4-no-expansion] to tighten Q4's rule against any expansion (illustrative or otherwise). Same run also exposed app-building framing in setup.md's interview questions, so [behaviour-agnosticism-audit] widened to cover setup.md alongside plugin-behaviour.md. Separately, the previously-captured self-hosting dependency gotcha promoted to [self-hosting-dependency-discipline] — initial draft was discipline-only, revised mid-session after the user pushed back to add a structural form: `--- Push required before continuing ---` queue marker + `(host-side)` annotation on `Depends on:`, with /next halting at the marker. Two parked captures: [freeform-on-demand] revising [ship-freeform-next-type] to be on-demand rather than queue-driven (queueing "I did some manual work" is ceremony), and [user-execution-batch-shape] deferring the question of whether non-coder projects need a new batch type for user-as-executor work until 2-3 such batches have actually run.

**Queue changes:**
- Promoted: [self-hosting-dependency-discipline] (placed at top — foundational discipline benefits later batches)
- Promoted: [setup-preexisting-content-handling] (appended)
- Promoted: [setup-q4-no-expansion] (appended after preexisting-content-handling — same setup.md thread)
- Revised: [behaviour-agnosticism-audit] (widened scope to include setup.md interview framings)
- Parked: [freeform-on-demand], [user-execution-batch-shape]

**Routed to Captures:** none new (1 unprocessed cleared via promotion)
