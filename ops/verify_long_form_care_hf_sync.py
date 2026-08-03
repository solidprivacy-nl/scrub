from __future__ import annotations

import hashlib
import json
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "care_test_examples.py",
    "care_test_example_expansions.py",
)
HF_BASE = "https://huggingface.co/spaces/solidprivacy/scrub/resolve/main"
HEALTH_URL = "https://solidprivacy-scrub.hf.space/_stcore/health"
MAX_ATTEMPTS = 30
RETRY_SECONDS = 10


def _fetch(url: str) -> tuple[int, bytes]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "solidprivacy-scrub-sync-verifier/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return int(response.status), response.read()


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def verify_once() -> dict:
    files = []
    all_match = True

    for path in FILES:
        local = (ROOT / path).read_bytes()
        try:
            status, remote = _fetch(f"{HF_BASE}/{path}")
            error = None
        except (urllib.error.URLError, TimeoutError) as exc:
            status, remote, error = 0, b"", str(exc)

        exact_match = status == 200 and local == remote
        all_match = all_match and exact_match
        files.append(
            {
                "path": path,
                "http_status": status,
                "local_sha256": _sha256(local),
                "remote_sha256": _sha256(remote) if remote else None,
                "exact_match": exact_match,
                "error": error,
            }
        )

    try:
        health_status, health_body = _fetch(HEALTH_URL)
        health_error = None
    except (urllib.error.URLError, TimeoutError) as exc:
        health_status, health_body, health_error = 0, b"", str(exc)

    healthy = health_status == 200 and health_body.strip().lower() == b"ok"
    return {
        "files": files,
        "all_files_exact_match": all_match,
        "health": {
            "http_status": health_status,
            "body": health_body.decode("utf-8", errors="replace").strip(),
            "healthy": healthy,
            "error": health_error,
        },
        "verified": all_match and healthy,
    }


def main() -> None:
    latest = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        latest = verify_once()
        latest["attempt"] = attempt
        print(json.dumps(latest, ensure_ascii=False, indent=2, sort_keys=True))
        if latest["verified"]:
            return
        if attempt < MAX_ATTEMPTS:
            time.sleep(RETRY_SECONDS)

    raise SystemExit("Hugging Face synchronization did not verify within the bounded retry window")


if __name__ == "__main__":
    main()
