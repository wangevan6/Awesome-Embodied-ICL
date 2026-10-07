#!/usr/bin/env python3
"""Build the public catalogue website using only Python's standard library."""

import argparse
from html import escape, unescape
import json
from pathlib import Path
import re
from urllib.parse import urlsplit, urlunsplit

if __package__:
    from .survey_collection import EXTERNAL_SURVEY_PDF, METHOD_GROUPS, load_collection, ordered, summary
else:
    from survey_collection import EXTERNAL_SURVEY_PDF, METHOD_GROUPS, load_collection, ordered, summary


ROOT = Path(__file__).resolve().parents[1]
SITE_NAME = 'Awesome In-context learning for Embodied AI system'
PUBLIC_DOCS = ("README.md", "CATALOGUE.md", "PROTOCOLS.md", "QUALITY.md", "CONTRIBUTING.md")
PUBLIC_HTML_DOCS = tuple(name.removesuffix(".md") + ".html" for name in PUBLIC_DOCS)
PUBLIC_LOGOS = ('logos/coowa.jpeg', 'logos/efort.png', 'logos/fudan.png', 'logos/hku.svg', 'logos/inspire.webp', 'logos/manifold.png', 'logos/ntu.png', 'logos/polimi.svg', 'logos/provenance.json', 'logos/teleai.svg', 'logos/tokyo.svg', 'logos/unix.png', 'logos/usi.svg', 'logos/weimar.png', 'logos/yale.png')
PUBLIC_FILES = frozenset(("index.html", "styles.css", "app.js", "favicon.svg", "sjtu-emblem.png", "figure-1.jpg", "data/papers.json", "data/collection.json", "data/survey-references.json", "data/survey-annotations.json", "data/sources.json", "data/manuscript-mapping.json", ".nojekyll", *PUBLIC_DOCS, *PUBLIC_HTML_DOCS, *PUBLIC_LOGOS))
TOKENS = {"__PAPER_DATA__", "__PAPER_CARDS__", "__PAPER_COUNT__", "__YEAR_RANGE__", "__ANNOTATED_COUNT__", "__MAPPED_COUNT__", "__SURVEY_TREE__", "__AGENT_LAST_RUN__", "__AGENT_PENDING__"}
FORMS = ("text", "visual", "trajectory", "multimodal")
DAILY_REPORTS = "docs/daily-collection"


def document_url(url):
    """Allow ordinary links and rewrite local Markdown document destinations."""
    if any(ord(character) < 32 for character in url) or "\\" in url:
        return None
    try:
        parsed = urlsplit(url)
    except ValueError:
        return None
    if parsed.scheme and parsed.scheme.lower() not in ("https", "http"):
        return None
    if parsed.netloc and not parsed.scheme:
        return None
    if not parsed.scheme and parsed.path.endswith(".md"):
        parsed = parsed._replace(path=parsed.path.removesuffix(".md") + ".html")
    if not parsed.scheme and parsed.path.removeprefix("./") not in PUBLIC_FILES | {"", "."}:
        return None
    return urlunsplit(parsed)


INLINE_PATTERN = re.compile(
    r"(?<!\\)`([^`\n]+)`|(?<!\\)\[([^\]\n]+)\]\(([^)\s]+)\)|(?<!\\)\*\*([^*\n]+)\*\*|(?<![\\*])\*([^*\n]+)\*(?!\*)"
)


def escape_markdown_text(value):
    """Decode authored Markdown escapes/entities, then escape once for HTML."""
    return escape(unescape(re.sub(r"\\([\\\[\]|*_<>])", r"\1", value)))


