# Image Performance Guidelines — for Phase 3

Phase 2 deliberately contains no content images (no Hero, no product
photos, no About/Contact imagery — see Phase 2 scope). This document is
the standing convention Phase 3 must follow for every image it adds, so
performance is built in from the first image rather than retrofitted.

## 1. Format strategy — AVIF primary, WebP fallback, JPG/PNG final fallback

Every content photo (product photos, banners, About/Contact photography)
must use `<picture>` with three sources, in this order:

```html
<picture>
  <source srcset="../assets/electricals/wires-cables.avif" type="image/avif" />
  <source srcset="../assets/electricals/wires-cables.webp" type="image/webp" />
  <img
    src="../assets/electricals/wires-cables.jpg"
    alt="FRLS copper wire coils in red, black, and blue"
    width="400"
    height="300"
    loading="lazy"
    decoding="async"
  />
</picture>
```

- The browser picks the first format it supports (AVIF → WebP → JPG/PNG),
  so older browsers still get a working image with no extra markup.
- `width`/`height` are **required** on the `<img>` — this is what
  reserves layout space and prevents the layout shift the Phase 1/2
  responsive requirements explicitly call out ("no layout shift").
- `alt` must always be a real, specific description (see the "Alt text"
  section below) — never left empty or generic on a content image.

## 2. Loading attributes — when to use which

| Image | `loading` | `decoding` | Reason |
|---|---|---|---|
| Header logo | `eager` | `async` | Above the fold on every page, must render immediately |
| Footer logo | `lazy` | `async` | Below the fold on every page |
| Hero image (Home) | `eager` | `async` | Largest Contentful Paint candidate — never lazy-load the hero |
| Every other content image (product photos, category banners, About/Contact photography, icons inside cards) | `lazy` | `async` | Below the fold on first paint |

Only the very first, above-the-fold image on a page should ever be
`eager`. Everything else defaults to `lazy`.

## 3. The `.aspect-box` utility (already built in `utilities.css`)

For any image whose container needs to reserve space before the image
loads (product cards, category cards, banners), wrap the `<picture>` in
the existing `.aspect-box` utility instead of inventing a new pattern:

```html
<div class="aspect-box" style="--aspect-ratio: 66.66%;">
  <picture>
    ...
    <img ... />
  </picture>
</div>
```

`--aspect-ratio` is a CSS custom property already read by
`.aspect-box::before` in `utilities.css` — set it inline per-instance
(e.g. `56.25%` for 16:9, `100%` for a 1:1 square) since it genuinely
varies per image, not per component.

## 4. Alt text

- Alt text must describe what the image actually shows, specific to the
  product/place/person in it — never "image", "photo", or the filename.
- Purely decorative images (background textures, dividers) get
  `alt=""` so screen readers skip them — never omit `alt` entirely.
- Icons already covered by adjacent visible text (e.g. a checkmark next
  to "Quality Assured") should be marked `aria-hidden="true"` rather than
  given alt text, to avoid announcing the same thing twice.

## 5. Background images (CSS)

If a design calls for a CSS background-image instead of an `<img>` (rare
— prefer `<img>`/`<picture>` wherever the image is meaningful content,
reserve CSS backgrounds for purely decorative treatments), use the
`data-bg-src` contract already wired up in `js/lazyload.js`:

```html
<div class="hero-banner" data-bg-src="../assets/about/factory-banner.jpg"></div>
```

`lazyload.js` applies the background via `IntersectionObserver` once the
element is near the viewport — no additional JS needed per page.

## Why this wasn't applied to actual images in Phase 2

Phase 2's explicit scope was the reusable foundation only — no Hero, no
product cards, no page content, per your instructions. There are
currently only two raster/vector assets in the whole project (the two
logo SVGs), and SVG is already the optimal format for a vector logo, so
no AVIF/WebP/`<picture>` conversion applies to it. This document ensures
the very first content image Phase 3 adds follows the convention above
from day one.
