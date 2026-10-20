# BlueLink Color Palette

**Version:** 1.0.0 | **Issue date:** 20 October 2026 | **Status:** Final  
**Organization:** BlueLink Blockchain Services | **Document ID:** BL-006

## Digital documentation palette

The following color roles apply to v1.0.0 documentation and new brand-library layouts. The values derive from the supplied raster logos, except for the added white neutral. They are **not recovered website CSS, native vector gradient stops or print color specifications**.

| Color | HEX | RGB | Use |
|---|---|---|---|
| Monogram Navy | `#11203F` | 17, 32, 63 | Headings, body text and supporting navy |
| Core Blue | `#155BBC` | 21, 91, 188 | Primary accent and links on white |
| Sky Blue | `#3D90F0` | 61, 144, 240 | Highlight on dark backgrounds; decorative accent |
| Bright Highlight | `#4497F2` | 68, 151, 242 | Decorative accent, not ordinary text on white |
| Dark Surface | `#11131F` | 17, 19, 31 | Dark presentation background |
| Source Light | `#FEFEFE` | 254, 254, 254 | Reference for the supplied light JPG background |
| White | `#FFFFFF` | 255, 255, 255 | Digital document surface |

## Measurement provenance

For the transparent source, the recorded colors use the median RGB of a 3 x 3 pixel region around the recorded coordinate. These are stored RGB values from near-opaque pixels, without compositing a new background. The JPG background references use a 9 x 9 region in the upper-left corner.

The source paths, coordinates and calculated ratios are recorded in [color-samples.json](../metadata/color-samples.json). The digital roles are this edition's standard; pixel sampling does not recover the designer's original color recipe.

## Text contrast

Ratios use WCAG's relative-luminance method. Displayed values are rounded to two decimals; qualification uses unrounded results.

| Pair | Ratio | Normal text, 4.5:1 | Large text, 3:1 |
|---|---|---|---|
| Navy on white | 16.13:1 | Pass | Pass |
| Core blue on white | 6.45:1 | Pass | Pass |
| Sky blue on white | 3.26:1 | Fail | Pass |
| Bright highlight on white | 3.02:1 | Fail | Pass |
| Sky blue on dark surface | 5.67:1 | Pass | Pass |
| White on core blue | 6.45:1 | Pass | Pass |

Use navy or core blue for small text on white. Large text is generally 18 point regular or 14 point bold under the referenced WCAG guidance. A passing flat-color pair does not establish that a whole interface, gradient or document meets WCAG. Test actual use, states and adjacent colors. [S08-S09]

## Production constraints

Preserve the supplied gradient artwork unchanged. Do not generate Pantone, CMYK, embroidery, foil or other manufacturing equivalents from this table. Print and physical production require a suitable source, color-managed proof and separate production approval.

[DESIGN-TOKENS.json](DESIGN-TOKENS.json) is the machine-readable standard. [brand.css](brand.css) supplies the corresponding CSS variables. Neither file redraws or recolors the logo.

Sources: [M01 and S08-S09](../governance/SOURCES.md).
