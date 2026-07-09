---
name: wiki-opsx-archive
description: Archive a completed OpenSpec change, harvest its crystallized knowledge into the saidwhen wiki as attributed facts and decisions, and update the Component pages the change altered. Use instead of plain archive when the project has a docs/knowledge/ bundle.
---

# wiki-opsx-archive

Run the standard OpenSpec archive flow, then **harvest before you forget**:

1. Read the change's `design.md` (Decisions section) and `proposal.md`.
2. For each decision that should outlive the change, apply the capture rules
   below. **Evidence must live in the bundle — never link into
   `openspec/changes/`**: archived changes move (and are often gitignored),
   so those paths are ephemeral. If the decision's evidence was a
   conversation during this change, distill it into attributed fact
   documents (`source:` + `timestamp:`) rather than pointing at change
   artifacts.
3. Harvest is distillation: a 10-task change usually yields 1–3 durable
   decisions, not 10.
4. Update the architecture pages the change altered — rules below.

Capture rules — verbatim from saidwhen capture v1.0 (normative source:
`behaviors/capture.md`; CI keeps this copy in sync):

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

Component upkeep rules — verbatim from saidwhen component-upkeep v1.0
(normative source: `behaviors/component-upkeep.md`; CI keeps this copy in
sync):

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

Finally, run the validator on the bundle (`scripts/validate.py` bundled with
the wiki-capture skill, or `validator/validate.py` in the saidwhen repo);
the bundle must pass.

## Optional: enforce the harvest automatically (Claude Code)

Relying on the agent to remember the harvest is the failure mode. The bundled
[`scripts/wiki-after-openspec.py`](scripts/wiki-after-openspec.py) closes the
loop with a Stop hook: if a change was archived more recently than
`docs/knowledge/log.md` was touched, it blocks stop with a one-line nudge to
harvest, and clears itself the moment you do. It stays **silent** — and costs
zero tokens — whenever the wiki is already current, so it only ever speaks up
when the wiki has actually fallen behind the specs.

Install: copy the script into `.claude/hooks/` and register it in
`.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      { "matcher": "", "hooks": [
        { "type": "command", "command": "python .claude/hooks/wiki-after-openspec.py" }
      ] }
    ]
  }
}
```

The hook needs no arguments and no dependencies — stdlib Python, reading the
repo from the working directory. It degrades to silence in any repo without a
`docs/knowledge/` wiki or an `openspec/changes/archive/`, so it is safe to
leave installed globally. Agents other than Claude Code can run the same
script from whatever end-of-turn mechanism they expose.
