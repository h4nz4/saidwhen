# Behavior: component-upkeep

Curated architecture pages (`docs/knowledge/systems/`, `type: Component`)
describe how the system hangs together and why. They are updated at the
moment reality changes — not discovered stale months later.

<!-- saidwhen:behavior component-upkeep v1.0 -->
## When a change lands

1. When an archived or completed change alters what a Component page
   describes, update that page in the same pass: state what changed and
   why, linking the driving decision where one exists.
2. Append one line to `docs/knowledge/log.md` for each updated page.
3. If the change touches load-bearing architecture no Component page
   describes yet, create the page (`type: Component`, with `source` and
   `timestamp` when it records a human's stated intent).

## Rules

- Component pages record curated knowledge — how it hangs together and
  why — not restatements of what the code plainly shows.
- A Component page you cannot verify against reality is flagged for
  review, not guessed at.
<!-- /saidwhen:behavior component-upkeep -->
