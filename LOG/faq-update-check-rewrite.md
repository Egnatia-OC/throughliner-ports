# [HASH] — Rewrote the "just updated the plugin, how do I check it works?" FAQ entry to the two-section model

The FAQ template's update-check answer still described the retired deferred-test lifecycle — "the method saves up exactly these checks for after an update… it's set aside," and "/plan will line up what's worth checking into a quick test session." Both halves leaned on the deferred-tests machinery and the retired test-session type, which the two-section redesign removes. Rewrote the answer to the two-section reality: there's no saved-up-checks section and no separate testing session — you just keep using the plugin and capture anything that behaves oddly, and a check that genuinely can only be done by you is already waiting in the queue as its own `[user]` line. The index summary is the question title, which didn't change, so it stays as-is.

**Files touched:**
- plugin/si-plugin/templates/faq-template.md — rewrote the update-check entry
- plugin/si-plugin/templates/faq-index-template.md — reviewed, unchanged

**Routed to Captures:** none
