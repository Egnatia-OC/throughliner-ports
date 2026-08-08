# 7a4b377 — A throwaway PostCompact probe registered and rezipped, so the one unknown blocking compaction re-injection can finally be answered

Fifteen lines of hook and one registration entry, to settle a question that had
been quietly stalling a queued design for three planning sessions.

**Why the item existed at all.** [compaction-reinjection-via-postcompact-flag]
carried its own instruction — "do not process until the firing check has an answer"
— and was skipped at three consecutive planning sessions on that instruction, while
nothing anywhere was producing the answer, because the check needs a live
experiment and no item existed to run one. That is a roll-forward failure rather
than a queue working correctly, and this item is the thing that breaks it.

**The one thing being measured** is whether Claude Code's `PostCompact` hook event
actually fires in the **desktop app**, which is this method's platform. Everything
else was already settled: the event is documented, it is documented as *unable* to
inject context itself while `UserPromptSubmit` can — which is exactly the relay
shape the design proposes — and this plugin's `hooks.json` registers events as a
plain name-to-handler map, so nothing needed reshaping to add one. The precedent
for doubting delivery is concrete and close to home: the `model` field is documented
in the session-start payload and simply never arrives in the desktop app, which is
what killed the two-docset selector.

**The probe does exactly one thing** — appends a timestamped line naming the
payload's `trigger` field to `.throughliner/probe-postcompact.log`, then exits zero.
It emits no output, blocks nothing, reads no project state, and fails silent: a
probe that can break a session is not worth the answer. Registered with no matcher,
so it fires on both manual and automatic compaction.

**The log filename is constrained by a published contract, not a preference.** The
companion reader treats any `.throughliner/editing-*.json` file as an
edit-in-progress marker, so a probe file matching that glob would be misread as this
plugin editing a file forever. `probe-postcompact.log` cannot match, and the reason
is written into the probe's own docstring so nobody renames it casually.

**Removal is a stated condition, not an intention.** The handler, its `hooks.json`
entry and the log are all deleted at the close of whichever session reads the
result, whichever way the answer comes out — if it fires, the real relay is built
from the design and the probe is redundant; if it doesn't, the direction dies and
the probe has nothing left to measure. That condition also lives on
[user-postcompact-firing-check], which is the item that will actually run, so
deleting this item from the queue did not take the removal instruction with it.
`hooks.json`'s description field now carries the same warning, since that file is
where someone would meet the registration without any of this context.

**The release risk is real and is contained by an existing rule**, which is why
this was cleared rather than shelved: a probe registered in the plugin package
would ship to consumers if a release fired, and it cannot, because the release
trigger fires only on `main` and this work is on a branch. The removal condition
must still be honoured before this branch merges — a probe reaching main is a probe
one ordinary close away from being published.

**One premise of the item was false, harmlessly.** It specified adding
`.throughliner/` to `.gitignore` as a deliberate small widening, on the grounds that
this project doesn't carry it. It does. No edit was made and `.gitignore` was left
untouched.

**Verification and the rezip.** The probe was driven with a real payload: exit 0,
silent, one line written. The test log and its folder were then removed so a
rehearsal can't be mistaken for the real result. Rezip took the host from
`1.19.0-test5` to `-test6`, with the `__pycache__` clear and the cache prune, and
then ran the target-versus-installed stamp comparison that
[rezip-ritual-lacks-stamp-comparison-step] had added to the ritual earlier in this
same run — its first real use. Both stamps read `5cd5411acdb8`.

The run ends there. The app restart and the actual compaction are the `[user]` half.

**Files touched:**
- `plugin/si-plugin/hooks/postcompact_probe.py` — new.
- `plugin/si-plugin/hooks/hooks.json` — the `PostCompact` registration, and a description-field warning that it is throwaway and must not reach main.
- `plugin/si-plugin/.claude-plugin/plugin.json` — test version `1.19.0-test6` (working-tree only, never committed).

**Routed to Captures:** none from this item.

**FAQ:** not needed because the probe is a throwaway measurement deleted before it can reach a release; no consumer will ever meet it.
