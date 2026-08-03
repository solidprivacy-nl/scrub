# Recognition profile configuration

Status: pure configuration implemented; live UI and analyzer integration remain gated  
Workpackage: `SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR`

## Purpose

Centralize recognition-profile behavior before adding the visible Zorg profile to the current Streamlit application.

The previous app keeps profile labels, thresholds and entity selection in several `if` branches. Four profiles would make that structure fragile. `recognition_profiles.py` now provides one pure source of truth without changing current live behavior.

## Defined profiles

| Profile | Internal value | Threshold | Entity groups | Candidate/examples |
| --- | --- | ---: | --- | --- |
| Algemeen Nederlands | `Dutch / EU` | 0.35 | base + Dutch general | none |
| Zorg | `Dutch Care Strict` | 0.30 | base + Dutch general + Dutch care | care |
| Juridisch | `Dutch Legal Strict` | 0.30 | base + Dutch general + Dutch legal | legal |
| Internationaal | `General / International` | 0.35 | all supported | none |

## Explicit UI orders

Current visible Streamlit order remains unchanged:

```text
Juridische controle — streng
Algemene Nederlandse controle
Algemene internationale controle
```

Future Streamlit order after the dedicated integration package:

```text
Zorgcontrole — streng
Juridische controle — streng
Algemene Nederlandse controle
Algemene internationale controle
```

Final desktop workspace order:

```text
Algemeen NL | Zorg | Juridisch | Internationaal
```

The current package does not expose the fourth profile yet.

## Entity composition

Profile entity resolution preserves the ordering supplied by the active analyzer engine.

- General Dutch: base entities plus Dutch general entities.
- Care: base entities plus Dutch general and dedicated care entities.
- Legal: base entities plus Dutch general and legal entities.
- International: all supported entities.

Care and Legal are isolated by default. Adding Zorg does not silently activate legal case/reference recognition, and Legal does not automatically activate the dedicated care entities.

## Care policy composition

The configuration maps dedicated care entities to the approved policy contract:

- patient/client identity and administrative references: replace;
- provider identity, BIG/AGB, organization, location, room/bed and care-event dates: review-selected;
- generic `ORGANIZATION`, `LOCATION` and `DATE_TIME` in Care: review-selected;
- generic patient/relative `PERSON`: replace.

Other profiles keep their current replace-oriented default in this pure configuration layer.

## Deterministic exact-span precedence

The Care profile may receive overlapping results from the existing broad recognizers and the new dedicated care recognizers. The configuration resolves only exact same-span collisions.

Examples:

```text
NL_AGB_CODE                  supersedes NL_BSN
NL_PATIENT_NUMBER            supersedes NL_HEALTHCARE_REFERENCE
NL_CARE_CLIENT_NUMBER        supersedes NL_CLIENT_REFERENCE / NL_CLIENT_NUMBER
NL_MEDICAL_RECORD_NUMBER     supersedes NL_DOSSIER_NUMBER / NL_HEALTHCARE_REFERENCE
NL_CARE_PROVIDER_NAME        supersedes PERSON
NL_CARE_ORGANIZATION         supersedes ORGANIZATION
NL_CARE_LOCATION_REFERENCE   supersedes LOCATION
NL_CARE_EVENT_DATE           supersedes DATE_TIME
```

Partial overlaps are deliberately preserved for later review and regression evidence rather than silently discarded.

## Integration boundary

This package does not:

- import the profile model into `presidio_streamlit.py`;
- register `dutch_care_recognizers.py` in `presidio_helpers.py`;
- alter the visible selector;
- change live thresholds or entity defaults;
- change review, export, Scrub Key or reinsert semantics.

The next package performs the current UI/analyzer integration sequentially and requires Hugging Face sync plus live app verification.

Human review remains mandatory. The configuration is not a production-readiness claim.
