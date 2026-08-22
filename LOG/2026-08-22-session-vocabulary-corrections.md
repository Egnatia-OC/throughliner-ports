# [HASH] — Every run-meaning "session" renamed to "run" across nine docs, from the audit's line list

The settled vocabulary (the user's decision, 2026-08-17): a run is a command executing, a session is the chat. The 2026-08-21 audit classified all 941 occurrences and listed ~50 run-meaning ones per file and line; this build renamed exactly those. Because the files had drifted since the audit's commit, each listed line was fetched from `15e10c9` by line number and matched by its text in the current file — no occurrence was re-classified and the stop-list was honoured rather than re-derived.

Renamed: next.md (3), plan.md (14), done.md (2), done-build.md (1), next-build.md (1), setup.md (2), skill-nonspecific-rules.md (5 occurrences on 3 lines, including the defining sentence, now "A plan run and a next run are runs of a command inside a chat"), rescan.md (2), SPEC.md (18). Deliberately left: the FAQ files (the audit found zero run-meaning occurrences there — the FAQ speaks the consumer's language where session means the chat throughout), `session_id` and the working-file name (harness-owned, per the item's refusal), and one audited next.md occurrence ("in a session whose whole premise…") that no longer exists — the restyle passes had already removed the sentence.

Tick: done, confirmed — each audited line located by its 15e10c9 text and edited; grep confirms.

**Files touched:** plugin/throughliner/docs/{next,plan,done,done-build,next-build,setup,rescan,skill-nonspecific-rules}.md, SPEC.md
**Routed to Captures:** none
Rule gate: not needed — a vocabulary rename applying an already-settled decision; no rule authored or amended.
FAQ: not needed because the FAQ carries zero run-meaning occurrences and nothing a user does changes.
