#!/usr/bin/env python3
"""Validate review-phase reports for required review-mode and Concrete Next Step structure."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_NEXT_STEP_FIELDS = [
    "next_step_type",
    "target",
    "action",
    "why_this_is_next",
    "blocking_condition",
    "suggested_prompt",
]

VALID_MODES = {
    "TASK_REVIEW",
    "ROADMAP_IMPLEMENTATION_REVIEW",
    "ARTIFACT_CONSISTENCY_REVIEW",
}

VALID_STATUSES = {
    "APPROVED",
    "APPROVED_WITH_MINOR_IMPROVEMENTS",
    "NEEDS_REVISION",
    "BLOCKED",
    "CONSISTENT",
    "CONSISTENT_WITH_MINOR_GAPS",
    "NEEDS_ARTIFACT_REVISION",
}

VALID_NEXT_STEP_TYPES = {
    "MERGE_OR_CLOSE_TASK",
    "APPLY_MINOR_FIXES",
    "RETURN_TO_IMPLEMENTATION",
    "RUN_IMPLEMENTATION",
    "RUN_REVIEW",
    "CREATE_PLAN",
    "UPDATE_PLAN",
    "CREATE_ARCHITECTURE",
    "UPDATE_ARCHITECTURE",
    "CREATE_ADR",
    "UPDATE_ADR",
    "CREATE_OR_UPDATE_ADR",
    "UPDATE_ROADMAP",
    "UPDATE_PRD",
    "REQUEST_MISSING_EVIDENCE",
    "REQUEST_MISSING_SOURCE_ARTIFACT",
    "SPLIT_REVIEW_SCOPE",
    "START_NEXT_PLAN",
    "STOP_AND_ESCALATE",
}

OLD_TERMS = [
    "Immediate Next Step",
    "Continuation Prompt",
    "next_step:",
    "follow_up:",
]

VAGUE_ACTION_PATTERNS = [
    r"^continue\b",
    r"^fix( the)? issues\b",
    r"^proceed\b",
    r"^review later\b",
    r"^do next step\b",
    r"^update docs as needed\b",
]

MODE_REQUIRED_SECTIONS = {
    "TASK_REVIEW": [
        "Business / Product Alignment",
        "Architecture Alignment",
        "ADR / Decision Alignment",
        "Plan Alignment",
        "Validation and Test Adequacy",
    ],
    "ROADMAP_IMPLEMENTATION_REVIEW": [
        "Roadmap Fulfillment Assessment",
        "Business / Product Alignment",
        "Architecture Alignment",
        "Cross-Task Alignment",
        "Validation and Integration Evidence",
    ],
    "ARTIFACT_CONSISTENCY_REVIEW": [
        "Authority Chain Check",
        "PRD ↔ Architecture Consistency",
        "Architecture ↔ ADR Consistency",
        "Architecture / ADR ↔ Roadmap Consistency",
        "Roadmap / Source Artifacts ↔ PLAN Consistency",
        "Handoff Contract Check",
    ],
}


def _extract_field(text: str, field: str) -> str | None:
    pattern = rf"-\s*`?{re.escape(field)}`?\s*:\s*(.+)"
    match = re.search(pattern, text)
    if not match:
        return None
    value = match.group(1).strip()
    value = value.strip("` ")
    return value


def validate(text: str) -> list[str]:
    errors: list[str] = []

    if text.count("## Concrete Next Step") != 1:
        errors.append("Report must contain exactly one '## Concrete Next Step' section.")

    for old in OLD_TERMS:
        if old in text:
            errors.append(f"Report contains deprecated terminal wording: {old!r}.")

    for field in REQUIRED_NEXT_STEP_FIELDS:
        value = _extract_field(text, field)
        if value is None:
            errors.append(f"Concrete Next Step missing required field: {field}.")
        elif value.strip() in {"", "-", "TBD", "TODO", "<target>", "<action>"}:
            errors.append(f"Concrete Next Step field has placeholder value: {field}.")

    next_step_type = _extract_field(text, "next_step_type")
    if next_step_type and next_step_type not in VALID_NEXT_STEP_TYPES:
        errors.append(f"Invalid next_step_type: {next_step_type}.")

    action = _extract_field(text, "action") or ""
    normalized_action = action.lower().strip(' .')
    for pattern in VAGUE_ACTION_PATTERNS:
        if re.search(pattern, normalized_action):
            errors.append(f"Concrete Next Step action is too vague: {action!r}.")
            break

    mode_match = re.search(r"Review mode:\s*`?([A-Z_]+)`?", text)
    if not mode_match:
        errors.append("Review mode is missing or not machine-readable.")
        mode = None
    else:
        mode = mode_match.group(1)
        if mode not in VALID_MODES:
            errors.append(f"Invalid review mode: {mode}.")

    status_match = re.search(r"Final status:\s*`?([A-Z_]+)`?", text)
    if status_match and status_match.group(1) not in VALID_STATUSES:
        errors.append(f"Invalid final status: {status_match.group(1)}.")

    if mode in MODE_REQUIRED_SECTIONS:
        for section in MODE_REQUIRED_SECTIONS[mode]:
            if section not in text:
                errors.append(f"{mode} report missing required section: {section}.")

    if next_step_type in {"MERGE_OR_CLOSE_TASK", "RUN_IMPLEMENTATION", "START_NEXT_PLAN"}:
        if "HIGH_URGENCY" in text and not re.search(r"HIGH_URGENCY\s*\|\s*(?:$|\s*\|\s*\|)", text):
            errors.append(
                "High-urgency findings appear incompatible with the selected next_step_type."
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to a review report markdown file")
    args = parser.parse_args()

    path = Path(args.path)
    text = path.read_text(encoding="utf-8")
    errors = validate(text)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Review report contract looks valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
