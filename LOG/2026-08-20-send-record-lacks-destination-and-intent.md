# b485ee3 — `INBOX/sent.md`: one line per outbound artifact, carrying destination, intent and what was claimed

Widened at processing to absorb two other items, both deleted once their content landed here. Raised by the user while asking whether an article had been passed to another project — checked rather than assumed, and the LOG entry said only *"she approved the exact text before it was sent"*. The design is Claude's, deferred to in her words: "as you recommend."

**Her rule, in her own framing.** A send may clear a work item where it hands that item to another project **for completion**. Where it defers only **continuation**, the item stays and a later capture wakes it. That rule gains operative wording here for the first time.

Three absences with one cause. No destination or intent on a send; no sent copy in the mailbox, whose archive holds twenty-two inbound messages and nothing outbound; and no record of what was announced, so a shipped change falsifies a past post unnoticed — the instance being the user's spec-driven-development post, inverted by [missed-spec-write-interrupts-the-run] in the same conversation and built in this same run.

One line per outbound artifact — mail, a feedback report, a GitHub issue, a public post, a delivered draft — carrying the date, the destination, the intent, what was claimed in one clause, and a pointer to the text that already exists. Written in the same turn as the approved send, because the text exists then and nothing later reconstructs it. No second copy of anything; the same shape as `LOG/index.md`.

It lives inside `INBOX/` because that folder is gitignored on every path and these lines name correspondent projects, which is the reason the address book lives there too. **The cost is the same and is stated rather than discovered: not version-controlled, so it can be lost.** `git check-ignore` was run against the new file to confirm the property the design depends on actually holds.

**One thing beyond the item.** This session had already made an approved send before the rule existed — the Taskflow message built as this run's first item — so its line was written into the new file rather than left as the first gap in a record created to close gaps. It is recorded as **for continuation**: the answers come back here, and [taskflow-personal-bridge] stays queued.

**Not built here — the check that reads it.** An item repealing shipped behaviour greps this file for the claim. That is a limb of [repeal-falsifies-a-posted-claim], which needed this file first; the ordering is written into both.

**Files touched:** `plugin/throughliner/docs-b/feedback-and-inbox.md` (the send flow writes the line, and the clearing rule), `CLAUDE.md` (the Discord section, host-only), new `INBOX/sent.md`, `faq-template.md` and `faq-index-template.md` with their `FAQ/` copies.

**Routed to Captures:** none.

Rule gate: run — the record obligation is a clause on the existing approved-send flow in a fetched doc, so no always-loaded slot is spent, and the user's clearing rule gains operative wording for the first time. Nothing evicted. Failure evidence is three recorded instances.

Tick: done, confirmed — `INBOX/sent.md` created and `git check-ignore` confirms it is covered.
