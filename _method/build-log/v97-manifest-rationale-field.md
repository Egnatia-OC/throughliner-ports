# V79 — 2026-05-27 — Manifest rationale field

**What shipped.** MANIFEST entry format extended with an inline italic rationale suffix: `*Rationale: [why it exists / vNN].*`. Six files changed: DOC-STRUCTURE.md (format spec + proxy note), MANIFEST-TEMPLATE.md (comment updated), close.md (step 1 writes rationale on new and legacy entries), planning.md (V79 instruction to check rationale before UX edits), crash-course docs.html and index.html (MANIFEST description updated). 19 footers bumped V78→V79, version trackers updated. 184 tests pass, no regressions.

**Decisions taken and why.** Four design questions resolved at session open: (1) rationale stays out of MANIFEST proxy — dip-only, keeps proxy lightweight; (2) inline italic suffix over second line or parenthetical — preserves one-entry-one-line invariant; (3) session tag included — cheap pointer to build-log for deeper context; (4) planning procedure gets explicit instruction to check rationale before UX rewrites — closes the loop on why rationale exists.

**Pivots and surprises.** Reference manual already mentioned rationale (added anticipatorily in a prior session) — no update needed there. No parser changes needed — existing regex captures rationale as part of the description group, which is backward-compatible.

**Carried forward.** Nothing.
