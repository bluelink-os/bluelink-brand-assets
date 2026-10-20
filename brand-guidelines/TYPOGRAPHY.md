# BlueLink Typography Standard

**Version:** 1.0.0 | **Issue date:** 20 October 2026 | **Status:** Final  
**Organization:** BlueLink Blockchain Services | **Document ID:** BL-007

## Scope

This type system governs v1.0.0 brand documentation and related digital layouts. It deliberately uses system fonts so the repository does not require distributing font software. It does not identify or replace a font used on a website whose stylesheet has not been inspected.

## Font stacks

Body text, headings and interface labels:

```css
font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
```

Filenames, code and checksums:

```css
font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", monospace;
```

These are fallback references to fonts available in the user's environment, not bundled font files or a redistribution license. GitHub renders Markdown using its own interface typography.

## Digital scale

| Role | Size | Weight | Line height |
|---|---|---|---|
| Page title | 36 px | 700 | 1.15 |
| Major section | 28 px | 700 | 1.25 |
| Subsection | 20 px | 600 | 1.35 |
| Body | 16 px | 400 | 1.60 |
| Caption | 14 px | 400 | 1.45 |
| Code | 14 px | 400 | 1.50 |

Keep paragraphs to a readable line length, normally about 45-80 characters. Use sentence case for headings. Avoid long all-capital passages, fully justified web copy and decorative type in technical identifiers. Permit reflow and zoom rather than enforcing fixed-height text containers.

## Logo and wordmark

The monogram is supplied artwork, not editable typography. Do not recreate it by typing initials in a font. The words BlueLink and BlueLink Token (BLT) may appear as ordinary text without pretending that the result is an official vector wordmark or product lockup.

## New font adoption

A future font change must document the family, source, required weights, fallback stack and relevant web, desktop or application rights. Do not publish proprietary font binaries or assume that a web license permits every other use. Font adoption follows the asset approval process.

## PDF typography

The companion handbook uses a neutral sans-serif document-production face for consistent rendering. That production choice is not an assertion about historical website typography. PDF text should remain selectable; accessible source content is also maintained in Markdown.
