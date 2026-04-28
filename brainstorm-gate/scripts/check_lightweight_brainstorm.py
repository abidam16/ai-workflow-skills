#!/usr/bin/env python3
"""Validate lightweight brainstorm outputs."""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from workflow_contracts import phase_next_step_types, validate_concrete_next_step

REQUIRED = [
    "## Lightweight Classification",
    "`mode`",
    "`reason`",
    "`scope`",
    "`why_prd_not_needed`",
    "`why_architecture_not_needed`",
    "`why_adr_not_needed`",
    "`why_roadmap_not_needed`",
    "`validation_path`",
    "`escalation_trigger`",
    "## Concrete Next Step",
    "`next_step_type`",
    "`target`",
    "`action`",
    "`why_this_is_next`",
    "`blocking_condition`",
    "`suggested_prompt`",
]
OLD = ["Immediate Next Step", "Continuation Prompt", "loose next_step"]


def main(path: str) -> int:
    text = Path(path).read_text(encoding="utf-8")
    errors = [f"Missing required marker: {m}" for m in REQUIRED if m not in text]
    errors += [f"Old terminal wording is not allowed: {m}" for m in OLD if m in text]
    errors.extend(
        validate_concrete_next_step(
            text,
            allowed_next_step_types=phase_next_step_types("brainstorm-gate"),
        )
    )
    if "USE_LIGHTWEIGHT_MODE" in text and "LIGHTWEIGHT_TASK" not in text:
        errors.append("USE_LIGHTWEIGHT_MODE requires mode: LIGHTWEIGHT_TASK")
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print("OK: lightweight brainstorm output is valid")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: check_lightweight_brainstorm.py <file>")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
