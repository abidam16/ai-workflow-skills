#!/usr/bin/env python3
"""Shared workflow contract helpers for local skill validators."""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Iterable

NEXT_STEP_TYPES_PATH = None

REQUIRED_NEXT_STEP_FIELDS = (
    "next_step_type",
    "target",
    "action",
    "why_this_is_next",
    "blocking_condition",
    "suggested_prompt",
)

DEPRECATED_TERMINAL_PATTERNS = (
    r"^##+\s+Immediate Next Step\s*$",
    r"^##+\s+Continuation Prompt\s*$",
    r"^\s*`?next_step`?\s*:",
    r"^\s*`?follow_up`?\s*:",
    r"^\s*-\s*`?next_step`?\s*:",
    r"^\s*-\s*`?follow_up`?\s*:",
)

PLACEHOLDER_VALUES = {
    "",
    "-",
    "...",
    "n/a",
    "tbd",
    "todo",
    "<action>",
    "<blocking_condition>",
    "<suggested_prompt>",
    "<target>",
    "<why_this_is_next>",
}

VAGUE_ACTION_PATTERNS = (
    r"^continue\b",
    r"^continue development\b",
    r"^do (it|the task|next step)\b",
    r"^fix( the)? issues\b",
    r"^implementation done\b",
    r"^implement( it| changes| the feature)?\.?$",
    r"^move forward\b",
    r"^proceed\b",
    r"^review later\b",
    r"^update docs as needed\b",
)


@lru_cache(maxsize=1)
def _next_step_types_text() -> str:
    path = next_step_types_path()
    if path is None:
        raise FileNotFoundError(
            "Could not find docs/workflow/NEXT_STEP_TYPES.md. "
            "Copy docs/workflow into the target repo or run validators from this repository."
        )
    return path.read_text(encoding="utf-8")


def next_step_types_path() -> Path | None:
    """Find the shared next-step enum from repo root or an installed skill path."""

    global NEXT_STEP_TYPES_PATH
    if NEXT_STEP_TYPES_PATH is not None:
        return NEXT_STEP_TYPES_PATH

    start = Path(__file__).resolve()
    for parent in (start.parent, *start.parents):
        candidate = parent / "docs" / "workflow" / "NEXT_STEP_TYPES.md"
        if candidate.exists():
            NEXT_STEP_TYPES_PATH = candidate
            return candidate
    return None

@lru_cache(maxsize=1)
def canonical_next_step_types() -> set[str]:
    """Return canonical values from section 2 of NEXT_STEP_TYPES.md."""

    text = _next_step_types_text()
    section = _between(text, "## 2. Canonical Values", "## 3. Allowed Values by Phase")
    return set(re.findall(r"`([A-Z][A-Z0-9_]+)`", section))


@lru_cache(maxsize=None)
def phase_next_step_types(phase: str) -> set[str]:
    """Return values allowed for one phase from NEXT_STEP_TYPES.md."""

    text = _next_step_types_text()
    pattern = rf"^###\s+`{re.escape(phase)}`\s*$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match:
        return set()
    fenced = re.search(r"```text\s*(.*?)```", text[match.end() :], flags=re.DOTALL)
    if not fenced:
        return set()
    values = {
        line.strip()
        for line in fenced.group(1).splitlines()
        if line.strip() and not line.strip().startswith("#")
    }
    return values


def validate_concrete_next_step(
    text: str,
    *,
    allowed_next_step_types: Iterable[str] | None = None,
    require_exactly_one: bool = True,
) -> list[str]:
    """Validate the shared Concrete Next Step contract."""

    errors: list[str] = []
    sections = concrete_next_step_sections(text)

    if require_exactly_one and len(sections) != 1:
        errors.append(
            f"Expected exactly one '## Concrete Next Step' section, found {len(sections)}."
        )
    elif not sections:
        errors.append("Missing required section: ## Concrete Next Step.")

    for pattern in DEPRECATED_TERMINAL_PATTERNS:
        if re.search(pattern, text, flags=re.MULTILINE | re.IGNORECASE):
            errors.append(f"Found deprecated terminal wording matching: {pattern}")

    section = sections[-1] if sections else ""
    for field in REQUIRED_NEXT_STEP_FIELDS:
        value = extract_next_step_field(section, field)
        if value is None:
            errors.append(f"Concrete Next Step missing required field: `{field}`.")
            continue
        if is_placeholder(value):
            errors.append(f"Concrete Next Step field `{field}` is empty or placeholder.")

    next_step_type = extract_next_step_field(section, "next_step_type")
    allowed = set(allowed_next_step_types or canonical_next_step_types())
    if next_step_type and not is_placeholder(next_step_type):
        clean_type = normalize_inline_value(next_step_type)
        if clean_type not in canonical_next_step_types():
            errors.append(f"Invalid next_step_type `{clean_type}`; not canonical.")
        elif allowed and clean_type not in allowed:
            errors.append(f"Invalid next_step_type `{clean_type}` for this phase.")

    action = extract_next_step_field(section, "action") or ""
    if is_vague_action(action):
        errors.append(f"Concrete Next Step action is too vague: {action!r}.")

    return errors


def concrete_next_step_sections(text: str) -> list[str]:
    matches = list(re.finditer(r"^## Concrete Next Step\s*$", text, flags=re.MULTILINE))
    sections: list[str] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append(text[start:end])
    return sections


def extract_next_step_field(section: str, field: str) -> str | None:
    pattern = rf"^-\s*`{re.escape(field)}`\s*:\s*(.*)$"
    match = re.search(pattern, section, flags=re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip()


def normalize_inline_value(value: str) -> str:
    return value.strip().strip("`").strip()


def is_placeholder(value: str) -> bool:
    normalized = normalize_inline_value(value).strip().lower()
    return normalized in PLACEHOLDER_VALUES or bool(re.fullmatch(r"<[^>]+>", normalized))


def is_vague_action(action: str) -> bool:
    normalized = normalize_inline_value(action).strip().lower().rstrip(".")
    return any(re.search(pattern, normalized) for pattern in VAGUE_ACTION_PATTERNS)


def _between(text: str, start_heading: str, end_heading: str) -> str:
    start = text.index(start_heading) + len(start_heading)
    end = text.index(end_heading, start)
    return text[start:end]
