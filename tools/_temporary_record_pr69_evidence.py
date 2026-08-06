from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def replace_required(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise RuntimeError(f"Expected text not found in {path}: {old!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


replace_required(
    "WORKPACKAGES.md",
    "Status: `RELEASE_CANDIDATE_READY`; GitHub Actions and independent governance verification pending.",
    "Status: `RELEASE_CANDIDATE_READY`; GitHub Actions PR #69 run #2097 green (`1165 passed in 9.62s`); independent governance verification pending.",
)
replace_required(
    "CHANGELOG.md",
    "Status: implementation `RELEASE_CANDIDATE_READY`; GitHub Actions and independent governance assurance pending.",
    "Status: implementation `RELEASE_CANDIDATE_READY`; GitHub Actions PR #69 run #2097 green (`1165 passed in 9.62s`); independent governance assurance pending.",
)
replace_required(
    "CHANGELOG.md",
    "- GitHub Actions pending on the candidate PR;",
    "- GitHub Actions PR #69 run #2097: `1165 passed in 9.62s`;",
)
