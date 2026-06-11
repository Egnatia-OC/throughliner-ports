# QUEUE

## Batches

Worked top to bottom. Each batch of changes or tests is one /next session of either type:

- build session where changes are applied, then claude runs all tests it is able to do itself
- test session where the user runs any testing only they can do

**Change LOG file boundary from per-release to per-entry** **[drop-log-per-release-split]**

The per-release log file split (log.md → log-v<VERSION>.md at each push) uses an arbitrary boundary — version groupings aren't load-bearing on any retrieve, and design threads span releases. But collapsing to one growing log.md only removes the split without improving retrieve — you still grep within the file to find an entry. The right fix is matching the file boundary to the logical boundary: each LOG entry gets its own file, so retrieve goes from index → hash → direct file open, no grep step. Entries are already per-commit; files should match. The per-commit alternative was considered in the f123eed discussion but not preserved in the LOG — this is the decision that session should have reached.

Build:
- Decide naming scheme for per-entry files. Slug-based (LOG/trickle-up-audit.md, LOG/plan-2026-06-09.md for sessions without a batch slug) avoids the hash-not-known-at-write-time problem and keeps filenames readable. Hash stays in file content + index.
- the /done per-type close-out sub-docs (done-build.md, done-test.md, done-audit.md, done-plan.md): write each LOG entry as its own file under LOG/ instead of appending to log.md.
- plugin/si-plugin/docs/plugin-behaviour.md: update why-pipeline retrieve rule — "search LOG/index.md, then open the matched entry's file directly."
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md: update LOG/ description to reflect per-entry files. Remove "this file covers the current release" framing.
- plugin/si-plugin/skills/setup/, plan/, next/, done/ procedure docs: grep for log-v*.md, single-log-file, and per-release references; revise to describe per-entry files.
- This project's CLAUDE.md (host-only): remove steps 3–4 from push-and-rezip (push marker in log entry and cap-and-rename ritual). Add a note that existing log.md and log-v*.md files stay in place — index references work by hash, so old entries remain findable.

Test:
- Self-verifying from doc edits.
- After the next push: ask Claude a "why did we decide X" question targeting an entry in an old log-v*.md file. Verify retrieve still works through index + grep fallback for pre-migration entries.

**Give deferred tests a structural home in QUEUE.md** **[deferred-tests-structural-home]**
Blocks: [hash-backfill-as-hook], [queue-format-lint-hook], [git-add-safety-hook-gap], [session-start-dirty-tree-check]

/next pre-flight asks "unconfirmed tests from a previous build?" but defines no place to read the answer from — the check ran on conversation memory four pre-flights running during the 2026-06-10 long session, and the two currently-deferred host-side tests are archived in log-v1.10.0.md where a fresh session has no instruction to look. On short weak-model sessions the tests would silently never surface; memory is covering for a missing structure, which the design target forbids. The fix is a mechanical slot: a Deferred tests section in QUEUE.md that /done writes when a test can't run in-session (host-side, needs-user, external event), /next's gate reads and re-presents, and the confirming session removes from. One line per entry — source batch slug, what to verify, what confirms it — so the gate's read needs no judgment. The lint hook tolerates the new section by design (deny-list). The Blocks: header is load-bearing: all four named batches carry host-side tests whose /done needs the slot to exist.

Build:
- This project's QUEUE.md: add a "## Deferred tests" section between Batches and Captures, seeded with the two pending host-side tests from log-v1.10.0 (done-split single-summary; _build.md narration moments), each with source slug and confirm-by condition.
- plugin/si-plugin/docs/done.md and the per-type sub-docs that close out tests (done-build.md, done-test.md): when a planned test can't run in-session, write it to Deferred tests — not as prose in the LOG entry.
- plugin/si-plugin/docs/next.md pre-flight gate: replace the memory-dependent question with a mechanical read of the Deferred tests section; re-present pending entries; the confirming session removes the entry and records the confirmation in its LOG entry.
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md and this project's CLAUDE.md Method docs section: describe the new QUEUE.md section so the format is documented for consumers and future sessions.
- plugin/si-plugin/templates/faq-template.md (+ index line): FAQ entry explaining the Deferred tests section — what it holds, who writes it, when entries leave.

Test:
- Structural part self-verifying. Behavioural: the next /done that defers a test writes an entry; the next /next pre-flight re-presents it. The four blocked hook batches are the natural first exercises.

--- Push required before continuing ---

**Move the LOG hash backfill into session_start as a hook** **[hash-backfill-as-hook]**
Depends on: [deferred-tests-structural-home] (host-side)

The backfill is the plugin's most mechanical procedure — grep for [HASH], run git log, replace — yet it's specified twice as model-executed procedure (plan.md Step 1, next.md Step 1.1). Research technique #1 (resources/research/model-instruction-compliance.md): what must happen mechanically belongs in a hook — deterministic, unskippable, identical on weak and strong models, zero procedure-doc lines. Supersedes [log-hash-backfill-in-done], whose /done+amend design also turned out unworkable: amending after writing the hash creates a new commit with a new hash, so the inline hash would dangle — a commit's hash can't be known before the commit is final, which is why the placeholder pattern exists. The hook scans shape-agnostically (all LOG/*.md) so the queued per-entry-file restructure needs no rework here. Known residual gap, closed in this batch: a session that runs /done then pushes in the same session hits push time with an unfilled placeholder — the hook fires at session start only — so the push ritual gains a backfill step of its own (absorbed from the push-ritual-placeholder capture; stale archived placeholders are how log-v1.8.0 and v1.9.0 shipped, healed later by hand). Absorbs [trickle-up-hash-backfill-duplication]: both procedure copies get deleted, not consolidated. Folded in from the prose-corruption capture: the 2f23dc6 backfill's blanket find-replace ate a prose line that mentioned the token literally, so replacement anchors to hash position and LOG prose stops writing the literal token at all.

