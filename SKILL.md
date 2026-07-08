---
name: amazon-product-analysis-agent
description: Agent-portable workflow for analyzing an Amazon product from an ASIN or Amazon product URL and producing an evidence-backed Chinese Markdown report.
---

# Amazon Product Analysis Agent Workflow

This directory is a portable analysis workflow, not a Codex-only skill.
Any agent can use it if it can:

- read the files in this directory;
- run Python 3 scripts, or manually perform their equivalent logic;
- browse public web pages or receive page captures from the user;
- write or return a Markdown report.

The workflow turns one ASIN or Amazon product URL into an evidence-based Chinese Markdown report. The core rule is: reconstruct the product from the first Amazon main image before evaluating the seller's marketing narrative. Treat the title, all secondary images, bullets, A+ content, image text, and specifications as seller-authored expression until independently supported.

## How To Use This Workflow In Any Agent

1. Paste or attach this whole directory to the agent.
2. Tell the agent: "Follow `SKILL.md` exactly. Read all required references before analysis."
3. Provide one Amazon ASIN, Amazon product URL, review URL, or short Amazon link.
4. Allow the agent to browse public pages, or provide screenshots/page exports if browsing is unavailable.
5. Ask for the final report in Chinese Markdown unless another language is needed.

This workflow does not require Codex-specific skill loading, `$skill` syntax, MCP tools, or a fixed workspace layout.

## Required Files

Before analyzing a product, the agent must read these files completely:

1. `references/evidence-policy.md`
2. `references/data-acquisition.md`
3. `references/analysis-framework.md`
4. `references/report-template.md`

The helper script is optional but recommended:

```bash
python scripts/parse_amazon_input.py "<ASIN-or-URL>"
```

If Python is unavailable, the agent may manually extract the ASIN and marketplace using the rules in `references/data-acquisition.md`.

## Reader-First Output Rules

Assume the reader is an Amazon operator or product manager, not an analyst.

- Lead with a three-minute summary: what it is, whether it is worth acting on, top risks, and next actions.
- Explain the business question before any score.
- Do not use an acronym in a heading unless the same heading contains its Chinese meaning.
- On first use, write the Chinese name plus the English name and acronym, then explain it in one sentence.
- Keep formulas and component scores in an optional methodology appendix.
- Never expose internal component acronyms such as `IMS`, `VSS`, `PAS`, `SFS`, `EC`, or `DRP` in the default report.
- Treat KIMS, CKAF, TM, and SM as optional analytical tools, not mandatory report sections. Include them only when they change a decision.
- If historical demand data is absent, write `市场趋势无法判断`; do not display a neutral-looking placeholder number.
- Translate operating labels. Use `建议采用 / 加护栏使用 / 小范围测试 / 不建议` instead of `Adopt / Guardrails / Test / Reject`.
- Every scored section must end with `这对经营意味着什么`.

## Workflow

### 1. Normalize The Input

Run:

```bash
python scripts/parse_amazon_input.py "<ASIN-or-URL>"
```

Use the returned ASIN, marketplace, canonical URL, and suggested filename.

- Infer the marketplace from a full Amazon URL.
- For a bare ASIN, default to `amazon.com` unless the user states another marketplace. Mark this as an assumption in the report.
- For `amzn.to` or another short link, open it, capture the final Amazon URL, then run the parser again.
- If the input cannot resolve to one ASIN, explain the issue and request a valid ASIN or product URL.

### 2. Select The Analysis Mode

Infer the mode from the user's request:

- `competitor-entry`: analyze a competitor or decide whether and how to enter the market.
- `owned-listing-audit`: analyze the user's own ASIN or whether its listing communicates the product well.
- `dual`: use when ownership or intent is unclear. Keep market opportunity and listing quality as separate conclusions.

State the selected mode in the report. Do not require clarification when `dual` can answer safely.

### 3. Run The Objective First Pass

Before reading the title, secondary images, bullets, A+ content, description, comparison tables, specifications, or promotional text:

1. Inspect only the first Amazon main image, expected to be the white-background product image.
2. Record the visible product form, components, countable included items, assembly relationship, possible primary job, ambiguity, and unknowns.
3. Freeze this baseline in notes before reading any seller-authored content.

Do not use the title to repair or enrich the first-image interpretation. If the first image does not reveal a property, record it as unknown. Follow the claim firewall in `references/evidence-policy.md`.

