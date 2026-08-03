"""Versioned synthetic recognizer contracts for Zorgfilter v1.

This module is specification data only. It does not implement or import the
future `dutch_care_recognizers` module.
"""

from __future__ import annotations

from typing import Any, Dict, Tuple

from care_profile_policy import (
    ACTION_REPLACE,
    ACTION_REVIEW_SELECTED,
    policy_for_entity,
)


CARE_RECOGNIZER_CONTRACT_SCHEMA_VERSION = "1.0"
CARE_RECOGNIZER_SUPPORTED_LANGUAGE = "en"
CARE_RECOGNIZER_MODULE = "dutch_care_recognizers"
CARE_RECOGNIZER_PUBLIC_API = (
    "get_dutch_care_entity_names",
    "get_dutch_care_recognizers",
)

CARE_RECOGNIZER_ENTITY_NAMES: Tuple[str, ...] = (
    "NL_PATIENT_NUMBER",
    "NL_CARE_CLIENT_NUMBER",
    "NL_MEDICAL_RECORD_NUMBER",
    "NL_EPD_ECD_NUMBER",
    "NL_HEALTH_INSURANCE_NUMBER",
    "NL_REFERRAL_NUMBER",
    "NL_TREATMENT_REFERENCE",
    "NL_LAB_SAMPLE_NUMBER",
    "NL_CARE_INCIDENT_NUMBER",
    "NL_CARE_INDICATION_REFERENCE",
    "NL_AGB_CODE",
    "NL_CARE_PROVIDER_NAME",
    "NL_CARE_ORGANIZATION",
    "NL_CARE_LOCATION_REFERENCE",
    "NL_ROOM_OR_BED_REFERENCE",
    "NL_CARE_EVENT_DATE",
)


def _positive(
    case_id: str,
    text: str,
    expected_value: str,
    entity_type: str,
    family: str,
    preserved_text: Tuple[str, ...],
    forbidden_entities: Tuple[str, ...] = (),
) -> Dict[str, Any]:
    rule = policy_for_entity(entity_type)
    if rule is None:
        raise ValueError(f"Missing care policy for {entity_type}")
    return {
        "id": case_id,
        "text": text,
        "expected_value": expected_value,
        "entity_type": entity_type,
        "policy_action": rule.action,
        "family": family,
        "preserved_text": list(preserved_text),
        "forbidden_entities": list(forbidden_entities),
    }


