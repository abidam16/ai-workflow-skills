#!/usr/bin/env python3
"""Lightweight validator for architecture-aware implementation reports.

Usage:
    python scripts/check_implementation_report.py IMPLEMENTATION_SUMMARY.md
    python scripts/check_implementation_report.py BLOCKER_REPORT.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_COMMON_SECTIONS = [
    "Outcome",
    "Source Artifacts Checked",
    "Architecture Sensitivity",
    "Concrete Next Step",
]

IMPLEMENTED_SECTIONS = [
    "Scope Lock",
    "What Was Implemented",
    "Files Changed",
    "Plan Fulfillment",
    "Validation and Tests",
]

BLOCKER_SECTIONS = [
    "Blocker Summary",
    "Blocking Issue",
    "Required Upstream Fix",
]

NEXT_STEP_FIELDS = [
    "next_step_type",
    "target",
    "action",
    "why_this_is_next",
    "blocking_condition",
    "suggested_prompt",
]

ALLOWED_STATUSES = {
    "IMPLEMENTED",
    "IMPLEMENTED_WITH_REPORTED_DEVIATION",
    "BLOCKED_REQUIRES_PLAN_CLARIFICATION",
    "BLOCKED_REQUIRES_PLAN_SPLIT",
    "BLOCKED_REQUIRES_ARCHITECTURE_CLARIFICATION",
    "BLOCKED_REQUIRES_ARCHITECTURE_UPDATE",
    "BLOCKED_REQUIRES_ADR_DECISION",
    "BLOCKED_REQUIRES_UPSTREAM_DECISION",
    "BLOCKED_BY_CONFLICTING_SOURCES",
    "BLOCKED_BY_VALIDATION_FAILURE",
}

ALLOWED_NEXT_STEP_TYPES = {
    "RUN_REVIEW",
    "RUN_VALIDATION",
    "APPLY_MINOR_FIX",
    "UPDATE_PLAN",
    "UPDATE_ARCHITECTURE",
    "CREATE_OR_UPDATE_ADR",
    "UPDATE_ROADMAP",
    "UPDATE_PRD",
    "SPLIT_PLAN",
    "REQUEST_MISSING_SOURCE_ARTIFACT",
    "RESOLVE_SOURCE_CONFLICT",
    "STOP_AND_ESCALATE",
}

VAGUE_ACTIONS = {
    "continue",
    "proceed",
    "move forward",
    "review done",
    "implementation done",
    "fix issues",
    "do next step",
    "next step",
    "review",
    "test",
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
        print("Usage: check_implementation_report.py IMPLEMENTATION_SUMMARY.md", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for section in REQUIRED_COMMON_SECTIONS:
        if not section_exists(text, section):
            errors.append(f"Missing required section: {section}")

    status = extract_field(text, "outcome_status")
    if not status:
        errors.append("Missing outcome_status field")
    elif status not in ALLOWED_STATUSES:
        errors.append(f"Invalid outcome_status: {status}")

    if status and status.startswith("IMPLEMENTED"):
        for section in IMPLEMENTED_SECTIONS:
            if not section_exists(text, section):
                errors.append(f"Missing implemented-report section: {section}")
    elif status and status.startswith("BLOCKED"):
        for section in BLOCKER_SECTIONS:
            if not section_exists(text, section):
                errors.append(f"Missing blocker-report section: {section}")

    for field in NEXT_STEP_FIELDS:
        if extract_field(text, field) is None:
            errors.append(f"Missing Concrete Next Step field: {field}")

    next_step_type = extract_field(text, "next_step_type")
    if next_step_type and next_step_type not in ALLOWED_NEXT_STEP_TYPES:
        errors.append(f"Invalid next_step_type: {next_step_type}")

    action = extract_field(text, "action")
    if action:
        normalized = action.lower().strip().rstrip(".")
        if normalized in VAGUE_ACTIONS:
            errors.append(f"Concrete Next Step action is too vague: {action}")

    suggested_prompt = extract_field(text, "suggested_prompt")
    if suggested_prompt:
        normalized = suggested_prompt.lower().strip().strip('"').rstrip(".")
        if normalized in VAGUE_ACTIONS or len(normalized.split()) < 6:
            errors.append(f"Concrete Next Step suggested_prompt is too vague: {suggested_prompt}")

    if errors:
        print("Implementation report validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Implementation report validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
