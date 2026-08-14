# 78fa417 — /setup now refuses cleanly during a build and describes itself during planning, and the update notice stops inviting the mid-session run

Captured by the user at a /plan wind-down, from a live instance in another project: a planning session was picked up partway through with a newly installed rezip, Claude rightly recommended /setup, and she ran it. Her framing is the finding — **/plan is normally always closed with /done, and /setup would come after that**, so a mid-session /setup is out of order and no step described it.

Read from the hooks rather than assumed, the two cases are genuinely different. In a planning session there is no build working file, so no scope-lock engages: writes to the usual few files pass silently and **everything else asks — never denies**. Nothing was blocked and nothing was silently bypassed. Mid-build is the serious case and worse than the capture first assumed: with a build working file present the scope-lock **denies** any path outside the run's file list, and /setup's scaffolding is never in a build's file list, so it would be refused write by write — the run halting or working around its own guard.

It recurs rather than being a one-off, because the trigger is a plugin update landing mid-session, which happens every time the plugin is updated while a session is open.

**Both open questions resolved yes.** /setup detects an active build from the working file's presence — the same signal the scope-lock already keys on, so no new detection was built — and says plainly that the build should be finished or closed first. And the plugin-update notice gains a clause saying /setup wants a session of its own, because that notice is what prompts the mid-session run in the first place. Refusing at the point of running is the backstop; not inviting it is the prevention.

**The 2026-08-13 narrowing was reversed, on the user's decision and on evidence from this session's own history.** That narrowing had put the planning half out of scope on the ground that it behaves acceptably. It does — but she ran /setup mid-/plan by accident on 2026-08-14, and it behaved acceptably **because the session stopped and asked what was meant, and no step told it to.** The stop was improvised from the project's state. So the earlier finding was right about the hooks and wrong about the procedure: nothing described the state, and the good outcome depended on the session noticing. A fresh short session is the design target precisely because it may not.

What the planning half needed was therefore smaller than the build half — not a refusal, since the planning case genuinely works, but a described route: say what is about to happen, note that the planning work is uncommitted and that /done is what records it, and let the user choose. **The failure to avoid is silence, not permission.**

**What this deliberately does not do.** It does not make /setup runnable during a build. Letting scaffolding writes through would mean the scope-lock yielding to the one command that most changes the project's files, which is the guard's whole purpose inverted. The fix is refusing cleanly, not permitting.

**Never exercised, and worth saying so.** No session has run /setup during a build; the conflict is read from the hook's behaviour rather than observed. It needs a plugin update to land while a run is active, which is rare — the user weighed that and chose to keep the item anyway.

All five suites under `resources/testing/` pass.

Rule gate: not needed — a procedure step added to setup.md and one clause on an existing hook notice. Nothing was added to the always-loaded corpus.

**Files touched:** `plugin/throughliner/docs-b/setup.md` (a new opening step carrying the build refusal and the planning-session route), `plugin/throughliner/hooks/session_start.py` (the plugin-update notice), `SPEC.md` (the Keeping-projects-current paragraph, which described that notice and said nothing about when /setup should be run).
**Routed to Captures:** none
