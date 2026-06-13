# SolidPrivacy Scrub — Risk Register

This register tracks product, privacy, security and trust risks.

Status values:

```text
open
mitigating
accepted
closed
```

Impact values:

```text
critical
high
medium
low
```

---

## R1 — False negatives / missed sensitive data

Status: mitigating  
Impact: critical

Risk:

```text
Sensitive data remains in the scrubbed output and the user wrongly trusts the result.
```

Current mitigations:

- Human review workflow.
- Review guidance and final review summary.
- WP19-WP24 created the recall/trust benchmark and report-only residual-risk foundation.

Gaps:

- No complete gold-label sidecars for the corpus yet.
- No accepted production recall/precision threshold or production-blocking gate exists.
- No production safety claim is supported.

Recommended workpackages:

- Later benchmark data package — complete gold-label sidecars.
- Later gated package — accepted thresholds and regression gate.

---

## R2 — Scrub Key leakage or accidental sharing

Status: mitigating  
Impact: critical

Risk:

```text
The Scrub Key is shared, leaked, retained too long, tampered with or mishandled, allowing full re-identification of scrubbed content.
```

Current mitigations:

- UI warnings around Scrub Key reinsert.
- Local-only/no-AI/no-cloud positioning for reinsert.
- WP25-WP29C covered threat model, lifecycle specs, warning planning/implementation, import/export tests and warning UI test scaffolding.
- WP28C warning/acknowledgement UI is closed out after Actions/HF/app verification.

Gaps:

- UI acknowledgements are safety prompts only; they are not encryption, protected storage, automatic deletion or a managed key vault.
- No approved key recovery model.

Recommended workpackages:

- Later implementation package — protected local file handling.
- Later implementation package — encrypted key container.
- Later implementation package — local vault / managed key store.

---

## R3 — Placeholder corruption during AI roundtrip

Status: mitigating  
Impact: high

Risk:

```text
An AI system rewrites, translates, merges or deletes placeholders, causing deterministic reinsert to fail or restore incompletely.
```

Current mitigations:

- Unknown placeholders and not-found placeholders are reported in reinsert audit flows.
- WP30-WP34 created placeholder robustness review, future robust format proposal, validation helper, audit helper and synthetic AI-output corruption tests.

Gaps:

- Robust placeholder generation has not been implemented in product flow.
- No migration or backward-compatibility implementation exists yet.
- No Scrub Key schema/version support for robust placeholder metadata exists yet.

Recommended workpackages:

- Later gated package — robust placeholder generation and compatibility implementation.
- Later audit/UI package — user-visible placeholder corruption warning integration.

---

## R4 — Hidden document content and metadata leakage

Status: mitigating  
Impact: high

Risk:

```text
DOCX metadata, comments, tracked changes, headers, footers or hidden content contain sensitive data that is not scrubbed or cleaned.
```

Current mitigations:

- DOCX reinsert limitations are documented.
- WP35 created DOCX hidden-content risk review.
- WP36A recorded residual placeholder/comments risk.
- WP37 created read-only extraction visibility for headers, footers, comments/person metadata and tracked-change markers.
- WP38 created a report-only DOCX hygiene audit helper.
- WP39 created `CLEAN_DOCX_EXPORT_POLICY.md`, defining that current DOCX output must not be claimed as clean DOCX export and that export blocking/clean claims require separate approved implementation.
- WP39B created `DOCX_HYGIENE_AUDIT_UI_PLAN.md`, planning how the existing report-only hygiene audit can later be surfaced without changing export behavior.
- WP39C added `tests/test_docx_hygiene_audit_ui_plan.py`, contract-testing that the planned UI remains report-only, does not claim clean DOCX, does not block export, does not clean/remove DOCX content, and does not change Scrub Key or reinsert behavior.
- WP39D implemented a small report-only DOCX hygiene audit UI panel near DOCX export, using the existing helper without export blocking, clean-DOCX claims, DOCX cleaning/removal, Scrub Key changes or reinsert behavior changes.

Gaps:

