# BlueLink Asset Manifest

**Version:** 1.0.0 | **Issue date:** 20 October 2026 | **Status:** Final  
**Organization:** BlueLink Blockchain Services | **Document ID:** BL-022

## Inventory

This release contains **11 image files: 3 unique original corporate assets and 8 raster derivatives**. Original bytes are unchanged. The byte-identical transparent duplicate is represented in provenance instead of being distributed as another variant.

| ID | Asset | Canvas | Classification |
|---|---|---|---|
| `BL-CORP-001` | [bluelink-icon-1024.png](logos/icons/bluelink-icon-1024.png) | 1024 x 1024 | Derived; upscaled |
| `BL-CORP-002` | [bluelink-icon-128.png](logos/icons/bluelink-icon-128.png) | 128 x 128 | Derived; downsampled |
| `BL-CORP-003` | [bluelink-icon-256.png](logos/icons/bluelink-icon-256.png) | 256 x 256 | Derived; downsampled |
| `BL-CORP-004` | [bluelink-icon-32.png](logos/icons/bluelink-icon-32.png) | 32 x 32 | Derived; downsampled |
| `BL-CORP-005` | [bluelink-icon-512.png](logos/icons/bluelink-icon-512.png) | 512 x 512 | Derived; upscaled |
| `BL-CORP-006` | [bluelink-icon-64.png](logos/icons/bluelink-icon-64.png) | 64 x 64 | Derived; downsampled |
| `BL-CORP-007` | [bluelink-logo-dark-background.jpg](logos/primary/bluelink-logo-dark-background.jpg) | 1024 x 1024 | Supplied original |
| `BL-CORP-008` | [bluelink-logo-light-background.jpg](logos/primary/bluelink-logo-light-background.jpg) | 1024 x 1024 | Supplied original |
| `BL-CORP-009` | [bluelink-monogram-dark-1024.png](logos/secondary/bluelink-monogram-dark-1024.png) | 1024 x 1024 | Derived; upscaled |
| `BL-CORP-010` | [bluelink-monogram-light-1024.png](logos/secondary/bluelink-monogram-light-1024.png) | 1024 x 1024 | Derived; upscaled |
| `BL-CORP-012` | [bluelink-monogram-transparent.png](logos/transparent/bluelink-monogram-transparent.png) | 358 x 358 | Supplied original |

## Source lineage

The native transparent PNG is the source for all eight derived exports. The two supplied JPG presentations are independent originals. Source uploads, byte counts, format, alpha-channel presence, hashes and derivation are recorded in [asset-manifest.json](metadata/asset-manifest.json).

The files `logo.png` and `logo - Copy.png` share the canonical transparent file hash; removing the duplicate from distribution loses no unique artwork. See [source-uploads.json](metadata/source-uploads.json).

## SHA-256 integrity

Use [metadata/SHA256SUMS](metadata/SHA256SUMS) for the image inventory and [metadata/REPOSITORY-SHA256SUMS](metadata/REPOSITORY-SHA256SUMS) for all packaged repository files. The repository checksum list excludes itself to avoid circular hashing.

```bash
python tools/verify_assets.py
python tools/verify_repository.py
```

A matching checksum is not a legal ownership record, a signature or proof that the checksum came from a trusted publisher. Obtain the inventory through a trusted company source.

## Source limits

The transparent original is 358 x 358 pixels. The 512/1024 icons and the 1024 secondary composites are upscaled convenience files. No file in the inventory is native SVG, an editable wordmark, a monochrome master or a separately designated BLT/product mark.
