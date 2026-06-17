# Recall / Precision Scorecard — Dutch legal recall refresh

Status: refreshed after the first Dutch legal recall pattern-fix round and synthetic gold-label corpus seed.  
Repository: `solidprivacy-nl/scrub`.  
Scope: benchmark/documentation-only. No product code, recognizer code, UI, export, Scrub Key or reinsert behavior is changed by this document.

---

## 1. Status after Dutch legal pattern fixes

This scorecard refresh records the current evidence after:

```text
WP_DUTCH_LEGAL_RECALL_GAP_TESTS
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY
WP_RECALL_SCORECARD_REFRESH
WP_RECALL_GOLD_LABEL_CORPUS_SEED
```

Current evidence:

- The Dutch legal recall gap baseline was added in `tests/test_dutch_legal_recall_gap_baseline.py`.
- The first pattern-fix round improved `candidate_scanner.py` only.
- The verified improvement is primarily review-candidate visibility: values that may have been missed by recognizers can be surfaced for human review.
- The candidate scanner remains a review/audit layer, not an automatic redaction layer.
- The verify workpackage is completed.
- Coordinator evidence confirmed GitHub Actions `Tests #1115`, `Sync to Hugging Face Space #1116` and a live Hugging Face smoke check for the verify closeout.
- A small synthetic gold-label corpus seed has been added for future quantitative benchmarking.
- Quantitative recall/precision is still pending a runner and broader gold-label corpus.
- The verified baseline reduces specific known gaps, but it does not support a broad product claim that all legal numbers are always detected.

Important interpretation:

```text
Improved candidate surfacing != complete automatic recognizer guarantee.
Gold-label seed != quantitative score until a runner compares predictions with sidecars.
```

---

## 2. Dutch legal reference coverage

| Value | Coverage status | Evidence | Scorecard interpretation |
|---|---|---|---|
| `10598721 / UE VERZ 26-441` | verified by baseline test; improved by candidate scanner; gold sidecar seed | `test_legal_reference_numbers_are_detectable`; `test_rechtspraak_like_rolnummers_are_detectable`; `legal_reference_seed_001.gold.json` | Reduced known rolnummer gap; now ready for runner measurement. |
| `ARN 26/4412` | verified by baseline test; improved by candidate scanner; gold sidecar seed | `test_legal_reference_numbers_are_detectable`; `test_rechtspraak_like_rolnummers_are_detectable`; `CASE_NUMBER_VALUE_RE` shape | Reduced Rechtspraak-like reference gap; still needs broader variants. |
| `ZK-WOON-55091` | verified by baseline test; improved by candidate scanner; gold sidecar seed | `test_legal_reference_numbers_are_detectable`; `test_client_dossier_and_zaak_numbers_are_detectable` | Reduced zaak-reference gap; candidate remains human-review controlled. |
| `CL-FAM-55201` | verified by baseline test; improved by candidate scanner; gold sidecar seed | `test_legal_reference_numbers_are_detectable`; client/reference context | Reduced client-reference gap; broader client-number corpus still needed. |
| `CLNT-2026-0042` | verified by baseline test; improved by candidate scanner; gold sidecar seed | `test_client_dossier_and_zaak_numbers_are_detectable` | Reduced client-number gap; still no production recall threshold. |
| `DOS-2026-778899` | verified by baseline test; improved by candidate scanner; gold sidecar seed | `test_client_dossier_and_zaak_numbers_are_detectable` | Reduced dossier-number gap; broader dossier variants still need coverage. |
| `WR-KLANT-2026-7712` | verified by baseline test; improved by candidate scanner; gold sidecar seed | `test_legal_reference_numbers_are_detectable`; client/customer context | Reduced internal customer-reference gap; still review-candidate level. |
| `FACT-2026-4481` | verified by baseline test; improved by candidate scanner; gold sidecar seed | `test_legal_reference_numbers_are_detectable`; factuur context | Reduced invoice-reference gap; false-positive traps still need broader benchmark. |
| `CAM-MAAS-2026-0518` | verified by baseline test; improved by candidate scanner; gold sidecar seed | `test_legal_reference_numbers_are_detectable`; camera context cue | Reduced camera-reference gap; still candidate/audit layer. |
| `INC-2026-0912` | verified by baseline test; improved by candidate scanner; gold sidecar seed | `test_legal_reference_numbers_are_detectable`; incident context cue | Reduced incident-reference gap; broader incident corpus still needed. |
| `REP-2026-4410` | verified by baseline test; improved by candidate scanner; gold sidecar seed | `test_legal_reference_numbers_are_detectable`; reparatie context cue | Reduced repair-reference gap; broader variants still needed. |
| `CLM-2026-112233` | verified by baseline test; reduced phone misclassification risk; gold sidecar seed | `test_clm_reference_must_not_be_phone_number` | Specific CLM/phone confusion risk reduced; does not prove all legal references can never be classified as phone. |

Summary classification:

```text
verified by baseline test: all listed values
improved by candidate scanner: all listed legal/admin reference values at review-candidate level
gold-label corpus seed: all listed values included in legal reference sidecar
still needs runner: all categories
remaining risk: no formal recall/precision threshold, no broad production safety claim
```

---

## 3. CLM / phone-number risk

The baseline explicitly checks:

```text
CLM-2026-112233 should be detected as a legal reference value
CLM-2026-112233 should not be returned with an entity type containing PHONE
```

