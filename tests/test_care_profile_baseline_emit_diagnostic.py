"""Temporary CI diagnostic for emitting the deterministic care baseline.

This file is removed after the machine-readable report is committed.
"""

import base64
import gzip
import json

from care_profile_baseline import build_current_care_baseline


def test_emit_compact_care_baseline_for_capture():
    report = build_current_care_baseline()
    compact_cases = []
    for case in report["cases"]:
        compact_cases.append(
            {
                "id": case["id"],
                "name": case["name"],
                "sector": case["sector"],
                "document_type": case["document_type"],
                "expected_value_count": case["expected_value_count"],
                "found_value_count": case["found_value_count"],
                "expectations": case["expectations"],
                "preserve_overlaps": case["preserve_overlaps"],
            }
        )
    compact_report = {
        key: value
        for key, value in report.items()
        if key != "cases"
    }
    compact_report["cases"] = compact_cases
    payload = gzip.compress(
        json.dumps(compact_report, ensure_ascii=False, sort_keys=True).encode("utf-8")
    )
    encoded = base64.b64encode(payload).decode("ascii")
    print("CARE_BASELINE_GZIP_B64_BEGIN")
    print(encoded)
    print("CARE_BASELINE_GZIP_B64_END")
    raise AssertionError("intentional diagnostic emission; remove after capture")
