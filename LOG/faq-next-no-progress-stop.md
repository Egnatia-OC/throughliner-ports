# [HASH] — faq-template + index: added FAQ entry for /next's no-progress stop

Two shipped /next behaviours were checked against the live FAQ. [next-no-progress-stop] — /next halts mid-run when the same error, an empty diff, or the same failing check repeats ~3× on one item, surfacing what repeated — is a narration moment a consumer meets and would ask about, and no FAQ entry covered it (the closest, the cleared-to-run marker entry, explains a clean stop at the line, not an error-repeat halt). So it earned an entry. [next-close-commit-rule] — one summary commit at a multi-item close — did NOT earn its own entry: the existing "committing vs pushing" FAQ already frames the commit at session-summary level.

This build authored one new faq-template.md entry — "Why did /next stop before finishing everything?" — explaining the no-progress stop (repeated error / empty diff / failing check ~3× → halt, naming what repeated, so a run never spins), plus its faq-index-template.md index line.

**Files touched:**
- templates/faq-template.md, templates/faq-index-template.md

**Routed to Captures:** none
