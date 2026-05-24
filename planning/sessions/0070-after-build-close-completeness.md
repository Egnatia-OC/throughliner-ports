# 0070 — After-build close completeness

## Goal

Port three dev-side session-close steps to the plugin-side after-build agent, making consumer project session close as complete as the dev side. Add a CLAUDE.md extensibility section so users can declare project-specific close steps the agent will execute.

## Background

The dev-side session close (BUILD-METHOD.md steps 1–6) has three capabilities the plugin-side after-build agent lacks:

1. **Doc-code parity audit.** Dev-side audits code changes against docs (vocabulary, mechanism descriptions, templates, inventory, ghost references). Plugin-side updates MANIFEST but doesn't check whether code changes broke alignment with UX.md descriptions, BACKLOG wording, or CLAUDE.md's path block.

2. **Idea sweep with triage routing.** Dev-side sweeps for ideas raised but not implemented, routing each to a specific destination. Plugin-side flags "out-of-scope improvements" in the recap but doesn't route them anywhere.

3. **Pre-commit checkpoint.** Dev-side explicitly verifies all prior steps completed before committing. Plugin-side goes straight to closing prompts without verification — if context gets compressed mid-run, steps can be silently skipped.

Additionally: the after-build agent owns a fixed step list with no mechanism for per-project extensions. CLAUDE.md is already the customisation point and already read by the agent — a recognised section there solves extensibility without a new mechanism.

## Inputs

- `BUILD-METHOD.md` — dev-side session close steps 1, 5, 6 (the three being ported).
- `plugin/agents/after-build.md` — current agent body (target of changes).
- `plugin/templates/CLAUDE-TEMPLATE.md` — target for extensibility section.

## Outputs

- **`plugin/agents/after-build.md`** — three new steps woven into the existing sequence:
  - **Doc-parity check** (after MANIFEST update, before recap): for each file in the batch's Files: list, grep UX.md, BACKLOG, and CLAUDE.md for references to renamed/deleted/moved things. Flag stale references in recap. Scoped to blast radius of what changed — not a full doc audit.
  - **Idea sweep** (after end-of-recap flags, before pre-commit checkpoint): sweep the session for ideas, suggestions, or observations raised but not acted on. Triage each to: add to BACKLOG (new item or flag for next planning), note in build-log as "not pursued, reason: ...", or flag in recap for user to decide.
  - **Pre-commit checkpoint** (immediately before closing prompts): verify MANIFEST updated, TEST-LOG rows written, build-log entry written, idea sweep done, doc-parity check done. If any missing, complete before prompting commit.
- **`plugin/agents/after-build.md`** — instruction to read and execute any steps in CLAUDE.md's project-specific close section (after standard steps, before closing prompts).
- **`plugin/templates/CLAUDE-TEMPLATE.md`** — optional section for project-specific close steps.
- **Tests** — new test cases for the three steps if testable at the unit level.

## Success criteria

- After-build agent body contains all three new steps in the correct sequence positions.
- CLAUDE-TEMPLATE contains the extensibility section with guidance on what belongs there.
- Existing after-build steps unchanged in substance.
- Step numbering and cross-references updated consistently.

## Open questions for this session

1. **Doc-parity scope.** Should the check also cover research/ docs, or just the spine (UX/BACKLOG/MANIFEST/CLAUDE.md)? Leaning spine-only to avoid false positives.
2. **Idea sweep — memory vs. docs.** Ideas can live in memory during the session and land in docs at sweep time. The sweep instruction should say "check conversation context" not "check memory" — but should it explicitly mention memory as a valid interim holding place?
3. **Extensibility section name.** "Project-specific close steps" is functional but long. Alternatives: "After-build additions", "Close steps", "Session close".

## Risks / dependencies

- The after-build agent body is already 120+ lines. Three new steps add density — risk of context-pressure skipping increases, which is ironic given that the pre-commit checkpoint exists to catch exactly that. Keep step instructions tight.
- No hard dependencies on other sessions. Can build whenever queued.
