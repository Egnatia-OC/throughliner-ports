# [Batch name]

<!--
Build batch file — two regions: scope context (Goal through Dependencies/Red flags)
and build operations (Changes through Serves). Full spec: DOC-STRUCTURE.md → Build batches.
-->

**Goal.** [One paragraph — why this batch exists, what will be different when it ships.]

**Outputs.** [Prose — what changes the user will experience after the batch ships.]

**Success criteria.** [Observable, testable conditions for knowing the batch succeeded.]

**Decisions to make this batch.** [Unresolved scope questions. Omit if all decisions are made.]

**Dependencies.** [What this batch needs from outside itself. Omit if none.]

**Red flags.** [Security/privacy/data-integrity concerns. Only present when detected.]

Changes:
- [Requested] [Change description — one line]
- [Suggested] [Change description]

Inputs:
- `[path/to/resource]` — [why this batch needs it]

Files:
- [ ] `[path/to/file]` — [one-sentence summary of the change]

Tests:
- [Test description] [Look and click] [User]
- [Test description] [Run and read] [Claude]

Serves UX.md: [entry name(s)].
