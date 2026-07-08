# Data Acquisition

Use this procedure to create a current, auditable evidence base from an ASIN or Amazon URL.

## 1. Input Resolution

Run `scripts/parse_amazon_input.py`.

Supported forms include:

- bare ASIN: `B0XXXXXXXX`;
- `/dp/<ASIN>`;
- `/gp/product/<ASIN>`;
- `/gp/aw/d/<ASIN>`;
- `/product-reviews/<ASIN>`;
- legacy `/exec/obidos/ASIN/<ASIN>`;
- URL query parameter `asin=<ASIN>`.

For a short URL such as `amzn.to`, follow the redirect with an available browser and parse the final URL. Never infer the ASIN from a shortened token.

For a bare ASIN, default to Amazon.com unless the user names another marketplace. The report must say that the marketplace was assumed.

## 2. Research Order

Use a strict two-pass sequence.

### Pass A: Objective Baseline

Inspect only the first Amazon main image, expected to be the white-background product image.

Freeze the product baseline before reading the title or any other page content. Current offer facts may be recorded separately, but must not influence the first-image product reconstruction.

### Pass B: Seller Narrative and Corroboration

Then inspect:

- the complete title;
- all secondary images;
- bullets, A+, description, specification tables, comparison charts;
- image text and lifestyle scenes;
- reviews and Q&A;
- independent manuals, certifications, tests, and comparable products.

Use `references/evidence-policy.md` to classify all evidence.

## 3. Source Priority

Prefer sources in this order:

1. Independent certification, regulator, test, or model-specific technical source.
2. Directly visible product structure and current Amazon offer facts.
3. Customer evidence with a stated sample method.
4. Seller-authored Amazon content and official brand claims.
5. Public retailer, distributor, search snippet, or third-party catalog.

This priority depends on the claim. Amazon is authoritative for what the current listing displays, but not automatically authoritative for whether the seller's performance or material claim is true.

Do not use inaccessible paid estimates from Keepa, Helium 10, Jungle Scout, Brand Analytics, or Seller Central unless the user provides access or exports. Never imply access to private seller metrics.

## 4. Target Product Capture

Capture as many of these fields as the public evidence supports:

| Group | Fields |
|---|---|
| Identity | ASIN, marketplace, canonical URL, title, brand, model |
| Offer | displayed price, coupon, deal, pack size, variation, availability |
| Social proof | rating, review count, visible recent review dates |
| Classification | category, subcategory, BSR, badges, only when visible |
| Seller narrative | bullets, description, A+ modules, comparison table, image text |
| Claimed product data | dimensions, weight, material, power, compatibility, included items |
| Commercial | seller, fulfillment, warranty, returns statements |
| First-image baseline | physical form, visible components, countable items, assembly relationship |
| Seller visual narrative | secondary images, accessories, scale claims, usage scenes, packaging |
| Claims | certifications, performance claims, audience and use-case claims |

Record the observation date because price, badges, review counts, sellers, and inventory change.

If a variation family is present, identify which child variation the page currently displays. Do not silently mix price, review, image, or specification data from different children.

For every product-data field, label it `visible`, `seller-claimed`, `externally corroborated`, `customer-reported`, or `unknown`.

## 5. Image and Claim Inspection

Inspect listing images in page order.

- Use image 1 only for the frozen objective baseline.
- Use image 2 onward to analyze seller expression, information architecture, use-scene positioning, and claims.

Use all secondary-image content as seller-authored evidence. A graphic saying "waterproof" proves only that the listing makes the claim.

Check consistency across title, bullets, images, A+, and specifications. Flag contradictions that can cause customer confusion or semantic drift.

## 6. Review Evidence

When reviews are accessible, sample recent and critical reviews rather than relying only on the star average.

Capture:

- repeated purchase reasons;
- praised features;
- repeated defects or return triggers;
- expectation gaps;
- size, fit, compatibility, durability, packaging, and instructions issues;
- whether a theme is frequent or only anecdotal.

Do not state prevalence unless the review sample supports it. Use wording such as `在可见样本中重复出现` and state the sample limitation.

## 7. Comparable Product Scan

When browsing permits, collect three to five close comparables using the target's core physical identity and primary use case.

A valid comparable should overlap in:

- product form and main job;
- target customer or use scene;
- expected price band;
- important specifications.

Avoid treating a substitute with a different physical form as a direct competitor. Put such products in a separate `替代品` group.

For each comparable, capture only visible facts:

| Field | Requirement |
|---|---|
| Product/ASIN | exact identifier or link |
| Price | current displayed price with observation date |
| Rating/reviews | current visible values |
| Positioning | one concise summary based on title/listing |
| Differentiator | evidence-backed |
| Relevance | direct comparable or substitute |

Do not claim category-wide market share or price distribution from a tiny sample.

## 8. Search and Keyword Evidence

Use exact-ASIN search to find corroborating pages. Use product-identity queries to understand public language and close competitors.

Public search results can support:

- common naming patterns;
- competing identity language;
- visible product alternatives;
- ambiguous or drifting terminology.

Public search results cannot prove:

- Amazon search volume;
- CPC;
- conversion rate;
- keyword rank history;
- sales volume;
- organic versus paid traffic share.

Without seller or specialist datasets, describe keywords as semantic intent candidates and label demand estimates qualitative.

## 9. Evidence Ledger

Maintain a compact ledger while researching:

| ID | Source | Evidence | Class | Date | Notes |
|---|---|---|---|---|---|
| S1 | URL | Main image shows two physical ports | Visible fact | YYYY-MM-DD | Target child |
| S2 | URL | Bullet claims IPX6 | Seller claim | YYYY-MM-DD | Unverified |
| S3 | URL | Certification record | External corroboration | YYYY-MM-DD | Same model |

Do not use the undifferentiated label `fact` for seller-authored specifications. The fact is that the seller made the statement; the product property remains unverified.

## 10. Access Failure and Degraded Mode

If the detail page is blocked or unavailable:

1. Search the exact ASIN.
2. Open cached public snippets or official brand sources when available.
3. Look for manuals, specification sheets, and retailer pages tied to the same model.
4. Analyze accessible images only if their provenance is clear.
5. Mark the report `受限分析`.

In degraded mode:

- omit or mark unknown all live commercial facts that cannot be verified;
- lower confidence;
- do not assign a precise operating stage from appearance alone;
- provide a list of data needed for a full report.
