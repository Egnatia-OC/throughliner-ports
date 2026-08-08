# 7a4b377 — Both desk-written rendering claims in the fencing rules corrected: the no-wrapping reason narrowed to remote control, and the copy-affordance note restated as a two-sided trade

Two rendering claims in adjacent rules, both written from the desk, both false on
the other surface. They were folded into one item at the user's approval because
they land in the same file and are the same finding twice.

**Limb one — the prose-never-in-a-fence rule.** Its entire justification was
"fences don't wrap in the app, so a long draft ran off-screen — a user on remote
control could not read the text they were being asked to approve." The sibling
fencing rule above it has two independent reasons; this one had one, and it was a
claim about rendering.

Tested at the desk, it was false: a ~280-character sentence in a plain fence
wrapped and was fully readable. That falsification alone would have argued for
deleting the rule — and deleting it on that evidence would have repeated the exact
mistake the whole verification pass exists to catch, since the recorded failure was
specifically on *remote control*, which had not been tested.

**The blocking answer came back before the build, and it is outcome two of three:
the rule narrows, it does not die.** Walked through with the user watching both
surfaces simultaneously, a ~300-character sentence in a plain fence **ran off the
side on the phone and wrapped on the desktop**. So "fences don't wrap in the app" is
false at the desk and true on remote control — the surface the original failure
happened on. The rule's reason is repairable rather than dead, and the narrowing
matters because it currently read as universal.

**Limb two — the copy-affordance parenthetical.** It rejected a superseded reason
(that the app's copy takes the whole message, so a fence is the only clean copy
affordance) on the grounds that "people select the text they want and copy that".
That clause was written deliberately to stop the old reason being reinstated, so it
was doing a real job and could not simply be deleted. But its own grounds are
desk-centric in the opposite direction: on a phone, selecting is press-and-hold,
two drag handles placed precisely in a scrolling view, often across the screen
boundary, and a copy menu that may itself be off-screen. The user's words at a
close: they preferred code blocks *"because I didn't have to use the fiddly select
then copy process on my phone."*

**So the corrected note states the trade rather than resolving it falsely.** Given
that fences don't wrap on remote control, the two options fail in opposite
directions there: a fence is easy to copy and unreadable; rendered prose is
readable and genuinely fiddly to copy. Nothing is good at both, and the old note
hid that by asserting selection is easy. The anti-restoration job survives intact —
the old reason stays rejected, because a blockquote is copyable and a paste block is
one word away — it just stops resting on a false claim.

**The design answer to "should the paste-block offer be more forward on remote
control" routes around the constraint rather than hitting it.** Nothing tells a
session which surface the user is on, and asking is the retired `Working mode:`
field's recorded failure. But the offer doesn't need the surface — it needs the
text's **purpose**. Claude cannot know the user is on a phone; it can know that an
announcement, a report, or a prompt destined for another app exists in order to be
pasted somewhere else. So the trigger is content-shaped: where doc-bound or draft
text is plainly for pasting elsewhere, offer the copy block in the same breath
rather than waiting to be asked. No setting, no guess, no new field.

Also banked from the same walkthrough and left standing: the Run button **does**
appear on a shell-tagged fence, which is the half that earns the one-command-per-block
discipline.

**Files touched:**
- `plugin/si-plugin/docs-b/plugin-behaviour.md` — the prose-never-in-a-fence rule's reason rewritten around remote control with the both-surfaces test cited, plus the purpose-triggered paste-block offer; the fenced-code-blocks rule's copy-affordance parenthetical rewritten as the two-sided trade.

**Routed to Captures:** none from this item.

**FAQ:** not needed because this changes how Claude renders text, not anything a user meets as a named feature or would think to ask about — they see better-chosen rendering, not a new behaviour to understand.
