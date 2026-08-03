from pathlib import Path

WP = "SCRUB-WP_CARE_PROFILE_V1_POLICY_AND_CORPUS_FOUNDATION"


def replace_once(path: str, old: str, new: str) -> None:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"Expected text not found in {path}: {old[:120]!r}")
    file_path.write_text(text.replace(old, new, 1), encoding="utf-8")


replace_once(
    "WORKPACKAGES.md",
    f"## 2026-08-03 15:31 Europe/Amsterdam — {WP}\n\nStatus: in_progress; helper/test-first implementation on dedicated branch.",
    f"## 2026-08-03 15:31 Europe/Amsterdam — {WP}\n\nStatus: completed; policy/corpus foundation implemented and validated.",
)
replace_once(
    "WORKPACKAGES.md",
    "Sequential follow-up:\n1. `SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE`",
    "Active next package:\n1. `SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE`",
)
replace_once(
    "CHANGELOG.md",
    f"## 2026-08-03 15:31 Europe/Amsterdam — {WP}\n\nStatus: in progress; policy/corpus foundation implemented on a dedicated branch.",
    f"## 2026-08-03 15:31 Europe/Amsterdam — {WP}\n\nStatus: completed; policy/corpus foundation implemented and validated.",
)
replace_once(
    "CHANGELOG.md",
    "Validation:\n- GitHub Actions pending on the branch;\n- Hugging Face sync not functionally relevant;\n- app verification not applicable.",
    "Validation:\n- full GitHub Actions run #1818 passed: 918 tests;\n- Hugging Face sync not functionally relevant because no runtime/UI file changed;\n- app verification not applicable.",
)
replace_once(
    "workpackage_claims/scrub_wp_care_profile_v1_policy_and_corpus_foundation.md",
    "Status: in_progress",
    "Status: completed",
)

handover_path = Path("handover/workpackages/20260803_1531_care_profile_v1_policy_and_corpus_foundation.md")
handover = handover_path.read_text(encoding="utf-8")
handover = handover.replace(
    "Status: implemented on branch; final validation running",
    "Status: completed; ready for merge",
    1,
)
handover = handover.replace(
    "- Final GitHub Actions status: running on the corrected head.",
    "- Final GitHub Actions run #1818: 918 tests passed on the corrected head.",
    1,
)
handover_path.write_text(handover, encoding="utf-8")

Path("ops/finalize_care_profile_v1_foundation.py").unlink(missing_ok=True)
Path(".github/workflows/finalize-care-profile-v1-foundation.yml").unlink(missing_ok=True)
