# 7a161aa — every stop's text must now name the replies that let it proceed, both sides of any binary

The reply suggestions Claude Code puts in the input box are the app's, not the
method's. They are generated from conversation context, they can be switched off,
they are reported to stop appearing for some users, and on remote control they
never render at all. So an ask that reads as a complete question at a desk can
arrive elsewhere as a bare statement with no visible way to answer it — which is
what happened when a close was relayed through a helper at the desktop: the
message carried "tell me any numbers to drop" and the accept side, "keep them
all", lived only in a suggestion. Closing that one session took about forty
minutes.

The rule lands in the behaviour doc as the general form of the existing
keep-going-or-stop rule, immediately beneath it, and it says the same thing about
every stop rather than one: write the stop so a reader holding only those words
can answer it, name both replies, and assume the suggestions are absent. The
mechanism is stated with it, because the reason a session would lean on the
suggestions is not knowing they aren't its own output.

The wording pass then fixed three close stops. The drop-offer at the wind-down
re-scan is the known offender and now names both sides. The shared LOG-entry
approval frame — the close's most-repeated stop, and the one most likely to be
read on a phone or handed to someone else — now says what a yes looks like and
what a change looks like. The session-file cleanup's deletion offer names both
replies too, because an offer that names only the delete side reads as an
announcement rather than a question.

`done-build.md`, `done-plan.md` and `done-audit.md` were checked and needed no
edit: all three delegate their approval ask to done.md's shared frame, so the fix
reaches them without a second copy of the wording to drift.

The alternative weighed and rejected: asking Claude Code to make the suggestions
steerable, or detecting whether they render. Neither is available — they are
app-authored and the method has no signal about them — and both would leave the
guarantee resting on someone else's feature. Writing self-sufficient asks costs a
clause per stop and works whether or not the suggestions ever appear.

No SPEC sentence was made wrong, so the spec-sync gate stayed silent; SPEC's
doc-bound-text paragraph describes how approval-time text renders and remains
accurate. No feature was added or removed, so the README feature list is unchanged.

Run under the overnight blitz's sanctioned departures (`resources/overnight-blitz-plan.md`):
approvals deferred, work committed to branch `overnight-blitz-2026-08-06`, no push
and no release.

FAQ: updated — new entry "Claude asked me something but I couldn't see how to
answer it. What happened?" in `templates/faq-template.md`, with its index line.
It explains whose the suggestions are, why they sometimes aren't there, and that
the user can always answer in their own words. The project's own `FAQ/` copy is
not patched: it is two months stale and awaiting the wholesale replace that
[host-faq-stale-pre-redesign] and [faq-backfill] both call for, so a single new
entry grafted into it would be lost at that replace.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md` (the new
Communication rule), `plugin/si-plugin/docs-b/done.md` (three stop wordings),
`plugin/si-plugin/templates/faq-template.md` and
`plugin/si-plugin/templates/faq-index-template.md` (the new entry and its index line).
**Routed to Captures:** none.
