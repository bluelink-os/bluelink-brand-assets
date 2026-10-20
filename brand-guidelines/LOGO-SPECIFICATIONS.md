# BlueLink Logo Specifications

**Version:** 1.0.0 | **Issue date:** 20 October 2026 | **Status:** Final  
**Organization:** BlueLink Blockchain Services | **Document ID:** BL-008

## Original corporate artwork

| File | Native canvas | Format | Intended use |
|---|---|---|---|
| `bluelink-logo-light-background.jpg` | 1024 x 1024 px | JPEG, opaque | Supplied light presentation |
| `bluelink-logo-dark-background.jpg` | 1024 x 1024 px | JPEG, opaque | Supplied dark presentation |
| `bluelink-monogram-transparent.png` | 358 x 358 px | PNG, RGBA | Transparent corporate mark |

Paths and SHA-256 values are listed in [ASSET-MANIFEST.md](../ASSET-MANIFEST.md). Two transparent uploads were byte-identical; one canonical file is distributed. The light and dark JPGs are separately supplied renderings, not a certified pair of geometrically identical recolors.

## Geometry and clear space

Keep the original aspect ratio, silhouette, internal spacing, gradients and orientation. The transparent file's nonzero-alpha bounds are x=29 through 323 and y=19 through 338 inclusive: **295 x 320 pixels** on a 358 x 358 pixel canvas. These bounds include faint edge pixels.

Reserve clear space of **H/8 on every side**, where H is the visible mark height. A 160 px visible mark therefore requires at least 20 px of clear space on each side. Existing canvas padding may count toward that space, but add layout margin whenever it is insufficient. Do not crop the original to eliminate padding.

## Size and background

For ordinary digital identity placements, use at least **64 CSS px of visible mark height**. Compact icons are exceptions: inspect the 32 and 64 px exports at their actual display size and provide an adjacent text label or accessible name where appropriate.

For transparent art, preserve contrast across the whole gradient. The original opaque presentations are the default when a background makes part of the transparent logo disappear. No reversed-white or monochrome artwork is included.

## Raster quality and print

The 512 and 1024 px icons and the 1024 px secondary composites are upscaled derivatives of the 358 px transparent source. They do not contain additional original detail. Use smaller derivatives for compact placements; do not treat a large file dimension as a vector or print-quality guarantee.

Use **20 mm visible height** as the minimum for ordinary print placements, with an actual-size proof. The transparent source's 320 px visible height supports about **27 mm at 300 pixels per inch** without enlargement. High-resolution print, large signage and manufacturing require a suitable native master; none is supplied in this release.

## Alternative text

For an informational corporate image, use `BlueLink corporate logo`. For a linked home-navigation image, use an accessible name that describes the destination, such as `BlueLink home`. Use empty alternative text only when the image is decorative and equivalent identification is already available in context.

## Excluded formats

There is no original SVG, editable wordmark, separate BLT mark, simplified micro-icon or print-certified vector master in v1.0.0. Do not create a purported original by embedding a PNG in an SVG wrapper, auto-tracing without qualification or changing a filename extension.

For future SVG submissions, inspect active content, external references and embedded resources before publication. Record any real conversion method and preserve the source.

Sources: supplied images and reproducible measurements [C02 and M01](../governance/SOURCES.md).
