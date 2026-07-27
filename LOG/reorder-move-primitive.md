# [HASH] — new scripts/reorder_queue.py + plan.md close reorder: mechanical byte-for-byte queue-reorder mover with self-check

/plan's close-out reorder asks Claude to re-sort the queue sections, but the only edit primitive is exact-string replace — so moving a work item means retyping its whole prose block verbatim, twice. Items run several hundred words, so on a long queue the sort silently degraded to a partial move, and a single transcription slip would corrupt an item with no error. The fix (decided 2026-07-25) was a mechanical mover, not accepting partial sorts or forcing items to stay short.

Built `plugin/si-plugin/scripts/reorder_queue.py`: it takes a section and the full desired top-to-bottom slug order, moves whole `####` blocks byte-for-byte, and self-checks before writing — same slug set before and after, each block's content preserved, marker presence preserved, and nothing outside the section changed; it refuses to write and exits non-zero on any failure. The cleared-to-run marker is placed via `--marker-after <slug|TOP|BOTTOM>` (omit to keep its current position). Output spacing is canonicalised so an identity reorder is a clean no-op. Only the *decision* (the slug order) passes through Claude; never the prose.

Design questions settled: (1) the skill locates the script relative to the plugin root (grandparent of the skill's base directory), so it resolves wherever installed — not a hardcoded path; (2) the ordering input is an ephemeral slug list, used once and discarded, deliberately NOT a persistent queue index (a standing index would invite proxy-reasoning from compressed lines, which the method forbids). The script ships in the plugin package and reaches consumers on reinstall.

Tested during the build: identity reorder is byte-identical; swaps and marker moves are correct with spacing preserved; a mismatched or bad slug set is refused with no write (caught repeatedly as the queue gained items externally mid-session).

**Files touched:**
- plugin/si-plugin/scripts/reorder_queue.py (new)
- plan.md (Step 3 "Reorder both sections" — invoke the mover; locate relative to plugin root; trust the self-check)

No SPEC/FAQ — internal reliability mechanism; the existing "Why did Claude reorder my queue" FAQ still covers the user-facing behaviour.

**Routed to Captures:** none