### 4. Acquire And Quarantine Current Evidence

Use available web search or browser tools because Amazon listing content, price, ratings, reviews, and competitors are live data.

After freezing the objective baseline, read the remaining product page and search the exact ASIN and product identity for corroboration and a small competitor set. Follow `references/data-acquisition.md`.

Record:

- observation date and marketplace;
- title, brand, displayed price and coupon, rating and review count;
- category or BSR only when visible;
- seller-authored bullets, description, A+ claims, image text, specifications, variations, seller, and fulfillment;
- image-supported structure, accessories, use scenes, packaging, and claim consistency;
- review themes when accessible;
- three to five close public comparables when enough evidence is available.

Do not merge seller claims into the objective baseline. Use them to evaluate positioning, persuasion, completeness, consistency, and claim risk. Seek independent corroboration for claims that affect product scoring.

Do not bypass login, CAPTCHA, bot protection, paywalls, or access controls. If Amazon blocks access, use public search results, manuals, certifications, and other accessible sources. Label the report `受限分析` when evidence remains incomplete.

### 5. Build An Evidence Ledger

Classify every important claim:

- `可见事实`: physically or transactionally observable, with source.
- `卖家声明`: seller-authored title, bullet, A+ content, specification, image text, or brand-page claim.
- `外部佐证`: independently corroborated manual, certification, test, or authoritative specification.
- `用户反馈`: review or forum report; useful but anecdotal unless sampled systematically.
- `推断`: derived from evidence; explain the reasoning.
- `未知`: not supported or conflicting.

Assign source IDs such as `[S1]`, `[S2]`, and cite numeric or time-sensitive facts inline. Phrase seller content as `页面声称...`, not `产品具备...`, until corroborated.

### 6. Apply The Analysis Framework

Use `references/analysis-framework.md` to analyze:

1. product success variables and operating decision;
2. real positioning and traffic identity;
3. traffic-driver strategy and identity drift;
4. operating stage and keyword strategy.

Keep all scores reproducible. Show component values or formulas only where they help the reader trust a decision. Do not invent search volume, CPC, sales, conversion rate, BSR history, inventory, margin, or advertising performance.

Product capability, differentiation, premium support, safety, durability, and risk-resilience scores may use only visible facts, external corroboration, and clearly labeled customer evidence. Seller claims alone may be scored only under listing communication and claim quality.

When only public listing data exists:

- call keyword work a semantic and intent strategy, not measured demand;
- write `市场趋势无法判断` when historical demand data is unavailable;
- treat listing-identity status as a confidence-rated inference, separate from market momentum;
- make the 1,000-impression funnel a scenario model, not a forecast;
- avoid firm inventory, cash-flow, or launch-budget prescriptions.

### 7. Write One Markdown Report

Follow `references/report-template.md`. Default to Chinese unless the user requests another language.

Use the template as a maximum structure, not a requirement to expose every analytical model. Remove optional score tables that do not improve the user's decision.

Write the report to the user-specified path. Otherwise create or return:

```text
outputs/<ASIN>-amazon-product-analysis-<YYYY-MM-DD>.md
```

If the agent cannot write files, return the complete Markdown report in the conversation.

## Quality Gate

Before delivery, verify:

- The ASIN and marketplace are correct.
- The analysis mode is explicit.
- The objective first pass uses only the first Amazon main image and is visibly separated from seller narrative.
- Seller-authored claims never appear as verified product facts without corroboration.
- The title and all secondary images are evaluated only after the first-image baseline is frozen.
- Live facts include an observation date and citations.
- No inaccessible metric is presented as fact.
- Score directions and formulas are consistent.
- The first two sections can be understood without reading a formula.
- Every acronym is expanded and explained on first use.
- Internal component acronyms are absent from the default report.
- Missing historical data is labeled `无法判断`, not represented by a neutral placeholder score.
- KIMS, CKAF, TM, and SM appear only when they materially change a recommendation; otherwise omit them.
- Each optional score is followed by a plain-language business interpretation.
- Competitors are genuinely comparable, not merely high-traffic substitutes.
- Keyword recommendations distinguish core, expansion, seasonal, test, and negative intent.
- Recommendations match the inferred stage and evidence strength.
- The report contains concrete P0, P1, and P2 actions.
- Unknowns and the data needed to resolve them are explicit.
- No template placeholders remain.
