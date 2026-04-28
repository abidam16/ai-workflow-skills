#!/usr/bin/env python3
"""Validate review-phase reports for required review-mode and Concrete Next Step structure."""

from __future__ import annotations

import argparse
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
    "LIGHTWEIGHT_TASK_REVIEW",
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
    "LIGHTWEIGHT_TASK_REVIEW": [
        "Lightweight Eligibility Check",
        "Findings",
        "Validation Assessment",
        "Acceptance Decision",
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

    errors.extend(
        validate_concrete_next_step(
            text,
            allowed_next_step_types=phase_next_step_types("review-phase"),
        )
    )

    next_step_type = extract_next_step_field(text, "next_step_type")

    action = extract_next_step_field(text, "action") or ""
    normalized_action = action.lower().strip(' .')
    for pattern in VAGUE_ACTION_PATTERNS:
        if re.search(pattern, normalized_action):
            errors.append(f"Concrete Next Step action is too vague: {action!r}.")
            break

    mode_match = re.search(r"Review mode:\s*`?([A-Z_]+)`?", text, flags=re.IGNORECASE)
    mode = mode_match.group(1) if mode_match else _extract_field(text, "mode")
    if not mode:
        errors.append("Review mode is missing or not machine-readable.")
    else:
        if mode not in VALID_MODES:
            errors.append(f"Invalid review mode: {mode}.")

    status_match = re.search(r"Final status:\s*`?([A-Z_]+)`?", text, flags=re.IGNORECASE)
    status = status_match.group(1) if status_match else _extract_field(text, "status")
    if status and status not in VALID_STATUSES:
        errors.append(f"Invalid final status: {status}.")

    if mode in MODE_REQUIRED_SECTIONS:
        for section in MODE_REQUIRED_SECTIONS[mode]:
            if section not in text:
                errors.append(f"{mode} report missing required section: {section}.")

    if next_step_type in {"MERGE_OR_CLOSE_TASK", "START_NEXT_PLAN"}:
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
