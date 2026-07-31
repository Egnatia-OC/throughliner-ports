# ee238d1 — Add CLAUDE.md to the routing taxonomy and make placement a self-check (plugin-behaviour.md + FAQ)

Built in a six-batch goal session (plugin off).

plugin-behaviour.md's Routing and discipline rules named memory, SPEC, QUEUE, and LOG as destinations but never CLAUDE.md, and didn't draw the lines that actually get confused. Two misroutes recur: writing into CLAUDE.md what's really product truth (SPEC), and putting into memory what belongs in CLAUDE.md. The existing memory-boundary rule guarded memory-vs-project-docs but left CLAUDE.md unplaced.

Change (plugin-behaviour.md), extending the existing bullets rather than adding a parallel rule:

- **Doc routing bullet** — now a four-destination taxonomy: SPEC.md = what the project is; QUEUE.md = what to work on next; LOG/ = what happened; CLAUDE.md (this project's) = how Claude should work on this project. The two distinguishing axes are named: SPEC vs CLAUDE.md is "what it is" vs "how to work on it"; CLAUDE.md vs memory is "this project" vs "all projects." Placement is framed as an active self-check Claude runs on its *own* routing, not only a flag on the user's, with the two recurring misroutes named. A user-side flag is added: when the user frames product truth as a behaviour/instruction change ("make Claude always do X" that's really "the app does X"), name it as SPEC content.
- **Memory boundaries bullet** — gains a clause closing the CLAUDE.md-vs-memory loop: an instruction specific to this project belongs in this project's CLAUDE.md, not memory.

Raised by the user 2026-06-23. Relates to [spec-sot-rethink] (a clearer SPEC makes the line easier to draw — not a blocker, the line is conceptual) and [done-spec-sync-check]. [method-doc-structure-pass] may later relocate these routing rules, but it composes (structure vs content), so this proceeded now.

Deferred host-side line written (the doc text landing is a review, not a pass/fail test).
