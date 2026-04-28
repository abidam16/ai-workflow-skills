#!/usr/bin/env python3
"""Validate architecture-aware PLAN.md files and normalized Concrete Next Step output.

Usage:
    python scripts/check_plan_doc.py PLAN.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from workflow_contracts import (
    extract_next_step_field,
    phase_next_step_types,
    validate_concrete_next_step,
)

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

ALLOWED_READINESS = {"NOT_RELEVANT", "READY", "PARTIAL", "MISSING", "CONFLICTING"}

OLD_TERMINAL_PATTERNS = [
    r"^##+\s+Immediate Next Step\s*$",
    r"^##+\s+Continuation Prompt\s*$",
    r"`?next_step`?\s*:",
    r"`?follow_up`?\s*:",
]

PLACEHOLDER_VALUES = {"", "todo", "tbd", "n/a", "-", "...", "<todo>", "<tbd>"}

VAGUE_ACTION_PATTERNS = [
    r"^continue\b",
    r"^proceed\b",
    r"^move forward\b",
    r"^fix issues\.?$",
    r"^do the task\.?$",
    r"^implementation\.?$",
    r"^the plan is ready\.?$",
]


def section_exists(text: str, heading: str) -> bool:
    pattern = rf"^##+\s+{re.escape(heading)}\s*$"
    return re.search(pattern, text, flags=re.MULTILINE) is not None


def count_section(text: str, heading: str) -> int:
    pattern = rf"^##+\s+{re.escape(heading)}\s*$"
    return len(re.findall(pattern, text, flags=re.MULTILINE))


def extract_field(text: str, field: str) -> str | None:
    pattern = rf"`{re.escape(field)}`\s*:\s*([^\n]+)"
    match = re.search(pattern, text)
    if not match:
        return None
    return match.group(1).strip().strip("`").strip()


def is_placeholder(value: str | None) -> bool:
    if value is None:
        return True
    return value.strip().lower() in PLACEHOLDER_VALUES


def is_vague_action(action: str) -> bool:
    normalized = action.lower().strip().rstrip(".")
    return any(re.search(pattern, normalized) for pattern in VAGUE_ACTION_PATTERNS)


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

    errors.extend(
        validate_concrete_next_step(
            text,
            allowed_next_step_types=phase_next_step_types("plan-writer"),
        )
    )

    readiness = extract_field(text, "architecture_readiness")
    if readiness and readiness not in ALLOWED_READINESS:
        errors.append(f"Invalid architecture_readiness: {readiness}")

    action = extract_next_step_field(text, "action")
    if action and is_vague_action(action):
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
