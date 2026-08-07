# [HASH] — A silent write of the user's absolute path into their repo removed, the tracked file deleted, and the published copies routed to the history rewrite

**Red flag · State: cleared** — carried through from processing, where it was cleared by designing the fix and telling the user plainly what deleting the file does and does not achieve.

`session_start.py`'s `_record_payload_once` wrote `resources/research/session-start-payload-sample.json` into the project whenever that folder existed. Nothing documented it — not SPEC, not the FAQ, not a procedure doc — so no user had any reason to know it happened or to look for the file.

**What was found here, checked rather than reasoned about:** the file existed, was **tracked and committed**, and held `cwd` — the absolute path of the project folder, including the Windows account name. This repo is public, so that path was readable by anyone and is in the history permanently.

**The severity, stated in both directions.** For this project it is a smaller exposure than one already queued: every commit here carries the user's real email address, which [history-rewrite-third-party-scrub] exists to remove, and that rewrite already touches every commit — so this string rides along in the same pass rather than needing an operation of its own. What earns it its own item is the **mechanism**, which is consumer-facing: any user whose project has a `resources/research/` folder got their own absolute path written there silently, with no doc telling them, no gitignore covering it, and every reason to commit it without noticing.

**Deleted rather than gitignored or gated behind a runtime prompt.** The need it served was a genuine one-off — establishing whether the desktop app omits the `model` field or sends it malformed. That question is answered, and the answer is preserved where it belongs: the payload carries exactly three keys, `cwd`, `hook_event_name` and `source`, which is the basis of the recorded `Model:` setting. A mechanism that keeps running after its one-off need is met is pure exposure. The removed function's site carries a comment recording all of this, including the condition on any future revival: it must be documented in SPEC and the FAQ and must never write into a user's repo unasked.

**Said plainly at build time, because it is the part that matters and is easy to gloss:** removing the file forward does **not** remove it from the history. That is exactly why the rewrite is the route for the published copies. A note was added to [history-rewrite-third-party-scrub]'s replacement set — with the instruction to derive the literal from git history at build time rather than from the queue, since writing the path into a queue in a public repo would republish precisely what the rewrite exists to remove.

**Files touched:** `plugin/si-plugin/hooks/session_start.py`, `resources/research/session-start-payload-sample.json` (deleted), `QUEUE.md` (the note on the rewrite's replacement set)
**Routed to Captures:** none
