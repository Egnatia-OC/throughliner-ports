# 96166c6 — The scaffolded FAQ is a local copy of the plugin's help: never committed, and restored whenever missing

/setup copies the FAQ templates into every adopted project. Those files explain how the **method** works — they are not part of what the user is building, and they get committed into the user's own repo where they read as clutter.

**The framing changed at processing, and that change is what makes the build correct rather than merely tidy: the FAQ is not a document in the project, it is a LOCAL COPY of something that ships with the plugin.** That decides everything else — a copy is not committed, and a copy must be regenerable. Stating it as "gitignore the folder" alone would deliver the first half and silently break the second.

**So the guarantee ships WITH the ignore rule, or this is a regression.** If the FAQ is not in the user's history, a fresh clone on another machine has no FAQ at all — and the FAQ is what `session_start` points every session at. The rule is **"never committed, and restored whenever absent"**, not "add a line to `.gitignore`". Recorded emphatically because the ignore line is the obvious half and the restore is the half that would be dropped.

**An already-committed FAQ needs a real action, not a rule.** A `.gitignore` entry does nothing to files git already tracks, so /setup detects that case and **offers** the untracking (leaving the files on disk) rather than doing it silently or leaving the job half-done. It changes what is in the user's repository, so it is theirs to approve.

**The scope question is answered: the argument reaches the FAQ and nothing else.** SPEC, the queue and the log are the user's own record and belong in their history; their CLAUDE.md is theirs too. The FAQ is the only scaffolded artifact that is purely an explanation of somebody else's tool, so there is no slope to slide down. Answered explicitly so a later pass does not re-open it.

**This project needs no mechanism to protect it**, and that is written down so nobody adds a special case guarding against something that cannot happen: here the FAQ *is* the product, but a self-hoster arrives by cloning the repo rather than running /setup, so the rule never fires in this project at all.

**Docset A freeze call, made explicitly: docs-b only** — for this and for the sibling `.throughliner` gitignore entry. The freeze excepts setup.md so a /setup *question* changes in both docsets or neither, and neither change adds or alters a question; both add behaviour, which is development. The honest consequence, stated rather than discovered later: a 4.8 session running /setup will not write either entry, which fails safe (the files get committed, the status quo) rather than misbehaving.

**Files touched:** `plugin/si-plugin/docs-b/setup.md`, `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md`, `SPEC.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`

**Routed to Captures:** none