REFERENCE_POSITIVE_CASES: Tuple[Dict[str, Any], ...] = (
    _positive(
        "patient_number_alphanumeric",
        "Patiëntnummer: PAT-2026-1148.",
        "PAT-2026-1148",
        "NL_PATIENT_NUMBER",
        "care_reference",
        ("Patiëntnummer",),
    ),
    _positive(
        "patient_number_numeric_date_shaped",
        "Patientnummer: 20260115.",
        "20260115",
        "NL_PATIENT_NUMBER",
        "care_reference",
        ("Patientnummer",),
        ("NL_CARE_EVENT_DATE",),
    ),
    _positive(
        "care_client_number",
        "Cliëntnummer: CL-ZORG-7712.",
        "CL-ZORG-7712",
        "NL_CARE_CLIENT_NUMBER",
        "care_reference",
        ("Cliëntnummer",),
    ),
    _positive(
        "medical_record_number",
        "Medisch dossiernummer: MD-2026-4412.",
        "MD-2026-4412",
        "NL_MEDICAL_RECORD_NUMBER",
        "care_reference",
        ("Medisch dossiernummer",),
    ),
    _positive(
        "epd_number",
        "EPD-nummer: EPD-2026-5501.",
        "EPD-2026-5501",
        "NL_EPD_ECD_NUMBER",
        "care_reference",
        ("EPD-nummer",),
    ),
    _positive(
        "ecd_number",
        "ECD-nummer: ECD-889144.",
        "ECD-889144",
        "NL_EPD_ECD_NUMBER",
        "care_reference",
        ("ECD-nummer",),
    ),
    _positive(
        "health_insurance_number",
        "Verzekerdennummer: VERZ-88441122.",
        "VERZ-88441122",
        "NL_HEALTH_INSURANCE_NUMBER",
        "care_reference",
        ("Verzekerdennummer",),
    ),
    _positive(
        "referral_number",
        "Verwijsnummer: VERW-2026-7711.",
        "VERW-2026-7711",
        "NL_REFERRAL_NUMBER",
        "care_reference",
        ("Verwijsnummer",),
    ),
    _positive(
        "treatment_number",
        "Behandelnummer: BEH-2026-1188.",
        "BEH-2026-1188",
        "NL_TREATMENT_REFERENCE",
        "care_reference",
        ("Behandelnummer",),
    ),
    _positive(
        "care_trajectory_number",
        "Zorgtrajectnummer: ZORG-2026-5512.",
        "ZORG-2026-5512",
        "NL_TREATMENT_REFERENCE",
        "care_reference",
        ("Zorgtrajectnummer",),
    ),
    _positive(
        "lab_sample_number",
        "Monsternummer: LAB-2026-4412.",
        "LAB-2026-4412",
        "NL_LAB_SAMPLE_NUMBER",
        "care_reference",
        ("Monsternummer",),
    ),
    _positive(
        "lab_accession_number",
        "Accessienummer: ACC-2026-1188.",
        "ACC-2026-1188",
        "NL_LAB_SAMPLE_NUMBER",
        "care_reference",
        ("Accessienummer",),
    ),
    _positive(
        "mic_incident_number",
        "MIC-nummer: MIC-2026-0912.",
        "MIC-2026-0912",
        "NL_CARE_INCIDENT_NUMBER",
        "care_reference",
        ("MIC-nummer",),
    ),
    _positive(
        "vim_incident_number",
        "VIM-nummer: VIM-2026-3301.",
        "VIM-2026-3301",
        "NL_CARE_INCIDENT_NUMBER",
        "care_reference",
        ("VIM-nummer",),
    ),
    _positive(
        "ciz_reference",
        "CIZ-nummer: CIZ-2026-5512.",
        "CIZ-2026-5512",
        "NL_CARE_INDICATION_REFERENCE",
        "care_reference",
        ("CIZ-nummer",),
    ),
    _positive(
        "wlz_reference",
        "Wlz-indicatie: WLZ-2026-1188.",
        "WLZ-2026-1188",
        "NL_CARE_INDICATION_REFERENCE",
        "care_reference",
        ("Wlz-indicatie",),
    ),
    _positive(
        "agb_code",
        "AGB-code: 01020304.",
        "01020304",
        "NL_AGB_CODE",
        "collision_guard",
        ("AGB-code",),
        ("NL_BSN",),
    ),
)


