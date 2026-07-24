# Comparison Accuracy Audit and Lovable Video Plan

## Purpose

This document defines the proposed work for improving the honesty, accuracy, and maintainability of the Sovereign Implementer comparison resource.

It is intended for review on the Claude side before implementation begins.

The project has two immediate goals:

1. Improve the comparison website so that each platform is represented fairly, consistently, and with current evidence.
2. Produce the first YouTube script for the Gambit App Studio channel, focused on Lovable for a non-coder audience.

This is a planning document only. It does not yet contain the completed platform research or the final Lovable narration.

---

## Important Product Update

The former **Cruise** workflow has been retired.

`/next` now runs autonomously by default, so all future documentation, comparison material, and maintenance instructions should treat `/next` as the autonomous execution workflow.

No new Codex port or comparison content should preserve Cruise as a current user-facing feature.

---

# Workstream 1: Audit the Existing Comparison Resource

## 1.1 Review the current site structure

Inspect:

- The main `/compare` page.
- Every full platform breakdown page.
- The current Lovable comparison page.
- The existing maintenance guide.
- Any shared data files, templates, schemas, or content components used to generate comparison rows.
- Any claims duplicated across multiple pages.

The purpose is to determine:

- Which statements are global.
- Which statements are platform-specific.
- Which claims are manually maintained.
- Which claims can drift apart across pages.
- Which wording rules should be encoded into the maintenance process.

## 1.2 Identify structural bias

Look for cases where Sovereign Implementer is favoured through wording rather than evidence.

Examples include:

- `Yes` versus `Complete`.
- `Yes` versus `Full`.
- `Low` versus wording that implies near-zero risk.
- Describing a competitor cost as a disadvantage while omitting the required Claude or Codex subscription for Sovereign Implementer.
- Describing ordinary local-code ownership as unusually absolute.
- Treating platform limitations as permanent lock-in when export or migration is genuinely available.
- Comparing the competitor's full product cost with only the free Sovereign Implementer plugin rather than the complete required toolchain.
- Giving Sovereign Implementer credit for capabilities that come from Claude Code, Codex, Git, the terminal, the selected framework, or the hosting provider.

The audit should distinguish between:

1. Sovereign Implementer's own capabilities.
2. Capabilities supplied by the underlying AI coding agent.
3. Capabilities supplied by normal developer tooling.
4. Capabilities supplied by the generated application's stack.
5. Capabilities supplied by external hosting, database, authentication, or deployment providers.

---

# Workstream 2: Define Comparison Honesty Rules

## 2.1 Equivalent row meaning on `/compare`

Every row on the main comparison page must measure the same thing across all platforms.

A row must not silently change meaning from one column to another.

For example:

- If the row is **Code ownership**, every cell should describe who owns the generated code.
- It should not describe code ownership for one platform and local file custody for another.
- If the row is **Self-hosting**, every cell should describe whether the generated application can be self-hosted.
- It should not compare application hosting in one column with whether the builder itself can be self-hosted in another.

Each row should have:

- A canonical definition.
- A defined scope.
- A defined evidence requirement.
- A controlled answer format.
- A clear distinction between the short table answer and the full explanation.

## 2.2 Equivalent column meaning on full breakdown pages

Every full breakdown page must preserve the same structure:

1. What the competitor provides.
2. What Sovereign Implementer provides.
3. Important qualifications for both.
4. Evidence and date checked.

The competitor and Sovereign Implementer cells must answer the same question at the same level of abstraction.

The comparison must not use:

- Product-level benefits for one side and ecosystem-level drawbacks for the other.
- Best-case usage for Sovereign Implementer and default usage for the competitor.
- Beginner experience for one side and expert experience for the other.
- Current published limits for the competitor and hypothetical future flexibility for Sovereign Implementer.

## 2.3 Controlled answer vocabulary

Where a row uses categorical answers, both columns should use the same vocabulary.

Examples:

- `Yes / Partial / No`
- `Low / Medium / High`
- `Included / Additional cost / Usage-based`
- `Local / Exportable / Platform-hosted`
- `Beginner / Intermediate / Advanced`

Avoid asymmetric intensifiers such as:

- Complete
- Full
- Absolute
- Total
- True
- Native
- Unlimited
- Permanent
- Entirely
- Fully sovereign

These terms should only appear when they describe a specifically defined capability and are supported by evidence.

A plain `Yes` should remain a plain `Yes`. The explanation should carry the nuance.

## 2.4 Total-cost honesty

All cost comparisons must include the complete minimum usable setup.

For Sovereign Implementer, that may include:

