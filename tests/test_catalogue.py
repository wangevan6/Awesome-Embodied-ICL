import copy
import json
import re
import unittest

from scripts.build_readme import (
    CATALOGUE, DATA, PROTOCOLS, README, ROOT, render_catalogue, render_protocols,
    render_readme, render_table, validate,
)
from scripts.survey_collection import EXTERNAL_SURVEY_PDF, load_collection, summary, validate_inventory


class CatalogueTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = json.loads(DATA.read_text(encoding="utf-8"))
        cls.records = load_collection()
        cls.by_number = {row["number"]: row for row in cls.records}

    def test_complete_reference_coverage_and_source_snapshot(self):
        source = self.inventory["source"]
        self.assertEqual({row["number"] for row in self.records}, set(range(1, 413)))
        self.assertEqual(len(self.records), 412)
        self.assertEqual(source["reference_count"], 412)
        sources = json.loads((ROOT / "data" / "sources.json").read_text(encoding="utf-8"))
        self.assertEqual(source["sha256"], sources["external_survey"]["sha256"])
        self.assertEqual(sources["external_survey"]["pdf_url"], EXTERNAL_SURVEY_PDF)
        for row in self.records:
            self.assertTrue(row["citation"])
            self.assertTrue(row["reference_pages"])
            self.assertTrue(all(76 <= page <= 95 for page in row["reference_pages"]))
            self.assertEqual(row["survey_url"], f"{EXTERNAL_SURVEY_PDF}#page={row['reference_pages'][0]}")

    def test_appendix_census_and_annotated_subset(self):
        counts = summary(self.records)
        self.assertEqual((counts["references"], counts["methods"], counts["supporting"], counts["annotated"]), (412, 260, 152, 21))
        self.assertEqual(counts["groups"], {
            "Context-conditioned policies": 123,
            "Geometric demonstration transfer": 24,
            "World-model-based control": 22,
            "Skill- and agent-based execution": 91,
            "Data resources": 44,
            "Evaluation": 39,
            "Foundations and surveys": 40,
            "Training and representations": 29,
        })

    def test_inventory_rejects_missing_reference_and_changed_family(self):
        missing = copy.deepcopy(self.inventory)
        missing["references"].pop()
        with self.assertRaisesRegex(ValueError, "exactly once"):
            validate_inventory(missing)
        changed = copy.deepcopy(self.inventory)
        changed["references"][0]["survey_group"] = "World-model-based control"
        with self.assertRaisesRegex(ValueError, "Appendix A"):
            validate_inventory(changed)

    def test_unmatched_legacy_papers_are_excluded(self):
        audits = json.loads((ROOT / "data/survey-annotations.json").read_text())
        legacy = json.loads((ROOT / "data/papers.json").read_text())
        self.assertEqual({row["paper_id"] for row in audits}, {row["id"] for row in legacy})
        absent = {row["paper_id"] for row in audits if row["survey_reference"] is None}
        self.assertEqual(absent, {"robossm-2025", "decompose-recompose-2026"})
        self.assertFalse(absent.intersection(row["id"] for row in self.records))
        catalogue = render_catalogue(self.records)
        for paper_id in absent:
            self.assertNotIn(f'<a id="{paper_id}">', catalogue)

    def test_annotations_follow_survey_interfaces(self):
        self.assertEqual(self.by_number[155]["family"], "Context-conditioned policies")
        self.assertEqual(self.by_number[41]["family"], "Context-conditioned policies")
        self.assertEqual(self.by_number[156]["family"], "Geometric demonstration transfer")
        self.assertEqual(self.by_number[24]["family"], "World-model-based control")
        self.assertIn("future clip", self.by_number[24]["action_mechanism"])
        self.assertIn("without generating", self.by_number[181]["action_mechanism"])
        self.assertEqual(self.by_number[92]["context_budget"], "10 demonstrations per task in main TWIN experiments")
        self.assertIn("fine-tuning", self.by_number[154]["test_time_weights"])

    def test_date_basis_preserves_publication_distinction(self):
        self.assertEqual((self.by_number[154]["year"], self.by_number[154]["bibliography_year"]), (2024, 2025))
        self.assertEqual((self.by_number[202]["year"], self.by_number[202]["bibliography_year"]), (2023, 2024))
        self.assertEqual(self.by_number[154]["year_basis"], "Appendix A first public year")
        support = next(row for row in self.records if not row["is_method"])
        self.assertEqual(support["year_basis"], "Bibliography year")
        self.assertEqual(support["year"], support["bibliography_year"])

    def test_every_reference_has_document_link_and_pdf_provenance(self):
        table = render_table(validate(self.records))
        catalogue = render_catalogue(self.records)
        self.assertEqual(catalogue.count('<a id="'), 412)
        for row in self.records:
            self.assertIn(f"CATALOGUE.md#{row['id']}", table)
            self.assertIn(f'<a id="{row["id"]}"></a>', catalogue)
            self.assertIn(f"{EXTERNAL_SURVEY_PDF}#page={row['reference_pages'][0]}", catalogue)
            if row.get("paper_url"):
                self.assertIn(row["paper_url"], catalogue)

    def test_bibliography_only_entries_have_no_fabricated_evidence(self):
        unannotated = [row for row in self.records if not row["annotated"]]
        self.assertEqual(len(unannotated), 391)
        for row in unannotated:
            for key in ("evidence", "context_budget", "test_time_weights", "setting", "action_mechanism"):
                self.assertNotIn(key, row)
        catalogue = render_catalogue(self.records)
        self.assertEqual(catalogue.count("Per-paper deployment and evaluation details have not been annotated."), 391)
        self.assertNotIn("All listed methods use frozen", catalogue + render_table(self.records))
        self.assertIn("parameter-adaptation comparisons", catalogue)
        # Weight-updating comparison branches remain valid catalogue records.
        changed = copy.deepcopy(self.records)
        changed[0]["test_time_weights"] = "updated"
        validate(changed)

    def test_context_amount_view_uses_only_audited_nonempty_values(self):
        protocols = render_protocols(self.records)
        included = {row["id"] for row in self.records if row.get("annotated") and row.get("context_budget")}
        self.assertEqual(included, {"one-shot-imitation-2017", "bicicle-2026", "relic-2024"})
        for row in self.records:
            self.assertEqual(f"CATALOGUE.md#{row['id']}" in protocols, row["id"] in included)
        self.assertIn("paper title", protocols)
        self.assertIn("not zero", protocols)

    def test_generated_markdown_is_current_and_reading_links_resolve(self):
        source = README.read_text(encoding="utf-8")
        self.assertEqual(source, render_readme(source, self.records))
        self.assertEqual(CATALOGUE.read_text(encoding="utf-8"), render_catalogue(self.records))
        self.assertEqual(PROTOCOLS.read_text(encoding="utf-8"), render_protocols(self.records))
        ids = {row["id"] for row in self.records}
        for anchor in re.findall(r"CATALOGUE\.md#([a-z0-9-]+)", source):
            self.assertIn(anchor, ids)
        for name in ("BADGES", "STATS", "FEATURED", "DAILY", "PAPERS"):
            with self.assertRaisesRegex(ValueError, f"pair of {name} markers"):
                render_readme(source.replace(f"<!-- {name}:END -->", "", 1), self.records)

    def test_readme_highlights_follow_the_data(self):
        source = README.read_text(encoding="utf-8")
        roadmap = json.loads((ROOT / "data" / "manuscript-mapping.json").read_text(encoding="utf-8"))["references"]
        outside = [item for item in roadmap if item["external_reference"] is None]
        stats = source.split("<!-- STATS:START -->", 1)[1].split("<!-- STATS:END -->", 1)[0]
        self.assertIn(f"| **{len(self.records)}** | **{len(roadmap)}** | **{len(roadmap) - len(outside)}** | **{len(outside)}** |", stats)
        badges = source.split("<!-- BADGES:START -->", 1)[1].split("<!-- BADGES:END -->", 1)[0]
        self.assertIn(f"badge/works-{len(self.records)}-", badges)
        featured = source.split("<!-- FEATURED:START -->", 1)[1].split("<!-- FEATURED:END -->", 1)[0]
        for item in roadmap:
            self.assertIn(f"**{item['name']}**", featured)
        for item in outside:
            self.assertIn(f"Our ref. [{item['manuscript_reference']}]", featured)
        for number in {item["external_reference"] for item in roadmap} - {None}:
            self.assertIn(f"CATALOGUE.md#{self.by_number[number]['id']}", featured)


if __name__ == "__main__":
    unittest.main()
