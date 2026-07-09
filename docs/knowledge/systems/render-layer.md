---
type: Component
title: Render layer
description: wiki_render.py compiles the bundle into disposable HTML views — why presentation is generated, never stored.
timestamp: 2026-07-08T20:30:00Z
tags: [architecture, render]
---

# Render layer

`render/wiki_render.py` (stdlib, one file) compiles a bundle into either a
single self-contained HTML page or a multi-page static site: index with
stats and the decision→evidence provenance graph, one page per document,
status badges, attribution chips, history timeline. CI renders the
project's own wiki on every push and publishes it as the `wiki-site`
artifact. Output is plain static HTML — hosting stays the user's choice
([why](../constraints/no-vendor-lock-in.md)).

**Why compiled, not stored:** rich pages rot and tax every agent read;
compiled views are dated, marked disposable, and regenerated for the cost
of a script run — zero LLM tokens
([why](../decisions/okf-wiki-pivot.md)). Every rendered page carries the
contract in its footer: the bundle is the source of truth; never edit
output.

**Known ceiling:** the embedded markdown renderer is minimal (headings,
lists, quotes, links, fenced code); Mermaid diagrams in bundle documents
render on GitHub and appear as code blocks in the HTML view — upgrade path
is bundling mermaid.js into the page if diagram-heavy wikis materialize.
