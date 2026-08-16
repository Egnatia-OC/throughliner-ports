# [HASH] — The docset stamp reads `current`, and the folder keeps its name for a reason now written down

The user asked at a close why `docs-b/` was still there when docset B had been absorbed as the main method. She was right about the model — there is one docset, A was retired, nothing picks between them — and the naming is the residue.

**It is two changes, and only one is worth making.**

The **stamp** is renamed. `docset: B` appears in 14 frontmatter lines plus the self-check string `session_start` emits, and it is the part that literally says "B". `CLAUDE.md` rules out *removing* the stamp, correctly, because the behaviour-rules self-check is a live consumer and is the one guard proving the always-loaded rules reached the session at all. But it says nothing against giving it a value that implies no sibling, and a self-check asserts a new value exactly as well as an old one. It now reads `docset: current`. The stamp and the check were confirmed to still agree after the change, since a mismatch would silently disable that guard.

The **folder is not renamed, and this is a refusal on the record rather than a deferral.** The ripple was traced by grep first, as the hook-enforced-path rule requires: 639 occurrences, of which **only 215 are live** — 22 files including all five skill entry points, the session-start hook, four of the docs themselves, four test suites, `CLAUDE.md`, `SPEC.md` and the migration recipe. The other **424 sit in `LOG/` and one archived message.** A rename does not remove the "B"; it moves it out of a live path, where `CLAUDE.md` can explain it, and into 424 historical references pointing at a folder that no longer exists. Rewriting those is not available — the session record is what the whole method rests on, and editing it to agree with a later decision falsifies it. Same reasoning that left the deleted Codex port's commits unreachable rather than rewriting history full of hashes the LOG depends on. **The rename would create drift by fixing drift.**

`CLAUDE.md`'s note is replaced rather than kept. It used to say the stamp was vestigial and removing it would be churn — true, and insufficient, since it did not stop the user asking. The replacement states the real reason: 424 references in the session record name that path.

One file was deliberately left alone. `resources/plugin-behaviour-retired.md` still carries the old stamp, because it is a retired archive and marking it `current` would make it claim to be live.

Depth: short.

Rule gate: run — no rule authored or evicted. One frontmatter value renamed across 14 files and one paragraph rewritten to state a better reason for an unchanged decision. **A rename of the folder was refused outright**, which is the substantive disposition. Failure evidence is the user's own question at a close, with the explanatory sentence already in place and not preventing it.

FAQ: not needed — the stamp is internal to the plugin's own files.

**Files touched:** the 14 files under `plugin/throughliner/docs-b/`, `plugin/throughliner/hooks/session_start.py`, `CLAUDE.md`.

**Routed to Captures:** none from this item.
