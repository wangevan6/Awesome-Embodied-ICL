#!/usr/bin/env python3
"""Rebuild the survey reference inventory from a local copy of its PDF, without network access.

Requires PyMuPDF (``python3 -m pip install pymupdf``). The PDF is not kept in this
repository: download the authors' copy, which the inventory's SHA-256 identifies,
from https://jethrojames.github.io/awesome-robots-icl/assets/robot-icl-survey.pdf
The bibliography is read from PDF pages 76–95; Appendix A (pages 96–97) is the
classification authority. The script checks that all 412 bibliography entries have
exactly one Appendix A assignment. External URLs come from the bibliography's PDF
link annotations. Run from any directory:
python3 scripts/extract_survey.py path/to/robot-icl-survey.pdf [--check]
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE_NAME = "robot-icl-survey.pdf"
OUTPUT = ROOT / "data" / "survey-references.json"
HEADER = "In-Context Learning for Robots: Methods and Applications"
GROUPS = {
    "C": "Context-conditioned policies",
    "G": "Geometric demonstration transfer",
    "W": "World-model-based control",
    "S": "Skill- and agent-based execution",
}
EXPECTED_COUNTS = {
    "Context-conditioned policies": 123,
    "Geometric demonstration transfer": 24,
    "World-model-based control": 22,
    "Skill- and agent-based execution": 91,
    "Data resources": 44,
    "Evaluation": 39,
    "Foundations and surveys": 40,
    "Training and representations": 29,
}


def collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def expand_numbers(text: str) -> list[int]:
    result = []
    for item in text.strip("[] ").split(","):
        parts = re.split(r"[–-]", item.strip())
        if len(parts) == 2:
            result.extend(range(int(parts[0]), int(parts[1]) + 1))
        else:
            result.append(int(parts[0]))
    return result


def appendix_assignments(doc: fitz.Document) -> dict[int, dict]:
    """Read the actual Appendix A table rather than maintaining a copied list."""
    # Blocks retain each table row and its continuation lines in reading order.
    text = doc[95].get_text()
    text = text.split("References\n", 1)[1]
    text = text.rsplit("\n96", 1)[0]
    # Each row begins with year/family/count, or with a support group heading.
    token_re = re.compile(
        r"(?P<year>20\d{2})\n(?P<family>[CGWS])\n(?P<count>\d+)\n"
        r"|(?P<family_only>[CGWS])\n(?P<count_only>\d+)\n"
        r"|(?P<support>Data resources|Evaluation|Foundations and surveys|Training and representations)\n(?P<support_count>\d+)\n"
    )
    rows = list(token_re.finditer(text))
    assignments = {}
    current_year = None
    for index, match in enumerate(rows):
        if match["year"]:
            current_year = int(match["year"])
        family = match["family"] or match["family_only"]
        group = GROUPS[family] if family else match["support"]
        expected = int(match["count"] or match["count_only"] or match["support_count"])
        end = rows[index + 1].start() if index + 1 < len(rows) else len(text)
        references = []
        for bracket in re.findall(r"\[([^\]]+)\]", text[match.end():end]):
            references.extend(expand_numbers(collapse(bracket)))
        assert len(references) == expected, (group, current_year, expected, references)
        for number in references:
            assert number not in assignments, f"Duplicate Appendix A assignment: {number}"
            assignments[number] = {"survey_group": group}
            if family:
                assignments[number]["first_public_year"] = current_year
    assert set(assignments) == set(range(1, 413)), "Appendix A is incomplete"
    return assignments


def citation_metadata(citation: str) -> tuple[str, str, int]:
    """Separate author, title and date while retaining the full source citation.

    Author initials contain periods, so sentence boundaries must skip initials.
    Question marks can be internal to titles: only treat them as a boundary when
    followed by an explicit venue marker. The inspected source has two such
    markers (arXiv and In). This is intentionally a parser for this PDF version.
    """
    for match in re.finditer(r"\. (?=\S)", citation):
        token = citation[:match.start()].split()[-1]
        pieces = re.split(r"[.\-]", token)
        is_initial = all(len(piece) <= 1 for piece in pieces)
        if not is_initial:
            authors = citation[:match.start() + 1]
            remaining = citation[match.end():]
            break
    else:
        raise ValueError(f"Missing author/title boundary: {citation}")
    boundary = re.search(r"\. |(?<=[?!]) (?=(?:arXiv|In)\b)", remaining)
    assert boundary, f"Missing title boundary: {citation}"
    title = remaining[:boundary.start()]
    title = re.sub(r",\s*(?:19|20)\d{2}$", "", title)
    # Ignore identifier-like year prefixes, and any access-date note after URL.
    dated_part = citation.split(" URL ", 1)[0]
    dated_part = re.sub(r"arXiv:\d{4}\.\d+", "", dated_part)
    dated_part = re.sub(r"doi:\s*\S+", "", dated_part)
    years = re.findall(r"\b((?:19|20)\d{2})\b", dated_part)
    assert years, f"Missing bibliography year: {citation}"
    return authors, title, int(years[-1])


def bibliography(doc: fitz.Document) -> tuple[list[dict], dict[int, list[int]]]:
    references = []
    current = None
    page_numbers = defaultdict(list)
    for page_index in range(75, 95):
        page = doc[page_index]
        external_links = [link for link in page.get_links() if link.get("uri")]
        in_bibliography = page_index > 75
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                text = "".join(span["text"] for span in line["spans"]).strip()
                if text == "References":
                    in_bibliography = True
                    continue
                if not in_bibliography or text in {HEADER, str(page_index + 1)} or not text:
                    continue
                match = re.match(r"^\[(\d+)\]\s+(.*)", text)
                if match:
                    current = {
                        "number": int(match[1]), "_lines": [],
                        "reference_pages": [], "source_urls": [],
                    }
                    references.append(current)
                    page_numbers[page_index].append(current["number"])
                    text = match[2]
                assert current is not None
                current["_lines"].append(text)
                if page_index + 1 not in current["reference_pages"]:
                    current["reference_pages"].append(page_index + 1)
                for link in external_links:
                    # Bibliographic URL annotations overlap the text baseline.
                    box = fitz.Rect(line["bbox"])
                    anchor = link["from"]
                    anchor_center_y = (anchor.y0 + anchor.y1) / 2
                    if box.y0 <= anchor_center_y <= box.y1 and box.intersects(anchor) and link["uri"] not in current["source_urls"]:
                        current["source_urls"].append(link["uri"])
    for record in references:
        record["citation"] = collapse(" ".join(record.pop("_lines")))
        authors, title, year = citation_metadata(record["citation"])
        record.update(authors=authors, title=title, year=year)
        urls = record["source_urls"]
        if urls:
            # Prefer the explicit primary-paper URL when both DOI and URL exist.
            record["paper_url"] = next((url for url in urls if "doi.org/" not in url), urls[0])
        arxiv = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d+)", record.get("paper_url", ""), re.I)
        if arxiv:
            record["arxiv_id"] = arxiv[1]
        doi = re.search(r"doi:\s*(10\.\d{4,9}/\S+)", record["citation"])
        if doi:
            record["doi"] = doi[1].rstrip(".")
    return references, page_numbers


def citation_pages(doc: fitz.Document, starts: dict[int, list[int]]) -> dict[int, list[int]]:
    """Use named PDF citation destinations, excluding the bibliography/index.

    Explicit citation links establish the reference IDs. Printed citation ranges
    are expanded only when both endpoints have matching citation links on that
    page. Appendix B pages 97–100 are included.
    """
    names_by_page = defaultdict(list)
    for name, destination in doc.resolve_names().items():
        if name.startswith("cite."):
            names_by_page[destination["page"]].append((destination["to"][1], name))
    name_to_number = {}
    for page_index, numbers in starts.items():
        names = [name for _, name in sorted(names_by_page[page_index], reverse=True)]
        assert len(names) == len(numbers), (page_index + 1, len(names), len(numbers))
        name_to_number.update(zip(names, numbers))
    pages = defaultdict(set)
    for page_index, page in enumerate(doc):
        if 76 <= page_index <= 95:
            continue
        linked_numbers = set()
        for link in page.get_links():
            name = link.get("nameddest", "")
            if name in name_to_number:
                linked_numbers.add(name_to_number[name])
        for number in linked_numbers:
            pages[number].add(page_index + 1)
        for bracket in re.findall(r"\[([\d\s,–-]+)\]", page.get_text()):
            for start, end in re.findall(r"(\d+)\s*[–-]\s*(\d+)", bracket):
                first, last = int(start), int(end)
                if first in linked_numbers and last in linked_numbers and first < last:
                    for number in range(first, last + 1):
                        pages[number].add(page_index + 1)
    return {number: sorted(values) for number, values in pages.items()}


def build(source: Path) -> dict:
    with fitz.open(source) as doc:
        assert len(doc) == 100, "This extractor targets the repository's 100-page survey"
        assignments = appendix_assignments(doc)
        references, starts = bibliography(doc)
        mentions = citation_pages(doc, starts)
        for record in references:
            record.update(assignments[record["number"]])
            record["mentioned_pages"] = mentions.get(record["number"], [])
    assert [record["number"] for record in references] == list(range(1, 413))
    assert dict(Counter(record["survey_group"] for record in references)) == EXPECTED_COUNTS
    assert all(record["title"] and len(record["title"]) > 10 for record in references)
    assert all(record["authors"] and 1900 <= record["year"] <= 2026 for record in references)
    assert all(record["reference_pages"] for record in references)
    assert all(record["mentioned_pages"] for record in references)
    assert all(record["paper_url"] in re.sub(r"\s", "", record["citation"]) for record in references)
    # These checks exercise author initials, corporate authors, title question
    # marks, titles with embedded versions, and page-spanning entries.
    by_number = {record["number"]: record for record in references}
    assert by_number[81]["title"].startswith("Unpacking Failure Modes")
    assert by_number[2]["paper_url"] == "https://arxiv.org/abs/1611.02779"
    assert by_number[122]["year"] == 2009
    assert by_number[99]["title"] == "Introducing S1: In-Context Learning for Robotics"
    assert by_number[239]["title"].startswith("AGIBOT Releases")
    assert by_number[290]["title"].endswith("Active Exploration?")
    assert by_number[321]["title"].endswith("simple function classes")
    assert by_number[389]["title"].startswith("GLOW:")
    return {
        "source": {
            "filename": SOURCE_NAME,
            "title": HEADER,
            "url": "https://arxiv.org/abs/2609.36012",
            "pages": 100,
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "scope": "All 412 bibliography references, including 260 method-family assignments and 152 supporting references; classification follows Appendix A exactly.",
            "bibliography_pages": [76, 95],
            "classification_pages": [96, 97],
            "reference_count": 412,
            "method_count": 260,
            "supporting_count": 152,
            "group_counts": EXPECTED_COUNTS,
            "year_provenance": "year is the bibliography date; first_public_year is supplied only for method references and follows Table A1.",
            "title_provenance": "PDF text extraction with whitespace normalized and author/date/venue fields separated; original capitalization is preserved. Full citations retain source wording.",
            "url_provenance": "Bibliography PDF link annotations only; source_urls preserves all external links attached to an entry. URLs are transcribed, not independently verified.",
            "mentioned_pages_provenance": "1-based PDF pages containing named citation links or interior members of printed citation ranges whose endpoints have named links on that page. Includes Appendix B; bibliography and Appendix A index are excluded.",
            "rebuild_command": "python3 scripts/extract_survey.py robot-icl-survey.pdf",
        },
        "references": references,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="local copy of the external survey PDF")
    parser.add_argument("--check", action="store_true", help="Compare extraction with the committed inventory without writing")
    args = parser.parse_args()
    inventory = build(args.pdf)
    encoded = json.dumps(inventory, ensure_ascii=False, indent=2) + "\n"
    if args.check:
        assert OUTPUT.read_text() == encoded, "Inventory differs; rerun the extractor"
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(encoded)
    print(f"{'Verified' if args.check else 'Extracted'} {len(inventory['references'])} references; all Appendix A counts match.")


if __name__ == "__main__":
    main()
