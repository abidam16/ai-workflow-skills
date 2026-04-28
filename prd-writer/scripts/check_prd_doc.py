#!/usr/bin/env python3
"""Lightweight PRD document checker for the prd-writer skill.

Usage:
    python scripts/check_prd_doc.py PRD.md

The checker is intentionally simple. It catches missing handoff/next-step
fields, old terminal contract labels, invalid PRD next_step_type values, and
common vague next-step wording.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from workflow_contracts import phase_next_step_types, validate_concrete_next_step

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

OLD_TERMINAL_LABELS = [
    "Immediate Next Step",
    "Continuation Prompt",
    "Recommended Follow-up",
    "Recommended Follow Up",
]

VAGUE_PHRASES = [
    "continue development",
    "proceed as needed",
    "proceed to next phase",
    "review later",
    "update docs",
    "implement the feature",
    "next phase",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_prd_doc.py <path-to-prd-or-prd-output.md>")
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

    errors.extend(
        validate_concrete_next_step(
            text,
            allowed_next_step_types=phase_next_step_types("prd-writer"),
        )
    )

    for label in OLD_TERMINAL_LABELS:
        if label in text:
            errors.append(f"Old terminal contract label detected: {label!r}")

    if re.search(r"^\s*-\s*`?next_step`?\s*:", text, flags=re.IGNORECASE | re.MULTILINE):
        errors.append("Loose 'next_step' field detected; use the normalized Concrete Next Step fields")

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
