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

VAGUE_ACTION_PATTERNS = [
    r"\bcontinue\b",
    r"\bproceed\b",
    r"\bfix issues\b",
    r"\breview later\b",
    r"\bupdate docs as needed\b",
    r"\bimplement changes\b",
]


def heading_exists(text: str, heading: str) -> bool:
    pattern = rf"^##+\s+{re.escape(heading)}\s*$"
    return re.search(pattern, text, flags=re.MULTILINE) is not None


def extract_field(text: str, field: str) -> str | None:
    pattern = rf"-\s*`{re.escape(field)}`\s*:\s*(.+)"
    match = re.search(pattern, text)
    if not match:
        return None
    return match.group(1).strip()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_adr_doc.py <adr-markdown-file>", file=sys.stderr)
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

    for field in REQUIRED_NEXT_STEP_FIELDS:
        value = extract_field(text, field)
        if value is None:
            errors.append(f"Missing Concrete Next Step field: `{field}`")
        elif value.strip() in {"", "TBD", "TODO", "<todo>", "<placeholder>"}:
            errors.append(f"Concrete Next Step field `{field}` is empty or placeholder")

    next_step_type = extract_field(text, "next_step_type")
    if next_step_type and next_step_type not in ALLOWED_NEXT_STEP_TYPES:
        errors.append(
            f"Invalid next_step_type `{next_step_type}`. Allowed: {', '.join(sorted(ALLOWED_NEXT_STEP_TYPES))}"
        )

    linkage_matches = re.findall(r"architecture_linkage`?\s*:\s*([A-Z_]+)", text)
    if linkage_matches:
        for linkage in linkage_matches:
            if linkage not in ALLOWED_ARCHITECTURE_LINKAGE:
                errors.append(
                    f"Invalid architecture_linkage `{linkage}`. Allowed: {', '.join(sorted(ALLOWED_ARCHITECTURE_LINKAGE))}"
                )
    elif heading_exists(text, "Architecture Linkage"):
        warnings.append("Architecture Linkage section exists but no explicit `architecture_linkage` field was found")

    action = extract_field(text, "action") or ""
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
