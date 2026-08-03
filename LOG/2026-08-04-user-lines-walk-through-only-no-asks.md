# [HASH] — Remove every completion ask from `[user]` items and retire the completion-mode setting they existed to govern

The user's own words: the asks around `[user]` items are jarring, don't feel right, and upset her every time. A standing reaction to a recurring pattern, not a one-off irritation. The instance that finally settled it was a close, immediately following a session that had walked one such item through from first step to result, asking which `[user]` items she had completed — listing all three in the queue. The answer was already fully in view.

The rule is now flat: a `[user]` line is walked through, and that is all. No completion ask anywhere in its lifecycle — not leading, not trailing, not as a light aside, and not in a planning session. What replaces it is inference from what the session can already see: a walk-through driven to its end this session is done, an item whose condition visibly hasn't cleared isn't, and the user mentioning one is the third way it can be known.

The counterargument was pre-empted rather than ignored. Some users would find a no-ask flow patronising; that's accepted, because they aren't the target market. The method is for novices, and being slightly over-helpful to an expert is a cost worth paying where irritating the target user is not.

The gap is written down deliberately, or it will be reinvented. Inference cannot cover an item completed alone between sessions with nothing observable to show for it. Such an item stays in place until the user mentions it — already a supported path. Stated explicitly in both the behaviour rules and the FAQ, because a future session will otherwise notice the hole and propose an ask to fill it.

This also resolved [user-completion-detection-doc-conflict] outright rather than by repair — that item recorded two docs disagreeing about *when* to ask, and with every ask removed the conflict has nothing left to disagree about. It was deleted rather than fixed. Its second, independent observation about the wind-down re-scan's ordering was rescued into its own capture first, since it would otherwise have gone with it.

Retiring the completion-mode field follows: it existed solely to toggle the /plan sweep, and a setting that governs nothing is a vestige that will confuse. The /setup question is gone from both docsets, the field is out of the template, and SPEC and README are corrected. Existing projects will keep carrying the line — no migration reaches every project — so a stale `Completion mode:` is now explicitly a thing to ignore silently, never an error.

The tension is recorded rather than glossed: the design had already tried twice to *minimise* this ask — the trailing note replaced a leading one, and completion mode existed to suppress the planning sweep. Both were mitigations of an ask nobody had questioned the existence of.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `docs-b/next.md`, `docs-b/done.md`, `docs-b/done-plan.md`, `docs-b/plan.md`, `docs-b/setup.md` and `docs/setup.md`, `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md`, `faq-template.md`, `faq-index-template.md`, `SPEC.md`, `README.md`, `QUEUE.md` (the deleted item).
**Routed to Captures:** [wind-down-rescan-runs-after-entry], [docset-a-completion-ask-inconsistency].
