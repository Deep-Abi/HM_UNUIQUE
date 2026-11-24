import os
import re
import json
import html as _htmlmod
from urllib.parse import quote as _urlquote
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------
# SEO base — the canonical domain is not yet registered/confirmed, so a
# placeholder is used consistently across canonical URLs, Open Graph
# og:url, sitemap.xml, and robots.txt. This is the ONE place to update
# once the real domain is live — search for SITE_URL usage.
# ---------------------------------------------------------------------
SITE_URL = "https://www.hmunique.com"

# Footer developer credit (Batch 35). The contact page is contact.html in DeepAbi's own source
# repo (listed in its sitemap; canonical https://www.deepabi.com/contact.html). Live resolution of
# the apex host was not testable from the build sandbox — change only these constants if needed.
DEVELOPER_URL = "https://deepabi.com"
DEVELOPER_CONTACT_URL = "https://deepabi.com/contact.html"
OG_IMAGE_ALT = "HM UNIQUE Technology Enterprises, George Town, Chennai: electricals, electronics components, hardware, industrial and commercial equipment, and industrial safety and packing materials."

# ---------------------------------------------------------------------
# Global contact details — the single source of truth for every phone/
# email/address usage across the site. Update here only; every page
# regenerates from these constants.
# ---------------------------------------------------------------------
# Approved contact numbers (user-approved 2026-10-30). Kept as strings.
# Which person/department answers each number is deliberately NOT stated
# anywhere on the site. PHONE_* = the one active phone number.
# A secondary phone number and its WhatsApp account are TEMPORARILY NOT IN USE (owner
# instruction 2026-11-22), so no constants for them exist and nothing renders them. WhatsApp must
# not be pointed at the primary number unless the owner confirms it supports WhatsApp. To
# re-enable, restore the secondary-phone and WhatsApp constants and their markup from
# backup_pre_unused_number_batch/build_pages.py (a sibling of the project folder).
# EMAIL_PRIMARY / EMAIL_SECONDARY confirmed by the owner 2026-11-21; wherever both
# addresses appear, the primary is listed first.
PHONE_DISPLAY = "+91 97101 81944"
PHONE_TEL = "+919710181944"
PHONE_SCHEMA = "+91-97101-81944"
EMAIL_PRIMARY = "business@hmunique.com"
EMAIL_SECONDARY = "hmunitecenterprises02@gmail.com"


def email_html(address):
    """Visible text of an e-mail address with a preferred line-break point just
    before the "@" (<wbr> adds no character, so copied text and the mailto: href
    stay exactly the address). On a narrow screen the address then wraps as
    "name" / "@domain" instead of splitting inside a word; the CSS keeps
    overflow-wrap as the safety net so nothing can overflow."""
    return address.replace("@", "<wbr>@")
ADDRESS_LINE1 = "No.271, Linghi Chetty Street"
ADDRESS_LINE2 = "George Town, Chennai &ndash; 600001"
ADDRESS_LINE3 = "Tamil Nadu, India"
ADDRESS_FULL_PLAIN = "No.271, Linghi Chetty Street, George Town, Chennai - 600001, Tamil Nadu, India"
# One category list used in every description, tagline and structured-data string so
# the five approved category names (visible label "Hardware") cannot drift apart.
CATEGORY_LIST_HTML = "Electricals, Electronics Components, Hardware, Industrial &amp; Commercial Equipments and Industrial Safety &amp; Packing Materials"
CATEGORY_LIST_PLAIN = "Electricals, Electronics Components, Hardware, Industrial & Commercial Equipments and Industrial Safety & Packing Materials"
MAPS_QUERY = "No.271, Linghi Chetty Street, George Town, Chennai, Tamil Nadu 600001"
MAPS_QUERY_ENCODED = "No.271%2C%20Linghi%20Chetty%20Street%2C%20George%20Town%2C%20Chennai%2C%20Tamil%20Nadu%20600001"

# ---------------------------------------------------------------------
# Page registry: nav key, title, output path, relative depth, breadcrumb,
# meta description, canonical URL (site-relative, from SITE_URL)
# ---------------------------------------------------------------------
PAGES = [
    {
        "key": "home",
        "title": "HM UNIQUE Technology Enterprises | Industrial Supplies in Chennai",
        "path": "index.html",
        "depth": 0,
        "breadcrumb": None,  # no breadcrumb on Home
        "description": "HM UNIQUE Technology Enterprises, George Town, Chennai: electricals, electronic components, hardware, industrial equipment and safety &amp; packing materials.",
        "canonical": "/",
    },
    {
        "key": "electricals",
        "title": "Electrical Supplies in Chennai | HM UNIQUE",
        "path": "pages/electricals.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Electricals", None)],
        "description": "Browse electrical product groups from HM UNIQUE in Chennai: wires &amp; cables, circuit protection, switches, distribution boards and lighting. Request a quote.",
        "canonical": "/pages/electricals.html",
    },
    {
        "key": "electronics",
        "title": "Electronic Components in Chennai | HM UNIQUE",
        "path": "pages/electronics.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Electronics Components", None)],
        "description": "Browse electronic component groups from HM UNIQUE in Chennai: resistors, capacitors, semiconductors, connectors, sensors and power supplies. Request a quote.",
        "canonical": "/pages/electronics.html",
    },
    {
        "key": "hardwares",
        "title": "Hardware Supplies in Chennai | HM UNIQUE",
        "path": "pages/hardwares.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Hardware", None)],
        "description": "Browse hardware groups from HM UNIQUE in Chennai: fasteners, hand and power tools, cutting tools, plumbing fittings and measuring tools. Request a quote.",
        "canonical": "/pages/hardwares.html",
    },
    {
        "key": "industrial",
        "title": "Industrial &amp; Commercial Equipments in Chennai | HM UNIQUE",
        "path": "pages/industrial-equipment.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Industrial &amp; Commercial Equipments", None)],
        "description": "Browse industrial and commercial equipment from HM UNIQUE in Chennai: pumps and motors, bearings, welding equipment, material handling and power backup.",
        "canonical": "/pages/industrial-equipment.html",
    },
    {
        "key": "safety-packing",
        "title": "Industrial Safety &amp; Packing Materials in Chennai | HM UNIQUE",
        "path": "pages/industrial-safety-packing.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Industrial Safety &amp; Packing Materials", None)],
        "description": "Browse industrial safety and packing materials from HM UNIQUE in Chennai: protective equipment, signage, tapes, stretch film and cartons. Request a quote.",
        "canonical": "/pages/industrial-safety-packing.html",
    },
    {
        "key": "about",
        "title": "About HM UNIQUE Technology Enterprises | George Town, Chennai",
        "path": "pages/about.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("About Us", None)],
        "description": "About HM UNIQUE Technology Enterprises: established in 2019, located in George Town, Chennai, with five product categories for commercial and industrial buyers.",
        "canonical": "/pages/about.html",
    },
    {
        "key": "contact",
        "title": "Contact HM UNIQUE | Linghi Chetty Street, George Town, Chennai",
        "path": "pages/contact.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Contact Us", None)],
        "description": "Contact HM UNIQUE Technology Enterprises at No.271, Linghi Chetty Street, George Town, Chennai. Call, email or send an enquiry.",
        "canonical": "/pages/contact.html",
    },
    {
        "key": "download-centre",
        "title": "Download Centre | HM UNIQUE",
        "path": "pages/download-centre.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Download Centre", None)],
        "description": "HM UNIQUE Download Centre: catalogue, company profile and datasheet documents. The files currently listed are drafts pending approval.",
        "canonical": "/pages/download-centre.html",
    },
]

NAV_ITEMS = [
    ("home", "Home", "index.html"),
    # Products is a dropdown, handled separately
    ("about", "About Us", "pages/about.html"),
    ("contact", "Contact Us", "pages/contact.html"),
]

PRODUCT_ITEMS = [
    ("electricals", "Electricals", "pages/electricals.html", "bolt"),
    ("electronics", "Electronics Components", "pages/electronics.html", "chip"),
    ("hardwares", "Hardware", "pages/hardwares.html", "wrench"),
    ("industrial", "Industrial &amp; Commercial Equipments", "pages/industrial-equipment.html", "factory"),
    ("safety-packing", "Industrial Safety &amp; Packing Materials", "pages/industrial-safety-packing.html", "helmet-safety"),
]


def rel(path_from_root, depth):
    """Turn a root-relative path into the correct relative path for a
    page living `depth` folders deep (0 = root, 1 = inside /pages).

    Special case: any path that starts with "pages/" and is being
    resolved from a page that is ALSO inside /pages (depth >= 1) must
    NOT get an extra "../pages/" prefix — those two pages are siblings
    in the same folder, so the link is just the bare filename.
    """
    if path_from_root.startswith("http"):
        return path_from_root

    if path_from_root.startswith("pages/") and depth >= 1:
        return path_from_root[len("pages/"):]

    prefix = "../" * depth
    return f"{prefix}{path_from_root}"


def nav_current(key, current_key):
    return ' aria-current="page"' if key == current_key else ""


def build_utility_bar(current_key, depth):
    return f"""  <div class="utility-bar">
    <div class="container utility-bar__inner">
      <div class="utility-bar__phones">
        <a class="utility-bar__phone" href="tel:{PHONE_TEL}">
          <i class="fa-solid fa-phone" aria-hidden="true"></i>
          <span>{PHONE_DISPLAY}</span>
        </a>
      </div>
      <div class="utility-bar__emails">
        <a class="utility-bar__email" href="mailto:{EMAIL_PRIMARY}">
          <i class="fa-solid fa-envelope" aria-hidden="true"></i>
          <span>{email_html(EMAIL_PRIMARY)}</span>
        </a>
        <a class="utility-bar__email" href="mailto:{EMAIL_SECONDARY}">
          <i class="fa-solid fa-envelope" aria-hidden="true"></i>
          <span>{email_html(EMAIL_SECONDARY)}</span>
        </a>
      </div>
    </div>
  </div>"""


def build_products_dropdown(current_key, depth):
    links = []
    for key, label, path, icon in PRODUCT_ITEMS:
        active = nav_current(key, current_key)
        links.append(
            f"""          <li>
            <a class="products-dropdown__link" href="{rel(path, depth)}" data-nav-key-link="{key}"{active}>
              <span class="products-dropdown__icon" aria-hidden="true">{ICONS[icon]}</span>
              <span class="products-dropdown__text">{label}</span>
            </a>
          </li>"""
        )
    return "\n".join(links)


def build_primary_nav(current_key, depth):
    home_active = nav_current("home", current_key)
    about_active = nav_current("about", current_key)
    contact_active = nav_current("contact", current_key)
    products_open = current_key in {key for key, _label, _path, _icon in PRODUCT_ITEMS}
    products_current = ' aria-current="page"' if products_open else ""

    return f"""      <ul class="primary-nav__list">
        <li class="primary-nav__item">
          <a class="primary-nav__link" href="{rel('index.html', depth)}" data-nav-key-link="home"{home_active}>Home</a>
        </li>
        <li class="primary-nav__item primary-nav__item--dropdown" data-nav-dropdown>
          <button type="button" class="primary-nav__link" data-nav-dropdown-trigger aria-haspopup="true" aria-expanded="false" aria-controls="products-dropdown-menu"{products_current}>
            Products
            <i class="fa-solid fa-chevron-down primary-nav__chevron" aria-hidden="true"></i>
          </button>
          <ul class="products-dropdown" id="products-dropdown-menu">
{build_products_dropdown(current_key, depth)}
          </ul>
        </li>
        <li class="primary-nav__item">
          <a class="primary-nav__link" href="{rel('pages/about.html', depth)}" data-nav-key-link="about"{about_active}>About Us</a>
        </li>
        <li class="primary-nav__item">
          <a class="primary-nav__link" href="{rel('pages/contact.html', depth)}" data-nav-key-link="contact"{contact_active}>Contact Us</a>
        </li>
      </ul>"""


def brand_icon_picture(depth, loading="eager"):
    """Supplied HM UNIQUE icon (cropped transparent derivatives; originals untouched
    in assets/logo/icon/). Decorative: the surrounding link/text carries the name."""
    b = rel("assets/logo/web/hm-unique-icon", depth)
    def ss(ext):
        return f"{b}-48.{ext} 1x, {b}-96.{ext} 2x, {b}-144.{ext} 3x"
    fp = ' fetchpriority="high"' if loading == "eager" else ""
    return (
        f'<picture>'
        f'<source type="image/avif" srcset="{ss("avif")}" />'
        f'<source type="image/webp" srcset="{ss("webp")}" />'
        f'<img src="{b}-96.png" alt="" width="112" height="48" loading="{loading}" decoding="async"{fp} />'
        f'</picture>'
    )



def build_mobile_nav(current_key, depth):
    home_active = nav_current("home", current_key)
    about_active = nav_current("about", current_key)
    contact_active = nav_current("contact", current_key)

    product_links = []
    for key, label, path, icon in PRODUCT_ITEMS:
        active = nav_current(key, current_key)
        product_links.append(
            f'''            <li>
              <a class="mobile-nav__submenu-link" href="{rel(path, depth)}" data-nav-key-link="{key}"{active}>
                <span class="mobile-nav__submenu-icon" aria-hidden="true">{ICONS[icon]}</span>
                <span>{label}</span>
              </a>
            </li>'''
        )
    product_links_html = "\n".join(product_links)

    return f"""  <div class="mobile-nav-overlay" data-mobile-nav-overlay inert></div>
  <nav class="mobile-nav" id="mobile-navigation" data-mobile-nav aria-label="Mobile navigation" aria-hidden="true" inert>
    <div class="mobile-nav__header">
      <a class="site-logo mobile-nav__brand" href="{rel('index.html', depth)}" aria-label="HM UNIQUE home">
        <span class="site-logo__mark">{brand_icon_picture(depth, "lazy")}</span>
        <span class="site-logo__name">HM UNIQUE</span>
      </a>
      <button type="button" class="mobile-nav__close" data-mobile-nav-close aria-label="Close menu"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
    </div>
    <ul class="mobile-nav__list">
      <li><a class="mobile-nav__link" href="{rel('index.html', depth)}" data-nav-key-link="home"{home_active}>Home</a></li>
      <li class="mobile-nav__item" data-mobile-nav-item>
        <button type="button" class="mobile-nav__link mobile-nav__submenu-toggle" data-mobile-submenu-toggle aria-expanded="false" aria-controls="mobile-products-submenu">
          Products
          <i class="fa-solid fa-chevron-down primary-nav__chevron" aria-hidden="true"></i>
        </button>
        <ul class="mobile-nav__submenu" id="mobile-products-submenu">
{product_links_html}
        </ul>
      </li>
      <li><a class="mobile-nav__link" href="{rel('pages/about.html', depth)}" data-nav-key-link="about"{about_active}>About Us</a></li>
      <li><a class="mobile-nav__link" href="{rel('pages/contact.html', depth)}" data-nav-key-link="contact"{contact_active}>Contact Us</a></li>
    </ul>
    <div class="mobile-nav__cta">
      <button type="button" class="btn btn--dark btn--block" data-modal-open="quote">
        Request a Quote
        {ICONS["circle-plus"]}
      </button>
    </div>
  </nav>"""


def build_header(current_key, depth):
    return f"""<header class="site-header" data-site-header>
{build_utility_bar(current_key, depth)}
  <div class="container site-header__inner">
    <a class="site-logo" href="{rel('index.html', depth)}" aria-label="HM UNIQUE home">
      <span class="site-logo__mark">
        {brand_icon_picture(depth, "eager")}
      </span>
      <span class="site-logo__text">
        <span class="site-logo__name">HM UNIQUE</span>
        <span class="site-logo__tagline">Electricals&nbsp;&middot; Electronics&nbsp;&middot; Hardware&nbsp;&middot; Industrial&nbsp;&middot; Safety&nbsp;&amp;&nbsp;Packing</span>
      </span>
    </a>

    <nav class="primary-nav" aria-label="Primary navigation">
{build_primary_nav(current_key, depth)}
    </nav>

    <div class="site-header__actions">
      <button type="button" class="btn btn--dark hide-on-mobile" data-modal-open="quote">
        Request a Quote
        {ICONS["circle-plus"]}
      </button>
      <button type="button" class="nav-toggle" data-nav-toggle aria-label="Open menu" aria-expanded="false" aria-controls="mobile-navigation">
        <span class="nav-toggle__bar"></span>
        <span class="nav-toggle__bar"></span>
        <span class="nav-toggle__bar"></span>
      </button>
    </div>
  </div>
</header>

{build_mobile_nav(current_key, depth)}"""


def build_breadcrumb(breadcrumb, depth):
    if not breadcrumb:
        return ""
    parts = []
    for i, (label, href) in enumerate(breadcrumb):
        if href:
            parts.append(f'<a href="{rel(href.lstrip("./").replace("../", ""), depth) if not href.startswith("..") else href}">{label}</a>')
        else:
            parts.append(f'<span class="breadcrumb__current" aria-current="page">{label}</span>')
        if i < len(breadcrumb) - 1:
            parts.append('<i class="fa-solid fa-chevron-right breadcrumb__sep" aria-hidden="true"></i>')
    inner = "\n      ".join(parts)
    return f"""  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      {inner}
    </nav>
  </div>
"""


# Social profiles. A profile is shown ONLY when it has a real URL here. No profile URL has
# been supplied yet, so none of these three icons is rendered (they used to be inert
# placeholders with no destination). Add the real URL to switch an icon on; do not use a
# generic platform home page.
SOCIAL_PROFILES = (
    ("Facebook", "fa-facebook-f", None),
    ("LinkedIn", "fa-linkedin-in", None),
    ("Instagram", "fa-instagram", None),
)


# Google Search Console HTML-tag verification token. Deliberately EMPTY: the token is issued by Search
# Console after the owner adds the property, and must never be invented. While empty, no meta tag is
# emitted. To use it, paste only the token (the content="..." value Search Console shows) here and
# regenerate.
SEARCH_CONSOLE_VERIFICATION = ""


def build_social_links():
    return "\n          ".join(
        f'<a href="{url}" target="_blank" rel="noopener noreferrer" aria-label="{name}"><i class="fa-brands {icon}" aria-hidden="true"></i></a>'
        for name, icon, url in SOCIAL_PROFILES
        if url
    )


