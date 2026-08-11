Place self-hosted font files here (e.g. .woff2) if/when the project
moves off Google Fonts CDN links to self-hosted fonts for performance
(avoids a third-party render-blocking request). Reference them via
@font-face in css/style.css, keeping the actual family names in sync
with the --font-heading / --font-body tokens in css/variables.css.

Not yet populated — Phase 1-3 fonts are referenced by name only
(Poppins / Inter font-stacks with system-font fallbacks); no external
font request is currently made by the project.
