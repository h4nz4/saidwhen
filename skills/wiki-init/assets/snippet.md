<!-- saidwhen: decision provenance (https://github.com/<owner>/saidwhen) -->
<!-- Embeds behaviors/read-first.md and behaviors/capture.md v1.0 — edit there, not here. -->

# Project wiki (saidwhen)

This project keeps its decision provenance in an OKF bundle at `docs/knowledge/`.
Follow these rules.

<!-- saidwhen:behavior read-first v1.0 -->
## Before planning, asking, or spelunking code

1. Read `docs/knowledge/index.md`. Follow links relevant to your current
   task (decisions, constraints, terms, components). Budget: read what's
   relevant, not the whole bundle — and read it BEFORE deriving project
   context from source files.
2. **Never ask the human a question the wiki already answers.** If a
   recorded fact or constraint answers it, cite the file and move on.
3. When your task touches an existing `Decision`:
   - `status: accepted` and its evidence still plausible → respect it. Do not
     re-litigate. Cite it.
   - Evidence may be stale (old timestamp, changed circumstances) → do NOT
     silently obey and do NOT silently override. Ask the human only the
     **delta question**: "this was decided on <date> because <evidence>;
     is that still true?"

## When the wiki is silent

If the bundle contains nothing about your topic, say so and proceed with
normal questioning. **Never cite a decision, fact, or constraint that does
not exist**, and never claim the wiki answers what it does not. Recorded
constraints that genuinely apply to the new topic still apply.
<!-- /saidwhen:behavior read-first -->

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