def render_inline(source, allow_links=True):
    """Render the catalogue's inline Markdown, escaping every plain-text span."""
    pieces = []
    cursor = 0
    for match in INLINE_PATTERN.finditer(source):
        pieces.append(escape_markdown_text(source[cursor:match.start()]))
        code, label, url, strong, emphasis = match.groups()
        if code is not None:
            pieces.append(f"<code>{escape(code)}</code>")
        elif label is not None:
            destination = document_url(url) if allow_links else None
            text = render_inline(label, allow_links=False)
            pieces.append(f'<a href="{escape(destination, quote=True)}">{text}</a>' if destination else text)
        elif strong is not None:
            pieces.append(f"<strong>{render_inline(strong, allow_links=allow_links)}</strong>")
        else:
            pieces.append(f"<em>{render_inline(emphasis, allow_links=allow_links)}</em>")
        cursor = match.end()
    pieces.append(escape_markdown_text(source[cursor:]))
    return "".join(pieces)


ANCHOR_PATTERN = re.compile(r'<a id="([a-z0-9]+(?:-[a-z0-9]+)*)"></a>')
HEADING_PATTERN = re.compile(r"(#{1,6})\s+(.+)")
LIST_PATTERN = re.compile(r"(?:([-*+])|(\d+)\.)\s+(.+)")
FENCE_PATTERN = re.compile(r"```([a-zA-Z0-9_-]*)\s*")
# Lines between these markers are GitHub presentation only (banner, badges, diagrams) and are not published.
GITHUB_ONLY_START = "<!-- github-only:start -->"
GITHUB_ONLY_END = "<!-- github-only:end -->"


def table_cells(line):
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_table_header(lines, index):
    return (index + 1 < len(lines) and "|" in lines[index]
            and all(re.fullmatch(r":?-{3,}:?", cell) for cell in table_cells(lines[index + 1])))


def render_markdown(source):
    """Render the existing documents' Markdown subset without raw HTML execution."""
    lines = source.splitlines()
    html = []
    used_ids = set()
    index = 0

    def is_block(line_index):
        line = lines[line_index].strip()
        return (not line or HEADING_PATTERN.fullmatch(line) or LIST_PATTERN.fullmatch(line)
                or FENCE_PATTERN.fullmatch(line) or ANCHOR_PATTERN.fullmatch(line)
                or line.startswith("<!--") or is_table_header(lines, line_index))

    while index < len(lines):
        line = lines[index].strip()
        if line == GITHUB_ONLY_START:
            index += 1
            while index < len(lines) and lines[index].strip() != GITHUB_ONLY_END:
                if lines[index].strip() == GITHUB_ONLY_START:
                    raise ValueError("Nested GitHub-only block")
                index += 1
            if index == len(lines):
                raise ValueError("Unclosed GitHub-only block")
            index += 1
            continue
        if not line or (line.startswith("<!--") and line.endswith("-->")):
            index += 1
            continue
        fence = FENCE_PATTERN.fullmatch(line)
        if fence:
            index += 1
            code = []
            while index < len(lines) and lines[index].strip() != "```":
                code.append(lines[index])
                index += 1
            language = f' class="language-{fence.group(1)}"' if fence.group(1) else ""
            html.append(f"<pre><code{language}>{escape(chr(10).join(code))}</code></pre>")
            index += 1
            continue
        anchor = ANCHOR_PATTERN.fullmatch(line)
        if anchor:
            anchor_id = anchor.group(1)
            if anchor_id in used_ids:
                raise ValueError(f"Duplicate document anchor: {anchor_id}")
            used_ids.add(anchor_id)
            html.append(f'<a id="{anchor_id}"></a>')
            index += 1
            continue
        heading = HEADING_PATTERN.fullmatch(line)
        if heading:
            level = len(heading.group(1))
            title = heading.group(2)
            slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-") or "section"
            heading_id = slug
            suffix = 0
            while heading_id in used_ids:
                suffix += 1
                heading_id = f"{slug}-{suffix}"
            used_ids.add(heading_id)
            html.append(f'<h{level} id="{heading_id}">{render_inline(title)}</h{level}>')
            index += 1
            continue
        if is_table_header(lines, index):
            headers = table_cells(line)
            html.append('<div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable reference table"><table>')
            html.append("<thead><tr>" + "".join(f'<th scope="col">{render_inline(cell)}</th>' for cell in headers) + "</tr></thead><tbody>")
            index += 2
            while index < len(lines) and lines[index].strip().startswith("|"):
                cells = table_cells(lines[index])
                if len(cells) != len(headers):
                    raise ValueError("Document table row does not match its header")
                html.append("<tr>" + "".join(f"<td>{render_inline(cell)}</td>" for cell in cells) + "</tr>")
                index += 1
            html.append("</tbody></table></div>")
            continue
        item = LIST_PATTERN.fullmatch(line)
        if item:
            ordered_list = item.group(2) is not None
            tag = "ol" if ordered_list else "ul"
            start = f' start="{int(item.group(2))}"' if ordered_list and int(item.group(2)) != 1 else ""
            html.append(f"<{tag}{start}>")
            while index < len(lines):
                item = LIST_PATTERN.fullmatch(lines[index].strip())
                if not item or (item.group(2) is not None) != ordered_list:
                    break
                html.append(f"<li>{render_inline(item.group(3))}</li>")
                index += 1
            html.append(f"</{tag}>")
            continue
        paragraph = [line]
        index += 1
        while index < len(lines) and not is_block(index):
            paragraph.append(lines[index].strip())
            index += 1
        html.append(f"<p>{render_inline(' '.join(paragraph))}</p>")
    return "\n".join(html)