- Claude Code or Codex access.
- The relevant Claude, ChatGPT, or API subscription.
- Usage limits or overage exposure.
- Hosting.
- Database services.
- Domain registration.
- Email, authentication, storage, analytics, or other external services where required.
- Any paid developer tool that is genuinely necessary.

For a competitor, include:

- Required subscription tier.
- Included credits.
- Overage or upgrade rules.
- Hosting costs.
- Database or backend costs.
- Export restrictions.
- Required third-party services.

Do not compare:

- A competitor's paid production plan with Sovereign Implementer's free repository.
- A competitor's complete hosted product with only Sovereign Implementer's instruction layer.
- A competitor's expected beginner workflow with an unusually frugal expert-managed Sovereign Implementer workflow.

Every cost row should state what is included and excluded.

## 2.5 Capability attribution

Every claim must be attributed to the correct layer.

Use the following categories:

### Sovereign Implementer method

Examples:

- Project state documents.
- Queue discipline.
- Scope controls.
- Session records.
- Planning and execution method.
- Autonomous `/next` behaviour.
- Maintenance and handoff conventions.

### AI coding agent

Examples:

- Code generation.
- Debugging ability.
- Context handling.
- Model reasoning quality.
- Tool use.
- Image or browser capabilities.
- Agentic execution.

### Local development environment

Examples:

- File ownership.
- Git history.
- Terminal access.
- Ability to inspect or edit source files.
- Choice of editor.

### Application stack

Examples:

- React, Next.js, TypeScript, Python, or another framework.
- Database portability.
- Authentication implementation.
- Test coverage.
- Hosting compatibility.

### External provider

Examples:

- Supabase.
- Vercel.
- Netlify.
- Cloudflare.
- Stripe.
- Firebase.
- Managed databases.
- Email providers.

A benefit should not be credited to Sovereign Implementer when it would be equally true of using Claude Code or Codex without Sovereign Implementer.

## 2.6 Symmetrical qualification

When one side receives a caveat, assess whether the other side needs the equivalent caveat.

Examples:

- If Lovable's builder interface is a vendor dependency, Claude Code or Codex is also a build-time vendor dependency.
- If Lovable's hosting creates operational dependence, self-hosting through Sovereign Implementer creates operational responsibility.
- If Lovable has credit limits, Claude and Codex subscriptions also have usage limits, rate limits, or plan constraints.
- If exported Lovable code can become difficult for a novice to maintain, locally generated Sovereign Implementer code may also be difficult for a novice to maintain without an AI agent.
- If platform closure could remove Lovable's editing experience, changes to Claude Code, Codex, model availability, subscriptions, or APIs could affect the Sovereign Implementer workflow.

This does not require pretending the risks are identical. It requires examining equivalent risks on both sides.

## 2.7 Separate factual claims from judgments

Each comparison entry should distinguish between:

### Fact

Example:

> Lovable supports GitHub synchronisation.

### Interpretation

Example:

> This reduces code lock-in.

### Judgment

Example:

> The remaining lock-in risk is low-to-medium.

Judgments should be traceable to stated criteria.

Terms such as `low`, `medium`, and `high` must have definitions in the maintenance guide.

## 2.8 Avoid hypothetical superiority

Do not award Sovereign Implementer a benefit because a capable developer could theoretically configure it.

Only claim the capability when:

- It is part of the documented workflow.
- It is usable by the intended audience.
- It has been tested.
- The required setup is disclosed.
- The user can reasonably reach the outcome without hidden expert intervention.

Similarly, do not penalise competitors based only on hypothetical worst cases.

## 2.9 Audience honesty

The resource is intended for non-coders and novice builders.

Every row should therefore consider:

- Whether a true beginner can perform the task.
- Whether the platform performs the task automatically.
- Whether the user needs terminal knowledge.
- Whether the user needs Git knowledge.
- Whether the user needs to understand hosting, databases, environment variables, authentication, security, or deployment.
- Whether the user can recover from failures.
- Whether documentation and support are suitable for beginners.

A capability is not meaningfully available to a non-coder merely because it is technically possible.

## 2.10 Evidence and freshness

Every material claim should have:

- A source.
- A date checked.
- A source type.
- A confidence level where evidence is incomplete.

Preferred evidence order:

1. Official documentation.
2. Official pricing pages.
3. Official terms or licensing pages.
4. Official product announcements.
5. Reputable independent testing.
6. Documented user examples.
7. Community reports, clearly labelled as anecdotal.

Marketing claims should not be treated as verified user outcomes without corroboration.

Each platform should be rechecked fortnightly using the maintenance workflow.

---

# Workstream 3: Rewrite the Maintenance Method

The old Claude maintenance guide should be updated so that each fortnightly review includes the following.

## 3.1 Platform-by-platform source check

