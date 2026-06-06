"""Review filter helpers for the Scrub replacement workflow.

The filters are intentionally presentation-oriented. They help the user focus on
specific rows, but they should not silently remove hidden rows from the export
workflow unless the UI explicitly implements safe merge-back behaviour.
"""

from __future__ import annotations

from typing import Any, Iterable, Mapping

FILTER_SHOW_ALL = "Toon alles"
FILTER_NEEDS_REVIEW = "Alleen controle nodig"
FILTER_LEGAL_REFERENCES = "Alleen juridische referenties"
FILTER_NAMES_ADDRESSES = "Alleen namen/adressen"
FILTER_LOW_CONFIDENCE = "Alleen lage zekerheid"

REVIEW_FILTER_OPTIONS = [
    FILTER_SHOW_ALL,
    FILTER_NEEDS_REVIEW,
    FILTER_LEGAL_REFERENCES,
    FILTER_NAMES_ADDRESSES,
    FILTER_LOW_CONFIDENCE,
]

LEGAL_REFERENCE_ENTITY_TYPES = {
    "NL_LEGAL_CASE_NUMBER",
    "NL_ROLNUMMER",
    "NL_REKESTNUMMER",
    "NL_PARKETNUMMER",
    "NL_DOSSIER_NUMBER",
    "NL_CLIENT_NUMBER",
    "NL_CJIB_NUMBER",
    "NL_POLICE_REPORT_NUMBER",
    "NL_INSURANCE_CLAIM_NUMBER",
    "NL_INCIDENT_NUMBER",
    "NL_CLAIM_NUMBER",
    "NL_OTHER_REFERENCE",
    "NL_CLIENT_REFERENCE",
    "NL_CASE_REFERENCE",
    "NL_INTERNAL_REFERENCE",
    "NL_CONTEXTUAL_REFERENCE",
    "NL_INVOICE_NUMBER",
    "NL_ORDER_OR_CONTRACT_NUMBER",
    "NL_SCHOOL_REFERENCE",
    "NL_CHILD_PROTECTION_REFERENCE",
    "NL_EMPLOYMENT_REFERENCE",
    "NL_INSURANCE_REFERENCE",
    "NL_HEALTHCARE_REFERENCE",
    "NL_POLICE_REFERENCE",
    "NL_IMMIGRATION_REFERENCE",
    "NL_MUNICIPAL_REFERENCE",
    "NL_REAL_ESTATE_REFERENCE",
    "NL_VEHICLE_REFERENCE",
    "NL_OBJECT_REFERENCE",
    "NL_SUSPICIOUS_REFERENCE_CANDIDATE",
    "NL_POSSIBLE_LICENSE_PLATE",
    "NL_ECLI",
    "NL_KVK_NUMBER",
    "NL_VAT_NUMBER",
    "NL_BIG_NUMBER",
}

NAME_ADDRESS_ENTITY_TYPES = {
    "PERSON",
    "NL_LEGAL_PARTY_NAME",
    "LOCATION",
    "NL_ADDRESS",
    "NL_POSTCODE",
    "ORGANIZATION",
    "NL_COURT_OR_AUTHORITY",
}


def _cell(row: Mapping[str, Any], key: str, default: Any = "") -> Any:
    value = row.get(key, default)
    return default if value is None else value


def _normalised_entity_type(row: Mapping[str, Any]) -> str:
    return str(_cell(row, "entity_type", "")).strip().upper()


def _normalised_status(row: Mapping[str, Any]) -> str:
    status = str(_cell(row, "review_status", "")).strip().lower()
    label = str(_cell(row, "review_status_label", "")).strip().lower()
    if status:
        return status
    if label == "controle nodig":
        return "needs_review"
    if label == "automatisch vervangen":
        return "auto_detected"
    if label == "handmatig toegevoegd":
        return "manual"
    if label == "onthouden vervanging":
        return "remembered"
    return ""


def _score(row: Mapping[str, Any]) -> float | None:
    raw = _cell(row, "score", None)
    if raw in (None, ""):
        return None
    try:
        return float(raw)
    except Exception:
        return None


def row_matches_review_filter(row: Mapping[str, Any], filter_label: str) -> bool:
    if filter_label == FILTER_SHOW_ALL:
        return True

    if filter_label == FILTER_NEEDS_REVIEW:
        return _normalised_status(row) == "needs_review"

    entity_type = _normalised_entity_type(row)

    if filter_label == FILTER_LEGAL_REFERENCES:
        return entity_type in LEGAL_REFERENCE_ENTITY_TYPES

    if filter_label == FILTER_NAMES_ADDRESSES:
        return entity_type in NAME_ADDRESS_ENTITY_TYPES

    if filter_label == FILTER_LOW_CONFIDENCE:
        confidence = str(_cell(row, "confidence", "")).strip().lower()
        score = _score(row)
        return confidence == "laag" or (score is not None and score < 0.60)

    return True


def filter_review_records(records: Iterable[Mapping[str, Any]], filter_label: str) -> list[Mapping[str, Any]]:
    return [row for row in records if row_matches_review_filter(row, filter_label)]


def filter_review_dataframe(df, filter_label: str):
    """Filter a pandas-like DataFrame without importing pandas at module import.

    Tests use the record-level function. The Streamlit app can use this helper
    with a pandas DataFrame.
    """
    if filter_label == FILTER_SHOW_ALL:
        return df
    if df is None or len(df) == 0:
        return df
    mask = [row_matches_review_filter(row, filter_label) for _, row in df.iterrows()]
    return df.loc[mask].reset_index(drop=True)
