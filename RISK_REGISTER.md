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

Gaps:

- WP28C still needs GitHub Actions, Hugging Face sync and app verification before it can be fully closed out.
- UI acknowledgements are safety prompts only; they are not encryption, protected storage, automatic deletion or a managed key vault.
- No approved key recovery model.

Recommended workpackages:

- WP28C verification/app evidence.
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

Gaps:

- Word comments / kantlijncommentaren are still not scrubbed or removed by the current DOCX scrub/reinsert flow.
- No clean DOCX export policy yet.
- No product UI consumes the hygiene audit report yet.
- No approved export-blocking policy for high-risk hidden content.

Recommended workpackages:

- WP39 — Clean DOCX export policy.
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
- WP45 created `LOCAL_RUNTIME_ARCHITECTURE_PLAN.md`.
- WP46 added the minimal local Streamlit launcher path.
- WP47 added local launcher/documentation privacy tests.
- WP48 added a minimal Windows portable proof-of-concept wrapper.
- WP49 created `DESKTOP_PACKAGING_DECISION.md` and accepted D014.
- D015 now defers local installer/MSI/desktop packaging to the final roadmap phase after online/web validation of logic, interface, security and trustworthiness.

Gaps:

- WP47/WP48 validate launcher/documentation boundaries only; they are not full network-traffic captures.
- No full offline demonstration.
- No runtime packet/network inspection.
- No production security certification is supported.
- No signed or managed enterprise deployment proof exists.
- Installer testing remains intentionally deferred because installable-app validation is more labor-intensive than web-interface validation.

Recommended workpackages:

- Continue online/web validation and trust hardening first.
- Later network/privacy validation package — runtime network-traffic capture and temp-file inspection under controlled local conditions.
- Final-phase installer/packaging proof only after coordinator approval and after core product behavior is acceptable.

---

## R6 — Streamlit review UX ceiling

Status: open  
Impact: medium

Risk:

```text
A table-first Streamlit interface may not support the document-centric review experience needed for high-trust legal/care workflows.
```

Current mitigations:

- Review table flow exists.
- Review filters and guidance exist.

Gaps:

- No document-centric review specification.
- No click-to-mark sensitive text prototype.
- No frontend architecture decision for professional review UX.

Recommended workpackages:

- WP40 — Document-centric review UX specification.
- WP41 — Highlight-based review prototype decision.
- WP42 — Streamlit feasibility boundary review.
- WP43 — Frontend architecture decision.
- WP44 — Click-to-mark sensitive text prototype.

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
- STATUS_MONITORING_RUNBOOK.md defines status-check expectations.

Gaps:

- Connector limitations can still prevent workflow/status lookup in some cases.

Recommended workpackages:

- Continue using status runbook and handover evidence discipline.
