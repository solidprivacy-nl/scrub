from __future__ import annotations

import json

from recall_benchmark_runner import (
    GoldDocument,
    GoldLabel,
    KnownTrap,
    Prediction,
    PreserveTerm,
    collect_benchmark_builtin_predictions,
    compare_document,
    dedupe_predictions,
    load_gold_documents,
    normalize_value,
    run_benchmark,
)


SUMMARY_FIELDS = {
    "document_count",
    "gold_label_count",
    "prediction_count",
    "required_label_count",
    "matched_required_exact_count",
    "matched_required_text_normalized_count",
    "matched_required_overlap_count",
    "missed_required_count",
    "wrong_type_count",
    "false_positive_candidate_count",
    "preserve_term_hit_count",
    "known_trap_hit_count",
}


def test_load_gold_sidecars_and_sources():
    documents = load_gold_documents("corpus")

    assert len(documents) >= 7
    assert all(document.source_text for document in documents)
    assert all(document.labels for document in documents)
    assert all(document.language == "nl" for document in documents)


def test_normalize_value_examples():
    assert normalize_value("CLM-2026-112233") == "clm2026112233"
    assert normalize_value("06-99887766") == "0699887766"
    assert normalize_value("NL91 ABNA 0417 1643 00") == "nl91abna0417164300"


def _single_label_document(entity_class: str, text: str, acceptable_entity_types: tuple[str, ...] = ()) -> GoldDocument:
    return GoldDocument(
        document_id="unit_doc",
        domain="legal",
        document_type="unit",
        language="nl",
        source_file="unit.txt",
        source_text=text,
        labels=(
            GoldLabel(
                id="L001",
                entity_class=entity_class,
                text=text,
                start=0,
                end=len(text),
                sensitivity="direct_identifier",
                required=True,
                acceptable_entity_types=acceptable_entity_types,
            ),
        ),
        preserve_terms=(),
        known_traps=(),
    )


def test_compare_document_matches_and_diagnostics():
    source = "CLM-2026-112233 arts 06-99887766 artikel 7:669 BW EXTRA"
    claim_start = source.index("CLM-2026-112233")
    phone_start = source.index("06-99887766")
    ecli_missing_start = len(source) + 10
    article_start = source.index("artikel 7:669 BW")
    arts_start = source.index("arts")
    extra_start = source.index("EXTRA")

    document = GoldDocument(
        document_id="unit_doc",
        domain="legal",
        document_type="unit",
        language="nl",
        source_file="unit.txt",
        source_text=source,
        labels=(
            GoldLabel(
                id="L001",
                entity_class="CLAIM_NUMBER",
                text="CLM-2026-112233",
                start=claim_start,
                end=claim_start + len("CLM-2026-112233"),
                sensitivity="claim_reference",
                required=True,
                acceptable_entity_types=("NL_CLAIM_NUMBER",),
            ),
            GoldLabel(
                id="L002",
                entity_class="PHONE",
                text="06-99887766",
                start=phone_start,
                end=phone_start + len("06-99887766"),
                sensitivity="direct_identifier",
                required=True,
                acceptable_entity_types=("PHONE_NUMBER",),
            ),
            GoldLabel(
                id="L003",
                entity_class="ECLI",
                text="ECLI:NL:UNIT:2026:1",
                start=ecli_missing_start,
                end=ecli_missing_start + len("ECLI:NL:UNIT:2026:1"),
                sensitivity="matter_reference",
                required=True,
                acceptable_entity_types=("NL_ECLI",),
            ),
        ),
        preserve_terms=(PreserveTerm(term="arts", start=arts_start, end=arts_start + len("arts"), reason="role"),),
        known_traps=(KnownTrap(text="artikel 7:669 BW", trap_type="legal_article_must_not_be_case_number"),),
    )

    predictions = [
        Prediction(
            text="CLM-2026-112233",
            entity_type="NL_CLAIM_NUMBER",
            start=claim_start,
            end=claim_start + len("CLM-2026-112233"),
            source="recognizer",
            benchmark_class="CLAIM_NUMBER",
        ),
        Prediction(
            text="06 99887766",
            entity_type="PHONE_NUMBER",
            start=phone_start + 1,
            end=phone_start + len("06-99887766"),
            source="recognizer",
            benchmark_class="PHONE",
        ),
        Prediction(
            text="arts",
            entity_type="PERSON",
            start=arts_start,
            end=arts_start + len("arts"),
            source="recognizer",
            benchmark_class="PERSON",
        ),
        Prediction(
            text="artikel 7:669 BW",
            entity_type="NL_LEGAL_CASE_NUMBER",
            start=article_start,
            end=article_start + len("artikel 7:669 BW"),
            source="candidate_scanner",
            benchmark_class="CASE_NUMBER",
        ),
        Prediction(
            text="EXTRA",
            entity_type="PERSON",
            start=extra_start,
            end=extra_start + len("EXTRA"),
            source="recognizer",
            benchmark_class="PERSON",
        ),
    ]

    report = compare_document(document, predictions)

    assert report["matched_exact"]
    assert report["matched_text_normalized"]
    assert report["matched_overlap"]
    assert report["missed_required"]
    assert report["false_positive_candidates"]
    assert report["preserve_term_hits"]
    assert report["known_trap_hits"]


