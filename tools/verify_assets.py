#!/usr/bin/env python3
"""Verify released image hashes without changing files. Python 3.9+; no dependencies."""
import json

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
        manifest = json.loads((ROOT / "metadata/asset-manifest.json").read_text(encoding="utf-8"))
        failures = []
        for item in manifest["assets"]:
            path = safe_path(item["path"])
            if sha256(path) != item["sha256"] or path.stat().st_size != item["bytes"]:
                failures.append(item["path"])
        if failures:
            print("FAILED: changed assets\n" + "\n".join(failures), file=sys.stderr)
            return 1
        print(f"PASS: {len(manifest['assets'])} image assets match the manifest.")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
