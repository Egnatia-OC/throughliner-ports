# [HASH] — Stopped inlining the behaviour rules and FAQ index in the session-start payload — 54,886 characters down to 3,288, against a documented 10,000 cap

Every session in this project had been running without its behaviour rules, and nothing said so. `session_start.py` read `<docset>/plugin-behaviour.md` and appended it whole — 50,685 bytes in docs-b, 89,411 in docs — producing a payload of 54,886 characters. The harness kept a preview and filed the rest away, so only the state lines and the docset directive ever arrived.

The item's first build point was to establish the threshold rather than infer it, because two truncated data points (~53KB and ~90KB) support no design and this item had already been wrong once by assuming. Checked against the documented hook contract and the issue tracker: **hook output strings are capped at 10,000 characters**, and past that the harness saves the text to a file and injects a ~2KB preview plus a path. Confirmed by anthropics/claude-code#44086 and #70460. So the cap was a fact to build against, not a number to guess.

The rules are now pointed at rather than pasted: an unconditional read-this-first directive naming the resolved docset path. This is a **redirect, not progressive disclosure**, and the distinction is what reconciles it with CLAUDE.md's decision never to split this file. Progressive disclosure fails for standing behavioural rules because a session has no trigger that would make it fetch "lead with the decision" — moving those behind an index deletes their effect. An unconditional read defers nothing and hides nothing; the file is not split and no rule moves behind an index. The mechanism is already proven in this exact payload, since the docset directive was the one part that survived truncation and was followed.

The FAQ index went the same way, for the opposite reason: unlike the rules it genuinely *has* a trigger, so a one-line pointer does its whole job.

The trade is honest and was the reason detection shipped in the same pass rather than after: today's failure is loud in effect but silent in appearance, and a skimmed redirect would be quieter still. So the directive carries a self-check, and the payload's ordering comment now records the real cap instead of a vague warning about truncation.

Measured after the change: **3,288 characters**, with the rules directive present and the rules file's own body verifiably absent.

**Files touched:** `plugin/si-plugin/hooks/session_start.py`, `resources/testing/hook_schema_check.py`
**Routed to Captures:** none from this item