def test_benchmark_entity_mapping_accepts_known_implementation_types():
    cases = [
        ("ADDRESS", "Parklaan 188, 3512 ZX Utrecht", "NL_ADDRESS"),
        ("IBAN", "NL91 ABNA 0417 1643 00", "NL_IBAN"),
        ("CASE_NUMBER", "ZK-WOON-55091", "NL_CASE_REFERENCE"),
        ("PERSON", "Sami El Amrani", "NL_LEGAL_PARTY_NAME"),
        ("EMAIL", "sami.elamrani@example.test", "EMAIL_ADDRESS"),
    ]

    for entity_class, text, prediction_type in cases:
        document = _single_label_document(entity_class, text)
        report = compare_document(
            document,
            [Prediction(text=text, entity_type=prediction_type, start=0, end=len(text), source="recognizer")],
        )

        assert report["matched_exact"], prediction_type
        assert not report["wrong_type"], prediction_type
        assert not report["missed_required"], prediction_type
        assert not report["false_positive_candidates"], prediction_type


def test_acceptable_entity_type_can_accept_care_reference_taxonomy():
    text = "ZORG-CL-2026-00441"
    document = _single_label_document("MEDICAL_OR_CARE_REFERENCE", text, acceptable_entity_types=("NL_CLIENT_REFERENCE",))
    report = compare_document(
        document,
        [Prediction(text=text, entity_type="NL_CLIENT_REFERENCE", start=0, end=len(text), source="recognizer")],
    )

    assert report["matched_exact"]
    assert not report["wrong_type"]
    assert not report["missed_required"]


def test_wrong_type_is_reported_for_overlapping_wrong_entity():
    source = "ECLI:NL:UNIT:2026:1"
    document = GoldDocument(
        document_id="wrong_type_doc",
        domain="legal",
        document_type="unit",
        language="nl",
        source_file="unit.txt",
        source_text=source,
        labels=(
            GoldLabel(
                id="L001",
                entity_class="ECLI",
                text=source,
                start=0,
                end=len(source),
                sensitivity="matter_reference",
                required=True,
                acceptable_entity_types=("NL_ECLI",),
            ),
        ),
        preserve_terms=(),
        known_traps=(),
    )
    predictions = [Prediction(text=source, entity_type="PHONE_NUMBER", start=0, end=len(source), source="recognizer", benchmark_class="PHONE")]

    report = compare_document(document, predictions)

    assert report["wrong_type"]
    assert report["missed_required"]


def test_duplicate_predictions_are_counted_once_in_report_accounting():
    source = "arts artikel 7:669 BW EXTRA"
    arts_start = source.index("arts")
    trap_start = source.index("artikel 7:669 BW")
    extra_start = source.index("EXTRA")
    duplicate_wrong = Prediction(text="arts", entity_type="PERSON", start=arts_start, end=arts_start + 4, source="recognizer", benchmark_class="PERSON")
    duplicate_trap = Prediction(
        text="artikel 7:669 BW",
        entity_type="NL_LEGAL_CASE_NUMBER",
        start=trap_start,
        end=trap_start + len("artikel 7:669 BW"),
        source="candidate_scanner",
        benchmark_class="CASE_NUMBER",
    )
    duplicate_false_positive = Prediction(text="EXTRA", entity_type="PERSON", start=extra_start, end=extra_start + 5, source="recognizer", benchmark_class="PERSON")
    document = GoldDocument(
        document_id="dedupe_doc",
        domain="legal",
        document_type="unit",
        language="nl",
        source_file="unit.txt",
        source_text=source,
        labels=(
            GoldLabel(
                id="L001",
                entity_class="ROLE_OR_CONTEXT_TERM_TO_PRESERVE",
                text="arts",
                start=arts_start,
                end=arts_start + 4,
                sensitivity="context",
                required=True,
                acceptable_entity_types=(),
            ),
        ),
        preserve_terms=(PreserveTerm(term="arts", start=arts_start, end=arts_start + 4, reason="role"),),
        known_traps=(KnownTrap(text="artikel 7:669 BW", trap_type="legal_article_must_not_be_case_number"),),
    )

    report = compare_document(
        document,
        [duplicate_wrong, duplicate_wrong, duplicate_wrong, duplicate_trap, duplicate_trap, duplicate_false_positive, duplicate_false_positive],
    )

    assert len(report["wrong_type"]) == 1
    assert len(report["wrong_type"][0]["predictions"]) == 1
    assert len(report["false_positive_candidates"]) == 2
    assert len(report["preserve_term_hits"]) == 1
    assert len(report["known_trap_hits"]) == 1


def test_matched_prediction_is_not_reported_as_false_positive():
    text = "NL91 ABNA 0417 1643 00"
    prediction = Prediction(text=text, entity_type="NL_IBAN", start=0, end=len(text), source="recognizer")
    report = compare_document(_single_label_document("IBAN", text), [prediction, prediction, prediction])

    assert len(report["matched_exact"]) == 1
    assert report["prediction_count"] == 1
    assert not report["false_positive_candidates"]


def test_benchmark_builtin_email_predictions_are_available():
    source = "Mail naar sami.elamrani@example.test."
    predictions = collect_benchmark_builtin_predictions(source)

    assert len(predictions) == 1
    assert predictions[0].text == "sami.elamrani@example.test"
    assert predictions[0].entity_type == "EMAIL_ADDRESS"
    assert predictions[0].benchmark_class == "EMAIL"


def test_dedupe_predictions_uses_report_accounting_key():
    prediction = Prediction(text="EXTRA", entity_type="PERSON", start=0, end=5, source="recognizer")

    assert dedupe_predictions([prediction, prediction, prediction]) == [prediction]


def test_corpus_smoke_report_is_json_serializable():
    report = run_benchmark("corpus", prediction_provider=lambda _source_text: [])

    assert report["summary"]["document_count"] >= 7
    assert report["summary"]["gold_label_count"] > 0
    assert SUMMARY_FIELDS <= set(report["summary"])
    json.dumps(report)
