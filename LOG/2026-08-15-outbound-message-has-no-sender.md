# b4de5bf — Outbound INBOX messages now name their sender, in the filename and in the body

An arriving message named its host version and build stamp but not the project that sent it, and identifying the sender took five separate checks that still did not settle it. Version files record the version at the last /setup rather than the host actually running; the quoted preamble text is shipped scaffold and identical everywhere; one project was eliminated only because it happened to have no preambles at all; two projects then matched on every artifact readable from here. It was resolved by the user showing a screenshot of the sending session.

Both sites are enforced on the sending side, because the send is the only moment the sender is known for certain. A receiving-side check can detect that the field is missing and cannot recover it — which is exactly the position that session was in.

Both, rather than one, because they fail differently. The filename is readable without opening anything, which is what makes a mailbox triageable, and it is the half any move, archive or rename can drop. The body line survives every rename and is invisible until the message is opened, so it does nothing for triage. Two cheap redundant records of one fact, where the fact's absence costs a reply that cannot be routed — and a reply that cannot be routed is a reply that does not get sent, which is the part of the INBOX design that makes it a channel rather than a suggestion box.

The rule is an amendment to the existing outbound-send procedure rather than a freestanding rule, which is what carries it past the gate's more-than-once bar on a single recorded instance. A message being authored already has a defined shape; this adds a field to it.

Nothing migrates. Older archived messages are untouched and a sender running an un-updated host still omits the field — the cost of an unattributed message is one investigation, and the population is small and shrinking.

**The fix proved itself twice within this same session, in both directions.** The reply written at this close was named and opened by the new convention. And two other replies could not be sent at all, because their messages predate it and neither the address book nor the user could identify who sent them.

Rule gate: run — amends the outbound-send procedure in `feedback-and-inbox.md` by adding a required field. Admitted as an amendment with a named parent. Evidence is one recorded instance, below the bar for a freestanding rule and adequate for an amendment.

FAQ: not needed because Claude writes the message and the user only approves the wording; what changes is a line they will see in the draft, not a step they take.

**Files touched:** `plugin/throughliner/docs-b/feedback-and-inbox.md`.

**Routed to Captures:** `[unattributed-mail-has-no-recovery-route]` — the backlog half this fix does not reach, filed at the close when two replies proved undeliverable.

**Reply drafts held for want of a recipient.** To the queue-lint reporter: the scaffold now writes both section preambles as blockquotes, matching the lint's existing exemption; the wider exemption (all prose between a section heading and its first item) was refused because it stops catching a destroyed first item's stranded rationale; an already-adopted project repairs itself by prefixing those two paragraphs with `> `; no format-epoch bump, because those files are noisy rather than structurally wrong. To Hexboard: the trailing-slash-command report was right and is fixed at the rule level rather than at its three sites — a command offered inside an ask is now named in words and never ends the sentence — with `plan.md`'s end-of-queue gate, last-item checkpoint and rung-6 offer all reworded, and the standing caveat kept that the method will not contort its prose only to steer a third-party heuristic.
