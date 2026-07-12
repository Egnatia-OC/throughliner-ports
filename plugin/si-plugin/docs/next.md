# /next procedure

You are building the cleared work from the queue. /next works the Processed section top-down — building Claude-work lines, handing over user-work — scope-locked to the files that work touches.

## The work-line model /next runs on

QUEUE.md holds two sections: **Unprocessed** (captured, not yet discussed) and **Processed** (discussed, agreed, ready). /next only ever builds from Processed, and only from above the `--- Cleared to run above this line ---` marker — the boundary /plan maintains between work greenlit to build (above) and work still being settled (below).

Each work line carries a flavor, set as an optional leading tag (plugin-behaviour.md Captures, Flavor marker):

- **(no tag)** — a build. Route to `next-build.md`.
- **`[audit]`** — a review pass. Route to `next-audit.md`.
- **`[freeform]`** — loosely-scoped work talked through. Route to `next-freeform.md`.
- **`[user]`** — handover. Work only the user can run; /next hands it over rather than building it.

## Step 1: Pre-flight

1. **Active build check:** If _build.md exists, a build is in progress — offer to resume it (read _build.md for state) rather than start new, opening with a [BRIEF] line naming what's being read and why: _build.md holds the interrupted build's progress and remaining work, so the session picks up where it stopped instead of starting over. If _build.md does not exist: [SILENT] — move on, no output.

2. **Read the Processed section and find the run.** [SILENT] Read QUEUE.md's Processed section top-down. The **run** is what this session will work: starting at the top, the consecutive work lines down to — but not including — the first `[user]` line, and never past the `--- Cleared to run above this line ---` marker. Two early exits:
   - **Nothing cleared.** If the first line in Processed *is* the `--- Cleared to run above this line ---` marker, there's no cleared work. Soft-stop [BRIEF]: tell the user the next work isn't cleared to run yet and recommend /plan to vet it. Don't pick a line past the marker.
   - **Top line is `[user]`.** If the first line is a `[user]` handover, there's no Claude-work to build first. Go straight to the handover in Step 3's handover branch [PROMPT] — state what the user needs to do and wait.

3. **Send the run.** [BRIEF] Put the run in front of the user as its own beat, before anything else. **Pointer instead of paste when an editor is recorded:** check CLAUDE.md for an `Editor:` field with a real value (anything other than `not recorded` or an absent field). When one is recorded, send a one-line pointer naming the run's lines and linking to the doc — e.g. `Top of the queue — **[slug-a]**, **[slug-b]** — is in [QUEUE.md](QUEUE.md) under Processed.` When no editor is recorded, send a one-line preamble then the run's work lines verbatim. The pointer is the token-saving path, the inline quote the safe default. These lines already exist in QUEUE.md, so this pointer's re-read is the resolves-check half of the view-in-doc pointer rule (plugin-behaviour.md View-in-doc pointers) — confirm the link lands before sending it.

4. **Confirm.** [BRIEF, PROMPT] Ask **"Ready?"** — the run is already visible. If the user wants to change scope or reorder, route to /plan. On confirm, Step 2 locks scope.

There is no blocker gate, push marker, or unpark/staleness scan — those belonged to the old batch model and are gone. Ordering and readiness are settled in /plan before work reaches the cleared region.

## Step 2: Lock scope [SILENT]

Once the user confirms:

1. **Pre-generate the candidate index entry** for each Claude-work line in the run, per plugin-behaviour.md Index entries (artifact touched + nature of change). This is the shape /done writes to LOG/index.md at close — pre-generating here makes it reusable. If a line builds as planned, /done reuses its entry verbatim; if scope shifts, /done re-authors against the same rule.

2. **Self-scope.** Derive the `Files:` list from the run's Claude-work lines: read each line's description and rationale, identify the files it will change, and list them. This replaces the old pre-authored Files list — /next reads the work and works out its own scope. If a line's files can't be determined from what it says, that's a signal the line is underspecified; surface it rather than guessing. (`[audit]` lines name no files to edit — an audit reads and reports; they contribute nothing to Files. A run of only audit lines gets an empty Files list, locking the session to method docs.)

3. **Create _build.md** with this structure:
```markdown
# Active Build

Run: [the flavor + slug of each Claude-work line in the run, top-down]

Entries:
[For each Claude-work line: its flavor tag (or "build"), its description, and all its rationale text — but drop any line that starts with `Files:`. The structured `Files:` section below is the only file list the scope-lock reads.]

Index entry candidates:
[the pre-generated entry from sub-step 1, one per Claude-work line]

Files:
- [each file the run's lines will change — one bare path per line, relative to project root, nothing else on the line]
[This section is the only file list the scope-lock reads. Keep it as bare-path bullets directly under this `Files:` header, and make sure no other line in this file starts with `Files:`.]

Progress:
[empty — ticked as each line completes]

Changes:
[empty — accumulated as each line completes]
```

   The `Files:` section feeds the scope-lock (plugin-behaviour.md Scope): the pre_tool_use hook allows edits only to the listed files plus the method docs (QUEUE.md, LOG/, _build.md) and denies everything else. Files: lines must be bare paths — one per line, nothing else — because the hook matches each line as an exact path; any annotation becomes part of the path and silently breaks the match.

