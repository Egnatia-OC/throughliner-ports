# [HASH] — Never stage the test-build version suffix — a recognised signature the close leaves dirty rather than committing

Every rezip bumps `plugin.json`'s `-testN` suffix as a working-tree-only change, reset to a clean version at the next real push. Between the two the file sits dirty, so the close's out-of-scope-dirty-path check surfaces it at every single session — predictable noise the capture proposed suppressing.

The premise turned out confirmed but the outcome worse than assumed. The file wasn't dirty at processing time because the suffix had been **committed**: the repo's committed version was `1.16.0-test4`, staged during an ordinary session close, not a release. The ritual states plainly that the suffix lives in the working tree only. That rule was silently broken.

The way it got broken is the actual finding. Faced with the same file surfacing at every close, a session made it stop by staging it — the path of least resistance, and one the existing wording left open, since the check surfaces the file and asks, and "commit it" is an available answer. The damage self-heals at the next release, but until then the public repo advertised a test build as its version.

So the fix is wider than the capture proposed. A carve-out that only said "don't ask about it" would still permit the file being swept into a commit unremarked — exactly what happened. The carve-out says **leave it dirty and never stage it**, and the doc says why it is stronger than the hash-backfill carve-out it sits beside. The signature is exact: a `plugin.json` diff whose *sole* change is the version string, and only where the new value carries the test suffix. Any other edit to that file surfaces normally, or the carve-out becomes a hole.

The Rezip ritual also now states that the dirty file is expected between a rezip and the next push, so a session reading the ritual doesn't independently decide to tidy it — which is how this went wrong the first time.

**Files touched:** `plugin/si-plugin/docs-b/done.md` (the commit core's out-of-scope-dirty-path detection), `CLAUDE.md` (the Rezip ritual's `-testN` section).
**Routed to Captures:** none.
