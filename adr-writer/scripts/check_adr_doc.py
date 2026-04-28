#!/usr/bin/env python3
"""Lightweight validator for architecture-aware ADR documents.

Usage:
    python scripts/check_adr_doc.py docs/adr/0001-example.md
"""

from __future__ import annotations

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

REQUIRED_HEADINGS = [
    "Status",
    "Decision Boundary",
    "Context / Problem",
    "Decision Drivers",
    "Considered Options",
    "Decision",
    "Consequences",
    "Architecture Linkage",
    "Downstream Impact",
    "Related Artifacts",
    "Concrete Next Step",
]

REQUIRED_NEXT_STEP_FIELDS = [
    "next_step_type",
    "target",
    "action",
    "why_this_is_next",
    "blocking_condition",
    "suggested_prompt",
]

ALLOWED_ARCHITECTURE_LINKAGE = {
    "NONE",
    "ARCHITECTURE_CONTEXT_ONLY",
    "ADD_ADR_INDEX_ENTRY",
    "UPDATE_ROOT_ARCHITECTURE",
    "UPDATE_INITIATIVE_ARCHITECTURE",
    "UPDATE_ROOT_AND_INITIATIVE_ARCHITECTURE",
    "ARCHITECTURE_CONFLICT_FOUND",
    "ARCHITECTURE_MISSING",
}

FORBIDDEN_TERMINAL_PATTERNS = [
    r"^##+\s+Immediate Next Step\s*$",
    r"^##+\s+Continuation Prompt\s*$",
    r"`?next_step`?\s*:",
    r"`?follow_up`?\s*:",
]

VAGUE_ACTION_PATTERNS = [
    r"\bcontinue\b",
    r"\bproceed\b",
    r"\bfix issues\b",
    r"\breview later\b",
    r"\bupdate docs as needed\b",
    r"\bimplement changes\b",
]

PLACEHOLDERS = {"", "TBD", "TODO", "-", "N/A"}


def heading_exists(text: str, heading: str) -> bool:
    pattern = rf"^##+\s+{re.escape(heading)}\s*$"
    return re.search(pattern, text, flags=re.MULTILINE) is not None


def count_heading(text: str, heading: str) -> int:
    pattern = rf"^##+\s+{re.escape(heading)}\s*$"
    return len(re.findall(pattern, text, flags=re.MULTILINE))


def extract_concrete_next_step_section(text: str) -> str:
    match = re.search(r"^##\s+Concrete Next Step\s*$", text, flags=re.MULTILINE)
    if not match:
        return ""
    start = match.start()
    next_heading = re.search(r"^##\s+", text[match.end():], flags=re.MULTILINE)
    if not next_heading:
        return text[start:]
    return text[start : match.end() + next_heading.start()]


def extract_field(section: str, field: str) -> str | None:
    pattern = rf"^-\s*`{re.escape(field)}`\s*:\s*(.*)$"
    match = re.search(pattern, section, flags=re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_adr_doc.py <adr-file>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    for heading in REQUIRED_HEADINGS:
        if not heading_exists(text, heading):
            errors.append(f"Missing required heading: ## {heading}")

    errors.extend(
        validate_concrete_next_step(
            text,
            allowed_next_step_types=phase_next_step_types("adr-writer"),
        )
    )

    section = extract_concrete_next_step_section(text)

    linkage_matches = re.findall(r"`architecture_linkage`\s*:\s*([A-Z_]+)", text)
    if linkage_matches:
        for linkage in linkage_matches:
            if linkage not in ALLOWED_ARCHITECTURE_LINKAGE:
                errors.append(
                    f"Invalid architecture_linkage `{linkage}`. "
                    f"Allowed: {', '.join(sorted(ALLOWED_ARCHITECTURE_LINKAGE))}"
                )
    elif heading_exists(text, "Architecture Linkage"):
        warnings.append("Architecture Linkage section exists but no explicit `architecture_linkage` field was found")

    action = extract_next_step_field(section, "action") or ""
    for pattern in VAGUE_ACTION_PATTERNS:
        if re.search(pattern, action, flags=re.IGNORECASE):
            warnings.append(f"Concrete action may be vague: `{action}`")
            break

    if errors:
        print("ADR validation failed:")
        for error in errors:
            print(f"- ERROR: {error}")
        for warning in warnings:
            print(f"- WARNING: {warning}")
        return 1

    print("ADR validation passed.")
    for warning in warnings:
        print(f"- WARNING: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
