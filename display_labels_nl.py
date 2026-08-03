ENTITY_DISPLAY_LABELS_NL = {
    "PERSON": "Naam / persoon",
    "LOCATION": "Locatie",
    "ORGANIZATION": "Organisatie",
    "EMAIL_ADDRESS": "E-mailadres",
    "PHONE_NUMBER": "Telefoonnummer",
    "IBAN_CODE": "IBAN",
    "CREDIT_CARD": "Betaalkaart",
    "DATE_TIME": "Datum/tijd",
    "URL": "URL",
    "IP_ADDRESS": "IP-adres",
    "GENERIC_PII": "Vertrouwelijke waarde",
    "NL_BSN": "BSN",
    "NL_POSTCODE": "Postcode",
    "NL_IBAN": "Nederlandse IBAN",
    "NL_KVK_NUMBER": "KvK-nummer",
    "NL_VAT_NUMBER": "Btw-nummer",
    "NL_PHONE_NUMBER": "Nederlands telefoonnummer",
    "NL_LICENSE_PLATE": "Kenteken",
    "NL_DRIVER_LICENSE": "Rijbewijsnummer",
    "NL_BIG_NUMBER": "BIG-nummer",
    "NL_ADDRESS": "Adres",
    "NL_DATE_OF_BIRTH": "Geboortedatum",
    "NL_ECLI": "ECLI",
    "NL_LEGAL_CASE_NUMBER": "Zaaknummer",
    "NL_ROLNUMMER": "Rolnummer",
    "NL_REKESTNUMMER": "Rekestnummer",
    "NL_PARKETNUMMER": "Parketnummer",
    "NL_DOSSIER_NUMBER": "Dossiernummer",
    "NL_CLIENT_NUMBER": "Clientnummer",
    "NL_CJIB_NUMBER": "CJIB-nummer",
    "NL_POLICE_REPORT_NUMBER": "Proces-verbaalnummer",
    "NL_INSURANCE_CLAIM_NUMBER": "Schade-/polisnummer",
    "NL_INCIDENT_NUMBER": "Incidentnummer",
    "NL_CLAIM_NUMBER": "Claimnummer",
    "NL_OTHER_REFERENCE": "Overige referentie",
    "NL_LEGAL_PARTY_NAME": "Procespartij / naam",
    "NL_COURT_OR_AUTHORITY": "Rechtbank of instantie",
    "NL_CLIENT_REFERENCE": "Clientreferentie",
    "NL_CASE_REFERENCE": "Zaakreferentie",
    "NL_INTERNAL_REFERENCE": "Interne referentie",
    "NL_CONTEXTUAL_REFERENCE": "Contextuele referentie",
    "NL_INVOICE_NUMBER": "Factuurnummer",
    "NL_ORDER_OR_CONTRACT_NUMBER": "Contract- of ordernummer",
    "NL_SCHOOL_REFERENCE": "Schoolreferentie",
    "NL_CHILD_PROTECTION_REFERENCE": "Jeugd-/beschermingsreferentie",
    "NL_EMPLOYMENT_REFERENCE": "Arbeidsrechtelijke referentie",
    "NL_INSURANCE_REFERENCE": "Verzekeringsreferentie",
    "NL_HEALTHCARE_REFERENCE": "Zorgreferentie",
    "NL_PATIENT_NUMBER": "Patiëntnummer",
    "NL_CARE_CLIENT_NUMBER": "Zorgcliëntnummer",
    "NL_MEDICAL_RECORD_NUMBER": "Medisch dossiernummer",
    "NL_EPD_ECD_NUMBER": "EPD- of ECD-nummer",
    "NL_HEALTH_INSURANCE_NUMBER": "Verzekerdennummer",
    "NL_REFERRAL_NUMBER": "Verwijsnummer",
    "NL_TREATMENT_REFERENCE": "Behandel- of zorgtrajectnummer",
    "NL_LAB_SAMPLE_NUMBER": "Laboratorium- of monsternummer",
    "NL_CARE_INCIDENT_NUMBER": "Zorgincidentnummer",
    "NL_CARE_INDICATION_REFERENCE": "Indicatie- of beschikkingreferentie",
    "NL_AGB_CODE": "AGB-code",
    "NL_CARE_PROVIDER_NAME": "Zorgverlener / naam",
    "NL_CARE_ORGANIZATION": "Zorgorganisatie",
    "NL_CARE_LOCATION_REFERENCE": "Zorglocatie, afdeling of team",
    "NL_ROOM_OR_BED_REFERENCE": "Kamer- of bedreferentie",
    "NL_CARE_EVENT_DATE": "Exacte zorgdatum",
    "NL_POLICE_REFERENCE": "Politie-/OM-referentie",
    "NL_IMMIGRATION_REFERENCE": "Vreemdelingenreferentie",
    "NL_MUNICIPAL_REFERENCE": "Bestuursrechtelijke referentie",
    "NL_REAL_ESTATE_REFERENCE": "Vastgoed-/huurreferentie",
    "NL_VEHICLE_REFERENCE": "Voertuig-/kentekenreferentie",
    "NL_OBJECT_REFERENCE": "Objectreferentie",
    "NL_SUSPICIOUS_REFERENCE_CANDIDATE": "Mogelijke referentie",
    "NL_POSSIBLE_LICENSE_PLATE": "Mogelijk kenteken",
    "REMEMBERED": "Onthouden vervanging",
    "MANUAL": "Handmatige vervanging",
}

SOURCE_LABELS_NL = {
    "detected": "Automatisch herkend",
    "candidate": "Mogelijke kandidaat",
    "remembered": "Onthouden",
    "manual": "Handmatig",
}


def entity_label(entity_type: str) -> str:
    return ENTITY_DISPLAY_LABELS_NL.get(entity_type or "", entity_type or "Onbekend")


def source_label(source: str) -> str:
    return SOURCE_LABELS_NL.get(source or "", source or "Onbekend")


def confidence_label(score) -> str:
    try:
        value = float(score)
    except Exception:
        return ""
    if value >= 0.85:
        return "Hoog"
    if value >= 0.60:
        return "Middel"
    return "Laag"
