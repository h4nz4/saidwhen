---
name: wiki-explore
description: Consult the project's saidwhen knowledge bundle (knowledge/) before planning, proposing, or asking the user anything. Use at the start of any feature evaluation, design discussion, or requirements question — and whenever a request might touch a recorded decision.
---

# wiki-explore

This project keeps decision provenance in an OKF bundle at `knowledge/`.

Read `behaviors/read-first.md` in this repo if present; otherwise (or if this
skill is installed globally) apply these rules, verbatim from saidwhen
read-first v0.1:

1. Read `knowledge/index.md` first. Follow links relevant to the current task
   (decisions, interviews, constraints). Read what's relevant, not the whole
   bundle.
2. Never ask the human a question the wiki already answers — cite the
   answering file instead.
3. When the task touches an accepted `Decision` with current evidence:
   respect it, cite it, do not re-litigate. When its evidence may be stale:
   ask only the delta question — "decided on <date> because <evidence>; is
   that still true?" — never silently obey or override.
4. When the wiki is silent on the topic, say so and question normally. Never
   cite documents that do not exist.

After exploring, if decisions crystallize, use the wiki-capture skill.
