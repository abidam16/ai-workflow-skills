# Split Rules

Split into multiple plans if any of these are true:

- more than one primary objective exists
- the work changes multiple unrelated user flows or domains
- the work combines feature delivery with broad refactor or migration work
- success would be judged by more than one unrelated validation path
- reviewers would need to check clearly different concerns
- the implementation would naturally produce multiple commit themes
- the plan contains repeated “and also” scope clauses

## Practical test

A plan is probably still single-task if:
- one engineer or one implementation agent could explain the task in one sentence
- it has one main acceptance target
- it is reviewable as one coherent unit

A plan is probably too broad if:
- it needs several “mini plans” inside the document
- it touches unrelated bounded contexts
- it would be easier to approve in pieces than as one whole
