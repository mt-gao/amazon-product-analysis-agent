# Amazon Product Analysis Agent

Portable instructions for analyzing an Amazon product from an ASIN or product URL.

This repository is designed for any capable agent, not only Codex. It contains:

- `SKILL.md`: the main agent workflow;
- `references/`: evidence rules, data acquisition rules, analysis framework, and report template;
- `scripts/parse_amazon_input.py`: a small helper that normalizes ASINs and Amazon URLs;
- `agents/openai.yaml`: an optional OpenAI-style prompt profile.

## Quick Start

Give an agent this whole directory and prompt it with:

```text
Follow SKILL.md exactly. Read all required references first. Analyze this Amazon product: <ASIN-or-URL>
```

If Python is available, normalize the input first:

```bash
python scripts/parse_amazon_input.py "B0XXXXXXXX"
```

The expected output is a Chinese Markdown report with:

- a three-minute business summary;
- an objective first-main-image reconstruction;
- a separated seller-claim audit;
- evidence labels and source IDs;
- positioning, keyword, competitor, risk, and action recommendations.

## Core Principle

The listing title, bullets, A+ content, specifications, and secondary images are seller-authored claims. They should not become product truth unless supported by visible facts, independent corroboration, or clearly labeled customer evidence.

## Minimum Agent Capabilities

- Read Markdown files.
- Run Python 3, or manually extract ASIN and marketplace.
- Browse public web pages, or accept user-provided screenshots/page exports.
- Write or return Markdown.

## Repository Status

This is the agent-portable edition converted from a local Codex skill.
