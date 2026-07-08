# Provenance — a "why layer" for AI-assisted development

> Your AI already interviewed you. Stop letting it forget the answers.

Every requirement traces to the **decision** that created it. Every decision
traces to the **human answer** that justified it. All of it is plain markdown
in your repo, in [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
— no server, no database, no vector index, no SDK.

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
re-interviewing, no blind obedience.

## What's here

| Path | What it is |
|------|-----------|
| [CONVENTION.md](CONVENTION.md) | The standard: layout, concept types, linking rules. One page. |
| [behaviors/read-first.md](behaviors/read-first.md) | The agent behavior: read wiki first, never re-ask, capture decisions. |
| [example/](example/) | A filled-in project (TaskLite) with a working provenance chain. |
| [scripts/validate.py](scripts/validate.py) | Bundle validator: frontmatter, links, decision-evidence rule. Stdlib only. |
| [VALIDATION.md](VALIDATION.md) | Pre-registered A/B experiments: 54 runs, 4 use cases, each independently p ≈ 0.0011 (< 0.005). |

## How it's different from agent-memory tools

Memory tools capture **everything ambiently** (transcripts, embeddings) and
hope retrieval finds the needle. This convention captures **at the moment of
decision** — the one point where the signal-to-noise ratio is highest — and
links it into a graph a human can browse on GitHub. It is a format and a
behavior, not a platform.

## Layers

1. **Convention** (OKF bundle layout + linking rules) — depends on nothing.
2. **Behaviors** (tool-agnostic prompts) — written against the convention.
3. **Adapters** (OpenSpec skill pack, Claude Code skills, AGENTS.md snippet)
   — bind behaviors to a tool's lifecycle moments. The wiki on disk is the
   contract; adapters never talk to each other.
