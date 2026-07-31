# /next procedure

You are building the cleared work from the queue. /next works the Processed section top-down — building Claude-work items, handing over user-work — scope-locked to the files that work touches.

## The work-item model /next runs on

QUEUE.md holds two sections: **Unprocessed** (captured, not yet fully processed) and **Processed** (discussed, agreed, ready). /next only ever builds from Processed, and only from above the `--- Cleared to run above this line ---` marker — the boundary /plan maintains between work greenlit to build (above) and work still being settled (below).

Each work item carries a flavor, set as an optional leading tag (plugin-behaviour.md Captures, Flavor marker):

- **(no tag)** — a build. Route to `next-build.md`.
- **`[audit]`** — a review pass. Route to `next-audit.md`.
- **`[user]`** — handover. Work only the user can run; /next hands it over rather than building it. A `[user]` item is also how a discovered user-action gets filed: when a session notices work only the user can do, it files a `[user]` item to Unprocessed rather than an untagged capture, so the action surfaces as queued work instead of prose a later session must re-notice (plugin-behaviour.md Routing and discipline, user-only discoveries).

## Step 1: Pre-flight

1. **Active build check:** If _build.md exists, a build is in progress — offer to resume it (read _build.md for state) rather than start new, opening with a [BRIEF] line naming what's being read and why: _build.md holds the interrupted build's progress and remaining work, so the session picks up where it stopped instead of starting over. If _build.md does not exist: [SILENT] — move on, no output.

2. **Read the Processed section and find the run.** [SILENT] Read QUEUE.md's Processed section top-down. The **run** is every cleared work item from the top of Processed down to — but never past — the `--- Cleared to run above this line ---` marker. The run **includes** any `[user]` items among the cleared work: /next hands each over (Step 3) *without ending the run*. Only the marker bounds the run; a `[user]` item no longer terminates it — this is the whole point of the run being marker-bounded rather than stop-at-first-`[user]`.

   How the two flavors of run item are handled keeps them from interleaving without any reorder logic in /next: Step 2 moves the run's **Claude-work items** into _build.md and builds them all, then Step 3 hands over the **`[user]` items**, which stay in QUEUE.md. Because the /plan close already places `[user]` items end-preferred so they don't split a contiguous Claude block (done-plan.md), the normal shape is Claude work together at the top with handovers after it — so "build all the Claude work, then hand over" is just what falls out. Even in an imperfectly-ordered queue where a `[user]` item sits mid-run, the same split holds: the Claude work is built and the handover follows, so the run never terminates early with cleared Claude work left unbuilt.

   Two early exits:
   - **Nothing cleared.** If the top of Processed *is* the `--- Cleared to run above this line ---` marker, there's no cleared work. Soft-stop [BRIEF]: tell the user the next work isn't cleared to run yet and recommend /plan to vet it. Don't pick an item past the marker.
   - **All cleared work is handovers.** If the run holds no Claude-work items — every cleared item is a `[user]` handover — there's nothing to build. Skip Step 2's build scaffolding and go straight to Step 3's handover branch [PROMPT], running the completion-ask below first.

   **Completion-ask before any handover** [PROMPT]. A `[user]` item can already have been done — the user ran it after a past session handed it over, but nothing removed it from Processed, so it's still sitting there. Before handing over any `[user]` item, ask **"Have you already done this one?"** — don't silently re-hand-over. Detection is by asking, not by scanning the filesystem for a produced artifact: a handover can be a device check or a decision, not a file, so there's often nothing to scan for. On **"yes, done"** → it's a completed handover to record, not work to hand over: tell the user to run /done to record it (which logs it and removes it from Processed) and don't hand it over again. On **"no, not yet"** → proceed to the handover.

3. **Present the run and offer a scope/reorder off-ramp — one beat.** [BRIEF, PROMPT] Put the run in front of the user and, in the *same* message, invite a last-glance change before scope locks — showing it and offering the off-ramp are one step, not two. **Don't ask "Ready?"**: invoking /next already signalled readiness, so a permission-to-start question is redundant. What the pause is *for* is the one deliberate human checkpoint before /next runs unattended-in-practice — a last chance to change scope or reorder — so frame it as exactly that, not as a start-confirmation. **Pointer instead of paste when mode is local and an editor is recorded:** the run's items already exist in QUEUE.md, so they're doc-resident and pointer-eligible per plugin-behaviour.md Working mode and view-in-doc rendering — when the `Working mode:` field is `local` AND an `Editor:` field carries a real value (anything other than `not recorded` or an absent field). When both hold, send a one-line pointer naming the run's items and linking to the doc — e.g. `Top of the queue — **[slug-a]**, **[slug-b]** — is in [QUEUE.md](QUEUE.md) under Processed.` When mode is remote, or no editor is recorded, send a one-line preamble then the run's work items verbatim. The pointer is the token-saving path, the inline quote the safe default. Because these items already exist in QUEUE.md, this pointer's re-read is the resolves-check half of the rule (plugin-behaviour.md Working mode and view-in-doc rendering) — confirm the link lands before sending it. Then close the same message with the off-ramp invitation, e.g. **"Say the word to change scope or reorder — otherwise I'll start."** If the user wants a change, route to /plan; otherwise Step 2 locks scope and the build begins. Present-once is deliberate: a separate "here it is" beat followed by a separate confirm beat is the redundant gate this collapses.

