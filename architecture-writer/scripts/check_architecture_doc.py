#!/usr/bin/env python3
"""Lightweight architecture document validator.

Checks for architecture structure and the normalized Concrete Next Step block.
This script is intentionally conservative: it reports warnings/errors but does
not try to prove architecture quality.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_NEXT_STEP_FIELDS = [
    "next_step_type",
    "target",
    "action",
    "why_this_is_next",
    "blocking_condition",
    "suggested_prompt",
]

VAGUE_NEXT_STEP_VALUES = [
    "continue development",
    "proceed",
    "proceed as needed",
    "next phase",
    "review is done",
    "implementation can continue",
    "implement it",
    "fix issues",
]

RECOMMENDED_ARCHITECTURE_SECTIONS = [
    "Purpose",
    "Architecture Summary",
    "Scope",
    "System Context",
    "Boundaries",
    "Data",
    "Runtime",
    "Integration",
    "Architecture Handoff Summary",
    "Concrete Next Step",
]


def extract_section(text: str, title: str) -> str | None:
    pattern = rf"^##\s+{re.escape(title)}\s*$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match:
        return None
    start = match.end()
    next_heading = re.search(r"^##\s+", text[start:], flags=re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(text)
    return text[start:end].strip()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_architecture_doc.py <path-to-architecture-doc-or-output>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: file does not exist: {path}")
        return 2

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    if "## Concrete Next Step" not in text:
        errors.append("Missing required section: ## Concrete Next Step")
    else:
        section = extract_section(text, "Concrete Next Step") or ""
        for field in REQUIRED_NEXT_STEP_FIELDS:
            if f"`{field}`" not in section:
                errors.append(f"Missing Concrete Next Step field: `{field}`")

        lowered = section.lower()
        for vague in VAGUE_NEXT_STEP_VALUES:
            if vague in lowered:
                warnings.append(f"Concrete Next Step may be vague: {vague!r}")

    if "## Architecture Handoff Summary" not in text:
        warnings.append("Missing recommended section: ## Architecture Handoff Summary")

    for section_name in RECOMMENDED_ARCHITECTURE_SECTIONS:
        if section_name not in text:
            warnings.append(f"Recommended architecture concept not found: {section_name}")

    if errors:
        print("FAILED")
        for error in errors:
            print(f"ERROR: {error}")
    else:
        print("PASSED")

    for warning in warnings:
        print(f"WARNING: {warning}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
