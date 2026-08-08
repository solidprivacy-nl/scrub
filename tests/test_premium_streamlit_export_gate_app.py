from __future__ import annotations

from pathlib import Path

from streamlit.testing.v1 import AppTest


REPO_ROOT = Path(__file__).resolve().parents[1]
APP_PATH = REPO_ROOT / "tests" / "streamlit_apps" / "premium_export_gate_flow_app.py"
PRODUCTION_APP_PATH = REPO_ROOT / "presidio_streamlit.py"


def _assert_no_exception(at: AppTest) -> None:
    assert len(at.exception) == 0, [item.value for item in at.exception]


def _values(elements) -> list[str]:
    return [str(getattr(element, "value", "")) for element in elements]


def _markdown(at: AppTest, prefix: str) -> str:
    for value in _values(at.markdown):
        if value.startswith(prefix):
            return value
    raise AssertionError(f"Missing markdown prefix {prefix!r}: {_values(at.markdown)!r}")


def _radio(at: AppTest, label: str):
    for widget in at.radio:
        if widget.label == label:
            return widget
    raise AssertionError(f"Missing radio {label!r}")


def _selectbox(at: AppTest, label: str):
    for widget in at.selectbox:
        if widget.label == label:
            return widget
    raise AssertionError(f"Missing selectbox {label!r}")


def _button(at: AppTest, label: str):
    for widget in at.button:
        if widget.label == label:
            return widget
    raise AssertionError(f"Missing button {label!r}; found {[widget.label for widget in at.button]!r}")


def _has_button(at: AppTest, label: str) -> bool:
    return any(widget.label == label for widget in at.button)


def _has_message(elements, text: str) -> bool:
    return any(text in value for value in _values(elements))


def test_completed_standard_to_expert_edit_blocks_export_until_explicit_recompletion() -> None:
    at = AppTest.from_file(str(APP_PATH)).run(timeout=30)
    _assert_no_exception(at)
    initial_source = _markdown(at, "STATE_SOURCE:")
    initial_generation = _markdown(at, "STATE_GENERATION:")
    assert _has_message(at.success, "EXPORT_AVAILABLE")
    assert "processed=current;reviewed=current;export=current" in _markdown(at, "STATE_LINEAGE:")

    _radio(at, "Weergave").set_value("Expert")
    at.run(timeout=30)
    _assert_no_exception(at)
    assert _markdown(at, "STATE_SOURCE:") == initial_source
    assert _markdown(at, "STATE_GENERATION:") == initial_generation
    assert "STATE_ANALYSIS_CACHE: `current`" == _markdown(at, "STATE_ANALYSIS_CACHE:")
    assert "STATE_REVIEW_CACHE: `current`" == _markdown(at, "STATE_REVIEW_CACHE:")
    assert _has_message(at.success, "EXPORT_AVAILABLE")

    _button(at, "Wijzig reviewbeslissing").click()
    at.run(timeout=30)
    _assert_no_exception(at)
    assert _markdown(at, "STATE_SOURCE:") == initial_source
    assert _markdown(at, "STATE_GENERATION:") == initial_generation
    assert "[PERSOON_TEST_99]" in _markdown(at, "STATE_REVIEW_ROW:")
    assert "processed=current;reviewed=stale;export=stale" in _markdown(at, "STATE_LINEAGE:")
    assert _has_message(at.info, "EXPORT_BLOCKED")
    assert not _has_message(at.success, "EXPORT_AVAILABLE")
    assert _has_button(at, "Controle opnieuw afronden")

    _button(at, "Controle opnieuw afronden").click()
    at.run(timeout=30)
    _assert_no_exception(at)
    assert "[PERSOON_TEST_99]" in _markdown(at, "STATE_REVIEW_ROW:")
    assert "processed=current;reviewed=current;export=current" in _markdown(at, "STATE_LINEAGE:")
    assert _has_message(at.success, "EXPORT_AVAILABLE")

    _radio(at, "Weergave").set_value("Standaard")
    at.run(timeout=30)
    _assert_no_exception(at)
    assert _markdown(at, "STATE_SOURCE:") == initial_source
    assert _markdown(at, "STATE_GENERATION:") == initial_generation
    assert "[PERSOON_TEST_99]" in _markdown(at, "STATE_REVIEW_ROW:")
    assert "STATE_ANALYSIS_CACHE: `current`" == _markdown(at, "STATE_ANALYSIS_CACHE:")
    assert "STATE_REVIEW_CACHE: `current`" == _markdown(at, "STATE_REVIEW_CACHE:")
    assert _has_message(at.success, "EXPORT_AVAILABLE")


def test_real_processing_setting_change_clears_caches_and_blocks_export() -> None:
    at = AppTest.from_file(str(APP_PATH)).run(timeout=30)
    _assert_no_exception(at)
    initial_generation = _markdown(at, "STATE_GENERATION:")

    _radio(at, "Weergave").set_value("Expert")
    at.run(timeout=30)
    _button(at, "Wijzig verwerkingsinstelling").click()
    at.run(timeout=30)
    _assert_no_exception(at)

    assert _markdown(at, "STATE_GENERATION:") != initial_generation
    assert "STATE_ANALYSIS_CACHE: `missing`" == _markdown(at, "STATE_ANALYSIS_CACHE:")
    assert "STATE_REVIEW_CACHE: `missing`" == _markdown(at, "STATE_REVIEW_CACHE:")
    assert "processed=stale;reviewed=stale;export=stale" in _markdown(at, "STATE_LINEAGE:")
    assert _has_message(at.info, "EXPORT_BLOCKED")
    assert not _has_button(at, "Controle opnieuw afronden")


def test_expert_only_operator_is_preserved_when_returning_to_standard() -> None:
    at = AppTest.from_file(str(APP_PATH)).run(timeout=30)
    _assert_no_exception(at)

    _radio(at, "Weergave").set_value("Expert")
    at.run(timeout=30)
    _selectbox(at, "Expert operator").set_value("highlight")
    at.run(timeout=30)
    _assert_no_exception(at)
    assert "STATE_OPERATOR: `highlight`" == _markdown(at, "STATE_OPERATOR:")

    _radio(at, "Weergave").set_value("Standaard")
    at.run(timeout=30)
    _assert_no_exception(at)
    assert "STATE_OPERATOR: `highlight`" == _markdown(at, "STATE_OPERATOR:")
    assert _has_message(at.warning, "EXPERT_OPERATOR_REQUIRED")
    assert _has_message(at.info, "EXPORT_BLOCKED")


def test_production_export_buttons_are_behind_the_executable_readiness_gate() -> None:
    source = PRODUCTION_APP_PATH.read_text(encoding="utf-8")
    gate_call = source.index("export_surface_ready = render_export_readiness_gate(")
    stop_guard = source.index("if not export_surface_ready:", gate_call)
    first_document_download = source.index('key="download_txt"', stop_guard)
    guarded_section = source[gate_call:first_document_download]

    assert gate_call < stop_guard < first_document_download
    assert "st.stop()" in guarded_section
    assert "reviewed_rows=edited_replacements_df.to_dict(\"records\")" in guarded_section
