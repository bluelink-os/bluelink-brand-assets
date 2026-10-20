# Contributing to BlueLink Brand Assets

**Version:** 1.0.0 | **Issue date:** 20 October 2026 | **Status:** Final  
**Organization:** BlueLink Blockchain Services | **Document ID:** BL-019

## Contribution scope

Contribute corrections, documentation improvements or artwork changes through a branch and pull request. Do not upload an unrequested redesign or assume that a contribution becomes an official identity merely because it appears in a public issue.

## Before submitting

Confirm you have the rights needed to submit the material for the proposed use. Identify the original source and any third-party component. Keep confidential contracts, personal data, credentials, unreleased designs and proprietary font files out of the submission.

Provide the reason for the change, affected identity and files, expected visual result and any evidence supporting new company or product claims. State when a file is derived or upscaled. A native SVG claim requires actual vector artwork, not an embedded bitmap renamed as a vector.

## File and documentation conventions

Use lowercase descriptive hyphenated asset filenames. Retain uppercase names for the policy files already established in the repository. Keep UTF-8 text and LF line endings. The supplied `.gitattributes` protects text handling across operating systems; do not convert image or PDF files as text.

Update the asset inventory for image changes and the document register for new controlled documents. Keep cross-links relative within the repository. Record source dates for time-sensitive statements and update the changelog.

## Verification

Run `python tools/verify_assets.py` and `python tools/verify_repository.py` against a finalized package. They are verification tools, not automatic inventory updaters; a legitimate content change requires regenerated metadata and checksum records before final packaging. Do not edit a checksum merely to disguise an unexplained file change.

## Review and authority

The appropriate brand, rights or product representative decides changes within their authority. A contribution, issue comment or maintainer merge does not by itself create a trademark license. Use the [asset approval process](governance/ASSET-APPROVAL-POLICY.md) for new identities and sensitive changes.

Report confidential concerns privately under [SECURITY.md](SECURITY.md). Use the issue tracker for nonsensitive documentation errors only.
