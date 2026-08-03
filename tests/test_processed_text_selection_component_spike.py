from __future__ import annotations

import ast
import importlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

import pytest

from processed_text_selection_component import (
    COMPONENT_NAME,
    FRONTEND_DIR,
    build_component_args,
    component_spike_contract,
    highlight_spans_to_utf16,
    normalize_highlight_spans,
    python_index_to_utf16_offset,
)


ROOT = Path(__file__).resolve().parents[1]
DEMO_PATH = ROOT / "processed_text_selection_component_spike_demo.py"
NODE_TEST_PATH = ROOT / "tests" / "frontend" / "processed_text_selection_component_core.test.js"
FRONTEND_FILES = (
    "index.html",
    "styles.css",
    "streamlit_bridge.js",
    "component_core.js",
    "component.js",
    "NOTICE.md",
)


def _frontend_text(name: str) -> str:
    return (FRONTEND_DIR / name).read_text(encoding="utf-8")


def test_frontend_is_complete_and_local():
    assert COMPONENT_NAME == "solidprivacy_processed_text_selection_spike"
    assert FRONTEND_DIR.is_dir()
    for name in FRONTEND_FILES:
        assert (FRONTEND_DIR / name).is_file(), name

    html = _frontend_text("index.html")
    assert '<link rel="stylesheet" href="styles.css">' in html
    assert '<script src="streamlit_bridge.js"></script>' in html
    assert '<script src="component_core.js"></script>' in html
    assert '<script src="component.js"></script>' in html
    assert "http://" not in html
    assert "https://" not in html


def test_wrapper_import_is_lazy_and_does_not_require_streamlit():
    source = (ROOT / "processed_text_selection_component.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    top_level_imports = [
        node
        for node in tree.body
        if isinstance(node, (ast.Import, ast.ImportFrom))
    ]
    assert not any(
        (
            isinstance(node, ast.Import)
            and any(alias.name.startswith("streamlit") for alias in node.names)
        )
        or (
            isinstance(node, ast.ImportFrom)
            and (node.module or "").startswith("streamlit")
        )
        for node in top_level_imports
    )

    sys.modules.pop("processed_text_selection_component", None)
    before = "streamlit" in sys.modules
    module = importlib.import_module("processed_text_selection_component")
    assert module.COMPONENT_NAME == COMPONENT_NAME
    if not before:
        assert "streamlit" not in sys.modules


def test_python_indices_are_converted_to_utf16_before_frontend_transport():
    text = "A😀BCDEF"
    assert len(text) == 7
    assert python_index_to_utf16_offset(text, 0) == 0
    assert python_index_to_utf16_offset(text, 1) == 1
    assert python_index_to_utf16_offset(text, 2) == 3
    assert python_index_to_utf16_offset(text, 4) == 5
    assert highlight_spans_to_utf16(text, [(2, 4)]) == ((3, 5),)

    args = build_component_args(
        source_text=text,
        processed_text=text,
        highlight_spans=[(2, 4)],
        document_scope_key="0123456789abcdef",
        processed_text_hash="a" * 64,
    )
    assert args["highlight_spans"] == [[3, 5]]
    assert args["component_contract"]["highlight_offset_unit"] == "utf16_code_units"


@pytest.mark.parametrize(
    "spans",
    [
        [(0, 0)],
        [(-1, 1)],
        [(0, 99)],
        [(2, 1)],
        [(0, 2), (1, 3)],
        [(True, 2)],
        [(0.0, 2)],
        ["bad"],
    ],
)
def test_highlight_span_validation_fails_closed(spans):
    with pytest.raises(ValueError):
        normalize_highlight_spans("abcdef", spans)


def test_component_args_are_json_serializable_and_non_mutating():
    args = build_component_args(
        source_text="SYNTHETIC source",
        processed_text="SYNTHETIC [WAARDE_01]",
        highlight_spans=[(10, 21)],
        document_scope_key="0123456789abcdef",
        processed_text_hash="b" * 64,
        inspection_result={
            "status": "ready",
            "inspection_id": "inspection_synthetic_0001",
            "selection_text": "SYNTHETIC",
            "occurrence_count": 1,
            "allowed_types": ["person"],
        },
        restore_source_scroll_ratio=0.25,
        restore_processed_scroll_ratio=0.5,
    )
    assert json.loads(json.dumps(args, ensure_ascii=False)) == args
    assert args["component_contract"] == {
        "schema_version": 1,
        "inspect_action": "inspect_selection",
        "commit_action": "commit_manual_mask",
        "requested_scope": "all_exact",
        "highlight_offset_unit": "utf16_code_units",
        "non_mutating_spike": True,
    }


