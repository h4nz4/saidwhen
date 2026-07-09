---
name: wiki-render
description: Compile the project's saidwhen knowledge bundle (docs/knowledge/) into a browsable static HTML wiki — index with provenance graph plus one page per document. Use when someone wants to read, publish, or share the project wiki, or to set up CI publishing. Output is a disposable view; the bundle stays the source of truth.
---

# wiki-render

This project keeps its knowledge in an OKF bundle at `docs/knowledge/`
(the saidwhen convention). This skill compiles that bundle into a rich,
disposable HTML view. The bundle is the source of truth; rendered output
is never edited by hand — regenerate it instead.

## Render

Multi-page site (index + one page per document):

```
python scripts/wiki_render.py docs/knowledge -o wiki-site/
```

Single self-contained file (easy to attach or open from disk):

```
python scripts/wiki_render.py docs/knowledge -o wiki.html
```

Stdlib-only Python; no dependencies, no network, no LLM tokens. The script
is bundled at `scripts/wiki_render.py` (canonical source:
`render/wiki_render.py` in the saidwhen repo; CI keeps copies identical).

## Rules

1. Never hand-edit rendered output; change the bundle and re-render.
2. Don't commit rendered output into the bundle directory. Publish it via
   CI, a `wiki-site/` directory ignored by the bundle validator, or as a
   build artifact.
3. If the bundle fails to render, run the bundled validator first — a
   non-conformant bundle is the usual cause.

## CI publishing (offer, don't force)

If the user wants the wiki always current, offer a CI step that renders on
every push and publishes the site. The output is plain static HTML with no
host-specific features — it works on any static host (GitHub/GitLab Pages,
Netlify, S3, an internal server) or as a build artifact; the hosting choice
is the user's, never the skill's. Example GitHub Actions step:

```yaml
- name: Render wiki
  run: python render/wiki_render.py docs/knowledge -o wiki-site
- name: Upload wiki site
  uses: actions/upload-artifact@v4
  with: {name: wiki-site, path: wiki-site}
```
