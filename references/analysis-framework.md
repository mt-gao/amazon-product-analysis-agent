# Analysis Framework

This framework consolidates the legacy four-module method into one non-repetitive report. All scores run from 0 to 100 unless stated otherwise. A higher score is always better, except for explicitly named risk metrics such as `Drift Risk`.

## 0. Reader-Facing Translation

Use the formulas to keep analysis consistent, not to make the reader decode the report.

For every optional score, present information in this order:

1. The business question it answers.
2. A plain-language result.
3. The evidence and uncertainty.
4. The recommended action.
5. The formula only in a methodology appendix when useful.

Default reader-facing grades:

| Score | Plain-language grade | Default action |
|---|---|---|
| 80-100 | 高度匹配 | 优先使用或重点验证 |
| 65-79 | 基本匹配 | 受控使用 |
| 50-64 | 匹配有限 | 小范围测试 |
| Below 50 | 不匹配或风险高 | 避免或否定 |

Do not expose component acronyms in the default report. Spell out the Chinese meaning if a component is necessary.

## 1. Evidence Confidence

Score report confidence from evidence completeness:

| Evidence block | Weight |
|---|---:|
| First-main-image reconstruction | 20 |
| Independent capability corroboration | 25 |
| Reviews or customer evidence | 15 |
| Comparable-product evidence | 15 |
| Seller-narrative capture and claim audit | 15 |
| Historical, advertising, or seller data | 10 |

For each block, apply:

- `1.0`: adequate and direct;
- `0.5`: partial or indirect;
- `0.0`: unavailable.

`Confidence = sum(weight x completeness factor)`

Use these labels:

- 85-100: high;
- 70-84: medium-high;
- 50-69: medium;
- 30-49: low;
- below 30: very low.

Confidence measures evidence coverage, not certainty that the strategy will succeed. A complete set of seller-authored content cannot substitute for independent corroboration.

## 2. Product Success Variables

Identify four to eight product variables grounded in visible physical structure, externally corroborated capabilities, or clearly qualified customer evidence.

Score each variable on:

| Dimension | Meaning |
|---|---|
| Positioning clarity | Helps customers and Amazon understand the product identity |
| Price support | Justifies the current or intended price |
| Traffic relevance | Connects naturally to valid purchase intent |
| Risk resilience | Resists defects, confusion, compliance risk, and easy copying |
| Lifecycle durability | Retains value beyond a short trend or season |
| Asset compounding | Can build reviews, brand memory, repeat purchase, ecosystem, or IP |

`Variable Score = arithmetic mean of the six dimensions`

Classification:

- 85-100: strategic core variable;
- 70-84: primary operating variable;
- 55-69: supporting variable;
- below 55: weak or risk variable.

Do not let seller claims alone raise these scores. If a variable depends on a title, bullet, A+, specification table, image label, brand claim, unknown cost, patent, certification, or failure rate, mark it unverified and exclude it from product-capability scoring until corroborated.

Also identify:

- must-have variables whose absence breaks the product promise;
- performance variables that improve CTR or CVR plausibly;
- premium/stretch variables that can support a higher price band;
- conflicts, such as strong visual attraction versus weak expectation accuracy;
- lifecycle threats: replacement, homogenization, price compression, structural obsolescence.

Inventory and cash-flow advice requires cost, lead time, sales velocity, seasonality, return rate, and available cash. Without them, provide only conditional guidance.

## 3. Real Positioning and Traffic Identity

Define:

- one Chinese positioning sentence;
- one English positioning sentence;
- core identity;
- what the product is and is not;
- physical identity;
- one primary customer problem;
- one primary scene and secondary scenes;
- prohibited scenes or expectation boundaries;
- direct substitutes.

Create two separate scores:

### Objective Identity Stability

| Component | Weight |
|---|---:|
| Physical boundary clarity | 40% |
| Primary-job clarity from first-image structure | 25% |
| Use plausibility from first-image physical form | 15% |
| External corroboration | 20% |

### Listing Communication Stability

