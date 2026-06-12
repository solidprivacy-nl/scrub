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

Why it matters:

A scrubber has asymmetric failure costs. A false positive is annoying; a false negative may create the exact privacy incident the product wanted to avoid.

Current mitigations:

- Human review workflow.
- Review guidance and final review summary.
- Synthetic regression tests for selected recognizers.
- WP19 created `RECALL_BENCHMARK_SPEC.md`, defining how Scrub will measure recall, precision, per-entity scorecards, context-term preservation and CI reporting on messy synthetic Dutch legal and care documents.
- WP20 created the first synthetic messy legal, zorg and mixed corpus fixtures.
- WP21 created the gold-label sidecar schema foundation in `benchmark/gold/schema/gold_label_schema.json`, covering canonical entity classes, zero-based inclusive/exclusive offsets, expected text spans, preserve terms, known traps, normalization guidance and future runner expectations.
- WP22 created `benchmark/run_recall_precision.py`, a deterministic local report-only runner that validates gold-label offsets and source spans, then reports exact and value-normalized recall/precision, per-domain metrics, per-entity-class metrics, false negatives, false positives, preserve-term failures, known-trap failures and diagnostic-only partial overlaps for supplied prediction JSON.
- WP23 created `benchmark/build_entity_scorecard.py`, a report-only entity-class scorecard builder that can write CI-friendly JSON and Markdown artifacts while explicitly recording `synthetic_only`, `report_only`, `thresholds_applied: false`, `production_gate: false` and `safe_for_production_claim: false`.
- WP24 created `benchmark/build_residual_risk_report.py`, a report-only false-negative residual-risk report builder that makes remaining limitations and residual risks explicit without adding thresholds, production gates or production safety claims.

Gaps:

- No complete gold-label sidecars for the corpus yet.
- The WP22 runner still scores supplied prediction JSON only; it does not invoke recognizers or establish accepted baselines.
- The WP23 scorecard and WP24 residual-risk report are report-only; no recall/precision threshold or production-blocking gate exists.
- No production safety claim is supported.
- No user-facing residual-risk/audit integration exists yet.

Recommended workpackages:

- Later benchmark data package — complete gold-label sidecars for the committed synthetic corpus.
- Later gated package — accepted thresholds and regression gate only after baselines and policy are approved.
- Later audit/support package — user-facing residual-risk/audit language after internal report output is stable.

---

## R2 — Scrub Key leakage or accidental sharing

Status: mitigating  
Impact: critical

Risk:

```text
The Scrub Key is shared, leaked, retained too long, tampered with or mishandled, allowing full re-identification of scrubbed content.
```

Why it matters:

The Scrub Key maps placeholders to real sensitive values. It is therefore concentrated sensitive re-identification data. Scrub Key-based output is pseudonymized, not fully anonymized, as long as the key exists.

Current mitigations:

- UI warnings around Scrub Key reinsert.
- Local-only/no-AI/no-cloud positioning for reinsert.
- `SCRUB_KEY_SPEC.md` states that Scrub Key-based output is pseudonymization, not full anonymization.
- WP25 created `SCRUB_KEY_THREAT_MODEL.md`, defining accidental sharing, local storage, download-folder, e-mail/AI-upload, shared-computer, retention, loss-of-key, tampering, malformed-key and import/export risks.
- WP26 created `SCRUB_KEY_LIFECYCLE_SPEC.md`, defining lifecycle states, retention/deletion expectations, loss-of-key and tampering consequences, audit/logging expectations and protection options.
- WP27 created `SCRUB_KEY_WARNING_UX_PLAN.md`, defining warning severity levels, acknowledgement expectations and proposed Dutch UI copy for Scrub Key creation, export/download, storage, import/reload, reinsert, restored downloads, expiry/delete guidance, shared-computer risk, e-mail/AI upload risk, loss-of-key and tampering/mismatch moments.
- WP28 created `SCRUB_KEY_EXPIRY_DELETE_POLICY.md`, defining user-controlled retention, expiry and deletion policy; Downloads/shared-computer/manual deletion guidance; loss-of-key and tampering consequences; audit/logging expectations; and the rule that Scrub must not silently delete keys or keep hidden recovery copies.
- WP28B created `SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md`, mapping warning copy and acknowledgement requirements to exact current Streamlit patch locations before UI implementation.
- WP28C implemented MVP warning/acknowledgement gating for Scrub Key export/import, local reinsert actions and restored-output downloads. This is pending GitHub Actions, Hugging Face sync and app verification.
- WP29 added secure import/export regression tests for the current Scrub Key helper surface.
- WP29B expanded edge-case coverage and added minimal validation hardening so unsupported `schema_version` values are reported instead of accepted.

