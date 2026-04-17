# QUALITY_BAR

A good implementation under this skill is:
- faithful to one approved plan
- bounded in scope
- correct in behavior
- consistent with repository patterns
- validated against the plan
- transparent about deviations or blockers
- ready for independent review with minimal confusion

It is not enough that the code compiles or tests pass.
The implementation should also:
- fulfill the plan objective
- respect in-scope / out-of-scope boundaries
- satisfy the detailed specification
- avoid unrelated changes

A weak implementation usually shows one of these failures:
- partial objective fulfillment
- silent scope expansion
- hidden deviation from the plan
- missing tests or weak validation
- unrelated refactor mixed in
- unresolved blocker ignored instead of escalated
