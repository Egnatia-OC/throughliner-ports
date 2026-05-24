# Open questions

Method-level questions not yet ready to be a session. Each stays until resolved — folded into a session's scope, promoted to its own session, or dropped with a reason in `BUILD-LOG.md`. Newest first. Removed when resolved.

Format and lifecycle: project `CLAUDE.md` → *Open questions*.

---

## Red-flag / threat-class marker for security-shaped batches

**The question.** Should BACKLOG batches touching security surfaces (auth, secrets, PII, deletion, payment) carry an explicit *Red flags* marker — as a batch sub-section, as planning-subagent auto-detection, or both?

**Why it matters.** Surfaced 2026-05-22. Walking V-file *Risks / dependencies* revealed conflation between build-dependency risk and security risk. Dependencies landed; Risks scoped out. No doc currently carries "be paranoid about this part."

**Next step.** **Partially shipped V47 (session v51).** Batch-level Red flags sub-section shipped — planning subagent auto-detects security-shaped scope and writes a persistent section. Remaining: threat-class marker on UX.md entries — unscheduled.

---

## Post-adopt and mid-loop UX friction (V42 smoke-test observations)

**The question.** Seven UX friction points from V42's live smoke test.

**The seven items.**

1. ~~Jargon in adopt subagent.~~ **Resolved V44.**
2. ~~No next-action prompt after `/setup`.~~ **Resolved V44.**
3. **Proposed-edit UX forces manual copy-paste.** Biggest friction point — user must open markdown, find section, paste, save. Distributed fold-ins restructured where edits live but don't address the paste UX.
4. ~~Permission modes vs. UX.md lock.~~ **Resolved V43.**
5. ~~After-build commit/tag prompt.~~ **Resolved V46.**
6. ~~Template placeholder cleanup.~~ **Resolved V47.**
7. ~~Pass/Fail/Skipped explanations.~~ **Resolved V44.**

**Next step.** Six of seven resolved. **Remaining:** item 3 (proposed-edit UX).

---

## Graduate sovereign implementer onto sovereign implementer

**The question.** Can this dev project dogfood the method's own plugin?

**Why it matters.** Surfaced 2026-05-21. Dogfooding would surface gaps Taskflow can't and validate non-UI project types.

**Prerequisites (all shipped):**

1. Distributed fold-ins + open questions — **Shipped V43.**
2. Automated vs. manual test split — **Shipped V46.**
3. Two-write rule shelved — **Done v40.**
4. UX.md non-GUI adaptation — **Shipped V47.**

**Next step.** **Indefinitely shelved** (v61). All prerequisites shipped, but E2E testing revealed efficiency/correctness fixes needed (0063–0068). Restore when the method is stable enough to dogfood without excessive token burn.

---

---

## Prose-only rewrite of the method

**The question.** Tool-agnostic prose-only version for users without Claude Code.

**V37 note:** V32's two-write rule delivered the docs-only set at repo root. V40 froze it at V39.

**Next step.** **Indefinitely parked** (v47). Promote if a real audience emerges.