def render_document(source, filename):
    title = next((line[2:].strip() for line in source.splitlines() if line.startswith("# ")), filename)
    page_title = title if title.startswith(SITE_NAME) else f"{title} — {SITE_NAME}"
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#ffffff">
  <title>{escape(page_title)}</title>
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&amp;family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&amp;family=IBM+Plex+Mono&amp;display=swap">
  <link rel="stylesheet" href="styles.css">
</head>
<body class="document-page">
  <a class="skip-link" href="#document-content">Skip to document</a>
  <header class="site-header">
    <div class="site-header-inner">
      <a class="wordmark" href="./" aria-label="{SITE_NAME} home"><svg viewBox="0 0 96 96" width="32" height="32" aria-hidden="true"><path d="M82 20H38C23 20 14 30 14 45V51C14 66 23 76 38 76H82M35 37V60M55 37V76" fill="none" stroke="currentColor" stroke-width="9"/></svg><span class="wordmark-name"><span>Awesome In-context learning</span> <span>for Embodied AI system</span></span></a>
      <nav aria-label="Document navigation"><a href="./#survey-map">Survey map</a><a href="./#catalogue">Papers</a><a href="{escape(filename, quote=True)}" download>Download Markdown ↓</a></nav>
    </div>
  </header>
  <main id="document-content" class="document-content">
{render_markdown(source)}
  </main>
  <footer class="site-footer"><a class="footer-brand" href="./">{SITE_NAME}</a><a href="./#catalogue">Back to the collection ↑</a></footer>
