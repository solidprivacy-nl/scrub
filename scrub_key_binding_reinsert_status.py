"""Pure user-facing status model for document/Scrub-Key binding results."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


_STATUS_LABELS = {
    "bound_match": "Documentgebonden match bevestigd",
    "legacy_unbound": "Legacy sleutel: documentmatch niet verifieerbaar",
    "binding_mismatch": "Document en Scrub Key horen niet bij elkaar",
    "mixed_document_bindings": "Document bevat meerdere documentcodes",
    "missing_document_binding": "Documentcode ontbreekt in het document",
    "invalid_mapping_digest": "Scrub Key-controlewaarde is ongeldig",
    "invalid_bound_key": "Documentgebonden Scrub Key is ongeldig",
    "legacy_key_for_bound_document": "Legacy sleutel past niet bij documentgebonden placeholders",
    "invalid_document": "Document kon niet veilig worden gevalideerd",
}

_FAIL_CLOSED_STATUSES = {
    "binding_mismatch",
    "mixed_document_bindings",
    "missing_document_binding",
    "invalid_mapping_digest",
    "invalid_bound_key",
    "legacy_key_for_bound_document",
    "invalid_document",
}


def binding_status_notice(result: Mapping[str, Any] | Any) -> dict[str, Any]:
    """Return stable Dutch status copy without rendering or side effects."""

    payload = result if isinstance(result, Mapping) else {}
    status = str(payload.get("binding_status") or "").strip()
    verified = payload.get("verified_document_match") is True
    legacy = payload.get("legacy_unbound") is True
    replacement_allowed = payload.get("replacement_allowed") is True

    if status == "bound_match" and verified and replacement_allowed:
        level = "success"
        message = (
            "Document en Scrub Key horen aantoonbaar bij elkaar. "
            "De documentcode en controlewaarde zijn geldig."
        )
    elif status == "legacy_unbound" and legacy and replacement_allowed:
        level = "warning"
        message = (
            "Deze oudere Scrub Key is niet documentgebonden. Terugzetten blijft mogelijk "
            "voor compatibiliteit, maar de app kan niet bewijzen dat deze sleutel bij dit document hoort."
        )
    elif status in _FAIL_CLOSED_STATUSES or not replacement_allowed:
        level = "error"
        message = (
            "Terugzetten is geblokkeerd voordat waarden zijn hersteld. "
            "Controleer of document en Scrub Key bij elkaar horen en ongewijzigd zijn."
        )
    else:
        level = "info"
        message = "De document- en sleutelbinding is nog niet vastgesteld."

    return {
        "binding_status": status,
        "status_label": _STATUS_LABELS.get(status, status or "Niet vastgesteld"),
        "level": level,
        "message": message,
        "replacement_allowed": replacement_allowed,
        "verified_document_match": verified,
        "legacy_unbound": legacy,
        "fail_closed": status in _FAIL_CLOSED_STATUSES or not replacement_allowed,
    }
