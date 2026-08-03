# Zorgfilter v1 — policy, corpus and implementation plan

Status: approved direction; foundation implementation in progress  
Repository: `solidprivacy-nl/scrub`  
Approved: 2026-08-03 Europe/Amsterdam

## 1. Product objective

Add an explicit Dutch care profile alongside the existing general Dutch, legal and international profiles.

The care profile removes or flags patient-, client-, relative-, provider- and care-trajectory identifiers while preserving clinical meaning.

Core rule:

```text
Replace identity and patient-specific administrative references.
Review contextual provider, location and event identifiers.
Preserve diagnosis, medication, dosage, laboratory values, observations and care meaning.
Warn about rare-case re-identification without blindly masking clinical content.
```

The profile is not a generic medical-term filter and must not make a document clinically unreadable.

## 2. Approved policy

### Replace by default

- patient/client names and names of relatives, representatives or informal carers;
- BSN and date of birth;
- address, postcode, e-mail and telephone number;
- patient number, care client number, EPD/ECD number and medical-record number;
- personal health-insurance number;
- patient-specific referral, treatment, laboratory-sample, care-incident and indication references.

### Review and select by default

- care-provider names;
- BIG numbers and AGB codes;
- care organizations, departments, teams and locations;
- room or bed references;
- exact admission, discharge, appointment, treatment and report dates other than date of birth.

These values are visible in review and selected by default, but the user can preserve them when professional context requires it.

### Preserve by default

- diagnosis and symptoms;
- medication names, dosage and administration schedules;
- laboratory results, units and reference values;
- observations, vital signs, allergies and functional status;
- treatment, procedure, care goals and clinical recommendations;
- generic clinical and professional role words;
- clinical classifications and codes unless evidence proves that a code is patient-specific.

### Audit only

Rare combinations of diagnosis, location, date, age or unusual case detail may still be indirectly identifying. Version 1 records this as residual-risk evidence and an audit warning. It does not blindly remove clinical content.

## 3. First supported document families

1. daily nursing or care report;
2. care plan and evaluation;
3. nursing transfer;
4. medical specialist discharge letter;
5. GP referral or consultation letter;
6. medication overview or administration list;
7. laboratory report;
8. MIC/MIM/VIM care-incident report.

Later extensions may cover mental-health progress notes, district-nursing intake, rehabilitation, CIZ/Wlz/Wmo documentation, multidisciplinary consultation, wound care, maternity care and youth care.

## 4. Architecture direction

Keep care-specific behavior in separate pure modules before UI integration:

```text
care_profile_policy.py
care_test_examples.py
care_profile_baseline.py
care_reference_taxonomy.py             # later recognizer package
dutch_care_recognizers.py              # later recognizer package
recognition_profiles.py                 # later central profile configuration
```

Do not continue expanding the legal taxonomy with all care behavior. The existing broad `NL_HEALTHCARE_REFERENCE` category must be assessed and split because it currently combines values with different privacy policies, including patient numbers and DBC-like codes.

## 5. Current Streamlit interface target

After the policy, corpus, baseline and recognizer packages pass, the current profile selector becomes:

```text
Zorgcontrole — streng
Juridische controle — streng
Algemene Nederlandse controle
Algemene internationale controle
```

Care-profile behavior:

```text
threshold: evidence-based, initial candidate 0.30
entities: general Dutch + care-specific
legal-only entities: not enabled by default
care candidate scan: enabled
synthetic care examples: available
profile explanation: visible
```

No export, Scrub Key or reinsert semantics change merely because a care profile is added.

## 6. Final desktop interface target

The future document workspace shows a compact, explicit profile choice:

```text
[ Algemeen NL ] [ Zorg ] [ Juridisch ] [ Internationaal ]
```

After a document opens, the toolbar shows `Profiel: Zorg` with a small change action. The full explanation and advanced entity selection remain under Options. Profile switching must never happen silently.

## 7. Test strategy

### Corpus contracts

Each fully synthetic document must define:

- exact values expected to be replaced;
- exact values expected to be shown for review;
- exact clinical values and phrases expected to be preserved;
- ambiguity traps and negative examples;
- sector and document type metadata.

### Current-engine baseline

Run the existing recognizer layer against the care corpus before adding care recognizers. Record:

- detected and missed expected values;
- wrong entity classification;
- partial-span matches;
- clinical over-masking;
- role-word over-masking.

The baseline is evidence, not a production gate.

### Recognizer validation

Measure at least:

- recall by care entity;
- precision by care entity;
- exact-span accuracy;
- false positives and false negatives;
- preserved clinical phrases;
- profile isolation across all four profiles.

### End-to-end validation

For TXT and DOCX:

```text
import -> detect -> review -> replace -> Scrub Key -> reinsert -> audit
```

Verify document binding, context preservation, header/footer behavior and fail-closed wrong-key handling.

## 8. Sequential workpackages

1. `SCRUB-WP_CARE_PROFILE_V1_POLICY_AND_CORPUS_FOUNDATION`
2. `SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE`
3. `SCRUB-WP_CARE_PROFILE_GAP_TRIAGE`
4. `SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS`
5. `SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION`
6. `SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR`
7. `SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION`
8. `SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX`
9. `SCRUB-WP_CARE_PROFILE_APP_VERIFY`
10. `SCRUB-WP_CARE_PROFILE_DESKTOP_UX_CONTRACT`

UI integration remains sequential and must not run in parallel with other edits to `presidio_streamlit.py` or the same review/export flow.

## 9. Safety and claim boundaries

- synthetic data only;
- human review remains required;
- no claim that all medical or care identifiers are always found;
- no automatic cloud document processing;
- no blind masking of clinical meaning;
- no production-readiness claim from corpus or benchmark results;
- no weakening of Scrub Key, export, audit or review controls.
