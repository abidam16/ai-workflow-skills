#!/usr/bin/python3
"""Lightweight PRD document checker for the prd-writer skill.

Usage:
    python scripts/check_prd_doc.py PRD.md

The checker is intentionally simple. It catches missing handoff/next-step fields and common vague next-step wording.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "## 14. Architecture Impact",
    "## 15. ADR Impact",
    "## 16. Roadmap Impact",
    "## 17. Implementation Plan Readiness",
    "## 19. PRD Handoff Summary",
    "## Concrete Next Step",
]

REQUIRED_NEXT_FIELDS = [
    "`next_step_type`",
    "`target`",
    "`action`",
    "`why_this_is_next`",
    "`blocking_condition`",
    "`suggested_prompt`",
]

ALLOWED_NEXT_TYPES = {
    "CREATE_OR_UPDATE_ARCHITECTURE",
    "CREATE_OR_UPDATE_ADR",
    "CREATE_OR_UPDATE_ROADMAP",
    "CREATE_OR_UPDATE_PLAN",
    "RETURN_TO_BRAINSTORM",
    "REQUEST_PRODUCT_DECISION",
    "REQUEST_MISSING_SOURCE_ARTIFACT",
    "REVISE_PRD",
    "START_IMPLEMENTATION",
    "RETURN_TO_REVIEW",
    "STOP_AND_ESCALATE",
}

VAGUE_PHRASES = [
    "continue development",
    "proceed as needed",
    "review later",
    "update docs",
    "implement the feature",
    "next phase",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_prd_doc.py <PRD.md>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: File not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"Missing required section: {section}")

    for field in REQUIRED_NEXT_FIELDS:
        if field not in text:
            errors.append(f"Missing required next-step field: {field}")

    type_match = re.search(r"`next_step_type`\s*:\s*([A-Z_]+)", text)
    if type_match and type_match.group(1) not in ALLOWED_NEXT_TYPES:
        errors.append(f"Invalid next_step_type: {type_match.group(1)}")

    lowered = text.lower()
    for phrase in VAGUE_PHRASES:
        if phrase in lowered:
            errors.append(f"Vague next-step wording detected: {phrase!r}")

    if errors:
        print("PRD check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PRD check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
