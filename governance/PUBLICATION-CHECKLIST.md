# BlueLink Publication Checklist

**Version:** 1.0.0 | **Issue date:** 20 October 2026 | **Status:** Final  
**Organization:** BlueLink Blockchain Services | **Document ID:** BL-025

## Package state

This checklist accompanies a **final v1.0.0 publication package**. It is a repeatable operational control for the person uploading the files, not a request to redraft the documentation. The machine-verifiable build checks are recorded in `metadata/build-validation.json`.

## Before upload

- [ ] Use the company `bluelink-brand-assets` repository, not the BLT smart-contract repository.
- [ ] Confirm the chosen brand tag does not already identify a published release.
- [ ] Extract and upload the repository contents, including `.gitattributes` and `.github` when using Git.
- [ ] Run both integrity tools successfully before modifying or distributing the package.
- [ ] Check that no unrelated private documents, secrets or completed permission forms have been added locally.

## Publish

- [ ] Inspect and commit the intended files; select the actual brand-source commit.
- [ ] Push the source and create the appropriate tag without replacing existing published history.
- [ ] Use the finalized release notes and attach the intended handbook/archive and checksum.
- [ ] Publish the GitHub release; record its actual timestamp and commit through GitHub.

## After publication

- [ ] Open the rendered README and test images and relative links.
- [ ] Download the release artifact and verify its bytes against its checksum.
- [ ] Confirm the tag points to the intended brand commit.
- [ ] Check that official-domain links and scope statements are correct.

The unchecked boxes intentionally represent actions performed by the publisher. They are not fictional claims that publication has already occurred.