| Component | Weight |
|---|---:|
| Identity consistency across listing elements | 30% |
| Claim-to-proof alignment | 25% |
| Primary-scene consistency | 20% |
| Customer expectation consistency | 15% |
| Variation consistency | 10% |

Never average the two into one score. A polished listing can communicate a weak or unverified product very well.

Build keyword groups:

- `Core Identity`: exact product identity and job;
- `Structural`: material, form, compatibility, mechanism;
- `Scene`: valid usage contexts;
- `Expansion`: adjacent but still accurate intent;
- `Seasonal/Emotional`: time-limited gift or event intent;
- `Negative Filters`: physically incompatible or expectation-breaking intent.

Treat references to Amazon systems, semantic models, or shopping assistants as practical listing-readability heuristics. Do not claim knowledge of proprietary ranking logic.

## 4. Traffic Driver Strategy

Evaluate five possible drivers:

1. Problem driven.
2. Feature driven.
3. Aesthetic driven.
4. Gift/emotional driven.
5. Hobby/identity driven.

For each driver, score the product opportunity:

- product match: 35%;
- public demand evidence: 20%;
- differentiation: 20%;
- conversion support: 15%;
- durability or repeatability: 10%;
- subtract `0.25 x driver risk`.

`Driver Score = clamp(0, 100, weighted positives - risk penalty)`

Use seller content only to identify the driver's intended narrative. It cannot establish product match, differentiation, conversion support, or durability by itself. When demand evidence is absent, label that component as heuristic and do not present the result as measured traffic potential.

Select:

- one primary long-term driver;
- one or two expansion drivers;
- optional seasonal driver;
- the identity-drift boundary.

Do not recommend arbitrary budget percentages as universal facts. If no advertising data exists, express allocations as starting hypotheses with monitoring conditions.

## 5. Current Operating Situation

This section answers two different questions. Keep them separate in the reader-facing report:

1. `市场需求现在是在上升还是下降？`
2. `Listing、关键词和用户认知是否指向同一种商品身份？`

Separate two concepts:

### Temporal Momentum (TM)

Chinese reader-facing name: `市场时间动量`. It estimates demand direction from historical sales, BSR, seasonality, search, or advertising evidence.

Public or supplied evidence of current demand momentum:

- 0.70-0.84: declining or off-season;
- 0.85-0.94: weak;
- 0.95-1.05: neutral;
- 1.06-1.15: rising;
- 1.16-1.30: strong or peak.

When no seasonality, trend, BSR history, sales, or advertising evidence exists:

- report `市场趋势：无法判断`;
- do not display `TM = 1.00`;
- do not multiply an unknown value into a stage index.

### Semantic Momentum (SM)

Chinese reader-facing name: `商品身份收敛度`. It estimates whether the listing, keywords, variations, reviews, and traffic evidence point to one clear product identity.

Evidence that listing identity and traffic are converging:

- 0.70-0.84: severe confusion or drift;
- 0.85-0.94: weak identity;
- 0.95-1.05: forming or neutral;
- 1.06-1.15: reinforced;
- 1.16-1.30: strongly established.

Without search-query, ad, ranking, or review evidence, infer this only from listing consistency and label it low confidence.

`Stage Index = TM x SM`

Interpretation:

- below 0.80: defensive correction;
- 0.80-0.94: validation or repair;
- 0.95-1.10: stable build;
- 1.11-1.30: controlled expansion;
- above 1.30: harvest or overheating risk.

Calculate and display the Stage Index only when both TM and SM have adequate evidence. Otherwise give a qualitative operating recommendation:

- market trend unknown + identity weak: `先修复定位和目录，再谈扩量`;
- market trend unknown + identity clear: `维持核心词，等待经营数据验证`;
- market rising + identity weak: `先防止流量浪费`;
- market rising + identity clear: `可受控扩张`.

Never infer a sales lifecycle stage solely because a listing looks new or polished.

## 6. Keyword Product-Fit Score (KIMS)

