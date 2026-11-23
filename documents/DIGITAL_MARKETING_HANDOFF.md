# HM UNIQUE — digital marketing setup checklist (updated Batch 31b, 2026-11-23)

No account was created, nothing was submitted or published, no tracking was added, no ads, no spend.

**Status key:** **[P]** Implemented in project · **[T]** Tested locally · **[A]** Requires account access · **[D]** Requires a deployed URL · **[O]** Requires owner confirmation

## 0. The single hostname decision (blocks most items below) — [O]
`https://www.hmunique.com` is an **assumption** used in every canonical, `og:url`, sitemap, robots and JSON-LD URL. **Decision needed:** www or apex (`hmunique.com`)? Whichever is chosen, the other must 301-redirect to it at the host, and `SITE_URL` in `build_pages.py` plus the Worker `ALLOWED_ORIGINS` must match. Changing it later = one constant and a regenerate.

## Presentation changes that affect launch checks (Batch 31b)
- Category name is now "Industrial & Commercial Equipments"; confirm the Business Profile category/wording the owner uses matches.
- Both emails (business@hmunique.com primary, hmunitecenterprises02@gmail.com secondary) show in the Contact hero.
- Home H1 is "Electricals"; re-check it in the live Search Console/inspection views.

## 1. Google Search Console
| Step | Status |
|---|---|
| Empty verification hook: `SEARCH_CONSOLE_VERIFICATION` in `build_pages.py` emits `<meta name="google-site-verification">` only when a token is pasted in (verified: nothing is emitted while empty) | [P][T] |
| Add the property (Domain via DNS TXT, or URL-prefix via the HTML tag) and paste the real token | [A][D][O] |
| Submit `/sitemap.xml` (9 intended URLs, verified locally) | [A][D] |
| URL-inspect home + one category page; request indexing | [A][D] |
| Check Page indexing, Breadcrumbs, FAQ and Organization reports; **no rich result is promised** | [A][D] |
| Confirm Google reports `404.html` as a real 404 (host must serve it with status 404) | [D] |
| Review queries monthly against the proposed themes in `KEYWORD_PAGE_MAP.md` | [A][D] |

## 2. Google Business Profile — nothing is published
| Step | Status |
|---|---|
| Find/claim the profile for No.271, Linghi Chetty Street, George Town, Chennai 600001; owner verification | [A][O] |
| Compare name, address, phone, hours and category with the site. **Address, hours and map have not been freshly verified** | [O] |
| Use only the primary phone +91 97101 81944; the secondary number is hidden and must not be added | [O] |
| Real photos only (site images are AI illustrations; do not upload them as photos of the business) | [O] |
| Keep name/address/phone identical to the site; never seed reviews | [O] |

## 3. Analytics and enquiry-conversion tracking — nothing installed
| Step | Status |
|---|---|
| Decide whether to use analytics, which tool, and whether a consent notice is needed | [O] |
| Privacy policy published first (still unresolved) | [O] |
| Count only **server-accepted** enquiries (the site already shows success only after backend acceptance, so a "success" signal can hook that existing state) | [P] design ready; tracking itself not added |
| Phone click and email click events; **no WhatsApp event** (WhatsApp is hidden) | [O] |
| Catalogue download event once real PDFs exist | [O] |
| Test events in the real analytics account | [A][D] |

## 4. Social profiles
| Step | Status |
|---|---|
| Owner supplies real URLs (Facebook, LinkedIn, Instagram…) | [O] |
| Add them to `SOCIAL_PROFILES` in `build_pages.py` and regenerate: footer icons appear **and** `sameAs` is added to the LocalBusiness JSON-LD automatically (both empty today; no markup emitted) | [P] |

## 5. Launch-time and post-launch checks — [D]
- Fetch `/robots.txt` and `/sitemap.xml` on the live host; confirm status 200 and host consistency.
- Confirm an unknown URL returns HTTP **404** with the `404.html` page (locally this was verified only against a simulated server).
- Confirm www/apex redirect and HTTPS.
- Run Google's Rich Results Test / Schema Markup Validator on the live URLs (**not done: external tools**).
- Run PageSpeed/Lighthouse on the live URLs (**not done**).
- Search Console: coverage after a few weeks; do not expect rankings on a schedule.

## 6. Future content and campaigns (suggestions; need owner-confirmed facts)
Real catalogues and photography; a "how to request a quotation" page once the process is confirmed; buying guides per product group; permissioned customer content (the "100+ clients" claim stays as confirmed, not expanded); directory listings only if the owner chooses; paid campaigns require budget approval — none started.

## Prerequisites owned by other work
Enquiry backend deployed and tested; privacy policy resolved; hosting/DNS and host decision; verified email sender domain.
