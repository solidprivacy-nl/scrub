"""DOCX hygiene audit report helper for SolidPrivacy Scrub.

WP38 turns the WP37 hidden-content extraction output into a report-only audit
structure. It does not clean, remove, rewrite, block export, change reinsert
behavior, change UI, call AI/cloud services or persist document content.
"""

from __future__ import annotations

from typing import Any

from docx_hidden_content_extractor import inspect_docx_hidden_content

HIGH_RISK_FINDINGS = {
    "headers_detected",
    "footers_detected",
    "comments_detected",
    "tracked_changes_detected",
}

SEVERITY_ORDER = {
    "none": 0,
    "low": 1,
    "medium": 2,
    "high": 3,
}


FINDING_COPY = {
    "headers_detected": {
        "title": "DOCX headers detected",
        "risk": "Headers can contain names, matter numbers, document labels or other confidential context outside normal body text.",
        "recommended_action": "Review header content before sharing or exporting the document.",
    },
    "footers_detected": {
        "title": "DOCX footers detected",
        "risk": "Footers can contain page labels, matter numbers, initials or other confidential context outside normal body text.",
        "recommended_action": "Review footer content before sharing or exporting the document.",
    },
    "comments_detected": {
        "title": "DOCX comments or person metadata detected",
        "risk": "Comments and margin notes can contain reviewer identities, strategy, client references or other sensitive values.",
        "recommended_action": "Review comments and comment metadata before sharing or exporting the document.",
    },
    "tracked_changes_detected": {
        "title": "DOCX tracked-change markers detected",
        "risk": "Tracked changes can preserve deleted or moved sensitive text that users may overlook.",
        "recommended_action": "Review tracked changes before sharing or exporting the document.",
    },
}


def _safe_count(items: Any) -> int:
    return len(items) if isinstance(items, list) else 0


def _severity_for_detection(detected: dict[str, bool], valid_docx: bool) -> str:
    if not valid_docx:
        return "medium"
    if any(detected.get(flag, False) for flag in HIGH_RISK_FINDINGS):
        return "high"
    return "low"


def _finding(flag: str, count: int) -> dict[str, Any]:
    copy = FINDING_COPY[flag]
    return {
        "id": flag,
        "severity": "high",
        "count": count,
        "title": copy["title"],
        "risk": copy["risk"],
        "recommended_action": copy["recommended_action"],
    }


def build_docx_hygiene_audit_report(content: bytes) -> dict[str, Any]:
    """Build a report-only DOCX hygiene audit from DOCX bytes."""
    extraction = inspect_docx_hidden_content(content)
    detected = extraction.get("detected") or {}
    valid_docx = bool(extraction.get("valid_docx"))

    counts = {
        "headers": _safe_count(extraction.get("headers")),
        "footers": _safe_count(extraction.get("footers")),
        "comments": _safe_count(extraction.get("comments")),
        "tracked_changes": _safe_count(extraction.get("tracked_changes")),
    }

    findings: list[dict[str, Any]] = []
    if detected.get("headers_detected"):
        findings.append(_finding("headers_detected", counts["headers"]))
    if detected.get("footers_detected"):
        findings.append(_finding("footers_detected", counts["footers"]))
    if detected.get("comments_detected"):
        findings.append(_finding("comments_detected", counts["comments"]))
    if detected.get("tracked_changes_detected"):
        findings.append(_finding("tracked_changes_detected", counts["tracked_changes"]))

    if not valid_docx:
        findings.append({
            "id": "invalid_docx",
            "severity": "medium",
            "count": 1,
            "title": "DOCX could not be inspected",
            "risk": "The file could not be parsed as a valid DOCX package, so hidden-content risk is unknown.",
            "recommended_action": "Use a valid DOCX file before relying on this hygiene audit.",
        })

    severity = _severity_for_detection(detected, valid_docx)
    summary = {
        "severity": severity,
        "high_risk_findings": sum(1 for finding in findings if finding["severity"] == "high"),
        "finding_count": len(findings),
        "safe_to_claim_clean": False,
        "export_blocking_applied": False,
        "cleaning_applied": False,
        "message": (
            "High-risk DOCX hidden content was detected; review is required before sharing."
            if severity == "high"
            else "No WP37-supported hidden-content parts were detected, but this is not a clean-DOCX guarantee."
            if severity == "low"
            else "DOCX hygiene risk could not be fully assessed."
        ),
    }

    return {
        "document_type": "docx",
        "audit_type": "docx_hygiene_audit",
        "synthetic_safe_structure": True,
        "local_only": True,
        "ai_processing": False,
        "cloud_processing": False,
        "report_only": True,
        "extraction_only": True,
        "cleaning_applied": False,
        "export_blocking": False,
        "export_semantics_changed": False,
        "valid_docx": valid_docx,
        "validation_issues": extraction.get("validation_issues", []),
        "summary": summary,
        "detected": detected,
        "counts": counts,
        "findings": findings,
        "warnings": extraction.get("warnings", []),
        "recommended_next_step": "WP39 — Clean DOCX export policy",
        "unsupported_scope_note": (
            "This report is based on WP37-supported parts only. Footnotes, endnotes, metadata, custom XML, text boxes, shapes and embedded objects remain future work."
        ),
        "source_extraction": extraction,
    }


def render_docx_hygiene_audit_markdown(report: dict[str, Any]) -> str:
    """Render a compact Markdown version of a DOCX hygiene audit report."""
    summary = report.get("summary", {})
    lines = [
        "# DOCX hygiene audit report",
        "",
        f"Severity: `{summary.get('severity', 'unknown')}`",
        f"Report-only: `{str(report.get('report_only')).lower()}`",
        f"Cleaning applied: `{str(report.get('cleaning_applied')).lower()}`",
        f"Export blocking: `{str(report.get('export_blocking')).lower()}`",
        "",
        str(summary.get("message", "")),
        "",
        "## Findings",
    ]
    findings = report.get("findings") or []
    if not findings:
        lines.append("- No WP37-supported hidden-content findings detected.")
    else:
        for finding in findings:
            lines.append(
                f"- **{finding['title']}** — severity `{finding['severity']}`, count `{finding['count']}`. {finding['recommended_action']}"
            )

    lines.extend([
        "",
        "## Boundaries",
        "- No DOCX cleaner was applied.",
        "- No comments or tracked changes were removed.",
        "- No export blocking was applied.",
        "- No Streamlit UI behavior was changed by this report helper.",
        "- This is not a clean-DOCX guarantee.",
    ])
    return "\n".join(lines) + "\n"
