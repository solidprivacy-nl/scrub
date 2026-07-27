from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CLOSEOUT_TITLE = "SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_APP_VERIFY_CLOSEOUT"
CLOSEOUT_MARKER = f"## 2026-07-27 18:28 Europe/Amsterdam — {CLOSEOUT_TITLE}"
HANDOVER_PATH = ROOT / "handover/workpackages/20260727_1828_mvp_reinsert_auto_flow_simplification_app_verify_closeout.md"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def prepend_once(path: str, marker: str, block: str) -> None:
    text = read(path)
    if marker not in text:
        write(path, block.rstrip() + "\n\n" + text)


workpackages_block = f"""{CLOSEOUT_MARKER}

Status: completed and app-verified.

Evidence:
- PR #38 merged as `390f381c1464883f220716655c5067dadd0bb4c9`.
- Final clean PR GitHub Actions run #1678 passed.
- The coordinator live-tested the deployed three-step workflow and confirmed it is working.
- The live result proves that the merged UI reached the Hugging Face Space.

Verified behavior:
- Step 1 begins with the source document or pasted text.
- Step 2 accepts and automatically validates the corresponding Scrub Key.
- Local deterministic reinsert starts automatically for one valid source/key pair.
- Redundant source/key acknowledgement checkboxes and execution buttons are absent.
- One confidentiality acknowledgement remains immediately before download.
- Existing output filenames, MIME types, audit reporting and DOCX/PDF boundaries remain intact.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.
"""
prepend_once("WORKPACKAGES.md", CLOSEOUT_MARKER, workpackages_block)

changelog_block = f"""{CLOSEOUT_MARKER}

Status: completed and app-verified.

Purpose:
- Record successful live verification of the document-first automatic reinsert workflow.
- Close the evidence-driven UI blocker before continuing Scrub Key roundtrip validation.

Validation result:
- PR #38 merge commit: `390f381c1464883f220716655c5067dadd0bb4c9`.
- Final clean PR GitHub Actions run #1678: passed.
- Full repository suite before merge: 797 passed.
- Hugging Face deployment: confirmed by live testing of the merged three-step workflow.
- App verification: passed; coordinator reported `getest en werkend`.

Verified product boundaries:
- Document/text remains step 1, Scrub Key step 2 and restored download step 3.
- Automatic source recognition, key validation and local deterministic reinsert work as intended.
- One final confidential-output acknowledgement remains at download.
- No Scrub Key schema, helper semantics, export filenames/MIME types, cloud, AI, OCR or restored-PDF behavior changed.
- Human review remains required; no production-readiness claim is made.

Files added:
- `workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_app_verify_closeout.md`
- `handover/workpackages/20260727_1828_mvp_reinsert_auto_flow_simplification_app_verify_closeout.md`

Files changed:
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_implementation.md`
- `handover/workpackages/20260727_1706_mvp_reinsert_auto_flow_simplification_implementation.md`

Next recommended step:
- Start `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

---
"""
prepend_once("CHANGELOG.md", CLOSEOUT_MARKER, changelog_block)

roadmap = read("ROADMAP.md")
roadmap = roadmap.replace(
    "Last roadmap strategy update: 2026-07-27 — DOCX fidelity is app-verified; a concrete Phase 6 reinsert-flow clarity blocker is being resolved before Scrub Key roundtrip validation continues.",
    "Last roadmap strategy update: 2026-07-27 — the document-first automatic reinsert flow is merged and app-verified; Scrub Key roundtrip validation is now active.",
)
roadmap = roadmap.replace(
    "SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION — active narrow evidence-driven UI blocker before the general Scrub Key roundtrip package.",
    "SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION — completed, synchronized and live-app verified.",
)
roadmap = roadmap.replace(
    "4. SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION — active evidence-driven blocker\n5. SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION",
    "4. SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION — completed and app-verified\n5. SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION — active",
)
write("ROADMAP.md", roadmap)

