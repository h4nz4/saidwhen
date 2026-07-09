# Behavior: bootstrap (populate a wiki from an existing project)

When a project adopts saidwhen with history already in place, the wiki
starts empty. This pass generates the initial content — proposing, never
inventing.

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
