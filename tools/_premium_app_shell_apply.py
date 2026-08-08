from pathlib import Path

source_path = Path("tools/_premium_app_shell_patch_source.txt")
source = source_path.read_text(encoding="utf-8")
start_marker = "          python - <<'PY'\n"
end_marker = "\n          PY\n"
start = source.index(start_marker) + len(start_marker)
end = source.index(end_marker, start)
raw_script = source[start:end]
lines = []
for line in raw_script.splitlines():
    if line.startswith("          "):
        line = line[10:]
    lines.append(line)
script = "\n".join(lines) + "\n"
compile(script, "_premium_app_shell_extracted_patch.py", "exec")
exec(compile(script, "_premium_app_shell_extracted_patch.py", "exec"), {})
Path("tools/_premium_app_shell_apply.py").unlink()
source_path.unlink()
