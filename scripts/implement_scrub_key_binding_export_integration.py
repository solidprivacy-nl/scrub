from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match in {path}; found {count}: {old[:80]!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


def prepend_once(path: str, marker: str, block: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if marker not in text:
        target.write_text(block + text, encoding="utf-8")


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def patch_document_tools() -> None:
    replace_once(
        "document_tools.py",
        "import csv\nimport re\n",
        "import csv\nimport re\n\nfrom scrub_key_binding import build_bound_placeholder\n",
    )
    replace_once(
        "document_tools.py",
        '''def placeholder_for_entity(entity_type: str, count: int) -> str:\n    label = PLACEHOLDER_LABELS.get(entity_type, entity_type)\n    return f"[{label}_{count:02d}]"\n\n\ndef build_placeholder_replacements(text, analyze_results):\n    """Build stable placeholder suggestions from Presidio results."""\n''',
        '''def placeholder_for_entity(\n    entity_type: str,\n    count: int,\n    document_binding_id: str | None = None,\n) -> str:\n    label = PLACEHOLDER_LABELS.get(entity_type, entity_type)\n    if document_binding_id:\n        return build_bound_placeholder(label, count, document_binding_id)\n    return f"[{label}_{count:02d}]"\n\n\ndef build_placeholder_replacements(\n    text,\n    analyze_results,\n    document_binding_id: str | None = None,\n):\n    """Build stable placeholder suggestions from Presidio results.\n\n    ``document_binding_id`` is optional for backwards-compatible helper use. The\n    anonymization/export flow supplies it so newly exported artifacts are bound.\n    """\n''',
    )
    replace_once(
        "document_tools.py",
        "        placeholder = placeholder_for_entity(entity_type, counters[entity_type])\n",
        "        placeholder = placeholder_for_entity(\n            entity_type, counters[entity_type], document_binding_id\n        )\n",
    )


def patch_manual_mask_entry() -> None:
    replace_once(
        "manual_mask_entry.py",
        "import re\n\n\nMANUAL_MASK_TYPE_TO_ENTITY_TYPE",
        "import re\n\nfrom scrub_key_binding import build_bound_placeholder, parse_bound_placeholder\n\n\nMANUAL_MASK_TYPE_TO_ENTITY_TYPE",
    )
    replace_once(
        "manual_mask_entry.py",
        '''def build_manual_placeholder(manual_type: str | None, existing_rows: Iterable[dict[str, Any]] | Any | None = None) -> str:\n    """Build a stable placeholder such as ``[PERSOON_HANDMATIG_01]``."""\n\n    entity_type = manual_type_to_entity_type(manual_type)\n    prefix = _ENTITY_TYPE_TO_PLACEHOLDER_PREFIX.get(entity_type, "WAARDE")\n    pattern = re.compile(rf"^\\[{re.escape(prefix)}_HANDMATIG_(\\d+)\\]$")\n    max_seen = 0\n    for row in _row_dicts(existing_rows):\n        match = pattern.match(str(row.get("replace_with", "")).strip())\n        if match:\n            max_seen = max(max_seen, int(match.group(1)))\n    return f"[{prefix}_HANDMATIG_{max_seen + 1:02d}]"\n''',
        '''def build_manual_placeholder(\n    manual_type: str | None,\n    existing_rows: Iterable[dict[str, Any]] | Any | None = None,\n    document_binding_id: str | None = None,\n) -> str:\n    """Build a stable legacy or document-bound manual placeholder."""\n\n    entity_type = manual_type_to_entity_type(manual_type)\n    prefix = _ENTITY_TYPE_TO_PLACEHOLDER_PREFIX.get(entity_type, "WAARDE")\n    legacy_pattern = re.compile(rf"^\\[{re.escape(prefix)}_HANDMATIG_(\\d+)\\]$")\n    max_seen = 0\n    for row in _row_dicts(existing_rows):\n        replacement = str(row.get("replace_with", "")).strip()\n        parsed = parse_bound_placeholder(replacement)\n        if (\n            document_binding_id\n            and parsed\n            and parsed["manual"] is True\n            and parsed["entity_label"] == prefix\n            and parsed["document_binding_id"] == document_binding_id\n        ):\n            max_seen = max(max_seen, int(parsed["index"]))\n            continue\n        match = legacy_pattern.match(replacement)\n        if match:\n            max_seen = max(max_seen, int(match.group(1)))\n\n    next_index = max_seen + 1\n    if document_binding_id:\n        return build_bound_placeholder(prefix, next_index, document_binding_id, manual=True)\n    return f"[{prefix}_HANDMATIG_{next_index:02d}]"\n''',
    )
    replace_once(
        "manual_mask_entry.py",
        '''def build_manual_mask_row(\n    *,\n    find_text: Any,\n    manual_type: str | None = None,\n    replace_with: Any = None,\n    existing_rows: Iterable[dict[str, Any]] | Any | None = None,\n) -> dict[str, Any]:\n''',
        '''def build_manual_mask_row(\n    *,\n    find_text: Any,\n    manual_type: str | None = None,\n    replace_with: Any = None,\n    existing_rows: Iterable[dict[str, Any]] | Any | None = None,\n    document_binding_id: str | None = None,\n) -> dict[str, Any]:\n''',
    )
    replace_once(
        "manual_mask_entry.py",
        "    replacement = normalise_manual_mask_value(replace_with) or build_manual_placeholder(manual_type, existing_rows)\n",
        "    replacement = normalise_manual_mask_value(replace_with) or build_manual_placeholder(\n        manual_type, existing_rows, document_binding_id\n    )\n",
    )


def create_export_helper() -> None:
    write(
        "scrub_key_bound_export.py",
        '''"""Pure helpers for creating document-bound Scrub Key export artifacts.\n\nThe helpers keep Streamlit/session details outside the binding model. They do not\nmodify arbitrary custom replacement values: only recognised legacy or bound\nplaceholder tokens are losslessly rebound to the active document ID.\n"""\n\nfrom __future__ import annotations\n\nimport re\nfrom collections.abc import Mapping\nfrom typing import Any\n\nfrom scrub_key import build_scrub_key\nfrom scrub_key_binding import (\n    BINDING_VERSION,\n    BOUND_SCHEMA_VERSION,\n    MAPPING_DIGEST_ALGORITHM,\n    build_bound_placeholder,\n    compute_mapping_digest,\n    generate_document_binding_id,\n    parse_bound_placeholder,\n    validate_document_binding_id,\n)\n\nSESSION_BINDING_IDS_KEY = "document_binding_ids"\n\n_LEGACY_MANUAL_PLACEHOLDER_RE = re.compile(\n    r"^\\[(?P<label>[A-Z][A-Z0-9_]*?)_HANDMATIG_(?P<index>\\d{2,})\\]$"\n)\n_LEGACY_AUTOMATIC_PLACEHOLDER_RE = re.compile(\n    r"^\\[(?P<label>[A-Z][A-Z0-9_]*?)_(?P<index>\\d{2,})\\]$"\n)\n\n\ndef document_binding_id_for_scope(\n    state: Any,\n    scope_key: Any,\n    *,\n    random_bytes: bytes | None = None,\n) -> str:\n    """Return one stable local binding ID for a source-text scope."""\n\n    if not hasattr(state, "get") or not hasattr(state, "__setitem__"):\n        raise TypeError("state must provide mapping-style get and item assignment.")\n    scope = str(scope_key or "").strip()\n    if not scope:\n        raise ValueError("scope_key cannot be empty.")\n\n    raw_mapping = state.get(SESSION_BINDING_IDS_KEY, {})\n    mapping = dict(raw_mapping) if isinstance(raw_mapping, Mapping) else {}\n    existing = str(mapping.get(scope, "")).strip()\n    if existing and not validate_document_binding_id(existing):\n        return existing\n\n    binding_id = generate_document_binding_id(random_bytes=random_bytes)\n    mapping[scope] = binding_id\n    state[SESSION_BINDING_IDS_KEY] = mapping\n    return binding_id\n\n\ndef bind_existing_placeholder(value: Any, document_binding_id: str) -> str | None:\n    """Rebind a recognised placeholder token; leave free replacement text alone."""\n\n    token = str(value or "").strip()\n    parsed = parse_bound_placeholder(token)\n    if parsed is not None:\n        return build_bound_placeholder(\n            parsed["entity_label"],\n            parsed["index"],\n            document_binding_id,\n            manual=parsed["manual"],\n        )\n\n    manual_match = _LEGACY_MANUAL_PLACEHOLDER_RE.fullmatch(token)\n    if manual_match is not None:\n        return build_bound_placeholder(\n            manual_match.group("label"),\n            int(manual_match.group("index")),\n            document_binding_id,\n            manual=True,\n        )\n\n    automatic_match = _LEGACY_AUTOMATIC_PLACEHOLDER_RE.fullmatch(token)\n    if automatic_match is not None:\n        return build_bound_placeholder(\n            automatic_match.group("label"),\n            int(automatic_match.group("index")),\n            document_binding_id,\n        )\n    return None\n\n\ndef build_bound_scrub_key(\n    rows: Any,\n    *,\n    document_binding_id: str,\n    document_label: str | None = None,\n) -> dict[str, Any]:\n    """Build a schema-1.1 key from current reviewed export rows."""\n\n    binding_errors = validate_document_binding_id(document_binding_id)\n    if binding_errors:\n        raise ValueError(binding_errors[0])\n\n    scrub_key = build_scrub_key(rows, document_label=document_label)\n    scrub_key["schema_version"] = BOUND_SCHEMA_VERSION\n    scrub_key["binding_version"] = BINDING_VERSION\n    scrub_key["document_binding_id"] = document_binding_id\n    scrub_key["mapping_digest_algorithm"] = MAPPING_DIGEST_ALGORITHM\n    scrub_key["mapping_digest"] = compute_mapping_digest(scrub_key)\n    return scrub_key\n''',
    )


def patch_app() -> None:
    replace_once(
        "presidio_streamlit.py",
        "from __future__ import annotations\n\nimport ast\n",
        "from __future__ import annotations\n\nfrom collections import Counter\nimport ast\n",
    )
    replace_once(
        "presidio_streamlit.py",
        '''    build_placeholder_replacements,\n    apply_replacements_to_text,\n''',
        '''    build_placeholder_replacements,\n    placeholder_for_entity,\n    apply_replacements_to_text,\n''',
    )
    replace_once(
        "presidio_streamlit.py",
        '''from scrub_key import (\n    build_scrub_key as build_export_scrub_key,\n    scrub_key_to_json as export_key_json,\n    validate_scrub_key as validate_export_scrub_key,\n)\n''',
        '''from scrub_key import scrub_key_to_json as export_key_json\nfrom scrub_key_binding import validate_bound_scrub_key\nfrom scrub_key_bound_export import (\n    bind_existing_placeholder,\n    build_bound_scrub_key,\n    document_binding_id_for_scope,\n)\n''',
    )
    replace_once(
        "presidio_streamlit.py",
        '''    if st_operator not in ("highlight", "synthesize"):\n        _, report_rows = build_placeholder_replacements(st_text, st_analyze_results)\n''',
        '''    if st_operator not in ("highlight", "synthesize"):\n        document_scope_key = manual_mask_document_key(st_text)\n        document_binding_id = document_binding_id_for_scope(\n            st.session_state, document_scope_key\n        )\n        _, report_rows = build_placeholder_replacements(\n            st_text,\n            st_analyze_results,\n            document_binding_id=document_binding_id,\n        )\n''',
    )
    replace_once(
        "presidio_streamlit.py",
        '''            replace_with = str(row.get("replace_with", "")).strip()\n            if not find_text or not replace_with:\n''',
        '''            replace_with = str(row.get("replace_with", "")).strip()\n            rebound_placeholder = bind_existing_placeholder(\n                replace_with, document_binding_id\n            )\n            if rebound_placeholder is not None:\n                replace_with = rebound_placeholder\n            if not find_text or not replace_with:\n''',
    )
    replace_once(
        "presidio_streamlit.py",
        '''        for candidate in candidate_rows:\n            find_text = str(candidate.get("text", "")).strip()\n''',
        '''        placeholder_counts = Counter(\n            row.get("entity_type", "") for row in report_rows\n        )\n        for candidate in candidate_rows:\n            find_text = str(candidate.get("text", "")).strip()\n''',
    )
    replace_once(
        "presidio_streamlit.py",
        '''            score = candidate.get("score", None)\n            review_status = review_status_for_source("candidate", entity_type, score)\n''',
        '''            score = candidate.get("score", None)\n            placeholder_counts[entity_type] += 1\n            candidate_placeholder = placeholder_for_entity(\n                entity_type,\n                placeholder_counts[entity_type],\n                document_binding_id,\n            )\n            review_status = review_status_for_source("candidate", entity_type, score)\n''',
    )
    replace_once(
        "presidio_streamlit.py",
        '''                    "replace_with": candidate.get("placeholder", "<MOGELIJKE_REFERENTIE>"),\n''',
        '''                    "replace_with": candidate_placeholder,\n''',
    )
    replace_once(
        "presidio_streamlit.py",
        "        manual_mask_key = manual_mask_document_key(st_text)\n",
        "        manual_mask_key = document_scope_key\n",
    )
    replace_once(
        "presidio_streamlit.py",
        '''        for manual_row in manual_mask_rows.get(manual_mask_key, []):\n            manual_find_text = str(manual_row.get("find", "")).strip()\n            if manual_find_text and manual_find_text not in seen_find_values:\n                default_editor_rows.append(manual_row)\n''',
        '''        for manual_row in manual_mask_rows.get(manual_mask_key, []):\n            manual_row = dict(manual_row)\n            manual_replacement = bind_existing_placeholder(\n                manual_row.get("replace_with", ""), document_binding_id\n            )\n            if manual_replacement is not None:\n                manual_row["replace_with"] = manual_replacement\n            manual_find_text = str(manual_row.get("find", "")).strip()\n            if manual_find_text and manual_find_text not in seen_find_values:\n                default_editor_rows.append(manual_row)\n''',
    )
    replace_once(
        "presidio_streamlit.py",
        '''                manual_placeholder = build_manual_placeholder(\n                    manual_type_label,\n                    replacement_editor_df,\n                )\n''',
        '''                manual_placeholder = build_manual_placeholder(\n                    manual_type_label,\n                    replacement_editor_df,\n                    document_binding_id,\n                )\n''',
    )
    replace_once(
        "presidio_streamlit.py",
        '''                    replace_with=manual_replace_with,\n                    existing_rows=replacement_editor_df,\n                )\n''',
        '''                    replace_with=manual_replace_with,\n                    existing_rows=replacement_editor_df,\n                    document_binding_id=document_binding_id,\n                )\n''',
    )
    replace_once(
        "presidio_streamlit.py",
        '''            scrub_key = build_export_scrub_key(scrub_key_rows)\n            scrub_key_issues = validate_export_scrub_key(scrub_key)\n            if scrub_key_issues:\n                st.warning("Scrub Key kan nog niet betrouwbaar worden geëxporteerd: " + "; ".join(scrub_key_issues[:3]))\n''',
        '''            scrub_key = build_bound_scrub_key(\n                scrub_key_rows,\n                document_binding_id=document_binding_id,\n            )\n            scrub_key_validation = validate_bound_scrub_key(scrub_key)\n            scrub_key_issues = scrub_key_validation.get("errors", [])\n            if scrub_key_issues:\n                st.warning(\n                    "Scrub Key kan nog niet betrouwbaar worden geëxporteerd. "\n                    "Alle geselecteerde vervangingen moeten documentgebonden placeholders zijn; "\n                    "vrije aangepaste vervangtekst blijft wel in de documentexport staan. "\n                    + "; ".join(scrub_key_issues[:3])\n                )\n''',
    )


def create_tests() -> None:
    write(
        "tests/test_scrub_key_bound_export.py",
        '''from __future__ import annotations\n\nfrom copy import deepcopy\nfrom types import SimpleNamespace\n\nfrom document_tools import build_placeholder_replacements, placeholder_for_entity\nfrom manual_mask_entry import build_manual_mask_row, build_manual_placeholder\nfrom scrub_key_binding import parse_bound_placeholder, validate_bound_scrub_key\nfrom scrub_key_bound_export import (\n    bind_existing_placeholder,\n    build_bound_scrub_key,\n    document_binding_id_for_scope,\n)\n\n\nBINDING_ID = "BK7M4Q2XR5TD3W6YZ"\nOTHER_BINDING_ID = "BABCDEFGHIJKLMNOP"\n\n\ndef reviewed_rows() -> list[dict]:\n    return [\n        {\n            "find": "BETROKKENE-TEST-A",\n            "replace_with": f"[PERSOON_{BINDING_ID}_01]",\n            "entity_type": "PERSON",\n            "type_label": "Naam / persoon",\n            "source": "detected",\n            "review_status": "auto",\n            "include": True,\n            "timestamp": "2026-07-27T19:00:00Z",\n        },\n        {\n            "find": "DOSSIER-TEST-2026-001",\n            "replace_with": f"[DOSSIERNUMMER_{BINDING_ID}_HANDMATIG_01]",\n            "entity_type": "NL_DOSSIER_NUMBER",\n            "type_label": "Dossiernummer",\n            "source": "manual",\n            "review_status": "manual",\n            "include": True,\n            "timestamp": "2026-07-27T19:00:00Z",\n        },\n    ]\n\n\ndef test_document_binding_id_is_stable_per_scope_and_local() -> None:\n    state: dict = {}\n    first = document_binding_id_for_scope(\n        state, "scope-a", random_bytes=b"0123456789"\n    )\n    second = document_binding_id_for_scope(\n        state, "scope-a", random_bytes=b"abcdefghij"\n    )\n    other = document_binding_id_for_scope(\n        state, "scope-b", random_bytes=b"abcdefghij"\n    )\n    assert first == second\n    assert other != first\n    assert parse_bound_placeholder(f"[PERSOON_{first}_01]") is not None\n\n\ndef test_existing_legacy_and_bound_placeholders_rebind_losslessly() -> None:\n    assert bind_existing_placeholder("[PERSOON_01]", BINDING_ID) == (\n        f"[PERSOON_{BINDING_ID}_01]"\n    )\n    assert bind_existing_placeholder("[PERSOON_HANDMATIG_02]", BINDING_ID) == (\n        f"[PERSOON_{BINDING_ID}_HANDMATIG_02]"\n    )\n    assert bind_existing_placeholder(\n        f"[IP_ADRES_{OTHER_BINDING_ID}_03]", BINDING_ID\n    ) == f"[IP_ADRES_{BINDING_ID}_03]"\n    assert bind_existing_placeholder("Synthetisch pseudoniem", BINDING_ID) is None\n\n\ndef test_document_tools_keep_legacy_default_and_support_bound_placeholders() -> None:\n    assert placeholder_for_entity("PERSON", 1) == "[PERSOON_01]"\n    assert placeholder_for_entity("PERSON", 1, BINDING_ID) == (\n        f"[PERSOON_{BINDING_ID}_01]"\n    )\n    result = SimpleNamespace(start=0, end=17, entity_type="PERSON", score=0.99)\n    replacements, report = build_placeholder_replacements(\n        "BETROKKENE-TEST-A", [result], document_binding_id=BINDING_ID\n    )\n    assert replacements == {\n        "BETROKKENE-TEST-A": f"[PERSOON_{BINDING_ID}_01]"\n    }\n    assert report[0]["placeholder"] == f"[PERSOON_{BINDING_ID}_01]"\n\n\ndef test_manual_helper_keeps_legacy_default_and_supports_bound_placeholders() -> None:\n    assert build_manual_placeholder("Persoon") == "[PERSOON_HANDMATIG_01]"\n    assert build_manual_placeholder(\n        "Persoon", document_binding_id=BINDING_ID\n    ) == f"[PERSOON_{BINDING_ID}_HANDMATIG_01]"\n    row = build_manual_mask_row(\n        find_text="BETROKKENE-TEST-A",\n        manual_type="Persoon",\n        document_binding_id=BINDING_ID,\n    )\n    assert row["replace_with"] == f"[PERSOON_{BINDING_ID}_HANDMATIG_01]"\n\n\ndef test_bound_scrub_key_export_matches_schema_and_digest_contract() -> None:\n    rows = reviewed_rows()\n    original = deepcopy(rows)\n    key = build_bound_scrub_key(rows, document_binding_id=BINDING_ID)\n    validation = validate_bound_scrub_key(key)\n    assert rows == original\n    assert validation["ok"] is True\n    assert key["schema_version"] == "1.1"\n    assert key["binding_version"] == "1"\n    assert key["document_binding_id"] == BINDING_ID\n    assert key["mapping_digest_algorithm"] == "sha256"\n    assert len(key["mapping_digest"]) == 64\n\n\ndef test_custom_replacement_remains_unchanged_and_blocks_verified_key() -> None:\n    rows = reviewed_rows()\n    rows[0]["replace_with"] = "Synthetisch pseudoniem"\n    key = build_bound_scrub_key(rows, document_binding_id=BINDING_ID)\n    validation = validate_bound_scrub_key(key)\n    assert rows[0]["replace_with"] == "Synthetisch pseudoniem"\n    assert validation["ok"] is False\n    assert "invalid_bound_key" in validation["error_codes"]\n''',
    )
    write(
        "tests/test_mvp_scrub_key_binding_export_integration.py",
        '''from __future__ import annotations\n\nfrom pathlib import Path\n\n\nROOT = Path(__file__).resolve().parents[1]\nAPP = (ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")\nDOCUMENT_TOOLS = (ROOT / "document_tools.py").read_text(encoding="utf-8")\nMANUAL = (ROOT / "manual_mask_entry.py").read_text(encoding="utf-8")\nHELPER = (ROOT / "scrub_key_bound_export.py").read_text(encoding="utf-8")\n\n\ndef test_app_creates_one_binding_id_before_default_replacements() -> None:\n    assert "document_binding_id_for_scope(" in APP\n    assert "document_scope_key = manual_mask_document_key(st_text)" in APP\n    assert "document_binding_id=document_binding_id" in APP\n    assert "build_placeholder_replacements(" in APP\n\n\ndef test_automatic_candidate_remembered_and_manual_paths_are_binding_aware() -> None:\n    assert "placeholder_for_entity(" in APP\n    assert "placeholder_counts = Counter(" in APP\n    assert "bind_existing_placeholder(" in APP\n    assert "build_manual_placeholder(" in APP\n    assert "document_binding_id,\n                )" in APP\n    assert "document_binding_id=document_binding_id" in APP\n    assert "build_bound_placeholder" in DOCUMENT_TOOLS\n    assert "build_bound_placeholder" in MANUAL\n\n\ndef test_bound_key_builder_and_validator_replace_legacy_export_builder() -> None:\n    assert "build_bound_scrub_key(" in APP\n    assert "validate_bound_scrub_key(" in APP\n    assert "build_scrub_key as build_export_scrub_key" not in APP\n    assert "validate_scrub_key as validate_export_scrub_key" not in APP\n    assert 'file_name="solidprivacy_scrub_key.json"' in APP\n    assert 'mime="application/json"' in APP\n\n\ndef test_free_custom_replacement_is_not_silently_rewritten() -> None:\n    assert "return None" in HELPER\n    assert "vrije aangepaste vervangtekst blijft wel in de documentexport staan" in APP\n    assert "Alle geselecteerde vervangingen moeten documentgebonden placeholders zijn" in APP\n\n\ndef test_export_integration_adds_no_new_confirmation_gate() -> None:\n    forbidden = [\n        "Bevestig documentbinding",\n        "Valideer documentbinding",\n        "Genereer gebonden Scrub Key",\n        "ack_document_binding",\n    ]\n    for marker in forbidden:\n        assert marker not in APP\n\n\ndef test_document_export_names_and_mime_types_remain_stable() -> None:\n    for marker in [\n        'file_name="opgeschoonde_tekst.txt"',\n        'docx_filename = "opgeschoonde_tekst.docx"',\n        'file_name="opgeschoonde_tekst.pdf"',\n        'mime="text/plain"',\n        'mime="application/pdf"',\n        'mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"',\n    ]:\n        assert marker in APP\n''',
    )


def update_governance() -> None:
    timestamp = "2026-07-27 21:45 Europe/Amsterdam"
    changelog_entry = f'''## {timestamp} — SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION\n\nStatus: implemented; targeted validation pending.\n\nPurpose:\n- Create document-bound placeholders and schema-1.1 Scrub Keys in the anonymization/export flow before reinsert enforcement.\n\nImplementation:\n- One locally random binding ID is retained per active source-text scope.\n- Automatic, candidate and default manual placeholders use the frozen bound grammar.\n- Legacy or already-bound placeholder tokens from remembered/manual rows are losslessly rebound to the active document.\n- Arbitrary custom replacement text is never silently rewritten.\n- A schema-1.1 Scrub Key with binding metadata and canonical SHA-256 mapping digest is exported only when every included mapping is bound.\n- An unbound custom replacement keeps working in document exports but visibly blocks verified Scrub Key download.\n\nIntentionally not changed:\n- reinsert validation/enforcement;\n- user-chosen custom replacement text;\n- document export filenames and MIME types;\n- review controls or legal context;\n- recognizers, thresholds, cloud, AI, OCR, signing or secret storage.\n\nNext:\n- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`.\n\n---\n\n'''
    prepend_once("CHANGELOG.md", "SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION", changelog_entry)

    workpackages_entry = f'''## {timestamp} — SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION\n\nStatus: implemented; targeted validation pending.\n\nSummary:\n- Bound placeholder and schema-1.1 key creation is integrated into anonymization/export.\n- Custom replacement text is preserved and cannot be silently represented as a verified bound mapping.\n- Reinsert enforcement remains the active next package.\n\nNext recommended step:\n- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`.\n\n'''
    prepend_once("WORKPACKAGES.md", f"{timestamp} — SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION", workpackages_entry)

    release_entry = '''## 2026-07-27 — Document en Scrub Key worden aan elkaar gekoppeld\n\n- Nieuwe standaardplaceholders bevatten een niet-gevoelige documentcode.\n- De bijbehorende Scrub Key bevat dezelfde code en een controlewaarde tegen onbedoelde wijzigingen.\n- Vrij aangepaste vervangtekst blijft ongewijzigd, maar kan niet als geverifieerde documentgebonden Scrub Key worden gedownload.\n- Bestandsnamen, documentformaten en de bestaande reviewstappen blijven gelijk.\n\n---\n\n'''
    prepend_once("RELEASE_NOTES.md", "2026-07-27 — Document en Scrub Key worden aan elkaar gekoppeld", release_entry)

    handover = f'''# Handover — SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION\n\nRepository worked in: solidprivacy-nl/scrub\n\n## Workpackage title\n\nSCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION\n\n## Status\n\nImplemented; targeted validation pending.\n\n## Files added\n\n- `scrub_key_bound_export.py`\n- `tests/test_scrub_key_bound_export.py`\n- `tests/test_mvp_scrub_key_binding_export_integration.py`\n- `workpackage_claims/scrub_wp_mvp_scrub_key_binding_export_integration.md`\n- `handover/workpackages/20260727_2145_mvp_scrub_key_binding_export_integration.md`\n\n## Files changed\n\n- `document_tools.py`\n- `manual_mask_entry.py`\n- `presidio_streamlit.py`\n- `CHANGELOG.md`\n- `WORKPACKAGES.md`\n- `RELEASE_NOTES.md`\n- `ROADMAP.md`\n- `RISK_REGISTER.md`\n- `DECISION_LOG.md`\n\n## Tests\n\n- Stable per-scope binding ID.\n- Automatic, candidate, remembered and manual bound placeholders.\n- Schema-1.1 key and canonical digest validation.\n- Custom replacement preservation and verified-key blocking.\n- Stable document filenames/MIME types and no new confirmation gates.\n- Full repository regression pending PR validation.\n\n## Validation\n\n- Targeted validation: pending.\n- GitHub Actions: pending PR validation.\n- Hugging Face sync: pending after merge.\n- App verification: required after export and reinsert integration are both deployed.\n\n## Notes / risks\n\n- Reinsert does not yet enforce binding; that remains the immediate next package.\n- Legacy v1.0 keys remain supported only as explicit unbound compatibility after reinsert integration.\n- Mapping digest is not malicious-tampering authenticity.\n- Human review remains mandatory; production readiness remains false.\n\n## Next recommended step\n\n- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`.\n'''
    write("handover/workpackages/20260727_2145_mvp_scrub_key_binding_export_integration.md", handover)

    claim_path = ROOT / "workpackage_claims/scrub_wp_mvp_scrub_key_binding_export_integration.md"
    claim = claim_path.read_text(encoding="utf-8")
    claim = claim.replace("Status: in_progress", "Status: implemented; targeted validation pending", 1)
    claim += '''\nImplementation result:\n- Bound placeholder defaults and schema-1.1 key export integrated.\n- Custom replacement text remains unchanged and blocks verified key export.\n- Reinsert enforcement remains out of scope.\n- Handover: `handover/workpackages/20260727_2145_mvp_scrub_key_binding_export_integration.md`.\n'''
    claim_path.write_text(claim, encoding="utf-8")

    roadmap = ROOT / "ROADMAP.md"
    road_text = roadmap.read_text(encoding="utf-8")
    road_text = road_text.replace(
        "Last roadmap strategy update: 2026-07-27 — the pure binding model is implemented and isolated; bound placeholder and Scrub Key export integration is now active before reinsert enforcement.",
        "Last roadmap strategy update: 2026-07-27 — bound placeholder and Scrub Key export integration is implemented; fail-closed reinsert enforcement is now active next.",
        1,
    )
    road_text = road_text.replace(
        "9. SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION — active\n10. SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION",
        "9. SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION — implemented\n10. SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION — active",
        1,
    )
    roadmap.write_text(road_text, encoding="utf-8")

    risk = ROOT / "RISK_REGISTER.md"
    risk_text = risk.read_text(encoding="utf-8")
    old = "The pure model now implements those contracts without changing current export or reinsert behavior. Risk remains open until bound placeholders and keys are created during export and binding validation gates replacement during reinsert."
    new = "The pure model implements those contracts, and anonymization/export now creates bound placeholders plus schema-1.1 keys when all selected mappings are bound. Arbitrary custom replacement text is preserved but visibly blocks verified key export. Risk remains open until binding validation gates replacement during reinsert."
    if old in risk_text:
        risk_text = risk_text.replace(old, new, 1)
    risk.write_text(risk_text, encoding="utf-8")

    decision = ROOT / "DECISION_LOG.md"
    decision_text = decision.read_text(encoding="utf-8")
    marker = "D036 — Preserve custom replacement text and fail verified key export rather than silently rewriting it"
    if marker not in decision_text:
        decision_block = f'''## 2026-07-27 — {marker}\n\nStatus: accepted export-integration decision\n\nDecision:\n\n```text\nGenerate document-bound placeholders by default. Rebind only recognised placeholder tokens. Never silently replace arbitrary user-chosen replacement text with a placeholder. When any included mapping remains unbound, keep the document export behavior but block schema-1.1 Scrub Key download with a visible validation warning.\n```\n\nReason:\n\n- Review choices remain source of truth.\n- Silent rewriting would change legal/readability semantics and user intent.\n- A bound key must not claim verified document matching for an unbound mapping.\n- Fail-visible key export is safer than a false binding claim.\n\n---\n\n'''
        decision.write_text(decision_block + decision_text, encoding="utf-8")


def main() -> None:
    patch_document_tools()
    patch_manual_mask_entry()
    create_export_helper()
    patch_app()
    create_tests()
    update_governance()
    print("Scrub Key binding export integration applied.")


if __name__ == "__main__":
    main()
