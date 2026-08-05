# Build procedure

Execution procedure for build-flavor work items. Reached from next.md after the run is confirmed and scope is locked. next.md routes here for each build item (a work item with no flavor tag); it handles `[audit]` items through their own doc.

## Execute [SILENT]

Execute the build item's work.

The silence here governs the success path — the routine bookkeeping of making changes and ticking the item when things go fine. It is not a gag on the moments that must speak: reporting a failure, asking before scope grows, and revealing a readable edit's new text (below) all speak. A response-shape tag on one of those specific moments overrides this step's silence — that's the precedence rule working as intended, not a conflict.

**No pre-edit preview.** Don't precede an edit with a point-form list of the changes you're about to make. The work was already agreed in /plan, and a "here's what I'm about to change" beat right before an edit that lands almost instantly is just noise. This holds for every edit, readable or code — the success path stays quiet until the item is done, minus that preview.

**Readable edits reveal their new text** [the reveal speaks; informational, not an ask]. When an edit changes readable (non-code) content — a doc, copy, a spec section, anything a person reads rather than runs — surface the actual new wording *after* making the edit. It's an informational reveal, so don't append an approval ask: the change was already agreed in /plan. Why it's worth surfacing: the exact wording is produced here in /next and was never seen in /plan, which agreed only the intent — so this is the first time the user meets the real words. A code edit doesn't get this half — a non-coder can't review code text the same way — so a code edit stays silent on the success path (still no preview).

**How the reveal renders follows the working-mode rule** (plugin-behaviour.md Working mode and view-in-doc rendering). The edited text is now doc-resident — its Write has succeeded — so it's a readable edit's post-write reveal, the doc-resident case: when mode is `local` AND an editor is recorded, point to it with a line-anchored link to the edited location rather than pasting the block, falling back to an inline excerpt or paste when a line-link won't resolve in the desktop app. When mode is `remote`, or no editor is recorded, paste the new wording inline as a wrapped, readable block — the user is on their phone and can't open the doc, so the words have to come to them. Either way the reveal happens only after the write is confirmed (write-then-verify-then-point).

**A small mid-build tweak to a just-surfaced readable edit is in scope** [PROMPT]. Once the new text is visible, the user may ask for a small "just change this one bit" tweak. A tweak that refines the build's already-agreed work product is refining the work, not new planning: make it, reveal the updated text, and record it in _build.md Changes so it folds into the LOG entry /done writes for this item — no separately logged object, and no /plan round-trip. A request that's actually new scope — a different feature, or a change to something that already worked — is not this; route it out via Scope management below, like any out-of-scope ask.

## Build the item

