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
- WP_DUTCH_LEGAL_RECALL_GAP_TESTS added tests-only baselines for known Dutch legal recall gaps.
- WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES improved the review-candidate layer for selected Dutch legal reference values.
- WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY confirmed the implementation is scope-contained and coordinator evidence confirms Actions/HF/app verification for the closeout commit.
- WP_RECALL_SCORECARD_REFRESH records the post-fix recall/precision status, evidence level and remaining benchmark gaps in `RECALL_PRECISION_SCORECARD.md`.
- WP_RECALL_GOLD_LABEL_CORPUS_SEED added the first synthetic source/sidecar corpus seed with exact gold-label offsets for future quantitative measurement.
- WP_RECALL_GOLD_LABEL_CORPUS_EXPAND expanded the synthetic gold-label corpus to cover more legal/care reference values, false-positive traps and role-preservation cases.
- WP_RECALL_BENCHMARK_RUNNER_MINIMAL adds a diagnostic runner that compares analyzer/helper predictions against the expanded gold-label corpus.
- WP_RECALL_BENCHMARK_REPORT_ARTIFACT adds a GitHub Actions artifact workflow so diagnostic runner output becomes visible as JSON and Markdown.
- WP_RECALL_BENCHMARK_REPORT_REVIEW reviewed the first artifact output and identified that raw counts were not ready for threshold planning because of mapping/taxonomy/deduplication noise.
- WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX cleans diagnostic mapping/counting noise for `NL_ADDRESS`, `NL_IBAN`, `NL_CASE_REFERENCE`, `NL_LEGAL_PARTY_NAME`, care `ZORG-CL-*` references, selected care-location references, duplicate prediction accounting and benchmark-only email behavior.
- WP_RECALL_BENCHMARK_REPORT_REVIEW_2 reviewed the cleaned artifact and confirmed the output is substantially less noisy: missed required 34 -> 18, wrong-type 11 -> 1 and false-positive candidates 8 -> 1.

Gaps:

- No accepted production recall/precision threshold exists.
- No production-blocking benchmark gate exists.
- No production safety claim is supported.
- Dutch legal and care reference gaps are now more measurable and visible, but this does not prove complete automatic classification for all reference types.
- Cleaned artifact review still shows 18 missed required labels, concentrated in person names, care room/location references and one client-number example.
- Remaining one false-positive candidate is a nested `NL_BSN` hit inside a phone-like value.
- Runner/report output remains diagnostic until thresholds and governance are separately approved.

Recommended workpackages:

- Next approved package — `WP_RECALL_BENCHMARK_THRESHOLDS_PLAN`, planning-only without enforcement.
- Later approved packages if needed — person-name coverage review, care-location/reference candidate planning and client-reference coverage review.
- Later gated package — accepted thresholds and regression gate only after planning approval.
- Later approved package only if cleaned metrics expose narrow pattern gaps — second narrow Dutch legal pattern round.

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
- WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION integrated synchronized scrolling in the side-by-side renderer.
- WP_REVIEW_SURFACE_CONTROL_CLEANUP made synchronized scrolling default without exposing a visible sync-checkbox and kept markers default-on.
- WP_REVIEW_SURFACE_DUPLICATE_HEADING_CLEANUP removed a duplicate review heading from the central side-by-side review surface.
- WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY closed out the promoted collapsible review table.
- WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP removed temporary candidate/helper artifacts after verified promotion.

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

## R8 — Workflow status and benchmark evidence visibility

Status: mitigating  
Impact: medium

Risk:

```text
Development slows or evidence becomes ambiguous because workers wait for screenshots, connector status can be incomplete, and diagnostic outputs are hard to inspect.
```

Current mitigations:

- Coordinator supplies screenshots/evidence when connector permissions cannot show the relevant run.
- Workpackages record Actions/sync status.
- `STATUS_MONITORING_RUNBOOK.md` exists and defines standard status states plus the expected Actions/Hugging Face verification order.
- Workers are instructed to use connector status tools first, then ask for coordinator evidence only when connector lookup is incomplete.
- WP_RECALL_BENCHMARK_REPORT_ARTIFACT adds a CI-visible diagnostic recall benchmark artifact workflow for benchmark evidence.
- WP_RECALL_BENCHMARK_REPORT_REVIEW reviewed the first uploaded artifact files and recorded findings in `RECALL_BENCHMARK_REPORT_REVIEW.md`.
- WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX cleaned report mapping/counting noise.
- WP_RECALL_BENCHMARK_REPORT_REVIEW_2 reviewed the cleaned artifact files and recorded threshold-planning readiness.

Gaps:

- Connector workflow-run lookup can still be incomplete for some push-triggered runs.
- No generalized automated status artifact exists yet.
- Future threshold planning must remain planning-only until separate gate approval.

Recommended workpackages:

- Next approved benchmark package — `WP_RECALL_BENCHMARK_THRESHOLDS_PLAN` as planning-only.
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
- WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY statically confirmed that the implementation is context-bound, value-only and limited to the candidate helper/test layer.
- Coordinator evidence confirms `Tests #1115`, `Sync to Hugging Face Space #1116` and app smoke verification are green for the verify closeout.
- `RECALL_PRECISION_SCORECARD.md` records current coverage status, CLM/phone risk reduction, role-word preservation evidence and open benchmark gaps.
- WP_RECALL_GOLD_LABEL_CORPUS_SEED added synthetic legal and care gold-label source/sidecar files, including role/name preservation cases and care-reference examples.
- WP_RECALL_GOLD_LABEL_CORPUS_EXPAND added legal false-positive traps, legal mixed identifiers, care role-preservation examples and care mixed identifiers.
- WP_RECALL_BENCHMARK_RUNNER_MINIMAL adds diagnostic reporting for missed labels, wrong types, false-positive candidates, preserve-term hits and known-trap hits.
- WP_RECALL_BENCHMARK_REPORT_ARTIFACT makes the diagnostic report visible as a JSON/Markdown CI artifact.
- WP_RECALL_BENCHMARK_REPORT_REVIEW reviewed the first artifact and confirmed `preserve_term_hit_count = 0`, but also found mapping/taxonomy/deduplication noise.
- WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX added runner/report mapping cleanup and duplicate accounting cleanup without changing product recognition.
- WP_RECALL_BENCHMARK_REPORT_REVIEW_2 confirmed the cleaned artifact is substantially less noisy and has `preserve_term_hit_count = 0`.

Gaps:

- This first pattern round improves review candidates; it does not prove all recognizer/entity classifications are complete.
- Broader production recall/precision thresholds remain future work.
- The corpus is improved but remains synthetic and not exhaustive.
- Role-word preservation still needs continued regression coverage as recognizers evolve.
- Cleaned artifact still reports 14 missed person labels, 3 missed care room/location references and 1 missed/wrong client number.
- Diagnostic runner/report output does not yet create a production gate.

Recommended workpackages:

- No immediate extra pattern round is recommended based on the cleaned artifact review.
- Next approved package — `WP_RECALL_BENCHMARK_THRESHOLDS_PLAN`, planning-only before any threshold/gate implementation.
- Later follow-ups if planning confirms need — person-name coverage review, care-location candidate planning and client-reference coverage review.
- If future cleaned report output exposes narrow detection gaps, use a separately approved `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2`.
