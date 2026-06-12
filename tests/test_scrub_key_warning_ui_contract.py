from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = REPO_ROOT / "tests" / "fixtures" / "scrub_key_warning_ui_contract.json"
PLAN_PATH = REPO_ROOT / "SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md"
PATCH_PATH = REPO_ROOT / "fix_streamlit_nested_expanders.py"
WORKPACKAGES_PATH = REPO_ROOT / "WORKPACKAGES.md"
CLAIMS_README_PATH = REPO_ROOT / "workpackage_claims" / "README.md"
WP29C_CLAIM_PATH = REPO_ROOT / "workpackage_claims" / "WP29C_scrub_key_warning_ui_regression_test_scaffolding.md"


def load_contract() -> dict:
    return json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))


def test_warning_ui_contract_fixture_is_scaffolding_only_and_targets_patch_layer():
    contract = load_contract()

    assert contract["schema_version"] == "wp29c_scrub_key_warning_ui_contract_v1"
    assert contract["synthetic_only"] is True
    assert contract["test_scaffolding_only"] is True
    assert contract["implements_ui"] is False
    assert contract["source_plan"] == "SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md"
    assert contract["target_patch_file"] == "fix_streamlit_nested_expanders.py"
    assert "presidio_streamlit.py" in contract["forbidden_files_for_scaffolding"]


def test_warning_ui_contract_covers_blocks_warning_moments_and_state_keys():
    contract = load_contract()

    assert {
        "review_summary_block",
        "scrub_key_import_ui_block",
        "two_mode_selection_block",
        "reinsert_ui_block",
        "txt_reinsert_ui_block",
        "docx_reinsert_ui_block",
    }.issubset(set(contract["required_ui_blocks"]))

    moment_ids = {moment["id"] for moment in contract["required_warning_moments"]}
    assert {
        "scrub_key_creation_preview",
        "scrub_key_export_download",
        "local_storage_downloads_guidance",
        "scrub_key_import_reload",
        "reinsert_mode_entry",
        "pasted_text_reinsert",
        "txt_reinsert",
        "txt_restored_download",
        "docx_reinsert",
        "docx_restored_download",
        "pdf_text_reinsert_if_present",
        "expiry_delete_guidance",
        "shared_computer_warning",
        "email_ai_upload_warning",
        "loss_of_key_warning",
        "tampering_mismatch_audit_warning",
    }.issubset(moment_ids)

    required_keys = set(contract["required_acknowledgement_state_keys"])
    assert {
        "ack_scrub_key_export_risk",
        "ack_scrub_key_import_risk",
        "ack_reinsert_text_confidential",
        "ack_reinsert_txt_confidential",
        "ack_reinsert_docx_confidential",
        "ack_reinsert_pdf_text_confidential",
        "ack_download_restored_txt_confidential",
        "ack_download_restored_docx_confidential",
    } == required_keys

    for moment in contract["required_warning_moments"]:
        if moment["acknowledgement_required"]:
            assert moment.get("state_key") in required_keys


def test_contract_fragments_and_audit_fields_are_grounded_in_warning_plan():
    contract = load_contract()
    plan = PLAN_PATH.read_text(encoding="utf-8")

    assert "## 5. MVP acknowledgement inventory" in plan
    assert "## 9. Later implementation test expectations" in plan

    for moment in contract["required_warning_moments"]:
        for fragment in moment["required_copy_fragments"]:
            assert fragment in plan, f"Missing planned warning fragment for {moment['id']}: {fragment}"

    for state_key in contract["required_acknowledgement_state_keys"]:
        assert state_key in plan

    for audit_field in contract["required_audit_fields_to_preserve"]:
        assert audit_field in plan


def test_contract_boundary_is_documented_and_patch_surface_exists_without_ui_implementation():
    contract = load_contract()
    plan = PLAN_PATH.read_text(encoding="utf-8")
    patch_text = PATCH_PATH.read_text(encoding="utf-8")

    for fragment in [
        "No UI implementation",
        "No Streamlit patch change",
        "No Scrub Key schema migration",
        "No import/export behavior change",
        "No reinsert behavior change",
        "No encryption implementation",
        "No automatic deletion implementation",
        "No expiry blocking",
        "No hidden recovery",
        "No cloud processing",
    ]:
        assert fragment in plan

    for block in contract["required_ui_blocks"]:
        assert block in patch_text


def test_workpackage_claim_protocol_is_present_and_wp29c_is_claimed():
    claims_readme = CLAIMS_README_PATH.read_text(encoding="utf-8")
    claim = WP29C_CLAIM_PATH.read_text(encoding="utf-8")
    workpackages = WORKPACKAGES_PATH.read_text(encoding="utf-8")

    assert "workpackage_claims/" in claims_readme
    assert "in_progress" in claims_readme
    assert "completed" in claims_readme
    assert "create a new claim file" in claims_readme
    assert "WP29C" in claim
    assert "Status: `in_progress`" in claim or "Status: `completed`" in claim
    assert "Required workpackage claim check" in workpackages
