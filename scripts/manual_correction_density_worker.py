from __future__ import annotations

from pathlib import Path


APP = Path("presidio_streamlit.py")
TEST = Path("tests/test_manual_correction_panel_density_implementation.py")
CHANGELOG = Path("CHANGELOG.md")
WORKPACKAGES = Path("WORKPACKAGES.md")
RELEASE_NOTES = Path("RELEASE_NOTES.md")
CLAIM = Path(
    "workpackage_claims/"
    "scrub_wp_manual_correction_panel_density_simplification_implementation.md"
)
HANDOVER = Path(
    "handover/workpackages/"
    "20260716_2040_manual_correction_panel_density_implementation.md"
)

TIMESTAMP = "2026-07-16 20:40 Europe/Amsterdam"
COMPACT_MARKER = (
    "value_col, type_col, replacement_col = "
    "st.columns([2.0, 1.1, 1.6])"
)

OLD = "\n".join(
    [
        '        with st.expander("Gemiste waarde toevoegen", expanded=False):',
        '            st.markdown("**Gemiste waarde toevoegen**")',
        '            st.caption("Voeg snel een waarde toe die Scrub heeft gemist.")',
        '            with st.form("manual_mask_entry_form", clear_on_submit=True):',
        '                manual_value = st.text_input("Waarde die alsnog gemaskeerd moet worden")',
        '                manual_type_label = st.selectbox("Type gegeven", list(MANUAL_MASK_TYPE_OPTIONS))',
        '                manual_placeholder = build_manual_placeholder(manual_type_label, replacement_editor_df)',
        '                manual_replace_with = st.text_input("Vervangen door", value=manual_placeholder)',
        '                manual_submit = st.form_submit_button("Toevoegen aan vervangtabel")',
        "",
    ]
)

NEW = "\n".join(
    [
        '        with st.expander("Gemiste waarde toevoegen", expanded=False):',
        '            st.caption("Voeg een gemiste waarde rechtstreeks toe aan de vervangtabel.")',
        "",
        '            with st.form("manual_mask_entry_form", clear_on_submit=True):',
        '                value_col, type_col, replacement_col = st.columns([2.0, 1.1, 1.6])',
        "",
        "                with value_col:",
        "                    manual_value = st.text_input(",
        '                        "Waarde die alsnog gemaskeerd moet worden"',
        "                    )",
        "",
        "                with type_col:",
        "                    manual_type_label = st.selectbox(",
        '                        "Type gegeven",',
        "                        list(MANUAL_MASK_TYPE_OPTIONS),",
        "                    )",
        "",
        "                manual_placeholder = build_manual_placeholder(",
        "                    manual_type_label,",
        "                    replacement_editor_df,",
        "                )",
        "",
        "                with replacement_col:",
        "                    manual_replace_with = st.text_input(",
        '                        "Vervangen door",',
        "                        value=manual_placeholder,",
        "                    )",
        "",
        "                manual_submit = st.form_submit_button(",
        '                    "Toevoegen aan vervangtabel",',
        "                    use_container_width=True,",
        "                )",
        "",
    ]
)

TEST_CONTENT = '''from __future__ import annotations

import ast
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP_PATH = REPO_ROOT / "presidio_streamlit.py"
THIS_TEST_PATH = REPO_ROOT / "tests" / "test_manual_correction_panel_density_implementation.py"


def app_source() -> str:
    return APP_PATH.read_text(encoding="utf-8")


def test_manual_correction_expander_stays_collapsed_and_has_compact_copy() -> None:
    source = app_source()
    assert 'with st.expander("Gemiste waarde toevoegen", expanded=False):' in source
    assert 'st.caption("Voeg een gemiste waarde rechtstreeks toe aan de vervangtabel.")' in source
    assert 'st.markdown("**Gemiste waarde toevoegen**")' not in source


def test_manual_correction_inputs_are_grouped_in_one_compact_row() -> None:
    source = app_source()
    assert "value_col, type_col, replacement_col = st.columns([2.0, 1.1, 1.6])" in source
    for marker in ["with value_col:", "with type_col:", "with replacement_col:"]:
        assert marker in source
    for label in ["Waarde die alsnog gemaskeerd moet worden", "Type gegeven", "Vervangen door"]:
        assert label in source


def test_existing_form_identity_and_action_are_preserved() -> None:
    source = app_source()
    assert 'with st.form("manual_mask_entry_form", clear_on_submit=True):' in source
    assert "manual_submit = st.form_submit_button(" in source
    assert '"Toevoegen aan vervangtabel"' in source
    assert "use_container_width=True" in source


def test_existing_manual_mask_behavior_markers_are_preserved() -> None:
    source = app_source()
    for marker in [
        "manual_value",
        "manual_type_label",
        "manual_placeholder",
        "manual_replace_with",
        "manual_submit",
        "build_manual_placeholder(",
        "validate_manual_mask_input(",
        "build_manual_mask_row(",
        "manual_mask_document_key(",
        'st.session_state["manual_mask_rows"]',
        "st.rerun()",
    ]:
        assert marker in source


def test_validation_block_stays_after_manual_submit() -> None:
    source = app_source()
    submit_index = source.index("if manual_submit:")
    validation_index = source.index("validate_manual_mask_input(", submit_index)
    row_index = source.index("build_manual_mask_row(", validation_index)
    rerun_index = source.index("st.rerun()", row_index)
    assert submit_index < validation_index < row_index < rerun_index


def test_implementation_test_is_source_level_only() -> None:
    tree = ast.parse(THIS_TEST_PATH.read_text(encoding="utf-8"))
    imported_roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".")[0])
    assert "streamlit" not in imported_roots
    assert "presidio_streamlit" not in imported_roots
'''

