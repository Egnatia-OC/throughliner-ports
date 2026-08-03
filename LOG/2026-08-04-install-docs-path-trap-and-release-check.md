# [HASH] — Give the install guide a command-not-found fallback and a version floor, and re-check the install path every release

The premise was corrected at capture: the install docs were already CLI-based, not stale in the expected way. What was actually wrong is more specific — the guide instructs a bare `claude plugin …` command that this project knows can fail with "command not found," and anticipates nothing when it does. A brand-new user's agent would hit that wall on the first step with no recorded way past it.

The fix is a fallback rather than an assertion, and that distinction is the whole point. Whether the PATH problem is universal or an artefact of one machine's install had never been checked, so stating it as fact would be building on an inferred limit — precisely what [harness-misbehaviour-diagnosis-order] forbids. The guide now instructs the install as before and adds: if the command isn't found, find the binary and run it by full path. Correct whether or not the bare command works elsewhere, one sentence, and a non-coder never has to learn what PATH means. INSTALL.md carries it as a line the user can paste to their agent; README carries the same in one sentence.

The unverified status is now recorded in CLAUDE.md's existing PATH note, and this session sharpened it: running `claude update` printed a warning that the native installation's directory isn't on PATH, which places the cause in the install method rather than in the desktop app. So it's an artefact of *how* this machine's CLI was installed, and whether other users hit it depends on how they installed. Recorded that way so a later session doesn't harden a local quirk into a claim about every environment.

A minimum version is now stated for the first time — 2.1.193 — since nothing anywhere named one and the rename work makes it concrete.

The standing check earns its keep on one argument: nobody who already has the plugin ever exercises the install path, so it can break completely and stay broken, and the only person who would notice is a new user who by definition can't diagnose it. Every other doc gets read by someone eventually. It rides the Push ritual's existing Pass B, which already reads project docs against what the unpushed commits changed — one more clause at a read moment that already happens, rather than a standalone gate that would be skipped.

**Files touched:** `INSTALL.md` (Branch B.1 — the fallback and the version floor), `README.md` (the Install section), `CLAUDE.md` (the Push ritual's Pass B clause, and the unverified-status note on the PATH guidance).
**Routed to Captures:** none.
