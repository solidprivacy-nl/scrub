from pathlib import Path


WORKFLOW = Path('.github/workflows/sync-to-huggingface.yml')


def test_hf_sync_ignores_only_clearly_non_runtime_surfaces() -> None:
    source = WORKFLOW.read_text(encoding='utf-8')

    assert 'paths-ignore:' in source
    for ignored in [
        '.github/**',
        'operator_triggers/**',
        'workpackage_claims/**',
        'handover/**',
        'tests/**',
        'output/**',
        'test_cases/**',
        'ROADMAP.md',
        'WORKPACKAGES.md',
        'CHANGELOG.md',
        'DECISION_LOG.md',
        'RISK_REGISTER.md',
        'RELEASE_NOTES.md',
        'STATUS_MONITORING_RUNBOOK.md',
    ]:
        assert f'- "{ignored}"' in source


def test_hf_sync_does_not_ignore_runtime_critical_files() -> None:
    source = WORKFLOW.read_text(encoding='utf-8')
    ignored_section = source.split('paths-ignore:', 1)[1].split('workflow_dispatch:', 1)[0]

    for runtime_path in [
        'README.md',
        'Dockerfile',
        'pyproject.toml',
        'poetry.lock',
        'requirements.txt',
        '*.py',
        'presidio_streamlit.py',
        'reinsert_mode_ui.py',
    ]:
        assert runtime_path not in ignored_section


def test_hf_sync_still_force_pushes_main_to_the_space() -> None:
    source = WORKFLOW.read_text(encoding='utf-8')

    assert 'branches:' in source
    assert '- main' in source
    assert 'git push --force huggingface HEAD:main' in source
    assert 'workflow_dispatch:' in source
