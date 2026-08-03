from __future__ import annotations

from pathlib import Path


TIMESTAMP = "2026-08-03 19:12 Europe/Amsterdam"
WP = "SCRUB-WP_CARE_PROFILE_APP_VERIFY"


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    Path(path).write_text(content, encoding="utf-8")


def prepend_once(path: str, marker: str, block: str) -> None:
    current = read(path)
    if marker not in current:
        write(path, block.rstrip() + "\n\n" + current)


def update_roadmap() -> None:
    path = "ROADMAP.md"
    text = read(path)
    anchor = (
        "The deterministic cross-profile regression matrix is now green. Across eight care "
        "document families and twelve legal examples, Care and International retain all 108 "
        "dedicated care expectations, Care/International and Legal/International dedicated-type "
        "parity hold, no dedicated Care or Legal entities leak into the wrong profiles, and no "
        "protected clinical phrase is overlapped. The historical legal metadata remains visible as "
        "132/148 deterministic expectations, sixteen recorded gaps and four negative observations; "
        "these are existing benchmark observations, not hidden or reclassified as Zorg success. "
        "Generic NER remains outside this matrix. The next gate is deployed app verification after "
        "GitHub-to-Hugging-Face sync is confirmed."
    )
    addition = anchor + (
        "\n\nGitHub-to-Hugging-Face synchronization is now independently verified for merge "
        "commit `cca4a25aaff28a7ba647c961d8e50f0e076921e2`: twelve relevant source files match "
        "byte-for-byte, all correctly scoped Zorg markers are present, the Streamlit health endpoint "
        "returns `200 / ok` and the Space root returns HTTP 200. The initial sync check produced a "
        "false negative because two marker groups were assigned to the wrong modules; the hashes were "
        "already equal and the corrected verification passed. The remaining gate is coordinator/user "
        "confirmation of the visible app behavior and generic-NER observation."
    )
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("ROADMAP app-verification anchor not found")
        write(path, text.replace(anchor, addition, 1))


def update_workpackages() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: implemented; Actions/sync verified; awaiting coordinator/user app verification.

Goal:
- Verify the deployed Zorgfilter selector and review behavior after technical integration and cross-profile regression passed.

Technical deployment result:

```text
GitHub main commit: cca4a25aaff28a7ba647c961d8e50f0e076921e2
Hugging Face Space: solidprivacy/scrub
Files compared: 12
Exact byte matches: 12/12
Correctly scoped markers: all passed
Space health: HTTP 200 / ok
Space root: HTTP 200
Technical deployment verified: true
Functional app verification: pending
Production ready: false
```

Evidence:
- `CARE_PROFILE_APP_VERIFICATION.md`
- `output/validation/care_profile_hf_sync_verification.json`
- `handover/workpackages/20260803_1912_care_profile_app_verify.md`

Pending coordinator/user checks:
- four profile choices and stable default;
- eight synthetic care examples;
- `Controle nodig` rendering for review-selected care rows while selected;
- patient/client replacement defaults;
- unchecked care candidates;
- unchanged Legal/General/International, review, export, Scrub Key and reinsert flows;
- no Script execution error.

Gate status:
- do not close or merge the verification-only package until the coordinator/user confirms the visible behavior.

Boundaries:
- verification-only; no product code or UI change;
- synthetic examples only;
- human review remains required;
- no production-readiness claim.
"""
    prepend_once("WORKPACKAGES.md", marker, block)


def update_changelog() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: technical deployment verified; visible app verification pending.

Purpose:
- Independently verify that the merged Zorgfilter integration reached Hugging Face before requesting human app verification.

Files added:
- `CARE_PROFILE_APP_VERIFICATION.md`
- `output/validation/care_profile_hf_sync_verification.json`
- `tests/test_care_profile_hf_sync_verification.py`
- `workpackage_claims/scrub_wp_care_profile_app_verify.md`
- `handover/workpackages/20260803_1912_care_profile_app_verify.md`

Verification result:
- compared twelve relevant GitHub and Hugging Face files byte-for-byte;
- verified equal SHA-256 values for all twelve files;
- verified correctly scoped Zorgfilter markers;
- verified Streamlit health `HTTP 200 / ok` and root HTTP 200;
- corrected an initial verification false negative caused by two marker groups being checked in the wrong modules;
- recorded functional app verification as pending rather than claiming success.

Validation context:
- UI integration final run #1885 passed: 986 tests;
- cross-profile matrix final run #1906 passed: 995 tests;
- verification-evidence tests and normal branch regression pending PR creation.

Intentionally not changed:
- product code, recognizers, profile behavior or UI;
- review, export, Scrub Key or reinsert semantics;
- runtime dependencies, cloud processing or production claims.
"""
    prepend_once("CHANGELOG.md", marker, block)


def update_risk_register() -> None:
    path = "RISK_REGISTER.md"
    text = read(path)
    anchor = (
        "The deterministic cross-profile matrix now passes all hard gates: 108/108 dedicated Care "
        "expectations are retained across Care and International, no dedicated Care or Legal entities "
        "leak into the wrong profiles, dedicated-type parity holds, and no protected clinical phrase "
        "is overlapped. Historical legal metadata remains explicitly recorded as 132/148 deterministic "
        "expectations, sixteen gaps and four negative observations. Risk R10 remains mitigating because "
        "GitHub-to-Hugging-Face deployment sync, generic-NER behavior and live app verification are still "
        "unconfirmed."
    )
    addition = anchor + (
        "\n\nDeployment sync is now independently verified: twelve relevant GitHub/Hugging Face "
        "files match byte-for-byte, all correctly scoped markers pass and the Space is healthy. Risk R10 "
        "remains mitigating only for the remaining human-visible app verification, generic-NER observation "
        "and the broader limitation that synthetic evidence does not prove production recall or precision."
    )
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("RISK_REGISTER app-verification anchor not found")
        write(path, text.replace(anchor, addition, 1))


def update_claim() -> None:
    path = "workpackage_claims/scrub_wp_care_profile_app_verify.md"
    text = read(path)
    if "Status: in_progress" in text:
        text = text.replace(
            "Status: in_progress",
            "Status: Actions/sync verified; awaiting coordinator/user app verification",
            1,
        )
    write(path, text)


def main() -> None:
    update_roadmap()
    update_workpackages()
    update_changelog()
    update_risk_register()
    update_claim()

    Path("ops/finalize_care_profile_app_verify_pending.py").unlink(missing_ok=True)
    Path(".github/workflows/finalize-care-profile-app-verify-pending.yml").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
