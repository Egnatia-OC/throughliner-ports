---
description: Lock the next batch's file list and verification burden before any code changes. Runs after a planning session; hands off with a "switch out of plan mode" prompt.
allowed-tools: Task
---

The user has invoked /before-build. Spawn the before-build subagent via the Task tool.

The subagent reads `BACKLOG.md`, `UX.md`, `MANIFEST.md`, and `DOC-STRUCTURE.md` → *Build batches* and *Files: sub-section* itself; no payload preparation is required from you. Pass it a short prose prompt naming the route — e.g. "User invoked /before-build. Lock the file list and verification burden for the top build batch."

Relay the subagent's recap to the user without restructuring.
