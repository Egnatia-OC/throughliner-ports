# BUILD-LOG.md

> **FROZEN at method version V39, 2026-05-21 (shelved in session v40).** The live template is at `plugin/templates/BUILD-LOG-TEMPLATE.md` — that's what `/adopt` scaffolds. The two-write rule that kept this copy aligned has been shelved (see `BUILD-METHOD.md` → *Two-write rule for canonical docs*). Restoring two-write maintenance is one `planning/OPEN-QUESTIONS.md` promotion away if a real audience for the no-plugin template set emerges.

A running record of decisions, changes, and reasoning for every build, newest-first. Maintained by Claude during builds (the after-build subagent writes one entry per completed batch). Not for cover-to-cover reading — search and scan when you need the "why" behind a previous build's choices.

For the canonical entry shape, see `DOC-STRUCTURE.md` → *BUILD-LOG.md structure*.

<!--
Entry format (newest first):

## <Session> — YYYY-MM-DD — One-line summary

**What shipped.** Short plain-English paragraph describing concrete deliverables. Reference TEST-LOG row range rather than restating test outcomes.

**Decisions taken and why.** Two or three bullets on load-bearing decisions — what was chosen, alternatives considered, what tipped the call. Skip housekeeping; focus on choices shaping future sessions.

**Pivots and surprises.** Anything that turned out differently than the plan expected — a bug, a wrong assumption, an external fact discovered mid-build.

**Carried forward.** Items raised but not done, with destination (which planning batch, BACKLOG entry, or "not pursued — reason").
-->

---
*No-code method — Version 39.*