Gaps:

- WP28C still needs GitHub Actions, Hugging Face sync and app verification before it can be considered fully closed out.
- UI acknowledgements are safety prompts only; they are not encryption, automatic deletion, expiry enforcement, protected storage or a managed key vault.
- No encryption/protection implementation.
- No implemented expiry/delete UI or automated lifecycle tooling.
- No tamper-proof or authenticated Scrub Key format.
- Secure import/export tests now cover the current helper surface, but future key-container, document-mismatch and protected-storage behavior still require separate approved work.
- No automatic cleanup for browser Downloads or unmanaged local storage.
- No local vault / managed key store.
- No approved key recovery model.

Recommended workpackages:

- WP28C-VERIFY — GitHub Actions, Hugging Face sync and app verification closeout.
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

Why it matters:

The current reinsert path is deterministic and exact-match based. This is safe when placeholders are preserved exactly, but fragile when scrubbed content is rewritten, translated, summarized or moved through markdown, HTML, DOCX or PDF text extraction. The most dangerous failure is silent partial restoration: some placeholders restore while others are missing, merged or changed.

Current mitigations:

- Unknown placeholders and not-found placeholders are reported in reinsert audit flows.
- Duplicate placeholders in the Scrub Key are detected and excluded from deterministic replacement.
- WP30 created `PLACEHOLDER_ROBUSTNESS_REVIEW.md`, documenting current assumptions, corruption examples, translation/summarization/formatting risks, candidate robust formats, checksum ideas, validation/audit direction, migration risks and backward compatibility concerns.
- WP31 created `PLACEHOLDER_FORMAT_PROPOSAL.md`, recommending the future architecture direction `[[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]]`, for example `[[SP_PERSON_0001_A7F3]]`, as proposal-only and additive to legacy placeholders.
- WP32 created `placeholder_validation.py`, an additive helper that parses and validates future robust placeholder tokens, computes deterministic integrity tokens from non-sensitive placeholder metadata only, and keeps legacy placeholders as a separate compatibility mode.
- WP33 created `placeholder_audit.py`, an additive audit helper that classifies legacy, robust, malformed, truncated, integrity-failed and unknown placeholder-like tokens without repairing or guessing intent.
- WP34 added synthetic AI-output placeholder corruption fixtures and tests for translation, summarization/deletion, markdown/HTML wrapping and split tokens, spacing mutation, punctuation preservation, robust truncation, integrity mismatch, placeholder merge and invented placeholder-like tokens.

Gaps:

- Robust placeholder generation has not been implemented in product flow.
- No migration or backward-compatibility implementation exists yet.
- No Scrub Key schema/version support for robust placeholder metadata exists yet.
- WP34 is still helper/audit-test focused; it does not wire placeholder-audit warnings into product UI/export flows.

Recommended workpackages:

- Later gated package — robust placeholder generation and compatibility implementation, only after validation and schema decisions.
- Later audit/UI package — user-visible placeholder corruption warning integration after audit semantics are approved.

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
- Roadmap already recognizes document hygiene and metadata-clean export as important.
- Current DOCX helper reports limitations and unsupported parts for headers, footers, comments, tracked changes, metadata and split-run placeholders.
- WP35 created `DOCX_HIDDEN_CONTENT_RISK_REVIEW.md`, defining current assumptions, hidden-content leakage risks, audit requirements, safe extraction/cleaning sequence and future warning/blocking policy boundaries.
- WP36A created `DOCX_RESIDUAL_PLACEHOLDER_COMMENTS_TRIAGE.md` and synthetic tests for the app-verification finding that DOCX restored output can still contain residual placeholders and that Word comments/kantlijncommentaren remain outside current processing.
- WP37 created `docx_hidden_content_extractor.py`, adding local read-only extraction/audit visibility for headers, footers, comments/person metadata and tracked-change markers without cleaning, removal, export blocking, UI changes or export semantics changes.
- WP38 created `docx_hygiene_audit.py`, turning WP37 extraction output into a report-only DOCX hygiene audit with severity, counts, findings and explicit non-change flags.

