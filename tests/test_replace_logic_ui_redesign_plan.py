from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REDESIGN_PLAN = REPO_ROOT / "REPLACE_LOGIC_UI_REDESIGN_PLAN.md"
SIDE_BY_SIDE_DIRECTION = REPO_ROOT / "SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md"
THIS_TEST = Path(__file__)

PRIMARY_ACTIONS = [
    "Vervangen",
    "Zichtbaar houden",
    "Aanpassen",
    "Later controleren",
]

FIRST_PHASE_SCOPES = [
    "Alleen deze plek",
    "Alle exact dezelfde waarden",
]

TECHNICAL_INTERNALS = [
    "creates_mapping",
    "mapping_candidates",
    "export_readiness",
    "raw decision states",
    "raw audit fields",
]

BLOCKED_BEHAVIORS = [
    "fuzzy matching",
    "guessed intent",
    "automatic replacement",
    "Scrub Key writes",
    "export blocking",
    "reinsert behavior changes",
    "click-to-mark",
    "advanced editor",
    "full-document marking",
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _normalized(path: Path) -> str:
    return _read(path).replace("`", "").lower()


def test_redesign_plan_and_side_by_side_direction_documents_exist():
    assert REDESIGN_PLAN.exists()
    assert SIDE_BY_SIDE_DIRECTION.exists()


def test_old_helper_panel_must_not_return_as_normal_user_facing_panel():
    redesign = _normalized(REDESIGN_PLAN)
    side_by_side = _normalized(SIDE_BY_SIDE_DIRECTION)

    assert "previous replacement decision helper panel is product-rejected" in redesign
    assert "technical helper assets remain useful, but helper internals must not become the normal user-facing panel" in redesign
    assert "it should not reintroduce replacement_decision_panel_ui.py as the normal user-facing panel" in redesign
    assert "the old replacement decision helper panel must not return as the normal user-facing ui" in side_by_side


def test_replacement_logic_is_task_oriented_not_helper_oriented():
    redesign = _normalized(REDESIGN_PLAN)

    assert "the real user task is not “create a replacementdecision”" in redesign
    assert "decide whether it should be replaced, kept visible, adjusted, or reviewed later" in redesign
    assert "replacement logic must be task-oriented, not helper-oriented" in redesign
    assert "helper internals must not be shown as the main ui" in redesign


def test_main_replacement_flow_is_simple_and_user_facing():
    redesign = _read(REDESIGN_PLAN)
    normalized = _normalized(REDESIGN_PLAN)

    for phrase in [
        "Gevonden waarde",
        "Context",
        "Voorgestelde vervanging",
        "Wat wil je doen?",
    ]:
        assert phrase in redesign

    assert "one found item -> context -> suggested replacement -> one simple choice -> optional exact-same scope" in normalized
    assert "Bereik, alleen als relevant" in redesign


def test_first_visible_choices_are_limited_to_four_simple_actions():
    redesign = _read(REDESIGN_PLAN)

    for action in PRIMARY_ACTIONS:
        assert action in redesign

    assert "Primary choice buttons" in redesign
    assert "Optional extra later, not first implementation default" in redesign
    assert "Als context behouden" in redesign


def test_first_scope_choices_are_only_current_or_exact_same_values():
    redesign = _read(REDESIGN_PLAN)
    normalized = _normalized(REDESIGN_PLAN)

    for scope in FIRST_PHASE_SCOPES:
        assert scope in redesign

    assert "do not expose all_normalized in the first redesigned ui" in normalized
    assert "all_normalized as a first user-facing scope" in normalized
    assert "Alle genormaliseerde gelijke waarden" in redesign
    assert "in the first redesigned UI" in redesign


def test_helper_audit_internals_are_not_main_ui_concepts():
    redesign = _normalized(REDESIGN_PLAN)
    side_by_side = _normalized(SIDE_BY_SIDE_DIRECTION)

    assert "the ui should not present helper names" in redesign
    assert "must not expose creates_mapping or mapping_candidates as main ui concepts" in redesign
    assert "do not show export_readiness internals as a main ui field" in redesign
    assert "avoid:" in redesign

    for internal in TECHNICAL_INTERNALS:
        assert internal.lower() in side_by_side
    assert "the normal ui must not show helper/audit internals" in side_by_side


def test_review_table_serial_review_and_context_boundaries_are_preserved():
    redesign = _normalized(REDESIGN_PLAN)
    side_by_side = _normalized(SIDE_BY_SIDE_DIRECTION)

    assert "the review table remains the source of truth and fallback" in redesign
    assert "the review table remains source of truth and fallback" in side_by_side
    assert "serial review is a guided review layer, not a replacement of the table" in redesign
    assert "serial review remains a guided review layer, not a replacement for the table" in side_by_side
    assert "context preview is essential" in redesign
    assert "the redesigned flow should always keep the value and local context close to the choice buttons" in redesign


def test_redesign_connects_to_side_by_side_review_direction():
    redesign = _normalized(REDESIGN_PLAN)
    side_by_side = _normalized(SIDE_BY_SIDE_DIRECTION)

    assert "side-by-side" in side_by_side
    assert "source text left | processed/checked text right" in side_by_side
    assert "optional highlights integrated in the processed text" in side_by_side
    assert "the replacement redesign should plug into the unified side-by-side review surface" in side_by_side
    assert "not as a separate helper/audit panel" in redesign


def test_markers_are_visual_aid_not_mutation_mechanism():
    redesign = _normalized(REDESIGN_PLAN)
    side_by_side = _normalized(SIDE_BY_SIDE_DIRECTION)

    assert "markeringen zijn visuele hulp, geen mutation mechanism" in redesign
    assert "highlights are visual only" in side_by_side
    assert "highlights are not a mutation mechanism" in side_by_side
    assert "highlighting should be integrated into the main processed-text pane" in side_by_side


def test_blocked_behaviors_remain_blocked_in_redesign_contract():
    redesign = _normalized(REDESIGN_PLAN)
    side_by_side = _normalized(SIDE_BY_SIDE_DIRECTION)
    combined = redesign + "\n" + side_by_side

    for behavior in BLOCKED_BEHAVIORS:
        assert behavior.lower() in combined

    assert "scrub key is not written from this flow without a separate package" in redesign
    assert "export is not blocked from this flow without a separate package" in redesign
    assert "reinsert is not changed from this flow" in redesign
    assert "no click-to-mark in this phase" in redesign


def test_contract_tests_are_required_before_new_implementation():
    redesign = _normalized(REDESIGN_PLAN)
    side_by_side = _normalized(SIDE_BY_SIDE_DIRECTION)

    assert "wp_replace_logic_ui_redesign_contract_tests" in redesign
    assert "that package should test the redesign plan" in redesign
    assert "only after that, and only after separate coordinator approval" in redesign
    assert "wp_replace_logic_ui_redesigned_implementation" in redesign
    assert "the replacement-flow tests can run in parallel" in side_by_side


def test_contract_uses_synthetic_values_only():
    rendered = THIS_TEST.read_text(encoding="utf-8") + "\n" + _read(REDESIGN_PLAN) + "\n" + _read(SIDE_BY_SIDE_DIRECTION)
    forbidden_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
        "Fatima " + "El " + "Amrani",
        "Peter " + "Bakker",
    ]

    for forbidden in forbidden_examples:
        assert forbidden not in rendered
