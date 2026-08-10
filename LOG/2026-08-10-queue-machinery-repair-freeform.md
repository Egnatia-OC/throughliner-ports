# Freeform: the six queue-machinery bugs the stopped /next run exposed

**Slug:** [queue-machinery-repair-freeform]
**Commit:** [HASH]
**Session type:** freeform — driven by hand, deliberately not through /next.

Four of the six bugs are in the machinery /next itself uses — the queue mover, the
scope-lock's cut-into-`_build.md` step, and the queue lint — so building them
through /next would have meant running the broken mechanism to repair itself. The
protection was never mechanical: nothing stopped /next picking the item up, and
the user simply didn't invoke it.

All six are built. Nothing was deferred.

---

## 1. The shell-write guard's wrong path — replaced with a searchable name

`hooks/pre_tool_use.py`'s two denial messages recommended `scripts/reorder_queue.py`.
There is no `scripts/` folder at a project root; the tool ships inside the plugin.
A session followed the recommended path, found nothing, checked `git log --all`,
found nothing, and filed a capture concluding the tool had never existed — every
step of that reasoning correct, and the conclusion wrong, because a denial message
reads as authoritative about its own project's layout.

**The decision the item asked for: a hook message should not carry a path.** Both
messages now name the tool (`reorder_queue.py`), say it ships under the plugin
root's `scripts/` folder, and tell the reader to search for the filename rather
than assume a path — because where the plugin is installed differs on every
machine, and a path is one folder move from being wrong again. A name survives a
move; a path doesn't. The guard's behaviour is untouched: it was correct, and the
finding was only ever about the advice.

## 2. plan.md's hardcoded path — brought in line with done-plan.md

`plan.md`'s skip-to-defer step invoked `python plugin/si-plugin/scripts/reorder_queue.py`
while `done-plan.md`, for the same tool, explicitly instructs deriving the plugin
root from the running skill's base directory and never hardcoding. So the skip
step resolved only in this project, and in a consumer project it fails — with the
fallback being hand-retyping a work item's prose, exactly the corruption exposure
the mover exists to remove. plan.md now carries the `<plugin-root>` form and the
same derivation note, with the reason it matters stated rather than asserted.
Three docs, one tool, one path shape.

## 3. The forward advisory — given a reserved slug of its own

The advisory was written as a `####` heading with the referenced item's slug
mid-line and none of its own. Two consequences: the lint flagged it on every
queue edit, so a consumer filing it in the documented format saw a complaint about
correct output; and the mover **aborted on the whole file** on meeting a slugless
heading, so no queue move of any kind could run while an advisory was present.
That second one was observed live in the /plan session of 2026-08-10, where three
approved deletions had to be done by hand instead.

**The fix is a format change and no code change.** The advisory now ends with a
fixed reserved slug:

```
#### Last session advises processing <slug> next [forward-advisory]
```

Both the lint's `SLUG_AT_END` and the mover's `SLUG_RE` take the *last* bracketed
token on the heading line, so the referenced item's slug sitting mid-line collides
with nothing. The advisory becomes an ordinary well-formed heading to both tools,
and neither needs a special case — which is why this was chosen over the other
three candidates (a reserved prefix, placement outside Unprocessed, or teaching
both tools to recognise the shape). The slug being *fixed* rather than derived is
what lets `done-plan.md` clear it by name with `--delete forward-advisory
Unprocessed`, which it now does instead of hand-editing.

**On whether it needs to live in QUEUE.md at all — decided: yes, it stays.** Its
only reader is the next /plan's opening, so a file of its own is defensible. It
lost because it would be one more document for a non-coder to learn about, for one
transient line. And it would not have fixed the thing that actually cost the user
time: the advisory was misread as unprocessed work twice in one session by two
independent readers, and that was never about *where* it sat. plan.md now says
explicitly that the advisory is not a work item and is skipped in the keep/delete
step.

## 4. The blocked-by lint's false fault — reworded, not taught to read `_build.md`

The check resolves `Blocked by: [slug]` against the items present in QUEUE.md, and
a blocker is legitimately absent in two normal cases: a run has taken it into
`_build.md`, or it has already shipped and been removed. It fired four times on
correct references, and in the most misleading direction available — it called the
blocker unreal at exactly the moment the blocker was being built or had just been
built, so the honest reading would have someone delete a correct reference.

The disposition was settled before this session and was not re-litigated. The
message now names all three causes and says only one is a fault, and tells the
reader to check LOG before changing anything, because a correct reference reads
exactly like a broken one here. An advisory lint's job is to make a human look,
not to diagnose.

## 5. Copy, never cut — the structural fix, and the largest change here

