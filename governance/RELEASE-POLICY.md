# BlueLink Brand Release Policy

**Version:** 1.0.0 | **Issue date:** 20 October 2026 | **Status:** Final  
**Organization:** BlueLink Blockchain Services | **Document ID:** BL-018

## Scope

Brand releases have a separate version history from software releases, deployments and audits. This package is **BlueLink Official Brand Assets v1.0.0**. Its final document state is independent of whether a maintainer has published it on GitHub.

## Publication procedure

Use the intended `bluelink-brand-assets` repository under the company organization. Confirm the remote, inspect staged files, run the integrity checks and identify the real commit before creating the release. Do not use the BLT smart-contract SHA as the brand repository's commit.

```bash
git remote -v
git status --short
python tools/verify_assets.py
python tools/verify_repository.py
git tag --list
git rev-parse HEAD
```

These are local inspection commands, not proof of permission or of a published release. Check that the target version has not already been used. If it has, choose a new appropriate version; do not overwrite an existing published tag.

## Release contents

Publish the intended brand-source commit, the release notes, the final handbook and any intended download package. Include a checksum for an uploaded archive. The release page and tag supply the actual publication timestamp and source commit. Do not insert invented publication metadata into prepublication files.

Use [RELEASE-NOTES.md](../RELEASE-NOTES.md) for the initial release. It states the actual asset scope and exclusions and does not imply that a native vector or a BLT-specific logo is included.

## Tag and asset protection

Use an annotated tag for the selected source commit. Where suitable, configure repository rules and immutable releases. Ordinary tags are not inherently immutable. GitHub's immutable-release feature protects the associated tag and attached assets after publication; this package does not claim the setting has been enabled. When using it, attach all intended assets while the GitHub release is still a draft, then publish. [S10-S11]

The platform's temporary draft-release state is an upload workflow, not the status of this finalized documentation.

## Final verification

Check the rendered README, relative links, source archives, asset downloads, checksums and tag-to-commit relationship after publication. Record the actual event in the repository history. Confirm that external references are labeled correctly and no confidential permissions or corporate records were uploaded.

## Corrections

Issue a new version for changed files. Do not silently replace a released logo, archive or hash under an existing release identity. Explain significant release-note corrections and any withdrawal. Existing external copies may remain available.

Sources: [S10-S11](SOURCES.md). Operational steps: [PUBLISHING.md](../PUBLISHING.md).
