# Open questions

Method-level questions that have been raised but aren't yet ready to be a session. Each entry stays here until the question resolves — at which point it either folds into an existing session's scope, becomes its own new session (with a row added to `PLAN.md` and a new `sessions/Vxx.md`), or is consciously dropped with a one-line reason recorded in `BUILD-LOG.md` so future-me knows it was considered.

Newest first. Removed when resolved.

For the format and lifecycle, see project `CLAUDE.md` → *Open questions*.

---

## Cross-version template reconciliation for Cowork-first users

**The question.** When a user authors their spine docs (`UX.md`, `BACKLOG.md`, etc.) in Cowork against, say, a V17 template they had locally, and then installs the no-code-method plugin (currently V19), the user's docs carry a V17 footer while the plugin's bundled templates carry V19. The structural rules between versions may differ. What does the plugin do about it?

**Why it matters.** Raised in V19 planning while discussing why bundled templates earn their keep in a Cowork-first authoring world. Cowork-first is now the recommended path for the planning phase (see `NO-CODE-METHOD.md` → *Detect template state* and the new-project route preamble), so the "user arrives at Claude Code with pre-authored docs" path is the *expected* case, not the exception. If the plugin silently treats those docs as current, structural drift compounds invisibly — a V17 `UX.md` running against V19 hooks may pass checks the V19 rules tightened.

**Working notes.**

- The model I'd argue for: **plugin is the runtime source of truth; the user's footer is the version their authoring assumed.** Mismatch is a tripwire, not an error.
- Where each piece would land in the migration roadmap:
  - **V20 (SessionStart extension).** Reads the user's CLAUDE.md / UX.md footers, compares to the plugin's bundled-template versions, surfaces the mismatch (plain English, no auto-fix). One read per session-start; cheap.
  - **V24 (`/migrate` skill).** Does the actual diff-and-propose work — comparing the user's `UX.md` (or whichever doc is mismatched) against the bundled V19 template's structural rules and proposing the edits to bring it up to spec. Already on the roadmap for migrating any non-conformant docs; this just gives it a specific tripwire to react to.
- The V19 piece is done already: every bundled template carries its version footer (already true; the session-close rule keeps them current).

**Next step.** Fold the tripwire half into V20's session scope; the worker half into V24's. Confirm during V20 planning that the SessionStart hook's foundational-reads step includes the footer-comparison check, and during V24 planning that `/migrate` knows how to handle a version-mismatch signal. Remove this entry once both folds are confirmed.

---

## Method response to direct-edit users (developers)

**The question.** How should the no-code method respond to users who edit code directly — i.e. developers who already write code and want the method's planning discipline without ceding all technical work to Claude?

**Why it matters.** Raised in Vibecord (vibe-coding Discord) — "developers will try to use it." The method as written assumes Claude does the technical work and the user reviews recaps. A user editing code directly breaks several method assumptions: `MANIFEST.md` drifts because the user's edits aren't recorded; the `BACKLOG.md` build-batch / `Serves UX.md:` discipline gets bypassed; drift checks catch *some* of it (the `MANIFEST.md` ↔ codebase check) but not all. If we don't address this, developers using the method will silently corrupt the project state and lose the benefits the method was supposed to provide.

**Working notes — three rough shapes the response could take.**

- *Tighten drift detection so manual edits get caught.* V20's `SessionStart` hook (or a `PostToolUse` hook) could compare the working tree against the last-known `MANIFEST.md` state and surface manual changes for triage. Smallest change, but only catches edits after the fact — doesn't prevent them mid-flow.
- *Add a "developer mode" entry point.* The plugin scaffolds a different doc set for developers — keeps `UX.md` / `BACKLOG.md` discipline (spec-first), drops the assumption that Claude does all the code. Requires deciding what the developer-mode equivalents of MANIFEST.md (which Claude maintains) and the build-recap flow look like.
- *Document that the method explicitly doesn't serve direct-edit users.* Add a "Who this is for" section to `NO-CODE-METHOD.md` so developers self-select out. Cheapest move but loses an audience.

**Next step.** Think during V20 (SessionStart hook extension). If drift detection covers the realistic failure modes, fold there and close the question. If not, promote to its own session somewhere in the V21–V24 range — add a row to `PLAN.md` and create a `sessions/Vxx.md` with whichever shape lands.