def test_component_contract_keeps_spike_mutation_disabled():
    contract = component_spike_contract()
    assert contract["api"] == "streamlit_components_v1"
    assert contract["local_assets_only"] is True
    assert contract["runtime_build_step"] is False
    assert contract["bidirectional"] is True
    assert contract["selection_offset_unit"] == "utf16_code_units"
    assert contract["highlight_offset_conversion"] == "python_codepoints_to_utf16"
    assert contract["calls_commit_action_model"] is False
    assert contract["replacement_table_mutation"] is False
    assert contract["session_state_mutation"] is False
    assert contract["production_renderer_integration"] is False
    assert contract["export_change"] is False
    assert contract["scrub_key_change"] is False
    assert contract["reinsert_change"] is False


def test_production_ui_uses_production_entry_point_and_not_spike_alias():
    side_source = (ROOT / "side_by_side_review_panel_ui.py").read_text(encoding="utf-8")
    app_source = (ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")
    assert "render_processed_text_selection_component" in side_source
    assert "render_processed_text_selection_component_spike" not in side_source
    assert "render_processed_text_selection_component_spike" not in app_source
    assert "handle_selection_component_event" in app_source


def test_demo_calls_inspection_only_and_never_calls_commit_model():
    source = DEMO_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported_names = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
        for alias in node.names
    }
    called_names = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    assert "inspect_selection" in imported_names
    assert "parse_commit_event" in imported_names
    assert "commit_manual_mask" not in imported_names
    assert "commit_manual_mask" not in called_names
    assert "replacement_rows_added\": 0" in source
    assert "production_ui_integrated\": False" in source


def test_frontend_has_no_external_network_storage_or_code_execution_paths():
    combined = "\n".join(
        _frontend_text(name)
        for name in ("index.html", "styles.css", "streamlit_bridge.js", "component_core.js", "component.js")
    )
    lowered = combined.lower()
    for forbidden in (
        "http://",
        "https://",
        "fetch(",
        "xmlhttprequest",
        "websocket",
        "eventsource",
        "localstorage",
        "sessionstorage",
        "indexeddb",
        "document.cookie",
        "navigator.sendbeacon",
        "eval(",
        "new function",
        ".innerhtml",
        "document.write",
    ):
        assert forbidden not in lowered

    component = _frontend_text("component.js")
    assert "document.createTextNode" in component
    assert ".textContent" in component
    assert "replaceChildren" in component


def test_bridge_uses_only_the_minimal_v1_message_protocol():
    bridge = _frontend_text("streamlit_bridge.js")
    for message_type in (
        "streamlit:render",
        "streamlit:componentReady",
        "streamlit:setFrameHeight",
        "streamlit:setComponentValue",
    ):
        assert message_type in bridge
    assert 'dataType: "json"' in bridge
    assert "postMessage" in bridge


def test_accessible_context_menu_and_fallbacks_are_present():
    html = _frontend_text("index.html")
    script = _frontend_text("component.js")
    assert 'role="menu"' in html
    assert 'role="status"' in html
    assert 'aria-live="polite"' in html
    assert "Masker selectie" in html
    assert 'setAttribute("role", "menuitem")' in script
    for keyboard_token in (
        'event.key === "F10"',
        'event.key === "ContextMenu"',
        'event.key === "ArrowDown"',
        'event.key === "ArrowUp"',
        'event.key === "Home"',
        'event.key === "End"',
        'event.key === "Escape"',
    ):
        assert keyboard_token in script
    assert "event.preventDefault()" in script


def test_component_reuses_server_result_only_for_matching_selection():
    script = _frontend_text("component.js")
    assert "inspectionMatchesSelection" in script
    assert "resultText === currentSelection.text" in script
    assert "lastRenderedInspectionToken" in script
    assert "renderInspectionResultMenu" in script


@pytest.mark.skipif(shutil.which("node") is None, reason="Node.js is not installed")
def test_dependency_free_node_component_core_suite():
    completed = subprocess.run(
        ["node", str(NODE_TEST_PATH)],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
        timeout=30,
    )
    assert completed.returncode == 0, completed.stdout + "\n" + completed.stderr
    assert "component core tests passed" in completed.stdout
