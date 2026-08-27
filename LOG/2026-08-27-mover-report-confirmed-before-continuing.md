# 99865ab — plan — [mover-report-confirmed-before-continuing] kept: mover runs confirmed from the tool's report, usage read before any retry

From the audit: the mover run three times to place the marker, usage read only after two wrong placements. The actual failure was retrying blind past the tool's own announcements, so the clause converts the report into the check — confirm the stated marker position matches intent; on a mismatch read the usage before a second attempt. Read-usage-first on every run was refused as taxing routine moves; the general verify rule's hand-over scope is untouched, as the capture itself wanted.

**Queue changes:** [mover-report-confirmed-before-continuing] filed and cleared; [queue-mover-help-read-after-two-wrong-placements] deleted as merged.
**Work processed:** kept — [mover-report-confirmed-before-continuing].
Rule gate: run at the keep — amendment; recorded on the item.
