from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match in {path}, found {count}: {old[:100]!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


replace_once(
    "processed_text_selection_component.py",
    "    non_mutating_spike: bool = False,\n) -> dict[str, Any]:",
    "    non_mutating_spike: bool = True,\n) -> dict[str, Any]:",
)
replace_once(
    "processed_text_selection_component.py",
    "        non_mutating_spike=non_mutating_spike,\n    )\n    value = component(**args, key=key, default=None)",
    "        non_mutating_spike=non_mutating_spike,\n    )\n    value = component(**args, key=key, default=None)",
)
# Production renderer must opt into mutation-capable transport explicitly.
replace_once(
    "side_by_side_review_panel_ui.py",
    "                key=f\"processed_text_selection_{document_scope_key}\",\n            )",
    "                key=f\"processed_text_selection_{document_scope_key}\",\n                non_mutating_spike=False,\n            )",
)

replace_once(
    "tests/test_processed_text_selection_integration.py",
    'BINDING = "ABCDEFGHIJKLMNOP"',
    'BINDING = "BABCDEFGHIJKLMNOP"',
)
replace_once(
    "tests/test_processed_text_selection_integration.py",
    '    event = inspect_event(text="Noor")',
    '    event = inspect_event(text="Zorg")',
)

replace_once(
    "tests/test_processed_text_selection_component_spike.py",
    '''def test_production_ui_does_not_import_or_call_the_spike():
    for path in (ROOT / "presidio_streamlit.py", ROOT / "side_by_side_review_panel_ui.py"):
        source = path.read_text(encoding="utf-8")
        assert "processed_text_selection_component" not in source
        assert "render_processed_text_selection_component_spike" not in source
''',
    '''def test_production_ui_uses_production_entry_point_and_not_spike_alias():
    side_source = (ROOT / "side_by_side_review_panel_ui.py").read_text(encoding="utf-8")
    app_source = (ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")
    assert "render_processed_text_selection_component" in side_source
    assert "non_mutating_spike=False" in side_source
    assert "render_processed_text_selection_component_spike" not in side_source
    assert "render_processed_text_selection_component_spike" not in app_source
    assert "handle_selection_component_event" in app_source
''',
)

replace_once(
    "tests/test_review_copy_polish_ui.py",
    '''    assert "Download veilig" in rendered
    assert "Twijfel je over een waarde?" in rendered
    assert "Open de vervangtabel of Meer controleopties hieronder." in rendered
    assert "Deze vergelijking wijzigt zelf niets." in rendered
''',
    '''    assert "Selecteer rechts een gemiste waarde" in rendered
    assert "Twijfel je over een waarde?" in rendered
    assert "Elke toevoeging blijft zichtbaar en aanpasbaar in de vervangtabel." in rendered
    assert "mutation_allowed\": False" in rendered
''',
)
replace_once(
    "tests/test_review_copy_polish_ui.py",
    '''        "contextmenu",
        "right click",
        "click-to-mark",
''',
    '''        "cloud telemetry",
        "external component asset",
        "click-to-mark",
''',
)

replace_once(
    "tests/test_review_surface_simplification_implementation.py",
    '''    assert "Controleer links de brontekst en rechts de verwerkte tekst." in SIDE_BY_SIDE_TEXT
    assert "Deze vergelijking wijzigt zelf niets." in SIDE_BY_SIDE_TEXT
''',
    '''    assert "Controleer links de brontekst en rechts de verwerkte tekst." in SIDE_BY_SIDE_TEXT
    assert "Selecteer rechts een gemiste waarde" in SIDE_BY_SIDE_TEXT
    assert '"mutation_allowed": False' in SIDE_BY_SIDE_TEXT
''',
)

replace_once(
    "tests/test_side_by_side_review_consolidation_dutch_sample.py",
    '''    assert "Twijfel je over een waarde? Open de vervangtabel of Meer controleopties hieronder." in text
    assert "Deze vergelijking wijzigt zelf niets." in text
''',
    '''    assert "Twijfel je over een waarde? Selecteer die rechts" in text
    assert "Elke toevoeging blijft zichtbaar en aanpasbaar in de vervangtabel." in text
    assert '"mutation_allowed": False' in text
''',
)

replace_once(
    "tests/test_side_by_side_review_ui_patch.py",
    '''        "Download veilig",
        "Brontekst",
        "Verwerkte tekst",
        "Markeringen tonen",
        "Geel = vervangen of gemaskeerde waarde",
        "Twijfel je over een waarde?",
        "Open de vervangtabel of Meer controleopties hieronder",
        "Deze vergelijking wijzigt zelf niets",
''',
    '''        "Selecteer rechts een gemiste waarde",
        "Brontekst",
        "Verwerkte tekst",
        "Markeringen tonen",
        "Geel = vervangen of gemaskeerde waarde",
        "Twijfel je over een waarde?",
        "Elke toevoeging blijft zichtbaar en aanpasbaar in de vervangtabel",
        "Masker selectie",
''',
)
replace_once(
    "tests/test_side_by_side_review_ui_patch.py",
    '''        '\"uses_streamlit_components_html\": True',
''',
    '''        '\"static_fallback_available\": True',
        '\"uses_streamlit_components_html\": static_fallback_used',
''',
)
replace_once(
    "tests/test_side_by_side_review_ui_patch.py",
    '''def test_marker_toggle_defaults_on_and_stays_report_only():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "side_by_side_review_show_markers" in text
    assert "value=True" in text
    assert '\"report_only\": True' in text
    assert '\"visual_only\": True' in text
    assert '\"mutation_allowed\": False' in text
''',
    '''def test_marker_toggle_defaults_on_and_renderer_never_mutates_rows():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "side_by_side_review_show_markers" in text
    assert "value=True" in text
    assert '\"report_only\": False' in text
    assert '\"visual_only\": False' in text
    assert '\"mutation_allowed\": False' in text
    assert '\"review_table_mutation\": False' in text
''',
)
replace_once(
    "tests/test_side_by_side_review_ui_patch.py",
    '''    assert "else escape(model[\"processed_pane\"][\"text\"])" in text
    assert "_highlighted_processed_inner_html(" in text
''',
    '''    assert "else escape(processed_text)" in text
    assert "_highlighted_processed_inner_html(" in text
    assert "render_processed_text_selection_component(" in text
''',
)
