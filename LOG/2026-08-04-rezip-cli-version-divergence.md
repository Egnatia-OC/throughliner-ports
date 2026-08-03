# [HASH] — Update the standalone CLI, add a CLI-vs-app version check, and prune the plugin cache in the rebuild rituals

The Rezip and Push rituals drive a standalone `claude` binary to re-snapshot the plugin. That binary reported 2.1.146 while the desktop app ran 2.1.219. Nothing was broken by it today, which is exactly why it sat there — but the rename work depends on a marketplace feature with a 2.1.193 floor, so the migration could not have been validly tested with the binary the rituals actually drive, and it would have failed in a way that reads as the rename design being wrong rather than the tool being old. This project has already lost a session to a wrong theory about a version gap.

The CLI was updated in-session: 2.1.146 → 2.1.220, clearing the floor. Its own output then answered a separate open question — it warned that the native installation exists but its directory is not on PATH. That pins the long-standing command-not-found problem to the install method rather than to the desktop app, which is what let the shipped install guidance be written as a fallback rather than an assertion (see [install-docs-path-trap-and-release-check]).

A divergence check now rides the ritual, because the update goes stale again the moment it's made: compare the CLI's version against the app's, say plainly when they differ, and update first if it's behind. Cheap, and it keeps working after this particular update ages.

The second finding was folded in at processing rather than filed separately, because both are one-line additions to the same steps in the same file and two items editing them would collide. The plugin cache held ten installed host snapshots — every test build ever installed, none ever removed. Beyond disk, it makes "which host is actually live?" harder to answer than it should be, which cost real time earlier in the week. The rezip step now prunes to four, the same shape as the Push ritual's existing zip-archive prune.

**Files touched:** `CLAUDE.md` (Rezip step 3 — the cache prune; Rezip step 4 — the version check and the PATH note's status; Push step 11 — both applied to the release reinstall). Plus the CLI itself, updated on this machine.
**Routed to Captures:** none.
