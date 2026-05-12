# Iteration playbook

A library of named iteration types — passes you can deliberately run on the no-code method or its surrounding docs. Not a sequence. Not a checklist. A catalog of recognisable shapes to reach for when the work in front of you matches one of them.

Sibling reference: `Taskflow planning passes.md` (one folder up) for project-level passes that aren't about developing the method.

## How to use this playbook

When something arrives that feels iteration-shaped — a batch of catches, a new upstream version, a structural change you've been turning over — scan the **roles** below, find the one matching your situation, and open the entry. Each entry stands alone; you don't need to read the rest of the playbook to use one.

If a pass produces a queued prompt for a future session, the next session uses [[Premise check]] before running it.

## Roles

The passes fall into a few roles. A pass can play more than one role in the same session — Catch consolidation and Downstream calibration both surface *and* execute, for instance.

**Surfacing.** Raise something that needs to change. [[Catch consolidation]] starts from accumulated catches. [[Principle audit]] starts from "what am I missing?" [[Downstream calibration]] starts from reading a real project's artefacts.

**Producing.** Turn a surfaced change into a queued prompt for a future session, when the change is too big or risky to absorb mid-flight. [[Reorg priming]] is the main one; [[Principle audit]] also closes with a queued prompt.

**Executing.** Make the edits and cut a version. [[Catch consolidation]] and [[Downstream calibration]] execute in the same session they surface. [[Spec-driven version cut]] is execute-only — it runs against a prompt drafted earlier.

**Reconciling.** Between a queued prompt and its execution: [[Premise check]] makes sure the prompt's assumed state still matches reality before you run it.

**Validating.** Stress-test a version after a cut. [[Reader test]] is the only one.

**Reflecting.** Harvest from any of the above. [[Rule and procedure extraction]] — the pass that built this playbook.

**Sub-pass shapes.** Nest inside an executing pass when the work surfaces a sub-issue mid-flight. [[Rule-application sweep]] and [[Mid-pass method amendment]].

**Cross-cutting.** Fire on their own triggers, separate from the main chain. [[Framework housekeeping]] and [[Sync-procedure hardening]].

## Common chain

The canonical chain when a queued prompt is involved: Reorg priming or Principle audit produces a prompt → Premise check reconciles it against current state → Spec-driven version cut executes it → Reader test validates → Rule and procedure extraction reflects.

The short-circuit chain when no queued prompt is involved: Catch consolidation or Downstream calibration surfaces *and* executes in one session → Reader test → Rule and procedure extraction.

Every entry is independently runnable. Sequence is a tendency, not a rule.

## Index by maturity

**Proven** — recurring shape across multiple sessions, well-understood.

- [[Catch consolidation]] — accumulated catches folded into a version bump
- [[Spec-driven version cut]] — execute a pre-authored change set
- [[Premise check]] — reconcile a queued prompt against current state before running
- [[Reorg priming]] — produce a queued prompt for a future structural change
- [[Reader test]] — stranger-perspective sub-agent stress test
- [[Rule and procedure extraction]] — end-of-session harvest
- [[Framework housekeeping]] — meta-shape of the docs shifts (organisation, versioning, location)

**Single-instance** — observed once, shape plausible but unrefined.

- [[Principle audit]] — state-driven step-back: what higher-leverage moves haven't I considered?
- [[Downstream calibration]] — read a downstream project to find where the method is thin
- [[Coherence sweep]] — single broken spot that cascades; each fix exposes the next inconsistency
- [[Sync-procedure hardening]] — patient is the procedure, not the docs

**Experimental** — first attempt, unclear yet whether the shape is right.

- [[Replant (method terms)]] — wholesale rewrite when a new source doc contradicts the method's foundation. (Method-level adaptation of a project-level pass; not yet observed at method level.)

**Sub-pass shapes** — nest inside an executing pass; tier-tagged individually.

- [[Rule-application sweep]] — cleanup revealed a class of violation; sweep for it. (Single-instance.)
- [[Mid-pass method amendment]] — absorb a substantive gap mid-flight inside another pass. (Single-instance.)

## Notes for future-Alex

- Add new entries as new shapes recognise themselves across two or more sessions. A one-off doesn't earn an entry; it earns a note in the source response folder until a second instance appears.
- Demote entries that stop working. A pass marked Proven that fails twice in a row should drop to Single-instance or be removed.
- The reflective pass that built this — [[Rule and procedure extraction]] — is also the pass that maintains it. Re-run after substantive sessions and update entries from what surfaces.
- The two source files that fed the initial extraction — `Doc development rules.md` and `Iteration Passes.md` (one folder up) — are kept for traceability. New entries don't need to add to them.
