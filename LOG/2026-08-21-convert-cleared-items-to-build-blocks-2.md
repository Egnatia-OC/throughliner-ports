# 461c999 — Eleven cleared items converted to build blocks by hand, and the epoch-4 marker made true

The run of [convert-cleared-items-to-build-blocks]. The planning entry under the same slug — `2026-08-21-convert-cleared-items-to-build-blocks.md` — records the item being processed; this one records it being done.

It ran as it was written: by hand, with Alex present, because telling instruction from decision history is the judgment `migrate-checklist.md` reserves for a moment the user is in the room. /setup had written `.throughliner-format-epoch` as 4 while skipping the conversion it names, so the marker asserted a shape this project did not have — and the marker is what `session_start`'s migration halt reads, so nothing would have raised it.

**The marker was set back to 3 as the first act and to 4 as the last, both by Alex's own hand.** The scope-lock denies that file to Claude in a freeform session exactly as it does in a build, which the item had checked in the code rather than assumed. Between the two edits the halt was armed, which is what the marker is for.

**The state was measured at the start rather than taken from the item, and it had moved.** The item recorded fifteen cleared items with one block; the queue held twenty with six, several having been authored at their keep-steps since it was filed. Two `[user]` posts and the freeform item itself need no block. So eleven were converted: [split-action-defeats-the-bands-in-aggregate], [rename-docs-b-folder], [two-column-fences-wrap-unreadably], [slug-never-explained-to-the-user], [memory-masks-method-defects], [plan-entry-split-wording-disagrees], [law-prose-restyle-heavy-docs], [law-prose-restyle-remaining-docs], [rationale-lens-after-the-build-view], [repeal-falsifies-a-posted-claim] and [queue-privacy-default].

**Every block is a projection and nothing moved.** Each was drafted from the item's own prose, shown to Alex for a yes, then appended beneath that item's rationale, which stays inline and whole. Only refusals travelled out of the decision history, per the checklist; where an item's prose recorded a fact a build would need but no refusal covered — a corrected file path, an excluded file, a stale count that must not be used as a file list — that went in as a `Note:` line rather than being invented into the Changes section.

**The queue lint's standing flags went from eleven to zero, one per conversion.** Those had been reported at every edit as "already present in the last commit", which is the phrasing that made them invisible, and watching the count fall by exactly one each time is what confirmed the blocks were landing in the shape the lint parses.

**The checklist's second branch never fired**, which was not assumed: every one of the eleven said what changes inside which files, so none had to be moved below the readiness line and no fate decision reached Alex. That branch exists for items that never passed the keep check, and this queue had none.

**The check-it-landed step disagreed with its own section**, which is this run's one real finding rather than a defect in the conversion. The generator reports `20 cleared item(s), 17 with a build block`, and the checklist reads equal numbers as complete — but the three without blocks are precisely the flavors the same section excludes by name four lines earlier. Filed as [build-view-completeness-test-unreachable].

**Also found: the mailbox scan reported this project's own outbound send record as waiting mail**, with the surfacing text instructing that it be archived. Followed literally that would file away the artifact [repeal-falsifies-a-posted-claim] is built to grep. It did not happen, because the file was read and recognised — judgment covering for a mechanism, which is the class this project treats as a mandatory capture. Filed as [sent-record-surfaced-as-waiting-mail].

**Files touched:** `QUEUE.md` (eleven build blocks appended, the shipped item removed, two captures filed), `.throughliner-format-epoch` (by Alex, 4 → 3 → 4).

**Routed to Captures:** [build-view-completeness-test-unreachable], [sent-record-surfaced-as-waiting-mail].

Rule gate: not needed — no rule authored or amended, and no rule-bearing file staged. The blocks transcribe dispositions already written at each item's keep-step; nothing here decided whether a rule may exist.

FAQ: not needed because nothing shipped changed. This was a migration of one project's own queue, and no consumer does anything differently.

**Also in this chat:** the conversion ran one item per message with an explicit yes on each, per the item's own requirement that the blocks be written with the user rather than for them. No block was contested or reworded.

---

**Tail, appended 2026-08-21 from the planning chat running alongside this one.** This commit also carries two edits to [freeform-close-gives-no-opening-prompt] that were made in that chat and were sitting uncommitted in QUEUE.md when this close staged the file. Nothing was lost and nothing here is wrong — the text is intact — but this entry describes the migration only, so the edits were committed without being described. Recorded here rather than in the other chat's next close, because a commit's own record is where a reader looks for what the commit contains.

**What they added.** First, that the opening prompt this close's predecessor handed over was amended before use — *"the freeform item at the end of the cleared region **in QUEUE**"* — with the correction that Claude does know `QUEUE.md` exists at session start and does not have its contents, so a prompt must name the file rather than assume a term like "the cleared region" resolves. Second, that the prompt should say the session ends with /done, marked as the weaker half since the run asked for it anyway and it earns its place only on an interrupted or abandoned session. Also settled in passing: every `[freeform]` item implies a session of its own, and not every freeform session comes from an item.

**Why this is worth a tail rather than a shrug.** Two chats were open on one working tree, which the always-loaded rules say not to do, and the outcome was exactly the documented one — the two disagree about the queue from the moment either writes, and a commit ends up containing changes its record does not describe. The rule held; nobody was following it. Filed as an observation rather than a capture, because the rule already exists and needs nothing added to it.

