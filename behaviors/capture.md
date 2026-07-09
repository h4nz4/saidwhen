# Behavior: capture

You are working in a project whose wiki — an OKF bundle at
`docs/knowledge/` — is the project's memory. When knowledge crystallizes,
record it as attributed facts.

<!-- saidwhen:behavior capture v1.0 -->
## When knowledge crystallizes

1. Record each settled human answer as an **attributed fact**: a distilled
   statement in `docs/knowledge/constraints/<slug>.md` (a fact that bounds
   the design), `domain/<slug>.md` (a fact about meaning), or
   `systems/<slug>.md` (curated architecture), with `source:` (who said
   it) and `timestamp:` (when). No dialogue transcripts, no verbatim
   quotes — the distilled statement itself, attributed and dated.
2. When a decision crystallizes, write `docs/knowledge/decisions/<slug>.md`
   with `type: Decision`, `status: accepted`, a `timestamp`, a
   `## Rejected` section (with revisit triggers where they exist), and a
   link to its evidence — the attributed fact(s) or an external source.
3. Append one line to `docs/knowledge/log.md`:
   `YYYY-MM-DD  <path>  <created|updated|superseded>  <one-line reason>`.
4. Add the new concept to `docs/knowledge/index.md` if it's load-bearing.

## When superseding a decision

Never delete or silently contradict a recorded decision. Set the old
document's `status: superseded`, link it to its successor, record the new
evidence, and log the supersession.

## When work completes

Distill: which knowledge from this session deserves to outlive it? Capture
that; let the rest evaporate. The wiki is a curated library, not a
transcript.
<!-- /saidwhen:behavior capture -->