Build:
- plugin/si-plugin/hooks/session_start.py: implement the backfill in Python — scan LOG/*.md (archives included) for [HASH]; replace the token only in hash position (an entry heading line, or the start of an index line) — never in body prose, which may mention the token literally. Anchor on position, not on today's file shapes, so the per-entry-file restructure needs no rework here. Per affected entry resolve the hash to the commit that introduced the entry: oldest git log -S "<entry title>" match, never the newest commit touching the file, because caps and renames touch entry text later and would return the wrong hash for archived files; edit in place; report one line via additionalContext. No model involvement.
- plugin/si-plugin/docs/plan.md Step 1: delete the "Backfill LOG hashes first" block.
- plugin/si-plugin/docs/next.md Step 1: delete the backfill sub-step.
- The LOG-entry-writing instruction in the /done per-type sub-docs (locate the shared statement; if a canonical home covers all four, one line there — don't duplicate per sub-doc): LOG-entry prose never writes the literal placeholder token; when an entry needs to describe the backfill, say it indirectly. Same patterns-as-data trap [git-add-safety-hook-gap] documents for the git-safety denials.
- This project's CLAUDE.md push-and-rezip ritual (host-only, does not propagate): add a step at the ritual's start — backfill any [HASH] placeholders anywhere in LOG/ before proceeding, same oldest-match rule and same hash-position-only replacement as the hook. Anchored at the ritual's start rather than before the log-cap step, so it survives [drop-log-per-release-split] deleting the cap.

Test:
- Claude-run: execute session_start.py directly against a temporary git-repo fixture containing a [HASH] placeholder; verify the in-place replacement, the resolved hash, and the report line. Cover the multi-placeholder fallback, and a body-prose line containing the literal token — it must survive untouched.
- Host-side (after push + reinstall): first session after a /done shows the hook's one-line report and no placeholder survives. Needs the deferred-test discipline — flag at /done if it can't run.

**PostToolUse lint hook for QUEUE.md structure** **[queue-format-lint-hook]**
Depends on: [deferred-tests-structural-home] (host-side)

The queue's format spec lives as front-loaded prose in plan.md and plugin-behaviour.md that the model holds in its head while writing — a less-capable model will drift it, and nothing catches drift until a later session trips over it. A PostToolUse hook linting QUEUE.md at write time feeds corrections back the moment an edit lands, per research technique #1 (resources/research/model-instruction-compliance.md): mechanical enforcement belongs in hooks. Deny-list by design — flag known violations, never treat unknown structure as one — so format evolution (new sections, new batch types) doesn't fight the linter. Scoped to QUEUE.md; _build.md linting deferred until its drift modes are enumerated. The long-term payoff (shrinking format prose in the docs to examples) is deliberately not in this batch — it follows once the hook has proven itself. Sibling tooling to [hash-backfill-as-hook].

Build:
- Verify first: confirm PostToolUse hook registration works for desktop-app plugins (Claude Code hooks docs / a quick registration test). If unsupported, halt and route findings back to Captures.
- plugin/si-plugin/hooks/: new PostToolUse hook on Edit/Write to QUEUE.md, registered in the plugin's hook config. Checks, all advisory warnings fed back to Claude: batch missing a **[slug]** marker; Parked item missing its Blocked by:/Parked: header; processed/unprocessed divider deleted; Depends on:/Blocks:/Blocked by: naming a slug that exists nowhere in the file; subheading inside a batch that isn't Build/Test/Audit (catches typos; must be updated if new batch types ship); prose naming a slug with no header carrying it ("dependency or citation?" — advisory precisely because evidence citations are legitimate).

Test:
- Claude-run: invoke the hook script directly with synthetic QUEUE.md content — one violation per check, verify each warning; one clean file, verify silence; one file with a novel-but-valid new section, verify tolerance (the deny-list property).
- Host-side (after push + reinstall): live confirmation on a real /plan edit. Needs the deferred-test discipline — flag at /done if it can't run.

**Extend git-safety hook: deny blanket adds and commit -a** **[git-add-safety-hook-gap]**
Depends on: [deferred-tests-structural-home] (host-side)

plugin-behaviour.md File safety forbids git add -A / git add ., but pre_tool_use only enforces reset --hard and push --force. The blanket-add rule is exactly as mechanical — a regex on the command — and a weaker model is far more likely to reach for git add -A than push --force; today nothing but prose stands in its way. Per research technique #1, enforcement this mechanical belongs in the hook, with the denial message doing the teaching at the moment it matters. plugin-behaviour.md keeps its one-line rule (done.md's restatements were already removed when [done-closeout-extraction] shipped). Sibling to [hash-backfill-as-hook] and [queue-format-lint-hook] in the hook cluster. Folded in: the git-safety false-positive sharp edge — the hook fires on command text, not intent, observed denying a test script that merely contained the patterns as data. Pattern-sharpening to skip quoted contexts was rejected: weakening a safety guard to reduce inexpensive false positives invites bypasses. Instead the deny messages self-document — the denial is the one channel guaranteed to be read at the moment of confusion, so it carries the workaround.

Build:
- plugin/si-plugin/hooks/pre_tool_use.py git-safety section: add deny patterns for git add -A, git add --all, git add ., and git commit -a / -am. Boundary care: git commit --amend must not match; git add ./path (explicit path) must not match. Denial message teaches explicit staging — name each path: git add <path> <path>.
- plugin/si-plugin/hooks/pre_tool_use.py: extend every git-safety deny message — the existing reset --hard / push --force pair and the new add/commit patterns — with one line: commands containing the pattern as data (tests, quoting, documentation) trigger this denial too; assemble such strings at runtime instead.

Test:
- Claude-run: invoke pre_tool_use.py directly with synthetic tool-call payloads — each forbidden form denied with the teaching message; near-misses pass (git commit --amend, git add <specific path>, git add ./scripts/x.py). Assemble test strings at runtime per the workaround from the earlier hook-test session, since the host hook denies command text containing the patterns.
- Host-side (after push + reinstall): live denial on a deliberate git add -A in a scratch context. Needs the deferred-test discipline — flag at /done if it can't run.

**Vocabulary rule: name background-only terms; require translate-or-omit when narrating** **[narration-vocabulary]**

plugin-behaviour.md already says internal procedure terms must not appear in user-facing chat, but the rule rides on Claude's judgment of which terms count as internal. Observed leakage in the last /plan session ("the loop," "Step 2") shows the rule is too abstract to catch the actual offenders. The fix is to name them: a short Vocabulary section listing background-only terms (loop, Step N, Phase X, sub-step, pass, gate, batch slug, etc.) and the companion rule — when narrating to the user, translate to user-facing language ("the next item," "moving through them one at a time") or omit the structural reference entirely. Marker-based enforcement (inline tags on internal terms in procedure prose) is deferred to a follow-up capture; ship the rule first, see whether Claude leaks despite the explicit list, then decide.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md: add a Vocabulary section under Communication listing the background-only terms (loop, Step N, Phase X, sub-step, pass, gate, batch slug, plus any others surfaced while drafting). State the translate-or-omit rule with one or two short examples ("the loop" → "the next item" or omit).
- plugin/si-plugin/docs/plugin-behaviour.md: cross-link the new section to the existing "no internal terms in user-facing chat" rule so the relationship is explicit — the new section sharpens the old rule by naming the offenders, not replacing it.

Test:
- Self-verifying on the next /plan or /next run: does Claude still narrate in structural terms, or does the explicit list catch it.

**Generalize audit-batch definition: lead with output contract, drop docs-as-target framing** **[audit-definition]**

The audit-batch type was written from the SI-developing-itself case (Claude reads procedure docs against criteria) and the wording reflects that. plan.md's thinking-work exception names the defining property as "systematic read of target docs against fixed criteria"; the sizing gate's vague-target example is "the procedure docs"; next.md's Audit procedure intro frames the shape as "systematic read of the target"; Step 2 says "Open every file named by the target." All four embed docs-as-target. The real defining property is the output contract — findings to Captures, no direct edits to artifacts — and that's what differentiates audit from build and test. Reader is always Claude; what gets read (procedure docs, the user's spec, code, UI flows, workflow output, any other artifact) is an implementation detail. Generalizing the wording lets audit cover any artifact type without rewriting the definition each time a new audit shape comes up. Doesn't change procedure substance — read-many-propose-many still describes how audits run — just lifts the assumptions out of the type's definition. Folded in from a capture: the same rule's "build" qualifier and exception framing let thinking work through as audit batches (the walkthrough batches promoted with decision-list outputs) — so the rewrite also drops the qualifier and recasts audit as a separate category defined by its output contract, not an exception to the thinking-work rule.

Build:
- plugin/si-plugin/docs/plan.md ground rules (line 11, thinking-work rule): three changes folded together. Drop the *build* qualifier — the rule covers all batch types, since thinking work can arrive in any batch shape. Reframe audit as a separate category rather than "the one exception": audit produces findings routed to Captures, thinking work produces decisions, and the two don't overlap — the exception framing is what made systematic-read-shaped thinking work look qualified. Key audit's definition on the output contract (findings to Captures, no direct edits) rather than "systematic read of target docs against fixed criteria" — the no-direct-edits property is the load-bearing reason, not the read-docs shape. Sharpen the closing test to match: output is decisions → planning work, run it in /plan; output is findings from a systematic read, routed to Captures → audit batch. Same test applies per seeded item, not just per batch: an audit's seeded check-items must be finding-shaped; decision-shaped checks (reconciliation, is-this-already-resolved) get resolved at planning time, not queued — observed at [output-tag-audit], where a seeded reconciliation item's resolution was a planning decision made mid-/next.
- plugin/si-plugin/docs/plan.md Step 3 (Audit batch sizing gate, line 107): keep the gate's substance (target + criteria specific enough that Claude can apply them) but broaden the vague-target example beyond "the procedure docs" so the gate reads as generic ("the docs", "the code", "the UI flows" — pick one or two).
- plugin/si-plugin/docs/next-audit.md intro (line 3): lead with the output contract, then describe the procedure shape (read-many-propose-many). Name target variety explicitly — procedure docs, user's spec, code, UI flows, workflow output, any other artifact — so the procedure reads as generic, not docs-specific.
- plugin/si-plugin/docs/next-audit.md Read the target section (line 7): change "Open every file named by the target" to "Read every artifact named by the target" so the procedure language doesn't assume files. Keep the criterion-pass-by-pass instruction — that generalizes cleanly.
- Sweep setup.md and done.md for stray audit-as-docs-read references; revise to match the generalized framing if any are found.

Test:
- Self-verifying from the doc text. After the rewrite, the audit-batch wording reads cleanly for any artifact type without requiring "(but adapt to your case)" handwaving.

**Pre-existing content handling in /setup Case B** **[setup-preexisting-content-handling]**

Setup.md is silent on what to do with pre-existing non-method content in a Case B folder (some content present, no method docs). Observed in a real /setup run on a tax-prep folder with one pre-existing brief: Claude judgment-called to peek at the brief before Q1 (used it to frame a clarifier without pre-answering) and to leave it untouched during scaffolding while naming it in the closing message. Both calls landed, but a different run could skip the peek (asking Q1 cold and missing context) or pre-answer Q1 from the brief (bundling, against the rules). The fix is to make both behaviours explicit so they don't ride on judgment.

Build:
- plugin/si-plugin/docs/setup.md Case B branch: add a rule that Claude peeks at any pre-existing user content before Q1 — use it to frame the question with a parenthetical clarifier if useful, never to pre-answer it. One short example showing the framing-vs-bundling line.
- plugin/si-plugin/docs/setup.md Case B branch: add a rule that pre-existing user content is left untouched during scaffolding and explicitly named in the closing message as a source doc the user can refer back to.

Test:
- Self-verifying on the next /setup run in a Case B folder.

**Forbid illustrative expansion in /setup Q4 batch entry** **[setup-q4-no-expansion]**

Setup.md Q4's rule is currently "Use the user's words, don't expand or split — scope decisions belong in /plan." Observed in a real /setup run: Claude wrote the batch with parenthesized examples drawn from a pre-existing source doc ("e.g. overlocker receipt, mortgage interest %"). Parenthesized examples read as illustrations not commitments, but they're still expansion beyond the user's words — and a queue entry with examples looks like the user agreed to those items even when they're in parens. The rule needs tightening: no expansion at all, even illustrative. If examples would clarify what's in scope, the place is a Q4 follow-up question to the user, not a parenthetical in the written entry.

Build:
- plugin/si-plugin/docs/setup.md Q4 rule: tighten the existing "Use the user's words, don't expand or split" to forbid illustrative expansion explicitly — "Use the user's words verbatim. No expansion, no illustrative examples, no parentheticals drawn from visible context. If examples would clarify scope, ask a Q4 follow-up; don't smuggle them into the entry."
- plugin/si-plugin/docs/setup.md Q4 rule: note that the existing one-follow-up-max rule for vague answers covers the case where examples actually are needed.

Test:
- Self-verifying on the next /setup run where Q4 is answered and visible source content exists.

**Setup close-outs name /done; scaffolding creates the repo** **[setup-closeout-redesign]**

From three [close-out-audit] findings (e120f3d), routed together as one design decision. setup.md is the only skill whose session ends never name /done. Step 4 closes with "/plan or /next" and stops. Step 2C's migration close does the same and reads no project state. So the scaffolded files sit uncommitted, no LOG entry gets written, and the project record starts with a gap — a consumer's first session teaches them to skip the close-out habit. The /next offer also contradicts setup's own Q4 rule: the interview deliberately writes the first entry rough and defers scoping to /plan, yet the close-out sends that unscoped entry toward execution. Two gaps surfaced at routing ride along. A fresh consumer folder has no git repository, so a /done recommendation is only honest once scaffolding creates one. And /done routes by _build.md, so a migration close can't blindly recommend /done when an interrupted build is present — the right pointer there is resuming the build.

Build:
- plugin/si-plugin/docs/setup.md Step 2 scaffold list: create a git repository when none exists, as part of scaffolding — silent and mechanical, like the rest of the scaffold. This is what makes the /done close work in a fresh consumer folder.
- plugin/si-plugin/docs/setup.md Step 4 close-out: replace "Run /plan to scope your first batch, or /next if you're ready to build" with a close that recommends /done. The file-list display stays as consent display — it shows what appeared in the folder; the LOG entry /done writes remains the session's single summary. State that relationship in one line.
- plugin/si-plugin/docs/setup.md Step 2C item 4: make the migration close state-aware — leftover _build.md present: name the interrupted build and recommend resuming it with /next, noting the migration changes get picked up at that build's close; otherwise recommend /done, matching Step 4.
- plugin/si-plugin/docs/done-plan.md: widen the close-out to setup-shaped sessions — the entry template's framing covers scaffolding sessions (what was set up and why, not "queue changes"), and recommend-next gains a branch: a fresh project whose only batch is the rough Q4 entry recommends /plan, never /next, because that entry is deliberately unscoped.

Test:
- Doc edits self-verifying. Behavioural, host-side (after push + reinstall): the next real /setup run in a fresh folder — repo created silently, close names /done, /done writes a setup-shaped LOG entry and commits the scaffold. Needs the deferred-test discipline — flag at /done if it can't run.

**Project-agnosticism sweep: rewrite setup.md to read for non-app projects too** **[setup-project-agnosticism-sweep]**

setup.md is the on-ramp every project enters through, and its current wording assumes the user is building an app: the five interview questions, the Step 4 close-out, the Step 1 folder-state cases, and the three scaffolded doc templates (SPEC.md, QUEUE.md) all use app-building framing ("building," "components," "functionality," "source code," "builds first then tests"). The behaviour-agnosticism audit (fac25ab) surfaced 11 findings; seven collapse into one sweep of mechanical-or-near-mechanical rewords applied across setup.md and its scaffolded templates. The Step 4 close-out reword originally counted here moved to [setup-closeout-redesign], which replaces that line entirely. The three more substantive findings — REGISTRY.md noun choice (Q3.5 interview question), the spec-entry-trigger threshold across project types, and plugin-behaviour.md doc-routing — are held in separate captures for their own consideration. This sweep changes wording only; no interview-flow changes, no rule-trigger changes.

Build:
- plugin/si-plugin/docs/setup.md Q1: reword to "What is this project, and who is it for?" (drop "building"). From [setup-q1-agnostic-wording].
- plugin/si-plugin/docs/setup.md Q2: reword to "What's the core of it — the main thing it produces, organises, or does?" (drop "functionality / does"). From [setup-q2-agnostic-wording].
- plugin/si-plugin/docs/setup.md Q3 examples: replace software-only example set with 3–4 examples spanning software + non-software projects. From [setup-q3-agnostic-examples].
- plugin/si-plugin/docs/setup.md Q4: reword inclusively — "What's the first thing to build or do? What would you want to have working or made progress on by the end of today?" Keeps build-shape framing for app projects, adds do/progress framing for others. From [setup-q4-inclusive-wording].
- plugin/si-plugin/docs/setup.md Step 1 folder-state cases: reword Case A / Case B to "No content" / "Content exists" (or similar project-agnostic phrasing). From [setup-step1-case-wording].
- plugin/si-plugin/docs/setup.md SPEC.md template (line 48): reword "What the app is" to "What the project is". From [setup-spec-template-agnostic].
- plugin/si-plugin/docs/setup.md QUEUE.md template (line 63): reword "Each batch is one /next session — builds first, then tests." to "Each batch is one /next session. Subheadings name the kind of work (Build, Test, Audit)." From [setup-queue-template-type-complete].

Test:
- Self-verifying from the doc text. After the rewrite, setup.md reads cleanly for a tax-prep, records-keeping, research, or writing project as well as for an app project.
- E2E follow-up (user-run, separate live session, queue as separate batch if desired): rerun /setup in a non-app folder and observe whether the questions land cleanly.

**setup.md goes tag-free: self-contained prose carries the behaviour** **[setup-self-contained-no-tags]**

From [output-tag-audit], the structural finding. setup.md's response-shape tags reference definitions that live in plugin-behaviour.md, which is injected only in adopted projects — and /setup's working cases run unadopted, so the tags are undefined tokens there. The prose restatements beside them are the real carriers. Decided at routing: setup.md stays deliberately self-contained in prose, and the tags come out — the alternative (inlining a compact copy of the definitions) creates a second, weaker copy that drifts, which is the duplication this arc keeps removing. Extends the [trickle-up-ask-when-unsure] precedent that setup.md carries its own copies by design. setup.md is exempt from [tag-restatement-trim] for the same reason.

Build:
- plugin/si-plugin/docs/setup.md: remove the three tag tokens ([BRIEF], [SEQUENCE, PROMPT], [BRIEF, PROMPT]). At each spot, check the adjacent prose carries everything the tag claimed — stop-and-wait, one-per-message, brevity — and write the missing piece where it doesn't. Locate by content, not line numbers.
- plugin/si-plugin/docs/setup.md, near the top: add one line stating why this doc carries no response-shape tags — its sessions run before the behaviour rules load, so prose carries the behaviour. This guards against a future session "fixing" the inconsistency by re-adding tags.
- plugin/si-plugin/docs/setup.md, the two untagged interaction spots from the same audit, landed as prose per this batch's decision: in Case C, make the wait explicit — tell the user, offer /plan, stop, and wait for their answer. In the Step 2 scaffolding, add a line that the work runs without narration — the close-out reports the file list, so nothing is lost by staying quiet.

Test:
- Self-verifying from the doc text. Behavioural: the next live /setup run should still ask one question per message and wait — now on prose alone.

**REGISTRY.md goes noun-free: drop "components," decouple from builds** **[setup-registry-template-and-noun]**

The scaffolded REGISTRY.md template assumes projects have "components" and that builds are what add to it — wrong on both counts for non-app projects (a tax-prep project registers a receipts folder, a lender list, a year-end packet, entered via audit or freeform work). The filed Q3.5 proposal — ask the user "what are this project's parts called?" and bake their noun in — was rejected twice over: asking a non-coder to do ontology cold is exactly the jargon-shaped interaction the interview avoids, and even deriving the noun from interview answers proved unnecessary once the right question got asked — nothing actually needs the noun. The template header goes noun-free, the update trigger decouples from builds, and conversation already speaks the user's domain words via the use-the-user's-language rule. This decision is the noun strategy [plugin-behaviour-doc-routing-agnostic] was parked waiting on: neutral wording everywhere in plugin-shipped docs, the user's own words in conversation. Sibling to [setup-project-agnosticism-sweep] — same file, held out of it only for the interview-question consideration, which is now settled.

Build:
- plugin/si-plugin/docs/setup.md REGISTRY.md template: reword the header noun-free — "What exists in this project. Updated as the project grows." (or equivalent) — dropping "Components" and "after each build."
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md: reword the REGISTRY.md description ("components list") noun-free to match.
- plugin/si-plugin/docs/done.md (and per-type sub-docs if they name it): reword the registry-update step's "components" language noun-free — what's new gets registered, regardless of how it entered the project.
- plugin/si-plugin/docs/plugin-behaviour.md, doc-routing bullet (Routing and discipline): reword agnostic — "what/who/how/why the project exists" for SPEC.md, and "what exists in the project, where it lives" for REGISTRY.md — matching the noun-free registry template. Folded in from [plugin-behaviour-doc-routing-agnostic], which inherited this batch's noun strategy.

Test:
- Grep "component" across plugin/si-plugin/docs and templates after the edit — remaining hits only where the software meaning is genuinely intended (expected: none in consumer-facing scaffolding).

**Key the spec-entry trigger on SPEC.md itself, not "features"** **[spec-entry-trigger-rethink]**

The pipeline rule — "New features need a spec entry before a build entry … Threshold: if a user would see or experience the difference" — assumes the project ships features to external users. Owner-only projects have neither, and the capture feared the rule would have to split per project type. It doesn't: both load-bearing problems dissolve by keying the trigger on the spec rather than a category of change — if landing the change would make SPEC.md's description of the project wrong or incomplete, update SPEC.md first. "Features" disappears (refactors pass untouched because they change no spec sentence; new capabilities, scope changes, and new output types all trip it, any project type); the audience question evaporates rather than getting answered, since noticeability was always a proxy for "the product truth changed" and the new form tests that directly. Mechanically checkable on a weak model: read SPEC.md — /plan already requires that — and ask whether any sentence in it goes wrong or incomplete. The per-type split stays rejected: two rules are double maintenance, one self-referential test covers both shapes. Same noun-free move as [setup-registry-template-and-noun]. From [behaviour-agnosticism-audit].

Build:
- plugin/si-plugin/docs/plugin-behaviour.md Routing and discipline, spec-entry pipeline bullet: replace the features-noun trigger and the noticeability threshold with the self-referential form — if landing this change would make SPEC.md's description wrong or incomplete, update SPEC.md first. Keep the pipeline sequence (idea → question if unclear → SPEC.md → QUEUE.md) unchanged.
- plugin/si-plugin/docs/plan.md ground rules, the pipeline line: matching reword — "spec entry (if it changes the product)" keyed to SPEC.md truth the same way, so the canonical statement and the restatement can't drift.

Test:
- Self-verifying from doc text: the rule reads cleanly for an app project and a tax-prep project alike, with no audience named.

**Reframe /plan Step 1 entry + follow-up as sequencing, not either/or** **[plan-step1-sequencing]**

plan.md Step 1's entry question ("Do you have something to discuss, or ready to process Captures?") and its follow-up after a discussion item ("Anything else, or ready for Captures?") both use "or" framing that reads as a branch — discuss-vs-process — when /plan always processes Captures and a discussion item is just an optional pre-step. The misreading surfaced twice in the 7563bc0+1 /plan: Claude reproduced the framing in the read-state summary ("if processing...") and bundled an unrelated housekeeping decision onto it as a conditional, the same wording bug surfacing in Claude's own output. Fix the wording so processing reads as the destination and discussion as the optional thing that happens first if there is one. Folded in from an [output-tag-audit] finding: the same two lines are stop-and-wait moments with no [PROMPT], and Step 1's scan block says "collect them silently" with no [SILENT]. Tag-only fixes. They ride along here because this batch rewrites two of the three lines anyway — tagging text another batch rewrites would collide.

Build:
- plugin/si-plugin/docs/plan.md Step 1 entry question: replace "Do you have something to discuss, or ready to process Captures?" with wording that frames processing as the destination — e.g. "Anything to discuss before we process Captures?" Keep the empty-Captures branch ("If Captures is empty, ask what they'd like to work on.") as-is. Tag the question [PROMPT].
- plugin/si-plugin/docs/plan.md Step 1 follow-up after a discussion item: replace "Anything else, or ready for Captures?" with matching wording — e.g. "Anything else before Captures?" Tag it [PROMPT].
- plugin/si-plugin/docs/plan.md Step 1 unpark + staleness scan block: tag it [SILENT]. The prose already says "collect them silently" — the tag makes it binding.
- plugin/si-plugin/docs/plan.md Step 1 branching structure ("If the user has something" / "When ready: Move to Step 2"): adjust so the prose matches the new framing — discussion items run first if present, then Step 2 always runs, no either/or branch.

Test:
- Self-verifying from the doc text on the next /plan run. The entry question and follow-up should read as sequencing, and Claude shouldn't reproduce "if processing" or similar branching framing in narration.

**Approval-time outputs render as blockquotes with a content-type lead-in** **[approval-display-blockquotes]**

Supersedes [fenced-block-content-type-label], whose label design assumed a fence language slot. User feedback (2026-06-11): the desktop app's fenced blocks don't wrap, so long drafts run off-screen and get read incompletely — defeating the fence's purpose, exact text read and approved. Blockquotes wrap. The standard, live-tested through a full /plan session: approval-time and verbatim displays render as markdown blockquotes, with a bold lead-in line above the quote naming the content type (batch draft, capture draft, commit message, log entry, parking reason). One exception: content whose exact characters are the substance — code, shell commands — keeps a fence, because rendering would corrupt it. Trade-off accepted at routing: a blockquote renders markdown, so syntax slips in a drafted entry are invisible to the approval read. Division of labour recorded: the human approves meaning; [queue-format-lint-hook] checks structure at write time.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md, the approval-time outputs rule: rewrite from fence to blockquote-with-lead-in, carrying the why (fences don't wrap; an unread draft defeats approval), the canonical content-type labels, and the code-keeps-fences exception.
- Sweep every procedure doc naming "fenced code block" at an approval or display moment — plan.md's promote sub-step, next-build.md's two capture-routing spots, next-test.md's, next-audit.md's (check what remains of it after [audit-findings-bulk-approval]), and the done family — and point each at the new standard. Locate by content, not line numbers.

Test:
- Behavioural, host-side (after push + reinstall): the next /plan or /done approval draft arrives as a labelled blockquote that wraps. Needs the deferred-test discipline — flag at /done if it can't run.

**Require an explicit ask after every approval-time draft** **[approval-ask-after-draft]**

Procedure docs show drafts for approval but never say to ask. plan.md's promote step says "Don't write to QUEUE.md until approved," the approval-time rule says to fence the draft, and the stop-and-wait tag already sits on the promote step — so Claude stops, but stopping silently satisfies all of it. Observed across multiple /plan sessions and confirmed as direct user feedback: the draft appears, then silence, leaving the user to figure out what's wanted. The fix sits one level above any single skill, because /done's LOG entries and commit messages and /setup's drafts can all fail the same way: every approval moment must end with the question.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md "approval-time outputs go in a fenced code block" rule: extend so presenting the block is only half the move — the message must end with an explicit ask naming the decision needed (e.g. "Approve this wording?", "Write it to the queue?"). Silence after a draft fails the rule even when Claude has stopped to wait. Author the rule compliance-hardened from the start — why-clause plus positive constraint per resources/research/model-instruction-compliance.md (e.g. "a draft isn't actionable until the user knows what's being asked; end the message with the question") — rather than hardening it in a later pass.

Test:
- Self-verifying from doc text on the next /plan or /done run — every draft shown for approval should be followed by an explicit ask.

**Captures and batch entries authored plain: complete, not compressed** **[human-readable-authoring]**

User feedback (2026-06-11), surfaced by the first verbatim-first presentation: captures and batch rationales were written in long clause-chained sentences — dense Claude-for-Claude style that the co-reading human couldn't comfortably read, at filing time, at presentation, and at approval. One batch rationale had to be rewritten live before the user could understand what she was approving; the plain rewrite carried the same content and was approved as the replacement. The load-bearing insight: what Claude needs from these artifacts is completeness — facts, references, conditions preserved — not syntactic compression. Same information, shorter sentences, one idea per sentence; the modest token cost is accepted. Home is plugin-behaviour.md because every skill drafts these — /next routes discoveries to Captures mid-build, /done routes stragglers at close, /plan writes both.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md Captures rule: add the authoring standard, compliance-hardened from the start (why-clause, positive constraint, explicit scope per resources/research/model-instruction-compliance.md) — keep everything (facts, references, conditions); write it in short sentences, one idea per sentence; the human co-reads this text and approves it, so unreadable is unapprovable. This is the canonical statement.
- plugin/si-plugin/docs/plugin-behaviour.md, the why-pipeline's rationale-authoring guidance: one line extending the same standard to batch rationales and pointing at the canonical statement — no duplication.

Test:
- Behavioural on later sessions of any skill: freshly authored captures and rationales read in plain sentences without losing references or conditions. Already validated live across this session's drafts.

**Show-before-write keyed to the action, not the loop** **[show-before-write]**

plan.md already says never write batch entries without showing the exact text first, but the rule rides on the loop's beats — and the beats live in conversation memory. Observed 2026-06-11, deep in a compacted session: a recommendation concrete enough to read as a draft merged the two approval beats, and an entry was written unshown. The hardened form needs no memory of which beat the item is on, because it keys to the write itself: the message immediately before any QUEUE.md batch write must contain the entry text verbatim, and approval attaches to shown text, never to a described shape. Sibling insurance to [plan-state-artifact], which fixes the structural cause; this rule holds even with no state at all.

Build:
- plugin/si-plugin/docs/plan.md ground rules: harden the show-first rule to the action-keyed form, compliance-hardened from the start (why-clause, positive constraint, explicit scope per resources/research/model-instruction-compliance.md) — the message immediately before any QUEUE.md batch write contains the entry verbatim; approval attaches to shown text, not to a described shape; a recommendation, however concrete, is not a draft.

Test:
- Behavioural, host-side (after push + reinstall): later /plan sessions write nothing to the queue without the verbatim entry in the immediately preceding message. The case to watch is late-session, after compaction — where the original slip happened.

**/plan resolves what it can; capture is only for what it can't** **[plan-resolves-by-default]**

