from __future__ import annotations

import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_ROOT = REPO_ROOT / "corpus"

REQUIRED_LABEL_FIELDS = {
    "id",
    "entity_class",
    "text",
    "start",
    "end",
    "sensitivity",
    "required",
}

ALLOWED_ENTITY_CLASSES = {
    "PERSON",
    "ADDRESS",
    "EMAIL",
    "PHONE",
    "BSN",
    "IBAN",
    "DATE",
    "NL_POSTCODE",
    "CASE_NUMBER",
    "DOSSIER_NUMBER",
    "CLIENT_NUMBER",
    "CLAIM_NUMBER",
    "INCIDENT_NUMBER",
    "ECLI",
    "ORGANIZATION",
    "MEDICAL_OR_CARE_REFERENCE",
    "ROLE_OR_CONTEXT_TERM_TO_PRESERVE",
}

ROLE_WORDS = {
    "slachtoffer",
    "arts",
    "getuige",
    "eiser",
    "verweerder",
    "minderjarige",
    "cliënt",
    "zorgmedewerker",
    "verpleegkundige",
    "behandelaar",
    "mantelzorger",
}

ALLOWED_PRESERVE_CONTEXT_TERMS = ROLE_WORDS | {
    "zaaknummer",
    "rolnummer",
    "dossier",
    "dossiernummer",
    "artikel",
    "lid",
    "pagina",
    "bijlage",
    "productie",
    "kamer",
    "afdeling",
}

EXPECTED_GOLD_SIDECARS = {
    "legal/legal_reference_seed_001.gold.json",
    "legal/legal_role_preservation_seed_001.gold.json",
    "legal/legal_false_positive_traps_seed_001.gold.json",
    "legal/legal_mixed_identifiers_seed_001.gold.json",
    "care/care_reference_seed_001.gold.json",
    "care/care_role_preservation_seed_001.gold.json",
    "care/care_mixed_identifiers_seed_001.gold.json",
}


def _gold_files() -> list[Path]:
    return sorted(CORPUS_ROOT.glob("**/*.gold.json"))


def test_gold_label_seed_files_exist():
    gold_files = _gold_files()
    relative_gold_files = {gold_file.relative_to(CORPUS_ROOT).as_posix() for gold_file in gold_files}

    assert gold_files, "Expected at least one .gold.json sidecar in corpus/"
    assert EXPECTED_GOLD_SIDECARS <= relative_gold_files


def test_gold_label_sidecars_are_valid_and_synthetic():
    for gold_file in _gold_files():
        sidecar = json.loads(gold_file.read_text(encoding="utf-8"))

        assert sidecar["synthetic"] is True
        assert sidecar["language"] == "nl"
        assert sidecar["labels"], f"{gold_file} must contain at least one label"
        assert isinstance(sidecar.get("preserve_terms", []), list)
        assert isinstance(sidecar.get("known_traps", []), list)


def test_gold_label_source_files_exist_and_offsets_match():
    for gold_file in _gold_files():
        sidecar = json.loads(gold_file.read_text(encoding="utf-8"))
        source_file = REPO_ROOT / sidecar["source_file"]

        assert source_file.exists(), f"source_file missing for {gold_file}"
        source_text = source_file.read_text(encoding="utf-8")
        for label in sidecar["labels"]:
            missing = REQUIRED_LABEL_FIELDS - set(label)
            assert not missing, f"{gold_file} label {label.get('id')} missing fields: {sorted(missing)}"
            assert label["entity_class"] in ALLOWED_ENTITY_CLASSES
            assert label["text"].strip(), f"{gold_file} label {label['id']} has empty text"
            assert isinstance(label["required"], bool)
            assert source_text[label["start"] : label["end"]] == label["text"]

        for preserve_term in sidecar.get("preserve_terms", []):
            assert preserve_term["term"].strip()
            assert source_text[preserve_term["start"] : preserve_term["end"]] == preserve_term["term"]


def test_seed_corpus_uses_reserved_example_email_domain_only():
    found_emails = []
    for source_file in CORPUS_ROOT.glob("**/*.txt"):
        source_text = source_file.read_text(encoding="utf-8")
        found_emails.extend(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+", source_text))

    assert found_emails, "Expected at least one synthetic email fixture in corpus/"
    for email in found_emails:
        assert email.endswith(".example.test"), f"Use .example.test only, got {email}"


def test_role_and_context_terms_are_preserved_not_sensitive_labels():
    for gold_file in _gold_files():
        sidecar = json.loads(gold_file.read_text(encoding="utf-8"))
        sensitive_label_texts = {label["text"].lower() for label in sidecar["labels"]}
        preserved_terms = {term["term"].lower() for term in sidecar.get("preserve_terms", [])}

        assert sensitive_label_texts.isdisjoint(ROLE_WORDS)
        assert preserved_terms <= ALLOWED_PRESERVE_CONTEXT_TERMS
