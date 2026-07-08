## Context

The working directory holds a validated PoC: CONVENTION.md, one behavior file,
a stdlib validator, four TaskLite fixtures (treatment + three controls), and
54 experiment transcripts across three pre-registered rounds. The hypothesis is
proven; nothing is packaged. Target audience: developers using AI coding
assistants who have never heard of OpenSpec or OKF — the repo must land in one
README read and install in minutes. Constraints: solo-maintainable, zero
runtime dependencies (the anti-agentmemory positioning is load-bearing),
vendor-neutral per OKF's ethos.

## Goals / Non-Goals

**Goals:**
- Publishable repo layout with the three-layer architecture explicit:
  convention (L1) → behaviors (L2) → adapters (L3).
- 5-minute quickstart: copy a snippet, agent starts reading/writing the wiki.
- Evidence as differentiator: experiments browsable, reproducible, linked
  from the README claims.
- CI that keeps the example bundle and validator honest.

**Non-Goals:**
- No MCP server, vector search, embeddings, or visualizer (Google ships one;
  link it). No new dependencies.
- No cross-model replication in this change (documented as future work).
- No npm/pip packaging — the validator stays a single file you vendor.
- No changes to experiment artifacts — evidence is immutable history; it
  moves, it is not edited.

## Decisions

**D1 — Repo layout: product at root, evidence quarantined.**
```
/                      README, CONVENTION, LICENSE, CONTRIBUTING
├── behaviors/         L2 prompts (read-first.md, capture.md, gc.md)
├── adapters/
│   ├── agents-md/     copy-paste snippet (lowest common denominator)
│   ├── claude-code/   skills: wiki-explore, wiki-capture, wiki-gc
│   └── openspec/      skill pack wrapping explore/propose/archive
├── example/           TaskLite with full provenance chain (unchanged)
├── validator/         validate.py + test_validate.py
├── evidence/          experiment/, example-control/, example-stale/,
│                      example-stale-control/, VALIDATION.md (moved intact)
└── .github/workflows/ ci.yml
```
Rationale: a first-time visitor must see product, not lab bench. Controls and
protocols are proof, so they stay in-repo — but one directory deep.
Alternative considered: separate evidence repo — rejected, splits the
differentiator from the pitch and doubles maintenance.

**D2 — Behaviors split into three files, composable.** `read-first.md` (recall
+ staleness delta rule), `capture.md` (decision/interview writing + log
discipline), `gc.md` (curation: merge duplicates, flag stale, fix links).
Rationale: adapters mix-and-match (a read-only CI reviewer wants read-first
only). The current single file already has these seams. The validated wording
of read-first is preserved verbatim where possible — it went 27/27; rewording
is risk with no upside.

**D3 — Adapters are thin pointers, not forks.** Each adapter contains only
tool-specific binding (frontmatter, trigger phrases, lifecycle hooks) and
references `behaviors/*.md` content by inclusion at install time (a small
install script or manual copy). Rationale: one source of truth; behavior fixes
propagate. Alternative: duplicated prompt text per adapter — rejected, rots.

**D4 — Validator becomes `validator/validate.py` with argparse and tests,
still stdlib-only, still one file.** Exit 0/1, `--strict` flag reserved for
future conformance levels. Tests are plain `pytest`-compatible functions but
runnable with `python -m unittest` fallback. Rationale: keep the "vendor this
one file" story while making CI meaningful.

**D5 — CI: GitHub Actions, one workflow.** Jobs: (1) validator self-tests,
(2) validate `example/knowledge`, (3) link-check README/CONVENTION. Rationale:
the repo's core promise is machine-checkable convention; CI is the public
demonstration of that.

**D6 — README claims map 1:1 to evidence links.** Every quantitative claim
("never re-asks", "6/6 vs 0/6", "p ≈ 0.0011") links to the protocol/results
file that backs it. Rationale: falsifiability is the brand; broken-link CI
keeps it true.

**D7 — License MIT.** Maximum adoption for a convention play; spec text and
prompts are the product, and forks that spread the convention are wins.

## Risks / Trade-offs

- [Evidence weight: fixtures + transcripts ≈ dozens of files] → quarantined in
  `evidence/`, excluded from the quickstart path; README links, never inlines.
- [Behavior rewording during split could break the validated 27/27 property]
  → wording preserved verbatim per D2; any semantic edit requires a re-run of
  the round-3 rubric before merge (documented in CONTRIBUTING).
- [Claude Code skill format churn] → adapters/claude-code kept minimal
  (SKILL.md + install note); AGENTS.md snippet is the stable fallback.
- [Solo-maintainer bus factor on curation of issues/PRs] → CONTRIBUTING sets
  expectations; convention is spec-frozen at v0.1 with amendment process.
- [Windows/Unix path and BOM quirks in validator] → already handles BOM;
  tests include a BOM fixture and a backslash-link case.

## Migration Plan

Pure file reorganization plus new files; no running system to migrate.
Order: create new dirs → git mv evidence pieces → update relative links in
moved files (VALIDATION.md paths) → run validator + link check → CI green.
Rollback: git revert (repo not yet public; no consumers).

## Open Questions

- ~~Final public repo name~~ **Resolved: `saidwhen`** (decided 2026-07-08).
  Verified zero exact-name collisions on GitHub; encodes the staleness
  delta-question ("said when?") that differentiates the convention. Rejected
  after availability checks: `provenance`, `lore`, `whygraph`, `saidso` (all
  taken), `hindsight` (18k-star agent-memory collision), `precedent`,
  `paper-trail`, `attest`, `chronicle`, `vouched` (prominent collisions).
- Whether the OpenSpec adapter ships in v0.1 or as fast-follow — included in
  tasks as last, cuttable without breaking the release.
