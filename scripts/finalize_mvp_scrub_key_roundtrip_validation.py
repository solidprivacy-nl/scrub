from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION"
MARKER = f"## 2026-07-27 18:55 Europe/Amsterdam — {TITLE}"
HANDOVER = ROOT / "handover/workpackages/20260727_1855_mvp_scrub_key_roundtrip_validation.md"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def prepend_once(path: str, marker: str, block: str) -> None:
    text = read(path)
    if marker not in text:
        write(path, block.rstrip() + "\n\n" + text)


workpackages_block = f"""{MARKER}

Status: completed; deterministic validation passed; PR verification pending.

Summary:
- Added a versioned synthetic adversarial matrix with 15 Scrub Key and placeholder roundtrip scenarios.
- Verified intact, repeated, missing, unknown, translated, merged, malformed and changed placeholder behavior.
- Verified duplicate, incomplete, malformed, tampered and wrong Scrub Key behavior.
- Confirmed deterministic local execution with no AI or cloud processing.
- Changed no product code, UI, Scrub Key schema, export or reinsert semantics.

Validation result:
- Cases: 15.
- Failing cases: 0.
- Findings: 2.
- Critical findings: 1.
- Medium findings: 1.
- Production readiness: false.
- Human review remains required.

Critical evidence:
- A structurally valid wrong or tampered Scrub Key that reuses the same placeholder namespace can restore incorrect original values without a detectable mismatch.
- This requires separate triage because a safe solution may affect document/key binding, Scrub Key schema or export semantics.

Secondary evidence:
- Malformed tokens outside the strict placeholder grammar are reported indirectly through expected placeholders not found, rather than as explicit unknown malformed tokens.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE`.
"""
prepend_once("WORKPACKAGES.md", MARKER, workpackages_block)

changelog_block = f"""{MARKER}

Status: completed; deterministic validation passed; PR verification pending.

Purpose:
- Validate Scrub Key import/reinsert and placeholder roundtrip behavior against adversarial synthetic mutations.
- Record evidence before authorizing any schema, export or reinsert changes.

Files added:
- `test_cases/mvp_phase6/scrub_key_roundtrip_manifest.json`
- `mvp_scrub_key_roundtrip_validation.py`
- `scripts/run_mvp_scrub_key_roundtrip_validation.py`
- `tests/test_mvp_scrub_key_roundtrip_validation.py`
- `tests/test_mvp_scrub_key_roundtrip_report_contract.py`
- `output/validation/mvp_scrub_key_roundtrip_validation_report.json`
- `handover/workpackages/20260727_1855_mvp_scrub_key_roundtrip_validation.md`

Files changed:
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_roundtrip_validation.md`

Validation result:
- 15 synthetic cases; 0 failed cases.
- 1 critical finding: no reliable document/key binding when a wrong valid key reuses the same placeholder namespace.
- 1 medium finding: malformed placeholder mutations outside the grammar are signalled indirectly.
- Existing duplicate, incomplete, invalid, unknown and translated cases fail closed or remain visibly auditable as expected.
- Local-only: true; external AI: false; cloud processing: false.
- Production ready: false; human review required: true.

Intentionally not changed:
- product code or UI;
- Scrub Key schema, mappings, export, storage or lifecycle;
- placeholder grammar or automatic repair;
- reinsert helper semantics;
- filenames, MIME types or audit fields;
- cloud, AI, OCR or restored-PDF behavior.

Next recommended step:
- Start `SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE` before implementing a fix.

---
"""
prepend_once("CHANGELOG.md", MARKER, changelog_block)

roadmap = read("ROADMAP.md")
roadmap = roadmap.replace(
    "Last roadmap strategy update: 2026-07-27 — the document-first automatic reinsert flow is merged and app-verified; Scrub Key roundtrip validation is now active.",
    "Last roadmap strategy update: 2026-07-27 — Scrub Key roundtrip validation is complete and exposed a critical document/key-binding gap; evidence triage is now active before any schema or export change.",
)
roadmap = roadmap.replace(
    "5. SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION — active\n6. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE\n7. SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT",
    "5. SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION — completed\n6. SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE — active\n7. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE\n8. SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT",
)
status_anchor = "SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION — completed, synchronized and live-app verified."
if "SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION — completed with" not in roadmap:
    roadmap = roadmap.replace(
        status_anchor,
        status_anchor
        + "\nSCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION — completed with 15/15 cases passing and a critical document/key-binding gap routed to triage.",
    )
write("ROADMAP.md", roadmap)

plan = read("MVP_PHASE6_EXECUTION_PLAN.md")
if "SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE" not in plan:
    plan = plan.replace(
        "### 5. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE",
        "### 4A. SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE\n\nClassify the critical finding that a structurally valid wrong key can reuse the same placeholder namespace and restore incorrect values without a detectable mismatch. Decide whether document/key binding requires a key identifier, content fingerprint, manifest binding or another explicit contract. Do not change schema, export or reinsert semantics in the triage package.\n\n### 5. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE",
    )
write("MVP_PHASE6_EXECUTION_PLAN.md", plan)