/plan has twice (observed) deferred work it could have done in-session: once by filing a capture asking /next to re-verify line refs and quoted strings after terseness edits, once by recommending park-with-"research needed" on the fenced-block label question that /plan itself was the right home for. Both were misroutes — /next executes the top batch and doesn't parse captures; "research needed" is the same skill-self-deferral. The pattern: when work is resolvable now and /plan is the home for that kind of work, doing it now is /plan's job. Capture is reserved for things /plan genuinely can't resolve in-session — needs more data than the session has, needs design discussion across sessions, needs user input not yet available, or surfaces a structural question whose answer would gate the work. Adding the rule to plan.md ground rules names it explicitly so the default flips from defer-via-capture to resolve-now.

Build:
- plugin/si-plugin/docs/plan.md ground rules: add a bullet stating /plan resolves what it can in-session — research, queue-wide cleanup (line-ref drift, quoted-string staleness after sweeps), cross-batch reconciliation, doc verification, anything else within /plan's reach. Capture is for things /plan genuinely can't resolve: needs data, needs design discussion, needs user input, surfaces a structural question that would gate the work. Frame the rule as a default, not an absolute — the test is "can /plan resolve this with what it has right now."

Test:
- Self-verifying from doc text on the next /plan run where a resolvable-now item surfaces. Claude should do the work in-session instead of filing it as a capture.

