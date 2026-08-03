import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "output" / "validation" / "care_profile_hf_sync_verification.json"


def _report():
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_hugging_face_sync_evidence_is_complete_and_green():
    report = _report()

    assert report["schema_version"] == "1.2"
    assert report["github_ref"] == "main"
    assert report["github_commit"] == "cca4a25aaff28a7ba647c961d8e50f0e076921e2"
    assert report["hugging_face_space"] == "solidprivacy/scrub"
    assert report["checked_file_count"] == 12
    assert report["exact_matching_file_count"] == 12
    assert report["verified_file_count"] == 12
    assert report["all_files_exact_match"] is True
    assert report["all_markers_match"] is True
    assert report["space_health"]["healthy"] is True
    assert report["space_health"]["attempts"][0]["http_status"] == 200
    assert report["space_health"]["attempts"][0]["body"] == "ok"
    assert report["space_health"]["root_http_status"] == 200
    assert report["sync_verified"] is True
    assert report["technical_deployment_verified"] is True


def test_app_verification_is_confirmed_by_user():
    report = _report()

    assert report["functional_app_verification"] is True
    assert report["functional_app_verification_status"] == "confirmed_all_green"
    assert report["app_verified_at"] == "2026-08-03T20:35:00+02:00"
    assert report["app_verification_source"] == "coordinator_user_confirmation"
    assert report["app_verification_confirmation"] == "alles groen"
    assert all(report["app_verification_checks"].values())
    assert report["human_review_required"] is True
    assert report["production_ready"] is False


def test_sync_report_contains_no_embedded_credentials_or_private_data():
    report_text = REPORT_PATH.read_text(encoding="utf-8")
    lowered = report_text.lower()

    forbidden = (
        "authorization:",
        "bearer ",
        "hf_token",
        "github_token",
        "access_token",
        "patient name",
        "real personal data",
    )
    assert not any(value in lowered for value in forbidden)

    report = json.loads(report_text)
    for item in report["files"]:
        assert item["http_status"] == 200
        assert item["exact_match"] is True
        assert item["markers_match"] is True
        assert item["verified"] is True
        assert item["local_sha256"] == item["remote_sha256"]
