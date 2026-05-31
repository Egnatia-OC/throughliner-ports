# V154 — 2026-05-31 — Merge Ideas into OQs + combine ideation/deliberation

**What shipped.** BACKLOG drops from 6 sections to 5 — the Ideas section is removed entirely, and its function absorbed into Open Questions (which now accepts light entries). `/sovideate` skill and `ideate.md` procedure deleted; `/sovdeliberate` absorbs both activities (OQ work-through and new idea capture). All 25 files across plugin templates, procedure docs, hooks, guides, and dev docs updated to remove Ideas as a separate concept. Consumer-project backward compatibility preserved via legacy-handler in the deliberate procedure.

**Decisions taken and why.** Keep `/sovdeliberate` (don't rename) — resolved in v153 deliberation. Quick thoughts land directly in OQs using a lighter format (heading + Surfaced + one sentence) rather than requiring full Why-it-matters / Next-step. The `IDEA_CAPTURE_PATTERNS` in UserPromptSubmit now route to the deliberate flow instead of a separate ideate flow.

**Pivots and surprises.** Three of six crash-course HTML files (disciplines, docs, walkthrough) had no references to update — verified by grep, no changes needed. The `replace_all` on `planning.md` created a duplicate sentence that needed manual consolidation. PreCompact hook blocked `/compact` after recap (see OQ "Pre-compact hook over-detects build phase").

## Performance
- **Batch completion:** Complete
- **Files in batch:** 25
- **Carve-outs:** None
- **Claude-verified tests:** 3 Pass, 0 Fail (of 3 total)
- **User-verified tests:** 1 pending
