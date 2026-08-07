# [HASH] — The session working file rescoped from resume artifact to the standing source of tracked-state claims

Claude presented an item as the session's last with one still remaining, then corrected itself. The count was reconstructed from conversation memory while a numbered list of all sixteen items — written at the start of processing, for exactly this purpose — sat unread in `_plan.md`.

The consequence was one wrong sentence. **The shape is the method's central design assumption failing:** the working file exists so a session does not depend on remembering, and the session remembered instead. The same reflex against a checkpoint's item, a disposition, or a skipped slug would produce a wrong queue rather than a wrong sentence, and nothing would catch it — the file would still say the right thing, unread.

**Verified by grep at processing, and the second finding is the sharper one: the working files are write-mostly.** `plan.md` says to create `_plan.md` and update it at each beat; the checkpoint says to *record* a skipped slug in it; nothing anywhere said to **read** it. `_build.md` has the identical shape in `next-build.md`. The only rule that said to read either was scoped to resuming — a single sentence in Context awareness. So the file was treated as a **resume artifact**, which means a session whose memory feels intact has no reason to open it, and that is exactly the session that gets the count wrong.

**The general form was taken over the narrow checkpoint fix**, on the reasoning above. But the trigger stays narrow as a design constraint rather than a caveat: a blanket "always re-read before speaking" would fire constantly and be ignored, this method's own recorded failure mode for over-firing rules. So the trigger names what it covers — assertions about the run's **tracked state**: how many items remain, which is next, what was disposed and how.

Three sites: `plugin-behaviour.md`'s Context awareness rescoped from resume-only to standing; `plan.md`'s checkpoint reads `_plan.md` before naming the next item and the count; `next-build.md` the same for `_build.md`. The third was marked "possibly" in the capture and is **in**, at the user's approval — an unattended run is where a wrong state claim has nobody watching, so it is the worse case rather than the lesser one.

**Worded as *composed from*, not *checked against*, and that is deliberate.** A count cannot be composed from a file that was never opened, whereas a verification can simply be forgotten. Same remedy shape as the pointer clause on [show-then-write-survives-at-step-level] — remove the availability of the wrong move rather than forbid it harder. The repetition is intentional.

**The honest limit:** no hook can tell whether a claim came from memory, so there is no mechanical backstop. One thing that already works and was not broken: the file is reliable when consulted — every disposition in both the observing session and the processing one was appended as it happened, and both records were intact.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/docs-b/plan.md`, `plugin/si-plugin/docs-b/next-build.md`
**Routed to Captures:** none
