# Build log — [Project Name]

A running record of decisions, changes, and reasoning for every build. One file per build in this folder, newest-first in this index. Maintained by Claude during builds (the after-build subagent writes one entry per completed batch and appends the index line). Not for cover-to-cover reading — search when you need the "why" behind a previous build's choices.

For the canonical entry shape, see `DOC-STRUCTURE.md` → *Build log structure*.

<!--
Index format — one entry per build, newest first:

- `NNN-batch-name.md` — YYYY-MM-DD — One-line summary

Entry file format (one file per build in this folder):

# <Session> — YYYY-MM-DD — One-line summary

**What shipped.** Short plain-English paragraph describing concrete deliverables. Reference TEST-LOG row range rather than restating test outcomes. Reference research files by path rather than embedding their content.

**Decisions taken and why.** Two or three bullets on load-bearing decisions — what was chosen, alternatives considered, what tipped the call. Skip housekeeping; focus on choices shaping future sessions.

**Pivots and surprises.** Anything that turned out differently than the plan expected — a bug, a wrong assumption, an external fact discovered mid-build.

**Carried forward.** Items raised but not done, with destination (which planning batch, BACKLOG entry, or "not pursued — reason").

## Performance

- **Batch completion:** Complete / Partial (handoff)
- **Files in batch:** N
- **Carve-outs:** None / N prerequisite, N re-batch
- **Claude-verified tests:** N Pass, N Fail (of N total)
- **User-verified tests:** N pending
- **Session notes:** (optional — added by the user after testing)
-->

---
*No-code method — Version 58.*