risk = read("RISK_REGISTER.md")
r2_old = (
    "The manual missed-value entry flows through the existing replacement table and existing Scrub Key/export paths without changing key semantics. No key storage, schema or lifecycle behavior is added by the automatic reinsert flow."
)
r2_new = r2_old + (
    " The Phase 6 adversarial roundtrip matrix exposes a critical unresolved gap: a structurally valid wrong or tampered key that reuses the same placeholder namespace can restore incorrect original values without a detectable mismatch. This is routed to `SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE`; no schema or export change is authorized by the validation package."
)
risk = risk.replace(r2_old, r2_new)
r3_old = "Current mitigations include placeholder robustness helper/test work and reinsert audit reporting."
r3_new = r3_old + (
    " The Phase 6 roundtrip matrix validates translated, merged, unknown, repeated and malformed mutations. Unknown grammar-valid placeholders are visible, while malformed tokens outside the strict grammar are signalled indirectly through expected placeholders not found. This diagnostic limitation is included in the document-binding gap triage."
)
risk = risk.replace(r3_old, r3_new)
write("RISK_REGISTER.md", risk)

decision = read("DECISION_LOG.md")
decision_marker = "## 2026-07-27 — D032 — Roundtrip evidence requires document/key-binding triage before implementation"
if decision_marker not in decision:
    insertion = f"""{decision_marker}

Status: accepted evidence-routing decision

Decision:

```text
Treat the missing document/Scrub-Key binding as a critical Phase 6 finding. Do not implement an implicit heuristic or silently change the Scrub Key schema, export or reinsert semantics inside the validation package. Open a separate triage package to define the binding contract and migration boundaries first.
```

Reason:

- A wrong key with a disjoint placeholder namespace is visibly rejected through unknown/not-found audit evidence.
- A structurally valid wrong or tampered key with the same placeholder names restores wrong original values with no validation issue, unknown placeholder or missing-placeholder signal.
- Document labels are descriptive metadata and are not currently a verified binding mechanism.
- A safe correction may affect key creation, scrubbed output metadata, import compatibility and export semantics.

Boundaries:

- Preserve current deterministic local behavior until the triage decision is approved.
- Do not guess whether a key belongs to a document.
- Do not auto-repair malformed placeholders.
- Preserve existing audit evidence and human review.
- Use synthetic data only; no production-readiness claim.

Evidence:

- `output/validation/mvp_scrub_key_roundtrip_validation_report.json`
- `test_cases/mvp_phase6/scrub_key_roundtrip_manifest.json`
- `tests/test_mvp_scrub_key_roundtrip_validation.py`

---

"""
    decision = decision.replace("---\n\n## 2026-07-27 — D031", "---\n\n" + insertion + "## 2026-07-27 — D031", 1)
write("DECISION_LOG.md", decision)

claim_path = "workpackage_claims/scrub_wp_mvp_scrub_key_roundtrip_validation.md"
claim = read(claim_path)
claim = claim.replace("Status: in_progress", "Status: completed; deterministic validation passed; PR verification pending")
claim = claim.replace(
    "- Add pure matrix/report helpers, manifest, tests and machine-readable evidence; then route any reproducible gap through a separate triage package.",
    "- Merge after GitHub Actions pass, then start `SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE`.",
)
if "Validation result:" not in claim:
    claim += """

Validation result:
- Cases: 15; failed cases: 0.
- Findings: 2; critical: 1; medium: 1.
- Critical finding: missing reliable document/key binding for a structurally valid wrong key reusing the same placeholder namespace.
- Medium finding: malformed tokens outside the grammar are signalled indirectly.
- Local-only: true; AI/cloud: false.
- Product code changed: false.
- Production ready: false; human review required: true.
- Report: `output/validation/mvp_scrub_key_roundtrip_validation_report.json`.
- Handover: `handover/workpackages/20260727_1855_mvp_scrub_key_roundtrip_validation.md`.
"""
write(claim_path, claim)

HANDOVER.parent.mkdir(parents=True, exist_ok=True)
HANDOVER.write_text(
    f"""# Handover — {TITLE}

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

{TITLE}

## Status

Completed; deterministic validation passed; PR verification pending.

## Summary

A pure synthetic adversarial matrix now validates Scrub Key and placeholder roundtrip behavior across 15 scenarios. All observed results match the explicit expectations. The matrix records one critical document/key-binding gap and one medium malformed-placeholder diagnostic limitation. No product semantics were changed.

## Files added

- `test_cases/mvp_phase6/scrub_key_roundtrip_manifest.json`
- `mvp_scrub_key_roundtrip_validation.py`
- `scripts/run_mvp_scrub_key_roundtrip_validation.py`
- `tests/test_mvp_scrub_key_roundtrip_validation.py`
- `tests/test_mvp_scrub_key_roundtrip_report_contract.py`
- `output/validation/mvp_scrub_key_roundtrip_validation_report.json`
- `handover/workpackages/20260727_1855_mvp_scrub_key_roundtrip_validation.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_roundtrip_validation.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

## Tests

- 15 manifest cases match the current deterministic helper behavior.
- Existing secure Scrub Key import/export and reinsert tests remain in the targeted validation set.
- Committed report must equal the deterministic generator output.
- No Streamlit, network, AI or cloud client imports are allowed in the validation module/tests.
- Synthetic-only and immutability contracts are included.

## Validation

- Cases: 15; failures: 0.
- Critical findings: 1.
- Medium findings: 1.
- Local-only: true.
- AI processing: false.
- Cloud processing: false.
- GitHub Actions: pending PR validation.
- Hugging Face sync: not functionally applicable; no runtime or app code changed.
- App verification: not applicable; no visible UI behavior changed.

## Notes / risks

- A wrong, structurally valid Scrub Key with the same placeholder namespace can silently restore incorrect originals.
- Malformed tokens outside the strict placeholder grammar are only indirectly signalled.
- No binding heuristic, schema change, export change or automatic repair was introduced.
- Human review remains mandatory and production readiness remains false.

## Next recommended step

- Start `SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE` before implementing a fix.
""",
    encoding="utf-8",
)
