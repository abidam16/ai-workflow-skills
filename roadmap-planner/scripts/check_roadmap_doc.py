#!/usr/bin/env python3
"""Lightweight validator for architecture-aware roadmap documents.

This script intentionally checks structure only. It does not judge roadmap quality.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "Source Artifacts",
    "Delivery Objective",
    "Architecture Constraints Used",
    "ADR Constraints Used",
    "Roadmap Phases",
    "Plan Handoff",
    "Concrete Next Step",
]

NEXT_STEP_FIELDS = [
    "next_step_type",
    "target",
    "action",
    "why_this_is_next",
    "blocking_condition",
    "suggested_prompt",
]

ALLOWED_NEXT_STEP_TYPES = {
    "CREATE_PLAN",
    "UPDATE_PLAN",
    "SPLIT_INTO_PLANS",
    "CREATE_OR_UPDATE_ARCHITECTURE",
    "CREATE_OR_UPDATE_ADR",
    "UPDATE_PRD",
    "REVISE_ROADMAP",
    "REQUEST_MISSING_SOURCE_ARTIFACT",
    "RETURN_TO_REVIEW",
    "STOP_AND_ESCALATE",
}

VAGUE_ACTIONS = [
    "continue development",
    "implement roadmap",
    "proceed as planned",
    "fix issues",
    "review later",
    "do next step",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_roadmap_doc.py path/to/ROADMAP.md", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    for section in REQUIRED_SECTIONS:
        if re.search(rf"^#+\s+.*{re.escape(section)}", text, re.MULTILINE | re.IGNORECASE) is None:
            errors.append(f"Missing required section: {section}")

    for field in NEXT_STEP_FIELDS:
        if re.search(rf"`?{re.escape(field)}`?\s*:", text, re.IGNORECASE) is None:
            errors.append(f"Missing Concrete Next Step field: {field}")

    match = re.search(r"`?next_step_type`?\s*:\s*`?([A-Z_]+)`?", text)
    if match:
        value = match.group(1).strip()
        if value not in ALLOWED_NEXT_STEP_TYPES:
            errors.append(f"Invalid next_step_type: {value}")
    else:
        errors.append("Could not parse next_step_type value")

    lower = text.lower()
    for phrase in VAGUE_ACTIONS:
        if phrase in lower:
            warnings.append(f"Vague wording found: {phrase!r}")

    if errors:
        print("Roadmap validation failed:")
        for error in errors:
            print(f"- ERROR: {error}")
        for warning in warnings:
            print(f"- WARNING: {warning}")
        return 1

    print("Roadmap validation passed.")
    for warning in warnings:
        print(f"- WARNING: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
