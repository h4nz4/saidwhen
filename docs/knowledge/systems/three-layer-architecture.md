---
type: Component
title: Three-layer architecture
description: How saidwhen hangs together — canonical bundle, behavior/skill layer, compiled presentation — and why the layers never blur.
timestamp: 2026-07-08T20:30:00Z
tags: [architecture]
---

# Three-layer architecture

```mermaid
flowchart LR
    subgraph L1 [Bundle — source of truth]
        B["docs/knowledge/<br>facts · decisions · terms · components"]
    end
    subgraph L2 [Behavior — how agents use it]
        BH[behaviors/*.md] -->|verbatim embeds,<br>CI-guarded| SK[skills/*]
    end
    subgraph L3 [Presentation — compiled, disposable]
        R[render/wiki_render.py] --> S[static wiki site]
    end
    SK -->|read-first / capture| B
    B --> R
    OS[OpenSpec changes] <-->|context in,<br>knowledge out| SK
    V[validator/validate.py] -.->|conformance,<br>docs-rot, diff check| B
```

**Why three layers.** The bundle stays small because agents pay to read it
on every task — richness would tax every session
([why](../decisions/okf-wiki-pivot.md)). Behaviors are the validated
wording; skills are delivery vehicles that embed it verbatim so there is
exactly one normative source ([why](../decisions/skills-first-distribution.md)).
Presentation is compiled and disposable — regenerated, never maintained —
so human-grade richness costs nothing at agent-read time.

**The load-bearing rule:** nothing flows upward. Rendered pages never feed
the bundle; skills never fork behavior wording; the bundle never stores
what code or a render pass can derive.