def build_footer(depth):
    social_links_html = build_social_links()
    # No empty container (and no gap) while no social profile URL has been confirmed.
    socials_block = (f'''<div class="site-footer__socials">
          {social_links_html}
        </div>''' if social_links_html.strip() else "")
    return f"""<footer class="site-footer" data-float-avoid=".site-footer__bottom-inner, .site-footer__credit-inner">
  <div class="site-footer__top">
    <div class="container site-footer__grid">
      <div class="site-footer__brand">
        <a class="site-logo site-footer__logo" href="{rel('index.html', depth)}" aria-label="HM UNIQUE home">
          <span class="site-logo__mark site-logo__mark--backed">
            {brand_icon_picture(depth, "lazy")}
          </span>
        </a>
        <p class="site-footer__about">HM UNIQUE Technology Enterprises supplies {CATEGORY_LIST_HTML} for commercial and industrial customers. Established in 2019.</p>
        {socials_block}
      </div>

      <div class="site-footer__col">
        <h3 class="site-footer__heading">Quick Links</h3>
        <ul class="site-footer__links">
          <li><a href="{rel('index.html', depth)}">Home</a></li>
          <li><a href="{rel('pages/about.html', depth)}">About Us</a></li>
          <li><a href="{rel('pages/contact.html', depth)}">Contact Us</a></li>
          <li><a href="{rel('pages/download-centre.html', depth)}">Download Centre</a></li>
        </ul>
      </div>

      <div class="site-footer__col">
        <h3 class="site-footer__heading">Product Categories</h3>
        <ul class="site-footer__links">
          <li><a href="{rel('pages/electricals.html', depth)}">Electricals</a></li>
          <li><a href="{rel('pages/electronics.html', depth)}">Electronics Components</a></li>
          <li><a href="{rel('pages/hardwares.html', depth)}">Hardware</a></li>
          <li><a href="{rel('pages/industrial-equipment.html', depth)}">Industrial &amp; Commercial Equipments</a></li>
          <li><a href="{rel('pages/industrial-safety-packing.html', depth)}">Industrial Safety &amp; Packing Materials</a></li>
        </ul>
      </div>

      <div class="site-footer__col">
        <h3 class="site-footer__heading">Contact Us</h3>
        <ul class="site-footer__contact">
          <li><span>{ADDRESS_LINE1}, {ADDRESS_LINE2}, {ADDRESS_LINE3}</span></li>
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL_PRIMARY}">{email_html(EMAIL_PRIMARY)}</a></li>
          <li><span>Mon &ndash; Sat: 9:00 AM &ndash; 9:00 PM</span></li>
        </ul>
      </div>
    </div>
  </div>

  <div class="site-footer__bottom">
    <div class="container site-footer__bottom-inner">
      <span>&copy; <span data-current-year></span> HM UNIQUE Technology Enterprises. All Rights Reserved.</span>
      <div class="site-footer__bottom-links">
        <a aria-disabled="true">Privacy Policy</a>
        <a aria-disabled="true">Terms &amp; Conditions</a>
      </div>
    </div>
  </div>

  <div class="site-footer__credit-bar">
    <div class="container site-footer__credit-inner">
      <p class="site-footer__credit">Website by <a href="{DEVELOPER_URL}" target="_blank" rel="noopener noreferrer">DeepAbi Innovations<span class="visually-hidden"> (opens in a new tab)</span></a></p>
      <a class="site-footer__credit-cta" href="{DEVELOPER_CONTACT_URL}" target="_blank" rel="noopener noreferrer">Let&rsquo;s Build Together <span aria-hidden="true">&#8599;</span><span class="visually-hidden"> (opens in a new tab)</span></a>
    </div>
  </div>
</footer>"""


def fill_phones(html):
    """Substitutes the phone placeholders in the two shared templates
    that are plain (non-f) strings, from the single set of constants
    at the top of this file."""
    return (html.replace("{PHONE_TEL}", PHONE_TEL)
                .replace("{PHONE_DISPLAY}", PHONE_DISPLAY))


# The floating Call button uses an INLINE SVG (Font Awesome Free 6.5.1 "phone", CC BY 4.0), not the
# icon-font <i>, so it can never render as a blank circle when the external icon font is slow,
# blocked or unavailable, and it needs no asset path (works at any URL depth, incl. 404.html).
def build_floating_actions():
    return fill_phones("""<div class="floating-actions floating-actions--right">
  <a class="floating-btn floating-btn--call" href="tel:{PHONE_TEL}" aria-label="Call HM UNIQUE">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor" aria-hidden="true" focusable="false"><path d="M164.9 24.6c-7.7-18.6-28-28.5-47.4-23.2l-88 24C12.1 30.2 0 46 0 64C0 311.4 200.6 512 448 512c18 0 33.8-12.1 38.6-29.5l24-88c5.3-19.4-4.6-39.7-23.2-47.4l-96-40c-16.3-6.8-35.2-2.1-46.3 11.6L304.7 368C234.3 334.7 177.3 277.7 144 207.3L193.3 167c13.7-11.2 18.4-30 11.6-46.3l-40-96z"/></svg>
  </a>
</div>
<button type="button" class="scroll-top-btn" data-scroll-top aria-label="Scroll to top">
  <i class="fa-solid fa-arrow-up" aria-hidden="true"></i>
</button>""")


def build_quote_modal():
    return fill_phones("""<div class="modal-overlay" data-modal="quote" aria-hidden="true">
  <div class="modal modal--quote" role="dialog" aria-modal="true" aria-labelledby="quote-modal-title">
    <button type="button" class="modal__close" data-modal-close aria-label="Close"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>

    <div class="modal__form-col">
      <div class="modal__header" data-quote-header>
        <span class="modal__header-icon" aria-hidden="true"></span>
        <div>
          <h2 class="modal__title" id="quote-modal-title">Request a Quote</h2>
          <p class="modal__subtitle">Share your requirements and our team will get back to you.</p>
        </div>
      </div>

      <form class="quote-form" data-form="quote" novalidate>
        <div class="form-row">
          <div class="form-field">
            <label class="form-field__label" for="quote-name">Your Name <span class="required">*</span></label>
            <input class="form-field__control" type="text" id="quote-name" name="name" data-required placeholder="Enter your full name" />
            <span class="form-field__error-msg">Please enter your name.</span>
          </div>
          <div class="form-field">
            <label class="form-field__label" for="quote-company">Company Name <span class="required">*</span></label>
            <input class="form-field__control" type="text" id="quote-company" name="company" data-required placeholder="Enter company name" />
            <span class="form-field__error-msg">Please enter your company name.</span>
          </div>
        </div>

        <div class="form-row">
          <div class="form-field">
            <label class="form-field__label" for="quote-email">Email Address <span class="required">*</span></label>
            <input class="form-field__control" type="email" id="quote-email" name="email" data-required data-type="email" placeholder="Enter your email" />
            <span class="form-field__error-msg">Please enter a valid email.</span>
          </div>
          <div class="form-field">
            <label class="form-field__label" for="quote-mobile">Mobile Number <span class="required">*</span></label>
            <input class="form-field__control" type="tel" id="quote-mobile" name="mobile" data-required data-type="phone" placeholder="Enter your mobile number" />
            <span class="form-field__error-msg">Please enter a valid mobile number.</span>
          </div>
        </div>

        <div class="form-row">
          <div class="form-field">
            <label class="form-field__label" for="quote-city">City <span class="required">*</span></label>
            <input class="form-field__control" type="text" id="quote-city" name="city" data-required placeholder="Enter your city" />
            <span class="form-field__error-msg">Please enter your city.</span>
          </div>
          <div class="form-field">
            <label class="form-field__label" for="quote-state">State <span class="required">*</span></label>
            <input class="form-field__control" type="text" id="quote-state" name="state" data-required placeholder="Enter your state" />
            <span class="form-field__error-msg">Please enter your state.</span>
          </div>
        </div>

        <div class="form-row">
          <div class="form-field">
            <label class="form-field__label" for="quote-category">Product Category <span class="required">*</span></label>
            <select class="form-field__control" id="quote-category" name="category" data-required>
              <option value="">Select a category</option>
              <option value="electricals">Electricals</option>
              <option value="electronics">Electronics Components</option>
              <option value="hardwares">Hardware</option>
              <option value="industrial">Industrial &amp; Commercial Equipments</option>
              <option value="safety-packing">Industrial Safety &amp; Packing Materials</option>
            </select>
            <span class="form-field__error-msg">Please select a category.</span>
          </div>
          <div class="form-field">
            <label class="form-field__label" for="quote-product">Product Name</label>
            <input class="form-field__control" type="text" id="quote-product" name="product" placeholder="Enter product name (optional)" />
          </div>
        </div>

        <div class="form-field">
          <label class="form-field__label" for="quote-quantity">Quantity</label>
          <input class="form-field__control" type="text" id="quote-quantity" name="quantity" placeholder="Enter quantity (optional)" />
        </div>

        <div class="form-field">
          <label class="form-field__label" for="quote-message">Message / Requirement <span class="required">*</span></label>
          <textarea class="form-field__control" id="quote-message" name="message" data-required placeholder="Please provide details about your requirement..."></textarea>
          <span class="form-field__error-msg">Please tell us about your requirement.</span>
        </div>

        <div class="form-field">
          <label class="form-checkbox">
            <input type="checkbox" id="quote-privacy" name="privacy" data-required />
            <span>I agree to the <a aria-disabled="true">privacy policy</a>.</span>
          </label>
          <span class="form-field__error-msg">Please agree to the privacy policy to continue.</span>
        </div>

        <div class="form-hp" aria-hidden="true"><label>Leave this field empty<input type="text" name="hp_url" tabindex="-1" autocomplete="off" /></label></div>

        <p class="form-submit-error" data-form-error hidden role="alert">
          Something went wrong sending your request. Please try again, or call us directly at <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.
        </p>

        <button type="submit" class="btn btn--primary btn--block mt-4">
          <span data-submit-label>Submit Request</span>
          <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
        </button>

        <p class="modal__note">
          <i class="fa-solid fa-shield-halved" aria-hidden="true"></i>
          For product enquiries, contact our team.
        </p>
      </form>

      <div class="modal__success" data-quote-success hidden>
        <svg class="modal__success-icon" viewBox="0 0 84 84" aria-hidden="true"><circle cx="42" cy="42" r="38" fill="none" stroke="currentColor" stroke-width="5" /><path d="M24 43l12 12 24-24" fill="none" stroke="currentColor" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" /></svg>
        <h2 class="modal__success-title" id="quote-success-title" data-quote-success-title tabindex="-1"></h2>
        <p class="modal__success-body" data-quote-success-body></p>
        <p class="modal__success-note" data-quote-success-note hidden>We couldn’t send a confirmation email, but your enquiry was received.</p>
        <button type="button" class="btn btn--primary" data-modal-close>Close</button>
      </div>
    </div>

    <aside class="modal__aside-col">
      <h3 class="mb-3">Why Choose HM UNIQUE?</h3>
      <ul class="modal__why-list">
        <li><span aria-hidden="true">&#10003;</span><span><strong>Commercial &amp; Industrial Supplies</strong><br />Products for commercial and industrial requirements.</span></li>
        <li><span aria-hidden="true">&#10003;</span><span><strong>Delivery Enquiries</strong><br />Ask our team about delivery for your requirement.</span></li>
                <li><span aria-hidden="true">&#10003;</span><span><strong>Product Enquiry Support</strong><br />Send your requirement and our team will respond.</span></li>
      </ul>
      <div class="modal__help-box">
        <p><strong>Need Help?</strong><br />Call us at <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
      </div>
    </aside>
  </div>
</div>""")


def build_enquiry_popup():
    """The post-submission confirmation popup (js/enquiry-popup.js). Hidden and empty until the
    server confirms an enquiry; it replaces the old 'Quote Request Submitted' dialog."""
    return """<div class="enquiry-popup" data-enquiry-popup role="status" aria-live="polite" aria-atomic="true" hidden>
  <svg class="enquiry-popup__icon" viewBox="0 0 84 84" aria-hidden="true"><circle cx="42" cy="42" r="38" fill="none" stroke="currentColor" stroke-width="5" /><path d="M24 43l12 12 24-24" fill="none" stroke="currentColor" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" /></svg>
  <div class="enquiry-popup__text" data-enquiry-popup-text></div>
  <button type="button" class="enquiry-popup__close" data-enquiry-popup-close aria-label="Close confirmation"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
</div>"""


def build_enquiry_confirmation():
    """Persistent, dismissible confirmation kept on the page after a Request a Quote success closes its
    dialog (js/quote-success.js). Hidden and empty until the server has confirmed an enquiry."""
    return """<div class="enquiry-confirmation" data-enquiry-confirmation role="status" aria-live="polite" aria-atomic="true" hidden>
  <i class="fa-solid fa-circle-check enquiry-confirmation__icon" aria-hidden="true"></i>
  <div class="enquiry-confirmation__text" data-enquiry-confirmation-text></div>
  <button type="button" class="enquiry-confirmation__close" data-enquiry-confirmation-close aria-label="Dismiss confirmation"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>
</div>"""


PAGE_MAIN_COMMENTS = {
    "home": "Home page sections (Hero, Category Grid, Featured Products, Why Choose Us, Industries Served, CTA) are built in Phase 3.",
    "electricals": "Electricals category page sections (banner, trust badges, sub-category tabs, product grid, catalogue CTA, stats) are built in Phase 3.",
    "electronics": "Electronics Components category page sections are built in Phase 3.",
    "hardwares": "Hardware category page sections are built in Phase 3.",
    "industrial": "Industrial &amp; Commercial Equipments category page sections are built in Phase 3.",
}

# ---------------------------------------------------------------------
# Icon set — minimal, consistent 24x24 stroke icons matching the
# concept's line-icon style. Shared across the Home page sections that
# need them (category cards, trust badges, why-choose-us, industries).
# ---------------------------------------------------------------------
ICONS = {
    "bolt": '<i class="fa-solid fa-bolt" aria-hidden="true"></i>',
    "chip": '<i class="fa-solid fa-microchip" aria-hidden="true"></i>',
    "wrench": '<i class="fa-solid fa-wrench" aria-hidden="true"></i>',
    "factory": '<i class="fa-solid fa-industry" aria-hidden="true"></i>',
    "helmet-safety": '<i class="fa-solid fa-helmet-safety" aria-hidden="true"></i>',
    "grid": '<i class="fa-solid fa-table-cells" aria-hidden="true"></i>',
    "shield-check": '<i class="fa-solid fa-shield-halved" aria-hidden="true"></i>',
    "award": '<i class="fa-solid fa-award" aria-hidden="true"></i>',
    "truck": '<i class="fa-solid fa-truck" aria-hidden="true"></i>',
    "tag": '<i class="fa-solid fa-tag" aria-hidden="true"></i>',
    "headset": '<i class="fa-solid fa-headset" aria-hidden="true"></i>',
    "hard-hat": '<i class="fa-solid fa-hard-hat" aria-hidden="true"></i>',
    "droplet": '<i class="fa-solid fa-droplet" aria-hidden="true"></i>',
    "building": '<i class="fa-solid fa-building" aria-hidden="true"></i>',
    "gear": '<i class="fa-solid fa-gear" aria-hidden="true"></i>',
    "box": '<i class="fa-solid fa-box" aria-hidden="true"></i>',
    "boxes-stacked": '<i class="fa-solid fa-boxes-stacked" aria-hidden="true"></i>',
    "triangle-exclamation": '<i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i>',
    "users": '<i class="fa-solid fa-users" aria-hidden="true"></i>',
    "circle-check": '<i class="fa-solid fa-circle-check" aria-hidden="true"></i>',
    "landmark": '<i class="fa-solid fa-building-columns" aria-hidden="true"></i>',
    "lightbulb": '<i class="fa-solid fa-lightbulb" aria-hidden="true"></i>',
    "city": '<i class="fa-solid fa-city" aria-hidden="true"></i>',
    "gears": '<i class="fa-solid fa-gears" aria-hidden="true"></i>',
    "diagram-project": '<i class="fa-solid fa-diagram-project" aria-hidden="true"></i>',
    "arrow-right": '<i class="fa-solid fa-arrow-right" aria-hidden="true"></i>',
    "circle-plus": '<i class="fa-solid fa-circle-plus" aria-hidden="true"></i>',
    "circle-right": '<i class="fa-solid fa-circle-right" aria-hidden="true"></i>',
    "play": '<i class="fa-solid fa-play" aria-hidden="true"></i>',
    "chevron-left": '<i class="fa-solid fa-chevron-left" aria-hidden="true"></i>',
    "chevron-right": '<i class="fa-solid fa-chevron-right" aria-hidden="true"></i>',
    "placeholder-image": '<i class="fa-regular fa-image" aria-hidden="true"></i>',
    "check": '<i class="fa-solid fa-check" aria-hidden="true"></i>',
    "download": '<i class="fa-solid fa-download" aria-hidden="true"></i>',
    "file": '<i class="fa-solid fa-file-lines" aria-hidden="true"></i>',
    "cable": '<i class="fa-solid fa-plug" aria-hidden="true"></i>',
    "screw": '<i class="fa-solid fa-screwdriver" aria-hidden="true"></i>',
    "pump": '<i class="fa-solid fa-gauge-high" aria-hidden="true"></i>',
    "map-pin": '<i class="fa-solid fa-location-dot" aria-hidden="true"></i>',
    "clock": '<i class="fa-solid fa-clock" aria-hidden="true"></i>',
    "phone": '<i class="fa-solid fa-phone" aria-hidden="true"></i>',
    "mail": '<i class="fa-solid fa-envelope" aria-hidden="true"></i>',
    "target": '<i class="fa-solid fa-bullseye" aria-hidden="true"></i>',
    "compass": '<i class="fa-solid fa-compass" aria-hidden="true"></i>',
    "handshake": '<i class="fa-solid fa-handshake" aria-hidden="true"></i>',
    "milestone": '<i class="fa-solid fa-timeline" aria-hidden="true"></i>',
}


def img_placeholder(label, ratio_class=""):
    """Neutral placeholder box standing in for a real photo/illustration
    that hasn't been supplied yet (only the concept PDF was provided,
    not source image files). Keeps the exact aspect ratio the layout
    needs (via an aspect-box modifier CLASS, never an inline style) so
    swapping in the final asset later requires no layout change — see
    documents/image-guidelines.md."""
    box_class = f"aspect-box {ratio_class}".strip()
    return f"""<div class="{box_class}" role="img" aria-label="{label} — placeholder, pending final product photography">
              <div class="img-placeholder">{ICONS['placeholder-image']}</div>
            </div>"""


# One approved photo shared by every CTA band above the footer (Home, About, Contact and
# Download Centre), so the closing band looks the same on each page. The file stays in
# assets/images/common/footer/ and is 1672 x 941 (16:9). The Home/About/Contact slots are 16:9;
# the Download Centre slot is square, so the same photo is centre-cropped there (object-fit: cover).
# `depth` goes through rel() so the URLs resolve from index.html and from pages/. Alt text
# describes only what is visible and does not claim the products belong to HM UNIQUE.
CTA_IMAGE = {
    "dir": "assets/images/common/footer",
    "stem": "hm-unique-quote-banner-product-assortment",
    "width": 1672,
    "height": 941,
    "alt": "Circuit breaker, proximity sensor, brass fittings, safety helmet, cardboard carton and ball bearing arranged on a dark teal surface.",
}


