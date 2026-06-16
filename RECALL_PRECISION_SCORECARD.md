# Recall / Precision Scorecard — Dutch legal recall refresh

Status: refreshed after the first Dutch legal recall pattern-fix round.  
Repository: `solidprivacy-nl/scrub`.  
Scope: benchmark/documentation-only. No product code, recognizer code, UI, export, Scrub Key or reinsert behavior is changed by this document.

---

## 1. Status after Dutch legal pattern fixes

This scorecard refresh records the current evidence after:

```text
WP_DUTCH_LEGAL_RECALL_GAP_TESTS
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY
```

Current evidence:

- The Dutch legal recall gap baseline was added in `tests/test_dutch_legal_recall_gap_baseline.py`.
- The first pattern-fix round improved `candidate_scanner.py` only.
- The verified improvement is primarily review-candidate visibility: values that may have been missed by recognizers can be surfaced for human review.
- The candidate scanner remains a review/audit layer, not an automatic redaction layer.
- The verify workpackage is completed.
- Coordinator evidence confirmed GitHub Actions `Tests #1115`, `Sync to Hugging Face Space #1116` and a live Hugging Face smoke check for the verify closeout.
- The verified baseline reduces specific known gaps, but it does not support a broad product claim that all legal numbers are always detected.

Important interpretation:

```text
Improved candidate surfacing != complete automatic recognizer guarantee.
```

---

## 2. Dutch legal reference coverage

| Value | Coverage status | Evidence | Scorecard interpretation |
|---|---|---|---|
| `10598721 / UE VERZ 26-441` | verified by baseline test; improved by candidate scanner | `test_legal_reference_numbers_are_detectable`; `test_rechtspraak_like_rolnummers_are_detectable`; context-bound case-number scan | Reduced known rolnummer gap; still needs broader corpus coverage. |
| `ARN 26/4412` | verified by baseline test; improved by candidate scanner | `test_legal_reference_numbers_are_detectable`; `test_rechtspraak_like_rolnummers_are_detectable`; `CASE_NUMBER_VALUE_RE` shape | Reduced Rechtspraak-like reference gap; still needs broader variants. |
| `ZK-WOON-55091` | verified by baseline test; improved by candidate scanner | `test_legal_reference_numbers_are_detectable`; `test_client_dossier_and_zaak_numbers_are_detectable` | Reduced zaak-reference gap; candidate remains human-review controlled. |
| `CL-FAM-55201` | verified by baseline test; improved by candidate scanner | `test_legal_reference_numbers_are_detectable`; client/reference context | Reduced client-reference gap; broader client-number corpus still needed. |
| `CLNT-2026-0042` | verified by baseline test; improved by candidate scanner | `test_client_dossier_and_zaak_numbers_are_detectable` | Reduced client-number gap; still no production recall threshold. |
| `DOS-2026-778899` | verified by baseline test; improved by candidate scanner | `test_client_dossier_and_zaak_numbers_are_detectable` | Reduced dossier-number gap; broader dossier variants still need coverage. |
| `WR-KLANT-2026-7712` | verified by baseline test; improved by candidate scanner | `test_legal_reference_numbers_are_detectable`; client/customer context | Reduced internal customer-reference gap; still review-candidate level. |
| `FACT-2026-4481` | verified by baseline test; improved by candidate scanner | `test_legal_reference_numbers_are_detectable`; factuur context | Reduced invoice-reference gap; false-positive traps still need broader benchmark. |
| `CAM-MAAS-2026-0518` | verified by baseline test; improved by candidate scanner | `test_legal_reference_numbers_are_detectable`; camera context cue | Reduced camera-reference gap; still candidate/audit layer. |
| `INC-2026-0912` | verified by baseline test; improved by candidate scanner | `test_legal_reference_numbers_are_detectable`; incident context cue | Reduced incident-reference gap; broader incident corpus still needed. |
| `REP-2026-4410` | verified by baseline test; improved by candidate scanner | `test_legal_reference_numbers_are_detectable`; reparatie context cue | Reduced repair-reference gap; broader variants still needed. |
| `CLM-2026-112233` | verified by baseline test; reduced phone misclassification risk | `test_clm_reference_must_not_be_phone_number` | Specific CLM/phone confusion risk reduced; does not prove all legal references can never be classified as phone. |

Summary classification:

```text
verified by baseline test: all listed values
improved by candidate scanner: all listed legal/admin reference values at review-candidate level
still needs broader benchmark: all categories
remaining risk: no full gold-label corpus, no formal recall/precision threshold, no broad production safety claim
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

Risk update:

- The generic role-word over-masking risk is reduced for the documented synthetic examples.
- Legal role structure must remain readable.
- `arts Jansen` remains an important future benchmark case: the role word `arts` should remain readable while the name `Jansen` should be masked when identifying.
- Future sidecars should explicitly label context-preserve terms separately from person names.

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

---

## 6. Open scorecard risks

The current evidence is useful but not yet a full quantitative benchmark.

Open risks:

- No complete gold-label corpus sidecars exist yet.
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

## 7. Recommendation

No immediate `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2` should start unless new concrete misses are demonstrated.

Recommended next options:

```text
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2 — only if concrete new recall gaps are found.
WP_DOCX_HYGIENE_RECALL_FOLLOWUP — if document/export risks now dominate.
benchmark/gold-label corpus package — if quantitative recall/precision measurement is needed.
```

Most useful next benchmark step:

```text
Create or refresh gold-label sidecars for synthetic Dutch legal/care corpus documents, then run a quantitative recall/precision scorecard.
```

---

## 8. Current scorecard status

| Area | Current state | Risk status |
|---|---|---|
| Dutch legal reference baseline | Present and normal assertions after pattern fix | Reduced for listed samples |
| CLM / phone confusion | Explicit baseline assertion | Reduced for listed sample |
| Role-word preservation | Explicit baseline assertions | Reduced for listed samples |
| Over-masking role structure | Explicit baseline assertion | Reduced for listed sample |
| Review/export regression | Covered by existing contract tests | Guarded, but CI remains source of truth |
| Quantitative recall | Not available | Open |
| Quantitative precision | Not available | Open |
| Gold-label corpus sidecars | Not complete | Open |
| Production safety claim | Not supported | Must remain blocked |
