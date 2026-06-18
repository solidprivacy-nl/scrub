from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_ROOT = REPO_ROOT / "corpus"

PERSON_GAP_REVIEW_INVENTORY = [
    "Hassan El Amrani",
    "Mila van Dijk",
    "Ahmed El Idrissi",
    "Bakker",
    "Sara El Idrissi",
    "Youssef Ait Ben",
    "Fatima Zahra",
    "Lina de Vries",
    "Omar Ben Salah",
    "Nora El Yassini",
    "Tariq de Jong",
    "Noor van Dijk",
    "Sami El Amrani",
    "Jansen",
    "Fatima El Amrani",
]

CONTEXT_CATEGORY_EXAMPLES = {
    "arabic_moroccan_style_multi_token": [
        "Hassan El Amrani",
        "Ahmed El Idrissi",
        "Sara El Idrissi",
        "Youssef Ait Ben",
        "Omar Ben Salah",
        "Nora El Yassini",
        "Sami El Amrani",
        "Fatima El Amrani",
    ],
    "dutch_tussenvoegsel_name": ["Mila van Dijk", "Lina de Vries", "Tariq de Jong", "Noor van Dijk"],
    "first_name_plus_surname": ["Ahmed El Idrissi", "Fatima Zahra", "Omar Ben Salah"],
    "single_surname": ["Bakker", "Jansen"],
    "professional_title_context": ["Bakker", "Lina de Vries", "Noor van Dijk", "Jansen"],
    "care_role_context": ["Bakker", "Sara El Idrissi", "Youssef Ait Ben", "Fatima Zahra"],
    "legal_role_context": ["Fatima El Amrani"],
    "name_near_contact_data": ["Hassan El Amrani", "Ahmed El Idrissi", "Omar Ben Salah", "Sami El Amrani"],
    "name_near_care_or_legal_reference": ["Hassan El Amrani", "Nora El Yassini", "Noor van Dijk"],
}

DOCUMENTATION_FILES = [
    REPO_ROOT / "RECALL_PERSON_NAME_COVERAGE_REVIEW.md",
    REPO_ROOT / "RECALL_PRECISION_SCORECARD.md",
    REPO_ROOT / "CHANGELOG.md",
    REPO_ROOT / "RISK_REGISTER.md",
]

DISALLOWED_CLAIMS = [
    "Alle persoonsnamen worden altijd gevonden.",
    "Alle persoonsgegevens worden altijd gevonden.",
    "De app is veilig zonder menselijke review.",
    "De benchmark bewijst production readiness.",
]

NON_CLAIM_CUES = [
    "disallowed",
    "disallowed claims",
    "disallowed wording",
    "product-claim boundary",
    "product-claim policy",
    "verboden",
    "niet gezegd",
]



def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")



def load_json(path: Path) -> dict:
    return json.loads(read_text(path))



def gold_sidecars() -> list[Path]:
    return sorted(CORPUS_ROOT.glob("**/*.gold.json"))



def source_files() -> list[Path]:
    return sorted(CORPUS_ROOT.glob("**/*.txt"))



def collect_person_labels() -> list[tuple[Path, dict, dict]]:
    labels: list[tuple[Path, dict, dict]] = []
    for sidecar_path in gold_sidecars():
        sidecar = load_json(sidecar_path)
        for label in sidecar.get("labels", []):
            if label.get("entity_class") == "PERSON":
                labels.append((sidecar_path, sidecar, label))
    return labels



def test_person_gap_review_inventory_is_documented_and_synthetic():
    review_text = read_text(REPO_ROOT / "RECALL_PERSON_NAME_COVERAGE_REVIEW.md")
    combined_corpus_text = "\n".join(read_text(path) for path in source_files())
    combined_sidecar_text = "\n".join(read_text(path) for path in gold_sidecars())

    for name in PERSON_GAP_REVIEW_INVENTORY:
        assert name in review_text, f"PERSON gap inventory must document {name!r}"
        assert name in combined_corpus_text or name in combined_sidecar_text, f"{name!r} must remain grounded in synthetic corpus fixtures"

    for sidecar_path in gold_sidecars():
        sidecar = load_json(sidecar_path)
        assert sidecar.get("synthetic") is True, f"{sidecar_path} must remain synthetic"



def test_gold_sidecars_contain_required_person_labels_for_review_inventory():
    person_labels_by_text: dict[str, list[tuple[Path, dict, dict]]] = {}
    for sidecar_path, sidecar, label in collect_person_labels():
        person_labels_by_text.setdefault(label["text"], []).append((sidecar_path, sidecar, label))

    for name in PERSON_GAP_REVIEW_INVENTORY:
        assert name in person_labels_by_text, f"Expected PERSON gold label for {name!r}"
        for sidecar_path, _sidecar, label in person_labels_by_text[name]:
            assert label["entity_class"] == "PERSON", f"{sidecar_path}:{label['id']} must remain PERSON"
            assert label["required"] is True, f"{sidecar_path}:{label['id']} must remain required"
            assert label["sensitivity"] == "direct_identifier", f"{sidecar_path}:{label['id']} must remain a direct identifier"
            acceptable = set(label.get("acceptable_entity_types", []))
            assert acceptable & {"PERSON", "NL_LEGAL_PARTY_NAME"}, (
                f"{sidecar_path}:{label['id']} should accept PERSON or NL_LEGAL_PARTY_NAME, got {sorted(acceptable)}"
            )



def test_person_context_categories_have_explicit_examples():
    inventory = set(PERSON_GAP_REVIEW_INVENTORY)

    assert set(CONTEXT_CATEGORY_EXAMPLES) == {
        "arabic_moroccan_style_multi_token",
        "dutch_tussenvoegsel_name",
        "first_name_plus_surname",
        "single_surname",
        "professional_title_context",
        "care_role_context",
        "legal_role_context",
        "name_near_contact_data",
        "name_near_care_or_legal_reference",
    }

    for category, examples in CONTEXT_CATEGORY_EXAMPLES.items():
        assert examples, f"{category} must contain at least one example"
        missing = set(examples) - inventory
        assert not missing, f"{category} examples must be part of the review inventory: {sorted(missing)}"



def test_disallowed_product_claims_only_appear_as_non_claim_boundaries():
    for path in DOCUMENTATION_FILES:
        text = read_text(path)
        lowered = text.lower()
        for claim in DISALLOWED_CLAIMS:
            start = 0
            while True:
                index = text.find(claim, start)
                if index == -1:
                    break
                before = lowered[max(0, index - 350) : index]
                assert any(cue in before for cue in NON_CLAIM_CUES), (
                    f"{path} contains disallowed product claim {claim!r} outside an explicit non-claim/disallowed section"
                )
                start = index + len(claim)



def test_person_coverage_diagnostics_do_not_introduce_enforcement_or_gate_claims():
    review_text = read_text(REPO_ROOT / "RECALL_PERSON_NAME_COVERAGE_REVIEW.md").lower()
    scorecard_text = read_text(REPO_ROOT / "RECALL_PRECISION_SCORECARD.md").lower()
    workflow_text = "\n".join(read_text(path).lower() for path in sorted((REPO_ROOT / ".github" / "workflows").glob("*.yml")))

    assert "the tests do not require current recognizers to pass all person examples" in review_text
    assert "no recognizer changes" in scorecard_text
    assert "no threshold enforcement" in scorecard_text or "no thresholds enforced" in scorecard_text
    assert "no production gate" in scorecard_text
    assert "test_recall_person_name_coverage_diagnostics" not in workflow_text
    assert "wp_recall_person_name_coverage_tests" not in workflow_text
