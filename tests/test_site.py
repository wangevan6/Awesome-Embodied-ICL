import copy
from html.parser import HTMLParser
import json
from pathlib import Path
import tempfile
import unittest
from urllib.parse import urljoin, urlparse

from scripts.survey_collection import EXPECTED_COUNTS, EXTERNAL_SURVEY_PDF, METHOD_GROUPS, load_collection, ordered
from scripts.build_site import (
    PUBLIC_DOCS, PUBLIC_LOGOS, ROOT, check_site, daily_report, load_daily_reports, render_cards, render_files,
    render_markdown, script_json, write_site,
)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.articles = {}
        self.links = []
        self.elements = []
        self.ids = []
        self.sections = []
        self.section_content = {}
        self._sections = []
        self.script_payload = ""
        self._article = None
        self._paper_data = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "section":
            section = attrs.get("id") or ("hero" if "hero" in attrs.get("class", "").split() else "")
            if not self._sections:
                self.sections.append(section)
            self._sections.append(section)
            self.section_content.setdefault(section, {"text": [], "elements": []})
        for section in self._sections:
            self.section_content[section]["elements"].append((tag, attrs))
        if tag == "article" and "paper-card" in attrs.get("class", "").split():
            self._article = attrs["id"]
            self.articles[self._article] = {"text": [], "links": [], "compare": [], "attrs": attrs}
        if tag == "script" and attrs.get("id") == "paper-data":
            self._paper_data = True
        if tag in ("a", "link", "script"):
            link = attrs.get("href", attrs.get("src"))
            if link:
                self.links.append(link)
                if self._article:
                    self.articles[self._article]["links"].append(link)
        if tag == "input" and "data-compare" in attrs and self._article:
            self.articles[self._article]["compare"].append(attrs)

    def handle_endtag(self, tag):
        if tag == "article":
            self._article = None
        if tag == "script":
            self._paper_data = False
        if tag == "section" and self._sections:
            self._sections.pop()

    def handle_data(self, text):
        if self._article:
            self.articles[self._article]["text"].append(text)
        if self._paper_data:
            self.script_payload += text
        for section in self._sections:
            self.section_content[section]["text"].append(text)


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_collection()
        cls.inventory = json.loads((ROOT / "data/survey-references.json").read_text(encoding="utf-8"))
        cls.annotations = json.loads((ROOT / "data/survey-annotations.json").read_text(encoding="utf-8"))
        cls.files = render_files()
        cls.page = PageParser()
        cls.page.feed(cls.files["index.html"].decode("utf-8"))

    def test_every_record_and_research_fact_is_available_without_javascript(self):
        self.assertEqual(list(self.page.articles), [row["id"] for row in ordered(self.records)])
        text_fields = ("year", "title", "authors", "citation", "family", "context", "action_mechanism", "setting",
                       "evidence", "why_it_matters", "adaptation_target", "limitation", "test_time_weights")
        for row in self.records:
            with self.subTest(paper=row["id"]):
                card = self.page.articles[row["id"]]
                text = " ".join(card["text"])
                for field in text_fields:
                    if field in row:
                        self.assertIn(str(row[field]), text)
                self.assertNotIn("hidden", card["attrs"])
                self.assertIn(f'[{row["number"]}]', text)
                if "context_budget" in row:
                    self.assertIn(row["context_budget"], text)
                expected_links = {row["survey_url"]}
                if row.get("paper_url"):
                    expected_links.add(row["paper_url"])
                if row.get("project_url"):
                    expected_links.add(row["project_url"])
                for field in ("reference_pages", "mentioned_pages", "annotation_pages"):
                    expected_links.update(f"{EXTERNAL_SURVEY_PDF}#page={page}" for page in row.get(field, []))
                self.assertEqual(set(card["links"]), expected_links)
                self.assertEqual(len(card["compare"]), 1)
                self.assertEqual(card["compare"][0]["data-compare"], row["id"])
                self.assertEqual(card["compare"][0]["aria-label"], f'Compare {row["title"]}')
        self.assertEqual(len(self.page.ids), len(set(self.page.ids)))
        self.assertEqual(json.loads(self.page.script_payload), ordered(self.records))
        self.assertEqual(json.loads(self.files["data/collection.json"]), ordered(self.records))
        for name in ("papers.json", "survey-references.json", "survey-annotations.json"):
            self.assertEqual(self.files[f"data/{name}"], (ROOT / "data" / name).read_bytes())

    def test_collection_matches_every_survey_reference_and_assignment(self):
        self.assertEqual(len(self.records), 412)
        self.assertEqual({row["number"] for row in self.records}, set(range(1, 413)))
        self.assertEqual(len({row["id"] for row in self.records}), 412)
        source_by_number = {row["number"]: row for row in self.inventory["references"]}
        for row in self.records:
            source = source_by_number[row["number"]]
            with self.subTest(reference=row["number"]):
                for field in ("title", "authors", "citation", "reference_pages", "mentioned_pages"):
                    self.assertEqual(row[field], source[field])
                self.assertEqual(row["family"], source["survey_group"])
                self.assertEqual(row["year"], source.get("first_public_year") or source["year"])
                self.assertEqual(row["is_method"], row["family"] in METHOD_GROUPS)
        self.assertEqual({group: sum(row["family"] == group for row in self.records) for group in EXPECTED_COUNTS}, EXPECTED_COUNTS)
        self.assertEqual(sum(row["is_method"] for row in self.records), 260)

    def test_research_notes_are_explicit_and_not_inferred_from_survey_membership(self):
        mapped = {row["survey_reference"]: row for row in self.annotations if row["survey_reference"] is not None}
        annotated = [row for row in self.records if row["annotated"]]
        self.assertEqual(len(annotated), 21)
        self.assertEqual({row["id"] for row in annotated}, {audit["paper_id"] for audit in mapped.values()})
        original = {row["id"]: row for row in json.loads(self.files["data/papers.json"])}
        research_fields = ("context", "action_mechanism", "test_time_weights", "evidence", "evidence_tier",
                           "setting", "limitation", "context_budget", "adaptation_target", "why_it_matters")
        for row in self.records:
            with self.subTest(reference=row["number"]):
                card_text = " ".join(self.page.articles[row["id"]]["text"])
                if row["annotated"]:
                    audit = mapped[row["number"]]
                    expected_note = {**original[row["id"]], **audit.get("updates", {})}
                    self.assertEqual(row["annotation_pages"], audit["annotation_pages"])
                    for field in research_fields:
                        self.assertEqual(row.get(field), expected_note.get(field) or None)
                else:
                    self.assertEqual(row["id"], f'ref-{row["number"]}')
                    self.assertTrue(all(field not in row for field in research_fields))
                    self.assertIn("Not yet annotated", card_text)
                    self.assertNotIn("Deployment weights", card_text)

    def test_external_survey_is_linked_on_arxiv_and_never_published(self):
        source = self.inventory["source"]
        sources = json.loads(self.files["data/sources.json"])
        self.assertEqual(sources["external_survey"]["sha256"], source["sha256"])
        self.assertEqual(sources["external_survey"]["pdf_url"], EXTERNAL_SURVEY_PDF)
        self.assertEqual([name for name in self.files if name.lower().endswith(".pdf")], [])

    def test_survey_structure_is_the_main_section_immediately_after_hero(self):
        self.assertEqual(self.page.sections[:3], ["hero", "guide", "catalogue"])
        guide = self.page.section_content["guide"]
        forms = [attrs["data-form"] for tag, attrs in guide["elements"] if tag == "a" and "data-form" in attrs]
        roles = [attrs["data-role"] for tag, attrs in guide["elements"] if tag == "a" and "data-role" in attrs]
        self.assertEqual(forms, ["text", "visual", "trajectory", "multimodal"])
        self.assertEqual(roles, ["task", "state", "behavior"])
        guide_text = " ".join(guide["text"]).lower()
        for concept in ("self-built context", "gradients at deployment", "beyond manipulation", "evaluation", "six open problems"):
            self.assertIn(concept, guide_text)
        self.assertFalse(any("data-family" in attrs for tag, attrs in guide["elements"]))
        self.assertNotIn("learning horizons", guide_text)
        self.assertTrue(all(not attrs.get("href", "").startswith(EXTERNAL_SURVEY_PDF) for tag, attrs in guide["elements"]))
        for anchor in ("guide-axes", "guide-evaluation", "guide-roadmap"):
            self.assertIn(anchor, self.page.ids)

    def test_survey_map_tree_places_every_roadmap_example_and_only_counts_daily_candidates(self):
        self.assertEqual(self.page.sections[:3], ["hero", "guide", "catalogue"])
        catalogue = self.page.section_content["catalogue"]
        leaves = [attrs for tag, attrs in catalogue["elements"] if "t-leaf" in attrs.get("class", "").split()]
        roadmap = json.loads(self.files["data/manuscript-mapping.json"])["references"]
        placed = [attrs for attrs in leaves if "t-new" not in attrs["class"].split()]
        expected = sum(max(1, len(item["forms"])) for item in roadmap)
        self.assertEqual(len(placed), expected)
        catalogue_text = " ".join(catalogue["text"])
        for item in roadmap:
            self.assertIn(item["name"], catalogue_text)
        external = {item["external_reference"] for item in roadmap if item["external_reference"] is not None}
        linked = {int(attrs["href"].split("%5B")[1].split("%5D")[0]) for attrs in placed if "t-in" in attrs["class"].split()}
        self.assertEqual(linked, external)
        for attrs in placed:
            if "t-out" in attrs["class"].split():
                self.assertNotIn("href", attrs)  # Our manuscript is not public yet.
        pending = [attrs for attrs in leaves if "t-new" in attrs["class"].split()]
        self.assertTrue(all(attrs.get("href") is None for attrs in pending))
        self.assertNotIn("ViGAR", catalogue_text)  # Unreviewed candidates are counted, never named.
        branches = [attrs["data-form"] for tag, attrs in catalogue["elements"] if tag == "a" and "data-form" in attrs]
        self.assertEqual(branches, ["text", "visual", "trajectory", "multimodal"])
        agent = [attrs for tag, attrs in self.page.elements if "agent-float" in attrs.get("class", "").split()]
        self.assertEqual(agent[0]["data-run-hour"], "7")

    def test_daily_research_reports_are_valid_new_candidates_awaiting_review(self):
        reports = load_daily_reports(ROOT)
        self.assertTrue(reports)
        known_ids = {row["arxiv_id"] for row in self.inventory["references"] if row.get("arxiv_id")}
        known_titles = {row["title"].casefold() for row in self.inventory["references"]}
        roadmap = json.loads(self.files["data/manuscript-mapping.json"])["references"]
        known_titles |= {item["title"].casefold() for item in roadmap}
        seen = set()
        for report in reports:
            for candidate in report["candidates"]:
                with self.subTest(report=report["run_date"], candidate=candidate["name"]):
                    self.assertNotIn(candidate["arxiv_id"], known_ids)
                    self.assertNotIn(candidate["title"].casefold(), known_titles)
                    self.assertNotIn(candidate["arxiv_id"], seen)
                    self.assertTrue(candidate["url"].startswith(f"https://arxiv.org/abs/{candidate['arxiv_id']}"))
                    self.assertLessEqual(candidate["submitted"], report["run_date"])
                    seen.add(candidate["arxiv_id"])
        pending = sum(candidate["decision"] == "pending" for report in reports for candidate in report["candidates"])
        self.assertEqual(daily_report(ROOT)["total"], pending)
        page = self.files["index.html"].decode("utf-8")
        self.assertIn(f"{pending} candidate{'' if pending == 1 else 's'} awaiting human review", page)
        for report in reports:
            for candidate in report["candidates"]:
                self.assertNotIn(candidate["title"], page)  # Candidates are counted on the site, never published.

    def test_source_ownership_is_recorded_without_publishing_either_pdf(self):
        sources = json.loads(self.files["data/sources.json"])
        self.assertEqual(sources["manuscript"]["title"], "In-Context Learning for Embodied Agents: Methods, Benchmarks, and Open Challenges")
        self.assertEqual(sources["external_survey"]["title"], "In-Context Learning for Robots: Methods and Applications")
        self.assertEqual(sources["manuscript"]["ownership"], "our work")
        self.assertEqual(sources["external_survey"]["ownership"], "external work")
        self.assertNotIn("filename", sources["manuscript"])  # The draft's local file name stays private.
        for key in ("manuscript", "external_survey"):
            self.assertRegex(sources[key]["sha256"], r"^[0-9a-f]{64}$")
        self.assertEqual([name for name in self.files if name.lower().endswith(".pdf")], [])

    def test_manuscript_identity_mapping_keeps_all_external_and_own_only_works(self):
        roadmap = json.loads(self.files["data/manuscript-mapping.json"])["references"]
        self.assertEqual(len(roadmap), 67)
        self.assertEqual(sum(row["framework_mapped"] for row in self.records), 38)
        self.assertEqual(sum(item["external_reference"] is None for item in roadmap), 29)
        own = {item["manuscript_reference"]: item for item in roadmap}
        external = {row["number"]: row for row in self.records}
        self.assertEqual(own[7]["external_reference"], 13)  # ICRT: different reference numbers.
        self.assertEqual(external[13]["context_forms"], ["trajectory"])
        self.assertEqual(external[13]["context_roles"], ["behavior"])
        self.assertEqual(external[24]["context_forms"], ["visual"])
        self.assertEqual(external[24]["context_roles"], ["task"])
        self.assertEqual(external[10]["adaptation_regimes"], ["update-dependent"])
        self.assertEqual(external[17]["adaptation_regimes"], ["gradient-free", "update-optional"])
        self.assertIsNone(own[44]["external_reference"])  # RoboSSM is in OUR manuscript.
        self.assertEqual(own[44]["name"], "RoboSSM")
        self.assertIn("RoboSSM", " ".join(self.page.section_content["guide"]["text"]))
        for row in self.records:
            if not row["framework_mapped"]:
                self.assertEqual(row["context_forms"], [])
                self.assertEqual(row["context_roles"], [])
                self.assertIsNone(row["manuscript_reference"])

    def test_html_text_and_attributes_are_escaped(self):
        row = copy.deepcopy(next(record for record in self.records if record["annotated"]))
        row["title"] = 'A "quoted" title & <img src=x onerror=alert(1)>'
        row["context"] = "O'Brien <script>alert(2)</script> & context"
        row["paper_url"] = 'https://example.com/?q=" onmouseover="alert(3)&x=1'
        html = render_cards([row])
        parser = PageParser()
        parser.feed(html)
        card = parser.articles[row["id"]]
        self.assertIn(row["title"], " ".join(card["text"]))
        self.assertIn(row["context"], " ".join(card["text"]))
        self.assertEqual(card["compare"][0]["aria-label"], f'Compare {row["title"]}')
        self.assertIn(row["paper_url"], card["links"])
        self.assertNotIn("<img", html)
        self.assertNotIn("<script", html)
        self.assertNotIn(' onmouseover="alert', html)

    def test_embedded_json_cannot_close_script_element(self):
        records = [{"text": '</script><script>alert("x")</script><!-- & >\u2028\u2029'}]
        payload = script_json(records)
        self.assertNotIn("<", payload)
        self.assertNotIn(">", payload)
        self.assertNotIn("&", payload)
        self.assertNotIn("\u2028", payload)
        self.assertNotIn("\u2029", payload)
        parser = PageParser()
        parser.feed(f'<script id="paper-data" type="application/json">{payload}</script>')
        self.assertEqual(json.loads(parser.script_payload), records)

    def test_publish_output_is_an_exact_allowlist(self):
        expected = {"index.html", "styles.css", "app.js", "favicon.svg", "sjtu-emblem.png", "figure-1.jpg", "data/papers.json", ".nojekyll",
                    "data/collection.json", "data/survey-references.json", "data/survey-annotations.json", "data/sources.json", "data/manuscript-mapping.json",
                    "README.md", "CATALOGUE.md", "PROTOCOLS.md", "QUALITY.md", "CONTRIBUTING.md",
                    "README.html", "CATALOGUE.html", "PROTOCOLS.html", "QUALITY.html", "CONTRIBUTING.html"}
        expected.update(PUBLIC_LOGOS)
        self.assertEqual(set(self.files), expected)
        for document in PUBLIC_DOCS:
            self.assertEqual(self.files[document], (ROOT / document).read_bytes())
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "public"
            write_site(self.files, output)
            self.assertEqual({path.relative_to(output).as_posix() for path in output.rglob("*") if path.is_file()}, expected)
            check_site(self.files, output)
            (output / "private-notes.pdf").write_bytes(b"not public")
            with self.assertRaisesRegex(ValueError, "file list differs"):
                check_site(self.files, output)
            with self.assertRaisesRegex(ValueError, "Unexpected output files"):
                write_site(self.files, output)
            self.assertEqual((output / "private-notes.pdf").read_bytes(), b"not public")

    def test_check_detects_stale_and_missing_files(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "public"
            with self.assertRaisesRegex(ValueError, "file list differs"):
                check_site(self.files, output)
            write_site(self.files, output)
            (output / "styles.css").write_text("stale", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "out of date: styles.css"):
                check_site(self.files, output)

    def test_output_rejects_links_to_private_files(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "public"
            output.mkdir()
            private = Path(directory) / "private"
            private.mkdir()
            (output / "data").symlink_to(private, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "symlinks"):
                write_site(self.files, output)

    def test_output_cannot_overwrite_the_source_template(self):
        with self.assertRaisesRegex(ValueError, "separate from project source"):
            write_site(self.files, ROOT / "site")

    def test_local_links_and_assets_work_under_a_repository_base_path(self):
        base = "https://example.github.io/embodied-research/"
        local_assets = set()
        for link in self.page.links:
            parsed = urlparse(link)
            if parsed.scheme or parsed.netloc:
                continue
            if not parsed.path:
                if parsed.fragment:
                    self.assertIn(parsed.fragment, self.page.ids)
                continue
            self.assertFalse(parsed.path.startswith("/"), link)
            resolved = urlparse(urljoin(base, link)).path
            self.assertTrue(resolved.startswith("/embodied-research/"), link)
            relative = resolved.removeprefix("/embodied-research/") or "index.html"
            self.assertIn(relative, self.files, link)
            local_assets.add(relative)
        self.assertTrue({"styles.css", "app.js", "favicon.svg", "data/collection.json"} <= local_assets)

    def test_reading_page_links_and_fragments_resolve(self):
        pages = {}
        for filename, content in self.files.items():
            if filename.endswith(".html"):
                parser = PageParser()
                parser.feed(content.decode("utf-8"))
                pages[filename] = parser
        for record in self.records:
            self.assertIn(record["id"], pages["CATALOGUE.html"].ids)
        for filename, page in pages.items():
            self.assertEqual(len(page.ids), len(set(page.ids)))
            if filename != "index.html":
                document = filename.removesuffix(".html") + ".md"
                downloads = [attrs["href"] for tag, attrs in page.elements if tag == "a" and "download" in attrs]
                self.assertEqual(downloads, [document])
            for tag, attrs in page.elements:
                if tag != "a" or "href" not in attrs:
                    continue
                parsed = urlparse(attrs["href"])
                if attrs["href"].startswith(EXTERNAL_SURVEY_PDF + "#"):
                    self.assertRegex(parsed.fragment, r"^page=[1-9]\d*$")
                    self.assertLessEqual(int(parsed.fragment.removeprefix("page=")), 100)
                if parsed.scheme or parsed.netloc:
                    continue
                target = parsed.path or filename
                if target == "./":
                    target = "index.html"
                self.assertIn(target, self.files)
                if target.endswith(".md"):
                    self.assertIn("download", attrs)
                if parsed.fragment:
                    self.assertIn(parsed.fragment, pages[target].ids, f"{filename}: {attrs['href']}")
            if filename != "index.html":
                self.assertNotIn("<script", self.files[filename].decode("utf-8"))

    def test_github_only_blocks_are_not_published(self):
        html = render_markdown("# Title\n\n<!-- github-only:start -->\n<p align=\"center\"><img src=\"banner.png\"></p>\n```mermaid\nflowchart LR\n```\n<!-- github-only:end -->\n\nShared text.\n")
        self.assertIn("<p>Shared text.</p>", html)
        self.assertNotIn("banner.png", html)
        self.assertNotIn("mermaid", html)
        with self.assertRaisesRegex(ValueError, "Unclosed GitHub-only block"):
            render_markdown("<!-- github-only:start -->\nText\n")
        with self.assertRaisesRegex(ValueError, "Nested GitHub-only block"):
            render_markdown("<!-- github-only:start -->\n<!-- github-only:start -->\n<!-- github-only:end -->\n")

    def test_document_markdown_is_readable_and_escapes_untrusted_html(self):
        escaped = render_markdown(r"# Text &amp; escaped \_underscore\_ and \[brackets\]")
        self.assertIn("Text &amp; escaped _underscore_ and [brackets]", escaped)
        self.assertNotIn("&amp;amp;", escaped)
        self.assertNotIn("<em>", escaped)
        source = '''# Example

A **bold** and *emphasized* paragraph with `inline code` and [catalogue](CATALOGUE.md#icrt-2024).

Source: [`build_readme.py`](scripts/build_readme.py).

<a id="authored-anchor"></a>

## Example

1. First item
2. Second item

- Bullet item

| Field | Meaning |
| --- | --- |
| `context` | Available examples |

```html
<img src=x onerror=alert(1)>
```

<script>alert(2)</script>
<a id="unsafe" onclick="alert(3)"></a>
[Unsafe link](javascript:alert(4))
'''
        html = render_markdown(source)
        parser = PageParser()
        parser.feed(html)
        self.assertIn('<h1 id="example">Example</h1>', html)
        self.assertIn('<h2 id="example-1">Example</h2>', html)
        self.assertIn('<a id="authored-anchor"></a>', html)
        self.assertIn('<a href="CATALOGUE.html#icrt-2024">catalogue</a>', html)
        self.assertIn("<strong>bold</strong>", html)
        self.assertIn("<em>emphasized</em>", html)
        self.assertIn("<code>inline code</code>", html)
        self.assertIn("Source: <code>build_readme.py</code>.", html)
        self.assertNotIn('href="scripts/', html)
        self.assertIn("<ol>\n<li>First item</li>\n<li>Second item</li>\n</ol>", html)
        self.assertIn("<ul>\n<li>Bullet item</li>\n</ul>", html)
        self.assertIn('class="table-scroll"', html)
        self.assertIn('<th scope="col">Field</th>', html)
        self.assertIn("&lt;img src=x onerror=alert(1)&gt;", html)
        self.assertIn("&lt;script&gt;alert(2)&lt;/script&gt;", html)
        self.assertFalse(any(tag in ("script", "img") for tag, _ in parser.elements))
        self.assertFalse(any(any(key.startswith("on") for key in attrs) for _, attrs in parser.elements))
        self.assertFalse(any(link.startswith("javascript:") for link in parser.links))


if __name__ == "__main__":
    unittest.main()
