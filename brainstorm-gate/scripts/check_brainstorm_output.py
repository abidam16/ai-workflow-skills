#!/usr/bin/env python3
"""Validate brainstorm-gate outputs for the normalized Concrete Next Step contract.

Usage:
    python brainstorm-gate/scripts/check_brainstorm_output.py path/to/brainstorm-output.md
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

OLD_TERMINAL_FIELDS = [
    "## Immediate Next Step",
    "## Continuation Prompt",
]

VAGUE_PHRASES = [
    "continue development",
    "continue with next step",
    "do the next step",
    "proceed as needed",
    "fix issues",
    "review already done",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_brainstorm_output.py <brainstorm-output.md>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: File not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    errors.extend(
        validate_concrete_next_step(
            text,
            allowed_next_step_types=phase_next_step_types("brainstorm-gate"),
        )
    )

    for old_field in OLD_TERMINAL_FIELDS:
        if old_field in text:
            errors.append(
                f"Old terminal section found: {old_field}. Use ## Concrete Next Step instead."
            )

    if errors:
        print("Brainstorm output failed validation:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Brainstorm output passes Concrete Next Step validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
