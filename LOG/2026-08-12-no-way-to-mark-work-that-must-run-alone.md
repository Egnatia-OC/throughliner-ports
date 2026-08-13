# 16ed591 — The queue can now say "ready, but must run alone", and /next reads it as a second run bound

Until now the only thing standing between a large atomic change and a run that swept it up was its position in the queue and a sentence in its own prose asking not to be built alongside anything else. Position does not bind, and prose has no mechanism behind it. [rename-to-throughliner] had carried exactly that instruction for days with nothing acting on it; the /plan that cleared twelve items ahead of it made the gap visible rather than creating it.

A work item can now carry `Runs alone` on its own line, in the same shape as `Blocked by:` and the red-flag marker. /next walks the cleared region top-down as before, and on reaching a marked item: where the run has already built something it stops there and says plainly why; where the marker sits on the run's first item it builds that one and ends the run after it. Whichever bound comes first ends the run, so this composes with the cleared-to-run line rather than replacing it.

Three things were checked rather than assumed. The queue lint needs no change: `post_tool_use.py` is deny-list by design — its own docstring says novel structure passes in silence — and it holds no set of valid fields, so a new marker line passes untouched. The queue digest *did* need one, and got it: a solo item changes how much of the ready region a single run can clear, which is precisely what a planning session is deciding when it reads the digest. And SPEC needed two edits, because it described the readiness line as *the* run bound in two separate places.

The marker was also applied to [rename-to-throughliner] itself, so the mechanism ships with the case it was built for actually wired up rather than waiting on a future planning session to do it.

The limit is stated wherever the marker is described and must not be softened: this binds /next and nothing else. It does not stop the work being done alongside other work by hand, and it is never a guarantee that the item runs alone — only that an unattended run will not sweep it up. One further honesty: the marker could not bind the run that built it, because /next reads the installed host.

`[freeform]` was rejected as the vehicle at /plan and the reasoning is worth keeping: `[freeform]` marks work /next must **not** build, and this is work /next **should** build, just not alongside anything else. Widening it would give one tag two meanings and blur the precise case it exists for.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`, `plugin/si-plugin/docs-b/next.md`, `plugin/si-plugin/scripts/queue_digest.py`, `SPEC.md`, `QUEUE.md`, `FAQ/faq.md`, `FAQ/index.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`

**Routed to Captures:** none

**FAQ:** updated — "A build run stopped early and said the next job 'runs alone'. Why?"

Rule gate: run — admitted. Parent named: /plan's `[freeform]` placement discipline and the existing work-item marker set, so the plan.md half is an amendment consuming no slot. The next.md half is genuinely freestanding — a second run bound has no parent to subordinate to — and consumes one slot in next.md. Distribution: not always-loaded; the rule fires in /plan and /next and in neither /setup nor /done, so it fails the four-skills test and lives in the two skill docs that use it. Nothing evicted, because this adds a marker rather than restating one. Admission evidence at its honest strength: one realised instance plus a standing instruction with no mechanism behind it — not a repeated failure. Doing nothing lost at /plan because the protection so far had been luck. A hook was considered and rejected: the lint is advisory and cannot bind a run mid-flight. No bare number introduced.
