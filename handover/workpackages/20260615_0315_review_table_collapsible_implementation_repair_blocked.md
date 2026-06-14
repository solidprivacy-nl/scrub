# Handover — WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION-REPAIR

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION-REPAIR`

Status: blocked/released; no production code change was made.

## Summary

The open implementation claim for `WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION` was reviewed after coordinator approval.

The intended change is clear and small, but it touches `presidio_streamlit.py`, a large central UI file. The GitHub contents connector available here only supports whole-file replacement for updates, not line-level patching. Because `presidio_streamlit.py` is large and active, a whole-file manual replacement through this connector is too risky and could corrupt unrelated review/export/Scrub Key/reinsert behavior.

Therefore the implementation was not made through this connector. The claim is released for a worker with a real repository checkout/Codespaces where a normal diff can be applied and reviewed.

## Intended implementation patch

In `presidio_streamlit.py`, replace the current section:

```python
st.divider()
st.subheader("3. Controleer gevonden gegevens")
st.caption(...)

if st_recognition_profile == "Dutch Legal Strict":
    with st.expander("Mogelijke gemiste waarden", expanded=bool(candidate_rows)):
        ...

edited_replacements_df = st.data_editor(..., key="replacement_editor")
```

with a non-nested collapsible review-table section:

```python
st.divider()
review_item_count = len(replacement_editor_df.index)
with st.expander(
    f"3. Controleer gevonden gegevens — {review_item_count} items",
    expanded=False,
):
    st.caption(
        "Vink fout-positieven uit, pas placeholders aan, voeg handmatige vervangingen toe "
        "en vink Onthouden aan voor vervangingen die je opnieuw wilt gebruiken. "
        "Mogelijke kandidaten staan standaard uitgevinkt. De vervangtabel blijft leidend."
    )

    if st_recognition_profile == "Dutch Legal Strict":
        st.markdown("**Mogelijke gemiste waarden**")
        if candidate_rows:
            st.warning(...)
            candidate_display_df = pd.DataFrame(candidate_rows)
            ...
            st.dataframe(candidate_display_df, use_container_width=True)
        else:
            st.success("Geen mogelijke gemiste referenties gevonden door de auditlaag.")

    edited_replacements_df = st.data_editor(
        replacement_editor_df,
        ...,
        key="replacement_editor",
    )
```

Important: do **not** put `with st.expander("Mogelijke gemiste waarden")` inside the new review-table expander. Nested Streamlit expanders have caused previous problems. Use a plain `st.markdown("**Mogelijke gemiste waarden**")` subheading inside the collapsible section instead.

`render_serial_review_panel(...)`, `edited_replacements` creation, memory, export/download, Scrub Key and reinsert behavior must remain outside and unchanged.

## Files added

- `handover/workpackages/20260615_0315_review_table_collapsible_implementation_repair_blocked.md`

## Files changed

- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION.md` should be updated to `blocked/released` after this handover.

## Tests/checks run

No shell/pytest execution was available through the connector.

No production code was changed, so no implementation validation was performed.

## Validation status

Blocked before product-code edit.

## GitHub Actions status

Not applicable for implementation because no production-code change was made in this repair.

## Hugging Face sync status

Not applicable for implementation because no production-code change was made in this repair.

## App verification status

Not applicable. The UI was not changed.

## Remaining risks

- `WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION` is not implemented yet.
- The review table remains non-collapsible.
- A future worker must use a normal repository checkout or Codespaces to apply a controlled diff to `presidio_streamlit.py`.

## Next recommended step

Use a worker with repo checkout/Codespaces to apply the exact patch above, then run:

```text
pytest tests/test_review_table_collapsible_contract.py
python -m pytest -q tests
```

After green Actions/HF sync, request app verification:

- section 3 is collapsible;
- heading shows `Controleer gevonden gegevens — <count> items`;
- table is still present inside the expander;
- `replacement_editor` still exists;
- `include`, `remember`, `find`, `replace_with` still work;
- export/download unchanged;
- Scrub Key unchanged;
- reinsert unchanged;
- no nested expander error.
