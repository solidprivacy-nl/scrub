from __future__ import annotations

import ast
from pathlib import Path

from recall_benchmark_report import DIAGNOSTIC_METADATA


ROOT = Path(__file__).resolve().parents[1]


def _module_docstring(path: Path) -> str:
    return ast.get_docstring(ast.parse(path.read_text(encoding="utf-8"))) or ""


def test_full_tests_workflow_is_the_exact_sha_release_regression_gate() -> None:
    workflow = (ROOT / ".github" / "workflows" / "tests.yml").read_text(encoding="utf-8")
    decision_log = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")

    assert "python -m pytest -q tests" in workflow
    assert "## D045" in decision_log
    assert "RELEASE REGRESSION GATE" in decision_log
    assert "`.github/workflows/tests.yml`" in decision_log


def test_recall_report_self_identifies_as_supplemental_diagnostic() -> None:
    assert DIAGNOSTIC_METADATA == {
        "status": "diagnostic_only",
        "synthetic_corpus": True,
        "production_gate": False,
        "thresholds_enforced": False,
    }

    decision_log = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")
    assert "SUPPLEMENTAL DIAGNOSTIC" in decision_log
    assert "`recall_benchmark_report.py`" in decision_log


def test_legacy_wp22_wp23_wp24_chain_is_not_promoted_to_release_authority() -> None:
    runner_doc = _module_docstring(ROOT / "benchmark" / "run_recall_precision.py")
    scorecard_doc = _module_docstring(ROOT / "benchmark" / "build_entity_scorecard.py")
    residual_doc = _module_docstring(ROOT / "benchmark" / "build_residual_risk_report.py")

    assert "does not call recognizers" in runner_doc.lower()
    assert "report-only" in scorecard_doc.lower()
    assert "report-only" in residual_doc.lower()

    decision_log = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")
    assert "WP22/WP23/WP24" in decision_log
    assert "not release authority" in decision_log.lower()


def test_capability_regressions_remain_evidence_without_competing_release_authority() -> None:
    decision_log = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")
    roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")

    assert "CAPABILITY REGRESSION EVIDENCE" in decision_log
    for required in [
        "Phase-6 synthetic E2E",
        "Scrub Key",
        "document hygiene/fidelity",
        "Zorg",
        "Premium Streamlit/AppTest",
    ]:
        assert required in decision_log

    assert "No diagnostic score is a merge gate" in roadmap
    assert "No new production recall/precision threshold" in roadmap
