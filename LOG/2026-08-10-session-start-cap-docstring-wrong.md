# 94bba66 — session_start.py's cap explanation corrected: the 10,000-character limit is per hook command

Split from [behaviour-rules-read-is-enforceable] at the keep-step because the two
halves differ in kind — this is certain and tiny, the other needs experiments
before anything can be designed.

The docstring on the rules-directive function explained that the rules are pointed
at rather than pasted because the file "is tens of kilobytes, so appending it whole
blew the cap by a wide margin and the rules reached no session at all." The Claude
Code hooks reference documents that cap as applying **per hook command**, not in
aggregate. The reasoning was therefore true of one command and did not say so.

Worth an edit rather than a shrug because it is a stated impossibility sitting in
the file a future session would open to design injection — that session would read
it and stop.

**Scope discipline: this corrects the explanation only.** The hook's behaviour is
unchanged, nothing new is injected, and whether multi-command injection is wanted
is still [behaviour-rules-read-is-enforceable]'s question. The corrected text says
plainly that the per-command limit is documented but that whether the harness
concatenates multiple SessionStart outputs cleanly, in stable order, with no
separate aggregate limit further up, is unverified here — an experiment nobody has
run. Evidence: `resources/research/hook-enforced-doc-reading.md`.

**Files touched:** `plugin/si-plugin/hooks/session_start.py`.

**FAQ: not needed because** it is a code comment; no behaviour changed.

**Routed to Captures:** none from this item.
