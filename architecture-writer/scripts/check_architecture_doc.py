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

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from workflow_contracts import phase_next_step_types, validate_concrete_next_step

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

    errors.extend(
        validate_concrete_next_step(
            text,
            allowed_next_step_types=phase_next_step_types("architecture-writer"),
        )
    )

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
