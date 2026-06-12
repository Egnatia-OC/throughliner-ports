# LOG entry — git-add-safety-hook-gap

## [HASH] — /next [git-add-safety-hook-gap]: pre_tool_use git-safety extended — blanket adds and commit -a denied, every denial teaches the fix

The File safety rules forbade blanket adds in prose only, while the hook enforced just the two destructive commands — and a weaker model is far likelier to reach for git add -A than a force-push. The gap was exactly hook-shaped: a regex on command text, with the denial message doing the teaching at the moment it matters. pre_tool_use.py gains two patterns — blanket adds (git add -A / --all / a bare-dot token) and blanket commits (git commit -a / -am / --all) — with boundary care so near-misses pass: explicit paths, ./path forms, dotfiles like .gitignore, --amend, --allow-empty. Both new denials teach explicit staging: name each path.

Both fold-ins landed as designed. Every git-safety denial — the existing pair and the new pair — now carries the patterns-as-data note: the check matches the command's text, not its intent, so test strings, quoting, and documentation trip it too, and the message tells the reader to assemble such strings at runtime. Weakening the patterns to skip quoted contexts stayed rejected — a safety guard loosened to absorb formatting noise invites bypasses. The scope-lock not-in-list denial now states the Files: bare-path rule, and next.md states it where Files: lines are authored, so an annotation-broken grant self-diagnoses at denial time instead of after source-reading.

22 synthetic payloads against the edited hook all pass: 11 denials carrying their teaching lines, 9 near-miss allows, and the two scope-lock cases (an annotated Files: line denied with the bare-path rule named; the same line bare grants). The live host-side denial can't run until push + reinstall — written to Deferred tests. One discovery from the build routed to Captures: the parser already silently strips dash-separated annotations from Files: lines (parentheticals are what break), so the code is partially tolerant while the decided rule says bare paths only — whether the dash-stripping goes is /plan's call. A second capture, raised by the user at close: the Deferred tests section surfaces pending tests at every /next but nothing triggers their execution; reinstall-gated tests have a mechanically detectable runnable moment (the session-start version check), user-run and external-event tests don't.

**Files touched:**
- plugin/si-plugin/hooks/pre_tool_use.py: blanket-add and commit-all patterns, two new deny blocks, patterns-as-data note on all four git-safety denials, bare-path rule in the scope-lock denial, docstring updated
- plugin/si-plugin/docs/next.md: Files: template line and explanation state the bare-path rule and why
- QUEUE.md: batch removed at lock; deferred-test line added; two captures appended
- REGISTRY.md: pre_tool_use.py description widened to the new coverage
- LOG/plan-2026-06-12-3.md + LOG/index.md: prior entry's hash placeholders backfilled to 09be806 at session start

**Routed to Captures:** the dash-stripping inconsistency (partial tolerance vs the bare-path rule); the deferred-tests execution-trigger gap (user-raised — surfacing solved, executing not, trigger flavors differ)
