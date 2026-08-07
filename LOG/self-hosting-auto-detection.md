# 96166c6 — Detected self-hosting at session start and suppressed the version-drift check, silently

The item's long-standing crux — what would detection switch on that ambient CLAUDE.md cannot? — was answered by an observed instance rather than by argument. A planning session opened with `session_start` reporting *"Plugin version changed since this project was last set up (1.12.0 → 1.19.0-test1) — an update has been installed."* That check exists for a consumer, to tell someone building their own app that their plugin updated. **In this project it is meaningless and permanently wrong**: `.si-version` records the version that ran /setup while `plugin.json` carries the current one, and the two can never agree again, because this is the project that produces the versions. Every rezip widens the gap by design, so the line fires at the top of every session, forever, carrying no information.

**And it is not alone** — the missing-setting top-up, retired in this same run, is the same family: consumer machinery running where it does not apply is the pattern, not one stray line.

**Why suppression is the payload that earns detection, stated plainly because the item's whole difficulty was that nothing did.** Ambient CLAUDE.md is prose; prose cannot stop a program printing a line. Every other candidate payload — a self-hosting banner, guarding host/target confusion — is information that could simply be written in CLAUDE.md, so none of them needs detection. Suppression does, because the thing being changed is a hook's behaviour.

The trigger is the plugin package living inside the repo the session was opened in. The anti-nag safeguard from the original capture stays: on the trigger firing, the hook checks for a recorded marker; if absent it asks **once** — "this looks like you're developing the method itself; is that right?" — and records the answer. A recorded "no" is honoured permanently, which cleanly covers the detected-but-not-wanted case. The recorded sign is what turns a would-be per-session nag into a single ask.

**Suppressed means silent, not "reported as suppressed"** — the behaviour rules are explicit that a silenced check contributes nothing to the opening narration, including no mention that it was silenced.

Verified live at build: this project returns *unknown* (so it will ask once), a bare folder returns *no*, and both recorded answers are honoured.

`CLAUDE-TEMPLATE.md` deliberately gets nothing: the marker belongs to a self-hosting project, which is seeded by cloning the repo rather than by /setup, so a consumer's scaffold must not carry the field. Recorded because the instinct is to add it.

The seeding question stays deliberately out of scope — two doors already solve it, and detection's value was never seeding.

**Files touched:** `plugin/si-plugin/hooks/session_start.py`, `SPEC.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`

**Routed to Captures:** none