def cta_band_picture(depth, ratio_class="aspect-box--wide"):
    """<picture> (AVIF, WebP, JPG fallback) filling the aspect-box of a CTA band."""
    img = CTA_IMAGE
    path = lambda ext: rel(f"{img['dir']}/{ext}/{img['stem']}.{ext}", depth)
    return f"""<div class="aspect-box {ratio_class}">
            <picture>
              <source srcset="{path('avif')}" type="image/avif">
              <source srcset="{path('webp')}" type="image/webp">
              <img
                src="{path('jpg')}"
                width="{img['width']}"
                height="{img['height']}"
                alt="{img['alt']}"
                loading="lazy"
                decoding="async">
            </picture>
          </div>"""


# Contact > Chennai Branch card. The supplied image is an AI-generated conceptual
# storefront illustration (not a photograph of the actual branch), so the alt text says
# so and a small visible caption repeats it. The file stays in assets/images/contact/chennai_branch/
# (1672 x 941, 16:9) in AVIF, WebP and JPG. `depth` goes through rel() like every other image.
CHENNAI_BRANCH_IMAGE = {
    "dir": "assets/images/contact/chennai_branch",
    "stem": "chennai_branch",
    "width": 1672,
    "height": 941,
    "alt": "Conceptual storefront illustration of the HM UNIQUE Chennai branch.",
    "caption": "Illustrative representation",
}


def chennai_branch_figure(depth):
    """<figure> with a <picture> (AVIF, WebP, JPG fallback) and a short caption.
    The 16:9 box matches the file's ratio and the image is contained, so the
    whole illustration is always visible at any width."""
    img = CHENNAI_BRANCH_IMAGE
    path = lambda ext: rel(f"{img['dir']}/{ext}/{img['stem']}.{ext}", depth)
    return f"""<figure class="branch-card__figure">
              <div class="aspect-box aspect-box--wide">
                <picture>
                  <source srcset="{path('avif')}" type="image/avif">
                  <source srcset="{path('webp')}" type="image/webp">
                  <img
                    src="{path('jpg')}"
                    width="{img['width']}"
                    height="{img['height']}"
                    alt="{img['alt']}"
                    loading="lazy"
                    decoding="async">
                </picture>
              </div>
              <figcaption class="branch-card__caption">{img['caption']}</figcaption>
            </figure>"""


# About > Who We Are: four square photos (1254 x 1254), files kept in assets/images/about_us/.
# Alt text describes only what is visible; nothing says the parts or people belong to HM UNIQUE.
WHO_WE_ARE_IMAGES = [
    ("01-project-requirements", "Hands holding a stainless steel threaded fitting beside a technical drawing of the same part."),
    ("02-product-range", "Metal shelving unit holding a coil of blue cable, terminal blocks, a circuit breaker, brass fittings and a ball bearing."),
    ("03-product-inspection", "Gloved hands measuring a round metal flange with a vernier caliper."),
    ("04-order-preparation", "Hands sealing a cardboard carton with a tape dispenser."),
]
WHO_WE_ARE_IMAGE_SIZE = 1254


# About > Our Vision / Our Mission: one 16:9 photo (1672 x 941) at the top of each card, files kept
# in assets/images/about_us/. Alt text describes only what is visible.
VISION_MISSION_IMAGES = {
    "vision": ("industrial-logistics-park", "Aerial view of large modern warehouse buildings with loading bays, trucks and landscaped roads at sunset."),
    "mission": ("industrial-parts-packing", "Worker in a dark blue uniform handling a clear bag containing a metal component, with more bagged parts in storage bins."),
}


def vision_mission_picture(key, depth):
    stem, alt = VISION_MISSION_IMAGES[key]
    path = lambda ext: rel(f"assets/images/about_us/{ext}/{stem}.{ext}", depth)
    return f"""<div class="aspect-box aspect-box--wide vision-mission__media">
              <picture>
                <source srcset="{path('avif')}" type="image/avif">
                <source srcset="{path('webp')}" type="image/webp">
                <img
                  src="{path('jpg')}"
                  width="1672"
                  height="941"
                  alt="{alt}"
                  loading="lazy"
                  decoding="async">
              </picture>
            </div>"""


def who_we_are_picture(index, depth):
    """<picture> for Who We Are slot `index` (0-3) inside a square .aspect-box."""
    stem, alt = WHO_WE_ARE_IMAGES[index]
    path = lambda ext: rel(f"assets/images/about_us/{ext}/{stem}.{ext}", depth)
    return f"""<div class="aspect-box aspect-box--square">
            <picture>
              <source srcset="{path('avif')}" type="image/avif">
              <source srcset="{path('webp')}" type="image/webp">
              <img
                src="{path('jpg')}"
                width="{WHO_WE_ARE_IMAGE_SIZE}"
                height="{WHO_WE_ARE_IMAGE_SIZE}"
                alt="{alt}"
                loading="lazy"
                decoding="async">
            </picture>
          </div>"""


def build_home_main():
    # -------------------------------------------------------------
    # 3. HERO BANNER
    #
    # Five slides (one per product category; slide 5 has no image yet), each a
    # self-contained mini-hero with its own photo, copy and CTA — see
    # css/pages/home.css's header comment. This block was previously
    # out of sync with the real, hand-finished markup in index.html
    # (it still generated 5 identical image-placeholder slides from an
    # earlier phase); it's brought up to date here, content copied
    # verbatim from the approved index.html, including Batch 3's
    # accessibility additions (the play/pause control and each slide's
    # static aria-hidden/inert baseline), so a future regeneration
    # reproduces the real hero instead of overwriting it with
    # placeholders.
    # -------------------------------------------------------------
    hero_slides_data = [
        {
            "img_base": "electricals_hero",
            "img_w": 1717,
            "img_h": 916,
            "loading": "eager",
            "fetchpriority": ' fetchpriority="high"',
            "alt": "Collection of HM UNIQUE electrical products including a distribution panel, MCBs, cable reels, switches, sockets and an LED flood light",
            "eyebrow": "HM UNIQUE Technology Enterprises",
            "title_tag": "h1",
            "title_html": '<span class="text-accent">Electricals</span>',
            "desc": "Supplying electrical products for residential, commercial and industrial applications.",
            "badges": [
                ("users", "Wide Product Range"),
                ("circle-check", "Product Enquiry Support"),
                ("landmark", "Commercial &amp; Industrial Supplies"),
                ("box", "Delivery Enquiries"),
            ],
            "cta_label": "Explore Electricals",
            "cta_href": "pages/electricals.html",
        },
        {
            "img_base": "electronics_components_hero",
            "img_w": 1717,
            "img_h": 916,
            "loading": "lazy",
            "fetchpriority": "",
            "alt": "Collection of electronics tools and equipment including a soldering station, hot-air rework tool, digital multimeter, solder reel, screwdriver bit set, tweezers, pliers and crimpers",
            "eyebrow": "Smart Electronics. Practical Solutions.",
            "title_html": '<span class="text-accent">Electronics Components</span>',
            "desc": "Electronic components, test instruments and tools for automation, control and industrial applications.",
            "badges": [
                ("chip", "Electronics Components"),
                ("circle-check", "Product Enquiry Support"),
                ("grid", "Wide Selection"),
                ("headset", "Technical Support"),
            ],
            "cta_label": "Explore Electronics",
            "cta_href": "pages/electronics.html",
        },
        {
            "img_base": "hardwares_hero",
            "img_w": 1672,
            "img_h": 941,
            "loading": "lazy",
            "fetchpriority": "",
            "alt": "Collection of HM UNIQUE hardware and tools including a cordless drill, circular saw, angle grinder, toolbox, wrenches, pliers and screwdrivers",
            "eyebrow": "Built for Every Project.",
            "title_html": 'Tools &amp; <span class="text-accent">Hardware</span>',
            "desc": "Hand tools, power tools, fasteners and hardware for professional and industrial applications.",
            "badges": [
                ("shield-check", "Product Enquiry Support"),
                ("grid", "Wide Range"),
                ("wrench", "Professional Tools"),
                ("circle-check", "Contact Us for Availability"),
            ],
            "cta_label": "Explore Hardware",
            "cta_href": "pages/hardwares.html",
        },
        {
            # Slide 4 keeps its original Industrial & Commercial Equipments
            # image. (A 2026-10-28 instruction to temporarily reuse the
            # Electronics hero here was SUPERSEDED before release: the
            # Electronics image then in use showed products the client does
            # not sell. That image has since been replaced by an approved
            # one; slide 4 keeps its own image.)
            "img_base": "industrial_commercial_equipment_hero",
            "img_w": 1672,
            "img_h": 941,
            "loading": "lazy",
            "fetchpriority": "",
            "alt": "Collection of HM UNIQUE industrial equipment including an electric motor, pump, control panel, variable frequency drives, safety gear and cabling",
            "eyebrow": "INDUSTRIAL &amp; COMMERCIAL EQUIPMENTS",
            "title_html": 'Industrial &amp; <span class="text-accent">Commercial Equipments</span>',
            "desc": "Explore our industrial and commercial equipment range and contact us to discuss your requirements.",
            "badges": [
                ("factory", "Industrial Equipment"),
                ("landmark", "Commercial &amp; Industrial Supplies"),
                ("grid", "Wide Applications"),
                ("headset", "Product Enquiry Support"),
            ],
            "cta_label": "Explore Industrial Equipment",
            "cta_href": "pages/industrial-equipment.html",
        },
        {
            # Slide 5 now uses the approved image (2026-10-30). The files
            # supplied on disk are named "industrial_safety_&_packing
            # materials_hero.{avif,webp,jpg}" (an "&" and a space, unsafe in
            # URLs/srcset), so byte-identical URL-safe copies named
            # industrial_safety_packing_materials_hero.* are what the markup
            # references. The "no_image" flag / .hero__slide--no-image
            # treatment is no longer used by any slide; the generator branch
            # is kept so a future image-less slide still works. Like slides
            # 1-4 it carries four icon-and-text highlights (added 2026-10-31).
            # Bright cardboard/packing sits behind the copy on narrow screens,
            # so this slide gets a slightly stronger scrim below 992px
            # (css/pages/home.css, .hero__slide--packing).
            "extra_class": "hero__slide--packing",
            "img_base": "industrial_safety_packing_materials_hero",
            "img_w": 1717,
            "img_h": 916,
            "loading": "lazy",
            "fetchpriority": "",
            "alt": "Collection of safety and packing supplies including a yellow hard hat, hi-visibility vest, ear defenders, safety goggles, work gloves, safety boots, cardboard boxes, stretch film, bubble wrap, packing tape and strapping",
            "eyebrow": "INDUSTRIAL SAFETY &amp; PACKING MATERIALS",
            "title_html": 'Industrial Safety &amp; <span class="text-accent">Packing Materials</span>',
            "desc": "Explore safety and packing supplies for industrial and commercial requirements. Contact us to discuss your needs.",
            "badges": [
                ("helmet-safety", "Personal Protection"),
                ("triangle-exclamation", "Workplace Safety"),
                ("box", "Packing Materials"),
                ("boxes-stacked", "Packing Accessories"),
            ],
            "cta_label": "Explore Safety &amp; Packing",
            "cta_href": "pages/industrial-safety-packing.html",
        },
    ]

    def build_hero_slide(slide, index):
        badges_html = "\n".join(
            f'''              <div class="trust-badge">
                <span class="trust-badge__icon">{ICONS[icon]}</span>
                <span>{label}</span>
              </div>'''
            for icon, label in slide["badges"]
        )
        # Every slide except the first starts aria-hidden + inert, so a
        # page that loads with JS disabled or still initializing never
        # exposes 2-4's links/buttons to keyboard or assistive tech —
        # the same static-baseline-plus-JS-toggle pattern already used
        # for the mobile nav drawer (see build_mobile_nav()). Once
        # slider.js runs, it owns this state from here via goTo().
        hidden_attrs = ' aria-hidden="true" inert' if index > 0 else ""
        # The page's single <h1> stays exposed to assistive tech while its slide is
        # inactive (js/slider.js masks everything else in that slide).
        persist = " data-slider-persistent-heading" if slide.get("title_tag") == "h1" else ""
        if slide.get("no_image"):
            slide_class = "hero__slide hero__slide--no-image"
            media_html = '<div class="hero__slide-media hero__slide-media--navy" aria-hidden="true"></div>'
        else:
            slide_class = "hero__slide" + (f" {slide['extra_class']}" if slide.get("extra_class") else "")
            media_html = f"""<div class="hero__slide-media">
              <picture>
                <source srcset="assets/images/home/hero/avif/{slide['img_base']}.avif" type="image/avif" />
                <source srcset="assets/images/home/hero/webp/{slide['img_base']}.webp" type="image/webp" />
                <img
                  src="assets/images/home/hero/jpg/{slide['img_base']}.jpg"
                  alt="{slide['alt']}"
                  width="{slide['img_w']}"
                  height="{slide['img_h']}"
                  loading="{slide['loading']}"
                  decoding="async"{slide['fetchpriority']}
                />
              </picture>
            </div>"""
        if slide["badges"]:
            badges_block = f"""

              <div class="hero__badges">
{badges_html}
              </div>"""
        else:
            badges_block = ""
        return f"""          <div class="{slide_class}" data-slider-slide{hidden_attrs}>
            {media_html}
            <div class="hero__slide-overlay"></div>
            <div class="container hero__inner">
              <div class="hero__content">
              <span class="eyebrow hero__eyebrow">{slide['eyebrow']}</span>
              <{slide.get("title_tag","h2")} class="hero__title"{persist}>{slide['title_html']}</{slide.get("title_tag","h2")}>
              <p class="hero__desc">{slide['desc']}</p>{badges_block}

              <div class="hero__actions">
                <a class="btn btn--primary" href="{slide['cta_href']}">
                  {slide['cta_label']}
                  {ICONS['circle-right']}
                </a>
                <a class="hero__watch-link" href="pages/about.html">
                  <span class="hero__watch-link__icon">{ICONS['play']}</span>
                  About HM UNIQUE
                </a>
              </div>
            </div>
            </div>
            </div>"""

    hero_slides_html = "\n".join(
        build_hero_slide(slide, i) for i, slide in enumerate(hero_slides_data)
    )

    hero_html = f"""    <section class="hero text-on-dark" aria-label="Hero" data-slider data-float-avoid=".hero__content, .hero__nav, .hero__pager" tabindex="-1">
      <div class="hero__slider-track" data-slider-track>
{hero_slides_html}
      </div>

      <button type="button" class="btn-icon hero__nav hero__nav--prev" data-slider-prev aria-label="Previous slide">{ICONS['chevron-left']}</button>
      <button type="button" class="btn-icon hero__nav hero__nav--next" data-slider-next aria-label="Next slide">{ICONS['chevron-right']}</button>
      <div class="hero__pager">
        <button type="button" class="btn-icon hero__nav hero__nav--playpause" data-slider-playpause aria-label="Pause slideshow">
          <i class="fa-solid fa-pause" aria-hidden="true" data-slider-playpause-icon></i>
        </button>
        <div class="hero__dots" data-slider-dots aria-label="Slide navigation"></div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # 4. PRODUCT CATEGORIES
    # -------------------------------------------------------------
    categories = [
        ("bolt", "Electricals", "Wires &amp; Cables, Switches, MCBs, Distribution Boards, Lighting &amp; more.", "pages/electricals.html"),
        ("chip", "Electronics Components", "Sensors, Power Supplies, Automation, Test Instruments &amp; more.", "pages/electronics.html"),
        ("wrench", "Hardware", "Fasteners, Hand Tools, Power Tools, Safety, Plumbing &amp; more.", "pages/hardwares.html"),
        ("factory", "Industrial &amp; Commercial Equipments", "Motors, Bearings, Pneumatics, Hydraulics, Welding &amp; more.", "pages/industrial-equipment.html"),
        ("helmet-safety", "Industrial Safety &amp; Packing Materials", "Protective equipment, workplace safety and packing materials.", "pages/industrial-safety-packing.html"),
    ]
    # Approved card photos (deployment-relative paths, exact file names/casing as uploaded; all
    # 700x467). A category with no upload keeps its placeholder. Only formats that exist are
    # listed (AVIF first, then WebP; the JPG is the fallback <img>). Keys match the names above.
    CARD_IMG_DIR = "assets/images/home/explore_our_product_categories"

    def _card_img(stem, alt):
        return {
            "avif": f"{CARD_IMG_DIR}/avif/{stem}.avif",
            "webp": f"{CARD_IMG_DIR}/webp/{stem}.webp",
            "jpg": f"{CARD_IMG_DIR}/jpg/{stem}.jpg",
            "width": 700,
            "height": 467,
            "alt": alt,
        }

    category_card_images = {
        "Electricals": _card_img(
            "electricals-category",
            "Electrical distribution board, circuit breakers, coiled cable, switch and LED bulb.",
        ),
        "Electronics Components": _card_img(
            "electronics-components-category",
            "Electronic circuit board, power supply, proximity sensor, digital multimeter and small components.",
        ),
        "Hardware": _card_img(
            "hardwares-category",
            "Cordless drill, spanner, screwdriver, bolts and nuts, and brass fittings.",
        ),
        "Industrial &amp; Commercial Equipments": _card_img(
            "industrial-commercial-equipment",
            "Electric motor, centrifugal pump, hydraulic cylinder and ball bearings.",
        ),
        "Industrial Safety &amp; Packing Materials": _card_img(
            "industrial-safety-packing-materials-category",
            "Safety helmet, goggles, gloves, cardboard carton, stretch wrap roll and packing tape.",
        ),
    }

    def category_card_media(name):
        img = category_card_images.get(name)
        if not img:
            return img_placeholder(name + ' category image')
        sources = "".join(
            f'\n                <source\n                  srcset="{img[ext]}"\n                  type="image/{ext}">'
            for ext in ("avif", "webp")
            if img.get(ext)
        )
        return (
            f'<picture>{sources}\n'
            f'                <img\n'
            f'                  src="{img["jpg"]}"\n'
            f'                  width="{img["width"]}"\n'
            f'                  height="{img["height"]}"\n'
            f'                  alt="{img["alt"]}"\n'
            f'                  loading="lazy"\n'
            f'                  decoding="async"\n'
            f'                  class="category-card__img">\n'
            f'              </picture>'
        )

    category_cards_html = "\n".join(
        f"""          <article class="card card--hover category-card" data-animate="fade-up">
            <span class="card__icon">{ICONS[icon]}</span>
            <div class="category-card__media">
              {category_card_media(name)}
            </div>
            <h3 class="category-card__title">{name}</h3>
            <p class="category-card__desc">{desc}</p>
            <a class="btn btn--outline btn--sm" href="{href}">
              Explore Category<span class="visually-hidden">: {name}</span>
              {ICONS['arrow-right']}
            </a>
          </article>"""
        for icon, name, desc, href in categories
    )

    categories_html = f"""    <section class="section section--light" aria-labelledby="categories-heading">
      <div class="container">
        <div class="section-heading section-heading--center" id="product-categories">
          <span class="eyebrow">Our Categories</span>
          <h2 class="section-heading__title" id="categories-heading">Explore Our <span class="text-accent">Product Categories</span></h2>
          <p class="section-heading__subtitle">HM UNIQUE Technology Enterprises is located in George Town, Chennai. Choose a category to see the product groups listed, then send an enquiry or request a quote.</p>
        </div>
        <div class="grid grid--4 category-grid">
{category_cards_html}
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # 5. FEATURED PRODUCTS
    # -------------------------------------------------------------
    # Approved assortment photos (assets/images/home/handpicked_products/{avif,webp,jpg}/<stem>.<ext>,
    # all 1254x1254). Generic showcase copy only: no brand, stock, performance, specification or
    # certification claims. Each card links to its main category page.
    HP_DIR = "assets/images/home/handpicked_products"
    products = [
        ("Electrical Supplies", "Wires, circuit protection, switches and lighting supplies.",
         "electrical_supplies", "Coil of teal electrical wire, a single-pole circuit breaker, a white switch and socket plate and a round LED downlight on a white platform.",
         "pages/electricals.html"),
        ("Electronics Components", "Relays, capacitors, resistors and terminal blocks.",
         "electronics_components", "Clear relay, two black capacitors, three resistors and a green terminal block on a white platform.",
         "pages/electronics.html"),
        ("Hardware Tools", "Hand tools for installation, maintenance and workshop tasks.",
         "hardware_tools", "Hammer, adjustable spanner, pliers, flat screwdriver and a yellow measuring tape arranged on a white surface.",
         "pages/hardwares.html"),
        ("Industrial &amp; Commercial Products", "Valves, bearings, couplings, pneumatic components and gauges.",
         "industrial_commercial_products", "Brass valve with a teal handle, ball bearings, a shaft coupling, a teal-ended pneumatic cylinder and a navy-and-yellow pressure gauge.",
         "pages/industrial-equipment.html"),
        ("Industrial Safety &amp; Packing Supplies", "Protective equipment and materials for workplace safety and packing.",
         "industrial_safety_packing_materials", "Yellow safety helmet, work gloves, clear safety goggles, brown packing tape and a roll of stretch film.",
         "pages/industrial-safety-packing.html"),
    ]

    def handpicked_picture(stem, alt):
        return (
            f'<picture>\n'
            f'                <source srcset="{HP_DIR}/avif/{stem}.avif" type="image/avif">\n'
            f'                <source srcset="{HP_DIR}/webp/{stem}.webp" type="image/webp">\n'
            f'                <img src="{HP_DIR}/jpg/{stem}.jpg" width="1254" height="1254" alt="{alt}" loading="lazy" decoding="async" class="product-card__img">\n'
            f'              </picture>'
        )

    product_cards_html = "\n".join(
        f"""          <article class="card card--hover product-card" data-animate="fade-up">
            <div class="product-card__media">
              {handpicked_picture(stem, alt)}
            </div>
            <h3 class="product-card__title">{name}</h3>
            <p class="product-card__desc">{desc}</p>
            <a class="btn btn--outline btn--block" href="{href}">Explore Products</a>
          </article>"""
        for name, desc, stem, alt, href in products
    )

    featured_html = f"""    <section class="section section--surface" aria-labelledby="featured-heading">
      <div class="container">
        <div class="section-header-row mb-6">
          <div class="section-heading">
            <span class="eyebrow">Featured Products</span>
            <h2 class="section-heading__title" id="featured-heading">Handpicked Products</h2>
          </div>
          <a class="link-arrow" href="#product-categories">
            View All Products
            {ICONS['arrow-right']}
          </a>
        </div>
        <div class="grid featured-grid">
{product_cards_html}
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # 5b. SAFETY & PACKING GROUPS
    # Three cards below Handpicked Products, one per sub-group of the
    # Industrial Safety & Packing Materials page. They replace the former
    # single full-width category card. Each links straight to a group on
    # pages/industrial-safety-packing.html using that page's own group key as
    # the URL fragment (see js/pages/industrial-safety-packing-catalog.js,
    # which activates the matching tab). Keys in use: "hand-body-protection"
    # (the first protective-equipment group), "workplace-safety-signage-fire-safety"
    # and "cartons-strapping-packing-accessories" (the group that carries the
    # "Packing Accessories" label; the other two packing groups are one tab away).
    # Pre-Step-21 fragments still resolve through OLD_KEY_ALIASES in that script. Descriptions
    # are deliberately generic showcase copy: no product, brand, specification
    # or certification claim. Images are the approved landscape photos in
    # assets/images/home/explore_safety_&_packing_supplies/.
    # -------------------------------------------------------------
    SP_DIR = "assets/images/home/explore_safety_&amp;_packing_supplies"
    safety_packing_groups = [
        ("helmet-safety", "Personal Protective Equipment", "Helmets, gloves, safety eyewear, footwear and reflective workwear.", "pages/industrial-safety-packing.html#hand-body-protection",
         "personal_protective_equipment", "Yellow safety helmet, grey work gloves, clear safety glasses, black safety shoes and a reflective hi-vis vest."),
        ("triangle-exclamation", "Workplace Safety &amp; Signage", "Cones, caution signs, barrier tapes and reflective bollards.", "pages/industrial-safety-packing.html#workplace-safety-signage-fire-safety",
         "workplace_safety_signage", "Orange traffic cone, yellow folding caution sign, black-and-yellow striped barrier tape and a yellow bollard."),
        ("boxes-stacked", "Packing Materials &amp; Accessories", "Packing tapes, stretch film, bubble wrap, cartons and strapping supplies.", "pages/industrial-safety-packing.html#cartons-strapping-packing-accessories",
         "packing_materials_accessories", "Cardboard carton, roll of stretch film, bubble wrap, brown packing tape, green packing strap and metal buckles."),
    ]

    def safety_packing_picture(stem, alt):
        return (
            f'<picture>\n'
            f'                <source srcset="{SP_DIR}/avif/{stem}.avif" type="image/avif">\n'
            f'                <source srcset="{SP_DIR}/webp/{stem}.webp" type="image/webp">\n'
            f'                <img src="{SP_DIR}/jpg/{stem}.jpg" width="1536" height="1024" alt="{alt}" loading="lazy" decoding="async" class="category-card__img">\n'
            f'              </picture>'
        )

    safety_packing_cards_html = "\n".join(
        f"""          <article class="card card--hover category-card" data-animate="fade-up">
            <span class="card__icon">{ICONS[icon]}</span>
            <div class="category-card__media">
              {safety_packing_picture(stem, alt)}
            </div>
            <h3 class="category-card__title">{name}</h3>
            <p class="category-card__desc">{desc}</p>
            <a class="btn btn--outline btn--sm" href="{href}">
              Explore Group
              {ICONS['arrow-right']}
            </a>
          </article>"""
        for icon, name, desc, href, stem, alt in safety_packing_groups
    )

    safety_packing_html = f"""    <section class="section section--light" aria-labelledby="safety-packing-heading">
      <div class="container">
        <div class="section-heading section-heading--center">
          <span class="eyebrow">Industrial Safety &amp; Packing Materials</span>
          <h2 class="section-heading__title" id="safety-packing-heading">Explore Safety &amp; <span class="text-accent">Packing Supplies</span></h2>
        </div>
        <div class="grid grid--3 category-grid safety-packing-grid">
{safety_packing_cards_html}
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # 6. WHY CHOOSE US
    # -------------------------------------------------------------
    why_choose = [
        ("box", "Commercial &amp; Industrial Supplies", "Products for commercial and industrial requirements across five categories."),
        ("diagram-project", "Wide Range", "Electricals, Electronics Components, Hardware, Industrial &amp; Commercial Equipments and Industrial Safety &amp; Packing Materials."),
        ("tag", "Request a Quotation", "Send us your requirement to request a quotation."),
        ("truck", "Delivery Enquiries", "Contact our team with your delivery requirements."),
        ("headset", "Product Enquiry Support", "Our team will respond to your product enquiries."),
    ]
    why_choose_html = "\n".join(
        f"""          <div class="feature-item feature-item--row" data-animate="fade-up">
            <span class="feature-item__icon">{ICONS[icon]}</span>
            <div>
              <h3 class="feature-item__title">{title}</h3>
              <p class="feature-item__desc">{desc}</p>
            </div>
          </div>"""
        for icon, title, desc in why_choose
    )

    why_choose_section = f"""    <section class="section section--dark text-on-dark" aria-labelledby="why-choose-heading">
      <div class="container">
        <div class="section-heading section-heading--center">
          <span class="eyebrow">Why Choose Us</span>
          <h2 class="section-heading__title" id="why-choose-heading">Commitment to Quality &amp; Service</h2>
        </div>
        <div class="grid grid--5 why-choose-grid">
{why_choose_html}
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # 7. INDUSTRIES WE SERVE
    # -------------------------------------------------------------
    industries = [
        ("factory", "Manufacturing"),
        ("hard-hat", "Construction"),
        ("lightbulb", "Power &amp; Energy"),
        ("droplet", "Oil &amp; Gas"),
        ("truck", "Transportation"),
        ("city", "Infrastructure"),
        ("gears", "Automation"),
        ("diagram-project", "OEMs"),
    ]
    industries_html = "\n".join(
        f"""          <div class="feature-item feature-item--compact" data-animate="fade-up">
            <span class="feature-item__icon">{ICONS[icon]}</span>
            <h3 class="feature-item__title">{label}</h3>
          </div>"""
        for icon, label in industries
    )

    industries_section = f"""    <section class="section section--light" aria-labelledby="industries-heading">
      <div class="container">
        <div class="section-heading section-heading--center">
          <span class="eyebrow">Industries We Serve</span>
          <h2 class="section-heading__title" id="industries-heading">Supporting Commercial &amp; Industrial Sectors</h2>
        </div>
        <div class="industries-grid">
{industries_html}
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # 8. BOTTOM CTA BANNER
    # -------------------------------------------------------------
    cta_section = f"""    <section class="cta-band cta-band--full cta-band--home text-on-dark" aria-labelledby="cta-heading">
      <div class="container cta-band__inner">
        <div class="cta-band__text">
          <h2 class="cta-band__title" id="cta-heading">Looking for the Right Products for Your Project?</h2>
          <p>Send us your requirement and our team will get back to you.</p>
        </div>
        <button type="button" class="btn btn--white cta-band__action" data-modal-open="quote">
          Request a Quote
          {ICONS['circle-right']}
        </button>
        <div class="cta-band__media">
          {cta_band_picture(0)}
        </div>
      </div>
    </section>"""

    return "\n\n".join([
        hero_html,
        categories_html,
        featured_html,
        safety_packing_html,
        why_choose_section,
        industries_section,
        build_faq_section("home", 0),
        cta_section,
    ])