**Detect and roll in user edits at /done commit time** **[user-edits-rollup-on-commit]**

User-made edits to target-tree files (plugin/si-plugin/) can happen at any time — mid-session, between sessions — but /done's per-build commit only stages files the build touched. Those edits sit dirty across sessions until the push-and-rezip ritual catches them at push time. Observed: 5 docs files stayed dirty across at least two sessions. The gap is /done's commit, which is the natural moment to detect and offer to include them. The push-and-rezip sweep stays as the safety net; this adds an earlier catch point.

Build:
- plugin/si-plugin/docs/done.md: at the commit step, add a sub-step — run `git status --porcelain plugin/si-plugin/`, compare against the active build's file list, surface any dirty paths outside scope with a one-line summary, and offer to stage + roll them into the commit.

**Session-start dirty-tree warning** **[session-start-dirty-tree-check]**
Depends on: [user-edits-rollup-on-commit], [deferred-tests-structural-home] (host-side)

session_start reports project state but not git state. A consumer project dirty at session start almost always means the previous session ended without /done — work sitting unrecorded that a non-coder won't notice for weeks (observed here: five doc files dirty across two-plus sessions, compensated by a manual check in this project's CLAUDE.md). The hook generalizes that check so every consumer project gets it: git status --porcelain at session start, one line when dirty. The Depends on is real, not thematic: the warning's promise — "/done will pick them up" — only becomes true once [user-edits-rollup-on-commit] teaches /done to offer dirty out-of-scope paths into its commit. Silent when _build.md exists: mid-build dirt is expected, not orphaned. Sibling to the hook cluster ([hash-backfill-as-hook], [queue-format-lint-hook], [git-add-safety-hook-gap]); shares session_start.py with the backfill hook, so whichever builds second sees the other's changes.

Build:
- plugin/si-plugin/hooks/session_start.py: run git status --porcelain; when non-empty and no _build.md is present, emit one line via additionalContext — "N files have uncommitted changes from a previous session — /done will pick them up."
- This project's CLAUDE.md (host-only, does not propagate via reinstall): remove the manual "Session-start dirty-tree check" section — the hook supersedes it. Accepted: a brief gap between this edit and the reinstall that activates the hook.

Test:
- Claude-run: session_start.py against a fixture repo — dirty tree without _build.md warns with the correct count; dirty with _build.md stays silent; clean stays silent.
- Host-side (after push + reinstall): live one-liner at the next session start with known dirt. Needs the deferred-test discipline — flag at /done if it can't run.

**Per-session /plan state artifact: _plan.md** **[plan-state-artifact]**
Depends on: [session-start-dirty-tree-check]

The capture-processing loop runs several beats per item, and the session's position in it lives only in conversation memory. A long compacted session lost a beat and wrote an entry unshown — the exact failure [short-session-design-target] predicts: memory covering for missing structure. "Planning sessions stay short" was the assumption, and 2026-06-11 disproved it. /next already externalizes execution state to _build.md; planning gets the same treatment. The artifact pays beyond the slip: it survives compaction, gives an interrupted /plan a resume path through session_start the way an interrupted build has one, and hands /done a mechanical record of what was routed where instead of a reconstruction from conversation. Sibling: [show-before-write] is the zero-state insurance at the write action; this batch removes the structural cause. The Depends on is real: one build entry extends the dirty-tree warning that batch installs.

Build:
- plugin/si-plugin/docs/plan.md: create _plan.md when capture processing begins — carried candidates, the item list, current item, beat reached. Update at each beat transition; append each routed item with its disposition (promoted, parked, dropped — with slug). One line per item so updates stay cheap.
- plugin/si-plugin/hooks/session_start.py: detect a leftover _plan.md the way _build.md is detected — report an interrupted planning session and point /plan at resuming from the recorded item and beat. Shares this file with the other hook batches; whichever builds second sees the other's changes.
- plugin/si-plugin/docs/done-plan.md: read _plan.md's routed list when writing the LOG entry; delete the artifact at close — same lifecycle as _build.md.
- plugin/si-plugin/hooks/pre_tool_use.py: verify _plan.md presence doesn't trip any build-scope behaviour; adjust only if it does.
- The dirty-tree warning from [session-start-dirty-tree-check]: extend its silence condition — uncommitted changes with _plan.md present are expected mid-plan, same as mid-build dirt with _build.md. Locate by content.
- plugin/si-plugin/templates/faq-template.md (+ index line): FAQ entry — what _plan.md is, why it appears in the project, why not to delete it.

Test:
- Claude-run: session_start.py against a fixture repo — leftover _plan.md detected with the right report line; neither artifact present, silent.
- Host-side (after push + reinstall): interrupt a /plan mid-processing, open a new session, watch for the resume offer. Needs the deferred-test discipline — flag at /done if it can't run.

**Loosen checkpoint wording: off-ramps available, not identically phrased** **[checkpoint-wording-loosen]**

The plan.md Step 2 checkpoint rule ("Offer three options every time, in uniform phrasing") pulls Claude toward rendering a numbered list at every checkpoint, which reads as bureaucratic form-fill. Observed across multiple /plan sessions — not a one-off. The rule's intent is sound (all three off-ramps available after every item), but "uniform phrasing" is being read as "identical wording each time." Loosening the wording so the three options must be available but can be delivered conversationally fixes the robotic delivery without losing the guarantee.

Build:
- plugin/si-plugin/docs/plan.md Step 2 sub-step 6 (Checkpoint): reword so the three off-ramps (continue to next, close out, share something else) are required to be available after every item, but drop "uniform phrasing" — conversational delivery that covers all three is fine.

**Add forced app-identification check to INSTALL.md routing** **[install-app-identification-check]**

The Claude Code / Claude chat app distinction is load-bearing for install routing but stated in one sentence inside Q2 that the desktop-app-confused persona read straight past. Result: confident misroute to Branch B, crash at a Customise menu hunt with no recovery path — the helping Claude would troubleshoot the missing menu rather than diagnose wrong-app. A screenshot or icon comparison goes stale; a forced positive identification check ("what does the title bar say?" or "does the window have a terminal-style input or a chat interface?") is self-correcting and version-independent. The check must happen before routing, not after — catching wrong-app after Branch B starts is too late.

Build:
- INSTALL.md Q2 section: replace or augment the current one-sentence distinction with a forced identification step — the user must report what they see (title bar text, interface description, or similar) before the guide routes them to Branch A or B.
- Add a wrong-app recovery path: if the identification check reveals the chat app, tell the user what Claude Code is and where to get it, then route to Branch A.
- Remove the "check Applications folder" hint that assumes the user can distinguish two Claude apps by name alone.

**Move AI-facing content out of the human's reading path in INSTALL.md** **[install-separate-ai-instructions]**
Depends on: [install-app-identification-check]

INSTALL.md opens with a "Note to Claude" block and closes with pacing rules — both AI-facing, both in positions the human reader hits first or last. Four out of four test personas bounced off the opening block. The guide is designed to be pasted into a Claude chat, so both human and AI content must stay in one file — but the AI content should be out of the human's natural reading path. Fix: restructure so human-readable content (what this is, who it's for, what to expect) opens the file; AI-facing instructions move to a clearly-marked section the human can skip. Folded in from [install-no-bypass-for-experienced-users]: the already-installed persona abandons the walkthrough at Step 1 — the three-question interview is dead weight for someone with Claude Code, a paid plan, and prior plugin experience — so the new introduction also carries an experienced-user bypass.

Build:
- INSTALL.md: move the "Note to Claude" frontmatter and the pacing rules block into a single clearly-marked AI-facing section (e.g., at the end of the file, or in a collapsed block with a "skip this" label).
- INSTALL.md: add a brief human-facing introduction at the top — what the guide is, who it's for, what to expect from the walkthrough.
- INSTALL.md: include an experienced-user bypass line in the introduction — "already have Claude Code and a paid plan?" — pointing via in-page anchor to the identification check, and Branch B beyond it. The bypass skips the interview, never the app-identification check.
- Verify the restructured guide still works when pasted into a Claude chat: Claude must still find and follow the AI instructions despite their new position.

**Surface paid-plan requirement before INSTALL.md interview** **[install-paid-plan-upfront]**

The paid-plan requirement (Pro minimum) is introduced at Q3 of the install interview with no preamble. Cold-stranger persona left to google pricing and didn't come back; free-plan persona hit it as a contradiction of lived experience. "Pay-as-you-go API credit" reads as uncapped to non-coders; plan limits aren't stated. Moving the requirement before Q1 turns it into an informed-consent gate — users who can't or won't pay learn that immediately instead of three questions in.

Build:
- INSTALL.md: add a brief upfront section before Q1 stating that a paid Claude Pro plan is required (not Max — Pro is sufficient), with a pointer to Anthropic's pricing page rather than an embedded dollar figure.
- INSTALL.md: remove or rewrite Q3's current paid-plan discovery so it doesn't re-ask what the upfront section already established. If Q3 serves a routing purpose beyond the paywall check, keep the routing and drop the discovery.
- INSTALL.md: clarify what "within plan limits" means in plain language — what happens when you hit the limit, is it a hard stop or a throttle.
- INSTALL.md Step 1 routing: replace "no paid plan" with "free plan or no plan" (or equivalent unambiguous phrasing) so free-plan users don't self-route past the paywall gate. If the upfront section makes this routing line redundant, remove it.

**Clarify plugin upload path and drop hedge in INSTALL.md** **[install-upload-path-clarity]**

All four test personas stalled at the plugin upload step. The UI path (Customise → + → Create a plugin → browse for .zip) is correct but "Create a plugin" reads as authoring, not installing — three personas hesitated or bailed. The guide's hedge "usually in the top menu or settings area" signals uncertainty and erodes trust. The path is known; the label is counterintuitive. Fix: state the path confidently, warn that "Create a plugin" is the upload path despite the name, add a screenshot, drop the hedge.

Build:
- INSTALL.md: replace the current breadcrumb with the confirmed path — Customise (top left) → + icon on the left → "Create a plugin" → browse and select the downloaded .zip. Drop "usually in the top menu or settings area."
- INSTALL.md: add a one-line heads-up before the "Create a plugin" step that the label is misleading — it's the upload/install path, not an authoring tool.
- INSTALL.md: add a screenshot of the Plugins screen showing the + icon and the "Create a plugin" option, so users can visually confirm they're in the right place.

**Add provenance and download expectation to INSTALL.md GitHub link** **[install-download-provenance]**

The raw GitHub URL for downloading si-plugin.zip triggered suspicion across all four test personas — "FlintCraftTech" doesn't match "Sovereign Implementer," the URL looks like an unknown-sender zip download, and nothing tells the user what happens when they click. Fix: add a one-line provenance statement (FlintCraftTech is the publisher account, Sovereign Implementer is the plugin) and tell the user what to expect (file auto-downloads as si-plugin.zip, or right-click > Save As if it opens in the browser).

Build:
- INSTALL.md: add a provenance line immediately before or after the download URL explaining the name mismatch and confirming it's the official source.
- INSTALL.md: add a one-line expectation — what happens when you click (auto-download as si-plugin.zip), and what to do if it doesn't (right-click > Save As).

**Define "open a project folder" action in INSTALL.md smoke test** **[install-define-open-folder]**

The install guide tells the user to "open a project folder in Claude Code" without defining what that means or what the physical action is. CS doesn't know if they need a special folder or what "open" looks like in the app. The install guide's job ends at "plugin works" — the smoke test just needs any folder open, not a real project. Defining project setup belongs in /setup. Fix: replace "open a project folder" with a concrete action for the smoke test context, and defer real project setup to /setup.

Build:
- INSTALL.md Step B.5 and Step 2: replace "open a project folder in Claude Code" with a concrete instruction — create an empty folder, then open it in Claude Code via File > Open Folder (or whatever the current action is). Frame it as a smoke-test step, not project setup.
- INSTALL.md: add a one-line note that /setup handles real project setup once the plugin is confirmed working.

**Specify the /setup smoke test in INSTALL.md: success signal, failure signal, diagnostics before uninstall** **[install-setup-smoke-test-underspecified]**