There is no blocker gate, push marker, or unpark/staleness scan — those belonged to the old model and are gone. Ordering and readiness are settled in /plan before work reaches the cleared region.

## Step 2: Lock scope [SILENT]

Once the user confirms:

1. **Pre-generate the candidate index entry** for each Claude-work item in the run, per plugin-behaviour.md Index entries (artifact touched + nature of change). This is the shape /done writes to LOG/index.md at close — pre-generating here makes it reusable. If an item builds as planned, /done reuses its entry verbatim; if scope shifts, /done re-authors against the same rule.

2. **Self-scope.** Derive the `Files:` list from the run's Claude-work items: read each item's description and rationale, identify the files it will change, and list them. This replaces the old pre-authored Files list — /next reads the work and works out its own scope. (`[audit]` items name no files to edit — an audit reads and reports; they contribute nothing to Files. A run of only audit items gets an empty Files list, locking the session to method docs.)

   **"Surface it" is scoped to the described work's *own* files — not to adjacent work you notice.** Two different situations must not be conflated:
   - **Genuine underspecification** — you can't tell which files *this item's described work* would change from what the item says. That's a real gap: surface it rather than guessing, because building it means inventing scope the user never agreed. This is the only case that halts.
   - **Adjacent-work discovery** — you *can* scope the described work, but while reading you notice *other* work worth doing beyond it (a related file that also carries an old term, a nearby cleanup). That is a discovery, not underspecification: **capture it and continue on the decided scope** — draft the capture, file it to Unprocessed, confirm-and-resume — never a blocking scope-ask. A blocking ask here both defeats the unattended run and reopens a scope decision the plan/next boundary reserves for /plan (plugin-behaviour.md Routing and discipline, discovery-decision rule, not-needed branch). The "third look" self-scoping gives is preserved by capturing what it finds, not by asking.

   Worked example: building a terminology rename, self-scoping enumerates the docs the item names. If a doc among them is silent on which sections change → underspecification, surface it. If instead you notice the *hooks* also carry the old term but the item didn't list them → adjacent-work discovery, capture "hooks still carry the old term" to Unprocessed and continue; don't stop to ask whether to expand scope.

3. **Create _build.md** with this structure:
```markdown
# Active Build

Run: [the flavor + slug of each Claude-work item in the run, top-down]

Entries:
[For each Claude-work item: its flavor tag (or "build"), its description, and all its rationale text — but drop any line that starts with `Files:`. The structured `Files:` section below is the only file list the scope-lock reads.]

Index entry candidates:
[the pre-generated entry from sub-step 1, one per Claude-work item]

Files:
- [each file the run's items will change — one bare path per line, relative to project root, nothing else on the line]
[This section is the only file list the scope-lock reads. Keep it as bare-path bullets directly under this `Files:` header, and make sure no other line in this file starts with `Files:`.]

Progress:
[empty — ticked as each item completes]

Changes:
[empty — accumulated as each item completes]
```

   The `Files:` section feeds the scope-lock (plugin-behaviour.md Scope): the pre_tool_use hook allows edits only to the listed files plus the method docs (QUEUE.md, LOG/, _build.md) and denies everything else. Files: lines must be bare paths — one per line, nothing else — because the hook matches each line as an exact path; any annotation becomes part of the path and silently breaks the match.

4. **Remove the run's Claude-work items from QUEUE.md** now that _build.md holds them (sub-step 3) — the queue is free for other sessions. **The run's `[user]` items are *not* removed — they stay in QUEUE.md.** A `[user]` item is handed over in Step 3, not built, and it's closed (logged and removed) only later by /done or /plan once the user has done it; extracting it into _build.md would strand it, since _build.md is deleted at close. So only the Claude-work items move. This removal is deliberately destination-first: those items were written into _build.md *before* being removed here, so the run is never lost even if something interrupts between the two. There's no both-sections window to avoid at this step — the destination is the working file (_build.md), not the other QUEUE section — so the source-first ordering the keep-step uses (plan.md) doesn't apply here; destination-first is the safe order when moving out of QUEUE into the working file. /done deletes _build.md after close.

5. **Narrate the lock** [BRIEF] — one sentence on what _build.md is for, in user-facing terms: the build's working file — it carries the run's work while QUEUE.md stays free, lists the files the safety check allows, tracks progress so an interrupted session can resume, and holds the reasoning /done writes into the session record.

Progress format varies by flavor:
- **Build items:** `- [x] item description — done`
- **Audit items:** `- [x] Finding description — captured` or `- [x] Finding description — dropped`

_build.md is the crash-recovery mechanism. If the session dies, the next session sees it and offers to resume.

## Step 3: Work the run

Work the run in two passes: **build all the Claude-work items first, then hand over the `[user]` items.** Build the _build.md items top-down, routing each by its flavor; then hand over any `[user]` items sitting in the cleared region of QUEUE.md. This two-pass shape is what lets a `[user]` item hand over without terminating the run — the Claude work is all built regardless of where a handover sat in the queue order.

