# d4f49bd — overnight blitz close: four items built, three captures filed, every unprocessed item triaged

The third run of `resources/overnight-blitz-plan.md`, on branch
`overnight-blitz-2026-08-06`. `main` is untouched and nothing was pushed.

## What was built

Four items, in two /next → /done cycles, each with its own scope-lock, log entry
and commit.

From the cleared region: **[commit-msg-tmp-permission-popup]** moved the close's
commit-message file to the session scratchpad, retiring the permission popup that
fired at every close; **[close-reliance-on-reply-chips]** added the rule that
every stop's text names the replies that let it proceed, both sides of any
binary, and reworded three close stops that had been leaning on the app's reply
suggestions.

Processed out of Unprocessed by this run and then built:
**[hook-internal-text-stale]** (filed by this run's own sweep) cleared retired
"batch" vocabulary from the plugin manifest and four code comments and corrected
`_fire_once`'s docstring against its caller; **[reorder-script-usage-string-underspecified]**
made the mover's error paths name the argument shape rather than only the valid
words.

The third cleared item, **[merged-plugin-live-verification]**, is `[user]` and
carries a set-aside marker — a hard boundary overnight twice over. Untouched.

## What was captured

Three, all from the run itself; none manufactured to fill a number.
**[docset-a-commit-msg-tmp-same-bug]** — docset A carries the identical root
temp-file instruction and the same untrue writability claim, which corrects
[commit-msg-tmp-permission-popup]'s own "docset B only" premise; held because
correcting a frozen docset is a call about the freeze, not a repair.
**[next-audit-route-step-untagged]** — a compliance-sweep finding; held because
which response-shape tag is right is a real call, not a typo.
And a third-instance note appended to **[claude-reached-for-shell-write-against-rule]**,
recorded below.

## The run's own slip, recorded because the project's rules require it

Removing a shipped work item from QUEUE.md, this run reached for a heredoc Python
splice instead of Edit — the third instance of the exact shape that capture
already records, and this time with the capture sitting in the file being edited
and having been read minutes earlier during triage. The write succeeded, the file
was verified intact against the committed version, and the session named it. It
happened in an *unattended* run, where neither a user nor the auto-mode classifier
was there to catch it, which is the condition the fix is actually for. The
remaining case for "state the rule more loudly" is now very weak; the item's own
candidate mechanical fix is the one that would have caught it.

The "file modified on disk since you last read it" warning fired once afterwards
and was **not** reasoned past: `git status` plus a heading-level diff against the
committed queue established the cause (the splice) and confirmed the structure
before any further write.

## The sweeps

Ran honestly and found little, which is itself the finding. The cross-doc
consistency grep over the shipped package found the retired-vocabulary drift in
the hooks (built) and confirmed that the Batches/Parked/Deferred-tests
vocabulary in `migrate-checklist.md` and `setup.md` is correct — those docs
describe the format being migrated *from*. The compliance sweep's tag-placement
lens found one genuinely untagged step (captured). Reading the hooks for
fail-open holes found none: the unscoped-build advisory, the malformed-Files
hardening, the planning gate's ask-never-deny and `_fire_once`'s
deliberately-fail-open direction are all sound and all carry their reasoning. The
queue lint produced no advisory at any point, on a queue edited a dozen times.

## Triage of everything left in Unprocessed — 34 items, and why each was held

This is the durable half of the handoff: the next /plan starts with its triage
already done.

**Both advisories** ([advisory-soak-blitz-branch-then-merge],
[advisory-cleared-run-then-history-rewrite]) — advisories are never processed.

**`[user]` items — hard boundary, need you live:** [report-url-404],
[respond-to-rygel-opencode-pr] (also outward-facing communication, held twice
over).

**Explicitly deferred by you already:** [setting-topup-mid-close] — the queue
records your call on 2026-08-06 and your lean toward retiring the mechanism
outright. Not for a blitz to reopen.

**Genuine design forks — the item names two or more real options and the choice
is yours:** [session-sizing-and-break-lines] (whether it is still worth building
for 5-series users at all), [next-start-order-handoff] (author into B now or
re-scope), [approval-flow-token-doubling-simplification] (three named options for
the consumer default, and it is an accessibility question about Pro-tier users
rather than a token-efficiency one), [post-close-tail-state] (is scope-lock-off a
bug to fix or a fact to state), [drive-testing-signals-skill-routing] (trigger
and destination unsettled), [done-delta-close] (trigger, keep/skip, log shape all
open), [self-hosting-auto-detection] (the trigger has no payload yet),
[plan-skill-did-not-engage] (harness quirk or method implication),
[skill-docset-override-unsanctioned] (follow the host, follow the project, or
halt), [scope-file-editable-vs-locked], [setup-runs-outside-behaviour-rules],
[method-advice-invents-capabilities-on-domain-mapping] (may split in two),
[no-standard-names-for-workflow-docs-vs-user-files] (a naming decision),
[memory-destination-invisible-to-the-record], [plan-session-order-diverges-from-file-order],
[plan-close-priorities-over-reorder], [bundled-double-ask-misapproval] (rule or
one-off), [next-audit-route-step-untagged] (which tag).

**Hook *behaviour* changes where the fix isn't fully stated — held by the blitz's
own boundary:** [shell-writes-bypass-file-scope-lock] (four options, a leading
candidate named but not chosen), [no-session-end-or-compaction-hook] (and it must
confirm the hook events exist before designing), [claude-reached-for-shell-write-against-rule]
(its fix is the same structured-write check).

**Held on other grounds:** [gitignore-scaffolded-faq] — the core fix is
describable but its two stated sub-questions are real, and it changes what /setup
does to a consumer's repo. [faq-as-claude-readable-reference] — explicitly a
hunch, and its first move is measurement rather than building.
[queue-pointer-hard-to-follow-and-possibly-stale] — tracks three external Claude
Code bugs; no method change is proposed, so there is nothing to build.
[move-to-vscode-extension] — a decision about your own working environment.
[retire-docset-a] — its conditions explicitly are not met (this branch is
unmerged and unsoaked, and the harness has not run). [docset-a-commit-msg-tmp-same-bug]
— a call about the freeze. [research-never-queued-for-next] — the rule itself is
settled in your words, but the item flags two open cases for processing (how it
sits with measurement-infrastructure builds, and with genuinely multi-session
investigations), so it fails the no-open-fork test by its own admission. Close to
buildable; a good first item for your /plan.

**One recommendation worth acting on:** [host-faq-stale-pre-redesign] and
[faq-backfill] are substantially the same work — the project's FAQ copy is two
months stale and both items conclude the fix is a wholesale replace from the
current template rather than patching. [faq-backfill] sits below the readiness
line in Processed awaiting your approval of exactly that recommendation, and
already carries the completed audit. Merging the Unprocessed one into it would
widen no scope. Held rather than done because the audit also recommends
regrouping the FAQ index under headings, which is a shape decision you should
make. This is also why this run's own new FAQ entry went into the shipped
template only and not the project copy — grafting it in would lose it at the
replace.

**Also worth naming:** [provenance-credit-audit] sits below the readiness line in
Processed, held only by a sequencing preference rather than by anything blocking.
It is an audit — it reads and reports and edits nothing — so it is the safest
possible thing to greenlight, and it has 40 credits to check with one known-bad
among them.

## Departures exercised, per the plan's override record

Approvals deferred: captures, log entries and commits proceeded without live
approval, all reviewable in the branch diff. Autonomous processing under the
softened bar: two items were moved from Unprocessed into Processed and built
without a /plan session, with the reasoning for each written into the item so a
disagreement has something to argue with. No push, no release: everything is
local on the branch, and the mechanical release trigger fires normally at the
first /done after you merge.

FAQ: updated — see `2026-08-06-stop-text-self-sufficiency.md`, which added the
one user-facing entry this run's work needed. The other three items were not
user-facing (a temp-file location, code comments, a Claude-only script's error
text), and each entry records that disposition.

**Queue changes:** four work items shipped and removed; two captures filed and
one of them shipped in the same run; a third-instance note appended to
[claude-reached-for-shell-write-against-rule]; the delivery advisory rewritten as
[advisory-soak-blitz-branch-then-merge]. Processed is down to 14 items with one
`[user]` item above the readiness line; Unprocessed holds 34 including two
advisories.
**Work processed:** kept and built — [hook-internal-text-stale],
[reorder-script-usage-string-underspecified]. Everything else held, with reasons
above. None deleted.
