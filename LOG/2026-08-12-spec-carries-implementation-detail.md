# [HASH] — The editing-state contract extracted to its own root doc; SPEC down 792 words to 5,367

**The extraction.** The editing-state signal's field-level contract — location, JSON field names, the version-2 migration and why it happened, per-edit firing, the recommended reader policy, the mtime-versus-`written_at` failure-direction argument, Windows path-case comparison, fail-open, the two known limits, housekeeping — now lives in `EDITING-STATE-CONTRACT.md` at the repository root, 1,048 words.

**SPEC keeps product truth and a link:** Claude publishes a signal saying when it is writing so another app on the same document can hold off; it is a heartbeat rather than a lock, so it fails open and a crashed session can never lock the user out.

**Why the repository root and not `resources/`.** This is a *published* contract another application is built against, so it cannot live anywhere a reader would not find it — `resources/` is a development folder and the wrong home. The doc says so in its own opening, so the placement survives a later tidy-up.

**The second, smaller cut: rationale inside the hook descriptions.** The `pre_tool_use`, `stop` and `post_tool_use` bullets argued for their design as they described it. The purpose-clause test was applied per sentence — delete it and read what remains; a complete statement means it was rationale, an unfinished one means it was operative. Four passages went that way (why a scripted write is blocked, what the earlier version let through, why the Stop hook exists, why the credential scan covers those files); the operative descriptions stand complete without them.

**Measured, because the whole item turns on proportion:** SPEC.md 6,159 → **5,367 words, −792**. The contract alone had been 1,035 words, 16% of the document.

**Why it was worth doing rather than tolerating** — and this sharpened during the run, because [spec-is-write-only-during-builds] shipped in the same session: /next now loads SPEC at every run start, so every word a build does not need is paid on every run. A 1,035-word interface contract is the clearest example of a word a build never needs.

**Out of scope deliberately:** no decision about whether SPEC survives at all (settled separately — it stays), and no rewriting for style. This removed content that belongs elsewhere; it did not compress content that belongs here.

**Files touched:** `SPEC.md`, `EDITING-STATE-CONTRACT.md` (new), `README.md`.

**Routed to Captures:** none.

Rule gate: not needed — no rule was authored or amended. This relocates reference content out of SPEC.md and applies the purpose-clause test to four rationale passages. SPEC is product truth, not method rules, and none of the always-loaded corpus was touched.
FAQ: not needed because nothing user-facing changes. The editing-state signal behaves exactly as before; its specification simply lives at a findable address now, and the README's existing paragraph points there.