</body>
</html>
'''


def script_json(records):
    """Encode JSON inside a script element without allowing HTML parser breakout."""
    payload = json.dumps(records, ensure_ascii=False, separators=(",", ":"))
    for character, replacement in (("&", "\\u0026"), ("<", "\\u003c"), (">", "\\u003e"),
                                   ("\u2028", "\\u2028"), ("\u2029", "\\u2029")):
        payload = payload.replace(character, replacement)
    return payload


def render_cards(records):
    cards = []
    for row in ordered(records):
        value = {key: escape(str(item), quote=True) for key, item in row.items()}
        number = row["number"]
        primary_url = value.get("paper_url") if row.get("paper_url") else value["survey_url"]
        source_label = "Paper" if row.get("paper_url") else "External citation"
        kind = "Method / comparison" if row["is_method"] else "Supporting reference"
        badge = escape(row.get("evidence_tier") or kind)
        notes = [("Full citation (external inventory)", row["citation"]), ("Year source", row["year_basis"]), ("External survey group", row["family"])]
        framework_label = " · ".join(filter(None, [row.get("context_form_labels"), row.get("context_role_labels")]))
        if row.get("framework_mapped"):
            framework_label = framework_label or "Manuscript: broader domains / evaluation"
            notes.extend([("Context form", row["context_form_labels"] or "Not assigned in Figure 2"),
                          ("Context role", row["context_role_labels"] or "Not assigned in Figure 2"),
                          ("Deployment updates in roadmap", ", ".join(row["adaptation_regimes"]) or "Not assigned in Figure 2")])
        else:
            framework_label = "Framework mapping pending"
        for label, field in (("Deployment context", "context"), ("Mechanism", "action_mechanism"),
                             ("Evaluation", "evidence"), ("Evaluation setting", "setting"),
                             ("Adaptation target", "adaptation_target"), ("Deployment weights", "test_time_weights"),
                             ("Why read it", "why_it_matters"), ("Interpretation limit", "limitation")):
            if row.get(field):
                notes.append((label, row[field]))
        notes_html = "".join(f'<div><dt>{label}</dt><dd>{escape(str(text))}</dd></div>' for label, text in notes)
        page_links = " ".join(f'<a href="{EXTERNAL_SURVEY_PDF}#page={page}">{page}</a>' for page in row["reference_pages"])
        notes_html += f'<div><dt>Bibliography pages</dt><dd>{page_links}</dd></div>'
        for label, field in (("Reading note evidence, external survey pages", "annotation_pages"), ("Cited on external survey pages", "mentioned_pages")):
            if row.get(field):
                links = ", ".join(f'<a href="{EXTERNAL_SURVEY_PDF}#page={page}">{page}</a>' for page in row[field])
                notes_html += f'<div><dt>{label}</dt><dd>{links}</dd></div>'
        if not row["annotated"]:
            notes_html += '<div><dt>Research notes</dt><dd>Not yet annotated. Inclusion and original group follow the external survey; deployment behavior and experimental results have not been independently reviewed here.</dd></div>'
        if row.get("framework_mapped"):
            notes_html += f'<div><dt>Our manuscript [{row["manuscript_reference"]}]</dt><dd>Roadmap, Figure 2</dd></div>'
        context = f'<p class="paper-context">{value["context"]}</p>' if row.get("context") else ''
        budget = f'<p class="budget-text">Context amount: {value["context_budget"]}</p>' if row.get("context_budget") else ''
        project = f'<a href="{value["project_url"]}">Project</a>' if row.get("project_url") else ''
        details_label = "Research notes & sources" if row["annotated"] else "Classification & sources"
        cards.append(f'''<article class="paper-card" id="{value['id']}" data-id="{value['id']}">
  <div class="paper-meta"><span class="paper-year">Ext. [{number}] · {value['year']}</span><span class="evidence-tag">{badge}</span></div>
  <h3><a href="{primary_url}">{value['title']}</a></h3>
  <p class="paper-authors">{value['authors']}</p>
  <p class="paper-family">{escape(framework_label)}</p>{context}{budget}
  <details><summary>{details_label}</summary><dl>{notes_html}</dl></details>
  <footer class="paper-footer"><div class="paper-links"><a href="{primary_url}">{source_label}</a>{project}<a href="{value['survey_url']}">External [{number}]</a></div>
    <label class="compare-label"><input type="checkbox" data-compare="{value['id']}" aria-label="Compare {value['title']}"><span>Compare</span></label>
  </footer>
