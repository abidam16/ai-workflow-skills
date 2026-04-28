#!/usr/bin/env python3
"""Validate lightweight PLAN documents."""
import re
import sys
from pathlib import Path

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
    if text.count("## Concrete Next Step") != 1:
        errors.append("Expected exactly one ## Concrete Next Step block")
    if re.search(r"Immediate Next Step|Continuation Prompt|\bnext_step\b|\bfollow_up\b", text):
        errors.append("Old/loose next-step wording is not allowed")
    if re.search(r"`action`:\s*(continue|fix issues|do it|implement)\s*$", text, re.I | re.M):
        errors.append("Concrete Next Step action is too vague")
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