# ---------------------------------------------------------------------
# CATEGORY PAGE DATA
# All content below is sourced verbatim from the concept PDF's four
# category-page screenshots (Electricals/"Wires & Cables", Electronics
# Components, Hardware, Industrial & Commercial Equipments). Two
# deliberate, documented adjustments were made — see
# documents/PHASE-4-CATEGORY-PAGES-REPORT.md:
#   1. The Electricals page's H1 is "Electricals" (category-level),
#      not "Wires & Cables" as literally shown in the PDF screenshot,
#      to match this phase's explicit "Category title" requirement and
#      the other 3 category pages' own precedent (they all use the
#      category name as H1, not a sub-category name).
#   2. Only one sub-category's real product data was available per
#      category (the one the PDF screenshot happens to show); the
#      other sub-category tabs are a visual preview of the full
#      taxonomy, not yet wired to fabricated product data.
# ---------------------------------------------------------------------

CATEGORIES = {
    "electricals": {
        "key": "electricals",
        "nav_key": "electricals",
        "icon": "bolt",
        "h1": "Electricals",
        "desc": "Wires &amp; cables, circuit protection, switches, distribution boards, lighting and more for industrial and commercial projects. Contact HM UNIQUE in George Town, Chennai with your requirement.",
        "trust_badges": [
            ("shield-check", "Commercial &amp; Industrial Supplies"),
            ("award", "Product Enquiry Support"),
            ("grid", "Wide Range"),
            ("headset", "Request a Quotation"),
        ],
        "subcategories": [
            ("cable", "Wires &amp; Cables"),
            ("bolt", "MCB, RCCB &amp; Distribution"),
            ("gear", "Switches &amp; Sockets"),
            ("bolt", "Lighting Solutions"),
            ("shield-check", "Control &amp; Protection"),
            ("wrench", "Conduits &amp; Accessories"),
            ("box", "Industrial Plugs &amp; Sockets"),
            ("cable", "Cable Management"),
            ("grid", "Electrical Panels"),
            ("gear", "Automation Components"),
            ("shield-check", "Earthing &amp; Safety"),
            ("box", "Electrical Accessories"),
        ],
        "popular_heading": "Popular Wires &amp; Cables",
        "popular_sub": "Explore popular wires and cables.",
        "products": [
            ("FRLS Copper Wire H07Z1-K", [
                ("Voltage Rating", "1100V"), ("Conductor", "Copper"), ("Insulation", "FRLS"),
                ("Available Sizes", "1 sq.mm &ndash; 240 sq.mm"), ("Application", "Industrial &amp; Building Wiring"),
            ]),
            ("XLPE Power Cable 1.1KV", [
                ("Voltage Rating", "1.1KV"), ("Insulation", "XLPE"), ("Conductor", "Copper"),
                ("Core", "1 Core to 4 Core"), ("Application", "Power Distribution"),
            ]),
            ("Flexible House Wire (FR)", [
                ("Voltage Rating", "1100V"), ("Insulation", "FR PVC"), ("Conductor", "Copper"),
                ("Available Sizes", "1 sq.mm &ndash; 16 sq.mm"), ("Application", "Residential Wiring"),
            ]),
            ("Control Cable (Multi Core)", [
                ("Voltage Rating", "1100V"), ("Insulation", "PVC"), ("Conductor", "Copper"),
                ("Core", "2 Core to 61 Core"), ("Application", "Control &amp; Signal Transmission"),
            ]),
            ("Submersible Pump Cable", [
                ("Voltage Rating", "1100V"), ("Insulation", "PVC"), ("Conductor", "Copper"),
                ("Core", "3 Core / 4 Core"), ("Application", "Submersible Pumps"),
            ]),
            ("Armoured Cable (SWA)", [
                ("Voltage Rating", "1.1KV / 3.3KV"), ("Insulation", "PVC / XLPE"), ("Conductor", "Copper"),
                ("Armouring", "Steel Wire Armour"), ("Application", "Outdoor &amp; Underground"),
            ]),
        ],
        "catalogue_name": "Electrical Product Catalogue",
        "href": "electricals.html",
    },
    "electronics": {
        "key": "electronics",
        "nav_key": "electronics",
        "icon": "chip",
        "h1": "Electronics Components",
        "desc": "Electronic components for design, prototyping and production, from passive parts and semiconductors to sensors and power supplies. Send HM UNIQUE in Chennai your requirement.",
        "trust_badges": [
            ("shield-check", "Product Enquiry Support"),
            ("grid", "Wide Range"),
            ("award", "Contact Us for Availability"),
            ("headset", "Commercial &amp; Industrial Supplies"),
        ],
        "subcategories": [
            ("chip", "Passive Components"),
            ("gear", "Active Components"),
            ("chip", "Semiconductors"),
            ("box", "Connectors"),
            ("gear", "Switches"),
            ("bolt", "Relays"),
            ("shield-check", "Sensors"),
            ("grid", "Display Modules"),
            ("shield-check", "Circuit Protection"),
            ("chip", "Development Boards"),
            ("box", "Other Components"),
        ],
        "popular_heading": "Popular Electronic Components",
        "popular_sub": "Explore popular electronic components for your projects and applications.",
        "products": [
            ("Metal Film Resistors", [
                ("Power Rating", "1/4W to 2W"), ("Tolerance", "&plusmn;1% / &plusmn;5%"),
                ("Range", "Wide Resistance Range"), ("Reliability", "High Stability &amp; Reliability"),
                ("Application", "General Purpose"),
            ]),
            ("Aluminium Electrolytic Capacitors", [
                ("Voltage Range", "10V to 450V"), ("Capacitance Range", "1&mu;F to 4700&mu;F"),
                ("Life", "Long Life &amp; High Reliability"), ("Ripple Current", "High Ripple Current"),
                ("Application", "Power Supply, Filtering"),
            ]),
            ("Transistors (NPN/PNP)", [
                ("Type", "NPN / PNP"), ("Voltage", "Up to 100V"), ("Current", "Up to 16A"),
                ("Switching Speed", "High Switching Speed"), ("Application", "Amplification &amp; Switching"),
            ]),
            ("LEDs", [
                ("Colors", "Red, Green, Blue, Yellow, White"), ("Lens Type", "Clear / Diffused"),
                ("Voltage", "1.8V to 3.2V"), ("Brightness", "High Brightness &amp; Low Power"),
                ("Application", "Indicators, Displays"),
            ]),
            ("ICs (Integrated Circuits)", [
                ("Types", "Analog, Digital, Linear"), ("Packages", "DIP, SOIC, SMD"),
                ("Functions", "Wide Range of Functions"), ("Performance", "High Performance &amp; Reliability"),
                ("Application", "Various Electronic Circuits"),
            ]),
            ("Connectors", [
                ("Types", "Terminal Blocks, Pin Headers"), ("Pitch", "2.54mm, 3.5mm, 5.08mm"),
                ("Current Rating", "Up to 16A"), ("Connection", "Secure &amp; Easy Connection"),
                ("Application", "PCB &amp; Wiring"),
            ]),
        ],
        "catalogue_name": "Electronics Components Catalogue",
        "href": "electronics.html",
    },
    "hardwares": {
        "key": "hardwares",
        "nav_key": "hardwares",
        "icon": "wrench",
        "h1": "Hardware",
        "desc": "Fasteners, hand and power tools, plumbing fittings and general hardware for construction, maintenance and industrial work. Enquire with HM UNIQUE in Chennai.",
        "trust_badges": [
            ("award", "Product Enquiry Support"),
            ("grid", "Wide Range"),
            ("shield-check", "Commercial &amp; Industrial Supplies"),
            ("headset", "Contact Us for Availability"),
        ],
        "subcategories": [
            ("screw", "Fasteners"),
            ("wrench", "Anchors &amp; Fixings"),
            ("wrench", "Hand Tools"),
            ("gear", "Power Tools"),
            ("box", "Door &amp; Window Fittings"),
            ("pump", "Plumbing Fittings"),
            ("cable", "Pipes &amp; Fittings"),
            ("shield-check", "Safety Products"),
            ("droplet", "Adhesives &amp; Sealants"),
            ("gear", "Abrasives &amp; Cutting"),
            ("box", "Hardware Accessories"),
        ],
        "popular_heading": "Popular Hardware Products",
        "popular_sub": "Explore popular hardware products.",
        "products": [
            ("Hex Bolt &amp; Nut", [
                ("Material", "Mild Steel"), ("Finish", "Zinc Plated"), ("Type", "Hex Head"),
                ("Size Range", "M6 &ndash; M20"), ("Application", "General Purpose"),
            ]),
            ("Rawl Plug with Screw", [
                ("Material", "Nylon Plug, MS Screw"), ("Finish", "Zinc Plated"), ("Type", "Expansion Anchor"),
                ("Size Range", "6mm &ndash; 12mm"), ("Application", "Concrete &amp; Masonry"),
            ]),
            ("Stainless Steel Bolt &amp; Nut", [
                ("Material", "SS 304"), ("Finish", "Natural"), ("Type", "Hex Head"),
                ("Size Range", "M6 &ndash; M20"), ("Application", "Corrosion Resistant"),
            ]),
            ("Self Drilling Screw", [
                ("Material", "Carbon Steel"), ("Finish", "Zinc Plated"), ("Type", "Phillips Head"),
                ("Size Range", "3.5mm &ndash; 6.3mm"), ("Application", "Metal to Metal Fixing"),
            ]),
            ("Hose Clamp", [
                ("Material", "Stainless Steel"), ("Finish", "Polished"), ("Type", "Worm Drive Clamp"),
                ("Size Range", "12mm &ndash; 100mm"), ("Application", "Pipe &amp; Hose Fixing"),
            ]),
            ("Blind Rivet", [
                ("Material", "Aluminium / Steel"), ("Finish", "Natural / Zinc Plated"), ("Type", "Closed End"),
                ("Size Range", "3.2mm &ndash; 6.4mm"), ("Application", "Metal Joining"),
            ]),
        ],
        "catalogue_name": "Hardware Product Catalogue",
        "href": "hardwares.html",
    },
    "industrial": {
        "key": "industrial",
        "nav_key": "industrial",
        "icon": "factory",
        "h1": "Industrial &amp; Commercial Equipments",
        "desc": "Pumps and motors, bearings, welding, material handling and power backup equipment for industrial, commercial and facility applications. Enquire with HM UNIQUE in Chennai.",
        "trust_badges": [
            ("award", "Commercial &amp; Industrial Supplies"),
            ("shield-check", "Product Enquiry Support"),
            ("grid", "Wide Range"),
            ("headset", "Contact Us for Availability"),
        ],
        "subcategories": [
            ("box", "Material Handling Equipment"),
            ("pump", "Pumps &amp; Motors"),
            ("gear", "Ventilation &amp; Air Equipment"),
            ("grid", "Electrical Enclosures"),
            ("chip", "Control &amp; Instrumentation"),
            ("shield-check", "Safety &amp; Security Equipment"),
            ("bolt", "Lighting Solutions"),
            ("bolt", "Power Backup &amp; Stabilizers"),
            ("droplet", "Cleaning Equipment"),
            ("box", "Other Industrial Supplies"),
        ],
        "popular_heading": "Popular Industrial &amp; Commercial Equipments",
        "popular_sub": "Explore popular equipment for industrial and commercial use.",
        "products": [
            ("Hand Pallet Truck", [
                ("Load Capacity", "2.5 Ton"), ("Min. Fork Height", "85mm"), ("Max Fork Height", "200mm"),
                ("Steering Type", "Manual"), ("Application", "Material Handling"),
            ]),
            ("Centrifugal Water Pump", [
                ("Power", "0.5 HP &ndash; 5 HP"), ("Flow Rate", "Up to 1000 LPM"), ("Head Range", "Up to 50 Meter"),
                ("Material", "CI / SS"), ("Application", "Water Transfer"),
            ]),
            ("Exhaust Fan", [
                ("Size", "300mm to 600mm"), ("Air Delivery", "High Flow"), ("Blade Material", "Aluminium / MS / PP"),
                ("Application", "Ventilation"),
            ]),
            ("LED High Bay Light", [
                ("Power", "100W / 150W / 200W"), ("Lumen Output", "High Efficiency"), ("Voltage", "100&ndash;277V"),
                ("IP Rating", "IP65"), ("Application", "Industrial Lighting"),
            ]),
            ("Control Panel", [
                ("Type", "Power / MCC / PCC"), ("Voltage", "415V / 440V"), ("Phase", "3 Phase / 4 Wire"),
                ("Protection", "Short Circuit, Overload"), ("Application", "Power Distribution"),
            ]),
            ("Servo Voltage Stabilizer", [
                ("Capacity", "5 KVA &ndash; 100 KVA"), ("Input Voltage", "140V &ndash; 280V"),
                ("Output Voltage", "230V &plusmn;1%"), ("Display", "Digital"), ("Application", "Voltage Regulation"),
            ]),
        ],
        "catalogue_name": "Industrial &amp; Commercial Equipments Catalogue",
        "href": "industrial-equipment.html",
    },
    # ---- Fifth category (Step 1: dedicated page only) --------------------
    # NO approved product information, brands, specifications, images or
    # catalogue exist yet, so this entry carries NO products (=> no Product
    # JSON-LD is generated), NO trust badges, NO stats strip and NO catalogue
    # download: the page shows honest "coming soon" states instead. The seven
    # sub-category labels are PROVISIONAL grouping labels, not verified
    # inventory (see DYNAMIC_CATALOGS["safety-packing"]).
    "safety-packing": {
        "key": "safety-packing",
        "nav_key": "safety-packing",
        "icon": "shield-check",
        "empty_state": True,
        "h1": "Industrial Safety &amp; Packing Materials",
        "desc": "Protective equipment, workplace safety supplies and packing materials for industrial and commercial use. Browse the product groups below or contact HM UNIQUE in Chennai.",
        "trust_badges": [],
        "subcategories": [],
        "popular_heading": "Personal Protective Equipment",
        "popular_sub": "Our product listing for this group is being prepared. Contact us for availability and details.",
        "products": [],
        "catalogue_name": "Industrial Safety &amp; Packing Materials Catalogue",
        "href": "industrial-safety-packing.html",
    },
}


