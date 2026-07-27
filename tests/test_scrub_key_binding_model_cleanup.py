from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_temporary_binding_model_files_are_absent() -> None:
    assert not (ROOT / ".github/workflows/mvp_scrub_key_binding_model_operator.yml").exists()
    assert not (ROOT / ".github/workflows/mvp_scrub_key_binding_model_finalizer.yml").exists()
    assert not (ROOT / "scripts/finalize_mvp_scrub_key_binding_model_implementation.py").exists()