claim_path = "workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_implementation.md"
claim = read(claim_path)
claim = claim.replace(
    "Status: implemented; full suite passed; final PR validation pending",
    "Status: completed and app-verified",
)
claim = claim.replace(
    "- Verify clean final standard Actions, merge, verify Hugging Face sync and request live app verification.",
    "- Start `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.",
)
if "App verification result:" not in claim:
    claim += """

App verification result:
- Passed on 2026-07-27 after PR #38 merge.
- Coordinator confirmed the deployed three-step reinsert workflow is tested and working.
- GitHub Actions run #1678 passed before merge.
- Live merged behavior confirms Hugging Face synchronization.
- Merge commit: `390f381c1464883f220716655c5067dadd0bb4c9`.
"""
write(claim_path, claim)

handover_path = "handover/workpackages/20260727_1706_mvp_reinsert_auto_flow_simplification_implementation.md"
handover = read(handover_path)
handover = handover.replace(
    "Implemented; full suite passed; final PR validation pending.",
    "Completed and app-verified.",
)
handover = handover.replace(
    "- GitHub Actions: final PR run pending after governance finalisation.\n- Hugging Face sync: pending after merge.\n- App verification: required after sync because the visible workflow changed.",
    "- GitHub Actions: final clean PR run #1678 passed.\n- Hugging Face sync: confirmed by live availability of the merged three-step workflow.\n- App verification: passed; coordinator confirmed the workflow is tested and working.",
)
handover = handover.replace(
    "- Verify PR Actions, merge, verify Hugging Face sync and live-test the three-step automatic flow.\n- Continue `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION` after app verification.",
    "- Start `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.",
)
write(handover_path, handover)

closeout_claim_path = "workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_app_verify_closeout.md"
closeout_claim = read(closeout_claim_path)
closeout_claim = closeout_claim.replace("Status: in_progress", "Status: completed and app-verified")
closeout_claim = closeout_claim.replace(
    "- Finalize closeout evidence, run standard GitHub Actions, merge, then start `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.",
    "- Merge this documentation-only closeout after GitHub Actions pass, then start `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.",
)
closeout_claim += """

Validation result:
- PR #38 final clean Actions run #1678 passed.
- Merge commit: `390f381c1464883f220716655c5067dadd0bb4c9`.
- Hugging Face sync: confirmed through live verification of merged behavior.
- App verification: passed on 2026-07-27.
- Handover: `handover/workpackages/20260727_1828_mvp_reinsert_auto_flow_simplification_app_verify_closeout.md`.
"""
write(closeout_claim_path, closeout_claim)

HANDOVER_PATH.parent.mkdir(parents=True, exist_ok=True)
HANDOVER_PATH.write_text(
    f"""# Handover — {CLOSEOUT_TITLE}

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

{CLOSEOUT_TITLE}

## Status

Completed and app-verified.

## Summary

The merged document-first automatic reinsert workflow was live-tested successfully. Users can upload the source document/text, upload the corresponding Scrub Key and proceed to the restored download without redundant intermediate acknowledgement checkboxes or execution buttons. One final confidential-output acknowledgement remains directly before download.

## Files added

- `workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_app_verify_closeout.md`
- `handover/workpackages/20260727_1828_mvp_reinsert_auto_flow_simplification_app_verify_closeout.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_implementation.md`
- `handover/workpackages/20260727_1706_mvp_reinsert_auto_flow_simplification_implementation.md`

## Tests

- No product-code tests added; documentation-only closeout.
- Implementation full repository suite before merge: 797 passed.
- Final clean PR GitHub Actions run #1678 passed.

## Validation

- GitHub Actions: passed for the implementation PR; closeout PR validation pending.
- Hugging Face sync: confirmed by live merged behavior.
- App verification: confirmed on 2026-07-27; coordinator reported the workflow is tested and working.

## Notes / risks

- One final confidentiality acknowledgement remains before restored-output download.
- Invalid or ambiguous Scrub Keys remain blocked by structural validation.
- Unknown, duplicate and missing placeholders remain visible in audit reporting.
- PDF remains restored TXT only; no OCR or restored PDF.
- Unsupported DOCX parts remain documented.
- Human review remains mandatory; no production-readiness claim is made.

## Next recommended step

- Start `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.
""",
    encoding="utf-8",
)
