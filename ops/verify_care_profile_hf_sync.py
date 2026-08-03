from __future__ import annotations

# Explicit second push after the verification workflow exists.
import hashlib
import json
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


SPACE_ID = "solidprivacy/scrub"
RAW_BASE = f"https://huggingface.co/spaces/{SPACE_ID}/resolve/main/"
SPACE_BASE = "https://solidprivacy-scrub.hf.space"
FILES = (
    "presidio_streamlit.py",
    "presidio_helpers.py",
    "care_candidate_scanner.py",
    "profile_ui_support.py",
    "dutch_care_recognizers.py",
    "recognition_profiles.py",
    "care_test_examples.py",
    "ui_texts_nl.py",
    "display_labels_nl.py",
    "document_tools.py",
)
EXPECTED_MARKERS = {
    "presidio_streamlit.py": (
        "Zorgcontrole — streng",
        "detected_review_status",
        "care_example_names",
        "resolve_configured_analysis_results",
    ),
    "presidio_helpers.py": (
        "get_dutch_care_recognizers",
        "register_custom_recognizers",
    ),
    "profile_ui_support.py": (
        "Dutch Care Strict",
        "Controle nodig",
    ),
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def request_bytes(url: str, timeout: int = 30) -> tuple[int | None, bytes, str | None]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "SolidPrivacy-Scrub-Verification/1.0",
            "Accept": "*/*",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return int(response.status), response.read(), None
    except urllib.error.HTTPError as exc:
        body = exc.read()[:500] if exc.fp is not None else b""
        return int(exc.code), body, f"HTTP {exc.code}: {exc.reason}"
    except Exception as exc:
        return None, b"", f"{type(exc).__name__}: {exc}"


def verify_files() -> tuple[list[dict], bool]:
    results: list[dict] = []
    all_match = True
    for path in FILES:
        local_bytes = Path(path).read_bytes()
        status, remote_bytes, error = request_bytes(RAW_BASE + path)
        exact_match = status == 200 and remote_bytes == local_bytes
        marker_results = {}
        remote_text = remote_bytes.decode("utf-8", errors="replace") if remote_bytes else ""
        for marker in EXPECTED_MARKERS.get(path, ()):
            marker_results[marker] = marker in remote_text
        markers_match = all(marker_results.values()) if marker_results else True
        file_ok = exact_match and markers_match
        all_match = all_match and file_ok
        results.append(
            {
                "path": path,
                "remote_url": RAW_BASE + path,
                "http_status": status,
                "error": error,
                "local_sha256": sha256(local_bytes),
                "remote_sha256": sha256(remote_bytes) if remote_bytes else None,
                "exact_match": exact_match,
                "expected_markers": marker_results,
                "verified": file_ok,
            }
        )
    return results, all_match


def verify_health() -> dict:
    health_url = SPACE_BASE + "/_stcore/health"
    attempts: list[dict] = []
    healthy = False
    for attempt in range(1, 11):
        status, body, error = request_bytes(health_url, timeout=20)
        text = body.decode("utf-8", errors="replace").strip()[:500]
        attempts.append(
            {
                "attempt": attempt,
                "http_status": status,
                "body": text,
                "error": error,
            }
        )
        if status == 200 and text.lower() in {"ok", "healthy"}:
            healthy = True
            break
        if status == 200 and text:
            healthy = True
            break
        time.sleep(6)

    root_status, root_body, root_error = request_bytes(SPACE_BASE + "/", timeout=30)
    return {
        "health_url": health_url,
        "healthy": healthy,
        "attempts": attempts,
        "root_url": SPACE_BASE + "/",
        "root_http_status": root_status,
        "root_error": root_error,
        "root_body_prefix": root_body.decode("utf-8", errors="replace")[:300],
    }


def main() -> None:
    file_results, files_match = verify_files()
    health = verify_health()
    sync_verified = files_match and health["healthy"]
    report = {
        "schema_version": "1.0",
        "workpackage": "SCRUB-WP_CARE_PROFILE_APP_VERIFY",
        "verified_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "github_ref": "main",
        "github_commit": "cca4a25aaff28a7ba647c961d8e50f0e076921e2",
        "hugging_face_space": SPACE_ID,
        "checked_file_count": len(FILES),
        "matching_file_count": sum(1 for item in file_results if item["verified"]),
        "all_files_exact_match": files_match,
        "space_health": health,
        "sync_verified": sync_verified,
        "technical_deployment_verified": sync_verified,
        "functional_app_verification": False,
        "functional_app_verification_status": "pending_coordinator_user_confirmation",
        "human_review_required": True,
        "production_ready": False,
        "files": file_results,
    }
    output = Path("output/validation/care_profile_hf_sync_verification.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    Path("ops/verify_care_profile_hf_sync.py").unlink(missing_ok=True)
    Path(".github/workflows/verify-care-profile-hf-sync.yml").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