The "type /setup" smoke test doesn't say where to type, whether to press Enter, what success looks like, or what failure looks like — the cold-stranger and free-plan personas both stalled there, and the current failure path jumps straight to gear-icon > Uninstall before ruling anything else out. One wrinkle from discussion: plugin skills can render namespaced in the command menu (this project's sessions run /sovereign-implementer:plan, not bare /plan), so a guide that says "/setup should appear" may strand a reader looking at a differently-labelled entry — the success signal must match what the menu literally shows.

Build:
- INSTALL.md smoke-test step: rewrite the "type /setup" instruction to name where to type (the chat box), that a menu of commands appears as you type, which entry to look for, and that Enter runs it. Before writing the success signal, ask the user to confirm the exact menu rendering in the current desktop app (bare /setup vs namespaced form); write it to match.
- INSTALL.md smoke-test step: describe the failure signal explicitly — what the reader sees when the plugin isn't registered (no matching entry appears as they type).
- INSTALL.md failure path: replace the jump-to-uninstall with a diagnostic ladder — (1) check the plugin is present and enabled in the Customise plugin list, (2) start a fresh session, since skills register at session start and a pre-install session won't see them, (3) uninstall and reinstall as the last resort.

**INSTALL.md endings polish: collapse "Updating later", add an end-of-guide close** **[install-updating-later-section-is-padding]**
Depends on: [install-separate-ai-instructions]

The "Updating later" section repeats the install steps the reader just finished — uninstall, download, repeat — and the already-installed persona registered it as trust-eroding padding. A one-liner that points back at the steps instead of restating them carries the same information without the filler, and stays correct when the download and upload wording changes under the other install batches. Folded in from [install-step2-trailing-ellipsis-reads-as-truncated]: the free-plan persona read the Step 2 First-run pointer's trailing prose and was unsure whether the guide had been cut off — an explicit close line marks the end of the human path, which after [install-separate-ai-instructions] sits just before the skippable AI-facing section rather than at the literal bottom of the file.

Build:
- INSTALL.md "Updating later" section: collapse to a single line — "To update: uninstall via the gear icon, download the latest zip from the same URL, and repeat the upload."
- INSTALL.md: add a one-line close at the end of the human reading path — "That's the end of the install guide — your friend's project is now ready to start" — placed just before the AI-facing section once the restructure has moved it to the back.

**Preserve rejected-alternative reasoning in LOG entries** **[log-rejected-alternative-reasoning]**
Depends on: [done-closeout-extraction]

Observed at f123eed: a /plan discussed and resolved a concern about one growing log.md getting too large to read, but the LOG entry recorded only the conclusion — not the concern or the reasoning that addressed it. Two sessions later the user couldn't retrieve why the alternative was rejected and second-guessed the decision, and the log-split design got relitigated. The why-pipeline's preserve rule carries rationale forward, but "rationale" currently means the reasoning behind the decision made, not the reasoning against the alternatives considered. The trigger needs a boundary so entries don't bloat: discussion-level consideration qualifies — a concern raised and resolved, an alternative seriously weighed — passing mentions don't. The intuitive-but-rejected path is the case that most needs preserving.

Build:
- plugin-behaviour.md why-pipeline Preserve rule: extend the definition of rationale to include concerns raised and resolved and alternatives seriously weighed, carried with why they lost. State the trigger boundary: discussion-level consideration qualifies, passing mentions don't, and decisions where the rejected path is the intuitive one always qualify.
- The LOG-entry-writing step in the /done per-type sub-docs (post-[done-closeout-extraction] shape): add one reinforcing check at writing time — does this entry carry any concern that was resolved or alternative that was weighed? Keep it to a single line pointing at the why-pipeline rule; don't restate the rule per sub-doc.

**File research by default when findings are non-trivial** **[research-filing-default]**

plugin-behaviour.md says where research goes (resources/research/) but never when — so filing only happens when the user asks, and findings from mid-conversation web searches stay in chat and evaporate. Observed across sessions; the trigger case was the fenced-block label question, where research had been done but couldn't be retrieved later because it never became a file, and the next /plan offered to redo the search. The fix flips the default: filing is part of using a finding, not a separate request. Visibility matters too — a silent rule can't be checked, so the file gets named in chat when it lands. A /done close-out backstop ("did research happen this session that isn't filed?") was considered and held in reserve in case leakage continues after the rule lands.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md Research section: add the default-filing rule — when a web search or external lookup yields a non-trivial finding, file it under resources/research/<topic>.md as part of using it, not only on request. Threshold: a finding that informed a decision or would have to be redone if lost gets filed; a fact checked once and discarded doesn't. Claude names the file in chat when it lands.
- plugin/si-plugin/docs/plugin-behaviour.md Communication section: fold the existing "File research under resources/research/" line into the Research section so one canonical statement remains.

Test:
- Self-verifying on the next session where a web search yields a real finding — the file should land and be named in chat without the user asking.

**Relationships exist only if written: position never encodes** **[relationships-must-be-written]**

Caught live this session: Claude stripped a Blocks: header from a batch draft, reasoning that adjacency in the queue already carried the relationship — exactly the positional encoding the slug convention exists to prevent, one step earlier than the convention reaches. The existing rule governs how references are written (slugs, never positional pointers) but not the decision of whether to write one, so "placement carries it" passes the current wording while losing the relationship to the next reorder. The user caught it; the rule should have.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md Dependency ownership: add the missing half to the slug-reference bullet — relationships between queue items exist only if written, in a header or as a slug reference in prose; queue position never encodes a relationship; placement is a convenience layered on top, never the carrier. Carry the why: queue order changes every session, so anything encoded as position is one promote or reorder away from silently vanishing.

Test:
- Self-verifying from doc text. Behavioural confirmation on the next /plan that places related batches — the relationship should land in a header even when the batches end up adjacent.

**Name the Blocked-by trigger flavors; non-default triggers must be written** **[blocked-by-trigger-flavors]**

The Blocked by: convention reads "the named slug shipped" as the firing condition, but dependencies carry at least three trigger flavors — landing (B needs A's changes in the tree), findings (B was generated by A's findings), clarity (B needs what A clarified, satisfied the moment the question resolves). The flavor difference is operational, not taxonomic: the unpark watch reads headers mechanically, and a clarity-shaped item under a ships-the-slug reading stays parked past its real readiness — observed live in the 2026-06-10 /plan, where a capture's blocker fired at decision time while the blocking batch remained unshipped, and earlier at 1b7d359. The fix adds no syntax and no flavor field (a closed taxonomy would force nuance into slots — the why-pipeline's own warning): the bare slug form keeps its landing-shaped default, and whenever the real trigger is anything else, the prose tail must state the firing condition. The flavors get named as illustrations of when that's needed, not as a classification to fill in.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md Dependency ownership, the Blocked by / Parked bullet: add the note — bare slug fires when the named item's changes ship (landing, the default); any other trigger (findings-generated, satisfied-at-decision, external event) must be written in the prose tail ("Blocked by: [slug] — satisfied once X is decided"). Name the three flavors with one example each, including that clarity-shaped triggers can fire at /plan-decision time before anything ships.

Test:
- Self-verifying from doc text. Behavioural on future unpark scans: items with non-landing tails fire at their stated condition, not at slug-ship.

**Force the Parked: choice and end its staleness exemption** **[parked-slot-discipline]**

Two accumulation risks share the Parked: slot. Filing: items with nameable behavioural triggers were twice filed Parked: even though the rule says trigger-means-Blocked-by — the slot choice rides on judgment with no forcing question. Review: plan.md's opening scan reads Parked: items only to skip them, so nothing ever asks whether the project has evolved past one; meaningless accumulation is the failure mode. A hand-run sweep already converted the backlog (2026-06-10 /plan, zero Parked: items left); this batch makes the discipline structural so the sweep never needs repeating. Placed after [blocked-by-trigger-flavors] — both shape the same slot-choice rule area.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md, the Blocked by / Parked bullet: filing as Parked: requires first affirming that no nameable trigger exists. State plainly that a behavioural trigger with no slug is a valid Blocked by: tail — the observed misfilings treated slug-less triggers as unparkable.
- plugin/si-plugin/docs/plan.md Step 1 scan: include Parked: items in the staleness watch (drop, rewrite, or keep), replacing "skip unless something else flags them."

Test:
- Behavioural on later /plan sessions: the next trigger-bearing item filed lands in Blocked by:, and the next scan visibly weighs Parked: items instead of skipping them.

**Present captures verbatim-first: quote before thinking** **[capture-verbatim-first]**

After "continue to the next item," Claude reads and thinks first while the user sits with nothing until the full presentation lands. The fix, designed and live-tested across a full /plan session (2026-06-11): the turn opens with a one-line preamble ("here it is, my thoughts to follow" or similar) and the item quoted verbatim, and only then does analysis begin. The live trial surfaced the load-bearing detail: ordering the text on the page isn't enough — the quote must be *sent* before the thinking starts, or it arrives bundled with the analysis and the waiting problem survives. No fresh read is needed; the queue is already loaded from the session's start. Deliberately silent on the rendering device — the approval-time display standard owns that.

Build:
- plugin/si-plugin/docs/plan.md Step 2, present-and-interview sub-step: the turn opens with the one-line preamble and the item's verbatim text, sent before any analysis or file reads begin; engagement and sharpening follow in the same turn. Covers unpark candidates the same way — they enter the same loop.

Test:
- Host-side (after push + reinstall): in the next /plan, the quote should land as its own beat before the analysis arrives — not bundled with it. Needs the deferred-test discipline — flag at /done if it can't run.

**Drop the skill-time re-read of plugin-behaviour.md** **[behaviour-doc-double-load]**

session_start injects plugin-behaviour.md in full every session, and /plan, /next, and /done each instruct a re-read — so every skill session carries the largest doc twice. The re-read insures against compaction aging out the injected copy, but paying double on every session to insure against an occasional event is backwards, and the short-session design target (post-June-20 weak-model sessions) shrinks the compaction risk further. Alternatives weighed: dropping the injection instead would gut outside-skill behaviour — mid-session captures happen precisely outside skills — and the progressive-disclosure restructure (compact core injected, full doc at skill time) costs a content split while the doc is still in flux under the queued audits, and is the *larger* footprint for skill sessions anyway since its skill-time load lands on top of the standing core. Revisit the restructure once the compliance arc settles the doc. /setup is deliberately untouched: it runs in unadopted projects where the injection may not fire, so its own load may be the only copy.

Build:
- plugin/si-plugin/skills/plan/SKILL.md, skills/next/SKILL.md, skills/done/SKILL.md: remove the "Re-read them before continuing" instruction. Keep the sentence naming plugin-behaviour.md as governing the skill — authority stays stated; only the duplicate load goes.

Test:
- Self-verifying from doc text. Behavioural watch after reinstall: any rule-leakage observed in a long session post-change is a mandatory capture (possible future: re-inject after compaction if the desktop app ever supports a compaction hook).

**Classify reference roles in the dependency scan: dependency vs evidence** **[dependency-scan-reference-roles]**

The routing gate parks any capture that names another item — "even if Claude reads the reference as incidental." But references run both ways: the observed case (40749f7+1) cited another item as evidence, and the default would have parked the blocker behind the thing it blocks, inverting the graph. The 2026-06-10 /plan confirmed the distribution problem: four captures in one pass carried evidence citations needing narrated overrides — in a capture style that requires including reasoning and origin, evidence citations may be the majority of references, so the default is tuned backwards. As written, every correct override is a rule violation, which trains a weak model to misroute or to treat rules as optional. Fix keeps the mechanism mechanical — classification by linguistic marker, not vibes: forward-looking language ("once X ships," "after Y," "depends on," "needs") keeps the park default; backward-looking language ("observed at," "see," "surfaced during," "from") lifts it, with the recommendation required to name the reference and its role so wrong classification stays user-catchable; ambiguous keeps the park default, the safe side. Matches the "dependency or citation?" language in [queue-format-lint-hook]'s advisory check.

Build:
- plugin/si-plugin/docs/plan.md Step 2 dependency-scan sub-step: replace the "even if incidental" rule with the two-role classification and its marker lists, the narration requirement for evidence-classified references, and the ambiguity default.
- plugin/si-plugin/docs/plan.md Capture and parking discipline, "Routing gate before recommendation" bullet: same change — the canonical statement and the step must not drift apart.

Test:
- Behavioural on the next /plan pass over citation-bearing captures: evidence citations route without false parking, and each classification is named at recommend time.

**State the short-session design target in CLAUDE.md** **[short-session-design-target]**

