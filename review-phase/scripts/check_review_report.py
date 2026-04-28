#!/usr/bin/env python3
"""
Lightweight validator for review-phase report shape.

Usage:
  python scripts/check_review_report.py path/to/review-report.md

This does not judge review quality. It checks that the report includes required sections
and a non-empty Concrete Next Step block.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED_NEXT_STEP_TYPES = {
    "MERGE_OR_CLOSE_TASK",
    "APPLY_MINOR_FIXES",
    "RETURN_TO_IMPLEMENTATION",
    "UPDATE_PLAN",
    "UPDATE_ARCHITECTURE",
    "CREATE_OR_UPDATE_ADR",
    "UPDATE_ROADMAP",
    "UPDATE_PRD",
    "REQUEST_MISSING_EVIDENCE",
    "SPLIT_REVIEW_SCOPE",
    "START_NEXT_PLAN",
    "STOP_AND_ESCALATE",
}

REQUIRED_PHRASES = [
    "Review mode",
    "Source Artifacts",
    "Executive Verdict",
    "Architecture Alignment",
    "Findings",
    "Concrete Next Step",
    "next_step_type",
    "target",
    "action",
    "why_this_is_next",
    "blocking_condition",
    "suggested_prompt",
]

VAGUE_NEXT_STEP_PATTERNS = [
    r"review is done",
    r"review already done",
    r"fix the issues",
    r"continue development",
    r"proceed as needed",
    r"consider improvements",
    r"next step depends",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_review_report.py path/to/review-report.md", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    lowered = text.lower()
    errors: list[str] = []

    for phrase in REQUIRED_PHRASES:
        if phrase.lower() not in lowered:
            errors.append(f"Missing required phrase/section: {phrase}")

    match = re.search(r"next_step_type`?\s*:\s*`?([A-Z_]+)`?", text)
    if not match:
        errors.append("Missing parseable next_step_type value")
    else:
        value = match.group(1).strip()
        if value not in ALLOWED_NEXT_STEP_TYPES:
            errors.append(f"Invalid next_step_type: {value}")

    concrete_match = re.search(r"#+\s*Concrete Next Step(?P<body>.*)$", text, flags=re.IGNORECASE | re.DOTALL)
    if not concrete_match:
        errors.append("Missing Concrete Next Step section")
    else:
        body = concrete_match.group("body").strip()
        if len(body) < 80:
            errors.append("Concrete Next Step section appears too short to be actionable")
        for pattern in VAGUE_NEXT_STEP_PATTERNS:
            if re.search(pattern, body, flags=re.IGNORECASE):
                errors.append(f"Vague next-step wording found: {pattern}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("OK: review report includes required structure and concrete next step fields.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
