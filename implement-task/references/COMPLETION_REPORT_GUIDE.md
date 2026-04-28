# Completion Report Guide

## Good implementation summary

A good summary lets `review-phase` evaluate the work without reconstructing every action from scratch.

It includes:

- exact outcome status
- source artifacts checked
- architecture sensitivity result
- files changed and reasons
- obligations fulfilled
- tests/validation and results
- deviations and impacts
- remaining gaps
- concrete next step

## Bad implementation summary

Avoid:

- “Implemented successfully.”
- “All done.”
- “Tests pass.”
- “Review the code.”
- “Continue to next phase.”

These are too vague for workflow handoff.

## Evidence format

Prefer tables when connecting files, obligations, and source artifacts.

Example:

| File | Change | Reason | Source artifact |
|---|---|---|---|
| `InvitationService.kt` | Add acceptance validation | Plan obligation: validate pending invitation | `PLAN.md`, `ARCHITECTURE.md` |

## Next-step clarity

The next step must say:

- which phase/tool should run next
- what target artifact/diff it should use
- why that is the next action
- what blocks that action, if anything
- suggested prompt