Observed on the first Fable day: development tipped to one long session, and three procedure gaps surfaced only because session memory covered them — gaps stop hurting under a capable model, so they stop getting found, while consumers and the post-June-20 development model still hit them. All three named gaps now have structural homes ([deferred-tests-structural-home], the push-ritual backfill folded into [hash-backfill-as-hook], and /next's blocker-gate capture scan), but the principle itself lives only in conversation memory — the exact failure mode it names. A third fix shape, a deliberate-freshness regression ritual, was considered and dropped: after June 20 the development model is the weaker model, so every session becomes the regression test naturally, and building a ritual for a ten-day window is process for its own sake.

Build:
- This project's CLAUDE.md, Rules for Claude: add the design-target rule — the system must work for fresh, short sessions on the weaker model; the files must suffice without session memory; conversation memory is a convenience, never a dependency.
- Same file, the route-observations rule (the "all use of the plugin is testing the plugin" bullet): sharpen with the named trigger — any moment Claude notices session memory covering for something the docs or files should carry is a mandatory capture.

Test:
- Self-verifying from doc text. The behavioural check arrives free after June 20: every short weak-model session exercises the contract.

**Install the scope anchor: one definition of build scope, wired through the docs** **[scope-anchor]**
Blocks: [scope-boundary-rule], [trickle-up-next-md-duplicates]

From [scope-distinction-audit]. Build scope has no canonical definition. The working definition assembles from three places, and plugin-behaviour.md — the only doc injected into every session — says "don't fix things outside current scope" without defining current scope. This batch installs one Scope statement in plugin-behaviour.md and points the skill docs at it. The statement also connects the two enforcement layers no doc currently relates: the entries' described work is the definition, enforced by judgment; the Files: list is its mechanical approximation, enforced by the hook as a backstop. A build can stay within listed files and still exceed the described work, so passing the hook never by itself makes work in-scope. The word "scope" also loses its second sense — the Dependency ownership bullet stops using it for project scope, leaving build scope as the word's only meaning. plan.md gains the authoring side: entries feed the lock, so build entries name their files, and scope gets decided at planning time instead of ask-by-ask at build time. Must land before [trickle-up-next-md-duplicates] deletes next-build.md's restatement — otherwise the rule's only remaining statement uses a term no doc defines.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md: add the Scope statement — build scope is the active batch's entries' described work; the Files: list in _build.md is its mechanical approximation, enforced by the pre_tool_use hook as a backstop; passing the hook never by itself makes work in-scope; work outside scope routes to Captures.
- plugin/si-plugin/docs/plugin-behaviour.md, Dependency ownership: reword "The user owns scope" to "The user owns what enters the queue, what gets parked or dropped, and whether a build expands."
- Grep "scope" across the procedure docs for other project-scope-sense uses; reword those the same way. Build scope becomes the word's only remaining meaning.
- plugin/si-plugin/docs/next.md and next-build.md: point their scope-definition statements at the anchor instead of restating it; keep the skill-specific rules. Locate by content, not line numbers.
- plugin/si-plugin/docs/next-build.md, Scope management: reword the scope-expansion ask from file-shaped to work-shaped — name the work, then the files it needs, listed or not — so work growing inside an already-listed file triggers the same ask a new file would.
- plugin/si-plugin/docs/plan.md Step 3, near the batch structure: build entries name the files they touch; the scope-lock is populated from them; an entry naming no files leaves the lock at method-docs-only. Files that don't exist yet count as named when the entry says what gets created and where.
- plugin/si-plugin/docs/plan.md, readiness gate: add the matching check — can the Files: list be populated from these entries?

Test:
- Grep the definition phrasing across the docs after the edit: one canonical statement in plugin-behaviour.md, pointers elsewhere.
- Grep "scope" for surviving project-scope-sense uses — expect none.

**Define the boundary moves: the discovery decision rule and routing move, stated once** **[scope-boundary-rule]**
Depends on: [scope-anchor]

From [scope-distinction-audit], two findings that are one thought. First: Claude-noticed out-of-scope discoveries have no defined routing move — "note them for the queue" names no destination, no mechanics, no timing, so a weak model can hold them in conversation memory, the exact failure the short-session design target forbids. The fix collapses the three-way split by noticer: who noticed doesn't change the artifact, so Claude-noticed discoveries take the same capture flow user-raised items already get — draft, show, "anything else?", resume — at the moment of noticing. Test failures keep their at-close path; interrupting a test run is the one case with a real reason to defer. Second: the decision rule for mid-session discoveries is real but never stated — needed → ask or split; not needed → capture and continue; premise broken → halt — visible only across five separate passages. It gets stated once, in plugin-behaviour.md beside the routing move, because "not needed → capture and continue" is that move; duplicating it per skill doc recreates the drift the trickle-up arc is removing. The skill docs' sections then read as elaborations of one rule.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md, Routing and discipline: replace "note them for the queue" wording with the defined move — Claude-noticed discoveries route to Captures at the moment of noticing, per the same capture flow as user-raised items (draft, show, "anything else?", resume).
- plugin/si-plugin/docs/plugin-behaviour.md, same spot: state the decision rule once — needed to complete the batch's entries → ask to add (minor) or propose splitting (significant); not needed → capture and continue; premise broken → halt and course-correct.
- plugin/si-plugin/docs/next-build.md (Rules during build) and next-test.md (Rules during test): replace their "note them for the queue" wording with a pointer to the defined move. Locate by content, not line numbers.
- plugin/si-plugin/docs/next-build.md and next-test.md, Scope management: open each section with a pointer to the decision rule so the existing passages read as its elaborations.

Test:
- Grep "note them for the queue" (and close variants) across the procedure docs after the edit — expect zero hits.
- Behavioural: the next /next session that meets a Claude-noticed discovery routes it at the moment of noticing, not "for the queue" at an undefined later.

**Remove rule duplicates from next.md and the per-type docs** **[trickle-up-next-md-duplicates]**
Depends on: [scope-anchor]

next.md and the per-type docs restate four rules that plugin-behaviour.md already carries: SPEC read-only (next-build.md, next-test.md), don't fix outside scope (next-build.md), state regressions plainly (next-build.md, next-test.md), one build at a time (next.md). Wording has already drifted slightly between copies — the cost of duplication made visible. Trickle-up discipline: plugin-behaviour.md is the canonical home; skill docs carry only what's skill-specific. This extends the same bet as [behaviour-doc-double-load]: post-dedup, these rules live in the session-start injection alone — the consistent direction, not a new exposure. Locate every removal by rule text, not the capture's line refs — the docs have been edited since filing.

Build:
- plugin/si-plugin/docs/next-build.md: remove the SPEC read-only, don't-fix-outside-scope, and state-regressions-plainly restatements. Keep the section's skill-specific rules (scope-expansion ask, REGISTRY not build scope).
- plugin/si-plugin/docs/next-test.md: remove the SPEC read-only and state-regressions-plainly restatements.
- plugin/si-plugin/docs/next.md: remove the one-build-at-a-time restatement. Keep entries-are-the-contract and per-entry ticking.

Test:
- Grep the four rule phrasings across next.md and the per-type docs after the edit — remaining hits should be in plugin-behaviour.md only.

**Generalize ask-when-unsure into plugin-behaviour.md** **[trickle-up-ask-when-unsure]**

next.md's "Unsure about an implementation choice? Ask. Don't guess and build wrong" is universal — /plan ordering calls, /setup scaffolding choices, /done routing decisions — but lives only in next.md, so every other skill runs without it. Trickle-up: the generalized rule belongs in plugin-behaviour.md Communication, adjacent to the web-search bullet so the two read as one decision rule with two branches — uncertain about an external fact → offer a search; uncertain about a choice the user owns → ask, don't guess and proceed. One deliberate addition beyond the capture as filed: a self-contained line in setup.md, because unadopted sessions get no behaviour-rules injection (confirmed in session_start.py this session) and /setup's scaffolding choices are a named use of the rule — setup.md carries its own copies by design. Same next.md rules area as [trickle-up-next-md-duplicates] touches; no ordering between them, placed adjacent for one-session convenience.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md Communication, next to the web-search bullet: add the generalized rule — when uncertain about a choice the user owns (implementation, scaffolding, routing), ask; don't guess and proceed.
- plugin/si-plugin/docs/next.md: remove the local copy (locate by rule text, not line ref).
- plugin/si-plugin/docs/setup.md: add one self-contained ask-when-unsure line where scaffolding choices are made.

Test:
- Grep the rule phrasing after the edit: present in plugin-behaviour.md and setup.md, gone from next.md.

**Queue-visible plan markers: write predictable planning moments into the queue** **[queue-plan-markers]**

Claude keeps recommending "run /plan first" at moments that feel unexpected to the user, but a subset of those moments is predictable when the queue is authored — an audit batch will file findings the next batch depends on; a batch's dependencies can only be estimated after a design decision a planning session has yet to make. Writing those moments into the queue converts a judgment-based session-end recommendation into a mechanical gate (weak-model friendly, the same bet as the push marker), makes the planning rhythm visible before it's hit, and carries the reason inline. Floor, not ceiling: planning must happen here at minimum, for the stated reason; ad-hoc /plan elsewhere stays unrestricted. Part of the autopilot prerequisite arc named in the cruise-control trigger. The FAQ entry for the marker is deliberately not in this batch — it rides with the FAQ-trigger capture's routing.

Build:
- plugin/si-plugin/docs/plan.md Step 3 (ordering/placement work): add the authoring rule — when placement puts an audit batch ahead of batches that depend on its findings, or queues a batch whose dependencies wait on an undecided design question, insert "--- Plan session here: <reason> ---" between batches at that spot. Name the two cases as illustrations, not a closed list.
- plugin/si-plugin/docs/plan.md Step 1: when the marker sits at the queue top, addressing its stated reason is part of this session's work; remove the marker once addressed.
- plugin/si-plugin/docs/next.md pre-flight: halt on a plan marker at the queue top, sibling to the push-marker halt — tell the user a planning session is needed and name the marker's reason.
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md and this project's CLAUDE.md (QUEUE.md format descriptions): document the marker line so it's recognizable in consumer projects.
- plugin/si-plugin/templates/faq-template.md (+ index line): FAQ entry explaining the plan-marker line a consumer may meet in their queue — what it means, what to do (run /plan).

Test:
- Self-verifying from doc text. Behavioural confirmation arrives naturally: the next /plan that authors an audit batch with dependent work should insert a marker; the next /next that meets one should halt and name the reason.

**FAQ entries become part of batch authoring** **[faq-authoring-trigger]**

The FAQ ships as faq-template.md, authored in this project and scaffolded to consumers at /setup — yet nothing routinely updates it: entries happen only when a batch explicitly includes one (observed once, [narrate-build-md-purpose]), and the pre-push sweep drift-checks existing answers without ever asking whether new concepts lack coverage. This is the FAQ twin of the spec-entry trigger, keyed at the same prospective moment — batch authoring. It's a host-project rule, not shipped plan.md: consumers never author FAQ entries, so the rule would misfire in their /plan sessions. The push-sweep coverage backstop was considered and held — the observed failure is no-trigger-at-all, not a leaking trigger; the sweep is already heavy; ship the rule and watch, add the backstop only if entries still slip through. The existing backlog is [faq-coverage-audit]'s job; already-queued batches introducing consumer-visible concepts ([queue-plan-markers], [deferred-tests-structural-home]) got FAQ entries added at routing time.

Build:
- This project's CLAUDE.md (host-only, does not propagate), with the self-hosting conventions: add the rule — when /plan authors a batch that introduces something a consumer would see or ask about (a new queue line, a new doc section, a new narration moment), the batch carries a faq-template.md entry (plus its index line) in its build list. The test mirrors the spec-entry trigger: would a non-coder meeting this change have a question the FAQ doesn't answer?

Test:
- Self-verifying from the rule text. Behavioural: the next /plan authoring a consumer-visible batch should include the FAQ entry without prompting.

**One-time FAQ coverage audit against the current plugin** **[faq-coverage-audit]**

[faq-authoring-trigger] only fixes the future. The FAQ's 13 Q&A pairs date from its original authoring; concepts shipped since have never been coverage-checked — the pre-push sweep only checks existing answers for drift. One sweep catches the backlog; findings route to Captures per the audit contract.

Audit:
- Target: plugin/si-plugin/templates/faq-template.md and faq-index-template.md, read against the consumer-visible concept surface of the current procedure docs (setup.md, plan.md, the next and done families, plugin-behaviour.md) and the scaffolded doc formats.
- Criteria: every shipped concept a non-coder consumer would meet and ask about, checked for an answer; and the reverse gap — existing answers naming concepts that no longer ship. For each finding: the concept, why a non-coder would ask, and whether the entry is missing or stale.

**No planning work in execution skills** **[no-planning-in-execution]**

The boundary between /plan and the execution skills rode on "no thinking work," which was the wrong axis — Claude thinks plenty while executing, and the audit auto-file direction deliberately leans on Claude's thinking. The real boundary is planning work: processing captures — routing, promoting, parking, deciding their fate — and the human decision-making that entails. Capture-making stays open to every session type (the never-restrict-ideation principle); capture-processing is /plan's monopoly. Observed leak: [output-tag-audit] seeded a reconciliation item whose resolution was a planning decision made mid-/next, its reasoning landing where no planning session looks. Part of the autopilot prerequisite arc named in the cruise-control trigger: unattended next→done→next is only safe if no decision the user must own can arise mid-run. plan.md's thinking-work ground rule stays as the /plan-side gate on what gets queued ([audit-definition] is rewriting it); this rule is its execution-side counterpart, living where execution sessions actually load rules.

Build:
- plugin/si-plugin/docs/plugin-behaviour.md: add the rule, compliance-hardened from the start (why-clause, positive constraint, explicit scope, per resources/research/model-instruction-compliance.md): no planning work in any execution skill — planning work is processing captures (routing, promoting, parking, deciding their fate); making and approving captures is open to every session type; processing them happens only in /plan. Scope: all execution session types, including any added later. One clarifying line for test sessions: the user's involvement in running tests and judging outcomes is the work itself, not planning; filing those outcomes is capture-making.

Test:
- Self-verifying from the rule text. Behavioural: the next /next session that meets a routable discovery should append it to Captures and move on — no routing discussion mid-execution.

**Audit findings: one numbered set, bulk approval, contested items one at a time** **[audit-findings-bulk-approval]**

The per-finding capture-or-drop loop is the most interactive /next shape there is, and it duplicates /plan — every surviving finding judged twice. The original capture proposed removing approval entirely (mechanical auto-file); revised at routing: the [output-tag-audit] live preview validated bulk approval, not zero approval — findings 2–10 were batch-drafted and batch-approved in one pass, so the friction was the round-trips, and a session whose output the user never sees gives no reason to run it interactively. Bulk approval keeps the Captures always-show rule fully intact (no approval exemption needed — the caveat lands in the sequencing rule instead) and stays within [no-planning-in-execution]'s "making and approving captures." Full no-approval auto-file moves to cruise control's design scope: straight-to-Captures is autopilot behaviour. Double judgment still dies: one bulk ask in /next, full per-finding judgment once, in /plan. Absorbs the next-audit.md half of the [output-tag-audit] routing-loops tag finding — the new flow is authored with its tags correct from the start.

Build:
- plugin/si-plugin/docs/next-audit.md: replace the per-finding route-approved-findings loop with the bulk flow — compile all findings, present them as one numbered set in a single message, ask the user to approve the set or list the numbers they don't accept as-is, cover contested ones one at a time (reword or drop), append the approved set to Captures, report the filed count at close. Tag the bulk ask and the contested-item loop correctly from the start.
- plugin/si-plugin/docs/next-audit.md, same rewrite: the new close defines its review tail from birth — reviewing means re-examining what was already found, not raising new work; anything new routes through the existing paths (out-of-scope via scope management, thinking work via Captures). From a [close-out-audit] finding (e120f3d): the current "keep reviewing" tail is undefined, leaving open the new-work-smuggling risk next-build.md's tail was hardened against.
- plugin/si-plugin/docs/plugin-behaviour.md Communication, sequencing rule: add the bulk-approval inversion alongside the existing alternatives inversion, hardened (why-clause, positive constraint, explicit scope) — a deterministic result set produced by user-approved criteria is presented as one numbered message for bulk approval; the ask invites listing contested numbers; contested items then run one at a time. One-item-at-a-time stays the default everywhere else.
- plugin/si-plugin/docs/done-audit.md: the LOG entry records bulk-step outcomes — findings rejected or reworded at approval, with reasons — so nothing decided at audit time goes unrecorded.

Test:
- Self-verifying from doc text. Host-side behavioural (after push + reinstall): the next audit session presents one numbered set — [faq-coverage-audit] is queued as the natural first exercise. Needs the deferred-test discipline — flag at /done if it can't run.

**Tag application across the next and done families** **[next-done-tag-sweep]**

From [output-tag-audit], its headline finding. The procedure docs use response-shape tags to control when Claude speaks. In next-build.md and next-test.md, the whole Execute step — where Claude does the build work — is tagged [SILENT]. But that step contains moments that must speak: reporting a failure, asking before scope grows, handing a user-run test over. A literal-minded weak model gets two contradictory instructions at those moments. It either breaks the silence tag, or honours it by suppressing a failure report — the dangerous case. The fix has two parts. Each speaking moment gets its own tag, because a tag on the specific moment overrides the tag on the surrounding step. And Execute gets one clarifying line: silence covers routine bookkeeping when things go fine; failures, asks, and handoffs always speak. This was the only audit finding needing new wording — every other finding is plain tag placement. Sibling tag findings from the same audit fold into this batch as they route. Locate every edit by content, not by the audit's line numbers — the docs shift under other queued batches.

Build:
- plugin/si-plugin/docs/next-build.md and next-test.md, Execute step: add the clarifying line — silence governs success-path bookkeeping; failures, asks, and handoffs speak.
- Same two docs, inside Execute: tag the scope-expansion ask and the user-run test handoff [PROMPT]; tag failure noting [BRIEF].
- Same two docs, Scope management: tag the scope-growth asks [PROMPT]. In next-build.md, "Scope grows during the build" takes the tag at section level — both its paths ask and wait. In next-test.md, "Test surfaces unexpected scope" takes it on the minor-case ask only — the significant case notes for the queue and continues, so a section-level tag would force a wait that shouldn't happen. Restores symmetry with the already-tagged "User raises something out of scope" sibling.
- plugin/si-plugin/docs/next.md pre-flight: tag the push-marker halt [BRIEF]. Tag the blocker gate's surfacing moments [BRIEF]. Tag [PROMPT] where a user decision gates proceeding — the deferred-tests check and the capture-overlap recommendation. By the time this batch runs, [deferred-tests-structural-home] and [queue-plan-markers] may have reshaped this gate; tag the text as it stands then.
- done-build.md, done-test.md, done-audit.md: tag the route-to-Captures approval loops [PROMPT] — the close-out steps where leftover findings are drafted into Captures for the user's approval. The routing prose stays; only the tag is added. The matching next-audit.md loop is not in this batch — [audit-findings-bulk-approval] replaces it wholesale, tagged from birth.
- done.md and the three sub-docs, close-out moments: tag the unticked-entries ask (finish or close partial) [PROMPT] in done-build.md, done-test.md, done-audit.md. Give the staleness sweep in all three the path-split treatment next.md's pre-flight already models — [SILENT] when clean, [BRIEF] when flagging. Tag done.md's router [SILENT] to match its own "don't ask" prose. Tag the minor bookkeeping moments [SILENT]: the registry update in done-build.md, the _build.md deletion in all three.

Test:
- Self-verifying from doc text. Watch later /next sessions: failure reports and scope asks speak; success-path bookkeeping stays silent.

**Trim tag-definition restatements from plan.md** **[tag-restatement-trim]**

From [output-tag-audit]. Four spots in plan.md restate in prose what the response-shape tag definitions already say — "one item at a time" beside [SEQUENCE], "don't narrate the absence" beside [SILENT]. The audit flagged a tension: trimming prevents the copies drifting apart, but local restatement also props up weak models. Resolved at routing: the propping has already been paid for centrally — the hardened definitions carry their own why-clauses and constraints — so keeping the restatements buys the same insurance twice while leaving wording to drift. The line to apply: trim where the hardened definition fully covers the content; keep prose that adds step-specific substance. The audit also flagged next-audit.md's "Don't preview upcoming findings," but that line lives in the section [audit-findings-bulk-approval] replaces wholesale, so it dissolves on its own and stays out of this batch. setup.md is excluded entirely — its restatements are load-bearing because its sessions may never load the definitions (separate finding). Locate every spot by content, not the audit's line numbers.

Build:
- plugin/si-plugin/docs/plan.md, four restatement spots: the ground-rules "One item at a time" line, Step 2's one-at-a-time/never-preview restatement (keep the ordering content — candidates first, oldest first, count scope — it's step-specific), the gap-noticing "One at a time," and "don't narrate the absence" after the Test-section [SILENT]. Apply the line above to each. Treat the ground-rules spot with care: no tag sits on the ground rules or Step 1, so the line may be covering territory the [SEQUENCE] definition doesn't reach there — if so, it stays.

