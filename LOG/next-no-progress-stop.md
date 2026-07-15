# [HASH] — Keep a lightweight no-progress stop in /next

Now that /next is the only runner and unattended in practice, a line that thrashes wastes the run with nobody watching. This is the one /cruise guard worth recycling: if the same error, an empty diff, or the same failing check repeats roughly three times on one line, /next stops and tells the user what repeated, routing through the existing "Approach not working" path.

Deliberately not a mechanical BLOCKED system — that was /cruise's, and it retired with it. This is an instruction to notice going in circles, framed as a judgment call: three is a rough trigger, and the point is surfacing a stuck line rather than tallying attempts.

The other /cruise hard-stops were dropped rather than recycled, and the reason is recorded here so they aren't re-proposed: an iteration ceiling and a per-run budget ceiling are both arbitrary (no principled number) and undetectable (the model can't see spend or reliably count its own iterations). Session length is handled at plan time instead — see [session-sizing-and-break-lines].

Landed as a new "Going in circles" subsection in next-build.md's Mid-build course-correction.

**Files touched:**
- plugin/si-plugin/docs/next-build.md: new "Going in circles" subsection under Mid-build course-correction

**Routed to Captures:** [next-rules-missing-faq-entries]
