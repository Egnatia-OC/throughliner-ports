---
description: Lock the next batch's file list and verification burden before code changes. Runs after planning; hands off with a "switch out of plan mode" prompt.
allowed-tools: Task
---

The user has invoked /before-build. Spawn the before-build subagent via Task tool.

The subagent reads BACKLOG, UX.md, MANIFEST.md, and DOC-STRUCTURE.md itself — no payload prep needed. Pass a short prose prompt: "User invoked /before-build. Lock the file list and verification burden for the top build batch."

Relay the subagent's recap without restructuring.
