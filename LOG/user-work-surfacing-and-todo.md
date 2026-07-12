# 80bb381 — plugin-behaviour.md + next.md: user-only discoveries now file as a `[user]` work line, not a plain capture, so user-actions surface as ordered queued work

The gap this closes: work only the user can do (a reinstall, a terminal command, a device check) would get filed as a plain untagged capture, so its next-ness — the fact that it's a concrete action, often one gating other work — survived only in whoever's session memory noticed it. That's the same "next-ness lives in memory" failure the `[user]` line and the readiness marker were built to remove.

The fix extends the existing discovery-decision rule rather than adding a new mechanism. The `[user]` flavor and its handover behaviour already existed; this build only routes discovered user-actions into it. In plugin-behaviour.md's Routing and discipline, the "not needed → capture and continue" branch now says: when the discovery is user-only work, file it as a `[user]` work line (leading tag) rather than an untagged capture, with the filing steps otherwise unchanged. next.md's `[user]` flavor definition gained a matching note that this is also the filing shape for a discovered user-action, cross-referencing the canonical rule.

The filing-vs-processing line is preserved: filing the `[user]` line stays an execution-skill move, ordering it into Processed by its dependencies stays /plan's — so nothing here crosses the no-planning-in-execution boundary.

Rejected and recorded (carried from the batch): a separate generated to-do list surface. Dropped because any surfaced list falls out of sync the moment the user acts on an item — the queue worked through /next is the surface, and a second list only adds something that can misreport.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md — extended the discovery-decision bullet with the user-only-discovery clause + why + filing/processing split
- plugin/si-plugin/docs/next.md — extended the `[user]` flavor definition with the discovered-user-action filing path

**Routed to Captures:** none
