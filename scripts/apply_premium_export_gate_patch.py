from pathlib import Path


path = Path("presidio_streamlit.py")
text = path.read_text(encoding="utf-8")

old_import = "from premium_streamlit_shell_ui import render_stage_header\n"
new_import = old_import + "from premium_streamlit_export_gate import render_export_readiness_gate\n"
if text.count(old_import) != 1:
    raise SystemExit(f"expected exactly one shell-ui import, found {text.count(old_import)}")
if "from premium_streamlit_export_gate import render_export_readiness_gate" not in text:
    text = text.replace(old_import, new_import, 1)

old_block = '''        if is_premium_standard:
            render_stage_header(premium_state, Stage.DOWNLOAD)
        else:
            st.subheader("3. Exporteer resultaat")
        st.caption("Download documenten; Scrub Key en auditbestanden blijven apart.")

        st.markdown("**Document downloaden**")
'''
new_block = '''        if is_premium_standard:
            render_stage_header(premium_state, Stage.DOWNLOAD)
        else:
            st.subheader("3. Exporteer resultaat")

        export_surface_ready = render_export_readiness_gate(
            st.session_state,
            is_expert=is_premium_expert,
            generation=current_processing_generation,
            reviewed_rows=edited_replacements_df.to_dict("records"),
        )
        if not export_surface_ready:
            if is_premium_standard:
                st.caption("Downloaden is beschikbaar nadat de huidige controle expliciet is afgerond.")
            st.stop()

        st.caption("Download documenten; Scrub Key en auditbestanden blijven apart.")
        st.markdown("**Document downloaden**")
'''
if text.count(old_block) != 1:
    raise SystemExit(f"expected exactly one export surface block, found {text.count(old_block)}")
text = text.replace(old_block, new_block, 1)

compile(text, str(path), "exec")
path.write_text(text, encoding="utf-8")
