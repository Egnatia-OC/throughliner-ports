---
name: next-audit
docset: current
note: Execution procedure for `[audit]`-flavor work items. Reached from next.md.
---

# Audit procedure

**The output contract defines an audit:** findings route to Unprocessed so /plan
can process them into normal work items — **no direct edits to the artifacts the
audit reads.**

What gets read varies — procedure docs, the user's spec, code, UI flows, workflow
output. The shape is the same regardless: **read many, propose many.**

An audit item names no files to edit, so it contributes nothing to the run's
`Files:` list. A run of only audit items has an empty list, holding the session to
the method docs — the strictest setting, matching a session that edits no source
files.

## If the audit item directs a write into a document, stop and ask  [PROMPT]

Before reading, check the item's wording against the contract.

```
item directs a write into a named document   ->  CONTRADICTS the contract
    ("append findings to MAP.md", or names        surface it; don't silently follow
     a findings doc to fill)
```

An item marked `[audit]` but pointed at a doc-write is a planning slip. Following
it silently writes unvetted findings straight into a durable doc — exactly what
the route-to-Unprocessed contract prevents.

Ask which the user wants, then wait before reading:

> "This item is an audit, but it says to write findings into review-notes.md. An
> audit files findings to the queue for vetting first — it doesn't write them into
> a doc. Want me to file them as captures, or run this as a build that writes
> review-notes.md directly?"

## Read the target systematically against the criteria  [SILENT]

Read every artifact the item names. **Apply the criteria pass by pass — one
criterion across the whole target, then the next** — not all criteria per
artifact. A single criterion held across the whole target is applied more
consistently than re-deciding every criterion afresh for each artifact, and it
groups findings by criterion ready for the compile step. Reading each artifact
once against everything tends to collapse into a per-artifact skim.

Read each artifact through, since an audit's value is reading what is there.
Accumulate observations in the build working file Changes with precise references
(file:line) so the user can verify each.

## Compile findings  [SILENT]

Group observations into discrete findings — **one finding per actionable change.**
Phrase each as *observed + why it matters*, the shape a capture takes, since
that's where they'll land.

## Present findings as one numbered set  [BRIEF, PROMPT]

One message, all findings. State the count upfront, then list each: number,
observation, file:line, why it matters. Ask the user to approve the whole set or
list the numbers they don't accept as-is. Then wait.

This keeps the always-show rule fully intact — the user reads every finding's
exact wording before any of it is filed.

## Handle contested findings one at a time  [SEQUENCE, PROMPT]

State how many, then take the first.

```
reword  ->  redraft, show the new wording for approval
drop    ->  remove it
```

Wait for the user's call on each before presenting the next. Every finding they
didn't contest is approved as-is.

## Route the approved set to Unprocessed

Append the approved findings to Unprocessed, each placed per the Captures
placement rule and written to the capture-authoring standard. Tick each in
the build working file Progress as `captured` or `dropped`.

## Close  [BRIEF, PROMPT]

When the audit item is done, next.md moves to the run's next item. When the whole
run is done, tell the user with the captured/dropped counts, and say: "Run /done
to record this and commit, or keep reviewing."

Reviewing means re-examining what was already found — not raising new work.
Anything new routes through the existing paths: a discovery outside the audit's
target follows the discovery rule; thinking work goes to Unprocessed. No chat
summary of the routed findings — the LOG entry /done writes is the single session
record.
