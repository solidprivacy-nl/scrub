from __future__ import annotations

from pathlib import Path


WORKFLOW_PATH = Path(".github/workflows/tests.yml")


def _workflow_text() -> str:
    return WORKFLOW_PATH.read_text(encoding="utf-8")


def test_tests_workflow_keeps_standard_and_manual_triggers() -> None:
    workflow = _workflow_text()

    assert "push:\n    branches:\n      - main" in workflow
    assert "  pull_request:\n" in workflow
    assert "  workflow_dispatch:\n" in workflow
    assert "paths:" not in workflow
    assert "paths-ignore:" not in workflow


def test_issue70_rerun_carrier_is_narrow_and_default_branch_scoped() -> None:
    workflow = _workflow_text()

    assert "  workflow_run:\n    workflows:\n      - Diagnostic recall benchmark report" in workflow
    assert "    types:\n      - completed" in workflow
    assert "github.event.workflow_run.run_attempt > 1" in workflow
    assert "github.event.workflow_run.conclusion == 'success'" in workflow
    assert "permissions:\n  contents: read" in workflow

    # workflow_run uses the last commit on the default branch as GITHUB_SHA.
    # No ref override is allowed: checkout must test that exact main commit.
    assert "uses: actions/checkout@v4" in workflow
    assert "ref:" not in workflow


def test_issue70_rerun_carrier_runs_the_unchanged_full_regression_command() -> None:
    workflow = _workflow_text()

    assert "python -m pytest -q tests" in workflow
    assert workflow.count("python -m pytest -q tests") == 1


def test_issue70_recovery_does_not_add_schedule_or_comment_triggers() -> None:
    workflow = _workflow_text()

    assert "schedule:" not in workflow
    assert "issue_comment:" not in workflow
