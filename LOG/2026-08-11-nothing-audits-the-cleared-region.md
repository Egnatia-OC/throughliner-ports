# 7c9922a — The digest flags items whose placement contradicts their own text, on both sides of the readiness marker [nothing-audits-the-cleared-region]

Captured by the user as three questions about why a design item sat cleared unnoticed; widened by them too — they raised that anything can happen to an item after it is placed. The diagnosis, the correction to it, and the mechanism are Claude's.

**The defect, stated as the user's third question answered.** An item is examined on the way into Processed and never again. A gate on the door and no inspection of the room are two different failures, and only the first was built. Fixing the entry path does not negate this: the restored keep-check stops *new* design items entering Processed and does nothing about those admitted while it was soft.

**One half of the widening turned out to be already handled**, and the item does not claim it: a deleted-or-absent blocker is caught by `plan.md`'s revisit and by `post_tool_use.py`'s lint, which fired three times during the session that filed this. What is genuinely unwatched is the other half — an item whose blocker is present and genuinely open, but whose own content has rotted. The revisit asks one question per held item and is silent when the answer is "still blocked", so the item's text is never read again.

**The live instance is the argument for building it.** `[concurrent-session-support]` sat in Processed carrying, in its own bold text, "it must not be built as written." If its blocker cleared, the revisit would lift it on the one question it asks, and a /next run would build the thing the item forbids. Nothing in the method would have objected. The detector caught exactly that on its first run.

**Site: session start, not the edit-time lint.** These conditions persist across sessions, so an edit-time lint would repeat the same flags many times per session — which is how a lint becomes noise people learn to scroll past, the one real cost weighed against building this. Once per session, when the revisit runs, is when the answer is used.

**A precision problem found by testing, and the guard that fixed it.** The first run produced nine flags, four of them false — items *quoting* another item's text, including the item that specifies the check quoting the very words the check looks for. A slug reference appearing before the phrase on the same line now suppresses the flag, cutting nine to seven and removing all four. The one remaining false positive was this item's own specification of the checks, which left the queue with the item. Precision matters here more than reach, for the same reason the site does.

**It flags; it does not decide.** Moving an item out of Processed is a fate decision and stays the user's at /plan. That is stated in the doc, in the digest's own output, and in the FAQ entry.

**Files touched:** `plugin/si-plugin/scripts/queue_digest.py`, `plugin/si-plugin/docs-b/plan.md`, `SPEC.md`, `FAQ/faq.md`, `FAQ/index.md`
**Routed to Captures:** none from this item
