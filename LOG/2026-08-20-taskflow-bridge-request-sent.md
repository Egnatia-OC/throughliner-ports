# b485ee3 — Three asks sent to Taskflow, so the bridge design has something to talk to

[taskflow-personal-bridge] cannot state what it would build until Taskflow answers three questions, so this item existed to ask them rather than to build anything here. The asks were kept deliberately concrete rather than opening a conversation: whether Claude acting on the user's behalf breaches Taskflow's local-first principle — their SPEC says the app "does not import from, sync to, or export to any external task app", and the reading offered was that Throughliner is not a task app being synced but Claude, which their paid tier sanctions; whether an **additive** import is possible, adding named tasks and leaving the rest of the database alone, as distinct from the whole-database restore that already exists; and whether completions are readable from an export, so a parent task's roll-up state is visible from outside.

The permission question was raised and settled by the user in the planning session that kept this. The parent-folder instruction says Taskflow may be read freely and never written to, which as written forbids putting a file in their mailbox. Her decision was that INBOX is an exception to it, and the reason is hers in her own words — that it is a communication method, "not part of the product itself." The no-write rule protects Taskflow's own contents; a mailbox is correspondence rather than contents, so nothing it protects is touched. The rule text itself is amended by [parent-claude-md-taskflow-no-write-stale], built in this same run, and this item did not wait on it: a decision is in force from the moment it is made, not from the moment it ships.

Two things were checked before writing rather than assumed — that Taskflow has an `INBOX/` at all, and that its own `.gitignore` covers it, so the message cannot be committed into their repository. The exact text was shown and approved before it was sent, as with everything that leaves this machine.

**Files touched:** `Taskflowapp/INBOX/2026-08-20-from-no-code-method-bridge-asks.md` (created, 15 lines). Nothing in this project changed. The send's line in `INBOX/sent.md` was written later in the same run, once [send-record-lacks-destination-and-intent] shipped — recorded there as **for continuation**, since the answers come back here rather than the work being handed over.

**Routed to Captures:** [mail-send-should-not-need-a-queue-item], raised by the user immediately after approving the send.

Rule gate: not needed — no rule was authored or amended. This item's whole work product was one message file written into another project's mailbox; nothing under `docs-b/`, this project's `CLAUDE.md`, `self-authoring-rules.md` or `rule-maintenance.md` was touched.

Tick: done, confirmed.
