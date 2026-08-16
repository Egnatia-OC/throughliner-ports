# 0e62afe — /rescan ships as the method's fifth skill, and the close's wind-down shrinks to pick up where it stopped

The wind-down re-scan was welded to the close, and every addition to close machinery added weight to the end of a chat and pulled the whole chat toward ending. The user's complaint was that it was already naggy and getting worse. A second problem rode with it: a re-scan finding becomes a capture, waits for a /plan, then a /next, then a reinstall — the wrong lifecycle for a finding about the machinery being used right now.

/rescan is the same step with its own trigger. It scans back only as far as the last /rescan in the chat, which is what lets it run repeatedly without re-surfacing what it already surfaced, and what makes it cheap enough to invoke mid-chat.

Three things were settled at processing and carried into the built text rather than re-decided:

**It files and never builds.** The user's answer, and her reason: "plan does not build" — the standing boundary already answered this. Two supporting points are kept because a later session would otherwise re-derive them. Building on the spot would not deliver what the latency complaint wants, since the installed plugin is a frozen snapshot and a fix made mid-chat cannot reach the chat that made it. And a skill that could both route and build would let any chat change the project without the user having agreed to the work.

**No durable marker.** The stopping point is held in the conversation, with the captures filed earlier that day as the fallback where that memory is gone — which is undetectable from the inside, exactly as a compaction is. Her decision, and her reason: context is massive, so the loss is not a live concern. Rejecting a new artifact also matches this project's record of deleting the state files it invents. The objection that a re-scan finding nothing leaves no boundary is answered rather than accepted: a stretch that yielded nothing yields nothing again, so the cost is re-reading, not duplicate items.

**The close keeps a shrunken version.** Removing it entirely would cost a chat that never invokes the skill its whole safety net — and that net exists because things get thought out loud and never flagged, demonstrated the same day when a held post went unposted. The close now looks back only to wherever /rescan last stopped, so the weight disappears exactly in the case the user objected to and remains exactly where it is still needed.

**Files touched:** `plugin/throughliner/skills/rescan/SKILL.md` (new), `plugin/throughliner/docs-b/rescan.md` (new), `plugin/throughliner/docs-b/done.md`, `plugin/throughliner/.claude-plugin/plugin.json`, `SPEC.md`, `README.md`, `plugin/throughliner/templates/CLAUDE-TEMPLATE.md`, `FAQ/faq.md`, `FAQ/index.md`, `plugin/throughliner/templates/faq-template.md`, `faq-index-template.md`

**Routed to Captures:** none

Rule gate: run — admitted. Genuinely new territory rather than a refinement with an unlooked-for parent: no existing rule governs a user-invoked review step, and the part that does have a parent — the close's wind-down — is amended in the same build rather than left standing alongside it. **The eviction is real and named: the close's full re-scan is replaced, not duplicated.** Failure evidence is two recorded instances: the user's complaint about close machinery accumulating, and `done.md`'s own record of a positional re-scan running three times in one chat.

FAQ: updated — new entry "What is /rescan, and when would I use it?" It introduces a command rather than describing a changed behaviour.

No `FORMAT_EPOCH` bump — nothing here makes an existing project's own documents structurally wrong.
