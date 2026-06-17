from __future__ import annotations

import json

from recall_benchmark_runner import (
    GoldDocument,
    GoldLabel,
    KnownTrap,
    Prediction,
    PreserveTerm,
    compare_document,
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


def test_corpus_smoke_report_is_json_serializable():
    report = run_benchmark("corpus", prediction_provider=lambda _source_text: [])

    assert report["summary"]["document_count"] >= 7
    assert report["summary"]["gold_label_count"] > 0
    assert SUMMARY_FIELDS <= set(report["summary"])
    json.dumps(report)