For each platform:

- Check pricing.
- Check included usage or credits.
- Check export rules.
- Check ownership terms.
- Check hosting and self-hosting options.
- Check database portability.
- Check supported integrations.
- Check plan restrictions.
- Check whether the product is still available.
- Check whether the target audience or positioning has changed.
- Check whether novice workflows have materially improved or worsened.

## 3.2 Claim ledger

Maintain a structured record for every comparison claim:

- Claim ID.
- Platform.
- Row ID.
- Short answer.
- Full explanation.
- Source.
- Source date.
- Last checked date.
- Evidence type.
- Confidence.
- Notes.
- Whether the claim applies to the builder, generated app, hosting, or external services.

This should become the source of truth for both `/compare` and the full breakdown pages.

## 3.3 Automated consistency checks

Add checks that flag:

- Different categorical vocabularies in the same row.
- Missing evidence.
- Expired review dates.
- Unsupported superlatives.
- Different row definitions across pages.
- Claims copied from one platform to another without validation.
- Sovereign Implementer claims that actually describe Claude Code, Codex, Git, or local development.
- Cost comparisons that omit required subscriptions.
- Full page wording that contradicts the summary table.
- References to the retired Cruise workflow.

## 3.4 Human review questions

Before publishing an update, ask:

1. Are both platforms being judged at the same level?
2. Are both platforms being judged for the same audience?
3. Are minimum required costs included on both sides?
4. Does each categorical answer use the same vocabulary?
5. Has any ordinary developer-tool capability been misattributed to Sovereign Implementer?
6. Is any competitor disadvantage exaggerated?
7. Is any Sovereign Implementer disadvantage hidden in explanatory text?
8. Does the row describe what a novice can realistically do?
9. Is the evidence current?
10. Would a representative of the compared platform consider the description recognisable and fair?

---

# Workstream 4: Lovable Page Accuracy Audit

## 4.1 Opening positioning

Review and replace statements such as:

> The trade you make for that smoothness is a monthly credit bill and a builder you don't control.

Problems to address:

- Sovereign Implementer also requires access to Claude Code or Codex.
- The competitor's recurring cost should not be presented as unique.
- The builder interface and the generated application's code should be discussed separately.
- `Don't control` is too broad if the user can export or synchronise code.
- The actual trade-off is likely a combination of convenience, abstraction, recurring service dependence, and reduced control over the builder experience.

The replacement should state both sides' dependencies clearly.

## 4.2 Review every table row

For each row:

1. Define the exact question.
2. Verify Lovable's current factual position.
3. Verify Sovereign Implementer's current factual position.
4. Remove asymmetric adjectives.
5. Add equivalent caveats.
6. Confirm cost assumptions.
7. Confirm whether the claim concerns the builder or the generated application.
8. Rewrite the short cells.
9. Rewrite the full explanations.
10. Record sources and dates.

## 4.3 Correct likely misconceptions in the Gemini narration

The Gemini output demonstrates several areas that require verification or correction before it can become a script.

Examples:

- The learning-time claims may be invented or unsupported.
- Lovable pricing and included credits may be outdated or oversimplified.
- Private GitHub access requirements need verification.
- Database portability may depend on the exact Lovable/Supabase setup.
- Copyright analysis is jurisdiction-dependent and should not be reduced to a single warning applied only to Sovereign Implementer.
- `Low-to-medium` and `low` lock-in judgments need defined criteria.
- Lovable hosting should not automatically be described as being `stuck`.
- Sovereign Implementer is not necessarily locked specifically to Claude Code once the Codex version exists.
- Self-hosting the generated application is different from self-hosting the builder.
- Sovereign Implementer does not itself supply a server, database, security operations, or uptime management.
- AI subscriptions and APIs should not be described as charging for `words`; pricing is normally based on tokens, plans, requests, or credits depending on the provider.
- Runtime independence and build-time dependence should be assessed symmetrically.

The final script should not reuse this narration without row-by-row verification.

---

# Workstream 5: Lovable YouTube Script

## 5.1 Intended channel context

Channel:

- Gambit App Studio

Playlist:

- Non-coder platform comparisons

First video:

- Lovable compared with Sovereign Implementer

Audience:

- People with little or no coding knowledge.
- People evaluating whether they can build and maintain an application.
- Viewers who need technical terms explained without being patronised.
- Viewers who should understand both convenience and responsibility.

## 5.2 Script structure

The final script should include:

1. A neutral introduction.
2. A clear explanation of what Lovable is.
3. A clear explanation of what Sovereign Implementer is.
4. A disclosure that Sovereign Implementer depends on Claude Code or Codex.
5. A row-by-row walkthrough.
6. The competitor cell first.
7. The Sovereign Implementer cell second.
8. Plain-English definitions of technical terms and acronyms.
9. Equivalent caveats for both sides.
10. A conclusion explaining who each option may suit.

