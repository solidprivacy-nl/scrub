from __future__ import annotations

import ast
from pathlib import Path

from scrub_key_binding_reinsert_status import binding_status_notice


ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "scrub_key_binding_reinsert_status.py"


def test_bound_match_is_verified_success() -> None:
    notice = binding_status_notice(
        {
            "binding_status": "bound_match",
            "replacement_allowed": True,
            "verified_document_match": True,
            "legacy_unbound": False,
        }
    )

    assert notice["level"] == "success"
    assert notice["fail_closed"] is False
    assert "aantoonbaar" in notice["message"]
    assert notice["status_label"] == "Documentgebonden match bevestigd"


def test_legacy_compatibility_is_visible_warning_not_verified() -> None:
    notice = binding_status_notice(
        {
            "binding_status": "legacy_unbound",
            "replacement_allowed": True,
            "verified_document_match": False,
            "legacy_unbound": True,
        }
    )

    assert notice["level"] == "warning"
    assert notice["fail_closed"] is False
    assert "niet documentgebonden" in notice["message"]
    assert "niet bewijzen" in notice["message"]


def test_every_frozen_failure_status_is_fail_closed() -> None:
    for status in [
        "binding_mismatch",
        "mixed_document_bindings",
        "missing_document_binding",
        "invalid_mapping_digest",
        "invalid_bound_key",
        "legacy_key_for_bound_document",
    ]:
        notice = binding_status_notice(
            {
                "binding_status": status,
                "replacement_allowed": False,
                "verified_document_match": False,
                "legacy_unbound": status == "legacy_key_for_bound_document",
            }
        )
        assert notice["level"] == "error"
        assert notice["fail_closed"] is True
        assert "geblokkeerd" in notice["message"]
        assert notice["status_label"]


def test_helper_is_streamlit_network_and_file_write_free() -> None:
    tree = ast.parse(HELPER.read_text(encoding="utf-8"))
    imports = set()
    calls = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.add(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.add(node.func.attr)

    assert "streamlit" not in imports
    assert "requests" not in imports
    assert "urllib" not in imports
    assert "open" not in calls
    assert "write_text" not in calls
    assert "write_bytes" not in calls
