# 96166c6 — Sent the behaviour rules to unadopted folders, and gave /setup the precedence line its siblings carry

**The exemption's stated reason had evaporated, confirmed by reading the hook rather than assumed.** Both docsets' `setup.md` justified omitting the behaviour rules by saying they "aren't loaded yet" because /setup runs before adoption. That described the **old delivery model**, where the hook inlined the rules into the session's context. It no longer does: the hook emits a directive telling the session to **read** `plugin-behaviour.md` from the installed plugin, and that file ships with the plugin, readable whether or not anything has been adopted. So the rules were absent not because they were unavailable, but because the unadopted branch did not point at them.

**And that same branch already accepts this exact argument for a different directive.** It deliberately emits the docset directive, with the reason written into the code: /setup lives in both docsets, so the redirect has to reach an unadopted folder or a 5-series session would scaffold from docset A while every later session ran docset B. Identical reasoning, already agreed, one directive away.

**Why the ungoverned window matters more than its size suggests.** It is the moment a folder is adopted and files are created — the highest-consequence moment in the method, and the only one a brand-new user ever sees. The response-shape tags in particular plainly apply there: a non-coder meeting the setup interview needs them more than anyone.

**Two things kept deliberate rather than tidied away.** /setup's local rules stay — leave the user's content untouched, never overwrite, never blind-rename, use the user's words verbatim. They are not replaced by inheritance; they are specific to adopting a stranger's folder, where belt-and-braces is the right posture. "These are now redundant" is the tempting and wrong read, so it is refused in the shipped text. And **no subset of the rules is carved out as pre-adoption-inapplicable**: rules referring to docs that do not exist yet are harmless, and the communication and safety rules are exactly what that moment needs.

**The docset-A freeze call was settled explicitly: A is corrected.** The claim there is false against the hook both docsets share, which is the correction shape the freeze permits, and setup.md is the one file the freeze excepts. Authored fresh in A's register, never pasted from B.

The precedence line lands in the skill file, which is shared by both docsets, so it reaches A for free.

**Files touched:** `plugin/si-plugin/hooks/session_start.py`, `plugin/si-plugin/skills/setup/SKILL.md`, `plugin/si-plugin/docs-b/setup.md`, `plugin/si-plugin/docs/setup.md`

**Routed to Captures:** none
