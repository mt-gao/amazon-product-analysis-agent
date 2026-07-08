#!/usr/bin/env python3
"""Normalize a bare ASIN or Amazon product URL without network access."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from urllib.parse import parse_qs, urlparse


ASIN_RE = re.compile(r"^[A-Z0-9]{10}$", re.IGNORECASE)
PATH_PATTERNS = (
    re.compile(r"/(?:dp|gp/product|gp/aw/d|product-reviews)/([A-Z0-9]{10})(?:[/?]|$)", re.IGNORECASE),
    re.compile(r"/exec/obidos/ASIN/([A-Z0-9]{10})(?:[/?]|$)", re.IGNORECASE),
)

DOMAIN_MARKETPLACES = {
    "amazon.com": "US",
    "amazon.ca": "CA",
    "amazon.com.mx": "MX",
    "amazon.com.br": "BR",
    "amazon.co.uk": "UK",
    "amazon.de": "DE",
    "amazon.fr": "FR",
    "amazon.it": "IT",
    "amazon.es": "ES",
    "amazon.nl": "NL",
    "amazon.se": "SE",
    "amazon.pl": "PL",
    "amazon.com.be": "BE",
    "amazon.co.jp": "JP",
    "amazon.in": "IN",
    "amazon.com.au": "AU",
    "amazon.sg": "SG",
    "amazon.ae": "AE",
    "amazon.sa": "SA",
    "amazon.com.tr": "TR",
}

SHORT_DOMAINS = {"amzn.to", "a.co"}


def normalize_domain(value: str) -> str:
    domain = value.strip().lower()
    if "://" in domain:
        domain = urlparse(domain).hostname or domain
    domain = domain.split(":", 1)[0]
    for prefix in ("www.", "smile.", "m."):
        if domain.startswith(prefix):
            domain = domain[len(prefix) :]
    return domain


def find_amazon_domain(hostname: str) -> str | None:
    host = normalize_domain(hostname)
    for domain in sorted(DOMAIN_MARKETPLACES, key=len, reverse=True):
        if host == domain or host.endswith("." + domain):
            return domain
    return None


def extract_asin(parsed_url) -> str | None:
    for pattern in PATH_PATTERNS:
        match = pattern.search(parsed_url.path)
        if match:
            return match.group(1).upper()

    query = parse_qs(parsed_url.query)
    for key in ("asin", "ASIN"):
        for value in query.get(key, []):
            candidate = value.strip().upper()
            if ASIN_RE.fullmatch(candidate):
                return candidate
    return None


def parse_input(raw_value: str, default_domain: str) -> dict:
    raw = raw_value.strip()
    default_domain = normalize_domain(default_domain)
    if default_domain not in DOMAIN_MARKETPLACES:
        raise ValueError(f"Unsupported default marketplace domain: {default_domain}")

    if ASIN_RE.fullmatch(raw):
        asin = raw.upper()
        domain = default_domain
        return build_result(
            raw=raw,
            input_type="asin",
            asin=asin,
            domain=domain,
            marketplace_assumed=True,
        )

    candidate_url = raw if "://" in raw else "https://" + raw
    parsed = urlparse(candidate_url)
    host = normalize_domain(parsed.hostname or "")

    if host in SHORT_DOMAINS:
        return {
            "ok": False,
            "input": raw,
            "input_type": "short_url",
            "needs_redirect_resolution": True,
            "message": "Open the short URL, capture its final Amazon URL, and parse that URL again.",
        }

    domain = find_amazon_domain(host)
    if not domain:
        return {
            "ok": False,
            "input": raw,
            "input_type": "unknown",
            "needs_redirect_resolution": False,
            "message": "Input is neither a 10-character ASIN nor a supported Amazon URL.",
        }

    asin = extract_asin(parsed)
    if not asin:
        return {
            "ok": False,
            "input": raw,
            "input_type": "amazon_url_without_asin",
            "domain": domain,
            "marketplace": DOMAIN_MARKETPLACES[domain],
            "needs_redirect_resolution": False,
            "message": "Amazon URL recognized, but no ASIN was found in the path or query string.",
        }

    return build_result(
        raw=raw,
        input_type="amazon_url",
        asin=asin,
        domain=domain,
        marketplace_assumed=False,
    )


def build_result(
    *,
    raw: str,
    input_type: str,
    asin: str,
    domain: str,
    marketplace_assumed: bool,
) -> dict:
    canonical_url = f"https://www.{domain}/dp/{asin}"
    return {
        "ok": True,
        "input": raw,
        "input_type": input_type,
        "asin": asin,
        "domain": domain,
        "marketplace": DOMAIN_MARKETPLACES[domain],
        "marketplace_assumed": marketplace_assumed,
        "canonical_url": canonical_url,
        "suggested_filename": f"{asin}-amazon-product-analysis-{date.today().isoformat()}.md",
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Normalize a bare ASIN or Amazon product URL."
    )
    parser.add_argument("value", help="ASIN or Amazon product URL")
    parser.add_argument(
        "--marketplace",
        default="amazon.com",
        help="Default Amazon domain for a bare ASIN, e.g. amazon.com or amazon.de",
    )
    args = parser.parse_args()

    try:
        result = parse_input(args.value, args.marketplace)
    except ValueError as exc:
        result = {"ok": False, "input": args.value, "message": str(exc)}

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("ok") else 2


if __name__ == "__main__":
    sys.exit(main())
