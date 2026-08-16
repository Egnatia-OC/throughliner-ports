# [HASH] — A session record gains a section for what the chat did outside its work items

The user's words: */done is not for wrapping up one next session or one plan session, it is for wrapping up ONE CHAT — that's why it is stupid that logs only record what was built or planned, and not everything that happened in the chat.*

The shape comes from the router: a build working file sends the close to the build path, its absence to the planning path, and each writes entries about the work items that ran. Anything the chat did outside those items has no entry to belong to, so it survives only if someone thinks to write it somewhere. Both closes were read at processing and the premise holds for both — each organises its entry around the work, and neither has anywhere to put something belonging to no item.

**The gap is narrower and sharper than "logs record the run".** `/rescan` already converts chat into **work**: it looks back for things decided, noticed or asked for and files them as captures. Nothing converts chat into **record**. A correction the user gives that changes shipped text is not future work — it is already done, and it was never a queue item, so it lands nowhere. That is precisely the class a capture cannot catch, because a capture is a thing still to do.

So the entry format gains an `Also in this chat:` section: corrections given, decisions reached in conversation, errors made and fixed, hand work between runs. The post-commit tail is the precedent and the proof of shape — a marked section in the entry that is not about any work item, already defined and already working. This is the same move applied one step earlier.

**A build-time correction to the item's own file list.** It named `done-build.md` and `done-plan.md`, with a note to check whether the shared entry format lives in `done.md` instead and not to add the same section in three places. Checked: both sub-docs delegate the format to `done.md`, so the section went there **once**. Following the file list literally would have put one rule in two files.

**The tension with the same run's subtraction pass is stated rather than left to be discovered.** [close-cost-scales-with-run-size] cut from `done.md` while this added to it. They are not in conflict — this adds content nothing else captures, that removes restatement of rules stated elsewhere — but the net effect on that file was growth, and the subtraction entry says so plainly.

Depth: full — the item's named files were wrong and the correct siting had to be established at build time.

Rule gate: run — admitted as an amendment to the existing write-the-LOG-entry format, which already defines what an entry contains; no freestanding rule and no always-loaded slot spent. Nothing evicted. Failure evidence is the user's own words plus three instances from the planning session that raised it, each of which shaped a decision and none of which had an entry to belong to.

FAQ: updated — "My session record has an 'Also in this chat' section. What goes in there?", with its index line.

**Files touched:** `plugin/throughliner/docs-b/done.md`, `plugin/throughliner/templates/faq-template.md`, `faq-index-template.md`, `FAQ/`.

**Routed to Captures:** none from this item.
