#!/usr/bin/env python3
"""Validate implement-task reports for the normalized Concrete Next Step contract.

Usage:
    python scripts/check_implementation_report.py path/to/implementation-summary.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from workflow_contracts import phase_next_step_types, validate_concrete_next_step

REQUIRED_FIELDS = [
    "next_step_type",
    "target",
    "action",
    "why_this_is_next",
    "blocking_condition",
    "suggested_prompt",
]

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

    errors.extend(
        validate_concrete_next_step(
            text,
            allowed_next_step_types=phase_next_step_types("implement-task"),
        )
    )

    if errors:
        print("Concrete Next Step validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Concrete Next Step validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
