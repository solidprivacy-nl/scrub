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
- WP39 created `CLEAN_DOCX_EXPORT_POLICY.md`, defining that current DOCX output must not be claimed as clean DOCX export and that export blocking/clean claims require separate approved implementation.

Gaps:

- Word comments / kantlijncommentaren are still not scrubbed or removed by the current DOCX scrub/reinsert flow.
- No product UI consumes the hygiene audit report yet.
- No clean DOCX export implementation exists.
- No approved export-blocking implementation exists for high-risk hidden content.
- The policy exists, but enforcement/UI/report integration remains future work.

Recommended workpackages:

- WP39B — DOCX hygiene audit UI planning, only if coordinator wants DOCX-specific UI planning first.
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
- WP42B created `highlight_preview.py`, a pure static highlight preview helper/model with tests for offsets, escaping, category labels and non-authoritative boundaries.
- WP42C created `STATIC_HIGHLIGHT_PREVIEW_UI_PLAN.md`, planning a future experimental read-only UI panel while preserving the review table as authoritative.
- WP42D attempted a small experimental read-only Streamlit preview panel, but the route failed repeatedly in runtime/startup verification.
- WP42D-ROLLBACK and WP42D-ROLLBACK-REPAIR disabled the startup mutation path and guarded against stale static-preview source/runtime state.
- WP42D-ROLLBACK-CLOSEOUT recorded that the Hugging Face app is back on the stable table-first interface and that the static-highlight/marking attempt is fully parked.
- WP_CONTEXT_CARD_HELPER created `context_cards.py`, a pure report-only helper for escaped prefix/match/suffix context cards around exact displayed-text offsets, with synthetic-only tests.
- WP_CONTEXT_CARD_STATUS_RECONCILE recorded the completed context-card helper in central project status after a parallel-edit conflict prevented the helper worker from updating shared documentation.
- WP_CONTEXT_CARD_UI_PLAN created planning/contract-only guidance for a non-authoritative context-card panel near the review table, with no UI implementation.
- WP_REPLACE_LOGIC_HELPER created `replacement_decision.py`, a pure replacement decision helper with tests for review states, conservative scope matching, report-only audit summaries and advisory export-readiness state.
- WP_REPLACE_LOGIC_UI_PLAN created `REPLACE_LOGIC_UI_PLAN.md`, planning future helper integration without changing Streamlit behavior.
- WP_REPLACE_LOGIC_UI_CONTRACT_TESTS added `tests/test_replace_logic_ui_contract.py`, locking the planned label/state/scope mappings and report-only/export-readiness boundaries before any replacement-decision UI implementation.
- WP_SERIAL_REVIEW_HELPER created a helper/tests-only serial review queue foundation for one-by-one review navigation and report-only audit summary.
- WP_SERIAL_REVIEW_UI_CONTRACT_TESTS created `SERIAL_REVIEW_UI_PLAN.md` and `tests/test_serial_review_ui_contract.py`, locking a future table-first, non-destructive, report-only serial review panel contract before any UI implementation.
- WP_SERIAL_REVIEW_UI_CONTRACT_STATUS_RECONCILE recorded the completed serial review UI contract tests in central project status after coordinator screenshot evidence showed green Actions and Hugging Face sync.
- WP43 created `FRONTEND_ARCHITECTURE_DECISION.md`, deciding to keep Streamlit for MVP validation and defer a separate frontend/professional document editor until MVP workflow evidence and user validation justify the migration risk.

Gaps:

- The stable table-first workflow is working again, but it still has the original document-context limitations.
- The static-highlight startup source mutation route is not safe enough to continue.
- Context cards are helper/planning-only and not yet integrated into a UI panel.
- Serial review queue and serial review UI contracts exist, but no UI implementation is approved yet.
- No combined review-panel view-model helper exists yet.
- No click-to-mark sensitive text prototype.
- No professional document editor exists.
- No separate frontend migration is approved.
- Replacement decision helper is not wired into the product UI yet.

Recommended workpackages:

- WP_REVIEW_PANEL_VIEW_MODEL_HELPER — pure helper combining serial queue and context-card data before any UI.
- WP_CONTEXT_CARD_UI_CONTRACT_TESTS — contract tests for the planned non-authoritative context-card panel.
- WP_SERIAL_REVIEW_UI — small non-destructive serial review panel only after explicit coordinator approval.
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
