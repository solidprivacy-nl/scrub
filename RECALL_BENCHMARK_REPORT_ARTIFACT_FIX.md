# Diagnostic recall benchmark report artifact fix

Workpackage: `WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX`

Repository: `solidprivacy-nl/scrub`

Status: implemented as benchmark/tooling/tests/documentation-only.

This package cleans diagnostic runner/report mapping and counting noise before any threshold planning. It does not change product detection behavior.

---

## 1. Scope and boundaries

Scope:

- diagnostic runner/report mapping cleanup;
- duplicate prediction accounting cleanup;
- acceptable entity type taxonomy clarification in selected gold sidecars;
- benchmark-only email behavior clarification;
- tests and documentation.

Boundaries:

- no product UI change;
- no `presidio_streamlit.py` change;
- no `candidate_scanner.py` change;
- no `dutch_recognizers.py` change;
- no product recognizer change;
- no app pattern fix;
- no export/download change;
- no Scrub Key change;
- no reinsert change;
- no threshold enforcement;
- no production gate;
- no product safety claim.

---

## 2. Mapping changes made

The diagnostic benchmark mapping now treats these implementation entity types as acceptable benchmark classes:

| Implementation entity | Benchmark class | Reason |
|---|---|---|
| `NL_ADDRESS` | `ADDRESS` | Dutch address recognizer output should count for address/location gold labels where appropriate. |
| `NL_IBAN` | `IBAN` | Dutch IBAN recognizer output should count for IBAN gold labels. |
| `NL_CASE_REFERENCE` | `CASE_NUMBER` | Dutch case-reference recognizer output should count for case-number gold labels. |
| `NL_LEGAL_PARTY_NAME` | `PERSON` | Legal-party-name recognizer output can count as person-name detection in the benchmark. |
| `EMAIL_ADDRESS` | `EMAIL` | Email predictions count as email gold-label matches. |

This is benchmark/report mapping only. It does not change product recognition or app masking behavior.

---

## 3. Acceptable-type taxonomy changes

Selected care sidecars were clarified so current recognizer outputs can be measured without changing product behavior.

Changes:

- `ZORG-CL-*` care references now accept `NL_CLIENT_REFERENCE` where the gold class remains `MEDICAL_OR_CARE_REFERENCE`.
- Care department/location references such as `Rozenhof 3` / `Magnolia 2` now accept `NL_ADDRESS` where the gold class remains care/reference context.
- Person-name labels in care role contexts now accept `NL_LEGAL_PARTY_NAME` as a benchmark-compatible person-name output.

This is a benchmark taxonomy cleanup. It does not change the source text, label spans or product detection behavior.

---

## 4. Deduplication changes made

The runner now deduplicates predictions by report-accounting identity:

```text
text
entity_type
start
end
source
```

Deduplication is applied to:

- collected predictions before document comparison;
- wrong-type candidate lists;
- preserve-term hits;
- known-trap hits;
- false-positive candidate accounting.

A prediction that matched a gold label is not reported as a false-positive candidate.

This changes diagnostic counting only. It does not change product detection behavior.

---

## 5. Email behavior decision

The first artifact review showed that email labels were missed because the runner only collected custom Dutch recognizers and candidate-scanner rows.

Decision:

- Add benchmark-only email collection inside `recall_benchmark_runner.py`.
- Use a local regex to emit `EMAIL_ADDRESS` predictions for the diagnostic runner.
- Mark these predictions with source `benchmark_builtin`.

This is intentionally not a product recognizer. It only prevents the diagnostic benchmark artifact from treating synthetic `@example.test` emails as missed because the runner does not instantiate Presidio's default email recognizer.

---

## 6. Tests added/updated

Updated:

```text
tests/test_recall_benchmark_runner_minimal.py
```

New/expanded test coverage:

- `NL_ADDRESS` counts as address/location benchmark match where appropriate.
- `NL_IBAN` counts as an IBAN benchmark match.
- `NL_CASE_REFERENCE` counts as a case-number benchmark match.
- `NL_LEGAL_PARTY_NAME` counts as a person-name benchmark match.
- `EMAIL_ADDRESS` counts as an email benchmark match.
- `NL_CLIENT_REFERENCE` can be accepted for care-reference taxonomy when listed in `acceptable_entity_types`.
- Duplicate predictions are counted once in report accounting.
- Matched predictions are not reported as false-positive candidates.
- Benchmark-only email predictions are emitted without trailing sentence punctuation.
- Report metadata remains diagnostic-only through existing report artifact tests.

---

## 7. Expected report impact

Expected qualitative effect on the next artifact:

- wrong-type count should be lower or better explained;
- false-positive candidate count should be lower or better explained;
- address, IBAN, case-reference and legal-party-name mapping cases should no longer inflate missed/wrong-type counts;
- synthetic email labels should be matched by benchmark-only email predictions;
- duplicate predictions should no longer inflate wrong-type, known-trap, preserve-term or false-positive accounting.

No hard target is set. The report remains diagnostic only.

---

## 8. Remaining noisy metrics

Possible remaining noise after this cleanup:

- genuinely unsupported person-name variants;
- care room references such as `C-118` / `B-214` that may still require a benchmark taxonomy or candidate-scanner decision;
- care device/medication references not currently surfaced by recognizers/helpers;
- overlap matches remain diagnostic and should not hide missed required labels in future threshold planning;
- corpus remains synthetic and small.

---

## 9. Threshold planning readiness

Threshold planning should not start until the cleaned artifact is generated and reviewed.

Recommended next step after Actions/artifact verification:

```text
WP_RECALL_BENCHMARK_REPORT_REVIEW_2
```

If the cleaned artifact is substantially less noisy and structurally sound, then consider:

```text
WP_RECALL_BENCHMARK_THRESHOLDS_PLAN
```

Threshold planning must still be planning-only and must not create a production gate without a separate approved package.

---

## 10. Non-claims

This cleanup is diagnostic only.

This cleanup does not prove production safety.

This cleanup does not define accepted thresholds.

This cleanup does not create a production gate.

This cleanup does not support the claim that all legal/care identifiers are always detected.
