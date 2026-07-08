# The Provenance Convention (v0.1)

A convention for giving AI-assisted development a **why layer**: every requirement
traces to the decision that created it, and every decision traces to the human
answer that justified it. Built on the
[Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md).
Just markdown. No runtime, no database, no server.

## Layout

```
knowledge/            ← an OKF bundle
├── index.md          ← entry point; agents read this FIRST
├── log.md            ← append-only chronological history
├── decisions/        ← type: Decision
├── interviews/       ← type: Interview (Q&A with a human, dated)
├── constraints/      ← type: Constraint (facts that bound the design)
├── domain/           ← type: Term (project glossary)
└── systems/          ← type: Component (architecture notes)
```

## Documents

Each concept is one markdown file with YAML frontmatter. Per OKF, `type` is the
only required field. Recommended: `title`, `description`, `timestamp`, `tags`.

`Decision` documents additionally use:

- `status:` `accepted` | `superseded` | `revisit`
- A `## Rejected` section naming discarded alternatives and why.

## Linking rules (the provenance chain)

```
spec requirement  ──why?──▶  Decision  ──who said?──▶  Interview / Constraint
```

1. A **Decision MUST link to its evidence** — the interview answer, constraint,
   or external source that justified it. A decision with no evidence link is
   an opinion, not a decision.
2. A **spec requirement SHOULD link to the Decision** that produced it
   (plain markdown link in the requirement text or a `<!-- why: -->` comment).
3. Links are ordinary relative markdown links. Broken links are convention
   violations (see `scripts/validate.py`).

## Behaviors

Conventions are inert without behavior. Agents working in a repo that follows
this convention MUST follow [behaviors/read-first.md](behaviors/read-first.md):
consult the wiki before planning or asking, capture new decisions on exit,
challenge stale facts instead of silently obeying or re-litigating them.

## Log discipline

Every write to the bundle appends one line to `log.md`:
`YYYY-MM-DD  <path>  <created|updated|superseded>  <one-line reason>`.
