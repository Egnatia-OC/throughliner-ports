# [HASH] — Caught structured shell writes in the scope-lock, and corrected SPEC's overstated containment claim

`pre_tool_use.py` returned early for every tool that is not Edit/Write/MultiEdit, so file enforcement never ran for Bash or PowerShell — those reached the git-safety checks only, which consult the build's file list not at all. The hook documented this about itself in its own header.

**Why it mattered more than the other known holes.** Elsewhere the lock is *off* in a named state. Here the lock is *on*, the session believes it is contained, and one tool class walks around it. It was the only hole in the one layer that cannot be skipped by instruction, so every doc-level scope rule rested on a floor with a gap in it.

Sharper prose was ruled out on evidence: three live instances, the decisive one inside an unattended `/next` run with no user present and no classifier in the way, while the session was editing the very file that held the capture warning about it.

**The build catches the structured forms only** — a write whose target path is literally present and extractable, a heredoc'd or `-c` Python script being the observed case. General shell parsing was considered and rejected as fragile: false denials train workarounds, which is the worse failure, and the independently-built tool this was compared against reached the same conclusion. Anything that does not parse cleanly **passes**, and that limit is stated in the denial text rather than hidden — a command whose target is computed at runtime is not detected, and the denial says so, naming it a gap rather than a permitted route.

The check runs only during a build, because outside one there is no agreed file list to check against and the planning gate already covers that stretch by design.

Every denial names the alternative — the editing tools, and the queue mover for the awkward removals that tempt a script route in the first place. That pairs with the sibling item shipped in the same run: this catches the attempt mechanically, that one removes the reason to make it. Both are worth having and neither substitutes for the other.

**SPEC was corrected in the same commit.** Its `pre_tool_use` paragraph described the scope-lock holding Claude to the agreed file list without saying shell tools reach the disk outside it. It now states the residual gap plainly rather than describing containment the hook does not provide.

**Files touched:** `plugin/si-plugin/hooks/pre_tool_use.py`, `SPEC.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`

**Routed to Captures:** none
