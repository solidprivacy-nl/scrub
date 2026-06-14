from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PLAN = REPO_ROOT / "SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md"
DIRECTION = REPO_ROOT / "SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md"
REPLACE_REDESIGN_PLAN = REPO_ROOT / "REPLACE_LOGIC_UI_REDESIGN_PLAN.md"
THIS_TEST = Path(__file__)

MAIN_SURFACE_PHRASES = [
    "one clear main review surface",
    "Brontekst links | Verwerkte/gecontroleerde tekst rechts",
    "Optionele markeringen geïntegreerd in de verwerkte tekst",
    "links = origineel / bron",
    "rechts = gecontroleerde versie / wat straks gebruikt of geëxporteerd wordt",
]

REQUIRED_UI_COPY = [
    "Controleer de tekst",
    "Vergelijk bron en verwerkte tekst",
    "Brontekst",
    "Verwerkte tekst",
    "Markeringen tonen",
    "Markeringen tonen in verwerkte tekst",
    "De vervangtabel blijft leidend. Controleer bij twijfel de tabel hieronder.",
]

REPLACEMENT_ACTIONS = [
    "Vervangen",
    "Zichtbaar houden",
    "Aanpassen",
    "Later controleren",
]

BLOCKED_BEHAVIORS = [
    "Streamlit UI implementation",
    "presidio_streamlit.py",
    "serial_review_panel_ui.py",
    "review_highlight_toggle_panel_ui.py",
    "custom HTML/component implementation",
    "synchronized scroll implementation",
    "review table behavior changes",
    "replacement behavior changes",
    "Scrub Key writes",
    "export blocking",
    "export/download behavior changes",
    "reinsert behavior changes",
    "click-to-mark",
    "advanced editor",
    "full-document marking",
    "dependency changes",
    "cloud processing",
    "real-data fixtures",
    "raw unsafe document HTML",
    "fuzzy matching or guessed intent",
    "automatic replacement",
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _normalized(path: Path) -> str:
    return _read(path).replace("`", "").lower()


def test_side_by_side_contract_documents_exist():
    assert PLAN.exists()
    assert DIRECTION.exists()
    assert REPLACE_REDESIGN_PLAN.exists()


def test_plan_requires_one_main_side_by_side_review_surface():
    text = _read(PLAN)
    normalized = _normalized(PLAN)

    for phrase in MAIN_SURFACE_PHRASES:
        assert phrase in text

    assert "the user should not have to decide which panel is the real review surface" in normalized
    assert "everything else should support this comparison, not compete with it" in normalized


def test_source_left_processed_right_and_headers_are_user_facing():
    text = _read(PLAN)
    normalized = _normalized(PLAN)

    assert "The left column shows the source text" in text
    assert "The right column shows the processed or checked text" in text
    assert "The right column is the primary place for visual review support" in text
    assert "recommended labels" in normalized

    for label in ["Brontekst", "Verwerkte tekst", "Originele tekst", "Gecontroleerde tekst"]:
        assert label in text

    for forbidden in ["input buffer", "processed buffer", "render target", "replacement output", "highlight engine"]:
        assert forbidden in text


def test_highlight_toggle_is_integrated_into_processed_pane_not_duplicate_preview():
    plan = _normalized(PLAN)
    direction = _normalized(DIRECTION)

    assert "the toggle belongs near the right column" in plan
    assert "the toggle affects only the right column" in plan
    assert "integrate highlights into the processed-text right column" in plan
    assert "highlighting should not live primarily in a separate highlight-only panel" in direction
    assert "the existing separate highlight-only panel is not the desired end-state" in direction
    assert "separate highlight-only duplicate preview" in plan
    assert "not the desired long-term ux" in plan


def test_highlights_are_visual_only_non_mutating_and_do_not_change_output_state():
    plan = _normalized(PLAN)
    direction = _normalized(DIRECTION)

    for required in [
        "only visual aid",
        "wijzigt niets aan de vervangtabel of export",
        "must not change source text, review table state, export payloads, scrub key state or reinsert behavior",
        "keep highlights visual-only",
    ]:
        assert required in plan

    assert "highlights are visual only" in direction
    assert "highlights are not a mutation mechanism" in direction


def test_repeated_gemarkeerd_labels_are_not_long_term_design():
    plan = _normalized(PLAN)
    direction = _normalized(DIRECTION)

    assert "avoid repeated per-highlight labels in the long-term design" in plan
    assert "repeated labels add noise" in plan
    assert "use one compact legend instead" in plan
    assert "no repeated inline gemarkeerd label" in direction
    assert "only use a label when it adds a real distinction" in direction


def test_single_compact_legend_is_allowed_but_not_repeated_inline_labels():
    text = _read(PLAN)
    normalized = _normalized(PLAN)

    assert "If a legend is needed, use one compact line above the processed text" in text
    assert "Geel = vervangen of gemaskeerde waarde" in text
    assert "Gemarkeerd = waarde die door de vervangtabel is vervangen" in text
    assert "use a single compact legend, not repeated labels on every highlight" in normalized


def test_review_table_remains_source_of_truth_and_fallback():
    plan = _normalized(PLAN)
    direction = _normalized(DIRECTION)

    assert "the review table remains authoritative" in plan
    assert "the review table remains the source of truth and fallback" in plan
    assert "the side-by-side surface must not silently replace table semantics" in plan
    assert "de vervangtabel blijft leidend" in plan
    assert "the review table remains source of truth and fallback" in direction


def test_serial_review_remains_guided_layer_not_table_replacement():
    plan = _normalized(PLAN)
    direction = _normalized(DIRECTION)

    assert "serial review remains a guided review layer" in plan
    assert "it is not a replacement for the review table" in plan
    assert "navigation/attention aid for the side-by-side surface" in plan
    assert "it should not multiply into more helper panels" in plan
    assert "serial review remains a guided review layer, not a replacement for the table" in direction


def test_replacement_review_plugs_into_side_by_side_without_helper_internals():
    plan = _read(PLAN)
    normalized = _normalized(PLAN)
    replacement_plan = _normalized(REPLACE_REDESIGN_PLAN)

    assert "Replacement review should plug into the side-by-side review surface" in plan
    assert "not return as the old helper/audit panel" in plan
    assert "Gevonden waarde -> Context -> Voorgestelde vervanging -> Wat wil je doen?" in plan

    for action in REPLACEMENT_ACTIONS:
        assert action in plan

    for forbidden in [
        "creates_mapping",
        "mapping_candidates",
        "export_readiness",
        "raw decision states",
        "state_counts",
        "apply_to_same_value_actions",
    ]:
        assert forbidden in plan

    assert "replacement logic must be task-oriented, not helper-oriented" in replacement_plan
    assert "helper internals must not be shown as the main ui" in replacement_plan


def test_all_normalized_is_not_first_normal_user_facing_scope():
    plan = _normalized(PLAN)
    replace_plan = _normalized(REPLACE_REDESIGN_PLAN)

    assert "all_normalized" in plan
    assert "blocks all_normalized as a first normal user-facing scope" in plan
    assert "all_normalized as a first user-facing scope" in replace_plan


def test_smallest_safe_first_implementation_is_bounded_read_only_and_no_scroll_sync():
    plan = _normalized(PLAN)

    assert "smallest safe first implementation" in plan
    assert "bounded side-by-side read-only surface" in plan
    assert "render source text left" in plan
    assert "render processed/checked text right" in plan
    assert "include the existing highlight toggle near the right pane" in plan
    assert "avoid synchronized scrolling in the first implementation" in plan
    assert "avoid custom components in the first implementation unless explicitly approved" in plan
    assert "avoid replacement action mutation" in plan


def test_blocked_behaviors_are_explicitly_blocked():
    text = _read(PLAN)

    for behavior in BLOCKED_BEHAVIORS:
        assert behavior in text

    assert "Synchronized scrolling is desirable, but must be a separate package with separate tests" in text


def test_html_rendering_requires_escape_and_blocks_raw_unsafe_document_html():
    plan = _normalized(PLAN)
    direction = _normalized(DIRECTION)

    assert "raw unsafe document html" in plan
    assert "requires escaping if any html-based rendering is later used" in plan
    assert "source/user text must be escaped if html rendering is used" in direction
    assert "no raw unsafe user-text html" in direction


def test_contract_tests_gate_implementation_and_define_next_package():
    plan = _normalized(PLAN)

    assert "wp_side_by_side_review_contract_tests" in plan
    assert "only after contract tests and separate coordinator approval should implementation be considered" in plan
    assert "wp_side_by_side_review_implementation" in plan
    assert "do not start these automatically" in plan
    assert "the next safe step is contract tests for this plan, not implementation" in plan


def test_contract_uses_synthetic_values_only():
    rendered = THIS_TEST.read_text(encoding="utf-8") + "\n" + _read(PLAN) + "\n" + _read(DIRECTION)
    forbidden_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
        "Fatima " + "El " + "Amrani",
        "Peter " + "Bakker",
    ]

    for forbidden in forbidden_examples:
        assert forbidden not in rendered