Gaps:

- Residual placeholders such as `[PERSOON_01]` can remain in restored DOCX when the loaded Scrub Key mapping does not match them exactly or Word splits placeholders across runs.
- Word comments / kantlijncommentaren are still not scrubbed or removed by the current DOCX scrub/reinsert flow; WP37/WP38 only detect and report them.
- Headers, footers and tracked changes are detectable/reportable, but no product UI consumes the audit report yet.
- No clean DOCX export policy yet.
- No implementation for footnotes/endnotes, custom XML, text boxes/shapes or embedded object handling.
- No approved export-blocking policy for high-risk hidden content.
- No DOCX metadata cleaner helper yet; WP36 remains blocked until a tighter metadata-only helper boundary is approved.

Recommended workpackages:

- WP39 — Clean DOCX export policy.
- Later gated package — DOCX metadata cleaner helper after explicit metadata-only boundary approval.

---

## R5 — Cloud-demo trust gap

Status: mitigating  
Impact: high

Risk:

```text
The product promise is local-first, but the current demo runs in a Hugging Face cloud container. Confidential real documents should not be processed there.
```

Current mitigations:

- Roadmap includes local desktop/offline direction.
- UI messaging emphasizes local/no-AI/no-cloud for helper operations where applicable.
- WP45 created `LOCAL_RUNTIME_ARCHITECTURE_PLAN.md`, defining the Hugging Face demo role, local-first trust requirements and a phased local runtime path.
- WP46 added `scripts/run_local_streamlit.py` and `LOCAL_RUN.md` as the minimal local Streamlit launcher path.
- WP47 added static/monkeypatch tests for the local launcher and local-run documentation, covering localhost binding, default port, disabled Streamlit usage stats, no cloud/AI/telemetry endpoints in launcher arguments, no document content or filenames in launcher arguments, no launcher logging/temp-file/packaging behavior and clear Hugging Face/local-runtime documentation boundaries.
- WP48 added `scripts/run_windows_portable_poc.ps1`, `WINDOWS_PORTABLE_POC.md` and static tests for a minimal Windows portable proof-of-concept wrapper around the existing local launcher.
- WP49 created `DESKTOP_PACKAGING_DECISION.md` and accepted D014 in `DECISION_LOG.md`, deciding that the first MVP distribution should remain a portable Python folder, with PyInstaller one-folder as a later approved proof option, Tauri as preferred later professional shell candidate, Electron as later alternative and MSI only as future managed-deployment option.

Gaps:

- WP47 and WP48 validate launcher/documentation boundaries only; they are not full network-traffic captures.
- WP49 is a decision only; it does not build a package, installer or desktop shell.
- No full offline demonstration.
- No runtime packet/network inspection.
- No production security certification is supported.
- No signed or managed enterprise deployment proof exists.

Recommended workpackages:

- WP48B — Portable Python folder hardening proof, only if coordinator approves.
- WP49B — PyInstaller one-folder packaging proof, only if coordinator approves.
- Later network/privacy validation package — runtime network-traffic capture and temp-file inspection under controlled local conditions.

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

Gaps:

- No formal monitoring runbook.
- No standard status states.
- No automated status artifact.

Recommended workpackages:

- WP57 — Workflow status monitoring runbook and checks.

---

## R9 — Pilot/commercial overclaim risk

Status: mitigating  
Impact: medium

Risk:

```text
The product is positioned commercially beyond what the current workflow can safely support.
```

Current mitigations:

- WP50 defined a controlled pilot design and separated demo, pilot and production.
- WP51 created `ICP_AND_PRICING_HYPOTHESIS.md`, keeping ICP and pricing as hypotheses only.
- WP51 explicitly records what must not yet be sold or claimed.

Gaps:

- No external pilot has validated willingness to pay yet.
- No ICP/pricing interview evidence exists yet.
- No pilot intake or agreement process exists yet.
- No production offer should be made before local runtime, document hygiene, review and support boundaries are clearer.

Recommended workpackages:

- WP52 — Pilot intake and NDA process.
- WP53 — Controlled pilot protocol.
- WP54 — Missers/false negatives feedback loop.
- WP55 — Residual-risk report as consultancy deliverable.