1. Read any relevant existing code or context.
2. Make the changes — no point-form preview first (see Execute above).
3. If the change is readable (non-code) content, reveal the new text — informational, no approval ask — rendering it per the working-mode rule above: a line-anchored link to the edited location when mode is local and an editor is recorded (inline excerpt fallback if the link won't resolve), an inline wrapped block when mode is remote or no editor is recorded. Code edits skip this; the success path stays silent.
4. Tick it in _build.md Progress: `- [x] item description — done`

**A check Claude can run is part of building, not a separate test.** When building the item, run whatever verification you can this session — read the code back, run a command, inspect output, check file content — as part of getting the item right. There's no separate test flavor: a check Claude can run is just building; a check that needs the user is a `[user]` work item, which /plan would have set as its own item and /next walks the user through, not something a build item defers. If, mid-build, you discover the work needs a user-run check that isn't already a `[user]` item, route it (see Course-correction below) — don't invent a deferral here.

## File structure — split by independent unit

When the build creates or grows the project's files and there's a choice about how to split the work across files, recommend a structure by this heuristic — it's guidance Claude offers, not a hard rule, so file structure stays case-by-case.

**Split by independent unit; keep reasoned-across content together.** Break the project into smaller single-purpose files along the lines of genuinely independent units — a self-contained tool, a standalone path through the app. But content that has to be understood as one connected whole stays in one file, even where splitting would look tidier.

The why, which is specific to a non-coder building with an AI: splitting into smaller files pays off *because the AI does the editing*. An edit's blast radius is one file, the AI reasons over less at once, and a mistake is contained by the file boundary rather than spreading across the whole project. That contained-blast-radius payoff is what makes the split worth its cost (each version has to be zipped and re-extracted), even though a browser opening files directly (`file://`) gets only shared-namespace `<script src>` splitting, not true module isolation — compiler-enforced isolation was never the point.

The counter-force that bounds it: an AI reasons *less* well across files than within one. So content the AI must hold as a connected whole — closely interdependent logic that's constantly reasoned about together — stays in a single file even when it's large, because splitting it would make the AI's job harder, not easier. Weigh the two forces per case: independent → split; reasoned-across → keep together.

## Rules during build

- Stay within the active run's described work — that's build scope (see plugin-behaviour.md Scope). Growing past it needs approval first (see Scope management below).

**Accumulate close notes** as you go — jot what changed in _build.md so /done needn't re-explore:
```
Changes:
- file1.ext: created new component, 45 lines
- file2.ext: added import + handler function
```

## Scope management

These sections elaborate the discovery decision rule in plugin-behaviour.md (Routing and discipline): work needed to complete the item is added or split; work not needed is captured and the session continues. The cases below are how that rule plays out during a build.

**When a mid-build discovery is work only the user can run — a rename Claude can't do, an account action, a device step — file it as a `[user]` work item, never float it as a live question.** This is the don't-under-file rule (plugin-behaviour.md Captures, Flavor marker): genuine user work must become a tracked `[user]` work item so it can't evaporate when the session ends. The failure to avoid is waving such work off as "separate work you'd handle yourself" or asking a yes/no question about it instead of filing it — that leaves real work living only in chat. If you can't yet script every step, file the line with a rough walkthrough anyway; not-yet-scriptable is not a reason to withhold it.

### User raises something out of scope [PROMPT]

1. Append it to Unprocessed in QUEUE.md, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Draft the wording first as a blockquote with a content-type lead-in (**Capture draft:**) for approval, per plugin-behaviour.md (Captures + approval-time outputs).
2. Ask "anything else?" — repeat until no.
3. Resume the build.

**Coherence exception:** Default is capture, per above. The exception is narrow and keyed to why-pipeline coherence: if the item would share the built item's log entry and index line — per plugin-behaviour.md Index entries — and folding it in makes the work easier to find later rather than harder, add it to _build.md as part of this item's work (appending any files it names to the `Files:` section) and continue. Evaluate against the coherence rules, not user convenience. When uncertain, capture.

### Scope grows during the build [PROMPT]

Both paths below ask and wait, so the tag sits on the whole section. If the work needs to grow past what the item describes — whether that means a new file or more change inside a file already listed — the trigger is the same: growth is measured against the described work, not the Files: list. Name the new work and the files it needs, then:

- **Minor** (a small prerequisite, one or two files): ask to add, naming the work and the files: "This needs [work], which means editing [file] — add it to scope?" Once approved, append any not-yet-listed file to _build.md's `Files:` section before editing it — the scope-lock denies edits to unlisted files.
- **Significant** (multiple new files, design uncertainty): propose splitting. Finish what's scoped, /done to close, then /plan to queue the rest.

**A SPEC change the build discovers it needs is a legitimate scope-grow.** SPEC.md is a normal file a build can add to scope. When the build finds a SPEC sentence must change for the work to be correct, treat it like any scope-grow: name the change and ask ("this needs SPEC to say X instead of Y — add SPEC.md to scope?"), and once approved, append SPEC.md to _build.md's `Files:` section before editing it (the scope-lock denies SPEC until it's listed). Then edit SPEC inline as part of the build. The why this is safe in-build: spec-driven development wants the spec to move in the same commit as the behaviour change, and the /done-build spec-sync gate (done-build.md) backstops it — that gate stops the close if the build changed product truth and SPEC wasn't brought into line. A SPEC change is product truth, so it always gets the explicit ask — it never rides in silently.

## Mid-build course-correction

### Claude discovers user-runnable testing is needed [PROMPT]

When Claude notices something will need user-runnable testing beyond what this build covers — a visual check, physical-device behaviour, a subjective judgment Claude can't verify — and it isn't already a `[user]` work item:

