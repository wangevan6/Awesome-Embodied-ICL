"""Preserve an external inventory; organize it with our manuscript framework."""

import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
METHOD_GROUPS = (
    "Context-conditioned policies",
    "Geometric demonstration transfer",
    "World-model-based control",
    "Skill- and agent-based execution",
)
SUPPORT_GROUPS = (
    "Data resources", "Evaluation", "Foundations and surveys", "Training and representations",
)
GROUPS = METHOD_GROUPS + SUPPORT_GROUPS
CONTEXT_FORMS = {"text": "Text", "visual": "Visual", "trajectory": "Trajectory", "multimodal": "Multimodal"}
CONTEXT_ROLES = {"task": "Task specification", "state": "State representation", "behavior": "Behavior specification"}

EXPECTED_COUNTS = dict(zip(GROUPS, (123, 24, 22, 91, 44, 39, 40, 29)))
# arXiv v1 has the same 100-page pagination as the copy the inventory was extracted from.
EXTERNAL_SURVEY_PDF = "https://arxiv.org/pdf/2609.36012v1"


def read_json(root, name):
    return json.loads((Path(root) / "data" / name).read_text(encoding="utf-8"))


def validate_inventory(inventory):
    records = inventory["references"]
    numbers = [record["number"] for record in records]
    if len(numbers) != 412 or set(numbers) != set(range(1, 413)):
        raise ValueError("Survey index must contain each PDF reference [1]–[412] exactly once")
    counts = Counter(record["survey_group"] for record in records)
    if counts != Counter(EXPECTED_COUNTS):
        raise ValueError(f"Survey assignments differ from Appendix A: {dict(counts)}")
    for record in records:
        for field in ("title", "authors", "citation"):
            if not isinstance(record.get(field), str) or not record[field].strip():
                raise ValueError(f"Reference {record['number']} needs {field}")
        if not record.get("reference_pages") or any(not 76 <= p <= 95 for p in record["reference_pages"]):
            raise ValueError(f"Reference {record['number']} has invalid bibliography pages")
        if any(not 1 <= p <= 100 for p in record.get("mentioned_pages", [])):
            raise ValueError("Invalid survey mention page")
        if record.get("paper_url"):
            parsed = urlparse(record["paper_url"])
            if parsed.scheme not in ("https", "http") or not parsed.netloc:
                raise ValueError(f"Reference {record['number']} has an invalid source URL")
    return inventory


def load_collection(root=ROOT):
    inventory = validate_inventory(read_json(root, "survey-references.json"))
    framework = read_json(root, "manuscript-mapping.json")["references"]
    manuscript = {}
    for item in framework:
        number = item["external_reference"]
        if number is None:
            continue
        if number in manuscript or not 1 <= number <= 412:
            raise ValueError("Manuscript mapping must use distinct valid external reference numbers")
        if not set(item["forms"]) <= CONTEXT_FORMS.keys() or not set(item["roles"]) <= CONTEXT_ROLES.keys():
            raise ValueError("Unknown manuscript axis")
        if not item["manuscript_pages"] or any(not 1 <= page <= 15 for page in item["manuscript_pages"]):
            raise ValueError("Manuscript mapping needs valid manuscript evidence pages")
        manuscript[number] = item
    original_notes = {row["id"]: row for row in read_json(root, "papers.json")}
    audits = read_json(root, "survey-annotations.json")
    if {row["paper_id"] for row in audits} != set(original_notes):
        raise ValueError("Every existing reading note must be reconciled with the survey")
    mapped = {}
    for audit in audits:
        number = audit.get("survey_reference")
        if number is None:
            continue
        if number in mapped or not 1 <= number <= 412:
            raise ValueError("Reading notes must map to distinct survey references")
        if not audit.get("annotation_pages"):
            raise ValueError("A reading note needs supporting survey pages")
        mapped[number] = audit
    collection = []
    note_fields = ("context", "action_mechanism", "test_time_weights", "setting", "evidence",
                   "why_it_matters", "adaptation_target", "evidence_tier", "limitation", "context_budget", "project_url")
    for ref in inventory["references"]:
        number = ref["number"]
        row = {
            **ref,
            "id": f"ref-{number}",
            "year": ref.get("first_public_year") or ref["year"],
            "bibliography_year": ref["year"],
            "year_basis": "Appendix A first public year" if ref.get("first_public_year") else "Bibliography year",
            "family": ref["survey_group"],
            "is_method": ref["survey_group"] in METHOD_GROUPS,
            "annotated": number in mapped,
            "survey_url": f"{EXTERNAL_SURVEY_PDF}#page={ref['reference_pages'][0]}",
        }
        axis = manuscript.get(number)
        row.update({
            "framework_mapped": axis is not None,
            "context_forms": axis["forms"] if axis else [],
            "context_roles": axis["roles"] if axis else [],
            "context_form_labels": ", ".join(CONTEXT_FORMS[key] for key in axis["forms"]) if axis else "",
            "context_role_labels": ", ".join(CONTEXT_ROLES[key] for key in axis["roles"]) if axis else "",
            "adaptation_regimes": axis["adaptation"] if axis else [],
            "manuscript_reference": axis["manuscript_reference"] if axis else None,
            "manuscript_pages": axis["manuscript_pages"] if axis else [],
            "framework_areas": axis["areas"] if axis else [],
            "source_authority": "external_survey",
        })
        if axis:
            row["acronym"] = axis["name"]
        if number in mapped:
            audit = mapped[number]
            note = {**original_notes[audit["paper_id"]], **audit.get("updates", {})}
            row.update({key: note[key] for key in note_fields if note.get(key)})
            row["id"] = audit["paper_id"]
            row["legacy_family"] = original_notes[audit["paper_id"]]["family"]
            row["annotation_pages"] = audit["annotation_pages"]
            # Use the survey's title, date, group and bibliography URL as the index truth.
            # A reviewed original primary link is retained only when the PDF lacks one.
            if not row.get("paper_url"):
                row["paper_url"] = note["paper_url"]
                row["url_provenance"] = "Existing reviewed reading note"
        collection.append(row)
    return collection


def ordered(records):
    return sorted(records, key=lambda row: (-row["year"], row["number"]))


def summary(records):
    return {
        "references": len(records),
        "methods": sum(row["is_method"] for row in records),
        "supporting": sum(not row["is_method"] for row in records),
        "mapped": sum(row["framework_mapped"] for row in records),
        "annotated": sum(row["annotated"] for row in records),
        "groups": dict(Counter(row["family"] for row in records)),
    }