# ---------------------------------------------------------------------
# DYNAMIC CATALOGUE PAGES (approved implementation)
# Every category page (Electricals, Electronics, Hardware, Industrial) is
# driven by its own js/pages/<script>.js: the product grid is rendered
# client-side from that file's CATALOG object, so the generated page carries
# an empty [data-catalog-grid] plus the data-catalog-* hooks the script binds
# to. The tab keys / labels below MUST match CATALOG in each script
# (checked by check_dynamic_tabs() on every build). `heading` / `desc` are
# the first tab's initial server-side text, `pdf` is the catalogue PDF
# basename and `script` the page script.
# ---------------------------------------------------------------------
# Sub-category tabs (key, Font Awesome icon, label). The keys/labels/order here MUST equal the
# CATALOG object in each js/pages/*-catalog.js (check_dynamic_tabs fails the build on drift).
# "heading"/"desc" are the server-side copy for the first group (the script re-renders them per tab).
# Safety & Packing has no "pdf": there is no approved catalogue, so that page shows
# "Catalogue coming soon" instead of any download.
DYNAMIC_CATALOGS = {
    "electricals": {
        "script": "electricals-catalog.js",
        "pdf": "electricals-catalogue.pdf",
        "heading": "Wires &amp; Cables",
        "desc": "Power, control and signal cables and wires for building and industrial wiring.",
        "tabs": [
            ("wires-cables", "fa-plug", "Wires &amp; Cables"),
            ("circuit-protection-switchgear", "fa-bolt", "Circuit Protection &amp; Switchgear"),
            ("contactors-relays-motor-starters", "fa-gears", "Contactors, Relays &amp; Motor Starters"),
            ("switches-sockets-industrial-plugs", "fa-toggle-on", "Switches, Sockets &amp; Industrial Plugs"),
            ("distribution-boards-panel-accessories", "fa-table-cells", "Distribution Boards &amp; Panel Accessories"),
            ("industrial-commercial-lighting", "fa-lightbulb", "Industrial &amp; Commercial Lighting"),
            ("conduits-cable-trays-wiring-accessories", "fa-grip-lines", "Conduits, Cable Trays &amp; Wiring Accessories"),
        ],
    },
    "electronics": {
        "script": "electronics-catalog.js",
        "pdf": "electronics-catalogue.pdf",
        "heading": "Resistors, Capacitors &amp; Inductors",
        "desc": "Passive components for circuit design, repair and prototyping.",
        "tabs": [
            ("resistors-capacitors-inductors", "fa-microchip", "Resistors, Capacitors &amp; Inductors"),
            ("diodes-transistors-integrated-circuits", "fa-memory", "Diodes, Transistors &amp; Integrated Circuits"),
            ("relays-switches-electromechanical-components", "fa-toggle-on", "Relays, Switches &amp; Electromechanical Components"),
            ("connectors-terminal-blocks-cable-assemblies", "fa-plug", "Connectors, Terminal Blocks &amp; Cable Assemblies"),
            ("sensors-control-modules", "fa-sliders", "Sensors &amp; Control Modules"),
            ("power-supplies-dc-converters", "fa-battery-full", "Power Supplies &amp; DC Converters"),
            ("circuit-protection-pcb-accessories", "fa-shield-halved", "Circuit Protection &amp; PCB Accessories"),
        ],
    },
    "hardwares": {
        "script": "hardwares-catalog.js",
        "pdf": "hardwares-catalogue.pdf",
        "heading": "Fasteners &amp; Anchors",
        "desc": "Bolts, nuts, screws, rivets and anchors for fixing and joining.",
        "tabs": [
            ("fasteners-anchors", "fa-screwdriver", "Fasteners &amp; Anchors"),
            ("hand-tools", "fa-wrench", "Hand Tools"),
            ("power-tools-accessories", "fa-gear", "Power Tools &amp; Accessories"),
            ("cutting-tools-abrasives", "fa-scissors", "Cutting Tools &amp; Abrasives"),
            ("pipes-valves-plumbing-fittings", "fa-faucet", "Pipes, Valves &amp; Plumbing Fittings"),
            ("measuring-inspection-tools", "fa-ruler", "Measuring &amp; Inspection Tools"),
            ("hinges-locks-general-hardware", "fa-lock", "Hinges, Locks &amp; General Hardware"),
        ],
    },
    "industrial": {
        "script": "industrial-catalog.js",
        "pdf": "industrial-catalogue.pdf",
        "heading": "Material Handling &amp; Storage Equipment",
        "desc": "Trucks, trolleys and storage equipment for moving and storing materials.",
        "tabs": [
            ("material-handling-storage-equipment", "fa-dolly", "Material Handling &amp; Storage Equipment"),
            ("pumps-electric-motors", "fa-gauge-high", "Pumps &amp; Electric Motors"),
            ("pneumatic-hydraulic-components", "fa-wind", "Pneumatic &amp; Hydraulic Components"),
            ("bearings-couplings-power-transmission", "fa-gears", "Bearings, Couplings &amp; Power Transmission"),
            ("welding-equipment-consumables", "fa-fire-flame-curved", "Welding Equipment &amp; Consumables"),
            ("industrial-cleaning-equipment-supplies", "fa-broom", "Industrial Cleaning Equipment &amp; Supplies"),
            ("power-backup-ups-voltage-stabilizers", "fa-car-battery", "Power Backup, UPS &amp; Voltage Stabilizers"),
        ],
    },
    "safety-packing": {
        "script": "industrial-safety-packing-catalog.js",
        "pdf": None,
        "heading": "Hand &amp; Body Protection",
        "desc": "Gloves and body protection for workplace tasks.",
        "tabs": [
            ("hand-body-protection", "fa-hand", "Hand &amp; Body Protection"),
            ("safety-footwear-head-protection", "fa-helmet-safety", "Safety Footwear &amp; Head Protection"),
            ("eye-face-hearing-respiratory-protection", "fa-glasses", "Eye, Face, Hearing &amp; Respiratory Protection"),
            ("workplace-safety-signage-fire-safety", "fa-triangle-exclamation", "Workplace Safety, Signage &amp; Fire Safety"),
            ("packing-tapes-adhesives-sealants", "fa-tape", "Packing Tapes, Adhesives &amp; Sealants"),
            ("stretch-film-bubble-wrap-cushioning", "fa-box-open", "Stretch Film, Bubble Wrap &amp; Cushioning"),
            ("cartons-strapping-packing-accessories", "fa-boxes-stacked", "Cartons, Strapping &amp; Packing Accessories"),
        ],
    },
}
DYNAMIC_CATALOG_KEYS = set(DYNAMIC_CATALOGS)


def check_dynamic_tabs(cat_key):
    """Fail loudly if the generated tab keys/labels drift from the CATALOG
    object in the page's catalogue script."""
    import html as _html
    import re as _re
    cfg = DYNAMIC_CATALOGS[cat_key]
    js_path = os.path.join(ROOT, "js", "pages", cfg["script"])
    if not os.path.exists(js_path):
        raise SystemExit(f"{cat_key}: catalogue script missing: {js_path}")
    js = open(js_path, encoding="utf-8").read()
    start = js.index("CATALOG")
    pairs = _re.findall(r'"([a-z0-9-]+)"\s*:\s*\{\s*label\s*:\s*"([^"]+)"', js[start:])
    pairs = [(k, _html.unescape(l)) for k, l in pairs]
    gen = [(k, _html.unescape(l)) for k, _i, l in cfg["tabs"]]
    if not pairs or pairs != gen:
        raise SystemExit(f"{cat_key} tab drift!\n  generator: {gen}\n  script:    {pairs}")


PRODUCT_CARDS_PER_GROUP = 9

# ---------------------------------------------------------------------
# APPROVED PRODUCT DATA (Step 22). product_data.py is the single source for the 315
# approved product cards. This module renders the first sub-category's cards into each
# category page, regenerates the `const CATALOG` block of each js/pages/*-catalog.js,
# and feeds the Product JSON-LD, so initial HTML and JS-rendered states cannot drift.
# ---------------------------------------------------------------------
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_data import PRODUCT_DATA  # noqa: E402
from product_images import PRODUCT_IMAGES  # noqa: E402

# Step 24: merge the id-keyed image mapping into every product so the server-side cards and the
# CATALOG written into each catalogue script come from one place.
for _groups in PRODUCT_DATA.values():
    for _g in _groups:
        for _pr in _g["products"]:
            _pr["image"] = PRODUCT_IMAGES.get(_pr["id"])


def _esc(s):
    return _htmlmod.escape(s, quote=False)


def validate_product_data():
    ids = set()
    total = 0
    if list(PRODUCT_DATA) != list(DYNAMIC_CATALOGS):
        raise SystemExit(f"product_data categories {list(PRODUCT_DATA)} != {list(DYNAMIC_CATALOGS)}")
    for cat_key, groups in PRODUCT_DATA.items():
        tabs = DYNAMIC_CATALOGS[cat_key]["tabs"]
        if len(groups) != 7:
            raise SystemExit(f"{cat_key}: expected 7 groups, got {len(groups)}")
        for g, (key, icon, label) in zip(groups, tabs):
            if (g["key"], g["icon"], _htmlmod.unescape(g["label"])) != (key, icon, _htmlmod.unescape(label)):
                raise SystemExit(f"{cat_key}: product_data group {g['key']} != tab {key}")
            if len(g["products"]) != PRODUCT_CARDS_PER_GROUP:
                raise SystemExit(f"{cat_key}/{key}: expected 9 products, got {len(g['products'])}")
            for pr in g["products"]:
                if pr["id"] in ids or pr["id"] != pr["id"].lower() or " " in pr["id"]:
                    raise SystemExit(f"bad or duplicate product id {pr['id']}")
                ids.add(pr["id"])
                total += 1
                img = pr.get("image")
                if img:
                    if not (img["dir"] and img["file"] and img["alt"] and img["width"] > 0 and img["height"] > 0):
                        raise SystemExit(f"incomplete image mapping for {pr['id']}")
                    img_root = os.path.join(ROOT, "assets", "images", "products")
                    for ext, _mime in PRODUCT_IMAGE_FORMATS:
                        if os.path.isdir(img_root) and not os.path.isfile(os.path.join(img_root, img["dir"], ext, f"{img['file']}.{ext}")):
                            # Only enforced when the images folder is present (e.g. not in a bare temp copy).
                            if os.path.isdir(os.path.join(img_root, img["dir"].split("/")[0])):
                                raise SystemExit(f"missing {ext} image for {pr['id']}: {img['dir']}/{ext}/{img['file']}.{ext}")
    if total != 315:
        raise SystemExit(f"expected 315 products, got {total}")


def _js(s):
    return json.dumps(s, ensure_ascii=False)


PRODUCT_IMAGE_BASE = "../assets/images/products/"  # category pages live in /pages/
PRODUCT_IMAGE_FORMATS = (("avif", "image/avif"), ("webp", "image/webp"), ("jpg", "image/jpeg"))


def product_image_dir_url(img):
    """URL-safe folder path: '&' and other reserved characters are percent-encoded."""
    return _urlquote(img["dir"], safe="/")


def product_image_html(pr):
    """<picture> (AVIF, WebP, JPG fallback) inside the square card image box. Mirrored by
    renderProductMedia() in each js/pages/*-catalog.js. Returns None when a product has no
    mapped image (the caller then keeps the placeholder)."""
    img = pr.get("image")
    if not img:
        return None
    base = PRODUCT_IMAGE_BASE + product_image_dir_url(img)
    url = lambda ext: f"{base}/{ext}/{img['file']}.{ext}"
    return f"""<div class="aspect-box aspect-box--square">
                <picture>
                  <source srcset="{url('avif')}" type="image/avif">
                  <source srcset="{url('webp')}" type="image/webp">
                  <img src="{url('jpg')}" width="{img['width']}" height="{img['height']}" alt="{_esc(img['alt'])}" loading="lazy" decoding="async">
                </picture>
              </div>"""


def catalog_js_block(cat_key):
    """The `const CATALOG = {...};` text for one category script."""
    blocks = []
    for g in PRODUCT_DATA[cat_key]:
        b = [f'  {_js(g["key"])}: {{', f'    label: {_js(_esc(g["label"]))},']
        if cat_key == "electricals":
            b.append(f'    icon: {_js(g["icon"])},')
        b += [f'    heading: {_js(_esc(g["label"]))},', f'    description: {_js(_esc(g["intro"]))},', "    products: ["]
        for pr in g["products"]:
            b += ["      {", f'        id: {_js(pr["id"])},', f'        name: {_js(_esc(pr["name"]))},', f'        description: {_js(_esc(pr["description"]))},']
            img = pr.get("image")
            if img:
                b.append(f'        image: {{ dir: {_js(product_image_dir_url(img))}, file: {_js(img["file"])}, width: {img["width"]}, height: {img["height"]}, alt: {_js(_esc(img["alt"]))} }},')
            b.append("        specs: [")
            b += [f"          [{_js(_esc(a))}, {_js(_esc(v))}]," for a, v in pr["specs"]]
            b += ["        ],", "      },"]
        b += ["    ],", "  },"]
        blocks.append("\n".join(b))
    return "const CATALOG = {\n" + "\n\n".join(blocks) + "\n};"


