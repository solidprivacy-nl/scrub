"""Pure policy contract for the first Dutch care recognition profile.

This module contains no Streamlit, Presidio, network, file-system or cloud logic.
It records what the future care profile should replace, review, preserve or only
surface as residual-risk evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Mapping, Sequence


ACTION_REPLACE = "replace"
ACTION_REVIEW_SELECTED = "review_selected"
ACTION_PRESERVE = "preserve"
ACTION_AUDIT_ONLY = "audit_only"

VALID_ACTIONS = {
    ACTION_REPLACE,
    ACTION_REVIEW_SELECTED,
    ACTION_PRESERVE,
    ACTION_AUDIT_ONLY,
}


@dataclass(frozen=True)
class CarePolicyRule:
    entity_type: str
    action: str
    label_nl: str
    reason_nl: str
    examples: tuple[str, ...]


CARE_POLICY_RULES: tuple[CarePolicyRule, ...] = (
    CarePolicyRule(
        "PERSON",
        ACTION_REPLACE,
        "Naam van patiënt, cliënt of naaste",
        "Directe persoonsidentificatie wordt standaard vervangen.",
        ("Ahmed El Mansouri", "mantelzorger Fatima El Mansouri"),
    ),
    CarePolicyRule(
        "NL_BSN",
        ACTION_REPLACE,
        "BSN",
        "Het BSN is een direct identificerend persoonsnummer.",
        ("123456782",),
    ),
    CarePolicyRule(
        "NL_DATE_OF_BIRTH",
        ACTION_REPLACE,
        "Geboortedatum",
        "De geboortedatum is in zorgdocumenten sterk herleidbaar.",
        ("14-02-1948",),
    ),
    CarePolicyRule(
        "NL_ADDRESS",
        ACTION_REPLACE,
        "Adres",
        "Een volledig woon- of verblijfadres identificeert de betrokkene.",
        ("Zorglaan 18, 3511 AB Utrecht",),
    ),
    CarePolicyRule(
        "NL_POSTCODE",
        ACTION_REPLACE,
        "Postcode",
        "Een postcode kan samen met andere gegevens herleidbaar zijn.",
        ("3511 AB",),
    ),
    CarePolicyRule(
        "EMAIL_ADDRESS",
        ACTION_REPLACE,
        "E-mailadres",
        "Een persoonlijk e-mailadres identificeert de betrokkene direct.",
        ("ahmed@example.invalid",),
    ),
    CarePolicyRule(
        "PHONE_NUMBER",
        ACTION_REPLACE,
        "Telefoonnummer",
        "Een persoonlijk telefoonnummer identificeert de betrokkene direct.",
        ("06 12345678",),
    ),
    CarePolicyRule(
        "NL_PHONE_NUMBER",
        ACTION_REPLACE,
        "Nederlands telefoonnummer",
        "Een persoonlijk telefoonnummer identificeert de betrokkene direct.",
        ("030 2345678",),
    ),
    CarePolicyRule(
        "NL_PATIENT_NUMBER",
        ACTION_REPLACE,
        "Patiëntnummer",
        "Een patiëntnummer koppelt tekst aan een specifieke patiëntregistratie.",
        ("PAT-2026-1148",),
    ),
    CarePolicyRule(
        "NL_CARE_CLIENT_NUMBER",
        ACTION_REPLACE,
        "Zorgcliëntnummer",
        "Een cliëntnummer koppelt tekst aan een specifieke zorgcliënt.",
        ("CL-ZORG-7712",),
    ),
    CarePolicyRule(
        "NL_MEDICAL_RECORD_NUMBER",
        ACTION_REPLACE,
        "Medisch dossiernummer",
        "Een medisch dossiernummer verwijst naar een individueel dossier.",
        ("MD-2026-4412",),
    ),
    CarePolicyRule(
        "NL_EPD_ECD_NUMBER",
        ACTION_REPLACE,
        "EPD- of ECD-nummer",
        "Een EPD/ECD-nummer koppelt het document aan een individuele registratie.",
        ("ECD-889144", "EPD-2026-5501"),
    ),
    CarePolicyRule(
        "NL_HEALTH_INSURANCE_NUMBER",
        ACTION_REPLACE,
        "Verzekerdennummer",
        "Een persoonsgebonden verzekerdennummer is administratieve identificatie.",
        ("VERZ-88441122",),
    ),
    CarePolicyRule(
        "NL_REFERRAL_NUMBER",
        ACTION_REPLACE,
        "Verwijsnummer",
        "Een patiëntspecifieke verwijzing kan het zorgtraject identificeren.",
        ("VERW-2026-7711",),
    ),
    CarePolicyRule(
        "NL_TREATMENT_REFERENCE",
        ACTION_REPLACE,
        "Behandel- of zorgtrajectnummer",
        "Een patiëntspecifieke behandelreferentie koppelt tekst aan een traject.",
        ("BEH-2026-1188",),
    ),
    CarePolicyRule(
        "NL_LAB_SAMPLE_NUMBER",
        ACTION_REPLACE,
        "Laboratorium- of monsternummer",
        "Een laboratoriumreferentie kan rechtstreeks naar de patiëntorder leiden.",
        ("LAB-2026-4412",),
    ),
    CarePolicyRule(
        "NL_CARE_INCIDENT_NUMBER",
        ACTION_REPLACE,
        "Zorgincidentnummer",
        "Een MIC/MIM/VIM- of incidentnummer koppelt tekst aan een specifieke melding.",
        ("MIC-2026-0912",),
    ),
    CarePolicyRule(
        "NL_CARE_INDICATION_REFERENCE",
        ACTION_REPLACE,
        "Indicatie- of beschikkingreferentie",
        "Een CIZ, Wlz, Wmo of zorgtoewijzingsreferentie kan de cliënt identificeren.",
        ("CIZ-2026-5512",),
    ),
    CarePolicyRule(
        "NL_CARE_PROVIDER_NAME",
        ACTION_REVIEW_SELECTED,
        "Naam zorgverlener",
        "De naam is herleidbaar, maar kan voor professionele context nodig zijn.",
        ("dr. Karin de Groot", "verpleegkundige Omar El Idrissi"),
    ),
    CarePolicyRule(
        "NL_BIG_NUMBER",
        ACTION_REVIEW_SELECTED,
        "BIG-nummer",
        "Het nummer identificeert een zorgverlener en wordt daarom gecontroleerd.",
        ("12345678901",),
    ),
    CarePolicyRule(
        "NL_AGB_CODE",
        ACTION_REVIEW_SELECTED,
        "AGB-code",
        "De code identificeert een zorgverlener, vestiging of onderneming.",
        ("01020304",),
    ),
    CarePolicyRule(
        "NL_CARE_ORGANIZATION",
        ACTION_REVIEW_SELECTED,
        "Zorgorganisatie",
        "Een instelling kan in combinatie met andere details indirect herleidbaar zijn.",
        ("Stichting Morgenlicht",),
    ),
    CarePolicyRule(
        "NL_CARE_LOCATION_REFERENCE",
        ACTION_REVIEW_SELECTED,
        "Zorglocatie, afdeling of team",
        "Een specifieke locatie kan een kleine patiëntgroep of casus identificeren.",
        ("locatie Parkzicht", "afdeling Neurologie B"),
    ),
    CarePolicyRule(
        "NL_ROOM_OR_BED_REFERENCE",
        ACTION_REVIEW_SELECTED,
        "Kamer- of bednummer",
        "Een kamer of bed kan samen met datum en locatie indirect identificeren.",
        ("kamer 214", "bed B-12"),
    ),
    CarePolicyRule(
        "NL_CARE_EVENT_DATE",
        ACTION_REVIEW_SELECTED,
        "Exacte zorgdatum",
        "Exacte opname-, ontslag-, afspraak- of behandeldatums worden gecontroleerd.",
        ("opgenomen op 12-06-2026",),
    ),
    CarePolicyRule(
        "CARE_DIAGNOSIS",
        ACTION_PRESERVE,
        "Diagnose",
        "Diagnose is klinische betekenis en wordt niet blind gemaskeerd.",
        ("diabetes mellitus type 2",),
    ),
    CarePolicyRule(
        "CARE_MEDICATION",
        ACTION_PRESERVE,
        "Medicatie",
        "Geneesmiddelnaam is noodzakelijke klinische inhoud.",
        ("metformine", "paracetamol"),
    ),
    CarePolicyRule(
        "CARE_DOSAGE",
        ACTION_PRESERVE,
        "Dosering en toedieningsschema",
        "Dosering en schema zijn noodzakelijke klinische inhoud.",
        ("500 mg tweemaal daags",),
    ),
    CarePolicyRule(
        "CARE_LAB_RESULT",
        ACTION_PRESERVE,
        "Laboratoriumuitslag",
        "Uitslag, eenheid en referentiewaarde moeten inhoudelijk intact blijven.",
        ("Hb 7,8 mmol/L",),
    ),
    CarePolicyRule(
        "CARE_OBSERVATION",
        ACTION_PRESERVE,
        "Observatie of voortgang",
        "Verpleegkundige en medische observaties dragen de inhoud van het document.",
        ("mobiliseert met rollator",),
    ),
    CarePolicyRule(
        "CARE_VITAL_SIGN",
        ACTION_PRESERVE,
        "Vitale parameter",
        "Bloeddruk, pols, temperatuur en saturatie zijn klinische inhoud.",
        ("bloeddruk 123/78 mmHg",),
    ),
    CarePolicyRule(
        "CARE_ALLERGY",
        ACTION_PRESERVE,
        "Allergie",
        "Een allergie is essentiële klinische informatie.",
        ("allergisch voor penicilline",),
    ),
    CarePolicyRule(
        "CARE_TREATMENT",
        ACTION_PRESERVE,
        "Behandeling of verrichting",
        "Behandelinhoud moet leesbaar blijven.",
        ("wondzorg volgens protocol",),
    ),
    CarePolicyRule(
        "CARE_GOAL",
        ACTION_PRESERVE,
        "Zorgdoel",
        "Zorgdoelen en evaluatiecriteria zijn noodzakelijke professionele context.",
        ("zelfstandig transfereren binnen zes weken",),
    ),
    CarePolicyRule(
        "CARE_ROLE",
        ACTION_PRESERVE,
        "Zorgrol",
        "Woorden zoals patiënt, arts en verpleegkundige blijven als rol leesbaar.",
        ("patiënt", "arts", "verpleegkundige"),
    ),
    CarePolicyRule(
        "CARE_CLINICAL_CODE",
        ACTION_PRESERVE,
        "Klinische classificatiecode",
        "Klinische codes worden behouden tenzij bewijs toont dat ze patiëntspecifiek zijn.",
        ("ICD-10 E11.9",),
    ),
    CarePolicyRule(
        "CARE_RARE_CASE_COMBINATION",
        ACTION_AUDIT_ONLY,
        "Zeldzame combinatie van casusdetails",
        "Indirecte herleidbaarheid wordt als restrisico gemeld zonder klinische inhoud blind te verwijderen.",
        ("zeldzame diagnose plus kleine locatie en exacte datum",),
    ),
)


CARE_POLICY_BY_ENTITY: Dict[str, CarePolicyRule] = {
    rule.entity_type: rule for rule in CARE_POLICY_RULES
}


def policy_for_entity(entity_type: str) -> CarePolicyRule | None:
    """Return the frozen care-profile rule for an entity type, if defined."""

    return CARE_POLICY_BY_ENTITY.get(str(entity_type or "").strip())


def entities_for_action(action: str) -> tuple[str, ...]:
    """Return entity types assigned to one policy action."""

    if action not in VALID_ACTIONS:
        raise ValueError(f"Unknown care-profile action: {action}")
    return tuple(rule.entity_type for rule in CARE_POLICY_RULES if rule.action == action)


def validate_care_policy_rules(
    rules: Sequence[CarePolicyRule] = CARE_POLICY_RULES,
) -> tuple[str, ...]:
    """Return deterministic contract errors; an empty tuple means valid."""

    errors: list[str] = []
    seen: set[str] = set()
    for index, rule in enumerate(rules):
        prefix = f"rule[{index}]"
        if not rule.entity_type.strip():
            errors.append(f"{prefix}: missing entity_type")
        elif rule.entity_type in seen:
            errors.append(f"{prefix}: duplicate entity_type {rule.entity_type}")
        seen.add(rule.entity_type)
        if rule.action not in VALID_ACTIONS:
            errors.append(f"{prefix}: invalid action {rule.action}")
        if not rule.label_nl.strip():
            errors.append(f"{prefix}: missing Dutch label")
        if not rule.reason_nl.strip():
            errors.append(f"{prefix}: missing reason")
        if not rule.examples:
            errors.append(f"{prefix}: missing examples")
        elif any(not str(value).strip() for value in rule.examples):
            errors.append(f"{prefix}: contains empty example")
    return tuple(errors)


def policy_snapshot() -> Mapping[str, str]:
    """Return a stable entity-to-action mapping for reports and tests."""

    return {rule.entity_type: rule.action for rule in CARE_POLICY_RULES}