`next.md`'s scope-lock wrote the run's Claude-work items into `_build.md` and then
removed them all from QUEUE.md at once. From that moment until the close,
`_build.md` held the **only** copy of every item in the run, built or not — and
`_build.md` is deleted at the close. The stopped run built two of fifteen, so
thirteen items existed nowhere else; returning them meant reading them out of the
working file and retyping every block by hand. Nothing counted thirteen out and
thirteen back, and nothing would have noticed a block returned with a line missing.
`done.md` did name a restore path, so it was written down rather than improvised —
but it was prose inside a branch of one step, with no mechanism and no check, and a
documented step with no artifact is indistinguishable from one that was skipped.

**The user's fix, and it is structural rather than a better restore.** Items are
now *copied* into `_build.md` and stay in QUEUE.md; each is removed individually,
by the mover, at the moment it is ticked in Progress. Tick first, then remove — an
interruption between the two then leaves the item in both files, which a resume can
see and settle, where the reverse order would leave it in neither.

Three things follow. No item's only copy is ever in a file scheduled for deletion.
An interrupted run loses nothing, so a partial close has nothing to restore — and
`done.md`'s completion check now says so plainly, replacing the restore branch with
a two-way consistency confirmation before `_build.md` is deleted. And the queue
visibly shrinks as the run progresses, so an item still showing means not built
yet, which the user wanted for its own sake: it reads more truthfully.

**The tension it overrides, recorded so it is not rediscovered as an objection.**
The bulk removal was deliberate — destination-first, so the run was never lost
between the two writes, and it freed QUEUE.md for concurrent sessions immediately.
Copy-per-item keeps both properties. What it gives up is that items sit in both
files while the build runs, and a duplication window is a far cheaper failure than
a single copy in a file scheduled for deletion.

## 6. The design-item fix — retrieved, not re-derived, and it was found

The stopped run met [rule-lifecycle-system], a design item whose own text says its
build list is the design's output. /next's self-scoping hit it as underspecification
and halted the pre-flight, which is the current doc's prescribed behaviour but puts
the cost on the user at build time for something settled at planning time.

The instruction was to retrieve the pre-revert fix rather than re-derive it, and to
**say so and stop** if the search came up empty. It did not come up empty.

Searched the reverted span (`6ba51d3..pre-revert-2026-08-09`, 65 commits). The
answer to the item's open question — /plan, /next, or both — is **both, weighted to
/plan**:

- **plan.md's keep-step carried a blocking two-limb check.** A keep could not
  proceed unless the build could be stated in both limbs: the files that change AND
  what changes inside them. It named the exact failure — "Files (rough):
  plugin-behaviour.md, plan.md" is what undesigned work looks like — and the exact
  consequence, items in that shape reaching Processed and stalling a /next run with
  a file list and nothing to build from. The current file had this softened to a
  non-blocking *forcing function* ("return to interviewing"), which is advice.
- **next.md carried the paragraph explaining why the test has two limbs** — that a
  files-only test doesn't discriminate, because design work almost always names
  files. The two-limb table survived the revert; the paragraph that makes it
  intelligible did not.

Both are restored, with one sentence added at each end tying them together: plan.md
says this is where a design item is caught and why that is the cheap place, and
next.md says meeting one at build time means it got through the keep-step.

---

**FAQ: updated "Why is there a 'Last session advises…' line at the top of my
queue?"** — the advisory now visibly carries `[forward-advisory]` in the user's own
queue, and a user who sees a bracketed name appear on a line they were told is not
work will ask what it means. The entry now says what it is and why it's there, in
plain English, without procedure vocabulary.

**SPEC: no change needed.** SPEC describes the advisory's *purpose* and lifecycle
(line 77) but not its written format, and it does not describe the `_build.md`
scope-lock mechanics at all — so nothing it says was made wrong by any of the six.

**Format epoch: not bumped.** Nothing here makes an existing project's own files
structurally wrong. The advisory format change affects only advisories written from
now on; an old-format advisory in a consumer's queue still reads fine and simply
keeps producing the lint complaint until that session's close clears it.

**Not in this session, as the brief specified:**
[invented-rationale-compounds-past-the-shipped-rule] and
[self-authoring-word-ceiling-unjustified] both need a decision first and stay in
Unprocessed. [restore-plan-file-gate] was offered as optionally foldable and was
left — it is a separate retrieval with its own scope, and folding it in would have
made the session's boundary a judgment call rather than the brief's.

**Verification:** all three hook test suites pass
(`hook_schema_check.py`, `test_reorder_queue.py`,
`test_pre_tool_use_shell_writes.py`). Their honest limit travels with them: they
assert output shape, not delivery.
