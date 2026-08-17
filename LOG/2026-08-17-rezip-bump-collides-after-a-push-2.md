# [HASH] — the rezip reads its next test number from the plugin cache, not from plugin.json

`release-ritual.md`'s rezip step 1 now takes the highest `-testN` present in the installed builds and adds one, listing the cache directory to see them. The start-at-`-test1` branch is deleted outright, surviving only as the narrow case it is actually right for: a release bump starts a new release line, which genuinely has no prior test builds.

Two rules disagreed and each was right alone. The rezip said to read the current version and increment, or start at `-test1` where the base carried no suffix; the push strips the suffix, so the committed version always carries none. Every rezip following a push therefore read a bare version and named a build that already existed.

What that costs is worse than an untidy number. `claude plugin update` matches on the version string, so re-installing a string the CLI has seen is a silent no-op: it reports success, re-snapshots nothing, and the session carries on believing it runs new code. That failure happened on 2026-08-09 and cost most of a session. It was checked before deciding, because Claude's first hypothesis — that the suffix was merely a label — was wrong.

Both recorded misfires, 2026-08-14 and 2026-08-15, were avoided only by someone listing the cache, which nothing in the ritual asked for. Writing that habit in is the fix.

Full decoupling was refused: stripping at the release instead would leave the committed version carrying a test suffix between releases, and a `-testN` reaching the public remote has already happened once and was treated as a defect.

Rule gate: run — a rewording of an existing step. The eviction is the start-at-`-test1` branch.

**Files touched:** `resources/release-ritual.md`
**Routed to Captures:** none