## 5.3 Narration rules

The script should:

- Explain rather than sell.
- Avoid winner language unless the row has an explicit, defensible criterion.
- Avoid treating local development as inherently superior.
- Avoid treating managed services as inherently inferior.
- State when an outcome depends on the user's technical skill.
- State when an outcome depends on the AI model.
- Explain builder lock-in separately from application lock-in.
- Explain convenience separately from ownership.
- Explain ownership separately from copyright.
- Explain code export separately from maintainability.
- Explain hosting separately from builder access.
- Explain subscription costs on both sides.
- Define acronyms on first use.
- Avoid unsupported time estimates.
- Avoid unsupported claims about what `most users` do.

## 5.4 Script deliverables

Produce:

- A full narration script.
- A shorter on-screen version of each row.
- Suggested visual callouts.
- A source list for the video description.
- A correction log showing where the original comparison wording changed.
- A list of claims that remain uncertain or need direct testing.

---

# Workstream 6: Non-Coder Suitability Audit

## 6.1 Review all providers listed on `/compare`

For each provider, assess whether it genuinely belongs in a non-coder comparison.

Use evidence rather than product branding alone.

Questions:

- Does the provider explicitly target non-coders?
- Can a novice begin without installing developer tools?
- Can a novice publish a working app?
- Can a novice make later changes?
- Can a novice recover from build failures?
- Is coding knowledge optional, helpful, or effectively required?
- Are real non-coder case studies available?
- Are independent user reports available?
- Does the platform's normal workflow match the way the comparison describes it?
- Is the platform actually a coding agent being stretched into a no-code category?

## 6.2 Evidence required for inclusion

A provider should have at least two of the following:

- Official non-coder positioning.
- A documented beginner workflow.
- Public examples from self-described non-coders.
- Independent reviews showing non-coder use.
- Tutorials intended for non-technical users.
- Evidence of successful deployment without prior coding knowledge.

Where evidence is weak, mark the provider as:

- `Non-coder focused`
- `Non-coder accessible with limitations`
- `Technical tool sometimes used by non-coders`
- `Not genuinely a non-coder platform`

The page should not advertise a use case merely because it is theoretically possible.

## 6.3 Likely stretch categories to inspect carefully

Without completing the live audit yet, the following categories deserve particular scrutiny:

- General-purpose AI coding agents.
- IDE-first coding assistants.
- Terminal-first agents.
- Framework generators that still require local setup.
- Open-source app builders requiring self-hosting.
- Tools whose onboarding assumes Git, package managers, environment variables, or cloud configuration.
- Tools that generate code but do not provide a beginner-safe maintenance workflow.

The final assessment must be based on the actual providers currently listed on `/compare`.

---

# Final Deliverables

The completed project should produce:

1. An audit of the current `/compare` page.
2. An audit of every full breakdown page.
3. A canonical row-definition document.
4. A comparison honesty and accuracy standard.
5. A rewritten fortnightly maintenance guide.
6. A claim ledger or structured source-of-truth format.
7. Automated consistency checks.
8. A fully corrected Lovable breakdown.
9. A Lovable YouTube narration script.
10. A visual and source plan for the Lovable video.
11. A non-coder suitability assessment for every listed provider.
12. A list of providers that should be removed, relabelled, or supported with stronger evidence.
13. Removal of all current Cruise references in favour of autonomous `/next`.

---

# Recommended Order of Execution

1. Pull the current project from Alex's computer.
2. Read the existing comparison data and maintenance guide.
3. Inventory every row and provider.
4. Define canonical row meanings.
5. Write and approve the honesty rules.
6. Build the claim ledger.
7. Audit Lovable first.
8. Correct the Lovable page.
9. Write the Lovable video script.
10. Audit non-coder evidence for all providers.
11. Update the remaining platform pages.
12. Add consistency checks.
13. Run a final fairness review across all columns and pages.

---

# Review Questions for Claude

Claude should review this plan and comment on:

- Whether any important source of bias is missing.
- Whether the proposed row-equivalence rules are enforceable.
- Whether the capability-attribution model is sufficiently clear.
- Whether the claim ledger should be Markdown, YAML, JSON, or another format.
- Which checks can be automated reliably.
- Which checks still require editorial judgment.
- Whether the YouTube script and website should share one canonical explanation source.
- How to generate short comparison cells and long narration from the same evidence without producing repetitive or promotional wording.
- How the maintenance method should detect changes in Claude, Codex, Lovable, and other provider pricing or capabilities.
