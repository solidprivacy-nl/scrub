# Zorgfilter v1 — recognizer contract

Status: frozen test/specification contract; implementation not included  
Workpackage: `SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS`

## Purpose

Freeze what the dedicated Dutch care recognizer layer must and must not do before implementation begins.

The future implementation module is:

```text
dutch_care_recognizers.py
```

Frozen public API:

```python
get_dutch_care_entity_names()
get_dutch_care_recognizers(supported_language="en")
```

The supported language remains `en` because the current app invokes Presidio with `language="en"` while adding Dutch custom recognizers.

## Dedicated entity contract

The care module owns sixteen explicit entities:

```text
NL_PATIENT_NUMBER
NL_CARE_CLIENT_NUMBER
NL_MEDICAL_RECORD_NUMBER
NL_EPD_ECD_NUMBER
NL_HEALTH_INSURANCE_NUMBER
NL_REFERRAL_NUMBER
NL_TREATMENT_REFERENCE
NL_LAB_SAMPLE_NUMBER
NL_CARE_INCIDENT_NUMBER
NL_CARE_INDICATION_REFERENCE
NL_AGB_CODE
NL_CARE_PROVIDER_NAME
NL_CARE_ORGANIZATION
NL_CARE_LOCATION_REFERENCE
NL_ROOM_OR_BED_REFERENCE
NL_CARE_EVENT_DATE
```

The module does not reimplement generic `PERSON`, e-mail, address, BSN, date-of-birth, telephone or BIG recognition.

## Positive contract corpus

The versioned contract contains:

- 17 care-reference/collision cases;
- 20 contextual review cases;
- 37 positive exact-span cases in total;
- 16 negative/clinical-preservation cases.

Positive cases freeze:

- exact expected value;
- intended entity type;
- approved replace or review-selected policy;
- surrounding label or professional role that must remain readable;
- forbidden conflicting entity types where precedence matters.

## Value-only and context rules

### Administrative care references

Labels remain readable and only the patient-specific value is returned.

Examples:

```text
Patiëntnummer: PAT-2026-1148
                  ^^^^^^^^^^^^^

Medisch dossiernummer: MD-2026-4412
                         ^^^^^^^^^^^^

Verwijsnummer: VERW-2026-7711
                ^^^^^^^^^^^^^^
```

### Care-provider names

Professional role words remain readable.

```text
Rapporteur: verpleegkundige Omar El Idrissi
                            ^^^^^^^^^^^^^^^^
```

A role without a name must not produce a provider-name result.

### Organizations and locations

Only strongly labeled care organizations and bounded location phrases are in scope. Narrative organization inference remains a generic NER/profile concern.

### Event dates

Only labeled care-event dates are classified as `NL_CARE_EVENT_DATE`, including admission, discharge, report, evaluation and incident dates. Date of birth remains `NL_DATE_OF_BIRTH` and is forbidden as a care-event result.

## AGB/BSN precedence

The contract freezes the baseline collision:

```text
AGB-code: 01020304
```

Expected:

```text
NL_AGB_CODE
```

Forbidden:

```text
NL_BSN
```

Conversely, `BSN: 123456782` and an eleven-digit BIG number must never become `NL_AGB_CODE`.

AGB therefore requires strong label context and deterministic overlap handling. An arbitrary eight-digit number is not an AGB code.

## Clinical-preservation negatives

The care recognizer layer must not convert these into care identifiers:

- blood pressure such as `123/78 mmHg`;
- temperature such as `36,8 °C`;
- medication and dosage such as `Metformine 500 mg`;
- administration times such as `20:00 uur`;
- laboratory values and reference ranges;
- glucose and other decimal results;
- pain scores;
- relative time such as `over zes weken`;
- DBC and ICD clinical/declaration codes;
- a generic word such as `kamer` without a room code;
- professional role words without a person name.

Rare-case indirect identifiability remains an audit concern and is not a positive regex contract.

## Implementation requirements

The next package must:

1. implement only the frozen public API and sixteen entities;
2. return deterministic Presidio `RecognizerResult` objects with exact spans;
3. preserve context labels and role words according to the fixtures;
4. pass all 37 positive and 16 negative contracts;
5. preserve existing Dutch legal/general recognizer behavior;
6. remain Streamlit-, network-, AI-, cloud- and file-write-free;
7. avoid registering the new recognizers in the app until a later profile integration package.

## Claim boundaries

- synthetic data only;
- contract success is not production readiness;
- generic NER is outside this module;
- no UI, export, Scrub Key or reinsert change;
- human review remains mandatory.
