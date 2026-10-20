#!/usr/bin/env python3
"""Verify all released files listed in the repository checksum inventory; read-only."""

from pathlib import Path
import hashlib
import sys
ROOT = Path(__file__).resolve().parents[1]

def safe_path(relative):
    candidate = (ROOT / relative).resolve()
    if not candidate.is_relative_to(ROOT) or not candidate.is_file():
        raise ValueError(f"Missing or unsafe path: {relative}")
    return candidate

def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    try:
        inventory = ROOT / "metadata/REPOSITORY-SHA256SUMS"
        rows = inventory.read_text(encoding="utf-8").splitlines()
        count = 0
        failures = []
        for row in rows:
            if not row.strip() or row.startswith("#"):
                continue
            expected, relative = row.split("  ", 1)
            if len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
                raise ValueError(f"Invalid SHA-256 entry: {relative}")
            path = safe_path(relative)
            count += 1
            if sha256(path) != expected:
                failures.append(relative)
        if failures:
            print("FAILED: changed files\n" + "\n".join(failures), file=sys.stderr)
            return 1
        print(f"PASS: {count} listed repository files match the packaged inventory.")
        print("The inventory excludes itself and does not authenticate its publisher.")
        return 0
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