Risk update:

- The specific observed `CLM-2026-112233` phone-number confusion is now covered by a normal baseline assertion.
- `CLM-2026-112233` is also represented in `corpus/legal/legal_reference_seed_001.gold.json` as a `CLAIM_NUMBER` with notes that it must not be `PHONE_NUMBER`.
- This lowers the known CLM/phone misclassification risk for the documented sample.
- It does not prove that every future legal reference that resembles a phone number will always be classified correctly.
- Future gold-label sidecars should include more claim-code variants, including near-phone, near-date and hyphenated formats.

---

## 4. Role words / over-masking

The baseline protects these role/context words from being treated as person values on their own:

```text
slachtoffer
arts
getuige
eiser
verweerder
minderjarige
```

Current test evidence:

- `test_role_words_alone_are_not_detected_as_person_values`
- `test_overmasking_does_not_remove_legal_role_structure`
- `corpus/legal/legal_role_preservation_seed_001.gold.json`
- `corpus/care/care_reference_seed_001.gold.json`

Risk update:

- The generic role-word over-masking risk is reduced for the documented synthetic examples.
- Legal role structure must remain readable.
- `arts Jansen`, `getuige Fatima El Amrani` and `de minderjarige Sami El Amrani` are now represented in the legal role-preservation seed.
- Future sidecars should continue to label context-preserve terms separately from person names.

---

## 5. Review/export regression boundaries

The Dutch legal recall changes should not silently alter review/export/Scrub Key/reinsert behavior.

Existing boundary tests that remain relevant:

```text
tests/test_review_table_collapsible_contract.py
tests/test_side_by_side_review_ui_patch.py
tests/test_side_by_side_review_consolidation_dutch_sample.py
```

Coverage summary:

- `replacement_editor` remains the review table source of truth and fallback.
- Download labels and export/download surfaces remain contract-tested.
- Side-by-side review remains report/visual only.
- Markers remain visual-only.
- No Scrub Key writes are introduced by review UI tests.
- No reinsert behavior change is introduced by the Dutch legal recall refresh.
- The gold-label corpus seed does not execute the app or analyzer.

---

## 6. Gold-label corpus seed

Added seed files:

```text
corpus/README.md
corpus/legal/legal_reference_seed_001.txt
corpus/legal/legal_reference_seed_001.gold.json
corpus/legal/legal_role_preservation_seed_001.txt
corpus/legal/legal_role_preservation_seed_001.gold.json
corpus/care/care_reference_seed_001.txt
corpus/care/care_reference_seed_001.gold.json
tests/test_recall_gold_label_corpus_seed.py
```

The sidecars provide:

- `labels` with exact zero-based offsets;
- `preserve_terms` for legal/care role/context terms;
- `known_traps` for legal articles, money amounts, role words and care-location ambiguity;
- `synthetic: true` for every document;
- `.example.test` email domains only.

This is not yet a quantitative score. A future runner must compare analyzer/helper output against these gold labels.

---

## 7. Open scorecard risks

The current evidence is useful but not yet a full quantitative benchmark.

Open risks:

- The corpus seed is intentionally small.
- No formal recall threshold exists.
- No formal precision threshold exists.
- No production-blocking benchmark gate exists.
- Helper-level candidate surfacing is not the same as automatic recognition.
- Candidate rows require human review and are not automatically applied.
- Broader legal-reference variants are not exhausted.
- False positives around legal article references, dates, money amounts and generic document references still need broader corpus coverage.
- DOCX metadata, comments, tracked changes, headers and footers remain separate document-hygiene risks.
- The app must not claim: `alle juridische nummers worden altijd herkend`.

Allowed wording:

```text
Nederlandse juridische referenties worden beter als review-kandidaat zichtbaar gemaakt wanneer automatische herkenning ze mist.
```

Disallowed wording:

```text
Alle juridische nummers worden altijd herkend.
```

---

## 8. Recommendation

No immediate `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2` should start unless new concrete misses are demonstrated.

Recommended next options:

```text
WP_RECALL_BENCHMARK_RUNNER_MINIMAL — compare sidecars with analyzer/helper output.
WP_RECALL_GOLD_LABEL_CORPUS_EXPAND — add more synthetic legal/care documents first.
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2 — only if concrete new recall gaps are found.
WP_DOCX_HYGIENE_RECALL_FOLLOWUP — if document/export risks now dominate.
```

Most useful next benchmark step:

```text
Build a minimal diagnostic runner or expand the gold-label corpus before more pattern work.
```

---

## 9. Current scorecard status

| Area | Current state | Risk status |
|---|---|---|
| Dutch legal reference baseline | Present and normal assertions after pattern fix | Reduced for listed samples |
| CLM / phone confusion | Explicit baseline assertion plus gold sidecar label | Reduced for listed sample |
| Role-word preservation | Explicit baseline assertions plus legal/care preserve terms | Reduced for listed samples |
| Over-masking role structure | Explicit baseline assertion and role seed | Reduced for listed sample |
| Review/export regression | Covered by existing contract tests | Guarded, but CI remains source of truth |
| Gold-label corpus sidecars | Small synthetic seed added | Improved measurability |
| Quantitative recall | Not available until runner exists | Open |
| Quantitative precision | Not available until runner exists | Open |
| Production safety claim | Not supported | Must remain blocked |
