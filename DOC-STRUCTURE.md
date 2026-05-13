# Document structure specifications

*Mode: planning, migration.*

This file holds the structural specifications for the project's documents — required sections, entry shape, rules for additional source-of-truth docs. Not loaded on every session.

Method-specific terms used here (planning batch, build batch, Serves line, source-of-truth doc, etc.) are defined in `NO-CODE-METHOD.md` → *Vocabulary*.

For the high-level role each doc plays, see `NO-CODE-METHOD.md` → *The documents that describe my projects*. For when to read each doc, see *When to read each document* in the same file.

## Additional source-of-truth docs

Some projects need an additional source-of-truth doc the three above don't cover — for example, a project with a Claude/MCP integration may need a `SYSTEM-PROMPT.md`; a project whose user-facing text is its primary deliverable may need a `COPY.md`. The three spine docs above remain the spine — additional docs sit alongside, not in place of. The project decides what the additional doc is for, who its audience is, and what it's named.

When a project adds one, the same structural rules that govern `UX.md` apply:

- **Read-only in Claude Code.** Same rule as `UX.md` — see `NO-CODE-METHOD.md` → *Editing surfaces*.
- **No placeholders, no soft gestures.** Source-of-truth docs describe decided behaviour. Don't write placeholders (`[TO FILL IN]`, `[Open: ...]`) and don't write sentences that gesture at the doc's own undecidedness ("currently undecided", "pending decision", "to be revisited", "see `BACKLOG.md` for the open question"). The status of an open question lives in `BACKLOG.md` only, not inside the doc body. If a default behaviour applies while the question is being resolved, state the default plainly without flagging it as provisional.
- **Intent level, not implementation.** Same rule `UX.md` follows: describe what the user (or the consumer of the doc, e.g. Claude in the case of a system-prompt doc) experiences and why, not how it's wired underneath.
- **Folding planning answers.** Planning batches whose resolutions describe behaviour belonging to the additional doc fold into *it* rather than `UX.md`. The planning batch in `BACKLOG.md` should say so when it's set up, so it's clear at fold-in time which doc the answers go into.
- **Build batches that change the additional doc's domain** add a `Serves <DOC>: ...` line alongside (or instead of) the `Serves UX.md: ...` line, naming the entry or section in the additional doc the batch implements.

A starter shape is available at `ADDITIONAL-DOC-TEMPLATE.md` — copy, rename, and adapt.

## UX.md structure

Every project's `UX.md` follows this shape. Start a new project by copying these headers; fill them in as the project develops.

**Header.** A brief statement of what `UX.md` does, plus two rules: (1) every entry must correspond to something the user can actually experience in the current build, and (2) `UX.md` only describes what has been decided — open questions live in `BACKLOG.md` as planning batches, not here as placeholders.

**Project context.** One paragraph stating what the app is, what it does, and what makes it distinct from existing apps in the space. Sits between the header and the UX principles. Filled in once the project's basic identity is settled.

**UX principles.** Three to six project-specific principles that inform every design decision. Each principle is a one-line claim plus a few sentences of reasoning. Principles act as guardrails: if a proposed change conflicts with a principle, flag it before building. Principles are project-specific, not method-wide.

**Functionalities.** Each functionality is one entry. Required shape:

> **Feature name**
> One paragraph describing how the user experiences this feature.
> The user needs this because... [rationale tying back to a UX principle or user context].

**Optional: Risk accepted.** When a feature's design has a known downside that's been weighed and explicitly chosen, end the entry with a `**Risk accepted:**` line stating the downside in one or two lines — for example, the cost of a chosen simplification, a deliberate omission, or a trade-off the user has signed off on. Use only for real downsides the user has consciously taken; not for general caveats.

**Cross-references.** Where a feature ties to or composes with another entry, link by entry name in italics: *(see Drag-target icons)*. Cross-references are encouraged where features genuinely compose; do not duplicate content across entries. If two entries keep needing to cross-reference each other for basic context, consider whether they're really one entry split in two.

**Nested entries.** Most functionalities are flat top-level entries. If a parent functionality has sub-areas with distinct user-facing rationale, each sub-area can have its own entry, named **Parent → Sub-area** (e.g. `Settings → Day begins at`). Use sparingly: if a sub-control's "user needs this because..." line is the same as the parent's, fold it into the parent rather than splitting.

**Scope: intent-level only.** UX.md describes features and behaviours at the user-intent level — what I came to do, plus distinct app behaviours with a user-facing rationale. Not every visible UI element. Not implementation details that produce visible output. Not standard platform conventions. The "user needs this because..." line is the test — if you can't write it, the thing doesn't belong in UX.md.

If a feature's behaviour is not yet decided, it does not belong here at all — it belongs in `BACKLOG.md` as a planning batch. (See *Additional source-of-truth docs* → "No placeholders, no soft gestures" for the rule against placeholders and soft-gesture wording, which applies here too.)

## MANIFEST.md structure

**Header.** A brief statement of what `MANIFEST.md` is: a glossary of named elements in the codebase, maintained by Claude during builds, not intended to be read cover-to-cover.

