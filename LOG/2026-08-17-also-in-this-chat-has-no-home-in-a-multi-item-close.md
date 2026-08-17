# dc52025 — chat-level record gets its own entry when a close writes several

The `Also in this chat:` section was authored against one entry per session, which is what a planning close used to write. A build close writes one entry per item, and the chat-level content belongs to none of them: on every entry it duplicates one text many times, on none it is lost. The close that first applied the rule put it on the first item's entry and recorded that as arbitrary.

Of the three shapes, the separate entry was taken. The two placement conventions — the last entry written, or naming which entry carries it — attach chat-level content to an item it does not belong to and then need a convention for a reader to find it. This matches what the content is: it belongs to the chat, so it gets a chat-level record, findable the ordinary way from its own index line. It is not a new kind of artifact, only a log entry with a different filename, so the index format is unchanged.

The condition falls out rather than needing an exception, which is what the authoring standard asks for: a close writing one entry keeps the section inline, unchanged, which is every planning close of the old shape; a close writing several writes the chat-level record separately.

The cost is one extra file and one extra index line per multi-entry close, against duplicating a text across many entries or losing it.

This close is the first to apply it, alongside the plan-entry split settled the same day.

Rule gate: run — a condition on the section shipped the day before; no freestanding rule and no always-loaded slot.

**Queue changes:** [also-in-this-chat-has-no-home-in-a-multi-item-close] kept into Processed, cleared to run.
**Work processed:** kept — [also-in-this-chat-has-no-home-in-a-multi-item-close].
