from __future__ import annotations

from pathlib import Path
import runpy


operator_path = Path("ops/apply_care_profile_current_ui_integration.py")
operator_text = operator_path.read_text(encoding="utf-8")

# Align two prepared source anchors with the current main-branch implementation.
operator_text = operator_text.replace(
    '"NL_POLICE_REFERENCE": "POLITIEREFERENTIE"',
    '"NL_POLICE_REFERENCE": "POLITIE_OF_OM_REFERENTIE"',
)
operator_text = operator_text.replace(
    "'''STRUCTURED_ENTITY_TYPES = LEGAL_ENTITY_TYPES | {\n''',",
    "'''STRUCTURED_ENTITY_TYPES = {\n''',",
)
operator_text = operator_text.replace(
    "STRUCTURED_ENTITY_TYPES = LEGAL_ENTITY_TYPES | CARE_ENTITY_TYPES | {",
    "STRUCTURED_ENTITY_TYPES = CARE_ENTITY_TYPES | {",
)
operator_path.write_text(operator_text, encoding="utf-8")

runpy.run_path(str(operator_path), run_name="__main__")
Path(__file__).unlink(missing_ok=True)