def sync_catalog_scripts():
    for cat_key, cfg in DYNAMIC_CATALOGS.items():
        path = os.path.join(ROOT, "js", "pages", cfg["script"])
        js = open(path, encoding="utf-8").read()
        s = js.index("const CATALOG = {")
        e = js.index("\n};", s) + 3
        new = js[:s] + catalog_js_block(cat_key) + js[e:]
        if new != js:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new)
            print(f"Wrote {path}")


def product_card_html(page_key, group, index):
    """Server-side mirror of renderProductCard + renderCardSlot in the catalogue scripts."""
    pr = group["products"][index]
    specs = "\n".join(
        f'<li><i class="fa-solid fa-check" aria-hidden="true"></i><span><strong>{_esc(a)}:</strong> {_esc(v)}</span></li>'
        for a, v in pr["specs"]
    )
    name = _esc(pr["name"])
    media = product_image_html(pr) or f"""<div class="aspect-box aspect-box--square" role="img" aria-label="{name} product image — placeholder, pending final product photography">
                <div class="img-placeholder"><i class="fa-regular fa-image" aria-hidden="true"></i></div>
              </div>"""
    return f"""          <article class="card card--hover product-card" data-slot-id="{page_key}-{group['key']}-{index + 1:02d}" data-product-id="{pr['id']}">
            <div class="product-card__media">
              {media}
            </div>
            <h3 class="product-card__title">{name}</h3>
            <p class="product-card__desc">{_esc(pr["description"])}</p>
            <ul class="card__specs">
{specs}
            </ul>
          </article>"""



def pending_product_card_html(page_key, group_key, group_label, index):
    """One 'Product details pending' placeholder card (mirror of renderPendingCard in the
    category catalogue scripts). No product name/spec/brand/stock claim/document link; the
    Cards carry no action buttons (enquiries use the page-level Request a Quote control)."""
    plain = group_label.replace("&amp;", "&")
    return f"""          <article class="card card--hover product-card product-card--pending" data-slot-id="{page_key}-{group_key}-{index + 1:02d}">
            <div class="product-card__media">
              <div class="aspect-box aspect-box--square" role="img" aria-label="{plain} product image &mdash; placeholder, pending approved photography">
                <div class="img-placeholder"><i class="fa-regular fa-image" aria-hidden="true"></i></div>
              </div>
            </div>
            <h3 class="product-card__title">Product details pending</h3>
            <p class="product-card__desc">Contact us for product details.</p>
          </article>"""



# ---------------------------------------------------------------------
# CATEGORY PAGE IMAGES (Step 20). Upper hero = assets/images/products/hero/<stem>.<ext>
# (700x467 landscape); lower catalogue cover = assets/images/products/catalogue/<stem>.<ext>
# (1122x1402 portrait booklet). Keyed by build_category_main's cat_key. The catalogue band
# markup is static (the sub-category tabs never rewrite it), so the cover is stable across tabs.
# ---------------------------------------------------------------------
CATEGORY_IMAGES = {
    "electricals": {
        "hero": ("electricals-category", "Electrical assortment: cable coil, distribution board, socket plate, circuit breakers and a bulb"),
        "cover": ("electricals", "Electricals catalogue booklet cover"),
    },
    "electronics": {
        "hero": ("electronics-components-category", "Electronic components: circuit board, power supply, sensor, multimeter and small parts"),
        "cover": ("electronics_components", "Electronics Components catalogue booklet cover"),
    },
    "hardwares": {
        "hero": ("hardwares-category", "Hardware assortment: cordless drill, spanner, screwdriver, fasteners and brass fittings"),
        "cover": ("hardwares", "Hardware catalogue booklet cover"),
    },
    "industrial": {
        "hero": ("industrial-commercial-equipment", "Industrial equipment: electric motor, pump, hydraulic cylinder and bearings"),
        "cover": ("industrial_commercial", "Industrial & Commercial catalogue booklet cover"),
    },
    "safety-packing": {
        "hero": ("industrial-safety-packing-materials-category", "Safety and packing materials: helmet, gloves, safety glasses, carton, stretch film and tape"),
        "cover": ("safety_packing", "Safety & Packing catalogue booklet cover"),
    },
}


def category_picture(cat_key, kind):
    """<picture> (AVIF, WebP, JPG fallback) for a category page. kind: 'hero' (eager) or 'cover' (lazy)."""
    stem, alt = CATEGORY_IMAGES[cat_key][kind]
    folder = "hero" if kind == "hero" else "catalogue"
    w, h = (700, 467) if kind == "hero" else (1122, 1402)
    base = f"../assets/images/products/{folder}"
    load = 'loading="eager" fetchpriority="high"' if kind == "hero" else 'loading="lazy"'
    cls = "category-hero__img" if kind == "hero" else "catalogue-band__img"
    return (
        f'<picture>\n'
        f'            <source srcset="{base}/avif/{stem}.avif" type="image/avif">\n'
        f'            <source srcset="{base}/webp/{stem}.webp" type="image/webp">\n'
        f'            <img src="{base}/jpg/{stem}.jpg" width="{w}" height="{h}" alt="{alt}" {load} decoding="async" class="{cls}">\n'
        f'          </picture>'
    )



def build_category_main(cat_key):
    """Builds the shared category-page template, populated with one
    category's data. Every category page (Electricals, Electronics,
    Hardware, Industrial & Commercial Equipments) calls this exact
    same function — zero HTML/CSS/JS is duplicated per category, only
    the data passed in differs, per this phase's explicit requirement."""
    cat = CATEGORIES[cat_key]

    # -------------------------------------------------------------
    # CATEGORY HERO
    # -------------------------------------------------------------
    badges_html = "\n".join(
        f"""            <div class="trust-badge">
              <span class="trust-badge__icon">{ICONS[icon]}</span>
              <span>{label}</span>
            </div>"""
        for icon, label in cat["trust_badges"]
    )
    empty_state = cat.get("empty_state", False)
    badges_block = (
        f"""          <div class="category-hero__badges">
{badges_html}
          </div>
"""
        if badges_html
        else ""
    )

    hero_html = f"""    <section class="category-hero" aria-label="{cat['h1']} overview">
      <div class="container category-hero__inner">
        <div class="category-hero__content">
          <h1 class="category-hero__title">{cat['h1']}</h1>
          <p class="category-hero__desc">{cat['desc']}</p>
{badges_block}        </div>
        <div class="category-hero__media">
          {category_picture(cat_key, 'hero')}
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # SUB-CATEGORY TAB STRIP
    # -------------------------------------------------------------
    dynamic = cat_key in DYNAMIC_CATALOG_KEYS
    if dynamic:
        tabs_html = "\n".join(
            f"""          <button type="button" class="category-tabs__item{' is-active' if i == 0 else ''}" data-category="{key}"{' aria-current="true"' if i == 0 else ''}>
            <i class="fa-solid {icon}" aria-hidden="true"></i>
            <span>{label}</span>
          </button>"""
            for i, (key, icon, label) in enumerate(DYNAMIC_CATALOGS[cat_key]["tabs"])
        )
    else:
        tabs_html = "\n".join(
            f"""          <button type="button" class="category-tabs__item{' is-active' if i == 0 else ''}"{' aria-current="true"' if i == 0 else ''}>
            {ICONS[icon]}
            <span>{label}</span>
          </button>"""
            for i, (icon, label) in enumerate(cat["subcategories"])
        )
    tabs_attr = "data-catalog-tabs" if dynamic else "data-tabs"

    tabs_section = f"""    <section class="section--sm section--light" aria-label="Sub-categories" data-float-avoid=".category-tabs__item">
      <div class="container">
        <div class="category-tabs" {tabs_attr} aria-label="{cat['h1']} sub-categories">
{tabs_html}
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # POPULAR PRODUCTS
    # -------------------------------------------------------------
    def specs_list(specs):
        items = "\n".join(
            f"""              <li>{ICONS['check']}<span><strong>{label}:</strong> {value}</span></li>"""
            for label, value in specs
        )
        return f'<ul class="card__specs">\n{items}\n            </ul>'

    product_cards_html = "\n".join(
        f"""          <article class="card card--hover product-card" data-animate="fade-up">
            <div class="product-card__media">
              {img_placeholder(name + ' product image', 'aspect-box--square')}
            </div>
            <h3 class="product-card__title">{name}</h3>
            {specs_list(specs)}
          </article>"""
        for name, specs in cat["products"]
    )

    if dynamic:
        _first = PRODUCT_DATA[cat_key][0]
        popular_heading = _esc(_first["label"])
        popular_sub = _esc(_first["intro"])
    else:
        popular_heading = cat["popular_heading"]
        popular_sub = cat["popular_sub"]
    heading_attr = " data-catalog-heading" if dynamic else ""
    desc_attr = " data-catalog-description" if dynamic else ""
    grid_open = (
        '<div class="grid grid--3" data-catalog-grid></div>'
        if dynamic
        else f'<div class="grid grid--3">\n{product_cards_html}\n        </div>'
    )
    if dynamic:
        # Server-side copy of the first sub-category's nine cards (the catalogue script
        # re-renders the same markup for whichever sub-category is active). Both come from
        # product_data.py.
        _first = PRODUCT_DATA[cat_key][0]
        _page = DYNAMIC_CATALOGS[cat_key]["script"].replace("-catalog.js", "")
        grid_open = '<div class="grid grid--3" data-catalog-grid>\n' + "\n".join(
            product_card_html(_page, _first, n) for n in range(PRODUCT_CARDS_PER_GROUP)
        ) + "\n        </div>"
    products_section = f"""    <section class="section section--surface" aria-labelledby="popular-heading" data-float-avoid=".section-heading__title, .section-heading__subtitle, .product-card__title, .product-card__desc, .card__specs li">
      <div class="container">
        <div class="section-heading section-heading--center">
          <h2 class="section-heading__title" id="popular-heading"{heading_attr}>{popular_heading}</h2>
          <p class="section-heading__subtitle"{desc_attr}>{popular_sub}</p>
        </div>
        {grid_open}
      </div>
    </section>"""

    # -------------------------------------------------------------
    # INLINE CTA
    # -------------------------------------------------------------
    inline_title_attr = " data-catalog-inline-title" if dynamic else ""
    quote_trigger_attr = " data-catalog-quote-trigger" if dynamic else ""
    if empty_state:
        inline_title_text = f"Looking for {DYNAMIC_CATALOGS[cat_key]['tabs'][0][2]}?"
        inline_text = "Share your requirements and contact us to discuss them."
    else:
        inline_title_text = f"Looking for more {cat['h1']} products?"
        inline_text = "Looking for a specific product? Contact us with your requirements."
    inline_cta = f"""    <section class="section--sm section--light" aria-label="Request more products">
      <div class="container">
        <div class="inline-cta">
          <span class="inline-cta__icon">{ICONS['file']}</span>
          <div class="inline-cta__text">
            <h3 class="inline-cta__title"{inline_title_attr}>{inline_title_text}</h3>
            <p>{inline_text}</p>
          </div>
          <button type="button" class="btn btn--primary" data-modal-open="quote"{quote_trigger_attr}>
            Request a Quote
            {ICONS['arrow-right']}
          </button>
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # CATALOGUE DOWNLOAD BAND
    # -------------------------------------------------------------
    catalogue_features = [
        ("file", "Technical Specifications"),
        ("box", "Product Datasheets"),
        ("grid", "Complete Product Range"),
    ]
    catalogue_features_html = "\n".join(
        f"""              <span class="catalogue-band__feature">{ICONS[icon]}{label}</span>"""
        for icon, label in catalogue_features
    )

    band_heading_attr = " data-catalog-catalogue-heading" if dynamic else ""
    if dynamic:
        band_cta = f"""<a class="btn btn--gold" href="../assets/catalogue/{DYNAMIC_CATALOGS[cat_key]['pdf']}#{DYNAMIC_CATALOGS[cat_key]['tabs'][0][0]}" download data-catalog-catalogue-pdf>
                {ICONS['download']}
                Download Catalogue PDF
              </a>"""
    else:
        band_cta = f"""<button type="button" class="btn btn--gold">
                {ICONS['download']}
                Download Catalogue PDF
              </button>"""
    catalogue_section = f"""    <section class="section--sm" aria-labelledby="catalogue-heading">
      <div class="container">
        <div class="cta-band cta-band--catalogue text-on-dark">
          <div class="catalogue-band__inner">
            <div class="catalogue-band__media">
              {category_picture(cat_key, 'cover')}
            </div>
            <div class="catalogue-band__text">
              <h2 class="catalogue-band__title" id="catalogue-heading"{band_heading_attr}>Download Complete<br />{cat['catalogue_name']}</h2>
              <p>Browse detailed specifications, technical drawings and complete product information.</p>
              <div class="catalogue-band__features">
{catalogue_features_html}
              </div>
              {band_cta}
            </div>
          </div>
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # STATS STRIP
    # -------------------------------------------------------------
    stats = [
        ("2019", "Established"),
        ("100+", "Clients Served"),
        ("15+", "Product Categories"),
        ("Enquiries", "Product Enquiry Support"),
        ("Contact Us", "for Availability"),
    ]
    stats_html = "\n".join(
        f"""          <div class="stat-item">
            <div class="stat-item__value">{value}</div>
            <div class="stat-item__label">{label}</div>
          </div>"""
        for value, label in stats
    )

    stats_section = f"""    <section class="section--sm section--dark text-on-dark" aria-label="Statistics">
      <div class="container">
        <div class="stats-strip">
{stats_html}
        </div>
      </div>
    </section>"""

    if empty_state:
        # Honest "coming soon" band replaces the catalogue download band, and
        # the stats strip (unverified product/brand/years figures) is omitted.
        catalogue_section = f"""    <section class="section--sm" aria-labelledby="catalogue-heading">
      <div class="container">
        <div class="cta-band cta-band--catalogue text-on-dark">
          <div class="catalogue-band__inner">
            <div class="catalogue-band__media">
              {category_picture(cat_key, 'cover')}
            </div>
            <div class="catalogue-band__text">
              <h2 class="catalogue-band__title" id="catalogue-heading">Catalogue coming soon&mdash;contact us for details</h2>
              <p>No catalogue has been published for this category yet.</p>
              <a class="btn btn--gold" href="contact.html">
                Contact Us
                {ICONS['arrow-right']}
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>"""
        return "\n\n".join([hero_html, tabs_section, products_section, inline_cta, catalogue_section])

    return "\n\n".join([
        hero_html,
        tabs_section,
        products_section,
        inline_cta,
        catalogue_section,
        stats_section,
    ])


# ---------------------------------------------------------------------
# DOWNLOAD CENTRE PAGE
# Reproduces the approved live pages/download-centre.html (its inline-SVG
# icon set and "/" breadcrumb separator are part of that approved
# implementation, so they are kept as-is rather than swapped for the
# Font Awesome variants used by newer templates). All six PDFs under
# assets/catalogue/ are one-page PLACEHOLDER documents that say so on
# their cover; the full documents are pending approval.
# ---------------------------------------------------------------------
DOWNLOAD_PLACEHOLDER_SVG = (
    '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="1.5" stroke="currentColor" stroke-width="1.4" fill="none"/>'
    '<circle cx="8.5" cy="9.5" r="1.6" stroke="currentColor" stroke-width="1.4" fill="none"/>'
    '<path d="M21 16l-5.5-5.5L9 17" stroke="currentColor" stroke-width="1.4" fill="none" stroke-linejoin="round"/></svg>'
)
DOWNLOAD_BTN_SVG = (
    '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2v8m0 0 3-3m-3 3L5 7M2 12v1a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-1" '
    'stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
)
DOWNLOAD_ARROW_SVG = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h12M9 3l5 5-5 5" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>'

# (card title, description, file under assets/catalogue/) — order is the
# approved on-page order. Titles/descriptions are the approved card copy.
DOWNLOAD_ITEMS = [
    ("Electrical Catalogue", "Wires &amp; Cables, Switches, MCBs, Distribution Boards, Lighting and more.", "electricals-catalogue.pdf"),
    ("Electronics Catalogue", "Passive, active, and semiconductor components for design and production.", "electronics-catalogue.pdf"),
    ("Hardware Catalogue", "Fasteners, hand tools, power tools, and industrial hardware accessories.", "hardwares-catalogue.pdf"),
    ("Industrial Catalogue", "Material handling, pumps &amp; motors, ventilation, and facility equipment.", "industrial-catalogue.pdf"),
    ("Company Profile", "An overview of HM UNIQUE, our history, values, and capabilities.", "company-profile.pdf"),
    ("Product Datasheets", "Technical specifications and datasheets across our full product range.", "product-datasheets.pdf"),
]


def _dc_placeholder(label, ratio_class):
    return f"""<div class="aspect-box {ratio_class}" role="img" aria-label="{label} — placeholder, pending final product photography">
              <div class="img-placeholder">{DOWNLOAD_PLACEHOLDER_SVG}</div>
            </div>"""


def build_download_centre_main():
    cards = "\n".join(
        f"""          <article class="card card--hover" data-animate="fade-up">
            <div class="download-card__media">
              {_dc_placeholder(title.replace(' Catalogue', ' Catalogue') + ' cover', 'aspect-box--tall')}
            </div>
            <h3 class="download-card__title">{title}</h3>
            <p class="download-card__desc">{desc}</p>
            <a class="btn btn--gold btn--block" href="../assets/catalogue/{filename}" download>
              {DOWNLOAD_BTN_SVG}
              Download PDF
            </a>
          </article>"""
        for title, desc, filename in DOWNLOAD_ITEMS
    )
    return f"""    <section class="page-banner text-on-dark" aria-label="Download Centre">
      <div class="container page-banner__inner">
        <span class="page-banner__eyebrow">Resources</span>
        <h1 class="page-banner__title">Download Centre</h1>
        <p class="page-banner__desc">Access our complete range of product catalogues, datasheets and company information &mdash; all in one place.</p>
      </div>
    </section>

    <section class="section section--light" aria-labelledby="downloads-heading">
      <div class="container">
        <div class="section-heading section-heading--center">
          <span class="eyebrow">Resources</span>
          <h2 class="section-heading__title" id="downloads-heading">Available Downloads</h2>
        </div>
        <p class="download-notice" role="note">
          <strong class="download-notice__label">Draft documents &mdash; pending approval.</strong>
          The files below are placeholder drafts provided for review only. They are not final catalogues, datasheets or company documents.
        </p>
        <div class="grid grid--3">
{cards}
        </div>
      </div>
    </section>

    <section class="cta-band cta-band--full text-on-dark" aria-labelledby="download-cta-heading">
      <div class="container cta-band__inner">
        <div class="cta-band__text">
          <h2 class="cta-band__title" id="download-cta-heading">Can&rsquo;t Find What You&rsquo;re Looking For?</h2>
          <p>Reach out to our team and we&rsquo;ll send you the specific documents or specifications you need.</p>
        </div>
        <button type="button" class="btn btn--white cta-band__action" data-modal-open="quote">
          Request a Quote
          {ICONS['circle-right']}
        </button>
        <div class="cta-band__media">
          {cta_band_picture(1)}
        </div>
      </div>
    </section>"""


