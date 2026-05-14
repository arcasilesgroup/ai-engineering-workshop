"""myapp CLI — minimal scaffold for the ai-engineering workshop exercise."""

from __future__ import annotations

import argparse
import subprocess
import sys


def _run(cmd: list[str]) -> str:
    return subprocess.run(
        cmd, capture_output=True, text=True, check=False
    ).stdout.strip()


def _branch() -> str:
    out = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    return out or "unknown"


def _uncommitted_count() -> int:
    out = _run(["git", "status", "--porcelain"])
    return 0 if not out else len(out.splitlines())


def _hello(_args: argparse.Namespace) -> int:
    print("hello, world")
    return 0


def _status(_args: argparse.Namespace) -> int:
    print(f"branch: {_branch()}")
    print(f"uncommitted: {_uncommitted_count()}")
    return 0


def _register_hello(subparsers: argparse._SubParsersAction) -> None:
    p = subparsers.add_parser("hello", help="print a greeting")
    p.set_defaults(func=_hello)


def _register_status(subparsers: argparse._SubParsersAction) -> None:
    p = subparsers.add_parser("status", help="print branch and uncommitted file count")
    p.set_defaults(func=_status)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="myapp", description="workshop starter CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)
    _register_hello(subparsers)
    _register_status(subparsers)
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
