# saidwhen

> Your AI already interviewed you. Stop letting it forget the answers.

**saidwhen** gives AI-assisted development a *why layer*: every requirement
traces to the **decision** that created it, and every decision traces to the
**human answer** — with a timestamp — that justified it. All of it is plain
markdown in your repo, in [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md):
no server, no database, no vector index, no SDK.

```
 spec requirement          decision                 human answer
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ "MUST use magic  │────▶│ chose magic links│────▶│ Q: SSO needed?   │
│  link login"     │ why?│ over OAuth       │ who │ A: "no, users are│
│                  │     │ because...       │said?│  external, no    │
└──────────────────┘     └──────────────────┘     │  IdP" —ivan      │
                                                  └──────────────────┘
```

Six months later someone asks "can we add OAuth?" — the agent follows the
links, finds it was rejected and why, and asks only: *"decided 2026-07-08
because users have no IdP — is that still true?"* No re-litigating, no
re-interviewing, no blind obedience. That's the delta question — the *said
when* — and it's the behavior this repo exists to produce.

## It measurably works

Every claim below is backed by pre-registered experiments with published
transcripts — 54 scored runs, three rounds, zero rubric exceptions.

| Claim | Evidence | Result |
|---|---|---|
| Recalls rejected features instead of re-planning them | [round 1](evidence/experiment/results.md) | 6/6 vs control 0/6, p ≈ 0.0011 |
| Reopens stale decisions via their own revisit triggers — no blind obedience | [rounds 2+3](evidence/experiment/round3/results.md) | 6/6 vs 0/6, p ≈ 0.0011 |
| Shapes ordinary proposals around recorded constraints | [rounds 2+3](evidence/experiment/round3/results.md) | 6/6 vs 0/6, p ≈ 0.0011 |
| Handles uncovered topics without fabricating provenance | [round 3](evidence/experiment/round3/results.md) | 6/6 vs 0/6, p ≈ 0.0011; 9/9 clean on the fabrication probe |
| Same behavior when delivered as an auto-triggering skill — on two different agent CLIs | [round 4](evidence/experiment/round4-skill-trigger/results.md) | 36/36 runs pass both rubrics; skill auto-triggered 24/24 |

Full write-up: [evidence/VALIDATION.md](evidence/VALIDATION.md). Honest
limitations included (single model family, demo-sized wikis, unblinded
scoring with published raw outputs).

## Quickstart (5 minutes)

1. Install the skills: copy directories from [skills/](skills/) into your
   agent's skills folder — `.claude/skills/` (Claude Code), `.agents/skills/`
   (Codex), or your agent's equivalent
   ([install matrix](skills/README.md)). Minimal set: `wiki-init`,
   `wiki-explore`, `wiki-capture`.
2. Ask your agent to set up provenance — `wiki-init` scaffolds `knowledge/`
   and offers the [AGENTS.md snippet](skills/wiki-init/assets/snippet.md), the
   ambient fallback for agents without Agent Skills support.
3. Work normally. Your agent now reads `knowledge/` before asking you
   anything, and writes decisions when they crystallize.

Optional: vendor [validator/validate.py](validator/validate.py) (one stdlib
file) and run `python validate.py knowledge` in CI — the wiki-capture skill
also bundles it. OpenSpec user? Install the `wiki-opsx-*` skills — explore
consults the wiki first, archive harvests decisions into it.

## What's in the box

| Layer | What | Where |
|---|---|---|
| **L1 Convention** | Bundle layout, concept types, linking rules, decision lifecycle. One page, versioned. | [CONVENTION.md](CONVENTION.md) |
| **L2 Behaviors** | Tool-agnostic prompts: [read-first](behaviors/read-first.md), [capture](behaviors/capture.md), [gc](behaviors/gc.md). The validated wording. | [behaviors/](behaviors/) |
| **L3 Skills** | Drop-in [Agent Skills](https://agentskills.io/home) (open standard, any supporting agent): init, explore, capture, gc, OpenSpec pack. The ambient [AGENTS.md snippet](skills/wiki-init/assets/snippet.md) ships inside wiki-init as the fallback. | [skills/](skills/) |
| Demo | TaskLite — browse a working provenance chain on GitHub. | [example/](example/) |
| Validator | Frontmatter, links, decision-evidence rule. Stdlib, one file. | [validator/](validator/) |
| Proof | Protocols, 54 raw transcripts, scoring, statistics. | [evidence/](evidence/) |

## How it's different from agent-memory tools

Memory tools capture **everything ambiently** (transcripts, embeddings) and
hope retrieval finds the needle. saidwhen captures **at the moment of
decision** — the point of highest signal — and links it into a graph a human
can browse on GitHub. It is a format and a behavior, not a platform: produced
without an SDK, consumed without an integration, portable between agents, and
it degrades gracefully to well-organized docs.

## License

[MIT](LICENSE). Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md),
especially the rule about re-validating behavior edits.