# ---------------------------------------------------------------------
# ABOUT US PAGE
# Content sourced from the concept PDF's About Us screenshot wherever
# it exists (intro paragraphs, stats, values, journey, why-choose-us).
# Two sections have no PDF source and are placeholder content, clearly
# flagged: Vision and Mission statements — the PDF never states these
# separately. See documents/PHASE-5-COMPLETION-REPORT.md.
# ---------------------------------------------------------------------

def build_about_main():
    # Banner
    # Hero: approved banner artwork (assets/images/about_us/{avif,webp,jpg}/about_us_hero_banner.*,
    # all 1671x941) behind editable HTML. The artwork is decorative (alt="" + aria-hidden):
    # the heading, paragraph and statistics carry the meaning. Eager + high priority because it
    # is the above-the-fold image. Styling is scoped to .about-hero in css/pages/about.css.
    ABOUT_HERO_DIR = "../assets/images/about_us"
    banner = f"""    <section class="about-hero text-on-dark" aria-labelledby="about-hero-heading">
      <picture class="about-hero__media" aria-hidden="true">
        <source srcset="{ABOUT_HERO_DIR}/avif/about_us_hero_banner.avif" type="image/avif">
        <source srcset="{ABOUT_HERO_DIR}/webp/about_us_hero_banner.webp" type="image/webp">
        <img src="{ABOUT_HERO_DIR}/jpg/about_us_hero_banner.jpg" width="1671" height="941" alt="" loading="eager" fetchpriority="high" decoding="async" class="about-hero__img">
      </picture>
      <div class="container about-hero__inner">
        <div class="about-hero__content">
          <span class="eyebrow about-hero__eyebrow">About HM UNIQUE</span>
          <h1 class="about-hero__title" id="about-hero-heading">Building <span class="about-hero__accent">Connections.</span> Powering Industries.</h1>
          <p class="about-hero__desc">Since 2019, HM UNIQUE has supplied {CATEGORY_LIST_HTML} to commercial and industrial customers.</p>
          <ul class="about-hero__stats" aria-label="HM UNIQUE at a glance">
            <li class="about-hero__stat about-hero__stat--solid">
              <span class="about-hero__stat-value">2019</span>
              <span class="about-hero__stat-label">Established</span>
            </li>
            <li class="about-hero__stat about-hero__stat--outline">
              <span class="about-hero__stat-value">100+</span>
              <span class="about-hero__stat-label">Clients Served</span>
            </li>
          </ul>
        </div>
      </div>
    </section>"""

    # Who We Are
    who_images = "\n".join(
        f"""          {who_we_are_picture(i, 1)}"""
        for i in range(4)
    )

    who_we_are = f"""    <section class="section section--light" aria-labelledby="who-we-are-heading">
      <div class="container who-we-are">
        <div class="who-we-are__text">
          <span class="eyebrow">Who We Are</span>
          <h2 class="section-heading__title" id="who-we-are-heading">Supplies for Industry and Business</h2>
          <p class="mt-4">We supply products for the needs of industries, contractors, professionals and businesses from our office in George Town, Chennai.</p>
          <p class="mt-3">Contact our team to discuss your requirements and check product availability.</p>
        </div>
        <div class="who-we-are__media grid grid--2">
{who_images}
        </div>
      </div>
    </section>"""

    # Statistics (4 stats, real PDF data)
    stats = [
        ("2019", "Established"),
        ("100+", "Clients Served"),
        ("15+", "Product Categories"),
        ("Enquiries", "Product Enquiry Support"),
    ]
    stats_html = "\n".join(
        f"""          <div class="stat-item">
            <div class="stat-item__value">{value}</div>
            <div class="stat-item__label">{label}</div>
          </div>"""
        for value, label in stats
    )
    stats_section = f"""    <section class="section--sm section--dark text-on-dark" aria-label="Statistics">
      <div class="container">
        <div class="grid grid--4">
{stats_html}
        </div>
      </div>
    </section>"""

    # Vision & Mission (placeholder content — flagged, no PDF source)
    vision_mission = f"""    <section class="section section--surface" aria-labelledby="vision-mission-heading">
      <div class="container">
        <h2 class="visually-hidden" id="vision-mission-heading">Our Vision and Mission</h2>
        <div class="grid grid--2">
          <article class="card">
            {vision_mission_picture('vision', 1)}
            <span class="card__icon">{ICONS['target']}</span>
            <h3 class="mb-2">Our Vision</h3>
            <p class="text-body">To be a dependable one-stop supplier of electrical, electronic, hardware and industrial products, valued for long-term customer relationships.</p>
          </article>
          <article class="card">
            {vision_mission_picture('mission', 1)}
            <span class="card__icon">{ICONS['compass']}</span>
            <h3 class="mb-2">Our Mission</h3>
            <p class="text-body">To supply products with timely delivery and expert support, helping industries and businesses build, operate and grow with confidence.</p>
          </article>
        </div>
      </div>
    </section>"""

    # Core Values (real PDF data, 5 items)
    values = [
        ("shield-check", "Quality First", "We aim to supply quality products and to respond to every enquiry with care."),
        ("headset", "Customer Focused", "Customer satisfaction is at the heart of everything we do."),
        ("handshake", "Reliability", "We aim to provide dependable service and clear communication."),
        ("award", "Integrity", "We conduct our business with honesty, transparency and ethics."),
        ("gear", "Continuous Improvement", "We constantly strive to improve and adapt to serve our customers better."),
    ]
    values_html = "\n".join(
        f"""          <div class="feature-item" data-animate="fade-up">
            <span class="feature-item__icon">{ICONS[icon]}</span>
            <h3 class="feature-item__title">{title}</h3>
            <p class="feature-item__desc">{desc}</p>
          </div>"""
        for icon, title, desc in values
    )
    values_section = f"""    <section class="section section--light" aria-labelledby="values-heading">
      <div class="container">
        <div class="section-heading section-heading--center">
          <span class="eyebrow">Our Values</span>
          <h2 class="section-heading__title" id="values-heading">What Drives Us Forward</h2>
        </div>
        <div class="grid grid--5">
{values_html}
        </div>
      </div>
    </section>"""

    # Our Journey / Company Strengths (real PDF timeline data)
    milestones = [
        ("milestone", "2019", "Company Established", "HM UNIQUE was founded with a vision to provide quality industrial products and reliable service."),
        ("target", "Today", "Moving Forward", "Continuing to supply products and enquiry support to commercial and industrial customers."),
    ]
    milestones_html = "\n".join(
        f"""          <article class="card milestone" data-animate="fade-up">
            <span class="milestone__icon">{ICONS[icon]}</span>
            <span class="milestone__year">{year}</span>
            <h3 class="milestone__title">{title}</h3>
            <p class="milestone__desc">{desc}</p>
          </article>"""
        for icon, year, title, desc in milestones
    )
    journey_section = f"""    <section class="section section--surface" aria-labelledby="journey-heading">
      <div class="container">
        <div class="section-heading section-heading--center">
          <span class="eyebrow">Our Journey</span>
          <h2 class="section-heading__title" id="journey-heading">From 2019 to Today</h2>
        </div>
        <div class="grid grid--3 milestones-grid">
{milestones_html}
        </div>
      </div>
    </section>"""

    # Why Choose HM UNIQUE (real PDF data, 6 items)
    why_choose = [
        ("grid", "Wide Product Range", "Electricals, Electronics Components, Hardware, Industrial &amp; Commercial Equipments and Industrial Safety &amp; Packing Materials."),
        ("tag", "Request a Quotation", "Send us your requirement to request a quotation."),
        ("truck", "Delivery Enquiries", "Contact our team with your delivery requirements."),
        ("headset", "Product Enquiry Support", "Our team will respond to your product enquiries."),
        ("award", "Commercial &amp; Industrial Supplies", "Products for commercial and industrial requirements across five categories."),
        ("shield-check", "After Sales Support", "We believe in long-term relationships and continuous customer support."),
    ]
    why_choose_html = "\n".join(
        f"""          <div class="feature-item" data-animate="fade-up">
            <span class="feature-item__icon">{ICONS[icon]}</span>
            <h3 class="feature-item__title">{title}</h3>
            <p class="feature-item__desc">{desc}</p>
          </div>"""
        for icon, title, desc in why_choose
    )
    why_choose_section = f"""    <section class="section section--light" aria-labelledby="about-why-choose-heading">
      <div class="container">
        <div class="section-heading section-heading--center">
          <span class="eyebrow">Why Choose HM UNIQUE?</span>
          <h2 class="section-heading__title" id="about-why-choose-heading">Reasons Businesses Choose Us</h2>
        </div>
        <div class="grid grid--3">
{why_choose_html}
        </div>
      </div>
    </section>"""

    # Industries Served — reused from Home's exact same approved data
    industries = [
        ("factory", "Manufacturing"),
        ("hard-hat", "Construction"),
        ("lightbulb", "Power &amp; Energy"),
        ("droplet", "Oil &amp; Gas"),
        ("truck", "Transportation"),
        ("city", "Infrastructure"),
        ("gears", "Automation"),
        ("diagram-project", "OEMs"),
    ]
    industries_html = "\n".join(
        f"""          <div class="feature-item feature-item--compact" data-animate="fade-up">
            <span class="feature-item__icon">{ICONS[icon]}</span>
            <h3 class="feature-item__title">{label}</h3>
          </div>"""
        for icon, label in industries
    )
    industries_section = f"""    <section class="section section--surface" aria-labelledby="about-industries-heading">
      <div class="container">
        <div class="section-heading section-heading--center">
          <span class="eyebrow">Industries We Serve</span>
          <h2 class="section-heading__title" id="about-industries-heading">Supporting Commercial &amp; Industrial Sectors</h2>
        </div>
        <div class="industries-grid">
{industries_html}
        </div>
      </div>
    </section>"""

    # CTA (real PDF data)
    cta_section = f"""    <section class="cta-band cta-band--full text-on-dark" aria-labelledby="about-cta-heading">
      <div class="container cta-band__inner">
        <div class="cta-band__text">
          <h2 class="cta-band__title" id="about-cta-heading">Let&rsquo;s Build Something Great Together</h2>
          <p>Contact HM UNIQUE to discuss your commercial and industrial supply requirements.</p>
        </div>
        <button type="button" class="btn btn--white cta-band__action" data-modal-open="quote">
          Request a Quote
          {ICONS['circle-right']}
        </button>
        <div class="cta-band__media">
          {cta_band_picture(1)}
        </div>
      </div>
    </section>"""

    return "\n\n".join([
        banner,
        who_we_are,
        stats_section,
        vision_mission,
        values_section,
        journey_section,
        why_choose_section,
        industries_section,
        cta_section,
    ])


# ---------------------------------------------------------------------
# CONTACT US PAGE
# Content sourced from the concept PDF's Contact Us screenshot.
# ---------------------------------------------------------------------

def build_contact_main():
    banner = f"""    <section class="page-banner page-banner--contact text-on-dark" aria-label="Contact Us">
      <div class="container page-banner__inner">
        <span class="eyebrow page-banner__eyebrow">Get In Touch</span>
        <h1 class="page-banner__title">Contact Us</h1>
        <p class="page-banner__desc">Send us your requirement, call or email our team, or find our office on Linghi Chetty Street, George Town, Chennai.</p>
        <div class="page-banner__quicklinks">
          <a class="page-banner__quicklink" href="tel:{PHONE_TEL}">{ICONS['phone']} Call Us: {PHONE_DISPLAY}</a>
          <a class="page-banner__quicklink" href="mailto:{EMAIL_PRIMARY}">{ICONS['mail']} Email Us (Primary): {email_html(EMAIL_PRIMARY)}</a>
          <a class="page-banner__quicklink" href="mailto:{EMAIL_SECONDARY}">{ICONS['mail']} Email Us (Secondary): {email_html(EMAIL_SECONDARY)}</a>
          <span class="page-banner__quicklink">{ICONS['clock']} Mon &ndash; Sat: 9:00 AM &ndash; 9:00 PM</span>
        </div>
      </div>
    </section>"""

    contact_form = f"""        <div>
          <h2 class="mb-2">Get In Touch</h2>
          <p class="text-body mb-5">Fill out the form and our team will get back to you shortly.</p>

          <form class="contact-form" data-form="contact" data-float-avoid=".form-field__label, .form-field__control, .form-checkbox, .form-field__error-msg, .form-submit-error, button[type=submit]" novalidate>
            <div class="form-row">
              <div class="form-field">
                <label class="form-field__label" for="contact-name">Your Name <span class="required">*</span></label>
                <input class="form-field__control" type="text" id="contact-name" name="name" data-required placeholder="Enter your full name" />
                <span class="form-field__error-msg">Please enter your name.</span>
              </div>
              <div class="form-field">
                <label class="form-field__label" for="contact-company">Company Name</label>
                <input class="form-field__control" type="text" id="contact-company" name="company" placeholder="Enter company name (optional)" />
              </div>
            </div>

            <div class="form-row">
              <div class="form-field">
                <label class="form-field__label" for="contact-email">Email Address <span class="required">*</span></label>
                <input class="form-field__control" type="email" id="contact-email" name="email" data-required data-type="email" placeholder="Enter your email" />
                <span class="form-field__error-msg">Please enter a valid email.</span>
              </div>
              <div class="form-field">
                <label class="form-field__label" for="contact-phone">Phone Number <span class="required">*</span></label>
                <input class="form-field__control" type="tel" id="contact-phone" name="phone" data-required data-type="phone" placeholder="Enter your phone number" />
                <span class="form-field__error-msg">Please enter a valid phone number.</span>
              </div>
            </div>

            <div class="form-field">
              <label class="form-field__label" for="contact-subject">Subject <span class="required">*</span></label>
              <select class="form-field__control" id="contact-subject" name="subject" data-required>
                <option value="">Select a subject</option>
                <option value="general">General Enquiry</option>
                <option value="product">Product Enquiry</option>
                <option value="support">Support</option>
                <option value="partnership">Partnership</option>
                <option value="other">Other</option>
              </select>
              <span class="form-field__error-msg">Please select a subject.</span>
            </div>

            <div class="form-field">
              <label class="form-field__label" for="contact-message">Message <span class="required">*</span></label>
              <textarea class="form-field__control" id="contact-message" name="message" data-required placeholder="Type your message here..."></textarea>
              <span class="form-field__error-msg">Please enter your message.</span>
            </div>

            <div class="form-field">
              <label class="form-checkbox">
                <input type="checkbox" id="contact-privacy" name="privacy" data-required />
                <span>I agree to the <a aria-disabled="true">privacy policy</a>.</span>
              </label>
              <span class="form-field__error-msg">Please agree to the privacy policy to continue.</span>
            </div>

            <div class="form-hp" aria-hidden="true"><label>Leave this field empty<input type="text" name="hp_url" tabindex="-1" autocomplete="off" /></label></div>

            <p class="form-submit-success" data-form-success hidden role="status">
              <i class="fa-solid fa-circle-check" aria-hidden="true"></i>Your enquiry has been received. Our team will contact you shortly.
              <span class="form-submit-success__note" data-form-success-note hidden>We couldn’t send a confirmation email, but your enquiry was received.</span>
            </p>

            <p class="form-submit-error" data-form-error hidden role="alert">
              Something went wrong sending your message. Please try again, or call us directly at <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.
            </p>

            <button type="submit" class="btn btn--primary btn--block mt-4">
              <span data-submit-label>Send Message</span>
              <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
            </button>
          </form>
        </div>"""

    contact_info = f"""        <div>
          <div class="card info-card">
            <h3 class="info-card__title">Contact Information</h3>
            <ul class="info-card__list">
              <li>{ICONS['map-pin']}<span>{ADDRESS_LINE1}<br />{ADDRESS_LINE2}<br />{ADDRESS_LINE3}</span></li>
              <li>{ICONS['phone']}<span><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></span></li>
              <li>{ICONS['mail']}<span><a href="mailto:{EMAIL_PRIMARY}">{email_html(EMAIL_PRIMARY)}</a><br /><a href="mailto:{EMAIL_SECONDARY}">{email_html(EMAIL_SECONDARY)}</a></span></li>
              <li>{ICONS['clock']}<span>Monday &ndash; Saturday: 9:00 AM &ndash; 9:00 PM<br />Sunday: Closed</span></li>
            </ul>
          </div>
        </div>"""

    get_in_touch = f"""    <section class="section section--light" aria-label="Get in touch">
      <div class="container contact-grid">
{contact_form}
{contact_info}
      </div>
    </section>"""

    map_section = f"""    <section class="section--sm section--surface" aria-label="Our location">
      <div class="container">
        <div class="card info-card">
          <div class="flex flex--between flex--wrap flex--gap-3 mb-4">
            <div>
              <h3 class="info-card__title mb-1">Find Us Here</h3>
              <p class="text-body mb-0">{ADDRESS_LINE1}, {ADDRESS_LINE2}, {ADDRESS_LINE3}.</p>
            </div>
            <a class="btn btn--outline btn--sm" href="https://www.google.com/maps/search/?api=1&amp;query={MAPS_QUERY_ENCODED}" target="_blank" rel="noopener">
              Get Directions
              {ICONS['arrow-right']}
            </a>
          </div>
          <div class="aspect-box aspect-box--wide map-embed">
            <iframe
              src="https://www.google.com/maps?q={MAPS_QUERY_ENCODED}&amp;output=embed"
              title="HM UNIQUE location map"
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
              allowfullscreen></iframe>
          </div>
        </div>
      </div>
    </section>"""

    branch_section = f"""    <section class="section section--light" aria-labelledby="branch-heading">
      <div class="container">
        <div class="section-heading section-heading--center">
          <span class="eyebrow">Our Branch</span>
          <h2 class="section-heading__title" id="branch-heading">Chennai Branch</h2>
        </div>
        <article class="card branch-card">
          <div class="branch-card__media">
            {chennai_branch_figure(1)}
          </div>
          <div class="branch-card__body">
            <h3 class="branch-card__title">HM UNIQUE &ndash; Chennai Branch</h3>
            <ul class="info-card__list">
              <li>{ICONS['map-pin']}<span>{ADDRESS_LINE1}, {ADDRESS_LINE2}, {ADDRESS_LINE3}</span></li>
              <li>{ICONS['phone']}<span><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></span></li>
              <li>{ICONS['mail']}<span><a href="mailto:{EMAIL_PRIMARY}">{email_html(EMAIL_PRIMARY)}</a><br /><a href="mailto:{EMAIL_SECONDARY}">{email_html(EMAIL_SECONDARY)}</a></span></li>
              <li>{ICONS['clock']}<span>Mon &ndash; Sat: 9:00 AM &ndash; 9:00 PM</span></li>
            </ul>
          </div>
        </article>
      </div>
    </section>"""

    cta_section = f"""    <section class="cta-band cta-band--full text-on-dark" aria-labelledby="contact-cta-heading">
      <div class="container cta-band__inner">
        <div class="cta-band__text">
          <h2 class="cta-band__title" id="contact-cta-heading">Looking for the Right Products for Your Project?</h2>
          <p>Talk to our team about your requirements.</p>
        </div>
        <button type="button" class="btn btn--white cta-band__action" data-modal-open="quote">
          Request a Quote
          {ICONS['circle-right']}
        </button>
        <div class="cta-band__media">
          {cta_band_picture(1)}
        </div>
      </div>
    </section>"""

    return "\n\n".join([
        banner,
        get_in_touch,
        map_section,
        branch_section,
        cta_section,
    ])