Test:
- Self-verifying from the doc text. Behavioural watch on later /plan sessions: one-at-a-time discipline holds without the trimmed prose; any leakage is a mandatory capture.

**Ship freeform: a fourth /next type for unqueued work** **[ship-freeform-next-type]**

Demand is observed, not speculative: twice in one day the work had no plugin path — an ad-hoc audit run with the plugin switched off, and a session that wanted captures surfaced without processing pressure — plus a general need for somewhere to discuss changes already made. Freeform is the fourth /next type for that work. Two forms ship together. Queue-driven: /plan scopes planned freeform work as a batch and /next picks it up. On-demand: `/next freeform` with no queued batch. Both pass the same gate first — could this be build, test, or audit? — with a one-line answer for why none fit; the gate runs in /plan for queue-driven and at session start for on-demand. Freeform is a refuge from ceremony, not from discipline. The scope lock holds, with files granted ask-by-ask by the user. Captures may be made but never processed — [no-planning-in-execution] already covers freeform through its written scope, no amendment needed. Freeform has no completion signal — nothing to tick — so it gets no Completion section: the session closes when the user runs /done, and the context-running-long nudge is the only close prompt Claude initiates. Expectation over time: recurring freeform shapes surface real new types, the way the audit type emerged. SPEC.md was updated at routing. Absorbs [freeform-on-demand]; both items leave Parked into this batch.

