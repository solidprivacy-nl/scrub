"""Report-only Streamlit panel for DOCX hygiene audit findings.

WP39D intentionally keeps this UI small and non-mutating. It shows the existing
``docx_hygiene_audit.py`` helper output near DOCX export/download controls.
It does not clean DOCX content, remove comments, remove tracked changes, remove metadata, block export, change export/download behavior, write Scrub Key data, change reinsert behavior, add dependencies, call cloud services or use real data.
"""

from __future__ import annotations

from typing import Any

import streamlit as st

from docx_hygiene_audit import build_docx_hygiene_audit_report


SEVERITY_LABELS = {
    "low": "laag",
    "medium": "onbekend / middel",
    "high": "hoog",
}


def _safe_count(report: dict[str, Any], key: str) -> int:
    counts = report.get("counts") or {}
    value = counts.get(key, 0)
    return value if isinstance(value, int) else 0


def _boundary_caption() -> str:
    return (
        "Alleen rapportage · Geen clean-DOCX garantie · Export wordt niet geblokkeerd · "
        "Bestaande export blijft ongewijzigd · Geen Scrub Key wijziging · Geen reinsert wijziging"
    )


def render_docx_hygiene_audit_panel(docx_bytes: bytes | None, *, source_label: str = "DOCX-export") -> dict[str, Any] | None:
    """Render a compact report-only DOCX hygiene audit panel.

    Returns the audit report for optional downstream display/testing. The return
    value is informational only; callers must not use it to block export or mutate
    document bytes.
    """

    if not docx_bytes:
        return None

    report = build_docx_hygiene_audit_report(docx_bytes)
    summary = report.get("summary") or {}
    severity = str(summary.get("severity", "unknown"))
    expanded = severity in {"medium", "high"}

    with st.expander("DOCX hygiene audit", expanded=expanded):
        st.markdown("**DOCX hygiene audit**")
        st.info(
            "Alleen rapportage. Dit is een audit/waarschuwing en geen automatische opschoning. "
            "De gebruiker blijft zelf verantwoordelijk voor controle vóór delen of exporteren."
        )
        st.caption(_boundary_caption())
        st.warning(
            "Geen clean-DOCX garantie. De huidige DOCX-export mag niet als ‘clean DOCX’ worden gepresenteerd."
        )
        st.caption(
            "Controleer metadata, opmerkingen, revisies en verborgen inhoud. "
            "Let ook op kopteksten, voetteksten, opmerkingen/kantlijncommentaren en bijgehouden wijzigingen."
        )

        metric_cols = st.columns(5)
        metric_cols[0].metric("Risiconiveau", SEVERITY_LABELS.get(severity, severity))
        metric_cols[1].metric("Findings", int(summary.get("finding_count", 0) or 0))
        metric_cols[2].metric("Kopteksten", _safe_count(report, "headers"))
        metric_cols[3].metric("Voetteksten", _safe_count(report, "footers"))
        metric_cols[4].metric("Revisies", _safe_count(report, "tracked_changes"))

        st.caption(f"Bron: {source_label}")
        st.caption("Report-only status: waar · Cleaning applied: false · Export blocking: false")
        st.caption("Bestaande export blijft ongewijzigd; deze UI wijzigt geen document en vervangt geen downloadknoppen.")

        if severity == "high":
            st.error("Verborgen of moeilijk zichtbare DOCX-inhoud is gevonden. Controleer dit vóór delen of exporteren.")
        elif severity == "medium":
            st.warning("DOCX-hygiënerisico kon niet volledig worden beoordeeld. Claim het bestand niet als schoon.")
        else:
            st.info("Geen ondersteunde verborgen DOCX-onderdelen gevonden, maar dit is geen clean-DOCX garantie.")

        findings = report.get("findings") or []
        if findings:
            st.markdown("**Verborgen onderdelen gevonden**")
            for finding in findings:
                title = finding.get("title", "DOCX finding")
                count = finding.get("count", 0)
                recommended_action = finding.get("recommended_action", "Controleer handmatig vóór delen.")
                st.write(f"- {title} — aantal: {count}. Aanbevolen controle: {recommended_action}")
        else:
            st.caption("Geen ondersteunde findings gevonden door deze audithelper.")

        warnings = report.get("warnings") or []
        if warnings:
            st.markdown("**Waarschuwingen**")
            for warning in warnings:
                st.write(f"- {warning}")

        unsupported_scope_note = report.get("unsupported_scope_note", "")
        if unsupported_scope_note:
            st.caption(unsupported_scope_note)

    return report
