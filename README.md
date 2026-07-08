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

Full write-up: [evidence/VALIDATION.md](evidence/VALIDATION.md). Honest
limitations included (single model family, demo-sized wikis, unblinded
scoring with published raw outputs).

## Quickstart (5 minutes)

1. Create the bundle skeleton in your repo — copy
   [example/knowledge/](example/knowledge/) and empty it, keeping `index.md`
   and `log.md`.
2. Paste [adapters/agents-md/snippet.md](adapters/agents-md/snippet.md) into
   your project's `AGENTS.md` (or `CLAUDE.md`).
3. Work normally. Your agent now reads `knowledge/` before asking you
   anything, and writes decisions when they crystallize.

Optional: vendor [validator/validate.py](validator/validate.py) (one stdlib
file) and run `python validate.py knowledge` in CI.

Claude Code user? Use the [skills adapter](adapters/claude-code/). OpenSpec
user? Use the [reference integration](adapters/openspec/).

## What's in the box

| Layer | What | Where |
|---|---|---|
| **L1 Convention** | Bundle layout, concept types, linking rules, decision lifecycle. One page, versioned. | [CONVENTION.md](CONVENTION.md) |
| **L2 Behaviors** | Tool-agnostic prompts: [read-first](behaviors/read-first.md), [capture](behaviors/capture.md), [gc](behaviors/gc.md). The validated wording. | [behaviors/](behaviors/) |
| **L3 Adapters** | Thin bindings: [AGENTS.md snippet](adapters/agents-md/), [Claude Code skills](adapters/claude-code/), [OpenSpec pack](adapters/openspec/). | [adapters/](adapters/) |
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
