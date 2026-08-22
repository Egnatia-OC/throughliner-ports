# [HASH] — The queue lint flags article-first headings on fresh captures

The always-loaded word-order rule did not fire on a capture headed "The brevity work went to…" filed into an outline of eleven consecutive "The" headings, and the user could not find it — the ninth recorded instance of a correctly worded rule with a stated site not firing, so per the record the fix is mechanical rather than louder wording. Two facts made the lint arm clean at the keep: an article at heading start is always wrong under the rule, so there is no legitimate case to false-positive on; and the lint's existing new-versus-HEAD split keeps existing headings quiet.

Built: an advisory check in post_tool_use.py — a `#### ` heading whose first word is The, A or An (a leading flavour tag tolerated) is flagged, with the message naming the word-order rule and stating the limit: the article case only, not a generically front-loaded heading, which needs judgment a lint cannot have.

Tick: done, confirmed — suite passes: article heading flagged, non-article passed, tag-prefixed article flagged, pre-existing article heading classified pre-existing rather than new.

**Files touched:** plugin/throughliner/hooks/post_tool_use.py, resources/testing/test_queue_lint_heading_articles.py (new)
**Routed to Captures:** none
Rule gate: not needed — hook code gains an advisory check; no method rule is authored or amended, and the always-loaded heading rule stands unchanged.
FAQ: not needed because the lint's advisory moment already exists; this is one more check inside it.