- **Build item** (no tag) → read and follow `next-build.md`.
- **`[audit]` item** → read and follow `next-audit.md`.

Between build items, keep going autonomously — the user confirmed the whole run at the Step 1.3 off-ramp, so there's no per-item re-confirmation. Tick each item in _build.md Progress as it finishes before starting the next.

**Handover branch — the `[user]` items** [PROMPT]. Once the Claude-work items are all built (or if the run had none — the all-handovers early exit in Step 1), hand over each `[user]` item still in the cleared region of QUEUE.md. These reach here because the /plan close placed ready `[user]` items above the cleared-to-run marker (done-plan.md); the marker is the single gate, so /next hands over whatever ready `[user]` work sits above it and never reaches below it. Handing over does **not** end the run — it's the last pass of a run whose Claude work is already done, not a stop that abandons cleared work.

Run the **completion-ask** (Step 1) first — the item may already be done from a past handover. If the user says it's done, don't hand it over: it's a completed handover to record, so recommend /done. Otherwise hand it over.

Hand it over **collaboratively — not as a bare hand-off.** State plainly what the user needs to do and why it's theirs to run, then offer to guide them through it: run whatever parts Claude *can* (commands, setup, anything Claude can drive), explain in plain words what the user needs to check or do, and walk them through it step by step if they want. The `[user]` tag marks who ultimately performs or witnesses the step — it does not mean Claude steps back and leaves the user to it.

**Multiple independent handovers are presented together, not one at a time.** When the final pass leaves more than one `[user]` item and they're *independent* of each other, present them all in one message — each naming its own close (run /done, or raise at the next /plan) — rather than releasing them one per message. This is the [SEQUENCE] inversion in plugin-behaviour.md for "a deterministic result set produced under criteria the user already approved": every one of these handovers was cleared in /plan and sits above the line, so they're an approved, independent set, and seeing them together lets the user plan and batch them instead of being drip-fed. **Carve-out:** if two handovers have a real order or dependency between them, sequence *those* — the bundle is for independent handovers only.

**Tell the user how the handover gets closed.** A `[user]` item stays in the queue for a later session — it isn't part of this build's _build.md — so it won't record or remove itself. Name plainly how completion is recorded: once they've done it, **run /done to record it** (which logs it under its slug and removes it from the queue), or **raise it at the next /plan** if they'd rather mention it there. Without this, a finished handover strands in the queue and the next /next hands it back as if unbuilt. Because the handover is the run's final pass, there's no cleared Claude work waiting behind it — the build is already done by the time you hand over. So when you reach this pass, tell the user the Claude-work is complete, name the user-work waiting, offer to walk them through it, and recommend /done to record the build (and the handover, if they complete it now).

**Copy discipline when the run is all handovers (no Claude-work ran first).** Two things keep this message clear, because a muddled version once read as confused and defensive. First, don't fold the silent active-build check into it: whether a build was already in progress is an internal check (Step 1's [SILENT] active-build check), so leading with "no active build" blurs two unrelated things — say only that the next ready item is a step for the user to run. Second, don't frame it as "there's nothing for me to build" — /next helps either way, so name the `[user]` step plainly, say why it's the user's to run, and offer to assist with it, then wait.

## Ending before scope-lock

Any session end before Step 2 locks scope — a soft-stop at the cleared-to-run marker, the user calling it off at "Ready?" — closes through this branch:

1. **Route any reshape direction to Unprocessed.** [PROMPT] The trigger is mechanical: session ending + no scope locked + a reshape direction or learning the queue needs in conversation = capture needed. Append it to Unprocessed as a capture naming the work item's slug — draft the wording, show it for approval, per plugin-behaviour.md Captures. This capture is written this turn, so if mode is local and an editor is recorded and you confirm it with a pointer, follow the write-then-verify-then-point ordering (plugin-behaviour.md Working mode and view-in-doc rendering): emit the "filed as [slug]" pointer only after the Write returned success and a re-read confirms the capture is in QUEUE.md. Unrouted, the direction survives only in the LOG entry, which /plan doesn't read at planning time, and the work re-presents unchanged at the next /next. Nothing reshape-shaped in conversation: skip, no output.
2. **Name /done as the next step.** [BRIEF] Whatever the session did before stopping — captures filed — gets recorded and committed only by /done. Other recommendations the stop requires (run /plan to vet the next work) ride alongside; they never replace naming /done.

What doesn't happen: no item returns to the queue, because none left it — scope was never locked, so QUEUE.md already holds the run's items.

## Rules

- The work items are the contract. Don't exceed the described work without explicit approval.
- Per-item ticking is mandatory — it's the crash-recovery mechanism.
- At build completion, the only valid next-step recommendation is /done — never /next, never another build. The finished build isn't recorded until /done writes its LOG entries and commits, so recommending more building first leaves the just-finished work without a record. (Completion counterpart to one-build-at-a-time in plugin-behaviour.md: that rule guards a build's start, this one guards its end.)
