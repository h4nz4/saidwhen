## 1. Repo restructure

- [x] 1.1 Initialize git repository at E:\PROJEKTI\okf (repo is not yet under version control) and make an initial commit of the current state as the pre-restructure baseline
- [x] 1.2 Create `evidence/` and move `experiment/`, `example-control/`, `example-stale/`, `example-stale-control/`, and `VALIDATION.md` into it intact
- [x] 1.3 Fix relative links broken by the move (VALIDATION.md → experiment paths, README → VALIDATION path, results files → fixture paths)
- [x] 1.4 Create `validator/` and move `scripts/validate.py` to `validator/validate.py`; update the reproduce instructions in evidence/VALIDATION.md

## 2. Convention v0.1

- [x] 2.1 Revise CONVENTION.md into the versioned v0.1 spec: add conformance criteria, decision lifecycle (`accepted`/`superseded`/`revisit`, supersession preserves history), and frontmatter field table
- [x] 2.2 Verify example/ bundle conforms to the final wording (run validator; supersession rule needs no fixture change but check log.md discipline)

## 3. Behaviors

- [x] 3.1 Split behaviors/read-first.md into read-first.md (recall + staleness delta) and capture.md (decision/interview writing + log discipline), preserving validated wording verbatim
- [x] 3.2 Write behaviors/gc.md (merge duplicates, flag decisions past revisit triggers, repair links, log every change)
- [x] 3.3 Add the no-fabrication rule explicitly to read-first.md (currently implicit; wording addition only, additive per design D2)

## 4. Validator hardening

- [x] 4.1 Add argparse CLI (bundle dir arg, `--strict` reserved), keep single-file stdlib-only
- [x] 4.2 Write validator/test_validate.py: pass case, missing-type, broken-link, evidence-less-decision, BOM fixture — pytest-compatible, unittest-runnable
- [x] 4.3 Run tests on Windows and confirm exit codes

## 5. Adapters

- [x] 5.1 Write adapters/agents-md/: snippet embedding read-first + capture, 3-step install instructions
- [x] 5.2 Write adapters/claude-code/: wiki-explore, wiki-capture, wiki-gc skills (SKILL.md each) referencing behaviors content, plus install note
- [x] 5.3 Document the adapter sync rule (single source of behavior truth) in each adapter README
- [x] 5.4 Write adapters/openspec/: skill pack wrapping explore/propose/archive with wiki read + harvest (cuttable to fast-follow if it delays release)

## 6. Public surface

- [x] 6.1 Rewrite README.md for the public audience under the name **saidwhen**: pitch, diagram, 5-minute AGENTS.md quickstart, layer overview, evidence table with claim→file links
- [x] 6.2 Add LICENSE (MIT) and CONTRIBUTING.md (convention amendment process, behavior-edit re-validation rule, adapter how-to)
- [x] 6.3 Add .github/workflows/ci.yml: validator tests, validate example/knowledge, link-check README.md and CONVENTION.md

## 7. Verification

- [x] 7.1 Run the full local check: validator tests green, example bundle validates, all README/CONVENTION/VALIDATION links resolve
- [x] 7.2 Fresh-eyes pass: follow the quickstart verbatim in a scratch project and confirm a wiki-aware agent session works end to end (agent captured decision+interview+log+index from AGENTS.md snippet alone; bundle validates: 4 documents, 0 errors)
- [x] 7.3 Re-run one treatment scenario (round-1 prompt) against the restructured repo to confirm the moved behaviors still produce a passing run (PASS on all rubric criteria; transcript in session scratchpad regression-run-1.md)
