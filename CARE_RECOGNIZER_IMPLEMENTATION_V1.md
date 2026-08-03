# Zorgfilter v1 — pure recognizer implementation

Status: implemented and contract-validated; app registration remains gated  
Workpackage: `SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION`

## Result

The pure module `dutch_care_recognizers.py` implements the frozen Zorgfilter v1 contract without changing the current application.

Public API:

```python
get_dutch_care_entity_names()
get_dutch_care_recognizers(supported_language="en")
```

Implemented entity families:

- patient, client, medical-record and EPD/ECD identifiers;
- health-insurance, referral, treatment and laboratory references;
- care incident and care indication references;
- strong-context AGB codes;
- care-provider names after bounded professional roles;
- labeled care organizations and bounded care locations;
- room, bed and apartment references;
- labeled care-event dates distinct from date of birth.

## Validation result

```text
Dedicated entities: 16
Frozen positive contracts: 37/37 passed
Forbidden positive collisions: 0
Frozen negative/collision contracts: 16/16 passed
Dedicated expectations in eight-document corpus: 54/54 passed
Protected clinical phrase overlaps: 0
Full repository regression run #1854: 953 tests passed
App registration: false
Production readiness: false
```

Evidence:

- `output/validation/care_recognizer_implementation_validation.json`
- `tests/test_dutch_care_recognizers.py`
- `tests/test_care_recognizer_validation.py`

## Design choices

### Strong care labels for references

Patient-specific codes are recognized only after explicit labels such as patient number, client number, EPD/ECD number, referral number, sample number or incident number. The recognizer returns only the value span and preserves the label.

### Provider roles remain readable

A provider name is recognized only after bounded roles such as nurse, GP, treating specialist, personal carer, prescriber or incident reporter. The role and titles such as `dr.` remain readable.

### Conservative organization and location handling

Organization detection is restricted to labeled fields. Location detection is restricted to bounded phrases such as `location`, `ward`, `team` or `residential location`. The module does not infer every narrative organization as a care organization.

### AGB collision protection

AGB requires explicit AGB context and exactly eight digits. The dedicated module does not infer AGB from arbitrary numbers and passes the frozen BSN/BIG negative cases. Cross-recognizer precedence with the existing BSN recognizer remains an explicit profile-integration responsibility.

### Clinical meaning is preserved

The module does not match medication, dosage, administration times, vital signs, laboratory values, pain scores, DBC/ICD codes or role words without a person name. The eight-document corpus produced zero overlaps with protected clinical passages.

## Integration boundary

The recognizers are intentionally not imported or registered by `presidio_helpers.py` or `presidio_streamlit.py` in this package. The next workpackage centralizes profile composition so Zorg can be added without further scattering profile-specific `if` statements across the UI.

No export, Scrub Key, reinsert, runtime, dependency or cloud-processing behavior changed.

Human review remains mandatory. Passing the synthetic contract does not establish production readiness.
