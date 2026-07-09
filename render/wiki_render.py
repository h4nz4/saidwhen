"""Render a saidwhen OKF bundle into a static HTML wiki.

The presentation layer of the saidwhen convention: the bundle stays the
small, canonical, agent-readable source of truth; this compiles a rich,
DISPOSABLE wiki view from it — an index page (stats, provenance graph,
navigation) plus one page per document. Regenerate whenever you want to
read it; never edit the output.

Stdlib only. Usage:
  python wiki_render.py <bundle-dir> -o <out-dir>       # multi-page site
  python wiki_render.py <bundle-dir> -o <out.html>      # single-file view
"""
import argparse
import datetime
import html
import re
from pathlib import Path

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)

STATUS_COLORS = {"accepted": "#15803d", "superseded": "#6b7280", "revisit": "#b45309"}
SECTIONS = [
    ("Decisions", ("Decision",)),
    ("Facts — constraints, terms &amp; components", ("Constraint", "Term", "Component")),
    ("History — interviews", ("Interview",)),
]


def field(fm: str, name: str) -> str:
    m = re.search(rf"^{name}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else ""


def slug(rel: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", rel.lower()).strip("-")


def load(bundle: Path) -> list[dict]:
    docs = []
    for p in sorted(bundle.rglob("*.md")):
        text = p.read_text(encoding="utf-8-sig")
        m = FRONTMATTER.match(text)
        fm = m.group(1) if m else ""
        rel = p.relative_to(bundle).as_posix()
        docs.append({
            "rel": rel, "slug": slug(rel), "dir": p.parent,
            "type": field(fm, "type"), "title": field(fm, "title") or p.stem,
            "description": field(fm, "description"),
            "status": field(fm, "status"), "timestamp": field(fm, "timestamp")[:10],
            "scope": field(fm, "scope"), "source": field(fm, "source"),
            "body": text[m.end():] if m else text,
        })
    return docs


def md2html(body: str, doc: dict, bundle: Path, known: dict, href) -> str:
    """Tiny markdown renderer — headings, lists, quotes, code, links, bold."""
    def link(m):
        label, target = m.group(1), m.group(2)
        if not target.startswith(("http://", "https://")):
            try:
                rel = (doc["dir"] / target).resolve().relative_to(bundle.resolve()).as_posix()
                if rel in known:
                    return f'<a href="{href(known[rel])}">{label}</a>'
            except ValueError:
                pass
            return f"<span class=extlink>{label}</span>"
        return f'<a href="{target}">{label}</a>'

    out, in_list, in_quote, in_fence, para = [], False, False, False, []

    def flush_para():
        if para:
            out.append(f"<p>{' '.join(para)}</p>")
            para.clear()

    body = html.escape(body)
    for raw in body.splitlines():
        line = raw.rstrip()
        if line.lstrip().startswith("```"):
            flush_para()
            out.append("</code></pre>" if in_fence else "<pre><code>")
            in_fence = not in_fence
            continue
        if in_fence:
            out.append(raw)
            continue
        if in_list and not line.lstrip().startswith(("-", "*")):
            out.append("</ul>"); in_list = False
        if in_quote and not line.startswith("&gt;"):
            out.append("</blockquote>"); in_quote = False
        if not line:
            flush_para()
            continue
        line = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", line)
        line = re.sub(r"`([^`]+)`", r"<code>\1</code>", line)
        line = re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", link, line)
        if line.startswith("# "):
            continue  # doc title already on the card
        if line.startswith("## "):
            flush_para()
            cls = " class=rejected" if "reject" in line.lower() else ""
            out.append(f"<h4{cls}>{line[3:]}</h4>")
        elif line.startswith("### "):
            flush_para()
            out.append(f"<h5>{line[4:]}</h5>")
        elif line.lstrip().startswith(("- ", "* ")):
            flush_para()
            if not in_list:
                out.append("<ul>"); in_list = True
            out.append(f"<li>{line.lstrip()[2:]}</li>")
        elif line.startswith("&gt;"):
            flush_para()
            if not in_quote:
                out.append("<blockquote>"); in_quote = True
            out.append(line[4:].lstrip() + "<br>")
        else:
            para.append(line)
    flush_para()
    if in_fence:
        out.append("</code></pre>")
    if in_list:
        out.append("</ul>")
    if in_quote:
        out.append("</blockquote>")
    return "\n".join(out)


def graph_svg(decisions: list[dict], evidence: list[dict], edges: list[tuple], href) -> str:
    """Two-column provenance graph: decisions -> their evidence."""
    if not decisions or not evidence:
        return ""
    row, pad, lw, rw = 46, 24, 380, 380
    h = pad * 2 + row * max(len(decisions), len(evidence))
    ly = {d["rel"]: pad + row * i + row // 2 for i, d in enumerate(decisions)}
    ry = {e["rel"]: pad + row * i + row // 2 for i, e in enumerate(evidence)}
    parts = [f'<svg viewBox="0 0 {lw + rw + 240} {h}" xmlns="http://www.w3.org/2000/svg" '
             f'font-family="inherit" font-size="13">']
    for rel_d, rel_e in edges:
        if rel_d in ly and rel_e in ry:
            y1, y2 = ly[rel_d], ry[rel_e]
            parts.append(f'<path d="M {lw} {y1} C {lw + 120} {y1}, {lw + 120} {y2}, {lw + 240} {y2}" '
                         f'fill="none" stroke="#94a3b8" stroke-width="1.5"/>')
    for d in decisions:
        y = ly[d["rel"]]
        c = STATUS_COLORS.get(d["status"], "#334155")
        parts.append(f'<a href="{href(d["slug"])}"><rect x="4" y="{y - 17}" rx="8" width="{lw - 8}" height="34" '
                     f'fill="#fff" stroke="{c}" stroke-width="1.5"/>'
                     f'<circle cx="22" cy="{y}" r="5" fill="{c}"/>'
                     f'<text x="36" y="{y + 4}" fill="#0f172a">{html.escape(d["title"][:44])}</text></a>')
    for e in evidence:
        y = ry[e["rel"]]
        parts.append(f'<a href="{href(e["slug"])}"><rect x="{lw + 240 + 4}" y="{y - 17}" rx="8" width="{rw - 8}" height="34" '
                     f'fill="#f8fafc" stroke="#cbd5e1"/>'
                     f'<text x="{lw + 240 + 18}" y="{y + 4}" fill="#334155">'
                     f'{html.escape((e["type"] or "?") + ": " + e["title"][:38])}</text></a>')
    parts.append("</svg>")
    return "".join(parts)


CSS = """
:root{--ink:#0f172a;--mut:#64748b;--line:#e2e8f0;--bg:#f8fafc;--card:#ffffff}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);
font:16px/1.65 ui-sans-serif,system-ui,'Segoe UI',sans-serif}
.wrap{max-width:1060px;margin:0 auto;padding:48px 28px 96px}
header h1{font-size:2.4rem;margin:0 0 4px;letter-spacing:-.02em}
header p{color:var(--mut);font-size:1.1rem;margin:0}
nav.crumb{margin-bottom:20px;font-size:.9rem}
.stats{display:flex;gap:14px;flex-wrap:wrap;margin:28px 0 8px}
.stat{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 18px}
.stat b{font-size:1.4rem;display:block}.stat span{color:var(--mut);font-size:.82rem;text-transform:uppercase;letter-spacing:.06em}
h2.sec{font-size:1.05rem;text-transform:uppercase;letter-spacing:.1em;color:var(--mut);
margin:52px 0 16px;border-bottom:1px solid var(--line);padding-bottom:8px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px 26px;margin:14px 0}
.card h3{margin:0 0 2px;font-size:1.25rem}.card .desc{color:var(--mut);margin:0 0 10px}
.toc a{display:block;padding:8px 14px;border-radius:10px}
.toc a:hover{background:var(--card);text-decoration:none}
.toc .mut{color:var(--mut);font-size:.85rem;margin-left:8px}
.meta{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0 14px}
.badge{font-size:.75rem;font-weight:600;padding:3px 10px;border-radius:999px;color:#fff}
.chip{font-size:.75rem;padding:3px 10px;border-radius:999px;background:var(--bg);
border:1px solid var(--line);color:var(--mut);font-family:ui-monospace,monospace}
.card h4{margin:18px 0 6px;font-size:.95rem;text-transform:uppercase;letter-spacing:.05em;color:#475569}
.card h4.rejected{color:#b91c1c}.card h5{margin:12px 0 4px}
.card p{margin:6px 0}.card ul{margin:6px 0;padding-left:22px}
blockquote{border-left:3px solid #cbd5e1;margin:10px 0;padding:6px 14px;color:#475569;
background:var(--bg);border-radius:0 8px 8px 0}
code{background:#eef2f7;padding:1px 6px;border-radius:6px;font-size:.88em}
pre{background:#0f172a;color:#e2e8f0;border-radius:12px;padding:16px 18px;overflow-x:auto;font-size:.85em;line-height:1.5}
pre code{background:none;padding:0;color:inherit}
a{color:#0369a1;text-decoration:none}a:hover{text-decoration:underline}
.extlink{border-bottom:1px dotted var(--mut)}
.graph{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;overflow-x:auto}
table{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}
td{padding:9px 14px;border-top:1px solid var(--line);vertical-align:top;font-size:.92rem}
td:first-child{white-space:nowrap;color:var(--mut)}
footer{margin-top:64px;color:var(--mut);font-size:.85rem;border-top:1px solid var(--line);padding-top:16px}
"""


def shell(title: str, body: str, bundle: Path) -> str:
    footer = (f"Compiled from <code>{html.escape(str(bundle))}</code> on "
              f"{datetime.date.today().isoformat()} by wiki_render.py — a disposable view. "
              f"The bundle is the source of truth; do not edit this file.")
    return (f"<!DOCTYPE html><html lang=en><head><meta charset=utf-8>\n"
            f'<meta name=viewport content="width=device-width,initial-scale=1">\n'
            f"<title>{html.escape(title)}</title><style>{CSS}</style></head><body><div class=wrap>\n"
            f"{body}\n<footer>{footer}</footer></div></body></html>")


def badges(d: dict) -> str:
    out = ""
    if d["status"]:
        out += (f'<span class=badge style="background:'
                f'{STATUS_COLORS.get(d["status"], "#334155")}">{d["status"]}</span>')
    if d["timestamp"]:
        out += f'<span class=chip>{d["timestamp"]}</span>'
    if d["source"]:
        out += f'<span class=chip>said by: {html.escape(d["source"])}</span>'
    for pat in d["scope"].split():
        out += f'<span class=chip>governs {html.escape(pat)}</span>'
    return out


def card(d: dict, bundle: Path, known: dict, href) -> str:
    desc = f'<p class=desc>{html.escape(d["description"])}</p>' if d["description"] else ""
    return (f'<div class=card id="{d["slug"]}"><h3>{html.escape(d["title"])}</h3>{desc}'
            f'<div class=meta>{badges(d)}</div>{md2html(d["body"], d, bundle, known, href)}</div>')


def analyze(bundle: Path):
    docs = load(bundle)
    known = {d["rel"]: d["slug"] for d in docs}
    index = next((d for d in docs if d["type"] == "Index"), None)
    log = next((d for d in docs if d["type"] == "Log"), None)
    decisions = [d for d in docs if d["type"] == "Decision"]
    evidence = [d for d in docs if d["type"] in ("Interview", "Constraint", "Term", "Component")]
    edges = []
    for d in decisions:
        for m in re.finditer(r"\]\(([^)\s]+)\)", d["body"]):
            target = m.group(1)
            if target.startswith(("http://", "https://")):
                continue
            try:
                rel = (d["dir"] / target).resolve().relative_to(bundle.resolve()).as_posix()
            except ValueError:
                continue
            if any(e["rel"] == rel for e in evidence):
                edges.append((d["rel"], rel))
    title = index["title"] if index else bundle.name
    intro = ""
    if index:
        para = []
        for l in index["body"].splitlines():
            if l.startswith(("#", "<!--", "-", "_", "|")):
                continue
            if not l.strip():
                if para:
                    break
                continue
            para.append(l.strip())
        intro = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", " ".join(para)) or index["description"]
    return docs, known, index, log, decisions, evidence, edges, title, intro


def header_and_graph(bundle, known, log, decisions, evidence, edges, title, intro, href, paged):
    n_acc = sum(1 for d in decisions if d["status"] == "accepted")
    stats = [(len(decisions), "decisions"), (n_acc, "in force"),
             (len(evidence), "evidence docs"), (len(edges), "provenance links")]
    svg = graph_svg(decisions, evidence, edges, href)
    log_rows = ""
    if log:
        for line in log["body"].splitlines():
            m = re.match(r"(\d{4}-\d{2}-\d{2})\s+(\S+)\s+(\S+)\s+(.*)", line.strip())
            if m:
                target = known.get(m.group(2)) if m.group(2) in paged else None
                path = f'<a href="{href(target)}">{m.group(2)}</a>' if target else f"<code>{m.group(2)}</code>"
                log_rows = (f"<tr><td>{m.group(1)}</td><td>{path}</td>"
                            f"<td>{m.group(3)}</td><td>{html.escape(m.group(4))}</td></tr>") + log_rows
    head = (f"<header><h1>{html.escape(title)}</h1><p>{html.escape(intro)}</p></header>"
            f"<div class=stats>{''.join(f'<div class=stat><b>{n}</b><span>{lbl}</span></div>' for n, lbl in stats)}</div>")
    graph = (f"<h2 class=sec>Provenance graph — every decision traces to who said it</h2>"
             f"<div class=graph>{svg}</div>") if svg else ""
    hist = f"<h2 class=sec>History</h2><table>{log_rows}</table>" if log_rows else ""
    return head, graph, hist


def render_single(bundle: Path) -> str:
    docs, known, index, log, decisions, evidence, edges, title, intro = analyze(bundle)
    href = lambda s: f"#{s}"
    paged = {d["rel"] for d in docs if d["type"] not in ("Index", "Log")}
    head, graph, hist = header_and_graph(bundle, known, log, decisions, evidence, edges, title, intro, href, paged)
    body = [head, graph]
    for name, types in SECTIONS:
        items = [d for d in docs if d["type"] in types]
        if items:
            body.append(f"<h2 class=sec>{name}</h2>" +
                        "".join(card(d, bundle, known, href) for d in items))
    body.append(hist)
    return shell(title, "\n".join(body), bundle)


def render_site(bundle: Path, outdir: Path) -> list[Path]:
    docs, known, index, log, decisions, evidence, edges, title, intro = analyze(bundle)
    href = lambda s: f"{s}.html"
    paged = {d["rel"] for d in docs if d["type"] not in ("Index", "Log")}
    outdir.mkdir(parents=True, exist_ok=True)
    written = []

    head, graph, hist = header_and_graph(bundle, known, log, decisions, evidence, edges, title, intro, href, paged)
    toc = []
    for name, types in SECTIONS:
        items = [d for d in docs if d["type"] in types]
        if items:
            toc.append(f"<h2 class=sec>{name}</h2><div class=toc>" + "".join(
                f'<a href="{href(d["slug"])}">{html.escape(d["title"])}'
                f'<span class=mut>{d["status"] or d["type"]}'
                f'{" · " + d["timestamp"] if d["timestamp"] else ""}</span></a>'
                for d in items) + "</div>")
    idx = outdir / "index.html"
    idx.write_text(shell(title, "\n".join([head, graph, *toc, hist]), bundle), encoding="utf-8")
    written.append(idx)

    for d in docs:
        if d["type"] in ("Index", "Log"):
            continue
        crumb = f'<nav class=crumb><a href="index.html">← {html.escape(title)}</a></nav>'
        page = outdir / f"{d['slug']}.html"
        page.write_text(shell(d["title"], crumb + card(d, bundle, known, href), bundle),
                        encoding="utf-8")
        written.append(page)
    return written


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("bundle", type=Path)
    ap.add_argument("-o", "--out", type=Path, default=Path("wiki.html"),
                    help="output .html file (single view) or directory (multi-page site)")
    args = ap.parse_args()
    if args.out.suffix.lower() == ".html":
        args.out.write_text(render_single(args.bundle), encoding="utf-8")
        print(f"OK  {args.out} rendered from {args.bundle}")
    else:
        pages = render_site(args.bundle, args.out)
        print(f"OK  {args.out} site rendered from {args.bundle} ({len(pages)} pages)")


if __name__ == "__main__":
    main()
