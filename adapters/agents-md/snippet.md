<!-- saidwhen: decision provenance (https://github.com/<owner>/saidwhen) -->
<!-- Embeds behaviors/read-first.md and behaviors/capture.md v0.1 — edit there, not here. -->

# Project knowledge (saidwhen)

This project keeps its decision provenance in an OKF bundle at `knowledge/`.
Follow these rules.

## Before planning or asking anything

1. Read `knowledge/index.md`. Follow links relevant to your current task
   (decisions, interviews, constraints). Budget: read what's relevant, not
   the whole bundle.
2. **Never ask the human a question the wiki already answers.** If an
   interview or constraint answers it, cite the file and move on.
3. When your task touches an existing `Decision`:
   - `status: accepted` and its evidence still plausible → respect it. Do not
     re-litigate. Cite it.
   - Evidence may be stale (old timestamp, changed circumstances) → do NOT
     silently obey and do NOT silently override. Ask the human only the
     **delta question**: "this was decided on <date> because <evidence>;
     is that still true?"

If the bundle contains nothing about your topic, say so and proceed with
normal questioning. Never cite a decision, interview, or constraint that does
not exist.

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

Never delete or silently contradict a recorded decision — supersede it
(`status: superseded`, link to successor, log it).
