## ADDED Requirements

### Requirement: AGENTS.md snippet adapter
The repo SHALL provide `adapters/agents-md/` containing a copy-paste snippet
that binds the read-first and capture behaviors for any agent that reads
AGENTS.md-style instructions, with install instructions of at most three
steps.

#### Scenario: Tool-agnostic install
- **WHEN** a user pastes the snippet into their project's AGENTS.md and their
  agent starts a task
- **THEN** the agent reads `knowledge/index.md` before asking questions,
  without any other tooling installed

### Requirement: Claude Code skills adapter
The repo SHALL provide `adapters/claude-code/` with skills binding the
behaviors to Claude Code: a wiki-aware explore/plan skill (read-first), a
capture skill (capture-on-decision), and a gc skill (curation), each with
SKILL.md frontmatter and install instructions.

#### Scenario: Skill invocation
- **WHEN** a user installs the skills and invokes the capture skill after a
  decision is made in conversation
- **THEN** the skill writes conformant Decision/Interview documents and log
  entries per the capture behavior

### Requirement: Single source of behavior truth
Adapters SHALL reference or embed the `behaviors/*.md` content without forking
its normative wording; adapter files contain only tool-specific binding.

#### Scenario: Behavior fix propagates
- **WHEN** a wording fix lands in `behaviors/read-first.md`
- **THEN** no adapter contains a divergent copy of the old normative wording
  after the documented sync step is run

### Requirement: OpenSpec skill pack
The repo SHALL provide `adapters/openspec/` wrapping the OpenSpec lifecycle:
explore and propose consult the wiki first; archive harvests the change's
decisions into the bundle. This adapter is the reference integration and MAY
ship as a fast-follow if it would delay the initial release.

#### Scenario: Archive harvest
- **WHEN** a user archives an OpenSpec change using the skill pack
- **THEN** the change's crystallized decisions are captured as Decision
  documents linked to their evidence, and the bundle still validates
