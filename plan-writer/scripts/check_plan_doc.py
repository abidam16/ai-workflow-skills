#!/usr/bin/env python3
"""Lightweight validator for architecture-aware PLAN.md files.

Usage:
    python scripts/check_plan_doc.py PLAN.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "Task Summary",
    "Plan Status",
    "Source Artifacts",
    "Architecture Readiness",
    "Objective",
    "Scope",
    "Binding Constraints",
    "Detailed Specification",
    "Files / Components to Change",
    "Validation and Tests",
    "Review Checklist",
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
    "IMPLEMENT_PLAN",
    "SPLIT_INTO_PLANS",
    "UPDATE_PRD",
    "CREATE_OR_UPDATE_ARCHITECTURE",
    "CREATE_OR_UPDATE_ADR",
    "UPDATE_ROADMAP",
    "REVISE_PLAN",
    "REQUEST_MISSING_SOURCE_ARTIFACT",
    "RETURN_TO_REVIEW",
    "STOP_AND_ESCALATE",
}

ALLOWED_READINESS = {"NOT_RELEVANT", "READY", "PARTIAL", "MISSING", "CONFLICTING"}

VAGUE_ACTIONS = {
    "continue",
    "fix issues",
    "do the task",
    "proceed",
    "move forward",
    "review done",
    "implementation",
}


def section_exists(text: str, heading: str) -> bool:
    pattern = rf"^##+\s+{re.escape(heading)}\s*$"
    return re.search(pattern, text, flags=re.MULTILINE) is not None


def extract_field(text: str, field: str) -> str | None:
    pattern = rf"`{re.escape(field)}`\s*:\s*([^\n]+)"
    match = re.search(pattern, text)
    if not match:
        return None
    return match.group(1).strip().strip("`")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_plan_doc.py PLAN.md", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for section in REQUIRED_SECTIONS:
        if not section_exists(text, section):
            errors.append(f"Missing required section: {section}")

    for field in NEXT_STEP_FIELDS:
        if extract_field(text, field) is None:
            errors.append(f"Missing Concrete Next Step field: {field}")

    next_step_type = extract_field(text, "next_step_type")
    if next_step_type and next_step_type not in ALLOWED_NEXT_STEP_TYPES:
        errors.append(f"Invalid next_step_type: {next_step_type}")

    readiness = extract_field(text, "architecture_readiness")
    if readiness and readiness not in ALLOWED_READINESS:
        errors.append(f"Invalid architecture_readiness: {readiness}")

    action = extract_field(text, "action")
    if action:
        normalized = action.lower().strip().rstrip(".")
        if normalized in VAGUE_ACTIONS:
            errors.append(f"Concrete Next Step action is too vague: {action}")

    if errors:
        print("PLAN.md validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("PLAN.md validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
