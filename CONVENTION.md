# The saidwhen Convention — v0.1

A convention for giving AI-assisted development a **why layer**: every
requirement traces to the decision that created it, and every decision traces
to the human answer that justified it — with a timestamp, so an agent can ask
the only question that matters later: *"you said that then; is it still true?"*

Built on the [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md).
Just markdown. No runtime, no database, no server. Validated experimentally —
see [evidence/VALIDATION.md](evidence/VALIDATION.md).

## Layout

```
docs/knowledge/       ← an OKF bundle
├── index.md          ← entry point; agents read this FIRST
├── log.md            ← append-only chronological history
├── decisions/        ← type: Decision
├── interviews/       ← type: Interview (Q&A with a human, dated)
├── constraints/      ← type: Constraint (facts that bound the design)
├── domain/           ← type: Term (project glossary)
└── systems/          ← type: Component (architecture notes)
```

Only `index.md`, `log.md`, and `decisions/` are required for conformance; the
other directories exist when there is content for them.

## Documents

Each concept is one markdown file with YAML frontmatter. Per OKF, `type` is
the only required field.

| Field | Required | Meaning |
|---|---|---|
| `type` | yes | `Decision`, `Interview`, `Constraint`, `Term`, `Component`, `Index`, `Log` |
| `title` | recommended | human-readable name |
| `description` | recommended | one-line summary |
| `timestamp` | recommended (Decisions: required) | ISO 8601; when the content was last true |
| `status` | Decisions only | `accepted` \| `superseded` \| `revisit` |
| `tags` | optional | array, for categorization |
| `resource` | optional | URL to the thing described (per OKF) |

## Linking rules (the provenance chain)

```
spec requirement  ──why?──▶  Decision  ──who said?──▶  Interview / Constraint
```

1. A **Decision MUST link to its evidence** — the interview answer, constraint,
   or external source that justified it. A decision with no evidence link is
   an opinion, not a decision.
2. A **spec requirement SHOULD link to the Decision** that produced it
   (plain markdown link in the requirement text).
3. Links are ordinary relative markdown links. Broken links are conformance
   violations.

## Decision lifecycle

- **`accepted`** — in force. Agents respect it and cite it; they do not
  re-litigate it while its evidence is current.
- A Decision SHOULD carry a `## Rejected` section naming the discarded
  alternatives, why, and a **revisit trigger** — the observable condition
  under which the decision should be reopened.
- **`revisit`** — the trigger appears to have fired or the evidence has aged;
  the decision awaits a human answer to its delta question.
- **`superseded`** — replaced. **Supersession preserves history**: the old
  document stays in the bundle with `status: superseded` and a link to its
  successor. Deleting a superseded decision is a conformance violation —
  the graph's value is that rejected paths stay visible.

## Log discipline

Every write to the bundle appends one line to `log.md`:
`YYYY-MM-DD  <path>  <created|updated|superseded>  <one-line reason>`.

## Conformance

A bundle conforms to saidwhen v0.1 iff:

1. Every `.md` document has YAML frontmatter with a `type` field.
2. Every relative markdown link resolves to an existing file.
3. Every `type: Decision` document links to at least one evidence document
   and has a `timestamp`.
4. `index.md` exists and links the load-bearing concepts.
5. `log.md` exists and is append-only.

Rules 1–3 are machine-checked by [validator/validate.py](validator/validate.py);
rules 4–5 are reviewed by humans (or the gc behavior). A conformant bundle is
also a valid OKF bundle.

## Behaviors

Conventions are inert without behavior. Agents working in a saidwhen repo
follow [behaviors/read-first.md](behaviors/read-first.md) (consult before
asking; challenge stale decisions with the delta question; never fabricate
provenance) and [behaviors/capture.md](behaviors/capture.md) (record decisions
at the moment they crystallize). Periodic curation: [behaviors/gc.md](behaviors/gc.md).

## Versioning

This document is versioned; v0.1 is intentionally minimal. Amendments follow
the process in [CONTRIBUTING.md](CONTRIBUTING.md) and MUST stay
backward-compatible within a major version: a bundle conformant to v0.1
remains conformant to every later v0.x.
