from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DIST_DIR = PACKAGE_ROOT / "dist"
PYPROJECT_PATH = PACKAGE_ROOT / "pyproject.toml"
CANONICAL_NAME = "oworker-aclip"


def run(command: list[str], *, cwd: Path = PACKAGE_ROOT, env: dict[str, str] | None = None) -> None:
    completed = subprocess.run(command, cwd=cwd, env=env, check=False)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)


def load_project_metadata() -> dict:
    with PYPROJECT_PATH.open("rb") as handle:
        return tomllib.load(handle)


def project_version() -> str:
    return str(load_project_metadata()["project"]["version"])


def clean_dist() -> None:
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True, exist_ok=True)


def build_canonical() -> None:
    run([sys.executable, "-m", "build", "--sdist", "--wheel", "--outdir", str(DIST_DIR)])


def build_all() -> None:
    clean_dist()
    build_canonical()


def dist_files() -> list[str]:
    files = sorted(str(path) for path in DIST_DIR.iterdir() if path.is_file())
    if not files:
        raise SystemExit("No distribution files were built.")
    return files


def check() -> None:
    build_all()
    run([sys.executable, "-m", "twine", "check", *dist_files()])


def publish() -> None:
    token = os.environ.get("PYPI_TOKEN")
    if not token:
        raise SystemExit("PYPI_TOKEN is required. PyPI no longer supports username/password uploads.")
    check()
    env = os.environ.copy()
    env["TWINE_USERNAME"] = "__token__"
    env["TWINE_PASSWORD"] = token
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    run(
        [
            sys.executable,
            "-m",
            "twine",
            "upload",
            "--non-interactive",
            "--disable-progress-bar",
            "--skip-existing",
            *dist_files(),
        ],
        env=env,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Build and publish the ACLIP Python SDK.")
    parser.add_argument("command", choices=("check", "publish"))
    args = parser.parse_args()

    if args.command == "check":
        check()
        return
    if args.command == "publish":
        publish()
        return


if __name__ == "__main__":
    main()

