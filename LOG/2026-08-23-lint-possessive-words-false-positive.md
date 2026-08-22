# [HASH] — Kept and cleared: the quote-claim lint narrows to introducer shapes, on a consumer's mailed false positive

A consumer project mailed a defect report: three correct items flagged because "her words" named a third party — items whose work is obtaining someone's words, so there is nothing to quote — with the flag re-firing on every queue write. Checked against current code the same session: the report holds; the check matches any listed possessive-plus-"words" phrase with no quote shape, blind to the referent, and does not honour an origin claim. The repetition half is already mitigated on current builds by the lint's split against the last commit. The fix narrows the trigger to the introducer shapes — the phrase followed by a colon, or "in her own words" — which are the shapes this project's own recorded failures took, while the consumer's sentence escapes both. Accepted miss stated: a colon-less bare claim passes unflagged. Also the first visible bite of the single-user assumption; the wider territory went to the [github-identity-naming] capture.

Rule gate: not needed — a hook script's match pattern narrows; no method rule text changes.

**Queue changes:** capture rewritten as a cleared build item.
**Work processed:** kept — [lint-possessive-words-false-positive].
