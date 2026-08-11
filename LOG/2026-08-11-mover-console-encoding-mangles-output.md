# 08c885b — The queue mover's console output forced to UTF-8, so item headings echo back readably on Windows

Captured by the user from repeated instances — every deletion the mover confirmed printed the item's heading back with em-dashes replaced by a replacement character. The diagnosis and scoping are Claude's.

**Why it matters rather than being cosmetic.** The echo exists so the user can confirm the right item was removed, and a mangled echo is hardest to read against the queue on a heading that differs from another only in its middle — exactly when the check earns its keep. It is also a shipped script misbehaving on the platform every user of this project is on.

**Cause, confirmed by reading the script rather than assumed.** All eight console messages go out through `sys.stderr.write` — not stdout, as the capture guessed — and nothing reconfigured the stream, so on Windows it fell back to the console's ANSI code page and any character outside it was lost. The file handles were always opened with `encoding='utf-8'` explicitly, which is why the queue itself was never corrupted.

The fix reconfigures both error and output streams to UTF-8 once, at import, before any message is emitted, with `errors='replace'` so a console that genuinely cannot render a character degrades rather than crashing mid-edit, and a guard so a stream that cannot be reconfigured (an old Python, a pipe, a test harness) behaves as before rather than raising.

**No regression case was added, and that is a decision rather than an omission.** The failure did not reproduce in either shell available here — Git Bash echoed em-dashes and an arrow cleanly, and a direct PowerShell test printed the same characters correctly. A test written from this machine would assert the fix's shape and not its effect. [mover-encoding-fix-verification] is what settles it, and it is a `[user]` line that earned its tag on a real capability check.

**Evidence gathered incidentally at this run.** Every mover call this session went through the *installed* copy at the plugin cache path, and its echo was still mangled after the target was fixed — which is the expected result and a clean demonstration that the fix is host-side and needs a rezip before the verification item can mean anything.

The existing mover test suite still passes.

**Files touched:**
- `plugin/si-plugin/scripts/reorder_queue.py` — stream reconfiguration at import, with the reasoning in a comment.

**Routed to Captures:** none.

FAQ: not needed because the fix restores output the user was already meant to see — nothing about the workflow changed, only whether its confirmation was legible.
