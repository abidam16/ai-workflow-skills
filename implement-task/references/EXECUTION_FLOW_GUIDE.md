# Execution Flow Guide

## Step 1: Intake

Read the plan and identify:

- primary objective
- source artifacts
- in-scope and out-of-scope boundaries
- expected files/components
- tests/validation
- review checklist

## Step 2: Source check

If the task is architecture-sensitive, read relevant architecture and ADR sections before coding.

If source artifacts are missing or contradictory, stop before modifying files.

## Step 3: Scope lock

Write or mentally maintain a scope lock:

- files/components likely to change
- behavior that must remain untouched
- assumptions
- validation commands

## Step 4: Minimal implementation

Make the smallest coherent set of changes that satisfies the plan and upstream constraints.

Avoid:

- broad cleanup
- unrelated formatting churn
- expanding task scope
- adding abstractions without plan need
- editing artifacts unrelated to the task

## Step 5: Validate

Run the commands requested by the plan when possible. Add focused tests only when they are in scope or necessary to prove correctness.

## Step 6: Report

Produce either:

- implementation summary
- implementation summary with deviation report
- blocker report

Always include a concrete next step.