The file starts empty at project start. The entry-format reminder lives inside an HTML comment so the file stays cleanly empty until the first build adds entries.

**Entries.** A single flat list, alphabetical by name. Each entry is one line:

> - **[Name]** — [one-line plain-English description of what this is and what it does]

Include things the user might plausibly ask about: components, screens, services, modules, files with a discrete purpose. Do not include trivial helpers, internal utility functions, or boilerplate.

If a project ever grows large enough that the flat list becomes hard to scan, switch to alphabetical sections by area.

## BACKLOG.md structure

`BACKLOG.md` consolidates everything that is deferred, in four sections in this fixed order.

**Maintained by Claude during planning, not by the user.** Whenever a planning decision changes `BACKLOG.md` — adding, removing, reordering, splitting, or reclassifying an item or batch — Claude edits the file directly. The user reviews the edits afterwards; the user does not apply them.

**Header.** A brief statement of purpose, the section order, and the maintenance rule (so a runtime reader of `BACKLOG.md` itself sees the rule too).

**Four sections, in this order:**

- **Red flags.** Security, privacy, data integrity, or safety concerns surfaced and explicitly deferred by the user. Empty by default. Each entry is a blockquote in the canonical format: `**`[RED FLAG]`**` [one-line description]. Found during [batch name] ([date]). Fix: [shortest possible fix]. Items are removed once addressed. Claude populates this section per the "Red flags — screen and surface" rule under *Method contract → Required of Claude* in `NO-CODE-METHOD.md`.

  **Red flags entries are concerns parked outside any active work stream.** Concerns inside an active build batch live there until the batch ships. Concerns attached to a feature in a planning batch become questions inside that planning batch — not Red flags entries. The Red flags section is specifically for concerns the user has explicitly chosen to defer with no active plan to address them.

- **Fold-ins pending.** Proposed source-of-truth content that Claude Code has formed but cannot write directly to read-only docs (`UX.md` and any additional source-of-truth docs). All fold-in pending blocks live here regardless of which route produced them — the new-project route, the migration route, a planning-batch resolution, or a mid-build edit attempt that the PreToolUse hook intercepted. Each block is a blockquote in the canonical format:

  > `**`[FOLD-IN PENDING]`**` `<DOC>.md` — [one-line description of the proposed change]. [Proposed text or shape of the change, inline or as an indented sub-quote]. Surfaced [date]; origin: [planning batch name | new-project route | migration route | mid-build edit attempt].

  Empty by default. Items are removed once the user folds them into the destination doc in a Cowork session (or consciously drops them). The full mechanism — when blocks get created and how they reconcile back into source-of-truth docs — is in `NO-CODE-METHOD.md` → *Editing surfaces*.

- **Planning batches.** Two kinds of question live here. **(a)** Open questions that must be resolved before some build batch can run. **(b)** Scope-existence questions whose resolution decides whether a build batch should ever exist (e.g. "should this app even have a search box?"). Each planning batch lists the questions and ends with a `Blocks:` line — either naming the build batch (or batches) it holds up, or noting `Blocks: scope decision — no build batch yet` when it's an existence question. Resolution mechanism: append the answer to the planning batch and add a corresponding `[FOLD-IN PENDING]` block to the *Fold-ins pending* section (with this batch's name as the *origin*). Leave the planning batch in place — the user removes it during the same Cowork session in which they fold the answer into `UX.md` (or the relevant additional source-of-truth doc). If a scope-existence batch resolves to "yes, build it," the planning batch may convert to a build batch (or spawn one) at that point, in addition to the fold-in.

  **One planning batch per discrete decision.** If a message contains multiple unrelated feature requests or scope questions, create separate planning batches — one per discrete feature. Bundle only when two items are tightly coupled (deciding one inevitably decides the other). Unrelated items in a single batch create a batch whose `Blocks:` line can't cleanly name what it blocks and whose resolution can't fold into a single source-of-truth-doc entry.

- **Build batches.** Engineering work, ordered top-to-bottom by priority. The top batch is the next build. Each batch is a heading plus a list of changes; each batch ends with a `Serves UX.md: ...` line listing the entries it implements (and/or a `Serves <DOC>: ...` line for additional source-of-truth docs the batch's work implements). If a build batch's purpose is to carry an additional source-of-truth doc to its runtime destination rather than implement any of its content, the `Serves <DOC>:` line names the delivery mechanism instead of a section (e.g. `Serves SYSTEM-PROMPT.md: connection-time delivery as Claude's system prompt`). Each batch must be small enough to build and test in one session — if it can't be, split it during *Before build*, not during the build itself. Completed batches are removed during the next planning session (see `NO-CODE-METHOD.md` → *During planning* for the mechanism). If a build session ends with the top batch only partly done, the unfinished portion stays as the top batch and the next session's first action is to resume it.

Build batches must serve an entry in a source-of-truth doc — see `NO-CODE-METHOD.md` → *How a new feature enters the project* for the pipeline. Red flags are the only deferred items that don't need such an entry behind them; they live in `BACKLOG.md` regardless of scope.

---
*No-code method — Version 20.*