</article>''')
    return "\n".join(cards)


# The survey map follows our manuscript: sections, then subsections, then roadmap examples by year.
TREE_GROUPS = (("§III", "Form of context", "#guide-axes"),
               ("§V", "Beyond manipulation", "#guide-beyond"),
               ("§VI", "Evaluation", "#guide-evaluation"))
TREE_BRANCHES = (  # key, label, section, group, destination
    ("text", "Text", "§III-A", 0, "?form=text#catalogue"),
    ("visual", "Visual", "§III-B", 0, "?form=visual#catalogue"),
    ("trajectory", "Trajectory", "§III-C", 0, "?form=trajectory#catalogue"),
    ("multimodal", "Multimodal", "§III-D", 0, "?form=multimodal#catalogue"),
    ("dynamics", "Dynamics identification", "§V", 1, "#guide-beyond"),
    ("icrl", "In-context RL", "§V", 1, "#guide-beyond"),
    ("beyond", "Task &amp; behavior", "§V · beyond the arm", 1, "#guide-beyond"),
    ("evaluation", "Evaluation practice", "§VI", 2, "#guide-evaluation"),
)
TREE_AREAS = {"dynamics-identification": "dynamics", "in-context-rl": "icrl", "beyond-arm-task-behavior": "beyond",
              "graded-novelty": "evaluation", "cross-task-evaluation": "evaluation", "mechanistic-diagnostics": "evaluation"}
TREE_BINS = (("≤ 2023", 204), ("2024", 136), ("2025", 184), ("2026", 196))
TREE_GROWING = 222
TREE_RAIL_START = 456
TREE_X0 = 470
TIERS = ("A1", "B1", "A2", "B2", "A3", "B3")


DAILY_FIELDS = {"name", "title", "url", "arxiv_id", "submitted", "priority", "form", "roles", "self_built", "decision"}
DAILY_DECISIONS = ("pending", "accepted", "rejected", "deferred")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


def load_daily_reports(root):
    """Read and validate every daily research summary (YYYY-MM-DD.json beside its Markdown report)."""
    reports = []
    for path in sorted((Path(root) / DAILY_REPORTS).glob("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9].json")):
        report = json.loads(path.read_text(encoding="utf-8"))
        if report.get("run_date") != path.stem:
            raise ValueError(f"{path.name}: run_date must match the file name")
        if not (path.with_suffix(".md")).is_file():
            raise ValueError(f"{path.name}: missing Markdown report {path.stem}.md")
        for candidate in report.get("candidates", []):
            missing = DAILY_FIELDS - set(candidate)
            if missing:
                raise ValueError(f"{path.name}: candidate {candidate.get('name')} lacks {sorted(missing)}")
            if candidate["form"] not in FORMS + (None,):
                raise ValueError(f"{path.name}: {candidate['name']} has unknown form {candidate['form']}")
            if not set(candidate["roles"]) <= {"task", "state", "behavior"}:
                raise ValueError(f"{path.name}: {candidate['name']} has unknown roles")
            if candidate["decision"] not in DAILY_DECISIONS:
                raise ValueError(f"{path.name}: {candidate['name']} has unknown decision {candidate['decision']}")
            if not re.fullmatch(r"\d{4}\.\d{4,5}", candidate["arxiv_id"] or ""):
                raise ValueError(f"{path.name}: {candidate['name']} needs a verified arXiv identifier")
        reports.append(report)
    return reports


def daily_report(root):
    """Summarize the latest daily research run: its date and pending candidates per context form."""
    reports = load_daily_reports(root)
    if not reports:
        return None
    latest = reports[-1]
    pending = {form: 0 for form in FORMS}
    open_candidates = [candidate for report in reports for candidate in report.get("candidates", []) if candidate["decision"] == "pending"]
    for candidate in open_candidates:
        if candidate["form"] in pending:
            pending[candidate["form"]] += 1
    year, month, day = (int(part) for part in latest["run_date"].split("-"))
    return {"date": f"{MONTHS[month - 1]} {day}, {year}", "total": len(open_candidates), "pending": pending}


def example_year(example, records_by_number):
    if example["external_reference"] is not None:
        return int(records_by_number[example["external_reference"]]["year"])
    years = re.findall(r"\b((?:19|20)\d\d)\b", example["citation"])
    if not years:
        raise ValueError(f"Roadmap example has no year: {example['name']}")
    return int(years[-1])


def render_survey_tree(roadmap, records, daily):
    """Lay out the survey map as positioned nodes; every roadmap example appears exactly once per branch."""
    records_by_number = {row["number"]: row for row in records}
    leaves = {key: [[] for _ in TREE_BINS] for key, *_ in TREE_BRANCHES}
    for example in sorted(roadmap, key=lambda item: item["manuscript_reference"]):
        branches = list(example["forms"]) or sorted({TREE_AREAS[area] for area in example["areas"] if area in TREE_AREAS})
        if not branches:
            raise ValueError(f"Roadmap example has no survey map branch: {example['name']}")
        year = example_year(example, records_by_number)
        column = 0 if year <= 2023 else min(year - 2023, len(TREE_BINS) - 1)
        for branch in branches:
            leaves[branch][column].append((year, example))
    pending = (daily or {}).get("pending", {})

    def width(label):
        return int(round((len(label) * 6.7 + 18) / 2.0)) * 2

    columns = []
    x = TREE_X0
    for label, size in TREE_BINS:
        columns.append((label, x, size))
        x += size
    growing_x = x
    total_width = growing_x + TREE_GROWING
    guides, lines, nodes, labels = [], [], [], []

    def hline(x1, x2, y, cls="t-line", style=""):
        lines.append(f'<span class="{cls}" style="left:{x1}px;top:{y - 1}px;width:{x2 - x1}px;height:2px{style}"></span>')

    def vline(x0, y1, y2, cls="t-line"):
        lines.append(f'<span class="{cls}" style="left:{x0 - 1}px;top:{y1}px;width:2px;height:{y2 - y1}px"></span>')

    y = 52
    rails = {}
    group_centres = []
    for group_index, (section, group_label, group_href) in enumerate(TREE_GROUPS):
        members = [branch for branch in TREE_BRANCHES if branch[3] == group_index]
        if group_index:
            y += 20
        for key, label, section_label, _, href in members:
            packed = []
            for (column_label, column_x, column_width), bucket in zip(columns, leaves[key]):
                tier, cursor, placed = 0, 16, []
                for year, example in sorted(bucket, key=lambda item: (item[0], item[1]["manuscript_reference"])):
                    size = width(example["name"])
                    while cursor + size > column_width - 6:
                        tier, cursor = tier + 1, 16
                    if tier >= len(TIERS):
                        raise ValueError(f"Survey map column is too crowded: {label} {column_label}")
                    placed.append((example, year, size, TIERS[tier], cursor))
                    cursor += size + 6
                packed.append(placed)
            count = len({item[0]["manuscript_reference"] for column in packed for item in column})
            tip = pending.get(key, 0)
            used = {item[3] for column in packed for item in column} | ({"A1"} if tip else set())
            above = max([int(name[1]) for name in used if name[0] == "A"] or [0])
            below = max([int(name[1]) for name in used if name[0] == "B"] or [0])
            rail = y + (max(36, 44 + (above - 1) * 32 + 10) if above else 36)
            rails[key] = rail
            form = f' data-form="{key}"' if key in FORMS else ""
            nodes.append(f'<a class="t-node t-branch b-{key}" href="{href}"{form} style="left:288px;top:{rail - 28}px">'
                         f'<b>{label}</b><small>{section_label} · {count}</small></a>')
            hline(TREE_RAIL_START, growing_x, rail, f"t-rail b-{key}")
            hline(growing_x, total_width - 6, rail, f"t-rail t-tip b-{key}")
            for (column_label, column_x, column_width), placed in zip(columns, packed):
                if not placed:
                    continue
                stem = column_x + 8
                centres = []
                for example, year, size, tier, offset in placed:
                    level = int(tier[1])
                    top = rail - 44 - (level - 1) * 32 if tier[0] == "A" else rail + 18 + (level - 1) * 32
                    centres.append(top + 13)
                    if offset == 16:
                        hline(stem, column_x + 16, top + 13, f"t-twig b-{key}")
                    name = escape(example["name"])
                    style = f"left:{column_x + offset}px;top:{top}px;width:{size}px"
                    if example["external_reference"] is not None:
                        number = example["external_reference"]
                        nodes.append(f'<a class="t-leaf t-in b-{key}" href="?q=%5B{number}%5D#catalogue" style="{style}" '
                                     f'title="{name} · {year} · in the collection as external reference [{number}]">{name}</a>')
                    else:
                        nodes.append(f'<span class="t-leaf t-out" style="{style}" '
                                     f'title="{name} · {year} · named in our manuscript, outside the 412-work collection">{name}</span>')
                vline(stem, min(centres + [rail]), max(centres + [rail]), f"t-twig b-{key}")
            if tip:
                top = rail - 44
                hline(growing_x + 8, growing_x + 16, top + 13, f"t-twig b-{key}")
                vline(growing_x + 8, top + 13, rail, f"t-twig b-{key}")
                label_text = f"+{tip} pending review"
                nodes.append(f'<span class="t-leaf t-new b-{key}" style="left:{growing_x + 16}px;top:{top}px;width:{width(label_text)}px" '
                             f'title="Daily research agent candidates with a tentative {key} form; not yet reviewed or added to the collection">{label_text}</span>')
            y = rail + (max(36, 18 + 26 + (below - 1) * 32 + 10) if below else 36)
        first, last = rails[members[0][0]], rails[members[-1][0]]
        centre = (first + last) // 2
        group_centres.append(centre)
        nodes.append(f'<a class="t-node t-group" href="{group_href}" style="left:140px;top:{centre - 26}px">'
                     f'<b>{section}</b><small>{group_label}</small></a>')
        if len(members) == 1:
            hline(260, 288, centre)
        else:
            hline(260, 274, centre)
            vline(274, first, last)
            for key, *_ in members:
                hline(274, 288, rails[key])
    height = y + 12
    root_centre = (group_centres[0] + group_centres[-1]) // 2
    hline(112, 126, root_centre)
    vline(126, group_centres[0], group_centres[-1])
    for centre in group_centres:
        hline(126, 140, centre)
    total = len(roadmap)
    nodes.insert(0, f'<span class="t-node t-root" style="left:0;top:{root_centre - 30}px"><b>In-context learning</b><small>{total} examples</small></span>')
    for label, column_x, _ in columns:
        guides.append(f'<span class="t-guide" style="left:{column_x}px;height:{height - 30}px"></span>')
        labels.append(f'<span class="t-year" style="left:{column_x + 12}px">{label}</span>')
    guides.append(f'<span class="t-guide t-guide-growing" style="left:{growing_x}px;height:{height - 30}px"></span>')
    when = f" · {daily['date']}" if daily else ""
    labels.append(f'<span class="t-year t-year-growing" style="left:{growing_x + 12}px">Growing · daily run{when}</span>')
    return (f'<div class="tree" style="width:{total_width}px;height:{height}px" role="group" aria-label="Survey map tree">'
            f'<span class="t-axis"></span>{"".join(guides)}{"".join(lines)}{"".join(nodes)}{"".join(labels)}</div>')


def read_public_source(root, relative):
    source = root / relative
    if source.is_symlink() or not source.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Public source must be a regular file within the project: {relative}")
    return source.read_bytes()


def render_files(root=ROOT):
    """Render the exact publish allowlist. Never recursively copy project files."""
    root = Path(root)
    data = read_public_source(root, "data/papers.json")
    records = ordered(load_collection(root))
    totals = summary(records)
    template = read_public_source(root, "site/index.html").decode("utf-8")
    present = set(re.findall(r"__[A-Z_]+__", template))
    if present != TOKENS:
        raise ValueError(f"Template placeholders: missing {sorted(TOKENS - present)}, unknown {sorted(present - TOKENS)}")
    years = [row["year"] for row in records]
    roadmap = json.loads(read_public_source(root, "data/manuscript-mapping.json"))["references"]
    daily = daily_report(root)
    pending = daily["total"] if daily else 0
    values = {
        "__SURVEY_TREE__": render_survey_tree(roadmap, records, daily),
        "__AGENT_LAST_RUN__": daily["date"] if daily else "not yet run",
        "__AGENT_PENDING__": f"{pending} candidate{'' if pending == 1 else 's'}",
        "__PAPER_DATA__": script_json(records),
        "__PAPER_CARDS__": render_cards(records),
        "__PAPER_COUNT__": str(len(records)),
        "__ANNOTATED_COUNT__": str(totals["annotated"]),
        "__MAPPED_COUNT__": str(totals["mapped"]),
        "__YEAR_RANGE__": f"{min(years)}–{max(years)}" if min(years) != max(years) else str(years[0]),
    }
    html = re.sub(r"__[A-Z_]+__", lambda match: values[match.group()], template)
    files = {"index.html": html.encode("utf-8"), "data/papers.json": data, ".nojekyll": b""}
    files["data/collection.json"] = (json.dumps(records, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    for name in ("survey-references.json", "survey-annotations.json", "sources.json", "manuscript-mapping.json"):
        files[f"data/{name}"] = read_public_source(root, f"data/{name}")
    for asset in ("styles.css", "app.js", "favicon.svg", "sjtu-emblem.png", "figure-1.jpg", *PUBLIC_LOGOS):
        files[asset] = read_public_source(root, f"site/{asset}")
    for document in PUBLIC_DOCS:
        files[document] = read_public_source(root, document)
        files[document.removesuffix(".md") + ".html"] = render_document(files[document].decode("utf-8"), document).encode("utf-8")
    return files


def inspect_output(output):
    output = Path(output)
    if output.is_symlink():
        raise ValueError("Output directory must not be a symlink")
    if not output.exists():
        return set()
    if not output.is_dir():
        raise ValueError("Output path must be a directory")
    names = set()
    for path in output.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Output must not contain symlinks: {path}")
        relative = path.relative_to(output).as_posix()
        if path.is_file():
            names.add(relative)
        elif relative not in {"data", "logos"}:
            raise ValueError(f"Unexpected output directory: {relative}")
    return names


def write_site(files, output):
    output = Path(output)
    destination_root = output.resolve()
    if (destination_root == ROOT or destination_root in ROOT.parents
            or any(destination_root.is_relative_to(ROOT / name)
                   for name in ("site", "data", "scripts", "tests", ".git", ".github"))):
        raise ValueError("Output directory must be separate from project source files")
    unexpected = inspect_output(output) - PUBLIC_FILES
    if unexpected:
        raise ValueError(f"Unexpected output files; use a clean output directory: {', '.join(sorted(unexpected))}")
    if set(files) != PUBLIC_FILES:
        raise ValueError("Rendered files do not match the public allowlist")
    for relative, content in files.items():
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)


def check_site(files, output):
    output = Path(output)
    if inspect_output(output) != set(files):
        raise ValueError("Generated site file list differs; run python3 scripts/build_site.py")
    stale = [name for name, content in files.items() if (output / name).read_bytes() != content]
    if stale:
        raise ValueError(f"Generated site is out of date: {', '.join(stale)}; run python3 scripts/build_site.py")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_site", help="destination directory (default: _site)")
    parser.add_argument("--check", action="store_true", help="verify all generated files match their sources")
    args = parser.parse_args()
    try:
        files = render_files()
        if args.check:
            check_site(files, args.output)
        else:
            write_site(files, args.output)
    except (ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")
    print(f"{'Verified' if args.check else 'Built'} {len(files)} public files in {args.output}")


if __name__ == "__main__":
    main()
