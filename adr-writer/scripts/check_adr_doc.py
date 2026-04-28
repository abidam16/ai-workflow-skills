#!/usr/bin/env python3
"""Lightweight validator for architecture-aware ADR documents.

Usage:
    python scripts/check_adr_doc.py docs/adr/0001-example.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

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

ALLOWED_NEXT_STEP_TYPES = {
    "UPDATE_ARCHITECTURE",
    "CREATE_OR_UPDATE_ROADMAP",
    "CREATE_OR_UPDATE_PLAN",
    "RETURN_TO_PRD",
    "RETURN_TO_ARCHITECTURE",
    "REVISE_ADR",
    "CREATE_SUPERSEDING_ADR",
    "REQUEST_MISSING_SOURCE_ARTIFACT",
    "REQUEST_DECISION_INPUT",
    "RETURN_TO_REVIEW",
    "START_IMPLEMENTATION",
    "STOP_AND_ESCALATE",
}

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

    concrete_next_step_count = count_heading(text, "Concrete Next Step")
    if concrete_next_step_count == 0:
        errors.append("Missing required section: ## Concrete Next Step")
    elif concrete_next_step_count > 1:
        errors.append("Multiple ## Concrete Next Step sections found; expected exactly one")

    section = extract_concrete_next_step_section(text)
    for field in REQUIRED_NEXT_STEP_FIELDS:
        value = extract_field(section, field)
        if value is None:
            errors.append(f"Missing Concrete Next Step field: `{field}`")
        elif value.strip() in PLACEHOLDERS:
            errors.append(f"Concrete Next Step field `{field}` is empty or placeholder")

    next_step_type = extract_field(section, "next_step_type")
    if next_step_type and next_step_type not in ALLOWED_NEXT_STEP_TYPES:
        errors.append(
            f"Invalid next_step_type `{next_step_type}`. "
            f"Allowed: {', '.join(sorted(ALLOWED_NEXT_STEP_TYPES))}"
        )

    for pattern in FORBIDDEN_TERMINAL_PATTERNS:
        if re.search(pattern, text, flags=re.MULTILINE | re.IGNORECASE):
            errors.append(f"Found legacy or loose terminal field matching: {pattern}")

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

    action = extract_field(section, "action") or ""
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