CHANGELOG_ENTRY = '''## 2026-07-16 — SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Status: implemented; local validation passed.

Purpose:

- Make the existing `Gemiste waarde toevoegen` panel materially shorter and less form-like.
- Remove the duplicate internal heading and group value, type and replacement controls in one compact row.
- Preserve the existing validation, session-state and replacement-table workflow.

Files changed:

- `presidio_streamlit.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/scrub_wp_manual_correction_panel_density_simplification_implementation.md`

Files added:

- `tests/test_manual_correction_panel_density_implementation.py`
- `handover/workpackages/20260716_2040_manual_correction_panel_density_implementation.md`

Validation status:

- Required worker validation passed.
- GitHub Actions pending after PR update.
- Hugging Face sync pending after merge.
- Live app verification required because visible UI behavior changed.

Intentionally not changed:

- validation rules or duplicate detection;
- placeholder generation or entity types;
- replacement-row structure or replacement semantics;
- export payloads, filenames or MIME types;
- Scrub Key JSON or warning behavior;
- reinsert behavior;
- recognizers, thresholds, document processing, runtime/startup or dependencies.

Next recommended step:

- Verify PR Actions, merge when green, verify Hugging Face sync and request live app verification.

---

'''

WORKPACKAGES_ENTRY = f'''## {TIMESTAMP} — SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Status: completed / ready for app verification.

Summary:
- Converted the open manual correction form from a vertical stack to one compact three-column input row.
- Removed the duplicate internal `Gemiste waarde toevoegen` heading.
- Kept the expander collapsed by default and retained one full-width submit action.
- Preserved validation, session state, replacement-table integration and all export/Scrub Key/reinsert semantics.

Validation:
- Required worker validation passed.
- GitHub Actions pending after PR update.
- Hugging Face sync pending after merge.
- App verification required after sync.

Next recommended step:
- `SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_APP_VERIFY`.

'''

RELEASE_ENTRY = '''## 2026-07-16 — Handmatige aanvulling compacter

- `Gemiste waarde toevoegen` gebruikt bij openen een compactere invoerregel voor waarde, type en vervanging.
- De dubbele interne kop is verwijderd; de functie en validatiemeldingen blijven ongewijzigd.
- De vervangtabel, exports, Scrub Key en terugzetworkflow zijn niet gewijzigd.

---

'''

HANDOVER_CONTENT = f'''# Handover — SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

## Status

Completed / ready for app verification.

## Files added

- `tests/test_manual_correction_panel_density_implementation.py`
- `{HANDOVER}`

## Files changed

- `presidio_streamlit.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/scrub_wp_manual_correction_panel_density_simplification_implementation.md`

## Tests

- `python -m py_compile presidio_streamlit.py`
- New source-level implementation tests.
- Required Review/Export/UI guardrail suite.
- Existing matching manual-mask tests.
- `git diff --check`.

## Validation status

Required local/worker validation passed.

## GitHub Actions status

Pending PR validation after implementation commit.

## Hugging Face sync status

Pending after merge.

## App verification status

Required after Actions and sync because visible UI behavior changed.

## Remaining risks

- Live verification must confirm the three controls remain usable at the deployed app width.
- Empty and valid synthetic submissions must retain existing warning/success behavior.
- Replacement-table and export integration must remain unchanged.

## Next recommended step

`SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_APP_VERIFY` after Actions and Hugging Face sync are green.
'''


def prepend_once(path: Path, marker: str, content: str) -> None:
    current = path.read_text(encoding="utf-8")
    if marker not in current:
        path.write_text(content + current, encoding="utf-8")


def main() -> None:
    source = APP.read_text(encoding="utf-8")
    if COMPACT_MARKER in source:
        print("Compact manual correction panel already implemented.")
        return
    if source.count(OLD) != 1:
        raise RuntimeError(
            f"Expected exactly one original manual panel; found {source.count(OLD)}"
        )

    APP.write_text(source.replace(OLD, NEW, 1), encoding="utf-8")
    TEST.write_text(TEST_CONTENT, encoding="utf-8")
    prepend_once(
        CHANGELOG,
        "SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION",
        CHANGELOG_ENTRY,
    )
    prepend_once(
        WORKPACKAGES,
        "2026-07-16 20:40 Europe/Amsterdam — "
        "SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION",
        WORKPACKAGES_ENTRY,
    )
    prepend_once(
        RELEASE_NOTES,
        "2026-07-16 — Handmatige aanvulling compacter",
        RELEASE_ENTRY,
    )

    claim = CLAIM.read_text(encoding="utf-8")
    claim = claim.replace(
        "Status: in_progress",
        "Status: completed / ready for app verification",
        1,
    )
    if "Implementation update:" not in claim:
        claim += (
            f"\n\nImplementation update:\n"
            f"- Implemented at: {TIMESTAMP}\n"
            "- Product change limited to compact manual correction panel layout.\n"
            "- Required worker validation passed.\n"
            f"- Handover: `{HANDOVER}`\n"
        )
    CLAIM.write_text(claim, encoding="utf-8")

    HANDOVER.parent.mkdir(parents=True, exist_ok=True)
    HANDOVER.write_text(HANDOVER_CONTENT, encoding="utf-8")
    print("Manual correction panel implementation applied.")


if __name__ == "__main__":
    main()
