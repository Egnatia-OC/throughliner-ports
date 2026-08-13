# [HASH] — An out-of-scope request mid-run gets a reason, and a second ask carries a small edit through

`next-build.md`'s out-of-scope capture now reports with one clause saying why the
work is being captured rather than done. And on a second ask for the same intent,
Claude yields — carrying a minor expansion (one or two files) straight through,
while a significant one still proposes the split.

The design is the user's. Her reasons for the narration, in her framing:
capturing protects against drift, and it lets the item be processed in a second,
later context against work still to come — the most AI bang for your buck, and
better dependency management. Two Claude would add and did: a captured item gets
a keep-check and a file list before anything is written, which is what stops a
half-designed change landing mid-run; and it reaches the queue where its
relationship to other work is visible rather than being decided by whoever
happened to be in the room.

Three settlements, Claude's recommendations, agreed. **Minor only** — a repeated
request does not make a large change small, and absorbing a many-file change
mid-run is precisely what the run bound exists to prevent. **The narration fires
every time**, not only when the user sounds impatient: judging that is the
noticing-based trigger this method has repeatedly found does not fire, since a
session that has settled on an answer notices nothing. Firing always costs one
clause; firing on a judgment costs the cases it misreads. **One clause, not two
sentences** — the reason is given so the user can act on it, not taught.

Left open deliberately and written as such: what counts as a second ask. Same
intent in different words is right in spirit and cannot be specified without a
judgment call, so the text says plainly that Claude decides rather than pretending
a mechanical test exists.

The yield fits the method rather than bending it. Claude's standing rules already
hold that where a concern is raised and the user repeats the request, that is
their decision and the work proceeds. This is that pattern reaching build scope —
not a new permission model, which is also why it consumed no admission slot.

The mechanical step is preserved in the text: every file the expansion touches is
appended to the working file's `Files:` before it is edited, since the scope-lock
denies unlisted files.

Rule gate: run — admitted as an amendment to the existing out-of-scope and
scope-grows sections.

FAQ: updated — added "I asked for something during a build and Claude wrote it
down instead of doing it. Can I insist?"

SPEC and README were synced at the close as an approved scope grow.

**Files touched:** `plugin/si-plugin/docs-b/next-build.md`, `FAQ/faq.md`,
`FAQ/index.md`, `SPEC.md`, `README.md`
**Routed to Captures:** none
