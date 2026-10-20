# Publishing BlueLink Brand Assets

**Version:** 1.0.0 | **Issue date:** 20 October 2026 | **Status:** Final  
**Organization:** BlueLink Blockchain Services | **Document ID:** BL-028

## What is finalized

This directory contains the final v1.0.0 source files and handbook. Upload its contents to the company brand repository. Do not upload the ZIP as the only repository file unless you intentionally want no browsable source tree.

## Before starting

Create or open the company repository named `bluelink-brand-assets`. Work from its intended local folder. Confirm there are no unrelated files, credentials or confidential corporate records in that folder. Do not run the commands from the BLT smart-contract repository.

Run:

```bash
python tools/verify_assets.py
python tools/verify_repository.py
git status
git remote -v
```

If this folder is not yet a Git repository, initialize it with `git init -b main`. If it is already a repository, retain and inspect its existing history instead of initializing over it.

## Connect the correct remote

For a new local repository with no `origin` remote:

```bash
git remote add origin https://github.com/bluelink-os/bluelink-brand-assets.git
```

If `origin` already exists and you have confirmed it should point to this brand repository:

```bash
git remote set-url origin https://github.com/bluelink-os/bluelink-brand-assets.git
```

Run only the command appropriate to the existing configuration. Remote setup does not create the GitHub repository.

## Commit and push

Inspect files before staging and inspect the staged change before committing:

```bash
git add .
git diff --cached --stat
git status
git commit -m "Release BlueLink brand assets v1.0.0"
git branch --show-current
```

For the intended `main` branch:

```bash
git push -u origin main
```

If the remote already has other commits, fetch and reconcile them before pushing. Do not force-push or replace remote history to bypass a rejection.

## Create the release

Inspect the current tags locally and on the remote. Use v1.0.0 only when it is available in this brand repository:

```bash
git tag --list
git ls-remote --tags origin
git rev-parse HEAD
```

After confirming the correct committed source and unused tag:

```bash
git tag -a v1.0.0 -m "BlueLink Official Brand Assets v1.0.0"
git push origin v1.0.0
```

In GitHub, create a release from that tag, title it **BlueLink Official Brand Assets - v1.0.0**, and use `RELEASE-NOTES.md`. Attach the handbook and any intended archive/checksum before publishing, especially when immutable releases are enabled. [S11-S12]

An unchanged delivered archive can be attached with its delivered checksum. If you change or repackage the archive, calculate and publish a new checksum for those exact bytes. Do not reuse the old archive checksum.

This procedure creates a GitHub publication only when you perform it with the authorized account. No remote upload or release publication is performed by the local package itself.

Sources: [S11-S13](governance/SOURCES.md).
