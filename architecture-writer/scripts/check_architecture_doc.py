#!/usr/bin/env python3
"""
Lightweight architecture document checker.

Usage:
    python scripts/check_architecture_doc.py ARCHITECTURE.md
    python scripts/check_architecture_doc.py docs/architecture/my-initiative-architecture.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT_REQUIRED = [
    "Purpose",
    "Architecture Summary",
    "Scope",
    "Component",
    "Data",
    "Runtime",
    "Integration",
    "Consistency",
    "Security",
    "Architectural Decisions",
    "Implementation Rules",
    "Open",
]

INITIATIVE_REQUIRED = [
    "Document Status",
    "Related Artifacts",
    "Problem Context",
    "Target Architecture",
    "Scope",
    "Component",
    "Data",
    "Runtime",
    "Integration",
    "Transaction",
    "Security",
    "ADRs",
    "Implementation Rules",
    "Open",
]


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def has_heading_like(text: str, phrase: str) -> bool:
    pattern = re.compile(r"^#{1,4}\s+.*" + re.escape(phrase.lower()), re.MULTILINE)
    return bool(pattern.search(text.lower()))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to architecture markdown file")
    parser.add_argument(
        "--initiative",
        action="store_true",
        help="Validate as initiative architecture instead of root architecture",
    )
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"ERROR: file does not exist: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    normalized = normalize(text)

    is_initiative = args.initiative or "docs/architecture/" in str(path).replace("\\", "/")
    required = INITIATIVE_REQUIRED if is_initiative else ROOT_REQUIRED

    missing = []
    for phrase in required:
        if not has_heading_like(text, phrase) and phrase.lower() not in normalized:
            missing.append(phrase)

    if missing:
        print("Architecture document check: WARN")
        print("Missing or unclear expected sections:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("Architecture document check: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
