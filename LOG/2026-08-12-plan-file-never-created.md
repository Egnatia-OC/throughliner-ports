# 16ed591 — A planning close with no planning record now says so in the session record, instead of quietly reconstructing from memory

A /plan session processed roughly twenty items and never created its planning working file. Nothing noticed until the close reached for it and found nothing to read, at which point the entry's queue-changes and work-processed lines were rebuilt from conversation memory — exactly what the file exists to prevent, and exactly what a fresh or compacted session could not have done.

The close now branches explicitly. Where no planning file exists it writes a plain line into the session record saying there was none and that the entry was written from what could still be remembered, so it may be incomplete. Then it writes the entry as best it can.

What that buys is narrow and is stated as such in the doc: it does **not** prevent the miss. It makes the miss impossible to hide. A from-memory reconstruction reads exactly like a complete record, which is why the original failure surfaced only by accident; a stated absence is a gap any later reader can see. That is what the method's other required-artifact obligations do and all they do.

A `post_tool_use` check was the obvious alternative — it could notice a QUEUE.md edit with no planning file present, and it is close in form to the existing lint. It lost because it adds standing friction to every planning session forever, while the file's value is realised at the close and at a resume, so the nag would be paid continuously against a cost incurred rarely.

Simply repealing the requirement was refuted rather than merely rejected, and the evidence is the session that processed this item. It created its file and used it continuously — the chosen order and the reason for it, ten dispositions with their routes and rejected alternatives, and a note recording a mid-session queue corruption and its repair. Had that session compacted at any point, everything its close needed was on disk. The earlier session did not survive without the file; it got away without it.

**Files touched:** `plugin/si-plugin/docs-b/done-plan.md`

**Routed to Captures:** none

Rule gate: not needed — an existing close step gains an explicit branch for a case it already reached and handled silently. No new obligation and no always-loaded text.