Build:
- plugin/si-plugin/docs/next.md router: add the freeform branch — a queued freeform batch at the top, or `/next freeform` with none. For on-demand, run the gate: ask whether the work could be build, test, or audit; require the one-line why-none-fit before proceeding.
- New doc plugin/si-plugin/docs/next-freeform.md: the procedure. Scope lock ask-by-ask — _build.md's Files list starts empty, and each file the work needs is requested and appended once the user grants it. The captures-append constraint: when the session yields captures, warn that /next can only append them, not process them, and offer the choice — move this to /plan now, or continue and process later. No Completion section. Authored with its response-shape tags correct from birth.
- plugin/si-plugin/docs/done.md router plus new done-freeform.md: record a freeform session — LOG entry describing what happened and what changed, registry check, commit. No batch to return, nothing to tick. Authored with tags from birth.
- plugin/si-plugin/docs/plan.md Step 3: the queue-driven shape — a Freeform subheading for planned freeform work, with the authoring-time gate (one line on why build, test, and audit don't fit).
- plugin/si-plugin/hooks/ lint hook (ships earlier in the queue): add Freeform to the allowed batch subheadings — its own batch notes this list must grow when new types ship.
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md: describe the freeform form in the workflow section.
- plugin/si-plugin/templates/faq-template.md (+ index line): FAQ entry — what a freeform session is, when to reach for it, and what it won't do (process captures).

Test:
- Self-verifying from the doc text for structure. Behavioural: the next real freeform need runs through `/next freeform` instead of switching the plugin off — the originally observed case is the natural live test. Host-side (after push + reinstall) — flag at /done if it can't run; needs the deferred-test discipline.

**Memory gets boundaries: enumerate what it must never hold, free the rest** **[memory-rule-boundaries]**

User direction, 2026-06-11. The route-observations rule's memory clause ("Not to memory, not discussed and dropped") is a blanket veto with no boundary, which makes it both too strong and too weak: it reads as forbidding memory entirely, while giving a weak model no list to check against. The tightened form enumerates what memory must never hold — project records that system docs own — and explicitly frees memory for everything else. Must-not-hold: behaviour observations and testing outcomes (Captures), design decisions and their reasoning (QUEUE, SPEC, LOG), project state and constraints (the method docs), procedure gaps noticed mid-session (Captures). Free: user preferences, working style, communication feedback, cross-project facts. Resolved at routing: consumers get their own version — their Claude has the same memory feature and a worse misroute risk, since memory is invisible to them, unversioned, and machine-local; a design decision saved there never reaches their project docs. Files over memory, in consumer clothes.

Build:
- This project's CLAUDE.md (host-only, does not propagate), the route-observations rule: replace the blanket "Not to memory" with the enumerated must-not-hold list and the explicit freed remainder, as above.
- plugin/si-plugin/docs/plugin-behaviour.md: add the consumer-facing version, compliance-hardened from the start (why-clause, positive constraint, explicit scope per resources/research/model-instruction-compliance.md) — project records belong in the project's docs, never in Claude's memory: ideas and discoveries to Captures, design decisions to QUEUE and SPEC, project state to the method docs. Memory stays free for what no project doc owns: user preferences, working style, communication feedback, cross-project facts. The why: memory doesn't travel with the project and the user can't read it; the method docs are the project's record.

Test:
- Self-verifying from the rule text. Behavioural watch: the next session where an observation or decision surfaces mid-work routes it to the docs, and memory use for preferences continues without hesitation.

**Close the overlap-scan gap in done-audit.md's recommendation** **[done-audit-overlap-scan]**

From a [close-out-audit] finding (e120f3d). done-audit.md is the only /done sub-doc whose recommendation step skips the unprocessed-Captures overlap scan. The default branch is unaffected — after findings route, the recommendation is already /plan. The gap bites when an audit routes nothing: in a project with pre-existing captures overlapping the top batch, the close recommends continuing into /next — the exact case the scan exists to catch. No exemption rationale exists, since an audit that routed nothing does nothing to clear pre-existing captures. The fix is one line, worded identically to the other three sub-docs so the rule reads the same everywhere it appears.

Build:
- plugin/si-plugin/docs/done-audit.md Phase 3, nothing-routed branch: open it with the overlap scan — "Before recommending, scan unprocessed Captures for overlap with the top batch — if found, recommend /plan first and name the overlap" — matching done-build.md, done-test.md, and done-plan.md verbatim.

Test:
- Self-verifying from the doc text. Grep the scan phrasing across the four /done sub-docs after the edit — expect four identical statements.

**State the single-summary rule in all four /done sub-docs** **[done-single-summary-line]**

From a [close-out-audit] finding (e120f3d). The single-summary rule is stated at five close-outs, but inside the /done sub-docs only done-plan.md carries it at the entry-writing step — done-build.md, done-test.md, and done-audit.md are silent on it. The pull the rule guards against lives exactly there: just after the commit, the natural move is to recap the session while recommending what's next, and a two-sentence recap satisfies the recommend-next [BRIEF] tag while still duplicating the entry. Grep-confirmed at routing: only done-plan.md has the line. The fix copies its exact wording so the rule reads identically everywhere it appears.

Build:
- plugin/si-plugin/docs/done-build.md, done-test.md, done-audit.md, entry-writing steps: add done-plan.md's line verbatim — "This entry is the session's summary — there is no separate chat recap." Locate each spot by content (the show-for-approval instruction in each entry step), not line numbers.

Test:
- Self-verifying. Grep "separate chat recap" across the /done sub-docs after the edit — expect four hits, identical wording.

**Fit the push offer to session shape and remote state** **[push-offer-fit]**

From a [close-out-audit] finding (e120f3d), plus one gap surfaced at routing. done.md's commit core asks "Commit and push, or just commit?" identically for every session shape. The dual ask fits build, test, and audit closes — work shipped or was verified, push is a real choice. It misfits planning closes: the staged paths are local planning state, so the standing offer treats planning work as a ship event. In the self-hosting host the cost is concrete — a push triggers the full push-and-rezip ritual off a commit that changed nothing in the plugin. A non-coder reads offered options as equally sensible defaults, so the ask teaches that pushing planning state is normal when the system reserves push for shipping. The routing-time gap: consumer repos may have no remote at all — nothing in setup or install creates one — so the ask can offer an option that errors when picked. The fix keeps the mechanics canonical in done.md and shapes the ask by context. The override is a default, not a prohibition — for consumers push is often just backup, and that stays available. Setup-shaped sessions inherit the override for free once [setup-closeout-redesign] routes them through done-plan.md.

Build:
- plugin/si-plugin/docs/done.md commit core: gate the push offer on a remote existing (one git remote check). No remote: ask about committing alone — don't offer what would error.
- plugin/si-plugin/docs/done.md commit core: add one line stating sub-docs may override the ask's default while the mechanics stay canonical here.
- plugin/si-plugin/docs/done-plan.md commit step: override the ask — planning sessions offer commit alone by default; push stays available when the user asks or is deliberately backing up. Carry the why: planning state is local bookkeeping, push is reserved for shipping, and in self-hosting projects a push triggers the full push-and-rezip ritual.

Test:
- Self-verifying from doc text. Behavioural, host-side (after push + reinstall): the next /done after a planning session asks commit-only; a /done after a build still offers the dual ask. Needs the deferred-test discipline — flag at /done if it can't run.

**Define next-test.md's completion review tail** **[next-test-review-tail]**

From a [close-out-audit] finding (e120f3d). The three /next-family completions share one shape — "Run /done to record this and commit, or X before closing" — but only next-build.md defines its X, and that definition exists deliberately to close a new-work-smuggling risk: an undefined tail can absorb fresh work past the batch's contract. next-test.md's "review what's already tested" carries no equivalent definition, so the same risk sits open there. The audit half of this finding rides in [audit-findings-bulk-approval], which rewrites next-audit.md's close; this batch covers the test half, mirroring next-build.md's wording so the rule reads the same in both places.

Build:
- plugin/si-plugin/docs/next-test.md Completion, after the "Run /done…" say-line: add the definition — reviewing means re-examining what was already tested, not raising new work; anything new routes through the existing paths (out-of-scope via Scope management, thinking work via Captures). Mirror next-build.md's tightening definition in structure and length.

Test:
- Self-verifying from the doc text. The two defined tails should read as the same rule in build and test clothing.

### Parked

## Captures

Captured outside /plan. Picked up and routed during the next /plan session. Processed captures (slug assigned, dependencies scanned) sit above the `---` divider; unprocessed raw captures collect below. See plan.md Capture and parking discipline.

---

- Deferred test from [next-pre-scope-lock-abort]. The new pre-scope-lock close needs live confirmation. At the next real /next that ends before a build is locked (push-marker halt, blocker-gate stop, or the user calling it off at "Ready?"), Claude should route any reshape direction to Captures and name /done — not /plan. This can't be confirmed in the build session itself: the new text only governs live sessions after push + reinstall, and the trigger is an abort that happens naturally. When [deferred-tests-structural-home] builds the Deferred tests section, this test belongs in its seed list alongside the two v1.10.0 tests.
  Blocked by: [next-pre-scope-lock-abort] shipping host-side (push + reinstall); fires at the next naturally-occurring pre-scope-lock end after that.

### Parked

- **[narration-vs-menu-drift]** Observed during 1b7d359 /plan: Claude defaulted to menu-style options ("file as capture, drop it, or commit to the rule now?") when narrating a recommendation would have been more appropriate. Dependency ownership's narration rule ("narrate the ordering work" — exercise judgment, recommend) is supposed to catch this. The mechanism failed under exploratory back-and-forth tone — the pull toward "lay out the options" was stronger than the pull toward "state the recommendation, let user push back." Worth watching whether this generalizes: when the conversation gets exploratory, does Claude soften from recommendation-narration into menu-listing? If so, the narration rule needs tightening — possibly explicit text that menu-style enumeration of equally-weighted options is *not* narration when Claude actually has a preference, and the recommendation must come first with the menu as fallback.
  Blocked by: a second observed instance of menu-style enumeration where a recommendation was due — behavioural trigger, no slug; fires at the /plan that processes such a capture.

- **[parked]** Decide whether to add an inline marker for internal-only terms in procedure prose. The marker would let procedure docs flag internal terms inline so the translate-or-omit rule fires mechanically rather than relying on Claude matching against the vocabulary list each time.
  Blocked by: [narration-vocabulary] + observed leakage after it ships

- **[user-execution-batch-shape]** When the user is the executor of a batch (gather these receipts, identify the lender, call the ATO) rather than Claude, the existing build/test/audit shapes don't quite fit. Build batches assume Claude executes; test batches are about verification; audit batches are read-and-route. A user-execution batch sits closest to a test batch in mechanics (user runs steps, Claude facilitates), but it's not verification — it's the primary work. Observed during /setup on a tax-prep folder: queueing batches that were mostly user-action items felt weird, even though step-by-step communication rules in plugin-behaviour.md would handle the running well. Three possible landings: (a) new `User:` subheading alongside Build/Test/Audit, (b) covered by existing types + freeform once shipped, (c) framing-only — "build" means "user does it" in non-coder projects, no new structure. Decision premature without running several user-execution batches first.
  Blocked by: experience from 2–3 user-execution batches run in the tax project — external behavioural trigger, no slug; fires when that experience reaches a /plan session here.

- Add scenarios to reader-test-workflow.js — evaluate which scenarios are still undertested and worth adding. Known blind spots regardless of refresh outcome: /setup interview (untested), push-and-rezip sweep (untested — lives in this project's CLAUDE.md, not plugin docs, so coverage question is whether it should even be in scope for plugin reader-tests), mid-build resume from a real _build.md (current next.md sim covers fresh /next, not resume), /done plan-mode close-out (current sim only covers build close-out), empty-queue handling, audit-batch flow (planning-as-work). Promote as one or more build batches once scenarios are picked.
  Blocked by: [reader-test-refresh] + refreshed workflow run once — the refreshed first run may surface blind spots not on this list, or may show that scenario count matters less than scenario specificity.

- Cruise control skill — a skill that runs build→commit→build→commit through a batch (or multiple batches) unattended, stopping only when it hits something requiring user input. Key design concerns: (1) wording that doesn't pressure Claude to push through uncertainty, (2) dependency management when Claude decides when to wrap a batch, (3) /done judgment steps can't get skipped for speed.
  Blocked by: the autopilot prerequisite arc shipping — the no-planning-in-execution rule ([no-planning-in-execution]), queue-visible plan markers ([queue-plan-markers]), and audit bulk approval ([audit-findings-bulk-approval]); fires when those have shipped and an unattended next→done→next run is plausible. Full no-approval auto-file of audit findings is in this item's own design scope — interactive audits keep bulk approval. Named as the end-goal in the thinking-work capture, 2026-06-10.

- **[self-hosting-support-during-setup]** Self-hosting support during /setup — if the user says they're rebuilding SI with SI (or building any Claude Code plugin with the plugin), scaffold the self-hosting workflow into their CLAUDE.md: push-and-rezip steps, host/target distinction, pre-push consistency sweep, version bumping, **and the dependency-management discipline** (host-vs-target distinction as it governs batch ordering, the host-side-after-push-marker rule, the `--- Push required before continuing ---` queue convention, and the `(host-side)` annotation on `Depends on:`). All of this carries into the new project's CLAUDE.md. Could be an additional /setup question ("Are you building a Claude Code plugin?" → yes triggers self-hosting scaffolding).
  Blocked by: a second self-hosting consumer appearing — a user reports building a plugin (or any project that ships itself) with the plugin, or Alex starts one; external behavioural trigger, no slug. The scoping decision (interview question vs skill vs template) waits for that real case to design against.

- **[done-spec-sync-check]** /done spec check at build close — when the session being closed was a /next build (not test or audit), /done reads SPEC.md against the just-landed changes and applies the spec-entry trigger test (post-[spec-entry-trigger-rethink] form: would these changes make SPEC.md's description wrong or incomplete?). If yes, /done files a mandatory capture naming the gap — it never edits SPEC.md directly; product-truth edits stay in /plan. Decided 2026-06-10: detect-and-file wins over sync-in-/done, keeping SPEC authorship in /plan while making the backstop mechanical. Evidence the backstop is needed: the prospective /plan gate leaked at [tag-definitions-compliance-rewrite] — no spec entry preceded the build, and the gap was caught only because the /done session noticed by judgment and filed a capture. This makes that lucky catch structural: prospective gate at /plan, mechanical detect-and-file at /done.
  Blocked by: [spec-entry-trigger-rethink] — the /done check applies the rewritten trigger wording, so it can't be authored until that wording has shipped.

- Threshold-based context management — if hooks ever gain token usage fields (e.g. `context_usage_pct`), the plugin could recommend `/compact` or `/clear` based on actual utilization instead of rule-based triggers. Research filed at resources/research/context-window-hook-access.md.
  Blocked by: Anthropic adding token data to hook event input — external trigger, no slug.
