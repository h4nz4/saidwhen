# The saidwhen Convention — v1.0

A convention for an **agent-maintained project wiki**: one OKF bundle of
plain markdown that serves three readers at once — agents (persistent
project memory across sessions), the spec workflow (the knowledge layer
specs draw on and feed), and humans (via compiled wiki views). Every entry
carries its integrity plumbing — who said it, when, and what would reopen
it — so the wiki can be trusted, challenged, and never silently rots.

Built on the [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md).
Just markdown. No runtime, no database, no server. The trust layer is
validated experimentally — see [evidence/VALIDATION.md](evidence/VALIDATION.md).

## Layout

```
docs/knowledge/       ← an OKF bundle: the project's wiki
├── index.md          ← entry point; agents read this FIRST
├── log.md            ← append-only chronological history
├── decisions/        ← type: Decision
├── constraints/      ← type: Constraint (attributed facts that bound the design)
├── domain/           ← type: Term (project glossary)
├── systems/          ← type: Component (curated architecture pages)
└── interviews/       ← type: Interview (legacy history; not produced by default)
```

Only `index.md`, `log.md`, and `decisions/` are required for conformance;
the other directories exist when there is content for them.

## What belongs in the wiki

Knowledge the code cannot express — facts, constraints, decisions, domain
meanings, intentions — **plus curated architecture** (Component pages
describing how the system hangs together and why). Nothing that a tool can
re-derive from source on demand: derived documentation rots, and compiled
views (see Render contract) cover presentation.

## Documents

Each concept is one markdown file with YAML frontmatter. Per OKF, `type` is
the only universally required field.

| Field | Required | Meaning |
|---|---|---|
| `type` | yes | `Decision`, `Constraint`, `Term`, `Component`, `Interview`, `Index`, `Log` |
| `title` | recommended | human-readable name |
| `description` | recommended | one-line summary |
| `timestamp` | Decisions and attributed facts: required | ISO 8601; when the content was last true |
| `source` | attributed facts: required | who said it (person or reference) |
| `status` | Decisions only | `accepted` \| `superseded` \| `revisit` |
| `tags` | optional | array, for categorization |
| `resource` | optional | URL to the thing described (per OKF) |
| `scope` | optional (Decisions only) | whitespace-separated fnmatch globs of the repo paths this decision governs; enables the diff check below |

## Fact-form capture

The default captured unit is an **attributed fact**: a distilled statement
in its own document with `source` (who said it) and `timestamp` (when said)
— no dialogue transcripts, no verbatim quotes. A Constraint is a fact that
bounds the design; a Term is a fact about meaning; a Component records
curated architecture knowledge. Any document carrying `source` MUST also
carry `timestamp` — an unattributed or undated fact cannot be challenged,
which makes it a rumor, not knowledge.

Interview documents remain valid as history and for the rare exchange whose
back-and-forth is itself the content, but capture does not produce them by
default.

## Linking rules (the integrity chain)

```
spec requirement  ──why?──▶  Decision  ──who said?──▶  attributed fact (Constraint/Term/Component)
```

1. A **Decision MUST link to its evidence** — an attributed fact, a legacy
   Interview, or an external source. A decision with no evidence link is
   an opinion, not a decision.
2. A **spec requirement SHOULD link to the Decision** that produced it
   (plain markdown link in the requirement text).
3. Links are ordinary relative markdown links. Broken links are conformance
   violations.
4. Evidence never links into ephemeral paths (e.g. `openspec/changes/`).

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
  the wiki's value is that rejected paths stay visible.

## Component upkeep contract

Curated architecture pages are the wiki's rot-prone asset, so their upkeep
has two named hooks:

- **At change time** — when an archived change alters what a Component page
  describes, the page is updated in the same pass, with a log line, linking
  the driving decision where one exists.
- **Periodically** — the curation pass audits Component pages against the
  current codebase; a page that no longer matches reality is **flagged for
  review** (status or log entry), never silently trusted and never silently
  rewritten.

