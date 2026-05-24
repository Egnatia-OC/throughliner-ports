# Open questions

Method-level questions not yet ready to be a session. Each stays until resolved — folded into a session's scope, promoted to its own session, or dropped with a reason in `BUILD-LOG.md`. Newest first. Removed when resolved.

Format and lifecycle: project `CLAUDE.md` → *Open questions*.

---

## Structured-markdown validator as a plugin component

**The question.** Should the plugin include a general-purpose structured-markdown linter that validates BACKLOG batch format, TEST-LOG column counts, scope-context section completeness, and other method-specific document shapes — beyond what `parse_backlog.py` currently does?

**Why it matters.** Surfaced 2026-05-24 during E2E testing research. `parse_backlog.py` validates BACKLOG structure, but TEST-LOG, build-log entries, and scope-context sections have no equivalent validation. Malformed docs cause silent failures downstream (subagents misread state, hooks gate on wrong data). A general lint could run as a PostToolUse check or a planning-session pre-flight.

**Next step.** Park. Revisit when E2E testing surfaces concrete instances of malformed docs causing problems.

---

## Plugin testing framework beyond bespoke pytest

**The question.** Should the project invest in a reusable plugin testing framework — run a hook against synthetic input and assert on output shape/content, without a full Claude Code session — or is the current bespoke pytest suite sufficient?

**Why it matters.** Surfaced 2026-05-24 during E2E testing research. The pytest suite at `tests/` covers hook subprocess tests and unit tests, but it's custom-built for this project. A framework could make it easier to add tests for new hooks, validate subagent prompts, and regression-test deny/allow paths. Counter-argument: the bespoke suite works, runs in under 5 seconds, and covers 124 tests — a framework might add abstraction without proportional value.

**Next step.** Park. Revisit if test maintenance burden grows or if other plugin projects would benefit from the same patterns.

---

## Plugin settings layer / per-project config file

**The question.** Should the plugin support a separate config file (or settings layer) that lets users override or extend plugin-owned workflows — as opposed to using CLAUDE.md sections for extensibility?

**Why it matters.** Surfaced 2026-05-24. Ideation on porting the dev-side session close to the plugin raised the question of user-extensible workflows (e.g. adding project-specific close steps, enabling footer bumps). CLAUDE.md is already the per-project customization point and already read by subagents, so a recognised section there is the simpler path. A separate config file would be a new mechanism to maintain. Worth revisiting if CLAUDE.md extensibility proves insufficient.

**Working notes.** 2026-05-25: Doc-parity check (0070) scoped to spine docs only. Users with additional source-of-truth docs declared in CLAUDE.md's path block may want those included in the parity check. The path block already provides discovery — wiring them in is a natural extension if CLAUDE.md-section extensibility proves too coarse.

**Next step.** Parked. Revisit if the CLAUDE.md-section approach ships and users hit limits.

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
