# Behavior: capture-on-decision

You are working in a project that keeps its decision provenance in an OKF
bundle at `knowledge/`. When knowledge crystallizes, record it.

## When a decision crystallizes

1. Write `knowledge/decisions/<slug>.md` with `type: Decision`,
   `status: accepted`, a `timestamp`, a `## Rejected` section (with revisit
   triggers where they exist), and a link to its evidence (interview answer,
   constraint, or source).
2. If the human gave you new answers, record them in
   `knowledge/interviews/<date>-<topic>.md` with `type: Interview`.
3. Append one line to `knowledge/log.md`:
   `YYYY-MM-DD  <path>  <created|updated|superseded>  <one-line reason>`.
4. Add the new concept to `knowledge/index.md` if it's load-bearing.

## When superseding a decision

Never delete or silently contradict a recorded decision. Set the old
document's `status: superseded`, link it to its successor, record the new
evidence, and log the supersession.

## When work completes

Distill: which decisions from this session deserve to outlive it? Capture
those; let the rest evaporate. The wiki is a curated library, not a transcript.