1. Append the discovery to Unprocessed in QUEUE.md as a `[user]` work item (what needs checking and why). Draft the wording, show before writing per plugin-behaviour.md Captures.
2. Ask "anything else?" — repeat until no.
3. Resume the build.

Don't attempt the check inline if it genuinely needs the user. Don't extend the current item's scope to include it.

**Before assuming a device or environment is absent, check.** When a check would need a device, emulator, or environment that "isn't available here," ask the user whether one is available rather than assuming none is. And before using any connected device, ask permission first: "May I use your connected device to test this?" — then wait for a yes. This applies the Device and hardware access rule in plugin-behaviour.md at the verification step. The why: a connected device the user didn't expect Claude to touch is a consent surprise, and a check wrongly skipped on a guess that no device was present sits unrun for weeks.

### Going in circles [PROMPT]

/next is unattended in practice — it works several items faster than the user can follow — so an item that silently thrashes wastes the run with no one watching. Watch for the signature of no progress on the item you're building: the **same error** recurring, an **empty diff** (an edit that changes nothing), or the **same check failing** the same way — roughly **three times** on one item. When you see it, stop; don't keep trying. Tell the user plainly what repeated — the exact error, or what wouldn't change — and hand them the decision, routing through Approach not working below.

This is a judgment call, not a mechanical counter: three is the rough trigger, and the point is to surface a stuck item rather than to tally attempts. The old autonomous runner's other limits — an iteration ceiling, a per-run spend ceiling — are deliberately not recreated here: they were arbitrary and undetectable, and session length is handled at plan time instead.

### Approach not working [DISCUSS, PROMPT]

If something goes wrong — a false assumption, a missing dependency, an approach that isn't working:

1. **Stop building.** Don't push through a broken approach.
2. **State the problem plainly.** What you expected, what happened, why the current approach won't work.
3. **Propose a path forward:**
   - **Adjust scope:** drop the item, add a prerequisite, change the approach. Update _build.md to match.
   - **Abort and requeue:** if the item is unsalvageable:
     1. Return the item to QUEUE.md's Processed section. Placement is Claude's call per plugin-behaviour.md Dependency ownership — original position or top, by what was learned.
     2. Append any captures surfaced during the attempt to Unprocessed as normal.
     3. Append the reshape direction to Unprocessed, naming the item's slug. The trigger is mechanical: abort + item returned + a reshape direction or learning the queue needs in conversation = capture needed. Unrouted, the direction survives only in the LOG entry, which /plan doesn't read at planning time, and the item re-presents unchanged at the next /next.
     4. Tell the user to run /done. _build.md stays in place so /done's router still fires the build close-out — see done.md. Differences from a completed build: the LOG entry describes the attempt and why it was aborted, and the item returns to QUEUE.md rather than disappearing into the log.
4. **Wait for the user's call.** Don't pick a path without confirmation.

## Context management

/next can't sense the context window filling — Claude only learns a session is wearing thin when the *user* says so (plugin-behaviour.md's fresh-session-handoff rule). So this isn't a trigger /next watches for; it's what to do **when the user reports the squeeze** ("this is getting long," "you're slowing down"). At that point, prefer in order:

1. **Finish and /done.** If most of the run is ticked, push through. Short-term memory is enough.
2. **Close partial.** If significant work remains, /done what's ticked and requeue the rest. The next session picks up cleanly from _build.md and QUEUE.md.

Either way, pair it with the fresh-session handoff offer (plugin-behaviour.md) — offer to carry the remaining work into a new session with a paste-ready handoff.

## Completion [BRIEF, PROMPT]

When this build item is done, next.md moves to the run's next item. When the whole run is built (every Claude-work item ticked, any `[user]` item walked through):

1. Tell the user the build is complete.
2. Say: "Run /done to record this and commit, or tighten what's already built before closing." Tightening means refining done work — not raising new work. Anything new routes through the existing paths: out-of-scope via Scope management above, thinking work via Unprocessed. No chat summary of the changes — the LOG entries /done writes are the single session record.

Do NOT delete _build.md yourself. That's /done's job.