# ---------------------------------------------------------------------
# AEO: compact visible FAQ. Every answer uses only information already confirmed on the site
# (categories, product groups listed, contact details, enquiry fields). No prices, stock, delivery
# times, warranties or policies are stated. The FAQPage JSON-LD is generated from the same data, so
# markup and visible text cannot drift apart. (No rich-result outcome is promised.)
# ---------------------------------------------------------------------
def _plain(html_text):
    t = re.sub(r"<[^>]+>", "", html_text)
    return (t.replace("&amp;", "&").replace("&rsquo;", "\u2019").replace("&mdash;", "\u2014").replace("&ndash;", "\u2013").replace("&nbsp;", " "))


def faq_items_for(page_key, depth):
    """Returns [(question_html, answer_html)] for a page, or [] when the page has no FAQ."""
    prefix = "" if depth == 0 else "../"
    page_href = (lambda name: f"{prefix}pages/{name}") if depth == 0 else (lambda name: name)
    contact = (f"{prefix}pages/contact.html" if depth == 0 else "contact.html")
    reach = (f'<a href="mailto:{EMAIL_PRIMARY}">{EMAIL_PRIMARY}</a> or '
             f'<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>')
    if page_key == "home":
        return [
            ("What does HM UNIQUE Technology Enterprises supply?",
             f'HM UNIQUE lists five product categories: <a href="{page_href("electricals.html")}">Electricals</a>, '
             f'<a href="{page_href("electronics.html")}">Electronics Components</a>, <a href="{page_href("hardwares.html")}">Hardware</a>, '
             f'<a href="{page_href("industrial-equipment.html")}">Industrial &amp; Commercial Equipments</a> and '
             f'<a href="{page_href("industrial-safety-packing.html")}">Industrial Safety &amp; Packing Materials</a>. Each category page shows the product groups currently listed.'),
            ("How do I request a quotation?",
             f'Select <strong>Request a Quote</strong> on any page, or contact the team at {reach}. Please mention the product name or category, the quantity if you know it, and your city so the team can understand your requirement.'),
            ("What should I include in an enquiry?",
             "The product category, the product name if you know it, the quantity if you know it, your city and state, and a phone number and email address so the team can reach you."),
            ("Does this website show prices, stock or delivery times?",
             f'No. Prices, stock and delivery details are not listed on this website. <a href="{contact}">Contact our team</a> with your requirement to ask about a quotation and availability.'),
            ("Where can I find the address and opening hours?",
             f'The office address, map and opening hours are on the <a href="{contact}">Contact page</a>. HM UNIQUE Technology Enterprises is located in George Town, Chennai.'),
        ]
    return []


def build_faq_section(page_key, depth):
    items = faq_items_for(page_key, depth)
    if not items:
        return ""
    body = "\n".join(
        f"""          <div class="faq__item">
            <h3 class="faq__question">{q}</h3>
            <p class="faq__answer">{a}</p>
          </div>"""
        for q, a in items
    )
    return f"""    <section class="section section--light faq" aria-labelledby="faq-heading">
      <div class="container">
        <div class="section-heading section-heading--center">
          <span class="eyebrow">Common Questions</span>
          <h2 class="section-heading__title" id="faq-heading">Frequently Asked Questions</h2>
        </div>
        <div class="faq__list">
{body}
        </div>
      </div>
    </section>"""


def build_faq_schema(page_key, depth):
    items = faq_items_for(page_key, depth)
    if not items:
        return None
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": _plain(q), "acceptedAnswer": {"@type": "Answer", "text": _plain(a)}}
            for q, a in items
        ],
    }, indent=2, ensure_ascii=False)


ORG_ID = SITE_URL + "/#organization"
WEBSITE_ID = SITE_URL + "/#website"
MAP_URL = f"https://www.google.com/maps/search/?api=1&query={MAPS_QUERY_ENCODED}"


def build_organization_schema():
    """Organization + LocalBusiness JSON-LD, sitewide. Only facts that are confirmed and visible on
    the site are included (name, 2019 founding, address, hours, phones, primary email). No ratings,
    reviews, prices, service-area, geo coordinates or social profiles are asserted."""
    data = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": ORG_ID,
        "name": "HM UNIQUE Technology Enterprises",
        "alternateName": "HM UNIQUE",
        "url": SITE_URL,
        "logo": f"{SITE_URL}/assets/logo/web/hm-unique-logo-192.png",
        "image": f"{SITE_URL}/assets/common/og-default.jpg",
        "description": f"Supplier of {CATEGORY_LIST_PLAIN}.",
        "foundingDate": "2019",
        "telephone": PHONE_SCHEMA,
        "email": EMAIL_PRIMARY,
        "hasMap": MAP_URL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "No.271, Linghi Chetty Street, George Town",
            "addressLocality": "Chennai",
            "addressRegion": "Tamil Nadu",
            "postalCode": "600001",
            "addressCountry": "IN",
        },
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "09:00",
            "closes": "21:00",
        },
        "contactPoint": [
            {"@type": "ContactPoint", "telephone": PHONE_SCHEMA, "contactType": "customer service", "email": EMAIL_PRIMARY},
        ],
    }
    # sameAs lists only owner-confirmed profile URLs (SOCIAL_PROFILES). None are confirmed yet, so
    # nothing is emitted; it appears automatically once a real URL is added.
    same_as = [url for _n, _i, url in SOCIAL_PROFILES if url]
    if same_as:
        data["sameAs"] = same_as
    return json.dumps(data, indent=2)


def build_website_schema():
    """WebSite JSON-LD, sitewide, linked to the organisation."""
    data = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": WEBSITE_ID,
        "name": "HM UNIQUE",
        "url": SITE_URL,
        "publisher": {"@id": ORG_ID},
    }
    return json.dumps(data, indent=2)


WEBPAGE_TYPES = {"about": "AboutPage", "contact": "ContactPage"}


def build_webpage_schema(page, canonical_url):
    """A typed WebPage node (CollectionPage for category pages) tying the page to the site and organisation."""
    ptype = WEBPAGE_TYPES.get(page["key"], "CollectionPage" if page["key"] in CATEGORIES else "WebPage")
    data = {
        "@context": "https://schema.org",
        "@type": ptype,
        "@id": canonical_url + "#webpage",
        "url": canonical_url,
        "name": _plain(page["title"]),
        "description": _plain(page["description"]),
        "isPartOf": {"@id": WEBSITE_ID},
        "about": {"@id": ORG_ID},
        "inLanguage": "en-IN",
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def build_breadcrumb_schema(breadcrumb, canonical_url):
    """BreadcrumbList JSON-LD matching the page's visible breadcrumb
    trail exactly (same items, same order). Every item — including
    the current page — gets an absolute "item" URL, per Google's
    structured-data guidelines."""
    if not breadcrumb:
        return None

    items = []
    for i, (label, href) in enumerate(breadcrumb):
        clean_label = (
            label.replace("&amp;", "&")
            .replace("&rsquo;", "\u2019")
            .replace("&ndash;", "\u2013")
        )
        if href:
            # Every breadcrumb in this project is exactly [Home, Current
            # Page] — the only non-final item is always Home.
            url = SITE_URL + "/"
        else:
            # Current (final) item — this page's own canonical URL.
            url = canonical_url
        items.append({
            "@type": "ListItem",
            "position": i + 1,
            "name": clean_label,
            "item": url,
        })

    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }
    return json.dumps(data, indent=2)


def build_product_schema(cat):
    """Product JSON-LD, one entry per product card, built from the same
    real spec data rendered on the page — never fabricated fields."""
    category_name = (
        cat["h1"].replace("&amp;", "&")
    )
    products = []
    for name, specs in cat["products"]:
        clean_name = name.replace("&amp;", "&")
        spec_text = "; ".join(
            f"{label}: {value}".replace("&amp;", "&").replace("&ndash;", "\u2013").replace("&plusmn;", "\u00b1").replace("&mu;", "\u00b5")
            for label, value in specs
        )
        products.append({
            "@context": "https://schema.org",
            "@type": "Product",
            "name": clean_name,
            "description": spec_text,
            "category": category_name,
        })
    return products


def build_schema_scripts(page, depth):
    """Assembles every JSON-LD <script> block for a given page."""
    blocks = [build_organization_schema(), build_website_schema()]
    blocks.append(build_webpage_schema(page, SITE_URL + page["canonical"]))
    faq_schema = build_faq_schema(page["key"], depth)
    if faq_schema:
        blocks.append(faq_schema)

    canonical_url = SITE_URL + page["canonical"]
    breadcrumb_schema = build_breadcrumb_schema(page["breadcrumb"], canonical_url)
    if breadcrumb_schema:
        blocks.append(breadcrumb_schema)

    if page["key"] in PRODUCT_DATA:
        # Product JSON-LD mirrors the nine cards rendered in the initial HTML.
        _cat = CATEGORIES[page["key"]]["h1"].replace("&amp;", "&")
        for pr in PRODUCT_DATA[page["key"]][0]["products"]:
            blocks.append(json.dumps({
                "@context": "https://schema.org",
                "@type": "Product",
                "name": pr["name"],
                "description": pr["description"],
                "category": _cat,
            }, indent=2, ensure_ascii=False))
    elif page["key"] in CATEGORIES:
        for product_data in build_product_schema(CATEGORIES[page["key"]]):
            blocks.append(json.dumps(product_data, indent=2))

    scripts = "\n  ".join(
        f'<script type="application/ld+json">\n{b}\n  </script>' for b in blocks
    )
    return scripts


# Page-specific stylesheet basenames where they differ from the page key.
PAGE_CSS_NAMES = {
    "industrial": "industrial-equipment",
    "safety-packing": "industrial-safety-packing",
}


def build_head(page, depth):
    # CSS loading order is a client-locked requirement:
    # variables -> utilities -> animations -> header -> footer ->
    # components -> style -> responsive -> page-specific (last, only
    # when that page's stub file has real rules in it).
    css_files = [
        "css/variables.css",
        "css/utilities.css",
        "css/animations.css",
        "css/header.css",
        "css/footer.css",
        "css/components.css",
        "css/style.css",
        "css/responsive.css",
        f"css/pages/{PAGE_CSS_NAMES.get(page['key'], page['key'])}.css",
    ]
    if page.get("noindex"):
        css_files.pop()  # the 404 page has no page-specific stylesheet
    links = "\n  ".join(f'<link rel="stylesheet" href="{rel(f, depth)}" />' for f in css_files)

    canonical_url = SITE_URL + page["canonical"]
    og_image = f"{SITE_URL}/assets/common/og-default.jpg"

    favicon_dir = rel("assets/favicon", depth)
    manifest_href = rel("site.webmanifest", depth)
    browserconfig_href = rel("browserconfig.xml", depth)

    noindex = page.get("noindex", False)
    schema_scripts = "" if noindex else build_schema_scripts(page, depth)
    verification_meta = (
        f'\n  <meta name="google-site-verification" content="{SEARCH_CONSOLE_VERIFICATION}" />'
        if SEARCH_CONSOLE_VERIFICATION else ""
    )

    return f"""<meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page['title']}</title>
  <meta name="description" content="{page['description']}" />
  {('<meta name="robots" content="noindex, follow" />' if noindex else f'<link rel="canonical" href="{canonical_url}" />')}{verification_meta}

  <!-- Favicon package -->
  <link rel="icon" href="{favicon_dir}/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="{favicon_dir}/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="{favicon_dir}/favicon-16x16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="{favicon_dir}/apple-touch-icon.png" />
  <link rel="manifest" href="{manifest_href}" />
  <meta name="msapplication-config" content="{browserconfig_href}" />
  <meta name="theme-color" content="#0c2836" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="HM UNIQUE" />
  <meta property="og:title" content="{page['title']}" />
  <meta property="og:description" content="{page['description']}" />
  {'' if noindex else f'<meta property="og:url" content="{canonical_url}" />'}
  <meta property="og:image" content="{og_image}" />
  <meta property="og:image:type" content="image/jpeg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="{OG_IMAGE_ALT}" />
  <meta property="og:locale" content="en_IN" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{page['title']}" />
  <meta name="twitter:description" content="{page['description']}" />
  <meta name="twitter:image" content="{og_image}" />
  <meta name="twitter:image:alt" content="{OG_IMAGE_ALT}" />

  <!-- Google Fonts: Plus Jakarta Sans (primary headings), Manrope
       (secondary headings), Inter (body/buttons/nav/labels/specs) —
       see css/variables.css for the full typography hierarchy this
       feeds into. -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&amp;family=Manrope:wght@600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet" />

  <!-- Font Awesome (icon system) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  {links}

  <!-- Structured data (JSON-LD) -->
  {schema_scripts}"""


# ---------------------------------------------------------------------
# 404 page. Written to /404.html, which static hosts (e.g. Cloudflare Pages) serve with a real 404
# status for unknown URLs. It is NOT in PAGES, so it is never in the sitemap, and it is noindex.
# A host may serve it from any URL depth, so every relative reference is rewritten root-absolute.
# ---------------------------------------------------------------------
NOTFOUND_PAGE = {
    "key": "notfound",
    "title": "Page not found | HM UNIQUE",
    "description": "This page could not be found. Use the links to find HM UNIQUE product categories or contact the team.",
    "path": "404.html",
    "depth": 0,
    "breadcrumb": None,
    "canonical": "/404.html",
    "noindex": True,
}


NOTFOUND_LINKS = (
    ("home", "Home", "index.html"),
    ("electricals", "Electricals", "pages/electricals.html"),
    ("electronics", "Electronics Components", "pages/electronics.html"),
    ("hardwares", "Hardware", "pages/hardwares.html"),
    ("industrial", "Industrial &amp; Commercial Equipments", "pages/industrial-equipment.html"),
    ("safety-packing", "Industrial Safety &amp; Packing Materials", "pages/industrial-safety-packing.html"),
    ("about", "About Us", "pages/about.html"),
    ("contact", "Contact Us", "pages/contact.html"),
)


def build_notfound_main():
    links = "\n".join(
        f'            <li><a href="{path}">{label}</a></li>'
        for _k, label, path in NOTFOUND_LINKS
    )
    return f"""    <section class="section section--light notfound">
      <div class="container notfound__inner">
        <p class="eyebrow">Error 404</p>
        <h1 class="notfound__title">Page not found</h1>
        <p class="notfound__text">The page you asked for is not on this website, or it has moved. These links may help:</p>
        <ul class="notfound__links">
{links}
        </ul>
        <p class="notfound__text">Not sure where to look? Call <a href="tel:+919710181944">+91 97101 81944</a> or email <a href="mailto:{EMAIL_PRIMARY}">{EMAIL_PRIMARY}</a>.</p>
      </div>
    </section>"""


def write_notfound():
    import re as _re
    html = build_page(NOTFOUND_PAGE)
    # make every relative src/href root-absolute (the 404 may be served from any URL depth)
    def _abs(m):
        attr, val = m.group(1), m.group(2)
        if val.startswith(("http:", "https:", "//", "/", "#", "mailto:", "tel:", "data:", "javascript:")):
            return m.group(0)
        return f'{attr}="/{val}"'
    html = _re.sub(r'\b(href|src|content)="([^"]*)"', lambda m: _abs(m) if m.group(1) != "content" or _re.match(r'^(assets|css|js)/', m.group(2)) else m.group(0), html)

    def _srcset(m):
        parts = []
        for cand in m.group(1).split(","):
            cand = cand.strip()
            parts.append(cand if cand.startswith(("http:", "https:", "/")) else "/" + cand)
        return 'srcset="' + ", ".join(parts) + '"'
    html = _re.sub(r'srcset="([^"]*)"', _srcset, html)
    out_path = os.path.join(ROOT, "404.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {out_path}")


def build_page(page):
    depth = page["depth"]
    key = page["key"]
    breadcrumb_html = build_breadcrumb(page["breadcrumb"], depth) if page["breadcrumb"] else ""

    js_files = [
        "js/main.js",
    ]
    # `type="module"` already defers execution per the HTML spec, but the
    # `defer` attribute is added explicitly as well — belt-and-braces so
    # the requirement is satisfied literally and unambiguously, and so
    # behavior stays correct even if a file is ever changed to a plain
    # (non-module) script in a later phase.
    scripts = "\n  ".join(
        f'<script type="module" src="{rel(f, depth)}" defer></script>' for f in js_files
    )

    if key in DYNAMIC_CATALOG_KEYS:
        check_dynamic_tabs(key)
        scripts += f'\n  <script src="{rel("js/pages/" + DYNAMIC_CATALOGS[key]["script"], depth)}" defer></script>'

    if key == "home":
        main_content = build_home_main()
    elif key in CATEGORIES:
        main_content = build_category_main(key)
    elif key == "about":
        main_content = build_about_main()
    elif key == "contact":
        main_content = build_contact_main()
    elif key == "download-centre":
        main_content = build_download_centre_main()
    elif key == "notfound":
        main_content = build_notfound_main()
    else:
        main_content = f"    <!-- {PAGE_MAIN_COMMENTS[key]} -->"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  {build_head(page, depth)}
</head>
<body data-nav-key="{key}">
  <a class="skip-link" href="#main-content">Skip to main content</a>

{build_header(key, depth)}

  <main id="main-content" tabindex="-1">
{breadcrumb_html}{main_content}
  </main>

{build_footer(depth)}

{build_quote_modal()}

{build_enquiry_popup()}

{build_enquiry_confirmation()}

{build_floating_actions()}

  {scripts}
</body>
</html>
"""
    return html


def write_page(page):
    out_path = os.path.join(ROOT, page["path"])
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(build_page(page))
    print(f"Wrote {out_path}")


def build_sitemap():
    """Generates sitemap.xml from the exact same PAGES data that drives every canonical URL and
    internal link, so the sitemap can never drift from the site. <lastmod> is deliberately omitted:
    the pages are regenerated together, so a build date would not reflect real content changes
    (and would make regeneration non-reproducible). changefreq/priority are ignored by search
    engines and are omitted too."""
    urls = "\n".join(f"  <url>\n    <loc>{SITE_URL}{p['canonical']}</loc>\n  </url>" for p in PAGES)
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + urls
        + "\n</urlset>\n"
    )
    out_path = os.path.join(ROOT, "sitemap.xml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    validate_product_data()
    sync_catalog_scripts()
    for p in PAGES:
        write_page(p)
    write_notfound()
    build_sitemap()
