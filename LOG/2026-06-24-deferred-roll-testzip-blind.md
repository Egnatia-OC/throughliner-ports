# ee238d1 — Deferred-test roll liveness check: content stamp replaces version comparison (session_start.py + plan.md + CLAUDE.md + FAQ)

Built in a six-batch goal session (plugin off).

The deferred-test roll decided whether host-side tests had gone live by comparing version numbers: host base ≥ target base ⇒ live. That is the wrong signal. A build batch changes host-side files (a hook, a procedure doc) without bumping any version, and the `-testN` suffix only moves on a rezip — so the installed host and the target can show the exact same version while the host is missing the latest changes, and the check still reports "live." The real question is whether the installed host's files match the target's current files — a content question, not a version one.

Changes:

- **session_start.py** — new `content_stamp(root)`: walks a plugin directory, hashes each file's bytes in sorted relative-path order, excludes `__pycache__` and `.pyc` (disposable, never shipped), and returns a short hex stamp. The hook computes it over the installed host (its own `CLAUDE_PLUGIN_ROOT`) and surfaces it at session start alongside the version it already reports.
- **plan.md** — the deferred-test roll resolution (Step 1 scan note + Step 2 host-side resolution) now compares stamps, not versions: compute the target's current stamp the same way (run the hook's `content_stamp()` over `plugin/si-plugin/`) and compare to the installed host's surfaced stamp — match ⇒ host-side lines live, mismatch ⇒ not reinstalled since the latest host-side change. The no-ask property is kept; the "host base ≥ target ⇒ live" wording is gone.
- **CLAUDE.md (project root)** — the deferred-tests description gains the content-stamp basis (CLAUDE.md carried no explicit version-base rule, so this adds the basis rather than replacing one), and names the old version-base rule it supersedes.
- **FAQ** — a brief entry on the build stamp shown at session start (what it is, why it's there, that nothing about the user's project goes into it), plus its index line.

Rejected alternatives, kept so they aren't relitigated: comparing the full version including `-testN` (the capture's first idea) is still blind to build-batch edits that bump nothing; baking the stamp into the zip at package time adds steps to the rezip and push rituals for no added correctness over hashing at runtime. Scope is self-hosting — a normal consumer installing a release is unaffected. Builds on [surface-installed-host-version].

Run-now test PASSED in-session: identical inputs produce equal stamps; a copy of the plugin dir matches the original; changing one file produces a mismatch; adding `__pycache__`/`.pyc` does not perturb the stamp. Deferred host-side line written for the first /plan after a rezip + reinstall.
