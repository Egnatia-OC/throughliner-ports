# 96166c6 — Slash commands are named in prose, never fenced

Reported from remote control with two screenshots: a session ended two messages — *"Run /done here to record the build and commit it?"* — and beneath each put a fenced block tagged **Bash** containing `/done`.

Checked rather than inferred: the shipped docs say nothing about how a slash command should be rendered. No rule required the fence and no rule forbade it. The procedure text models the right shape without ever stating it as a rule.

**Two rules collide to produce it.** The behaviour rules say fenced blocks are for code and shell commands; the harness instructs that a shell command the user might run goes in its own `bash`-tagged fence, because the app attaches a Run button to shell-tagged blocks. Neither excludes slash commands, so `/done` gets classified as a shell command it is not — run in a terminal it would simply fail.

**Why it is worse than untidy, and worse on remote control specifically.** The fence is the loudest element on a phone screen and carries an affordance that does the wrong thing, while the actual ask sits above it in ordinary text. The method already has a rule that no part of an ask may live only in the reply suggestions, for exactly this reason — a stop must be answerable from its own words. This is the mirror failure: the ask is present but out-competed by a control that misleads.

The fix is one clause on the existing fenced-code-block rule. Both of that rule's stated reasons for fencing — protecting characters whose exactness is the substance, and the Run button — argue *against* fencing a slash command rather than for it, so this is a boundary the rule was always missing rather than a change of direction.

The Claude Code half was filed separately and is done: an issue asking for either suppressing the shell affordance on a bare slash command or rendering it with the chip the app already has. **Nothing here waited on it** — the method clause is correct whether or not the app ever changes, because a slash command is not shell input and does not belong in a shell container regardless of how that container is rendered.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`

**Routed to Captures:** none