Reader-facing name: `关键词与商品匹配度`. It answers: `这个词带来的买家，看到商品后会不会觉得货对版？`

KIMS ranks semantic fit, not search volume, CPC, rank, conversion rate, or sales potential.

Use the following components internally:

- IMS, intent match: 35%;
- VSS, first-main-image support: 25%;
- PAS, price and purchase support: 20%;
- SFS, stage fit: 10%;
- EC, evidence confidence: 10%;
- DRP, drift risk penalty: subtract 30% of DRP.

`KIMS = clamp(0, 100, 0.35*IMS + 0.25*VSS + 0.20*PAS + 0.10*SFS + 0.10*EC - 0.30*DRP)`

Seller keyword usage and secondary images can reveal a market narrative, but they must not raise VSS. Only the first Amazon main image can support VSS; unknown properties remain unknown.

Classification:

- 80-100: core defend or primary test;
- 65-79: controlled secondary;
- 50-64: small-budget test;
- below 50: negative or avoid unless stronger data changes the decision.

Do not add a TM x SM multiplier to KIMS. Stage changes the tactic, not the semantic truth of a keyword.

Default reader-facing table:

| 关键词 | 匹配等级 | 为什么 | 建议动作 | 主要风险 |
|---|---|---|---|---|
| example | 高度匹配 | 商品形态和购买意图一致 | 核心使用 | 无 |

Put the numeric KIMS score in an optional `方法与评分附录`. Do not show IMS, VSS, PAS, SFS, EC, or DRP unless the user explicitly requests calculation details.

## 7. Competitor-Keyword Safety Filter (CKAF)

Reader-facing name: `竞品词借用安全度`. It answers: `借用这个竞品或替代品相关词，会带来相符买家，还是带来错误预期？`

Use CKAF internally for competitor or substitute terms:

- physical fit: 40%;
- user-intent overlap: 30%;
- visual-expectation overlap: 15%;
- price/position overlap: 15%;
- subtract `0.30 x drift risk`.

`CKAF = clamp(0, 100, weighted overlap - risk penalty)`

Decision:

- 75-100: `建议采用`;
- 60-74: `加护栏使用`;
- 45-59: `小范围测试`;
- below 45: `不建议`.

For `Guardrails`, specify:

- anchor term;
- negative shield;
- stage gate;
- budget or click stop condition.

Default reader-facing table:

| 竞品 / 替代词 | 是否建议使用 | 原因 | 使用边界 |
|---|---|---|---|
| example | 加护栏使用 | 核心需求相似，但产品形态不同 | 限定场景并添加否定词 |

Put the numeric CKAF score and formula in the optional methodology appendix.

## 8. Scenario Funnel

A 1,000-impression model is allowed only as a scenario:

`Clicks = impressions x assumed CTR`

`Orders = clicks x assumed CVR`

State every assumption and provide a sensitivity range. Do not call scenario values actual performance or forecasted sales.

## 9. Claim Audit

For every major seller claim, classify:

- `supported and communicated well`;
- `plausible but unproven`;
- `contradicted by another listing element or customer evidence`;
- `irrelevant or distracting`;
- `high-risk claim requiring test, certification, or legal review`.

Use this audit for listing recommendations, not as a substitute for product validation.

## 10. Decision Rules

Recommendations must be conditional on evidence:

- Public listing only: reconstruct the objective baseline from the first main image, then separately analyze the title, secondary images, listing clarity, unproven claims, review risks, and semantic keyword architecture.
- Listing plus competitor scan: add relative price and feature positioning.
- Listing plus review corpus: add prioritized customer pain points.
- Listing plus seller data: add stage, advertising, inventory, and cash-flow decisions.
- Listing plus historical tools: add trend and lifecycle analysis, with source attribution.

Use P0, P1, and P2:

- P0: fix factual errors, expectation gaps, compliance risks, severe defects, or identity drift.
- P1: improve conversion support, differentiation, and controlled traffic expansion.
- P2: build defensible product, brand, content, or ecosystem assets.
