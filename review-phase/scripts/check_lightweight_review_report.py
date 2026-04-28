#!/usr/bin/env python3
"""Validate lightweight task review reports."""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from workflow_contracts import phase_next_step_types, validate_concrete_next_step

REQUIRED = [
    "## Review Mode",
    "LIGHTWEIGHT_TASK_REVIEW",
    "## Review Status",
    "## Lightweight Eligibility Check",
    "`one_objective_preserved`",
    "`product_behavior_clear_or_unaffected`",
    "`architecture_unchanged`",
    "`no_adr_decision_introduced`",
    "`no_roadmap_need_introduced`",
    "`validation_sufficient`",
    "## Findings",
    "## Validation Assessment",
    "## Acceptance Decision",
    "## Concrete Next Step",
    "`next_step_type`",
    "`target`",
    "`action`",
    "`why_this_is_next`",
    "`blocking_condition`",
    "`suggested_prompt`",
]


def main(path: str) -> int:
    text = Path(path).read_text(encoding="utf-8")
    errors = [f"Missing required marker: {m}" for m in REQUIRED if m not in text]
    errors.extend(
        validate_concrete_next_step(
            text,
            allowed_next_step_types=phase_next_step_types("review-phase"),
        )
    )
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print("OK: lightweight review report is valid")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: check_lightweight_review_report.py <file>")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
