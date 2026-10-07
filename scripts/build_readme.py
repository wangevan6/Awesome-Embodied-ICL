#!/usr/bin/env python3
"""Render deterministic Markdown views of the survey's complete reference index."""

import argparse
from collections import Counter
import html
import json
from pathlib import Path
import re

try:
    from .survey_collection import EXTERNAL_SURVEY_PDF, GROUPS, EXPECTED_COUNTS, load_collection, ordered, summary
    from .build_site import TREE_AREAS, daily_report, example_year, load_daily_reports
except ImportError:
    from survey_collection import EXTERNAL_SURVEY_PDF, GROUPS, EXPECTED_COUNTS, load_collection, ordered, summary
    from build_site import TREE_AREAS, daily_report, example_year, load_daily_reports

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "survey-references.json"
README = ROOT / "README.md"
CATALOGUE = ROOT / "CATALOGUE.md"
PROTOCOLS = ROOT / "PROTOCOLS.md"
REPOSITORY = "https://github.com/wangevan6/Awesome-Embodied-ICL"
ROLE_LABELS = {"task": "Task specification", "state": "State representation", "behavior": "Behavior specification"}
REGIME_LABELS = {"gradient-free": "Gradient-free", "update-optional": "Update-optional", "update-dependent": "Update-dependent"}
FEATURED_GROUPS = (  # heading, branch keys from the survey map, manuscript section
    ("Text context", ("text",), "§III-A"),
    ("Visual context", ("visual",), "§III-B"),
    ("Trajectory context", ("trajectory",), "§III-C"),
    ("Multimodal context", ("multimodal",), "§III-D"),
    ("Beyond manipulation", ("dynamics", "icrl", "beyond"), "§V"),
    ("Evaluation", ("evaluation",), "§VI"),
)
AREA_LABELS = {"dynamics": "Dynamics identification", "icrl": "In-context RL", "beyond": "Task and behavior beyond the arm", "evaluation": "Evaluation practice"}
FAMILIES = GROUPS


