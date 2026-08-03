from pathlib import Path

path = Path("presidio_streamlit.py")
text = path.read_text(encoding="utf-8")

replacements = {
    '''    current_profile_options_with_care,\n    detected_reason,\n    resolve_configured_analysis_results,\n''':
        '''    current_profile_options_with_care,\n    detected_reason,\n    detected_review_status,\n    resolve_configured_analysis_results,\n''',
    '''    model_help_text = (\n        "Kies het NER-model dat naast regelherkenning wordt gebruikt. "\n        "De Nederlandse juridische herkenners zijn regelgebaseerd."\n    )\n''':
        '''    model_help_text = (\n        "Kies het NER-model dat naast regelherkenning wordt gebruikt. "\n        "De Nederlandse profielherkenners voor zorg en juridisch zijn regelgebaseerd."\n    )\n''',
    '''            review_status = review_status_for_source("detected", entity_type, score)\n''':
        '''            review_status = detected_review_status(\n                st_recognition_profile, entity_type\n            )\n''',
}

for old, new in replacements.items():
    if old not in text:
        raise RuntimeError(f"Expected Streamlit integration anchor missing: {old[:120]!r}")
    text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
Path("ops/apply_care_review_status_ui_fix.py").unlink(missing_ok=True)
Path(".github/workflows/apply-care-review-status-ui-fix.yml").unlink(missing_ok=True)
