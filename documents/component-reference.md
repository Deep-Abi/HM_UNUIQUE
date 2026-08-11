# Component Reference — Source of Truth

This project has **no server-side templating**, so the header, footer, and
both modals are physically duplicated into all 9 HTML files. To keep them
identical (a client-locked requirement — see Phase 1 §1.9), **every one of
the 9 pages was generated from the single script `build_pages.py`** rather
than hand-typed.

## Do not hand-edit header/footer/modal markup in individual pages

If the header, footer, Products dropdown, mobile nav, Quote modal, or
Thank You modal ever need to change:

1. Edit the corresponding `build_*()` function in `build_pages.py`.
2. Re-run `python3 build_pages.py` from the project root.
3. This regenerates all 9 pages with the change applied identically,
   and preserves every page's own `<main>` content, since page sections
   are written directly into each file after generation (Phase 3+) and
   are not touched by the header/footer functions.

> Note: from Phase 3 onward, once `<main>` contains real page sections,
> regenerating with this script would overwrite that content. At that
> point, header/footer/modal changes should be applied with a careful
> find-and-replace across all 9 files instead, using this document to
> confirm the markup is applied identically everywhere. `build_pages.py`
> remains useful as the canonical reference for what "identical" means.

## Canonical component list (see `css/header.css`, `css/footer.css`,
## `css/components.css` for styling)

| Component | Data hooks used by JS |
|---|---|
| Nav toggle (hamburger) | `[data-nav-toggle]` |
| Mobile nav drawer | `[data-mobile-nav]` |
| Mobile nav overlay | `[data-mobile-nav-overlay]` |
| Mobile nav close button | `[data-mobile-nav-close]` |
| Mobile Products accordion toggle | `[data-mobile-submenu-toggle]` |
| Products dropdown (desktop) | `[data-nav-dropdown]`, `[data-nav-dropdown-trigger]` |
| Active nav link marker | `[data-nav-key-link="<key>"]` matched against `<body data-nav-key="<key>">` |
| Header scroll state | `[data-site-header]` |
| Request a Quote trigger (any button/link) | `[data-modal-open="quote"]` |
| Quote modal | `[data-modal="quote"]` |
| Thank You modal | `[data-modal="thank-you"]` |
| Any modal close button | `[data-modal-close]` |
| Quote form | `[data-form="quote"]` |
| Contact form (Phase 3) | `[data-form="contact"]` |
| Scroll-to-top button | `[data-scroll-top]` |
| Current year (footer copyright) | `[data-current-year]` |
| Scroll-reveal element | `[data-animate="fade-up|fade|scale"]` |
| Count-up stat | `[data-count-to="5000"]` + optional `[data-count-suffix="+"]` |
| Lazy background image | `[data-bg-src="path/to/image.jpg"]` |
| Hero slider (Phase 3) | `[data-slider]`, `[data-slider-track]`, `[data-slider-slide]`, `[data-slider-prev]`, `[data-slider-next]`, `[data-slider-dots]` |

## Nav keys

`home`, `electricals`, `electronics`, `hardwares`, `industrial`, `about`,
`contact`, `download-centre`

Each page's `<body>` carries `data-nav-key="<key>"`. The Products dropdown
trigger and the desktop/mobile Electricals/Electronics/Hardwares/Industrial
links all receive `aria-current="page"` automatically when their key
matches the current page.
