#!/usr/bin/env python3
"""Shared validator for lightweight-mode documents.

It checks the common lightweight markers and the normalized Concrete Next Step block.
This is intentionally lightweight and can be used on brainstorm outputs, plans,
implementation summaries, or review reports.
"""
import re
import sys
from pathlib import Path

from workflow_contracts import validate_concrete_next_step

COMMON_NEXT_STEP = [
    "## Concrete Next Step",
    "`next_step_type`",
    "`target`",
    "`action`",
    "`why_this_is_next`",
    "`blocking_condition`",
    "`suggested_prompt`",
]
LIGHTWEIGHT_MARKERS = [
    "LIGHTWEIGHT_TASK",
]
FORBIDDEN = [
    "Immediate Next Step",
    "Continuation Prompt",
    "loose next_step",
    "loose follow_up",
]


def main(path: str) -> int:
    text = Path(path).read_text(encoding="utf-8")
    errors = []
    for marker in COMMON_NEXT_STEP + LIGHTWEIGHT_MARKERS:
        if marker not in text:
            errors.append(f"Missing required marker: {marker}")
    errors.extend(validate_concrete_next_step(text))
    for marker in FORBIDDEN:
        if marker in text:
            errors.append(f"Forbidden old/loose terminal wording: {marker}")
    if re.search(r"`action`:\s*(continue|fix issues|do it|review later|proceed)\b", text, re.I):
        errors.append("Concrete Next Step action is too vague")
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print("OK: lightweight mode document is valid")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: check_lightweight_mode.py <file>")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