4. **Remove the run's lines from QUEUE.md** (move them into _build.md — the queue is now free for other sessions). /done deletes _build.md after close.

5. **Narrate the lock** [BRIEF] — one sentence on what _build.md is for, in user-facing terms: the build's working file — it carries the run's work while QUEUE.md stays free, lists the files the safety check allows, tracks progress so an interrupted session can resume, and holds the reasoning /done writes into the session record.

Progress format varies by flavor:
- **Build lines:** `- [x] line description — done`
- **Audit lines:** `- [x] Finding description — captured` or `- [x] Finding description — dropped`
- **Freeform lines:** ticked as the work is agreed complete, per next-freeform.md.

_build.md is the crash-recovery mechanism. If the session dies, the next session sees it and offers to resume.

## Step 3: Work the run

Work the run's lines top-down. Route each Claude-work line by its flavor, and hand over at a `[user]` line.

- **Build line** (no tag) → read and follow `next-build.md`.
- **`[audit]` line** → read and follow `next-audit.md`.
- **`[freeform]` line** → read and follow `next-freeform.md`.

Between lines, keep going autonomously — the user confirmed the whole run at Ready, so there's no per-line re-confirmation. Tick each line in _build.md Progress as it finishes before starting the next.

**Handover branch — a `[user]` line** [PROMPT]. The run stops at the first `[user]` line (this is where the run boundary was drawn in Step 1). Hand it over: state plainly what the user needs to do and why it's theirs to run, then wait. Don't build past it. A `[user]` line stays in the queue for a later session — it isn't part of this build's _build.md — so when the whole run before it is built, tell the user the Claude-work is done, name the user-work waiting, and recommend /done to record the build.

**Copy discipline when the top line is `[user]` (no Claude-work ran first).** Two things keep this message clear, because a muddled version once read as confused and defensive. First, don't fold the silent active-build check into it: whether a build was already in progress is an internal check (Step 1's [SILENT] active-build check), so leading with "no active build" blurs two unrelated things — say only that the next ready line is a step for the user to run. Second, don't frame it as "there's nothing for me to build" — /next helps either way, so name the `[user]` step plainly, say why it's the user's to run, and offer to assist with it, then wait.

## On-demand freeform: `/next freeform` with no cleared work line

When the user runs `/next freeform` and the top of the cleared queue isn't a `[freeform]` line, this is on-demand freeform work. Run the gate first [PROMPT]: ask whether the work could instead be a build or an audit — those have homes already, and freeform is the refuge only for work that fits neither. Require a one-line answer naming why neither fits before proceeding; don't start until it's stated. Once it is, follow `next-freeform.md` directly — there's no queued line to read or lock, so the Step 1 run-pick and the Step 2 line-move don't apply; next-freeform.md creates _build.md with an empty Files list and grows scope ask-by-ask.

## Ending before scope-lock

Any session end before Step 2 locks scope — a soft-stop at the cleared line, the user calling it off at "Ready?" — closes through this branch:

1. **Route any reshape direction to Unprocessed.** [PROMPT] The trigger is mechanical: session ending + no scope locked + a reshape direction or learning the queue needs in conversation = capture needed. Append it to Unprocessed as a capture naming the work line's slug — draft the wording, show it for approval, per plugin-behaviour.md Captures. This capture is written this turn, so if an editor is recorded and you confirm it with a pointer, follow the write-then-verify-then-point ordering (plugin-behaviour.md View-in-doc pointers): emit the "filed as [slug]" pointer only after the Write returned success and a re-read confirms the capture is in QUEUE.md. Unrouted, the direction survives only in the LOG entry, which /plan doesn't read at planning time, and the work re-presents unchanged at the next /next. Nothing reshape-shaped in conversation: skip, no output.
2. **Name /done as the next step.** [BRIEF] Whatever the session did before stopping — captures filed — gets recorded and committed only by /done. Other recommendations the stop requires (run /plan to vet the next work) ride alongside; they never replace naming /done.

What doesn't happen: no line returns to the queue, because none left it — scope was never locked, so QUEUE.md already holds the run's lines.

## Rules

- The work lines are the contract. Don't exceed the described work without explicit approval.
- Per-line ticking is mandatory — it's the crash-recovery mechanism.
- At build completion, the only valid next-step recommendation is /done — never /next, never another build. The finished build isn't recorded until /done writes its LOG entries and commits, so recommending more building first leaves the just-finished work without a record. (Completion counterpart to one-build-at-a-time in plugin-behaviour.md: that rule guards a build's start, this one guards its end.)
- If context runs long mid-build, suggest finishing the current line and running /done. A clean close beats pushing into a context squeeze — the next session resumes cleanly from _build.md.
