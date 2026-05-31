# v142b — 2026-05-29 — Skill invocation flowchart and prerequisite audit

**What shipped.** Completed batch 0142. Produced a Mermaid flowchart of all 13 skill invocation paths and a prerequisite audit identifying 5 gaps in procedure docs. Flowchart and audit stored in `Dev/Resources/research/skill-invocation-flowchart.md`. Filed gaps as new batch 0143 (procedure-doc fixes to align with V90 snapshot architecture).

**Decisions taken and why.** Bundled all 5 gaps into a single batch (0143) rather than individual entries — they're all procedure-doc text changes with a common root cause (V90 architecture made some pre-V90 checks dead or misleading). Chose Mermaid for the flowchart format — renderable in GitHub, crash course, and most markdown previewers. Graded gaps by severity: 3 medium (dead gate, vacuous build, wrong-batch validation), 2 low (doc inconsistency, confusing-but-harmless message).

**Pivots and surprises.** None. The audit confirmed the hook layer is solid — all 5 gaps are in procedure-doc text, not in enforcement code. The V90 snapshot architecture works well; the procedures just haven't all caught up to it.
