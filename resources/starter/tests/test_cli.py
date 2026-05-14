"""Tests for the workshop starter CLI."""

from __future__ import annotations

import pytest

from myapp.cli import main


def test_hello_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["hello"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "hello, world"


def test_status_prints_branch_and_uncommitted(
    capsys: pytest.CaptureFixture[str],
) -> None:
    exit_code = main(["status"])
    captured = capsys.readouterr()
    assert exit_code == 0
    lines = captured.out.strip().splitlines()
    assert len(lines) == 2
    assert lines[0].startswith("branch: ")
    assert lines[1].startswith("uncommitted: ")