CONTEXTUAL_REVIEW_POSITIVE_CASES: Tuple[Dict[str, Any], ...] = (
    _positive(
        "provider_nurse_reporter",
        "Rapporteur: verpleegkundige Omar El Idrissi.",
        "Omar El Idrissi",
        "NL_CARE_PROVIDER_NAME",
        "contextual_review",
        ("Rapporteur", "verpleegkundige"),
    ),
    _positive(
        "provider_specialist",
        "Behandelend internist: dr. Jeroen de Bruin.",
        "Jeroen de Bruin",
        "NL_CARE_PROVIDER_NAME",
        "contextual_review",
        ("Behandelend internist", "dr."),
    ),
    _positive(
        "provider_gp",
        "Huisarts: dr. Miriam Vos, AGB-code 01020304.",
        "Miriam Vos",
        "NL_CARE_PROVIDER_NAME",
        "contextual_review",
        ("Huisarts", "dr.", "AGB-code"),
    ),
    _positive(
        "provider_personal_carer",
        "Persoonlijk begeleider: Sanne de Wit.",
        "Sanne de Wit",
        "NL_CARE_PROVIDER_NAME",
        "contextual_review",
        ("Persoonlijk begeleider",),
    ),
    _positive(
        "organization_care_group",
        "Zorgorganisatie: Zorggroep Kompas.",
        "Zorggroep Kompas",
        "NL_CARE_ORGANIZATION",
        "contextual_review",
        ("Zorgorganisatie",),
    ),
    _positive(
        "organization_hospital",
        "Ziekenhuis: Medisch Centrum Rivierenland.",
        "Medisch Centrum Rivierenland",
        "NL_CARE_ORGANIZATION",
        "contextual_review",
        ("Ziekenhuis",),
    ),
    _positive(
        "organization_pharmacy",
        "Apotheek: Apotheek Waterlinie.",
        "Apotheek Waterlinie",
        "NL_CARE_ORGANIZATION",
        "contextual_review",
        ("Apotheek",),
    ),
    _positive(
        "organization_laboratory",
        "Laboratorium: Diagnostiek Centrum Delta.",
        "Diagnostiek Centrum Delta",
        "NL_CARE_ORGANIZATION",
        "contextual_review",
        ("Laboratorium",),
    ),
    _positive(
        "location_named",
        "Locatie: Stichting Morgenlicht, locatie Parkzicht.",
        "locatie Parkzicht",
        "NL_CARE_LOCATION_REFERENCE",
        "contextual_review",
        ("Locatie", "Stichting Morgenlicht"),
    ),
    _positive(
        "location_department",
        "Verzendende organisatie: Stedelijk Ziekenhuis Noord, afdeling Neurologie B.",
        "afdeling Neurologie B",
        "NL_CARE_LOCATION_REFERENCE",
        "contextual_review",
        ("Verzendende organisatie", "Stedelijk Ziekenhuis Noord"),
    ),
    _positive(
        "location_team",
        "Ontvangende organisatie: Wijkzorg Rijnmond, team Kralingen.",
        "team Kralingen",
        "NL_CARE_LOCATION_REFERENCE",
        "contextual_review",
        ("Ontvangende organisatie", "Wijkzorg Rijnmond"),
    ),
    _positive(
        "location_residence",
        "Zorgorganisatie: Zorggroep Kompas, woonlocatie De Linde.",
        "woonlocatie De Linde",
        "NL_CARE_LOCATION_REFERENCE",
        "contextual_review",
        ("Zorgorganisatie", "Zorggroep Kompas"),
    ),
    _positive(
        "room_number",
        "Cliënt verblijft in kamer 214.",
        "kamer 214",
        "NL_ROOM_OR_BED_REFERENCE",
        "contextual_review",
        ("Cliënt verblijft in",),
    ),
    _positive(
        "bed_reference",
        "Patiënt ligt op bed B-12.",
        "bed B-12",
        "NL_ROOM_OR_BED_REFERENCE",
        "contextual_review",
        ("Patiënt ligt op",),
    ),
    _positive(
        "apartment_reference",
        "Cliënt woont in appartement 3B.",
        "appartement 3B",
        "NL_ROOM_OR_BED_REFERENCE",
        "contextual_review",
        ("Cliënt woont in",),
    ),
    _positive(
        "admission_date",
        "Opnamedatum: 10-06-2026.",
        "10-06-2026",
        "NL_CARE_EVENT_DATE",
        "contextual_review",
        ("Opnamedatum",),
        ("NL_DATE_OF_BIRTH",),
    ),
    _positive(
        "discharge_date",
        "Ontslagdatum: 14-06-2026.",
        "14-06-2026",
        "NL_CARE_EVENT_DATE",
        "contextual_review",
        ("Ontslagdatum",),
        ("NL_DATE_OF_BIRTH",),
    ),
    _positive(
        "report_date",
        "Rapportagedatum: 12-06-2026.",
        "12-06-2026",
        "NL_CARE_EVENT_DATE",
        "contextual_review",
        ("Rapportagedatum",),
        ("NL_DATE_OF_BIRTH",),
    ),
    _positive(
        "evaluation_date",
        "Evaluatiedatum: 01-07-2026.",
        "01-07-2026",
        "NL_CARE_EVENT_DATE",
        "contextual_review",
        ("Evaluatiedatum",),
        ("NL_DATE_OF_BIRTH",),
    ),
    _positive(
        "incident_date",
        "Incidentdatum: 21-06-2026 om 20:15 uur.",
        "21-06-2026",
        "NL_CARE_EVENT_DATE",
        "contextual_review",
        ("Incidentdatum", "20:15 uur"),
        ("NL_DATE_OF_BIRTH",),
    ),
)


