# 7e3c1c8 — the queue mover can file a capture, and the hook exemption turned out to be unnecessary

`reorder_queue.py` gains `--append <Section> --body <path>`, placing a new entry at the bottom of a named section. The body arrives by file rather than on the command line, because a multi-paragraph rationale does not survive shell quoting on this platform — Claude writes it to the session scratchpad with the ordinary editing tools, which is already permitted, and the queue itself is still only ever touched by the script.

Addressed by section rather than by an anchor, which is the whole gain. Filing was the last queue operation done by hand: an exact-string edit anchored to whatever sat at the end of the file. An anchor read before the file changed underneath it put one capture into Processed above the readiness line, where a run would have tried to build an item whose entire content was three undesigned routes. It was found only because the user asked for an unrelated summary.

The always-loaded filing rule now names the tool, the way the keep-step names the mover, and states that it is subordinate to the ideation loop — the append runs once the loop releases the write, never as a reason to write earlier.

**`pre_tool_use.py` needed no change, and this was checked rather than assumed.** The item asked for the script-write ban to gain the same exemption the mover has. The mover has no exemption: the ban reads command text for write calls, and invoking a script file contains none. Running the new append through Bash confirmed it passes untouched.

Exercised against a scratch copy of the real queue — em-dash, quotes and a dollar sign all intact, a duplicate slug refused with nothing written — and used three times in this close to file its own findings.

Rule gate: run — a clause on the existing filing rule; the tool it names replaces a hand procedure rather than adding one.

**Files touched:** `plugin/throughliner/scripts/reorder_queue.py`, `plugin/throughliner/docs-b/skill-nonspecific-rules.md`
**Routed to Captures:** none