## Render contract

The bundle is the single source of truth and stays small; presentation is
**compiled**. Rendered wiki views (HTML sites, graphs, tours) are
disposable artifacts: regenerated on demand or by CI, dated, clearly marked
as compiled views, and never hand-edited. Richness lives in the render
layer; storage stays cheap for the agents that read it on every task.

## OpenSpec interoperability

The wiki and [OpenSpec](https://github.com/Fission-AI/OpenSpec) form one
loop:

- **In (proposal time):** exploring or proposing a change consults the wiki
  first and pulls the relevant Terms, Constraints, Components, and
  Decisions into the proposal's context, by link.
- **Out (archive time):** archiving a change writes crystallized knowledge
  back — attributed facts and Decisions — and updates the Component pages
  the change altered.
- **Both directions are machine-checked:** spec why-links are validated
  (resolution + superseded-citation detection), and the diff check maps
  changed paths back to the Decisions that govern them.

## Log discipline

Every write to the bundle appends one line to `log.md`:
`YYYY-MM-DD  <path>  <created|updated|superseded>  <one-line reason>`.

## Conformance

A bundle conforms to saidwhen v1.0 iff:

1. Every `.md` document has YAML frontmatter with a `type` field.
2. Every relative markdown link resolves to an existing file.
3. Every `type: Decision` document links to at least one evidence document
   and has a `timestamp`.
4. Every document carrying `source` also carries `timestamp`.
5. `index.md` exists and links the load-bearing concepts.
6. `log.md` exists and is append-only.

Rules 1–4 are machine-checked by [validator/validate.py](validator/validate.py);
rules 5–6 are reviewed by humans (or the gc behavior). A conformant bundle
is also a valid OKF bundle. A bundle conformant to v0.1 still validates —
v1.0 adds acceptance (fact evidence), not new obligations on old documents.

The validator also offers an advisory **diff check**: given the paths a
change touches, it reports which Decisions govern them (via their `scope`
globs), so a PR review — human or agent — starts from the recorded why
instead of rediscovering it:

```
git diff --name-only main | python validate.py docs/knowledge --check-diff -
WHY   decisions/eur-only.md (accepted) governs: index.html
```

Advisory means advisory: hits never fail validation, and decisions without
`scope` simply don't participate.

## Migrating a v0.1 bundle

Nothing moves and nothing breaks:

- Existing Interview documents stay where they are — they remain valid
  evidence and readable history.
- Existing Decisions keep validating; their interview evidence links stay
  legal.
- Going forward, capture produces attributed facts (Constraint/Term/
  Component with `source` + `timestamp`) instead of transcripts, and new
  Decisions link to those.
- Optional: add `scope` globs to decisions you want the diff check to
  watch.

## Behaviors

Conventions are inert without behavior. Agents working in a saidwhen repo
follow [behaviors/read-first.md](behaviors/read-first.md) (the wiki is
project memory: consult before asking or spelunking code; challenge stale
decisions with the delta question; never fabricate provenance) and
[behaviors/capture.md](behaviors/capture.md) (record knowledge as
attributed facts at the moment it crystallizes). Populating a fresh wiki from an existing
project: [behaviors/bootstrap.md](behaviors/bootstrap.md). Architecture
upkeep: [behaviors/component-upkeep.md](behaviors/component-upkeep.md).
Periodic curation: [behaviors/gc.md](behaviors/gc.md).

## Versioning

This document is versioned. v1.0 is a clean break from v0.x — it re-centers
the convention on the wiki, makes fact-form capture the default, and adds
the Component-upkeep and render contracts ([why](docs/knowledge/decisions/okf-wiki-pivot.md)).
Amendments follow the process in [CONTRIBUTING.md](CONTRIBUTING.md) and
MUST stay backward-compatible within a major version: a bundle conformant
to v1.0 remains conformant to every later v1.x.
