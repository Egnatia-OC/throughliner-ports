# Planning procedure: "what you don't do" constraint

**Goal.** Prevent Claude from offering to implement changes during /sovplan sessions. Currently procedures/planning.md defines what planning does but not what it doesn't — the V67 carve-out for source-of-truth doc editing creates ambiguity about what's allowed vs what should route through a build batch.

**Outputs.** Updated procedures/planning.md with explicit constraints section.

**Success criteria.** Claude never offers to "implement now" during a /sovplan session. All non-BACKLOG changes route through build batches. The distinction between "editing scope docs to reflect planning decisions" (allowed) and "implementing new rules or features" (not allowed, even as doc edits) is explicit.

Changes:
- [Requested] Add "What you don't do" section to procedures/planning.md. At minimum: don't implement, don't build, don't edit CLAUDE.md project-specific notes outside scope decisions. All changes route through BACKLOG.
- [Suggested] Clarify V67 boundary: source-of-truth doc edits during planning are for scope decisions (adding/removing/revising UX entries), not for implementing behavioral rules or project configuration.
- [Suggested] Fix invalid escape sequence `\`` in pre_tool_use.py line 681 (SyntaxWarning on Python 3.12+; will become an error in a future version). Use raw string or `\\``.

Serves UX.md: Planning sessions.
