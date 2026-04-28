#!/usr/bin/env python3
"""Validate implement-task reports for the normalized Concrete Next Step contract.

Usage:
    python scripts/check_implementation_report.py path/to/implementation-summary.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "next_step_type",
    "target",
    "action",
    "why_this_is_next",
    "blocking_condition",
    "suggested_prompt",
]

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

BANNED_TERMS = [
    "Immediate Next Step",
    "Continuation Prompt",
    "`next_step`",
    "next_step:",
    "`follow_up`",
    "follow_up:",
]

VAGUE_ACTION_PATTERNS = [
    r"^\s*continue\s*\.?\s*$",
    r"^\s*continue development\s*\.?\s*$",
    r"^\s*fix issues\s*\.?\s*$",
    r"^\s*update docs as needed\s*\.?\s*$",
    r"^\s*review later\s*\.?\s*$",
    r"^\s*implementation done\s*\.?\s*$",
]

PLACEHOLDERS = {"", "tbd", "todo", "n/a", "-", "...", "<todo>", "<tbd>"}


def extract_field(block: str, field: str) -> str | None:
    # Supports: - `field`: value
    pattern = rf"^-\s*`{re.escape(field)}`:\s*(.*)$"
    match = re.search(pattern, block, flags=re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_implementation_report.py <path>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")

    errors: list[str] = []

    count = len(re.findall(r"^## Concrete Next Step\s*$", text, flags=re.MULTILINE))
    if count == 0:
        errors.append("Missing required section: ## Concrete Next Step")
    elif count > 1:
        errors.append("Multiple ## Concrete Next Step sections found; expected exactly one")

    for banned in BANNED_TERMS:
        if banned in text:
            errors.append(f"Banned old/loose next-step term found: {banned}")

    if count == 1:
        block = text.split("## Concrete Next Step", 1)[1]
        for field in REQUIRED_FIELDS:
            value = extract_field(block, field)
            if value is None:
                errors.append(f"Missing required field: `{field}`")
                continue
            normalized = value.strip().strip('"').strip("'").lower()
            if normalized in PLACEHOLDERS:
                errors.append(f"Field `{field}` has placeholder/empty value: {value!r}")

        next_step_type = extract_field(block, "next_step_type")
        if next_step_type:
            next_step_type_clean = next_step_type.strip().strip("`").strip()
            if next_step_type_clean not in ALLOWED_NEXT_STEP_TYPES:
                errors.append(
                    f"Invalid next_step_type: {next_step_type_clean}. "
                    f"Allowed: {', '.join(sorted(ALLOWED_NEXT_STEP_TYPES))}"
                )

        action = extract_field(block, "action") or ""
        for pattern in VAGUE_ACTION_PATTERNS:
            if re.match(pattern, action, flags=re.IGNORECASE):
                errors.append(f"Vague action wording is not allowed: {action!r}")

    if errors:
        print("Concrete Next Step validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Concrete Next Step validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
