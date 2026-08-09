# [HASH] — Releases now run only when asked for, the rezip moved ahead of the push, and the push cleans the test version on its way out

The automatic release trigger is gone. From 2026-08-04 a release fired at any /done whose commits touched `plugin/si-plugin/`, and CLAUDE.md explicitly barred asking whether one was warranted, barred proposing to hold one back, and barred adding any condition. Alex stopped a release twice in her own words, most recently with "push and rezip only" — so following the document was producing exactly the behaviour she was interrupting.

The superseded reasoning is recorded rather than deleted, because it was sound and a future session reading it cold would restore the trigger in good faith. Welding release to push had made every routine save ask "is this good enough to publish?" — a question with no honest answer on a project that will never feel finished — so releases stopped happening and the work stayed invisible. That is outweighed, not refuted: an automatic publish the user has to interrupt is a worse failure than a release that waits to be asked for.

The intuitive compromise is named and rejected in the document itself, because it is the first thing a later session will reach for: keeping the trigger automatic but pausing once before publishing. That pause *is* the readiness question, and it is the exact moment Alex stopped both times.

The pre-revert state was checked before any of this was written, since the obvious alternative explanation was that the 2026-08-09 emergency revert had restored stale text. It had not — `7a4b377` carries the same automatic trigger and the same reasoning, so this is a genuine change of mind and needed recording as one.

The second half is Alex's, in her own words: the test copy should get pushed as well, rather than being generated after the push and left behind. So the rezip now runs *before* the push, and the build she actually exercised is the build the commit carries. That ordering only works with a version reset at the push, because the working tree now reaches the push holding a `-testN` suffix — and a `-testN` version reaching the remote has happened once already, when a session silenced the recurring dirty `plugin.json` by committing it and the public repo advertised `1.16.0-test4` until the next release. The push now resets to a clean number, closing that window to a single session.

That reordering also answered a queued capture rather than leaving both open: `[test-suffix-plugin-json-close-noise]` exists to silence the dirty `plugin.json` at every close, and with the push cleaning the version there is no recurring close-time noise left to silence. No close carve-out was restored to the shipped `/done` docs, and none should be — those ship to consumers who never rezip.

**Files touched:** `CLAUDE.md` (the Rezip/Push/Release section retitled and rewritten, the release-due `git diff` check deleted, the Push step given a version-reset step 1, the Release ritual retitled and its tag-lookup rationale moved to its top, the archive-accuracy paragraph corrected now that only Release builds the zip).

**Routed to Captures:** none from this item.

FAQ: not needed because the release ritual is host-only — consumers never rezip, push this repo, or publish its releases, and no shipped doc describes it.