NEGATIVE_CASES: Tuple[Dict[str, Any], ...] = (
    {
        "id": "bsn_is_not_agb",
        "text": "BSN: 123456782.",
        "forbidden_entities": ["NL_AGB_CODE"],
        "preserved_text": ["BSN", "123456782"],
    },
    {
        "id": "big_is_not_agb",
        "text": "BIG-nummer: 11223344556.",
        "forbidden_entities": ["NL_AGB_CODE"],
        "preserved_text": ["BIG-nummer", "11223344556"],
    },
    {
        "id": "date_of_birth_is_not_event_date",
        "text": "Geboortedatum: 14-02-1948.",
        "forbidden_entities": ["NL_CARE_EVENT_DATE"],
        "preserved_text": ["Geboortedatum", "14-02-1948"],
    },
    {
        "id": "blood_pressure",
        "text": "Bloeddruk 123/78 mmHg.",
        "forbidden_entities": list(CARE_RECOGNIZER_ENTITY_NAMES),
        "preserved_text": ["Bloeddruk 123/78 mmHg"],
    },
    {
        "id": "temperature",
        "text": "Temperatuur 36,8 °C.",
        "forbidden_entities": list(CARE_RECOGNIZER_ENTITY_NAMES),
        "preserved_text": ["Temperatuur 36,8 °C"],
    },
    {
        "id": "medication_dosage",
        "text": "Metformine 500 mg tweemaal daags.",
        "forbidden_entities": list(CARE_RECOGNIZER_ENTITY_NAMES),
        "preserved_text": ["Metformine 500 mg tweemaal daags"],
    },
    {
        "id": "administration_time",
        "text": "Apixaban wordt om 20:00 uur toegediend.",
        "forbidden_entities": list(CARE_RECOGNIZER_ENTITY_NAMES),
        "preserved_text": ["20:00 uur"],
    },
    {
        "id": "laboratory_result",
        "text": "Hemoglobine: 7,8 mmol/L, referentie 8,5-11,0.",
        "forbidden_entities": list(CARE_RECOGNIZER_ENTITY_NAMES),
        "preserved_text": ["7,8 mmol/L", "8,5-11,0"],
    },
    {
        "id": "glucose_result",
        "text": "Glucose: 4,4 mmol/L.",
        "forbidden_entities": list(CARE_RECOGNIZER_ENTITY_NAMES),
        "preserved_text": ["Glucose: 4,4 mmol/L"],
    },
    {
        "id": "pain_score",
        "text": "De pijnscore daalde van 6 naar 3.",
        "forbidden_entities": list(CARE_RECOGNIZER_ENTITY_NAMES),
        "preserved_text": ["pijnscore", "6 naar 3"],
    },
    {
        "id": "dosage_not_room",
        "text": "De totale dosering bedraagt 214 mg.",
        "forbidden_entities": ["NL_ROOM_OR_BED_REFERENCE"],
        "preserved_text": ["214 mg"],
    },
    {
        "id": "clinical_dbc_code",
        "text": "DBC-code: DBC-2026-7711 blijft klinische/declaratiecontext.",
        "forbidden_entities": [
            "NL_PATIENT_NUMBER",
            "NL_MEDICAL_RECORD_NUMBER",
            "NL_TREATMENT_REFERENCE",
        ],
        "preserved_text": ["DBC-code", "DBC-2026-7711"],
    },
    {
        "id": "clinical_icd_code",
        "text": "Diagnosecode ICD-10 E11.9 voor diabetes mellitus type 2.",
        "forbidden_entities": list(CARE_RECOGNIZER_ENTITY_NAMES),
        "preserved_text": ["ICD-10 E11.9", "diabetes mellitus type 2"],
    },
    {
        "id": "relative_time_is_not_event_date",
        "text": "Controle bij de neuroloog over zes weken.",
        "forbidden_entities": ["NL_CARE_EVENT_DATE"],
        "preserved_text": ["over zes weken"],
    },
    {
        "id": "generic_room_word",
        "text": "De behandeling vond plaats in een rustige kamer.",
        "forbidden_entities": ["NL_ROOM_OR_BED_REFERENCE"],
        "preserved_text": ["rustige kamer"],
    },
    {
        "id": "professional_role_without_name",
        "text": "De verpleegkundige controleert de medicatielijst.",
        "forbidden_entities": ["NL_CARE_PROVIDER_NAME"],
        "preserved_text": ["verpleegkundige", "medicatielijst"],
    },
)


ALL_POSITIVE_CASES: Tuple[Dict[str, Any], ...] = (
    REFERENCE_POSITIVE_CASES + CONTEXTUAL_REVIEW_POSITIVE_CASES
)


def contract_snapshot() -> Dict[str, Any]:
    """Return the stable, serializable recognizer-contract snapshot."""

    return {
        "schema_version": CARE_RECOGNIZER_CONTRACT_SCHEMA_VERSION,
        "module": CARE_RECOGNIZER_MODULE,
        "public_api": list(CARE_RECOGNIZER_PUBLIC_API),
        "supported_language": CARE_RECOGNIZER_SUPPORTED_LANGUAGE,
        "entity_names": list(CARE_RECOGNIZER_ENTITY_NAMES),
        "positive_cases": [dict(case) for case in ALL_POSITIVE_CASES],
        "negative_cases": [dict(case) for case in NEGATIVE_CASES],
        "production_ready": False,
        "human_review_required": True,
    }
