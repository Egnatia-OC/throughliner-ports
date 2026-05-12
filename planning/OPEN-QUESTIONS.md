# Open questions

Method-level questions that have been raised but aren't yet ready to be a session. Each entry stays here until the question resolves — at which point it either folds into an existing session's scope, becomes its own new session (with a row added to `PLAN.md` and a new `sessions/Vxx.md`), or is consciously dropped with a one-line reason recorded in `BUILD-LOG.md` so future-me knows it was considered.

Newest first. Removed when resolved.

For the format and lifecycle, see project `CLAUDE.md` → *Open questions*.

---

## Method response to direct-edit users (developers)

**The question.** How should the no-code method respond to users who edit code directly — i.e. developers who already write code and want the method's planning discipline without ceding all technical work to Claude?

**Why it matters.** Raised in Vibecord (vibe-coding Discord) — "developers will try to use it." The method as written assumes Claude does the technical work and the user reviews recaps. A user editing code directly breaks several method assumptions: `MANIFEST.md` drifts because the user's edits aren't recorded; the `BACKLOG.md` build-batch / `Serves UX.md:` discipline gets bypassed; drift checks catch *some* of it (the `MANIFEST.md` ↔ codebase check) but not all. If we don't address this, developers using the method will silently corrupt the project state and lose the benefits the method was supposed to provide.

**Working notes — three rough shapes the response could take.**

- *Tighten drift detection so manual edits get caught.* V20's `SessionStart` hook (or a `PostToolUse` hook) could compare the working tree against the last-known `MANIFEST.md` state and surface manual changes for triage. Smallest change, but only catches edits after the fact — doesn't prevent them mid-flow.
- *Add a "developer mode" entry point.* The plugin scaffolds a different doc set for developers — keeps `UX.md` / `BACKLOG.md` discipline (spec-first), drops the assumption that Claude does all the code. Requires deciding what the developer-mode equivalents of MANIFEST.md (which Claude maintains) and the build-recap flow look like.
- *Document that the method explicitly doesn't serve direct-edit users.* Add a "Who this is for" section to `NO-CODE-METHOD.md` so developers self-select out. Cheapest move but loses an audience.

**Next step.** Think during V20 (SessionStart hook extension). If drift detection covers the realistic failure modes, fold there and close the question. If not, promote to its own session somewhere in the V21–V24 range — add a row to `PLAN.md` and create a `sessions/Vxx.md` with whichever shape lands.
