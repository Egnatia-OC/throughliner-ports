# [HASH] — The ordering-ladder Discord post, written to its third subject and posted

`[user]` item, walked through live and **completed this session** — the user posted it and confirmed. The item is removed from Processed at this close.

**Files touched:** none in the repository; the artifact is a Discord post, with its text recorded below.

**Routed to Captures:** [method-purpose-orientation], raised by the user off the back of writing this post and the comparison article.

Rule gate: not needed — a Discord post authors no method rule.

FAQ: not needed because an announcement changes nothing a user does.


`[user]` work, walked through live in this session. Actions appended as they happen.

## Walk-through record

- Walk-through opened. Confirmed against the record that everything the post would claim has shipped: the four-rung ladder landed in `b485ee3` (`LOG/2026-08-20-decay-rung-unreachable-in-practice.md`), with the SPEC rebuild in `8330209`. The standing rule that a post announces only shipped behaviour is therefore satisfied.
- Wrote the third subject the item requires. The first two were overtaken — the post originally announced six rungs cut to three, then that ladder was itself replaced before the post went out. The subject is now the whole sequence, which is what the item predicted would make the better piece: a mechanism got wrong twice and corrected in public.
- **First draft rejected by the user, and the reason is worth keeping:** it narrated how the ladder was built — six rungs to three, the rung found unreachable, the rebuild — rather than what a user now gets. Her words: *"This is narration about how we built the ladder. Not a useful post about what users can now get out of Throughliner."* Rewritten from the reader's outcome; the whole construction history was cut, along with the verbatim quotation, which was evidence for a design argument the post no longer makes.
- She then supplied the missing half herself: long entries earn half the alternating picks because they are what make a queue expensive to reason across, so clearing them shortens it fastest — the reason the post had stated as a bare mechanism.
- She edited the draft and asked for verification. Five findings, four accepted and applied: "15-20 handful of items" (typo, and the record says only "a handful" — 15–20 is this project's recent rate); "subtracts two dates" corrected to "two line numbers" per SPEC, an error this session introduced and she inherited; "which ordering it used and why" narrowed to what SPEC promises; `QUEUE.md's` to `QUEUE.md files`. **Two of the five were resolved in her favour and the verification was wrong to raise them as defects.** Her "most-designed work" was challenged as reinstating the rejected best-designed claim; she had changed the word deliberately, and the distinction holds — the record's "enriched across many sessions without resolving" *is* most design effort, and only the quality claim was tested and rejected. And her 60-item figure was challenged as an underivable limit; it is derived, from her own observed experience that sessions degrade past that point, which is exactly what the gate asks for. The post now states that derivation. The 800–1000 line figure was dropped as this project's own measurement, which does not travel to consumers whose items are shorter.
- Post approved at 1,847 characters. The user posts it; Claude has no route to Discord. Under the one-a-day pacing this is the day's post — the comparison article's post is not going out, since the article is unpublished and held.
- The user's own words are quoted verbatim from `LOG/2026-08-20-decay-rung-unreachable-in-practice.md`, where they were recorded as a quotation at the time — so this is a quote claim the text can support, not a paraphrase dressed as one. (The quotation was later cut with the rest of the construction history.)

- After approval the user raised that authoring these pieces had shown how badly Claude understands the method, and proposed skill intros plus a plugin intro in the always-loaded rules. Checked the shipped package: nothing in it states the method's purpose, and a consumer's `SPEC.md` is about their own app, so consumer sessions run on procedure with no purpose statement at all — this project only appears to have one because its product happens to be Throughliner. Filed as [method-purpose-orientation], carrying the three failures from this session as its evidence and the unmeasurability as its stated limit.

- She asked whether the most-unblocking rung was still live, having noticed it was absent from the post. Verified in `plan.md`: it is live twice over — the named default of the opening question, and rung 2 of the fallback ladder, ordering by how many other entries cite an item's slug. Rung 1, an uncleared red flag in Unprocessed, was also missing, and the post's framing implied alternation was the ordering rather than the last resort beneath three other rungs. She added the full four-rung ladder by hand.
- **Posted 2026-08-23.** The posted text is below and differs from the approved draft: she added the numbered ladder, cut the arithmetic explanation in the opening, and folded most-unblocking into the first section. The record carries what went out rather than what was approved.

## The posted text, verbatim

> Throughliner update: your old queue items stop getting skipped
>
> You may have noticed the same items coming up across plan sessions while items captured weeks ago never surfaced at all. That was arithmetic, not just bad luck. The ladder as it now stands:
>
> 1. an uncleared red flag in Unprocessed — a breach outranks a delay
> 2. unblock-potential — most-cited first
> 3. long and old, oldest first
> 4. Alternating, oldest first, every other pick from the long half
>
> What's different now:
>
> One items are processed most-unblocking first, old and/or long captures are deliberately surfaced in a /plan run. Ordering alternates: oldest first, with every other pick taken from your longer entries. Length earns that slot for a concrete reason — long entries are what make a queue expensive to reason across, so clearing them is what shortens the queue fastest, and a short queue is one Claude can hold in view all at once. Keeping it short is good practice (in my own experience, past about 60 items the sessions degrade); the ordering now does part of that for you.
>
> The work that keeps coming back gets surfaced first. Items both longer and older than your queue's own midpoints go near the top. That combination may include some of your most-designed work — items you've added to across many sessions. In practice they're usually waiting on one decision only you can make, and /plan will now ask you for it rather than enriching/lengthening the item again.
>
> The order is computed, not judged. Every step on this "ladder" either reads a number worked out at the session's start or subtracts two line numbers. Claude doesn't get an opinion about what matters. So the order is the same whoever runs it — and /plan tells you in one line which ordering it used.
>
> Nothing to configure and nothing to turn on. Open /plan and it's how your queue is handed to you.

## The earlier approved draft, superseded by the above

> **Throughliner update: your old queue items stop getting skipped**
>
> In long QUEUE.md files, you may have noticed the same items coming up across plan sessions while items captured weeks ago never surfaced at all. That was arithmetic rather than bad luck: the old item ordering had to work through half your queue before it reached anything else. But a planning session usually only gets through 15–20 items, so everything underneath was reachable in theory but never in practice.
>
> What's different now:
>
> **Old captures actually come up in a /plan run, and long ones get half the picks.** Ordering alternates: oldest first, with every other pick taken from your longer entries. Length earns that slot for a concrete reason — long entries are what make a queue expensive to reason across, so clearing them is what shortens the queue fastest, and a short queue is one Claude can hold in view all at once. Keeping it short is good practice (in my own experience, past about 60 items the sessions degrade); the ordering now does part of that for you.
>
> **The work that keeps coming back gets surfaced first.** Items both longer *and* older than your queue's own midpoints go near the top. That combination may include some of your most-designed work — items you've added to across many sessions. In practice they're usually waiting on one decision only you can make, and /plan will now ask you for it rather than enriching/lengthening the item again.
>
> **The order is computed, not judged.** Every step on this "ladder" either reads a number worked out at the session's start or subtracts two line numbers. Claude doesn't get an opinion about what matters. So the order is the same whoever runs it — and /plan tells you in one line which ordering it used.
>
> Nothing to configure and nothing to turn on. Open /plan and it's how your queue is handed to you.
