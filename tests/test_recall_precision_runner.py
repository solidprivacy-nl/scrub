import importlib.util
import json
import sys
from pathlib import Path


def load_runner():
    module_path = Path(__file__).resolve().parents[1] / "benchmark" / "run_recall_precision.py"
    spec = importlib.util.spec_from_file_location("run_recall_precision", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def test_runner_scores_exact_normalized_preserve_and_trap(tmp_path):
    runner = load_runner()
    source = "Naam: Jan Jansen\nTel: 06 1234 5678\nContext: cliënt\nTrap: 13-03-2026\n"
    source_path = tmp_path / "benchmark" / "corpus" / "legal" / "mini.txt"
    source_path.parent.mkdir(parents=True)
    source_path.write_text(source, encoding="utf-8")

    person_start = source.index("Jan Jansen")
    phone_start = source.index("06 1234 5678")
    preserve_start = source.index("cliënt")
    trap_start = source.index("13-03-2026")

    gold_path = tmp_path / "benchmark" / "gold" / "examples" / "mini.gold.example.json"
    write_json(
        gold_path,
        {
            "schema_version": "1.0.0",
            "document_id": "mini_001",
            "domain": "legal",
            "document_type": "unit test fixture",
            "language": "nl",
            "source_file": "benchmark/corpus/legal/mini.txt",
            "source_text_encoding": "utf-8",
            "synthetic": True,
            "completeness": "schema_example_only",
            "labels": [
                {
                    "label_id": "L001",
                    "entity_id": "person_jan_jansen",
                    "entity_class": "PERSON",
                    "text": "Jan Jansen",
                    "start": person_start,
                    "end": person_start + len("Jan Jansen"),
                    "sensitivity": "direct_identifier",
                    "required": True,
                    "normalization_profile": "casefold",
                },
                {
                    "label_id": "L002",
                    "entity_id": "phone_jan",
                    "entity_class": "PHONE",
                    "text": "06 1234 5678",
                    "start": phone_start,
                    "end": phone_start + len("06 1234 5678"),
                    "sensitivity": "direct_identifier",
                    "required": True,
                    "normalization_profile": "phone_digits_normalized",
                },
            ],
            "preserve_terms": [
                {
                    "term_id": "P001",
                    "term": "cliënt",
                    "start": preserve_start,
                    "end": preserve_start + len("cliënt"),
                    "entity_class": "ROLE_OR_CONTEXT_TERM_TO_PRESERVE",
                    "reason": "context term",
                    "expected_behavior": "must_remain_readable",
                }
            ],
            "known_traps": [
                {
                    "trap_id": "T001",
                    "text": "13-03-2026",
                    "start": trap_start,
                    "end": trap_start + len("13-03-2026"),
                    "trap_type": "date_must_not_be_bsn_or_phone",
                    "expected_behavior": "must_not_match_as_this_entity_class",
                    "not_entity_class": ["BSN", "PHONE"],
                }
            ],
        },
    )

    predictions_path = tmp_path / "predictions.json"
    write_json(
        predictions_path,
        {
            "predictions": [
                {
                    "document_id": "mini_001",
                    "entity_class": "PERSON",
                    "text": "Jan Jansen",
                    "start": person_start,
                    "end": person_start + len("Jan Jansen"),
                },
                {
                    "document_id": "mini_001",
                    "entity_class": "PHONE",
                    "text": "0612345678",
                    "start": phone_start,
                    "end": phone_start + len("06 1234 5678") - 1,
                },
                {
                    "document_id": "mini_001",
                    "entity_class": "PERSON",
                    "text": "cliënt",
                    "start": preserve_start,
                    "end": preserve_start + len("cliënt"),
                },
                {
                    "document_id": "mini_001",
                    "entity_class": "BSN",
                    "text": "13-03-2026",
                    "start": trap_start,
                    "end": trap_start + len("13-03-2026"),
                },
            ]
        },
    )

    report = runner.run_benchmark(tmp_path, gold_path, predictions_path)

    assert report["summary"]["gold_count"] == 2
    assert report["summary"]["prediction_count"] == 4
    assert report["summary"]["true_positive_exact"] == 1
    assert report["summary"]["true_positive_normalized"] == 2
    assert report["summary"]["recall_exact"] == 0.5
    assert report["summary"]["recall_normalized"] == 1.0
    assert len(report["preserve_term_failures"]) == 1
    assert len(report["known_trap_failures"]) == 1
    assert report["partial_overlaps"][0]["policy"] == "diagnostic_only"


def test_runner_rejects_gold_offset_text_mismatch(tmp_path):
    runner = load_runner()
    source_path = tmp_path / "benchmark" / "corpus" / "legal" / "mini.txt"
    source_path.parent.mkdir(parents=True)
    source_path.write_text("Naam: Jan Jansen\n", encoding="utf-8")
    gold_path = tmp_path / "benchmark" / "gold" / "examples" / "bad.gold.example.json"
    write_json(
        gold_path,
        {
            "schema_version": "1.0.0",
            "document_id": "bad_001",
            "domain": "legal",
            "language": "nl",
            "source_file": "benchmark/corpus/legal/mini.txt",
            "source_text_encoding": "utf-8",
            "synthetic": True,
            "completeness": "schema_example_only",
            "labels": [
                {
                    "label_id": "L001",
                    "entity_id": "person_wrong",
                    "entity_class": "PERSON",
                    "text": "Wrong Person",
                    "start": 6,
                    "end": 16,
                    "sensitivity": "direct_identifier",
                    "required": True,
                }
            ],
            "preserve_terms": [],
            "known_traps": [],
        },
    )

    try:
        runner.load_gold_sidecars(gold_path, tmp_path)
    except ValueError as exc:
        assert "text/span mismatch" in str(exc)
    else:
        raise AssertionError("Expected ValueError for mismatched gold label offset")


def test_cli_writes_json_report(tmp_path, capsys):
    runner = load_runner()
    source_path = tmp_path / "benchmark" / "corpus" / "legal" / "mini.txt"
    source_path.parent.mkdir(parents=True)
    source_path.write_text("Naam: Jan Jansen\n", encoding="utf-8")
    start = source_path.read_text(encoding="utf-8").index("Jan Jansen")
    gold_path = tmp_path / "benchmark" / "gold" / "examples" / "mini.gold.example.json"
    write_json(
        gold_path,
        {
            "schema_version": "1.0.0",
            "document_id": "mini_001",
            "domain": "legal",
            "language": "nl",
            "source_file": "benchmark/corpus/legal/mini.txt",
            "source_text_encoding": "utf-8",
            "synthetic": True,
            "completeness": "schema_example_only",
            "labels": [
                {
                    "label_id": "L001",
                    "entity_id": "person_jan_jansen",
                    "entity_class": "PERSON",
                    "text": "Jan Jansen",
                    "start": start,
                    "end": start + len("Jan Jansen"),
                    "sensitivity": "direct_identifier",
                    "required": True,
                }
            ],
            "preserve_terms": [],
            "known_traps": [],
        },
    )
    output_path = tmp_path / "report.json"

    result = runner.main(["--repo-root", str(tmp_path), "--gold", str(gold_path), "--output", str(output_path)])

    assert result == 0
    assert json.loads(output_path.read_text(encoding="utf-8"))["summary"]["gold_count"] == 1
    assert capsys.readouterr().out == ""
