#!/usr/bin/env python3
"""Lightweight validator for architecture-aware roadmap documents.

This script checks structural consistency only. It does not judge roadmap quality.
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

OLD_TERMINAL_PATTERNS = [
    r"^#+\s+Immediate Next Step\b",
    r"^#+\s+Continuation Prompt\b",
    r"`?next_step`?\s*:",
    r"`?follow_up`?\s*:",
]

PLACEHOLDER_PATTERNS = [
    r"`?next_step_type`?\s*:\s*$",
    r"`?target`?\s*:\s*(<.*?>)?\s*$",
    r"`?action`?\s*:\s*(<.*?>)?\s*$",
    r"`?why_this_is_next`?\s*:\s*(<.*?>)?\s*$",
    r"`?blocking_condition`?\s*:\s*(<.*?>)?\s*$",
    r"`?suggested_prompt`?\s*:\s*(<.*?>)?\s*$",
]

VAGUE_ACTIONS = [
    "continue development",
    "implement roadmap",
    "proceed as planned",
    "fix issues",
    "review later",
    "do next step",
    "continue",
    "move forward",
    "update docs as needed",
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

    cns_matches = re.findall(r"^##\s+Concrete Next Step\s*$", text, re.MULTILINE)
    if len(cns_matches) == 0:
        errors.append("Missing exact section heading: ## Concrete Next Step")
    elif len(cns_matches) > 1:
        errors.append("Multiple ## Concrete Next Step sections found; exactly one is allowed")

    for field in NEXT_STEP_FIELDS:
        matches = re.findall(rf"`?{re.escape(field)}`?\s*:", text, re.IGNORECASE)
        if not matches:
            errors.append(f"Missing Concrete Next Step field: {field}")

    match = re.search(r"`?next_step_type`?\s*:\s*`?([A-Z_]+)`?", text)
    if match:
        value = match.group(1).strip()
        if value not in ALLOWED_NEXT_STEP_TYPES:
            errors.append(f"Invalid next_step_type: {value}")
    else:
        errors.append("Could not parse next_step_type value")

    for pattern in OLD_TERMINAL_PATTERNS:
        if re.search(pattern, text, re.MULTILINE | re.IGNORECASE):
            errors.append(f"Old or loose terminal field is not allowed: {pattern}")

    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, text, re.MULTILINE | re.IGNORECASE):
            errors.append(f"Placeholder or empty Concrete Next Step value found: {pattern}")

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