- Word comments / kantlijncommentaren are still not scrubbed or removed by the current DOCX scrub/reinsert flow.
- Product UI now reports supported DOCX hygiene risk, but it does not clean or remove hidden content.
- No clean DOCX export implementation exists.
- No approved export-blocking implementation exists for high-risk hidden content.
- Unsupported DOCX parts remain future work.

Recommended workpackages:

- WP39D-VERIFY — closeout/app verification for DOCX hygiene audit UI after Actions and Hugging Face sync are green.
- Later gated package — DOCX metadata cleaner helper after explicit metadata-only boundary approval.

---

## R5 — Cloud-demo trust gap and deferred installer risk

Status: mitigating  
Impact: high

Risk:

```text
The final product promise is local-first, but the current fast validation surface is the Hugging Face cloud demo. Confidential real documents should not be processed there, and installer work should not start before core behavior is trusted.
```

Current mitigations:

- Roadmap includes local desktop/offline direction.
- UI messaging emphasizes local/no-AI/no-cloud for helper operations where applicable.
- WP45-WP49 completed the local runtime and packaging decision line through decision-only packaging deferral.

Gaps:

- No full offline demonstration.
- No runtime packet/network inspection.
- No production security certification is supported.
- No signed or managed enterprise deployment proof exists.

Recommended workpackages:

- Continue online/web validation and trust hardening first.
- Final-phase installer/packaging proof only after coordinator approval and after core product behavior is acceptable.

---

## R6 — Review UX and replace-flow ceiling

Status: mitigating  
Impact: medium

Risk:

```text
A table-first interface and unclear replacement decisions may not support the document-centric review experience needed for high-trust legal/care workflows.
```

Current mitigations:

- Review table flow exists and is the current working baseline/fallback.
- Review filters and guidance exist.
- WP40 created the document-centric review UX specification.
- WP41 created the highlight-based review prototype decision.
- WP42 created the Streamlit feasibility boundary.
- WP42D rollback/closeout parked the failed static-highlight startup mutation route.
- Context-card, serial-review and review-panel view-model helper/planning/test work created safer helper-driven review surfaces.
- WP_SERIAL_REVIEW_UI is completed and app-verified as a small non-destructive panel.
- WP43 created `FRONTEND_ARCHITECTURE_DECISION.md`, deciding to keep Streamlit for MVP validation and defer a separate frontend/professional document editor until MVP workflow evidence and user validation justify the migration risk.

Gaps:

- The stable table-first workflow remains the source of truth and fallback.
- The static-highlight startup source mutation route is not safe enough to continue.
- No click-to-mark sensitive text prototype.
- No professional document editor exists.
- No separate frontend migration is approved.
- Replacement decision helper is not wired into a mutating product UI yet.

Recommended workpackages:

- Later approved package — replacement decision UI implementation.
- Click-to-mark sensitive text prototype only after separate approval and after frontend/MVP evidence.

---

## R7 — PDF limitations misunderstood by users

Status: mitigating  
Impact: high

Risk:

```text
Users may assume PDF support means complete restored PDF reinsert or OCR, while the approved scope is text-based extraction to restored TXT only.
```

Current mitigations:

- WP15 reliability review.
- WP16 helper-only path.
- WP17 UI planning.
- WP18 UI warnings and audit fields.
- WP18-FIX and WP18B completed the verification/closeout path.

Boundaries:

- No restored PDF output.
- No OCR.
- No PDF-to-DOCX reconstruction.
- No layout preservation promises.

Recommended workpackages:

- Keep PDF scope warnings clear in future UI changes.

---

## R8 — Workflow status dependence on coordinator screenshots

Status: open  
Impact: medium

Risk:

```text
Development slows because workers wait for coordinator screenshots instead of self-checking GitHub Actions and Hugging Face sync where connector permissions allow.
```

Current mitigations:

- Coordinator supplies screenshots/evidence.
- Workpackages record Actions/sync status.

Gaps:

- No formal monitoring runbook.
- No standard status states.
- No automated status artifact.

Recommended workpackages:

- WP57 — Workflow status monitoring runbook and checks.
