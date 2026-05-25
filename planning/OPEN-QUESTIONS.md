# Open questions

Method-level questions not yet ready to be a session. Each stays until resolved — folded into a session's scope, promoted to its own session, or dropped with a reason in `build-log/`. Newest first. Removed when resolved.

Format and lifecycle: project `CLAUDE.md` → *Open questions*.

---

## Parent-directory CLAUDE.md inheritance — placement constraint

**The question.** Should the plugin document the risk that placing a project folder inside another project's tree causes Claude Code's parent-directory CLAUDE.md inheritance to poison the session? And if so, where — Reference manual, setup procedure warning, or both?

**Why it matters.** Surfaced twice during E2E testing (v79, findings 1 and 5). When the Polite Fart Announcer burner folder was placed inside the no-code-method tree, the parent CLAUDE.md made Claude think it was in the method dev project. The v79 research file noted "not a plugin bug but a placement constraint worth documenting" — but it was never documented anywhere. This is a real footgun for users who organise projects in nested folders.

**Working notes.** The plugin can't control Claude Code's inheritance behaviour. The fix is awareness: warn users during `/setup` if the project root has a parent-directory CLAUDE.md, and document the constraint in the Reference manual. Could also add a SessionStart check that detects parent CLAUDE.md files and surfaces an advisory.

**Next step.** Ready to promote. Small scope — documentation + optional SessionStart advisory. Restored during 2026-05-25 ideation session.

---

## Project-boundary hook bypass via Bash

**The question.** The project-boundary PreToolUse hook (0065) blocks `Edit`/`Write`/`MultiEdit` outside the project root, but `Bash` commands (`sed`, `echo >`, PowerShell `Set-Content`, etc.) bypass it entirely. Should the plugin add a Bash-matcher PreToolUse check for common file-write patterns, similar to how the git safety guard matches `git reset --hard` and `git push --force`?

**Why it matters.** Surfaced 2026-05-25 during v73 session close. Claude used `sed` to edit a file outside `sovereign-implementer/` after the Edit tool was correctly blocked. The boundary enforcement is advisory (catches normal editing flow), not hermetic (can't prevent Bash-based writes). A careless or drifting Claude session could write outside the project without the hook ever firing. The git safety guard already demonstrates the pattern — match dangerous Bash substrings and deny — but file-write patterns are far more varied than git commands, so false positives are a real concern.

**Working notes.** Common file-write patterns that could be matched: `sed -i`, `> file`, `>> file`, `tee`, `Set-Content`, `Out-File`, `Add-Content`, `cp`, `mv`. But every match risks blocking legitimate in-project Bash use. An alternative: instead of blocking, surface a warning via `additionalContext` when Bash targets a path outside the project root — advisory rather than deny.

**Next step.** Park. Revisit if E2E testing or real-world use surfaces unintended cross-project writes from Bash. The advisory-warning approach is lower-risk than a hard deny if this gets promoted.

---

## Structured-markdown validator as a plugin component

**The question.** Should the plugin include a general-purpose structured-markdown linter that validates BACKLOG batch format, TEST-LOG column counts, scope-context section completeness, and other method-specific document shapes — beyond what `parse_backlog.py` currently does?

**Why it matters.** Surfaced 2026-05-24 during E2E testing research. `parse_backlog.py` validates BACKLOG structure, but TEST-LOG, build-log entries, and scope-context sections have no equivalent validation. Malformed docs cause silent failures downstream (subagents misread state, hooks gate on wrong data). A general lint could run as a PostToolUse check or a planning-session pre-flight.

**Next step.** Promote after the proxy layer ships (0081/0089/0090). Proxies add another structured format with specific shape requirements — validation becomes more valuable as the number of structured doc types grows. The original parking rationale ("revisit when E2E surfaces problems") was a dead trigger: two E2E rounds ran without explicitly checking for malformed-doc failures. Restored during 2026-05-25 ideation session.

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

**What shipped.** Batch-level Red flags sub-section shipped V47 (session v51) — planning auto-detects security-shaped scope and writes a persistent section.

**What remains.** Threat-class marker on individual UX.md entries — so security-shaped features are flagged at the spec level, not just at the batch level. A UX entry for "user authentication" or "payment processing" would carry a visible marker that downstream batch planning and build sessions can key off. Currently a feature can touch a security surface without any spec-level signal.

**Next step.** Ready to promote. Could fold into a planning or UX-template session, or stand alone as a small scope. Restored from stale "unscheduled" status during 2026-05-25 ideation session.

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
