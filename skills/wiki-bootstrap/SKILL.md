---
name: wiki-bootstrap
description: Populate a project's saidwhen wiki (docs/knowledge/) from the existing codebase — generate curated architecture (Component) pages with diagrams, a domain glossary, and a use-cases index, without inventing rationale. Use after wiki-init on a project that already has code and history, or when the user asks to generate architecture documentation or an initial knowledge base.
---

# wiki-bootstrap

This project's wiki — an OKF bundle at `docs/knowledge/` — is its memory:
knowledge the code can't express, kept trustworthy by built-in provenance.
This skill fills an empty (or thin) wiki from a project that already
exists. Apply these rules — verbatim from saidwhen bootstrap v1.0
(normative source: `behaviors/bootstrap.md`; CI keeps this copy in sync):

<!-- saidwhen:behavior bootstrap v1.0 -->
## The pass

1. **Survey before writing.** Read the README, docs, specs, commit history,
   and code structure. List candidate knowledge: architecture worth a
   Component page, recurring project vocabulary worth a Term, constraints
   and decisions the project clearly operates under.
2. **Write few, load-bearing pages.**
   - `systems/` — Component pages for how the system hangs together and
     why, with a diagram where structure warrants one (Mermaid renders on
     GitHub). Curated knowledge, not restatements of what the code plainly
     shows.
   - `domain/` — Terms for the project's own vocabulary.
   - `index.md` — a use-cases section: what the project is for, each case
     linked to the mechanism that serves it.
3. **Never invent a why.** Record rationale only where evidence exists — a
   doc, a commit message, an issue, a human answer — and link it. Where a
   reason is undiscoverable, record an open question / capture target: an
   honest gap beats fabricated provenance.
4. **No unattributed facts, no bootstrap decisions.** Documents with
   `source:` come only from human answers. Candidate decisions discovered
   in the code are listed as questions for the owner, never written as
   `status: accepted`.
5. **Propose, then review.** Present the generated pages to the human for
   correction before treating them as trusted. Log every file in `log.md`,
   add load-bearing entries to `index.md`, and run the validator — the
   bundle must pass.
<!-- /saidwhen:behavior bootstrap -->

The open questions this pass produces are interview material: when the
owner answers them, capture the answers as attributed facts (wiki-capture)
— that is how the bootstrap's gaps become provenance instead of staying
holes.