def validate(records):
    """Validate the joined publication index, without requiring invented annotations."""
    if not isinstance(records, list) or len(records) != 412:
        raise ValueError("Survey collection must contain all 412 references")
    if {row.get("number") for row in records} != set(range(1, 413)):
        raise ValueError("Each survey reference number must occur exactly once")
    if len({row.get("id") for row in records}) != len(records):
        raise ValueError("Duplicate catalogue id")
    if Counter(row.get("family") for row in records) != Counter(EXPECTED_COUNTS):
        raise ValueError("Catalogue groups must match Appendix A")
    for row in records:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", row["id"]):
            raise ValueError("Invalid catalogue id")
        for field in ("title", "citation", "year_basis", "survey_url"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise ValueError(f"Reference {row['number']} needs {field}")
        if type(row.get("year")) is not int or not 1900 <= row["year"] <= 2100:
            raise ValueError("Invalid reference year")
        if not row.get("reference_pages"):
            raise ValueError("Reference needs bibliography page provenance")
        if row.get("annotated") and not row.get("annotation_pages"):
            raise ValueError("Reading note needs survey page evidence")
    return records


def markdown(value):
    """Preserve source text while escaping syntax that could alter a Markdown table."""
    text = html.escape(str(value), quote=False).replace("\\", "\\\\")
    for character in ("[", "]", "|", "*", "_"):
        text = text.replace(character, "\\" + character)
    return text.replace("\n", " ")


def page_links(pages):
    return ", ".join(f"[p. {page}]({EXTERNAL_SURVEY_PDF}#page={page})" for page in pages)


def source_metadata():
    return json.loads(DATA.read_text(encoding="utf-8"))["source"]


def render_table(records):
    lines = [
        "| External ref. | Year | Reference | Our context form / role | Reading note |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in ordered(records):
        lines.append(
            f"| [{row['number']}] | {row['year']} | "
            f"[{markdown(row['title'])}](CATALOGUE.md#{row['id']}) | "
            f"{' / '.join(filter(None, [row['context_form_labels'], row['context_role_labels']])) or ('Broader domains / evaluation' if row['framework_mapped'] else 'Mapping pending')} | {'Available' if row['annotated'] else 'Bibliography only'} |"
        )
    lines.extend([
        "",
        "The index preserves every external survey reference. The context forms and roles come from our manuscript roadmap. Method groups include supporting control mechanisms and parameter-adaptation comparisons; inclusion does not imply frozen deployment weights. The 21 reading notes are grounded in cited external survey passages. Other entries provide bibliography and classification only.",
    ])
    return "\n".join(lines)


def render_catalogue(records):
    source = source_metadata()
    lines = [
        "# Awesome In-context learning for Embodied AI system — Paper catalogue",
        "",
        "Our manuscript, *In-Context Learning for Embodied Agents: Methods, Benchmarks, and Open Challenges*, defines this catalogue’s context forms and roles. All 412 references imported from the external survey *In-Context Learning for Robots: Methods and Applications* are retained, including parameter-adaptation comparisons. The two surveys have independent reference numbering.",
        "",
        "Entries are grouped by their first listed context form; roles are independent and may overlap. Roadmap examples about broader domains and evaluation have a separate group; all other works await mapping. Each entry preserves its external reference number, citation, source URL, original group, and bibliography pages. The 21 annotated entries add reading notes supported by explicit survey pages. An unannotated entry has no inferred context budget, deployment update regime, or experimental result.",
        "",
        "Method years follow Appendix A's first public year; supporting-reference years use the bibliography date. Both dates are shown when they differ. Source URLs are transcribed from the PDF and have not been independently verified for availability.",
        "",
        f"**External inventory snapshot:** [inventory and provenance](data/survey-references.json) · [external survey PDF, arXiv v1]({EXTERNAL_SURVEY_PDF}) · SHA-256 of the extracted copy `{source['sha256']}`.",
    ]
    fields = (
        ("context", "Deployment context"),
        ("action_mechanism", "Action mechanism"),
        ("test_time_weights", "Deployment weights"),
        ("setting", "Setting discussed"),
        ("evidence", "Survey evidence"),
        ("why_it_matters", "Why read it"),
        ("adaptation_target", "Adaptation target"),
        ("evidence_tier", "Evidence description"),
        ("context_budget", "Context amount"),
        ("limitation", "Interpretation limit"),
    )
    def framework_group(row):
        if row["context_forms"]:
            return row["context_forms"][0].title() + " context"
        return "Broader domains and evaluation" if row["framework_mapped"] else "Framework mapping pending"
    lines.extend(["", "**Conceptual authority:** our manuscript’s roadmap (Figure 2) · [full roadmap mapping](data/manuscript-mapping.json) · [source identities](data/sources.json). The roadmap includes 29 further works outside the external inventory; those remain recorded in the mapping data, including RoboSSM."])
    for family in ("Text context", "Visual context", "Trajectory context", "Multimodal context", "Broader domains and evaluation", "Framework mapping pending"):
        subset = [row for row in ordered(records) if framework_group(row) == family]
        lines.extend(["", f"## {family}", "", f"{len(subset)} references."])
        for row in subset:
            date_note = row["year_basis"]
            if row["bibliography_year"] != row["year"]:
                date_note += f"; bibliography publication: {row['bibliography_year']}"
            lines.extend([
                "", f'<a id="{row["id"]}"></a>',
                f"### External [{row['number']}] {markdown(row['title'])} ({row['year']})", "",
                f"**Date basis:** {date_note}. **Bibliography:** {page_links(row['reference_pages'])}.", "",
                f"**Citation:** {markdown(row['citation'])}", "",
            ])
            if row["framework_mapped"]:
                lines.extend([f"**Our manuscript [{row['manuscript_reference']}]:** roadmap, Figure 2. **Form:** {row['context_form_labels'] or 'Not assigned in roadmap'}. **Role:** {row['context_role_labels'] or 'Not assigned in roadmap'}.", ""])
            else:
                lines.extend(["**Our framework:** Mapping pending; this reference is retained in the full collection.", ""])
            lines.extend([f"**External survey group:** {row['family']}.", ""])
            if row.get("paper_url"):
                lines.append(f"**Source URL:** [paper or source]({row['paper_url']}) — transcribed from the external survey.")
            else:
                lines.append("**Source URL:** Not supplied by the survey bibliography; use the linked PDF citation.")
            if row["annotated"]:
                lines.extend(["", f"**Reading-note evidence:** {page_links(row['annotation_pages'])}.", ""])
                for key, label in fields:
                    if row.get(key):
                        lines.append(f"- **{label}:** {markdown(row[key])}")
            else:
                lines.extend(["", "**Annotation status:** Bibliography and survey classification only. Per-paper deployment and evaluation details have not been annotated."])
    return "\n".join(lines) + "\n"


def render_protocols(records):
    rows = [row for row in ordered(records) if row.get("annotated") and row.get("context_budget")]
    lines = [
        "# Context amounts supported by the external survey",
        "",
        f"Only {len(rows)} audited reading notes retain an explicit, nonempty context amount, sourced to the external survey. Our manuscript supplies the conceptual framework. This is not a complete protocol matrix for the 412 references. Amounts are supported by the linked survey passages or, where marked, the cited paper title; they have not been independently checked against every full paper. Demonstrations and interaction steps are different units.",
        "",
        "| Reference | Context amount | Setting discussed | Survey evidence |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| [{markdown(row['title'])}](CATALOGUE.md#{row['id']}) | "
            f"{markdown(row['context_budget'])} | {markdown(row.get('setting', 'Not detailed in the survey'))} | "
            f"{page_links(row['annotation_pages'])} |"
        )
    lines.extend([
        "", "A missing amount means it is unannotated, not zero. Before comparing numerical results, consult each primary paper for task splits, embodiment, observation and action spaces, baseline resources, metrics, success criteria, and inference costs. No cross-paper ranking is implied.",
    ])
    return "\n".join(lines) + "\n"


def replace_block(source, name, content):
    """Replace the generated content between one pair of named README markers."""
    start, end = f"<!-- {name}:START -->", f"<!-- {name}:END -->"
    if source.count(start) != 1 or source.count(end) != 1:
        raise ValueError(f"README needs exactly one pair of {name} markers")
    prefix, rest = source.split(start, 1)
    _, suffix = rest.split(end, 1)
    return prefix + start + "\n" + content + "\n" + end + suffix


def badge(label, message, colour, alt, href):
    def part(text):
        return text.replace("-", "--").replace("_", "__").replace(" ", "%20")
    return f'<a href="{href}"><img alt="{html.escape(alt, quote=True)}" src="https://img.shields.io/badge/{part(label)}-{part(message)}-{colour}?style=flat-square"></a>'


def render_badges(records, roadmap, daily):
    pending = daily["total"] if daily else 0
    return "\n".join([
        '<a href="https://github.com/sindresorhus/awesome"><img alt="Awesome list" src="https://img.shields.io/badge/awesome-list-162f4b?style=flat-square&logo=awesomelists&logoColor=white"></a>',
        badge("works", str(len(records)), "183c68", f"{len(records)} works in the collection", "#paper-list"),
        badge("roadmap examples", str(len(roadmap)), "234fa0", f"{len(roadmap)} roadmap examples", "#survey-map"),
        badge("daily agent", f"{pending} awaiting review", "0f8b7f", f"Daily research agent: {pending} candidates awaiting review", "#daily-research-agent"),
        badge("suggest", "a paper", "7048c8", "Suggest a paper", f"{REPOSITORY}/issues/new?template=paper.yml"),
    ])


def render_stats(records, roadmap, daily):
    totals = summary(records)
    outside = sum(item["external_reference"] is None for item in roadmap)
    pending = daily["total"] if daily else 0
    return "\n".join([
        f"| **{len(records)}** | **{len(roadmap)}** | **{len(roadmap) - outside}** | **{outside}** | **{totals['annotated']}** | **{pending}** |",
        "| --- | --- | --- | --- | --- | --- |",
        "| works in the collection | examples in our manuscript’s roadmap | roadmap examples in the collection | roadmap examples outside it | works with reading notes | daily candidates awaiting review |",
    ])


def survey_branches(example):
    if example["forms"]:
        return list(example["forms"])
    return sorted({TREE_AREAS[area] for area in example["areas"] if area in TREE_AREAS})


ARXIV_CITATION = re.compile(r"arXiv:(\d{4}\.\d{4,5})")


def featured_title(example, title):
    """Drop a leading "Name:" that would repeat the short name shown in bold."""
    prefix = example["name"].casefold() + ":"
    return title.split(":", 1)[1].strip() if title.casefold().startswith(prefix) else title


def featured_labels(example):
    labels = [ROLE_LABELS[role] for role in example["roles"]]
    if example["self_built"]:
        labels.append("Self-built context")
    labels.extend(REGIME_LABELS[regime] for regime in example["adaptation"])
    return " · ".join(labels) or "—"


def render_featured(records, roadmap):
    by_number = {row["number"]: row for row in records}
    lines = ["Every example our manuscript’s roadmap assigns, grouped like the survey map and newest first. Labels show the role at deployment, self-built context, and deployment updates only where our manuscript assigns them. Works outside the 412-work collection are named by our manuscript, with the arXiv identifier its bibliography cites when it gives one."]
    for heading, keys, section in FEATURED_GROUPS:
        rows = []
        for example in roadmap:
            branches = [key for key in survey_branches(example) if key in keys]
            if not branches:
                continue
            year = example_year(example, by_number)
            if example["external_reference"] is not None:
                record = by_number[example["external_reference"]]
                work = f"**{markdown(example['name'])}** — {markdown(featured_title(example, record['title']))}"
                links = [f"[Paper]({record['paper_url']})"] if record.get("paper_url") else []
                links.append(f"[Catalogue](CATALOGUE.md#{record['id']})")
            else:
                # Titles extracted from our manuscript's bibliography keep PDF line-break artifacts, so name the work only.
                work = f"**{markdown(example['name'])}**"
                arxiv = ARXIV_CITATION.search(example["citation"])
                links = [f"[arXiv](https://arxiv.org/abs/{arxiv.group(1)})"] if arxiv else []
                links.append(f"Our ref. [{example['manuscript_reference']}]")
            area = AREA_LABELS.get(branches[0], "")
            rows.append((-year, example["name"].casefold(), work, year, area, featured_labels(example), " · ".join(links), example["external_reference"] is not None))
        in_collection = sum(row[7] for row in rows)
        lines.extend(["", f"### {heading} · {section}", "", f"{len(rows)} roadmap examples · {in_collection} in the collection", ""])
        with_area = len(keys) > 1
        lines.append("| Work | Year | " + ("Area | " if with_area else "") + "Our manuscript’s labels | Links |")
        lines.append("| --- | --- | " + ("--- | " if with_area else "") + "--- | --- |")
        for _, _, work, year, area, labels, links, _ in sorted(rows):
            lines.append(f"| {work} | {year} | " + (f"{area} | " if with_area else "") + f"{labels} | {links} |")
    return "\n".join(lines)


def render_daily(daily, reports):
    if not daily:
        return "No daily run has been recorded yet."
    latest = reports[-1]
    pending = daily["pending"]
    forms = ", ".join(f"{count} {form}" for form, count in pending.items() if count)
    return "\n".join([
        f"**Latest run:** {daily['date']} · [report](docs/daily-collection/{latest['run_date']}.md) · [summary](docs/daily-collection/{latest['run_date']}.json)",
        "",
        f"**Awaiting human review:** {daily['total']} candidate{'' if daily['total'] == 1 else 's'}" + (f" ({forms})" if forms else "") + ". Candidates stay out of the collection until a reviewer accepts them.",
    ])


def render_readme(source, records, root=ROOT):
    root = Path(root)
    roadmap = json.loads((root / "data" / "manuscript-mapping.json").read_text(encoding="utf-8"))["references"]
    daily = daily_report(root)
    reports = load_daily_reports(root)
    source = replace_block(source, "BADGES", render_badges(records, roadmap, daily))
    source = replace_block(source, "STATS", render_stats(records, roadmap, daily))
    source = replace_block(source, "FEATURED", render_featured(records, roadmap))
    source = replace_block(source, "DAILY", render_daily(daily, reports))
    return replace_block(source, "PAPERS", render_table(records))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify generated Markdown views are current")
    args = parser.parse_args()
    records = validate(load_collection())
    source = README.read_text(encoding="utf-8")
    outputs = {
        README: render_readme(source, records),
        CATALOGUE: render_catalogue(records),
        PROTOCOLS: render_protocols(records),
    }
    if args.check:
        if any(not path.exists() or path.read_text(encoding="utf-8") != content for path, content in outputs.items()):
            raise SystemExit("Generated views are out of date; run python3 scripts/build_readme.py")
        print(f"Validated {len(records)} survey references; generated views are current")
    else:
        for path, content in outputs.items():
            path.write_text(content, encoding="utf-8")
        print(f"Rendered {len(records)} survey references and {summary(records)['annotated']} reading notes")


if __name__ == "__main__":
    main()
