# [HASH] — Taskflowapp pair read together: 5 findings from a run that stalled twice, for two unrelated reasons

Both transcripts slimmed to conversation text the same way as the sibling pair — 87 turns kept from the planning session, 14 from the build — and read planning first. Unlike the sibling, this build genuinely stalled, and it stalled twice.

**The first stall was the queue's.** Six of the 26 cleared items could not be scoped, and the run stopped before locking scope rather than inventing what they meant: a tier model naming no billing library, cloud sync whose backend was never chosen, an MCP setup screen pointing at a server with no host, that server itself, a reconciliation item depending on it, and a content item waiting on words still unwritten in Unprocessed. All six were already in the ready region from earlier sessions. The planning run hours earlier worked the fourteen unprocessed captures, reported "24 items cleared to build", and flagged nothing. The digest is meant to report an item whose file list names nothing to change; whether it failed to reach these items or reported and nothing surfaced was not established, because the digest was not run against that queue — so the capture states what was observed and names the diagnosis as outstanding rather than asserting a cause.

**The second stall was the build's own.** A Gradle build was piped through `tail`, the pipeline's exit code was read as the compiler's, and the compile was reported as passing when Gradle had already failed. Then, with the real failure visible, the run concluded it could not compile and offered to carry on uncompiled — without asking whether Alex could build. She quoted the rule back: *"you're supposed to ask me if I have android studio then add it to a list of tools the project has on hand, as I understand Throughliner method"*. Claude's own correction names the defect precisely — what it had established was "can't compile *from my shell*", not "can't compile". The session ended there with the question open and twenty items part-built.

Her second expectation had no answer at all, and that became its own finding: the facts that session established — where the bundled JDK is, where the SDK is, that Gradle's daemon fails from Claude's shell specifically — have nowhere durable to live, so the next session re-derives them or repeats the assumption.

The fifth finding is from the planning half: a sent-register line recorded three answers as sent when the message that went out contained none of them. Claude caught it within the hour, but the register exists precisely so a later repeal can be checked against what was really claimed, and a line written from the session's decisions rather than from the approved text defeats that.

**Clean passes:** a two-option question answered "yes" was re-asked rather than guessed at, on a delete; the `Not before:` date was proposed with its reasoning and approved rather than applied silently; both outbound replies were shown in full before sending.

Files touched: none — an audit edits nothing outside the scratchpad. Read: `536b761a` (planning) and `8731b6b2` (build), both under the Taskflowapp project.
Routed to Captures: [unbuildable-items-persist-in-the-ready-region], [piped-check-reports-the-wrong-exit-code], [environment-check-skipped-user-had-to-cite-it], [no-home-for-a-projects-tool-facts], [sent-line-written-from-decisions-not-from-the-message]
Approval outcomes: all five findings approved as-is, in one pass.
Rule gate: not needed — an audit authors no rules; findings become captures.

Every finding was checked against the current build before being filed as live. Depth: full, alternative seriously weighed. Ticked as done, confirmed.
