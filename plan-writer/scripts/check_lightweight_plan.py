#!/usr/bin/env python3
"""Validate lightweight PLAN documents."""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from workflow_contracts import phase_next_step_types, validate_concrete_next_step

REQUIRED = [
    "## Plan Mode",
    "`mode`: LIGHTWEIGHT_TASK",
    "`why_lightweight`",
    "`escalation_trigger`",
    "## Objective",
    "## Scope",
    "### In Scope",
    "### Out of Scope",
    "## Existing Behavior",
    "## Target Behavior",
    "## Implementation Approach",
    "## Validation Checklist",
    "## Risk Check",
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
            allowed_next_step_types=phase_next_step_types("plan-writer"),
        )
    )
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print("OK: lightweight plan is valid")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: check_lightweight_plan.py <file>")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
