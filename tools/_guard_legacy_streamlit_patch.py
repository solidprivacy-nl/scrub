from pathlib import Path
import ast

path = Path("fix_streamlit_nested_expanders.py")
text = path.read_text(encoding="utf-8")
needle = 'text = APP_FILE.read_text(encoding="utf-8")\n'
guard = '''text = APP_FILE.read_text(encoding="utf-8")

# The Premium app shell is now direct source. Legacy runtime source mutation
# must not re-inject the retired form/two-mode UI into that source.
if "premium_streamlit_shell_ui" in text:
    APP_FILE.write_text(text, encoding="utf-8")
    raise SystemExit(0)
'''
if 'if "premium_streamlit_shell_ui" in text:' not in text:
    if needle not in text:
        raise SystemExit("legacy patch read marker not found")
    text = text.replace(needle, guard, 1)
path.write_text(text, encoding="utf-8")
ast.parse(text)
Path("tools/_guard_legacy_streamlit_patch.py").unlink()
Path(".github/workflows/premium-legacy-patch-guard.yml").unlink()
