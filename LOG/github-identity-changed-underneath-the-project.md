# [HASH] — Corrected the project's GitHub identity to FlintcraftTech/throughliner after the rename happened outside the method

The user mentioned in passing that their GitHub username had changed because they needed the name for a new organisation. Checking rather than taking the heads-up at face value found more than it covered: the repo itself had already been renamed to `throughliner`, and the old username now belongs to an organisation.

Everything currently works because GitHub 301-redirects the old owner/repo path. That redirect is load-bearing and its behaviour in this specific configuration — old username now held by an organisation — has not been verified by anyone. Recorded as the thing to check rather than assume.

The scope came from grepping the literal strings at build time rather than from the discussion, and the fix corrects an **address**, not the product. The plugin's own identity stays exactly as it was: plugin name `sovereign-implementer`, marketplace id `flintcraft`, install target `sovereign-implementer@flintcraft`. Renaming the product is a separate queued job and must not be started here.

The honest consequence, stated in the shipped text rather than left to surprise someone: the install instructions now read slightly oddly — add a marketplace hosted at `throughliner`, then install something called `sovereign-implementer`. That is correct and working, merely inelegant, so README, INSTALL and the FAQ each say plainly that the mismatch is expected and not a typo.

This was done now rather than folded into the rename because the rename is held for a deliberate session with no date, and the install path is the one path this project's own release ritual singles out as never exercised by anyone who already has the plugin. It can break completely and stay broken, and the only person who would notice is a brand-new user who by definition cannot diagnose it.

The five research files under `resources/research/` were left untouched on purpose: they are dated findings recording what was true when written, and rewriting them would falsify the record rather than correct it.

Also recorded in CLAUDE.md for a later job: the GitHub no-reply address needed before any history rewrite, with the instruction to re-derive it at build time rather than trusting the written value, since the id is not guessable and the login has already changed once.

**Files touched:** `README.md`, `INSTALL.md`, `plugin/si-plugin/templates/faq-template.md`, `.claude-plugin/marketplace.json`, `CLAUDE.md`

**Routed to Captures:** none
