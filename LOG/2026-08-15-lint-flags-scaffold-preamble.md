# b4de5bf — /setup's queue scaffold writes its section preambles as blockquotes, so the lint stops firing on them

Reported by another project running this plugin: the queue structure lint fired two advisory flags on every PostToolUse invocation — every Bash call, every Edit — saying the prose under `## Processed` and under `## Unprocessed` belongs to no work item.

Checked against the mechanism rather than taken on the report's word. `_check_orphaned_prose` in `post_tool_use.py` exempts any line beginning `>`, and its docstring says why: /setup scaffolds each section's description as a blockquote, positionally identical to a destroyed first item's stranded rationale, so form discriminates where position cannot. But `setup.md`'s scaffold wrote both preambles as plain paragraphs. The exemption and the scaffold disagreed, so every project the shipped /setup created tripped the check forever. The hook was already correct; this build makes the scaffold match the hook rather than the reverse.

It matters past the noise for the reporter's own reason: the flag's text warns that a destroyed heading leaves rationale orphaned exactly like this, which is the corruption the hand-move fallback exists to catch. Firing on every tool call trains sessions to skim past it, so a genuine overwritten heading arrives looking identical to the two that are always there.

The wider fix — exempting all prose between a section heading and its first item — was refused at processing. It repairs every existing project at once with no migration, which is a real advantage, but it widens the hole the check guards: a first item whose heading is destroyed leaves its rationale in precisely that position. The user chose the narrow fix, which keeps the teeth against the expensive case.

The residual is accepted rather than solved: a project already adopted, which never migrates again, keeps emitting both flags until someone edits its QUEUE.md by hand. Any project that migrates for any reason picks the new form up for free, because the migration checklist already refreshes method-shipped boilerplate from the current template — checked rather than assumed, so no step was added there. No format-epoch bump: those files are noisy, not structurally wrong, and bumping would halt every consumer on a migration prompt over two advisory warnings.

A reply to the reporting project was drafted this session and could not be sent: the message names no sending project, which is the defect `[outbound-message-has-no-sender]` fixed in this same run, and neither the address book nor the user could identify the sender. The draft is held rather than guessed at a recipient. Its substance: the fix, the refused wider alternative and why, the one-line hand repair for an already-adopted project, and the reason no epoch bump was made.

Rule gate: not needed — this changes a scaffold's formatting, and authors no method rule.

FAQ: not needed because the scaffold's wording is unchanged and nothing a user does changes; what stops is two advisory lines they were never asked to act on.

**Files touched:** `plugin/throughliner/docs-b/setup.md`.

**Routed to Captures:** none.
