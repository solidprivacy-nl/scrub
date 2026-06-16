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
- WP_DUTCH_LEGAL_RECALL_GAP_TESTS added tests-only xfail baselines for known Dutch legal recall gaps.
- WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES improved the review-candidate layer for selected Dutch legal reference values.

Gaps:

- No complete gold-label sidecars for the corpus yet.
- No accepted production recall/precision threshold or production-blocking gate exists.
- No production safety claim is supported.
- Dutch legal reference gaps are reduced for selected helper-level review candidates, but final CI/app evidence is still required.

Recommended workpackages:

- Later benchmark data package — complete gold-label sidecars.
- Later gated package — accepted thresholds and regression gate.
- Later approved package — verify and, if needed, continue a second narrow Dutch legal pattern round.

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

- Review table flow exists and remains the source of truth/fallback.
- Review filters and guidance exist.
- WP_SERIAL_REVIEW_UI is completed and app-verified as a small non-destructive panel.
- WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK removed the non-intuitive replacement helper panel from the normal flow.
- WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION added the bounded side-by-side review surface.
- WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX made the side-by-side panes visually equal-height.
- WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE was visually approved by the coordinator.
- WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION integrated bounded percentage-based synchronized scrolling in the side-by-side renderer.
- WP_REVIEW_SURFACE_CONTROL_CLEANUP made synchronized scrolling default without exposing a visible sync-checkbox and kept markers default-on.
- WP_REVIEW_SURFACE_DUPLICATE_HEADING_CLEANUP removed a duplicate review heading from the central side-by-side review surface.
- WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY closed out the promoted collapsible review table: visual pressure in the review phase is reduced while the replacement table remains source of truth and fallback.
- WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP removed temporary candidate/helper artifacts after verified promotion, reducing repo confusion without changing active app behavior.

Gaps:

- The review table remains the source of truth and fallback.
- Percentage-based synchronized scrolling can create imperfect alignment when source and processed text differ structurally after masking/replacement.
- No click-to-mark sensitive text prototype.
- No professional document editor exists.
- No separate frontend migration is approved.
- Replacement-decision helper internals should not be exposed directly as a user-facing panel.

Recommended workpackages:

- Later approved package — small redesigned replacement review implementation after separate explicit approval.
- Click-to-mark sensitive text prototype only after separate approval and after frontend/MVP evidence.
- Optional later UX cleanup — make Serial review compacter/collapsible only after separate coordinator approval.

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

Status: mitigating  
Impact: medium

Risk:

```text
Development slows because workers wait for coordinator screenshots instead of self-checking GitHub Actions and Hugging Face sync where connector permissions allow.
```

Current mitigations:

- Coordinator supplies screenshots/evidence when connector permissions cannot show the relevant run.
- Workpackages record Actions/sync status.
- `STATUS_MONITORING_RUNBOOK.md` exists and defines standard status states plus the expected Actions/Hugging Face verification order.
- Workers are instructed to use connector status tools first, then ask for coordinator evidence only when connector lookup is incomplete.

Gaps:

- Connector workflow-run lookup can still be incomplete for some push-triggered runs.
- No automated status artifact exists yet.

Recommended workpackages:

- Later status package — automated status artifact/check if connector limitations continue to slow closeouts.

---

## R9 — Dutch legal reference under-detection and role over-masking

Status: mitigating  
Impact: high

Risk:

```text
Dutch legal matter references can be missed or misclassified, while generic legal role words can be masked in ways that damage legal meaning.
```

Current mitigations:

- Human review table remains source of truth and fallback.
- `RECALL_BENCHMARK_SPEC.md` defines legal reference classes, context terms to preserve and over-masking traps.
- `tests/test_dutch_legal_recall_gap_baseline.py` captures known Dutch legal reference and role-preservation cases using synthetic text.
- WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES improved the candidate scanner for case-number-shaped values with spaces and extra Dutch legal/admin context cues.

Gaps:

- This first pattern round improves review candidates; it does not prove all recognizer/entity classifications are complete.
- Final CI/HF verification is still required because local test execution was unavailable in this environment.
- Broader production recall/precision thresholds and corpus sidecars remain future work.
- Role-word preservation still needs continued regression coverage as recognizers evolve.

Recommended workpackages:

- Later approved package — `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY` to verify Actions/HF and review whether any gaps remain.
- Later benchmark package — expand gold-label sidecars for Dutch legal/care documents.
