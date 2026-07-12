# [HASH] — plugin-behaviour.md Communication — added a "don't assume the user's environment" guard: surface the setup a step needs and let the user judge whether it's theirs

Claude defaults to assuming the user works in a terminal/CLI and often ignores the desktop app entirely — a poor default for a plugin whose users are non-coders who may never open a terminal. The new Communication bullet turns that around: wherever a step would presume a particular setup (suggesting a command, framing a step around a tool, asking for something needing a specific environment), Claude names the requirement plainly and lets the user judge whether it fits, rather than presuming. Placed right after "Run commands yourself" since both concern the user's execution environment. Authored 4.8-shaped — positive action, an exemplar, explicit scope. Split from [user-run-assumes-user-can-run] on 2026-06-23 as the broader default underneath the narrow test-routing case that fixed.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md: added the "Surface the environment a step needs" bullet to Communication rules.

**Routed to Captures:** none
