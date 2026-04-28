#!/usr/bin/env python3
"""Regression tests for shared workflow contracts."""

from __future__ import annotations

import unittest
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from workflow_contracts import (
    canonical_next_step_types,
    phase_next_step_types,
    validate_concrete_next_step,
)


VALID_BLOCK = """# Report

## Concrete Next Step

- `next_step_type`: IMPLEMENT_PLAN
- `target`: `PLAN.md`
- `action`: Implement the approved plan within its documented scope.
- `why_this_is_next`: The plan is approved and has explicit validation.
- `blocking_condition`: Stop if source artifacts conflict.
- `suggested_prompt`: Use `implement-task` to implement `PLAN.md`.
"""


class WorkflowContractTests(unittest.TestCase):
    def test_canonical_enum_excludes_deprecated_aliases(self) -> None:
        canonical = canonical_next_step_types()

        self.assertIn("IMPLEMENT_PLAN", canonical)
        self.assertIn("CREATE_LIGHTWEIGHT_PLAN", canonical)
        self.assertNotIn("CREATE_OR_UPDATE_ADR", canonical)
        self.assertNotIn("START_IMPLEMENTATION", canonical)

    def test_phase_allowed_values_are_read_from_next_step_types_doc(self) -> None:
        plan_values = phase_next_step_types("plan-writer")
        implementation_values = phase_next_step_types("implement-task")
        review_values = phase_next_step_types("review-phase")

        self.assertIn("IMPLEMENT_LIGHTWEIGHT_PLAN", plan_values)
        self.assertIn("RUN_LIGHTWEIGHT_REVIEW", implementation_values)
        self.assertIn("IMPLEMENT_PLAN", review_values)
        self.assertIn("SPLIT_INTO_PLANS", review_values)
        self.assertIn("CREATE_PLAN", review_values)
        self.assertIn("CREATE_ARCHITECTURE", review_values)
        self.assertIn("ESCALATE_TO_FULL_WORKFLOW", review_values)
        self.assertNotIn("CREATE_OR_UPDATE_ARCHITECTURE", plan_values)
        self.assertNotIn("RUN_IMPLEMENTATION", review_values)

    def test_valid_block_passes_for_allowed_phase_value(self) -> None:
        errors = validate_concrete_next_step(
            VALID_BLOCK,
            allowed_next_step_types=phase_next_step_types("plan-writer"),
        )

        self.assertEqual([], errors)

    def test_rejects_multiple_blocks_and_deprecated_alias(self) -> None:
        text = VALID_BLOCK + VALID_BLOCK.replace("IMPLEMENT_PLAN", "CREATE_OR_UPDATE_ADR")

        errors = validate_concrete_next_step(
            text,
            allowed_next_step_types=phase_next_step_types("plan-writer"),
        )

        self.assertTrue(any("exactly one" in error for error in errors))
        self.assertTrue(any("Invalid next_step_type" in error for error in errors))

    def test_rejects_old_terminal_wording_and_placeholders(self) -> None:
        text = """# Report

## Immediate Next Step

## Concrete Next Step

- `next_step_type`: TODO
- `target`: <target>
- `action`: Continue.
- `why_this_is_next`: TBD
- `blocking_condition`: -
- `suggested_prompt`: ...
"""

        errors = validate_concrete_next_step(text)

        self.assertTrue(any("deprecated terminal wording" in error for error in errors))
        self.assertTrue(any("placeholder" in error for error in errors))
        self.assertTrue(any("too vague" in error for error in errors))

    def test_review_validator_accepts_lightweight_template_mode_shape(self) -> None:
        report = """# Lightweight Task Review Report

## Review Mode

- `mode`: LIGHTWEIGHT_TASK_REVIEW
- `plan`: `PLAN.md`
- `implementation_summary`: implementation summary

## Review Status

- `status`: APPROVED

## Lightweight Eligibility Check

- `one_objective_preserved`: true
- `product_behavior_clear_or_unaffected`: true
- `architecture_unchanged`: true
- `no_adr_decision_introduced`: true
- `no_roadmap_need_introduced`: true
- `validation_sufficient`: true

## Findings

None.

## Validation Assessment

Validation evidence is sufficient.

## Acceptance Decision

Approved.

## Concrete Next Step

- `next_step_type`: MERGE_OR_CLOSE_TASK
- `target`: current task
- `action`: Close the reviewed task as accepted.
- `why_this_is_next`: The lightweight review found no blocking findings.
- `blocking_condition`: none
- `suggested_prompt`: Close the task after this approved lightweight review.
"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            report_path = Path(tmp_dir) / "lightweight-review.md"
            report_path.write_text(report, encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    "review-phase/scripts/check_review_report.py",
                    str(report_path),
                ],
                cwd=Path(__file__).resolve().parents[1],
                text=True,
                capture_output=True,
            )

        self.assertEqual("", result.stderr)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_skill_validator_works_when_installed_without_root_scripts(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        output = VALID_BLOCK.replace("IMPLEMENT_PLAN", "CREATE_PRD")

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_repo = Path(tmp_dir)
            shutil.copytree(repo_root / "docs" / "workflow", tmp_repo / "docs" / "workflow")
            installed_scripts = tmp_repo / ".agents" / "skills" / "brainstorm-gate" / "scripts"
            shutil.copytree(repo_root / "brainstorm-gate" / "scripts", installed_scripts)
            output_path = tmp_repo / "brainstorm.md"
            output_path.write_text(output, encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(installed_scripts / "check_brainstorm_output.py"),
                    str(output_path),
                ],
                cwd=tmp_repo,
                text=True,
                capture_output=True,
            )

        self.assertEqual("", result.stderr)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
