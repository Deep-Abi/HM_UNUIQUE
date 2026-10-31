import os
import json

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------
# SEO base — the canonical domain is not yet registered/confirmed, so a
# placeholder is used consistently across canonical URLs, Open Graph
# og:url, sitemap.xml, and robots.txt. This is the ONE place to update
# once the real domain is live — search for SITE_URL usage.
# ---------------------------------------------------------------------
SITE_URL = "https://www.hmunique.com"

# ---------------------------------------------------------------------
# Global contact details — the single source of truth for every phone/
# email/address usage across the site. Update here only; every page
# regenerates from these constants.
# ---------------------------------------------------------------------
# Approved contact numbers (user-approved 2026-10-30). Kept as strings.
# Which person/department answers each number is deliberately NOT stated
# anywhere on the site. PHONE_* = primary; PHONE2_* = secondary;
# WA_* = the WhatsApp number (currently the same as the secondary).
PHONE_DISPLAY = "+91 97101 81944"
PHONE_TEL = "+919710181944"
PHONE_SCHEMA = "+91-97101-81944"
PHONE2_DISPLAY = "+91 63796 20433"
PHONE2_TEL = "+916379620433"
PHONE2_SCHEMA = "+91-63796-20433"
WA_DISPLAY = "+91 63796 20433"
PHONE_WA = "916379620433"
EMAIL_PRIMARY = "hmunitecenterprises02@gmail.com"
EMAIL_SECONDARY = "business@hmunique.com"
ADDRESS_LINE1 = "No.271, Linghi Chetty Street"
ADDRESS_LINE2 = "George Town, Chennai &ndash; 600001"
ADDRESS_LINE3 = "Tamil Nadu, India"
ADDRESS_FULL_PLAIN = "No.271, Linghi Chetty Street, George Town, Chennai - 600001, Tamil Nadu, India"
MAPS_QUERY = "No.271, Linghi Chetty Street, George Town, Chennai, Tamil Nadu 600001"
MAPS_QUERY_ENCODED = "No.271%2C%20Linghi%20Chetty%20Street%2C%20George%20Town%2C%20Chennai%2C%20Tamil%20Nadu%20600001"

# ---------------------------------------------------------------------
# Page registry: nav key, title, output path, relative depth, breadcrumb,
# meta description, canonical URL (site-relative, from SITE_URL)
# ---------------------------------------------------------------------
PAGES = [
    {
        "key": "home",
        "title": "HM UNIQUE | Electricals, Electronics, Hardwares &amp; Industrial Equipment",
        "path": "index.html",
        "depth": 0,
        "breadcrumb": None,  # no breadcrumb on Home
        "description": "HM UNIQUE supplies quality Electricals, Electronics Components, Hardwares, Industrial &amp; Commercial Equipment and Industrial Safety &amp; Packing Materials. Trusted brands, wide product range and pan-India delivery.",
        "canonical": "/",
    },
    {
        "key": "electricals",
        "title": "Electricals | HM UNIQUE",
        "path": "pages/electricals.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Electricals", None)],
        "description": "Explore HM UNIQUE&rsquo;s Electricals range &mdash; wires &amp; cables, MCBs, switches, distribution boards, lighting and more. Request a quote or download our catalogue.",
        "canonical": "/pages/electricals.html",
    },
    {
        "key": "electronics",
        "title": "Electronics Components | HM UNIQUE",
        "path": "pages/electronics.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Electronics Components", None)],
        "description": "Browse HM UNIQUE&rsquo;s Electronics Components &mdash; resistors, capacitors, transistors, LEDs, ICs and connectors for design, prototyping and production.",
        "canonical": "/pages/electronics.html",
    },
    {
        "key": "hardwares",
        "title": "Hardwares | HM UNIQUE",
        "path": "pages/hardwares.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Hardwares", None)],
        "description": "Shop HM UNIQUE&rsquo;s Hardware range &mdash; fasteners, hand tools, power tools and hardware accessories built for strength and reliability.",
        "canonical": "/pages/hardwares.html",
    },
    {
        "key": "industrial",
        "title": "Industrial &amp; Commercial Equipment | HM UNIQUE",
        "path": "pages/industrial-equipment.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Industrial &amp; Commercial Equipment", None)],
        "description": "Discover HM UNIQUE&rsquo;s Industrial &amp; Commercial Equipment &mdash; material handling, pumps &amp; motors, ventilation and power backup solutions.",
        "canonical": "/pages/industrial-equipment.html",
    },
    {
        "key": "safety-packing",
        "title": "Industrial Safety &amp; Packing Materials | HM UNIQUE",
        "path": "pages/industrial-safety-packing.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Industrial Safety &amp; Packing Materials", None)],
        "description": "Industrial safety and packing materials from HM UNIQUE. Product details are being prepared &mdash; contact us to discuss your requirements.",
        "canonical": "/pages/industrial-safety-packing.html",
    },
    {
        "key": "about",
        "title": "About Us | HM UNIQUE",
        "path": "pages/about.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("About Us", None)],
        "description": "Learn about HM UNIQUE &mdash; 7+ years supplying Electricals, Electronics, Hardwares, Industrial Tools and Industrial Safety &amp; Packing Materials with a commitment to quality and customer satisfaction.",
        "canonical": "/pages/about.html",
    },
    {
        "key": "contact",
        "title": "Contact Us | HM UNIQUE",
        "path": "pages/contact.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Contact Us", None)],
        "description": "Get in touch with HM UNIQUE. Call, email or WhatsApp our team, or visit our Chennai office.",
        "canonical": "/pages/contact.html",
    },
    {
        "key": "download-centre",
        "title": "Download Centre | HM UNIQUE",
        "path": "pages/download-centre.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Download Centre", None)],
        "description": "Download HM UNIQUE&rsquo;s product catalogues, company profile and datasheets for Electricals, Electronics, Hardwares and Industrial Equipment.",
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
    ("hardwares", "Hardwares", "pages/hardwares.html", "wrench"),
    ("industrial", "Industrial &amp; Commercial Equipment", "pages/industrial-equipment.html", "factory"),
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
        <a class="utility-bar__phone" href="tel:{PHONE2_TEL}">
          <i class="fa-solid fa-phone" aria-hidden="true"></i>
          <span>{PHONE2_DISPLAY}</span>
        </a>
      </div>
      <div class="utility-bar__emails">
        <a class="utility-bar__email" href="mailto:{EMAIL_PRIMARY}">
          <i class="fa-solid fa-envelope" aria-hidden="true"></i>
          <span>{EMAIL_PRIMARY}</span>
        </a>
        <a class="utility-bar__email" href="mailto:{EMAIL_SECONDARY}">
          <i class="fa-solid fa-envelope" aria-hidden="true"></i>
          <span>{EMAIL_SECONDARY}</span>
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
        <span class="site-logo__tagline">Electricals &middot; Electronics &middot; Hardwares &middot; Industrial Tools</span>
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


def build_footer(depth):
    return f"""<footer class="site-footer">
  <div class="site-footer__top">
    <div class="container site-footer__grid">
      <div class="site-footer__brand">
        <a class="site-logo" href="{rel('index.html', depth)}" aria-label="HM UNIQUE home">
          <span class="site-logo__mark site-logo__mark--backed">
            {brand_icon_picture(depth, "lazy")}
          </span>
          <span class="site-logo__text">
            <span class="site-logo__name site-footer__name"><span class="site-footer__name-main">HM UNIQUE</span> <span class="site-footer__name-sub">Technology Enterprises</span></span>
            <span class="site-logo__tagline">Electricals &middot; Electronics &middot; Hardwares &middot; Industrial Tools</span>
          </span>
        </a>
        <p class="site-footer__about">HM UNIQUE is a trusted supplier of Electricals, Electronics, Hardwares, Industrial Tools and Industrial Safety &amp; Packing Materials committed to quality, reliability and customer satisfaction.</p>
        <div class="site-footer__socials">
          <a aria-label="Facebook" aria-disabled="true"><i class="fa-brands fa-facebook-f" aria-hidden="true"></i></a>
          <a aria-label="LinkedIn" aria-disabled="true"><i class="fa-brands fa-linkedin-in" aria-hidden="true"></i></a>
          <a aria-label="Instagram" aria-disabled="true"><i class="fa-brands fa-instagram" aria-hidden="true"></i></a>
          <a href="https://wa.me/{PHONE_WA}" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i></a>
        </div>
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
          <li><a href="{rel('pages/hardwares.html', depth)}">Hardwares</a></li>
          <li><a href="{rel('pages/industrial-equipment.html', depth)}">Industrial &amp; Commercial Equipment</a></li>
          <li><a href="{rel('pages/industrial-safety-packing.html', depth)}">Industrial Safety &amp; Packing Materials</a></li>
        </ul>
      </div>

      <div class="site-footer__col">
        <h3 class="site-footer__heading">Contact Us</h3>
        <ul class="site-footer__contact">
          <li><span>{ADDRESS_LINE1}, {ADDRESS_LINE2}, {ADDRESS_LINE3}</span></li>
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li><a href="tel:{PHONE2_TEL}">{PHONE2_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL_PRIMARY}">{EMAIL_PRIMARY}</a></li>
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
</footer>"""


def fill_phones(html):
    """Substitutes the phone placeholders in the two shared templates
    that are plain (non-f) strings, from the single set of constants
    at the top of this file."""
    return (html.replace("{PHONE_TEL}", PHONE_TEL)
                .replace("{PHONE_DISPLAY}", PHONE_DISPLAY)
                .replace("{PHONE_WA}", PHONE_WA))


def build_floating_actions():
    return fill_phones("""<div class="floating-actions floating-actions--left">
  <a class="floating-btn floating-btn--whatsapp" href="https://wa.me/{PHONE_WA}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
    <i class="fa-brands fa-whatsapp" aria-hidden="true"></i>
  </a>
</div>
<div class="floating-actions floating-actions--right">
  <a class="floating-btn floating-btn--call" href="tel:{PHONE_TEL}" aria-label="Call HM UNIQUE">
    <i class="fa-solid fa-phone" aria-hidden="true"></i>
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
      <div class="modal__header">
        <span class="modal__header-icon" aria-hidden="true"></span>
        <div>
          <h2 class="modal__title" id="quote-modal-title">Request a Quote</h2>
          <p class="modal__subtitle">Share your requirements and our team will get back to you with the best solution.</p>
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
              <option value="hardwares">Hardwares</option>
              <option value="industrial">Industrial &amp; Commercial Equipment</option>
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

        <p class="form-submit-error" data-form-error hidden role="alert">
          Something went wrong sending your request. Please try again, or call us directly at <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.
        </p>

        <button type="submit" class="btn btn--primary btn--block mt-4">
          Submit Request
          <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
        </button>

        <p class="modal__note">
          <i class="fa-solid fa-shield-halved" aria-hidden="true"></i>
          Your information is safe with us. We never share your data.
        </p>
      </form>
    </div>

    <aside class="modal__aside-col">
      <h3 class="mb-3">Why Choose HM UNIQUE?</h3>
      <ul class="modal__why-list">
        <li><span aria-hidden="true">&#10003;</span><span><strong>Quality Products</strong><br />We provide only high-quality products from trusted manufacturers.</span></li>
        <li><span aria-hidden="true">&#10003;</span><span><strong>Timely Delivery</strong><br />On-time delivery with safe and efficient logistics.</span></li>
        <li><span aria-hidden="true">&#10003;</span><span><strong>Expert Support</strong><br />Our experienced team is always ready to assist you.</span></li>
        <li><span aria-hidden="true">&#10003;</span><span><strong>Customer Satisfaction</strong><br />Your satisfaction is our top priority in every collaboration.</span></li>
      </ul>
      <div class="modal__help-box">
        <p><strong>Need Help?</strong><br />Call us at <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
      </div>
    </aside>
  </div>
</div>""")


def build_thank_you_modal():
    return """<div class="modal-overlay" data-modal="thank-you" aria-hidden="true">
  <div class="modal modal--thank-you" role="dialog" aria-modal="true" aria-labelledby="thank-you-modal-title">
    <button type="button" class="modal__close" data-modal-close aria-label="Close"><i class="fa-solid fa-xmark" aria-hidden="true"></i></button>

    <svg class="success-check" viewBox="0 0 84 84" aria-hidden="true">
      <circle class="success-check__circle" cx="42" cy="42" r="40" fill="none" stroke="currentColor" stroke-width="3" />
      <path class="success-check__mark" d="M24 43l12 12 24-24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
    </svg>

    <h2 id="thank-you-modal-title">Quote Request Submitted</h2>
    <p class="mt-2">Thank you for reaching out to HM UNIQUE.</p>
    <p class="mt-3">Your request has been received. Our team will review your requirement and contact you shortly.</p>

    <div class="modal__note-box">
      <span aria-hidden="true">&#9993;</span>
      <span>We appreciate your interest in HM UNIQUE. We look forward to connecting with you!</span>
    </div>

    <button type="button" class="btn btn--primary" data-modal-close>
      Close
    </button>
  </div>
</div>"""


PAGE_MAIN_COMMENTS = {
    "home": "Home page sections (Hero, Category Grid, Featured Products, Why Choose Us, Industries Served, CTA) are built in Phase 3.",
    "electricals": "Electricals category page sections (banner, trust badges, sub-category tabs, product grid, catalogue CTA, stats) are built in Phase 3.",
    "electronics": "Electronics Components category page sections are built in Phase 3.",
    "hardwares": "Hardwares category page sections are built in Phase 3.",
    "industrial": "Industrial &amp; Commercial Equipment category page sections are built in Phase 3.",
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
    "whatsapp": '<i class="fa-brands fa-whatsapp" aria-hidden="true"></i>',
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
            "eyebrow": "One Source. Complete Solution.",
            "title_html": 'Your Trusted Partner in <span class="text-accent">Electricals</span>',
            "desc": "Supplying quality electrical products and solutions for residential, commercial and industrial applications.",
            "badges": [
                ("users", "Wide Product Range"),
                ("circle-check", "Quality Assured"),
                ("landmark", "Trusted Brands"),
                ("box", "Timely Delivery"),
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
            "eyebrow": "Smart Electronics. Reliable Solutions.",
            "title_html": 'Reliable <span class="text-accent">Electronics Components</span>',
            "desc": "Quality electronic components, test instruments and tools for automation, control and industrial applications.",
            "badges": [
                ("chip", "Quality Components"),
                ("circle-check", "Reliable Performance"),
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
            "title_html": 'Quality <span class="text-accent">Hardware</span>',
            "desc": "Dependable hand tools, power tools, fasteners and hardware solutions for professional and industrial applications.",
            "badges": [
                ("shield-check", "Durable Products"),
                ("grid", "Wide Range"),
                ("wrench", "Professional Tools"),
                ("circle-check", "Reliable Quality"),
            ],
            "cta_label": "Explore Hardwares",
            "cta_href": "pages/hardwares.html",
        },
        {
            # Slide 4 keeps its original Industrial & Commercial Equipment
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
            "eyebrow": "INDUSTRIAL &amp; COMMERCIAL EQUIPMENT",
            "title_html": 'Industrial &amp; <span class="text-accent">Commercial Equipment</span>',
            "desc": "Explore our industrial and commercial equipment range and contact us to discuss your requirements.",
            "badges": [
                ("factory", "Industrial Grade"),
                ("landmark", "Trusted Products"),
                ("grid", "Wide Applications"),
                ("headset", "Reliable Support"),
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
              <h1 class="hero__title">{slide['title_html']}</h1>
              <p class="hero__desc">{slide['desc']}</p>{badges_block}

              <div class="hero__actions">
                <a class="btn btn--primary" href="{slide['cta_href']}">
                  {slide['cta_label']}
                  {ICONS['circle-right']}
                </a>
                <a class="hero__watch-link" href="pages/about.html">
                  <span class="hero__watch-link__icon">{ICONS['play']}</span>
                  About HM Unique
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
        ("wrench", "Hardwares", "Fasteners, Hand Tools, Power Tools, Safety, Plumbing &amp; more.", "pages/hardwares.html"),
        ("factory", "Industrial &amp; Commercial Equipment", "Motors, Bearings, Pneumatics, Hydraulics, Welding &amp; more.", "pages/industrial-equipment.html"),
        ("helmet-safety", "Industrial Safety &amp; Packing Materials", "Protective equipment, workplace safety and packing materials.", "pages/industrial-safety-packing.html"),
    ]
    category_cards_html = "\n".join(
        f"""          <article class="card card--hover category-card" data-animate="fade-up">
            <span class="card__icon">{ICONS[icon]}</span>
            <div class="category-card__media">
              {img_placeholder(name + ' category image')}
            </div>
            <h3 class="category-card__title">{name}</h3>
            <p class="category-card__desc">{desc}</p>
            <a class="btn btn--outline btn--sm" href="{href}">
              Explore Category
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
        </div>
        <div class="grid grid--4 category-grid">
{category_cards_html}
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # 5. FEATURED PRODUCTS
    # -------------------------------------------------------------
    products = [
        ("Polycab FRLS Copper Cable", "High quality flame retardant electric cables."),
        ("Schneider iC65N MCB", "Advanced protection &amp; performance."),
        ("Philips LED Highbay Light", "High efficiency industrial LED lighting."),
        ("Crompton Industrial Motor", "Energy efficient motor for industrial use."),
        ("Bosch Professional Drill", "Powerful, durable &amp; built for industrial use."),
    ]
    product_cards_html = "\n".join(
        f"""          <article class="card card--hover product-card" data-animate="fade-up">
            <div class="product-card__media">
              {img_placeholder(name + ' product image', 'aspect-box--square')}
            </div>
            <h3 class="product-card__title">{name}</h3>
            <p class="product-card__desc">{desc}</p>
            <button type="button" class="btn btn--outline btn--block" data-modal-open="quote">View Details</button>
          </article>"""
        for name, desc in products
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
    # which activates the matching tab). Keys in use: "personal-protective-
    # equipment", "workplace-safety-signage" and "boxes-strapping-packing-
    # accessories" (the group that carries the "Packing Accessories" label;
    # the page's other two packing groups are one tab away). Descriptions
    # are deliberately generic: no product, brand, specification or
    # certification claim, and they say plainly that the listing is still
    # being prepared. Images stay placeholders until approved photography
    # is supplied.
    # -------------------------------------------------------------
    safety_packing_groups = [
        ("helmet-safety", "Personal Protective Equipment", "Protective equipment for industrial and commercial workplaces. Our product listing is being prepared; contact us for availability.", "pages/industrial-safety-packing.html#personal-protective-equipment"),
        ("triangle-exclamation", "Workplace Safety &amp; Signage", "Safety and signage supplies for workplaces. Our product listing is being prepared; contact us for availability.", "pages/industrial-safety-packing.html#workplace-safety-signage"),
        ("boxes-stacked", "Packing Materials &amp; Accessories", "Packing materials and accessories for industrial and commercial requirements. Our product listing is being prepared; contact us for availability.", "pages/industrial-safety-packing.html#boxes-strapping-packing-accessories"),
    ]
    safety_packing_cards_html = "\n".join(
        f"""          <article class="card card--hover category-card" data-animate="fade-up">
            <span class="card__icon">{ICONS[icon]}</span>
            <div class="category-card__media">
              {img_placeholder(name + ' image')}
            </div>
            <h3 class="category-card__title">{name}</h3>
            <p class="category-card__desc">{desc}</p>
            <a class="btn btn--outline btn--sm" href="{href}">
              Explore Group
              {ICONS['arrow-right']}
            </a>
          </article>"""
        for icon, name, desc, href in safety_packing_groups
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
        ("box", "Quality Products", "We supply only high quality products from trusted manufacturers."),
        ("diagram-project", "Wide Range", "One-stop solution for Electricals, Electronics, Hardwares, Industrial tools and Industrial Safety &amp; Packing Materials."),
        ("tag", "Competitive Pricing", "Best value for your money across all products."),
        ("truck", "Timely Delivery", "Prompt delivery ensuring minimal downtime for your projects."),
        ("headset", "Expert Support", "Our team is always ready to help you find the right products."),
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
          <h2 class="section-heading__title" id="industries-heading">Powering Industries Across The Nation</h2>
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
          <p>Send us your requirement and our experts will get back to you with the best solution.</p>
        </div>
        <button type="button" class="btn btn--white cta-band__action" data-modal-open="quote">
          Request a Quote
          {ICONS['circle-right']}
        </button>
        <div class="cta-band__media">
          {img_placeholder('Request a quote illustration', 'aspect-box--wide')}
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
        cta_section,
    ])


# ---------------------------------------------------------------------
# CATEGORY PAGE DATA
# All content below is sourced verbatim from the concept PDF's four
# category-page screenshots (Electricals/"Wires & Cables", Electronics
# Components, Hardwares, Industrial & Commercial Equipment). Two
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
        "desc": "Wires &amp; Cables, Switches, MCBs, Distribution Boards, Lighting and more &mdash; high performance electrical products for safe, reliable and efficient connections across industrial and commercial projects.",
        "trust_badges": [
            ("shield-check", "Safe &amp; Reliable"),
            ("award", "Premium Quality"),
            ("grid", "Wide Range"),
            ("headset", "Expert Support"),
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
        "popular_sub": "Explore our most in-demand wires and cables built for performance and durability.",
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
        "desc": "High quality electronic components for design, prototyping and production.",
        "trust_badges": [
            ("shield-check", "Quality Assured"),
            ("grid", "Wide Range"),
            ("award", "RoHS Compliant"),
            ("headset", "Reliable Supply"),
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
        "popular_sub": "Explore our most in-demand electronic components for your projects and applications.",
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
        "h1": "Hardwares",
        "desc": "High quality hardware products for construction, maintenance and industrial applications.",
        "trust_badges": [
            ("award", "Premium Quality"),
            ("grid", "Wide Range"),
            ("shield-check", "Corrosion Resistant"),
            ("headset", "Reliable &amp; Durable"),
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
        "popular_sub": "Explore our most in-demand hardware products built for strength and reliability.",
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
        "h1": "Industrial &amp; Commercial Equipment",
        "desc": "Reliable and efficient equipment for industrial, commercial and facility management applications.",
        "trust_badges": [
            ("award", "High Performance"),
            ("shield-check", "Reliable &amp; Durable"),
            ("grid", "Wide Range"),
            ("headset", "After Sales Support"),
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
        "popular_heading": "Popular Industrial &amp; Commercial Equipment",
        "popular_sub": "Explore our most in-demand equipment for industrial and commercial use.",
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
        "catalogue_name": "Industrial &amp; Commercial Equipment Catalogue",
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
        "desc": "Safety and packing supplies for industrial and commercial use. Our product listing for this category is being prepared &mdash; contact us to discuss your requirements.",
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
# Every category page (Electricals, Electronics, Hardwares, Industrial) is
# driven by its own js/pages/<script>.js: the product grid is rendered
# client-side from that file's CATALOG object, so the generated page carries
# an empty [data-catalog-grid] plus the data-catalog-* hooks the script binds
# to. The tab keys / labels below MUST match CATALOG in each script
# (checked by check_dynamic_tabs() on every build). `heading` / `desc` are
# the first tab's initial server-side text, `pdf` is the catalogue PDF
# basename and `script` the page script.
# ---------------------------------------------------------------------
DYNAMIC_CATALOGS = {
    "electricals": {
        "script": "electricals-catalog.js",
        "pdf": "electricals-catalogue.pdf",
        "tabs": [
            ("wires-cables", "fa-plug", "Wires &amp; Cables"),
            ("switches-sockets", "fa-toggle-on", "Switches &amp; Sockets"),
            ("mcb-rccb", "fa-bolt", "MCB &amp; RCCB"),
            ("distribution-boards", "fa-table-cells", "Distribution Boards"),
            ("lighting-solutions", "fa-lightbulb", "Lighting Solutions"),
            ("conduits-accessories", "fa-wrench", "Conduits &amp; Accessories"),
            ("electrical-accessories", "fa-box", "Electrical Accessories"),
        ],
    },
    "electronics": {
        "script": "electronics-catalog.js",
        "pdf": "electronics-catalogue.pdf",
        "heading": "Popular Passive Components",
        "desc": "Resistors, capacitors and inductors for reliable circuit design and prototyping.",
        "tabs": [
            ("passive-components", "fa-microchip", "Passive Components"),
            ("active-components", "fa-gear", "Active Components"),
            ("semiconductors", "fa-microchip", "Semiconductors"),
            ("connectors", "fa-box", "Connectors"),
            ("sensors", "fa-shield-halved", "Sensors"),
            ("circuit-protection", "fa-shield-halved", "Circuit Protection"),
            ("development-boards", "fa-microchip", "Development Boards"),
        ],
    },
    "hardwares": {
        "script": "hardwares-catalog.js",
        "pdf": "hardwares-catalogue.pdf",
        "heading": "Popular Fasteners",
        "desc": "Bolts, nuts, screws and rivets built for strength and reliable, long-lasting joints.",
        "tabs": [
            ("fasteners", "fa-screwdriver", "Fasteners"),
            ("hand-tools", "fa-wrench", "Hand Tools"),
            ("power-tools", "fa-gear", "Power Tools"),
            ("plumbing-fittings", "fa-gauge-high", "Plumbing Fittings"),
            ("pipes-fittings", "fa-plug", "Pipes &amp; Fittings"),
            ("safety-products", "fa-shield-halved", "Safety Products"),
            ("hardware-accessories", "fa-box", "Hardware Accessories"),
        ],
    },
    "industrial": {
        "script": "industrial-catalog.js",
        "pdf": "industrial-catalogue.pdf",
        "heading": "Popular Material Handling Equipment",
        "desc": "Pallet trucks, trolleys and lifting equipment for safe, efficient material movement.",
        "tabs": [
            ("material-handling-equipment", "fa-box", "Material Handling Equipment"),
            ("pumps-motors", "fa-gauge-high", "Pumps &amp; Motors"),
            ("electrical-enclosures", "fa-table-cells", "Electrical Enclosures"),
            ("safety-security-equipment", "fa-shield-halved", "Safety &amp; Security Equipment"),
            ("lighting-solutions", "fa-bolt", "Lighting Solutions"),
            ("power-backup-stabilizers", "fa-bolt", "Power Backup &amp; Stabilizers"),
            ("cleaning-equipment", "fa-droplet", "Cleaning Equipment"),
        ],
    },
    # Provisional grouping labels (NOT verified inventory). No "pdf": there is
    # no approved catalogue, so the page shows "Catalogue coming soon" instead
    # of any download.
    "safety-packing": {
        "script": "industrial-safety-packing-catalog.js",
        "pdf": None,
        "heading": "Personal Protective Equipment",
        "desc": "Our product listing for this group is being prepared. Contact us for availability and details.",
        "tabs": [
            ("personal-protective-equipment", "fa-shield-halved", "Personal Protective Equipment"),
            ("safety-footwear-head-protection", "fa-helmet-safety", "Safety Footwear &amp; Head Protection"),
            ("eye-face-hearing-protection", "fa-glasses", "Eye, Face &amp; Hearing Protection"),
            ("workplace-safety-signage", "fa-triangle-exclamation", "Workplace Safety &amp; Signage"),
            ("tapes-adhesives", "fa-tape", "Tapes &amp; Adhesives"),
            ("wrapping-cushioning-materials", "fa-box-open", "Wrapping &amp; Cushioning Materials"),
            ("boxes-strapping-packing-accessories", "fa-boxes-stacked", "Boxes, Strapping &amp; Packing Accessories"),
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


def build_category_main(cat_key):
    """Builds the shared category-page template, populated with one
    category's data. Every category page (Electricals, Electronics,
    Hardwares, Industrial & Commercial Equipment) calls this exact
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
          {img_placeholder(cat['h1'] + ' hero image', 'aspect-box--tall')}
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

    tabs_section = f"""    <section class="section--sm section--light" aria-label="Sub-categories">
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
            <div class="card__actions">
              <a class="btn btn--outline btn--sm" href="../assets/catalogue/{cat['key']}-catalogue.pdf" download>
                {ICONS['download']}
                Download PDF
              </a>
              <button type="button" class="btn btn--primary btn--sm" data-modal-open="quote">Request Quote</button>
            </div>
          </article>"""
        for name, specs in cat["products"]
    )

    popular_heading = DYNAMIC_CATALOGS[cat_key].get("heading", cat["popular_heading"]) if dynamic else cat["popular_heading"]
    popular_sub = DYNAMIC_CATALOGS[cat_key].get("desc", cat["popular_sub"]) if dynamic else cat["popular_sub"]
    heading_attr = " data-catalog-heading" if dynamic else ""
    desc_attr = " data-catalog-description" if dynamic else ""
    grid_open = (
        '<div class="grid grid--3" data-catalog-grid></div>'
        if dynamic
        else f'<div class="grid grid--3">\n{product_cards_html}\n        </div>'
    )
    if empty_state:
        first_label = DYNAMIC_CATALOGS[cat_key]["tabs"][0][2]
        grid_open = f'''<div class="grid grid--3" data-catalog-grid>
          <div class="catalog-empty" data-catalog-empty>
            <div class="catalog-empty__media">
              {img_placeholder(first_label + ' image', 'aspect-box--wide')}
            </div>
            <div class="catalog-empty__body">
              <h3 class="catalog-empty__title">Products coming soon</h3>
              <p>We have not published products for {first_label} yet. Contact us to discuss your requirements.</p>
              <div class="catalog-empty__actions">
                <button type="button" class="btn btn--primary" data-modal-open="quote" data-catalog-quote-trigger data-product-name="{first_label}">Request a Quote</button>
                <a class="btn btn--outline" href="contact.html">Contact Us</a>
              </div>
            </div>
          </div>
        </div>'''
    products_section = f"""    <section class="section section--surface" aria-labelledby="popular-heading">
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
        inline_text = "We supply hundreds of additional variants from leading brands to match your exact requirements."
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
        ("shield-check", "Certifications"),
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
              {img_placeholder(cat['catalogue_name'] + ' cover', 'aspect-box--square')}
            </div>
            <div class="catalogue-band__text">
              <h2 class="catalogue-band__title" id="catalogue-heading"{band_heading_attr}>Download Complete<br />{cat['catalogue_name']}</h2>
              <p>Browse detailed specifications, technical drawings, certifications and complete product information.</p>
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
        ("10,000+", "Products"),
        ("500+", "Trusted Brands"),
        ("25+", "Years of Experience"),
        ("Pan India", "Delivery"),
        ("100%", "Customer Satisfaction"),
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
              {img_placeholder(cat['catalogue_name'] + ' cover', 'aspect-box--square')}
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

    <section class="section--sm" aria-labelledby="download-cta-heading">
      <div class="container">
        <div class="cta-band text-on-dark">
          <div class="cta-band__inner">
            <div class="cta-band__text">
              <h2 class="cta-band__title" id="download-cta-heading">Can&rsquo;t Find What You&rsquo;re Looking For?</h2>
              <p>Reach out to our team and we&rsquo;ll send you the specific documents or specifications you need.</p>
              <button type="button" class="btn btn--white mt-4" data-modal-open="quote">
                Request a Quote
                {DOWNLOAD_ARROW_SVG}
              </button>
            </div>
            <div class="cta-band__media">
              {_dc_placeholder('Download Centre illustration', 'aspect-box--square')}
            </div>
          </div>
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
    banner = f"""    <section class="page-banner text-on-dark" aria-label="About HM UNIQUE">
      <div class="container page-banner__inner">
        <span class="eyebrow page-banner__eyebrow">About HM UNIQUE</span>
        <h1 class="page-banner__title">Building Connections. Powering Industries.</h1>
        <p class="page-banner__desc">With 7+ years of experience, HM UNIQUE has emerged as a trusted supplier of Electricals, Electronics, Hardwares, Industrial Tools and Industrial Safety &amp; Packing Materials. Our commitment to quality, reliability and customer satisfaction drives everything we do.</p>
        <div class="page-banner__badge">
          <div class="page-banner__badge-item">
            <div class="page-banner__badge-value">7+</div>
            <div class="page-banner__badge-label">Years of Experience</div>
          </div>
          <div class="page-banner__badge-item">
            <div class="page-banner__badge-value">2017</div>
            <div class="page-banner__badge-label">Since</div>
          </div>
        </div>
      </div>
    </section>"""

    # Who We Are
    who_images = "\n".join(
        f"""          {img_placeholder('HM UNIQUE facility photo ' + str(i), 'aspect-box--square')}"""
        for i in range(1, 5)
    )

    who_we_are = f"""    <section class="section section--light" aria-labelledby="who-we-are-heading">
      <div class="container who-we-are">
        <div class="who-we-are__text">
          <span class="eyebrow">Who We Are</span>
          <h2 class="section-heading__title" id="who-we-are-heading">Your Trusted Partner for Quality &amp; Performance</h2>
          <p class="mt-4">We supply high-quality products that meet the evolving needs of industries, contractors, professionals and businesses.</p>
          <p class="mt-3">Through strong partnerships with reputed manufacturers and brands, we ensure timely delivery, competitive pricing and unmatched service.</p>
        </div>
        <div class="who-we-are__media grid grid--2">
{who_images}
        </div>
      </div>
    </section>"""

    # Statistics (4 stats, real PDF data)
    stats = [
        ("5000+", "Products"),
        ("1000+", "Happy Clients"),
        ("7+", "Years of Experience"),
        ("15+", "Cities Served"),
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
            <span class="card__icon">{ICONS['target']}</span>
            <h3 class="mb-2">Our Vision</h3>
            <p class="text-body">To be India&rsquo;s most trusted one-stop partner for electrical, electronic, hardware and industrial products &mdash; recognized for quality, reliability and long-term customer relationships.</p>
          </article>
          <article class="card">
            <span class="card__icon">{ICONS['compass']}</span>
            <h3 class="mb-2">Our Mission</h3>
            <p class="text-body">To supply high-quality, certified products with timely delivery and expert support, helping industries and businesses build, operate and grow with confidence.</p>
          </article>
        </div>
      </div>
    </section>"""

    # Core Values (real PDF data, 5 items)
    values = [
        ("shield-check", "Quality First", "We source and supply only premium quality products from trusted manufacturers."),
        ("headset", "Customer Focused", "Customer satisfaction is at the heart of everything we do."),
        ("handshake", "Reliability", "We are committed to delivering consistent quality and dependable service, every time."),
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
        ("milestone", "2017", "Company Established", "HM UNIQUE was founded with a vision to provide quality industrial products and reliable service."),
        ("handshake", "2018", "Building Partnerships", "We expanded our product range and built strong partnerships with trusted manufacturers."),
        ("gear", "2020", "Growing Stronger", "Strengthened our supply chain and improved infrastructure to ensure faster delivery."),
        ("grid", "2022", "Expanding Reach", "Served more industries and clients across multiple cities with excellent support."),
        ("award", "2024", "Commitment to Excellence", "Continued our focus on quality, service and customer satisfaction."),
        ("target", "Today", "Moving Forward", "Continuing to grow with innovation, trust and a customer-first approach."),
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
          <h2 class="section-heading__title" id="journey-heading">Company Strengths Built Over Time</h2>
        </div>
        <div class="grid grid--3">
{milestones_html}
        </div>
      </div>
    </section>"""

    # Why Choose HM UNIQUE (real PDF data, 6 items)
    why_choose = [
        ("grid", "Wide Product Range", "One-stop solution for Electricals, Electronics, Hardwares, Industrial Tools and Industrial Safety &amp; Packing Materials."),
        ("tag", "Competitive Pricing", "Best value for your money without compromising on quality."),
        ("truck", "Timely Delivery", "Efficient logistics and on-time delivery to keep your projects on track."),
        ("headset", "Expert Support", "Our experienced team is always ready to help you choose the right products."),
        ("award", "Trusted Brands", "We partner with leading brands to bring reliable and certified products."),
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
          <h2 class="section-heading__title" id="about-industries-heading">Powering Industries Across The Nation</h2>
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
          <p>Partner with HM UNIQUE for reliable, exceptional service and lasting business relationships.</p>
        </div>
        <button type="button" class="btn btn--white cta-band__action" data-modal-open="quote">
          Request a Quote
          {ICONS['circle-right']}
        </button>
        <div class="cta-band__media">
          {img_placeholder('HM UNIQUE team illustration', 'aspect-box--wide')}
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
    banner = f"""    <section class="page-banner text-on-dark" aria-label="Contact Us">
      <div class="container page-banner__inner">
        <span class="eyebrow page-banner__eyebrow">Get In Touch</span>
        <h1 class="page-banner__title">Contact Us</h1>
        <p class="page-banner__desc">We&rsquo;re here to help you find the right products and solutions for your business.</p>
        <div class="page-banner__quicklinks">
          <a class="page-banner__quicklink" href="tel:{PHONE_TEL}">{ICONS['phone']} Call Us: {PHONE_DISPLAY}</a>
          <a class="page-banner__quicklink" href="tel:{PHONE2_TEL}">{ICONS['phone']} Call Us: {PHONE2_DISPLAY}</a>
          <a class="page-banner__quicklink" href="mailto:{EMAIL_PRIMARY}">{ICONS['mail']} Email Us: {EMAIL_PRIMARY}</a>
          <span class="page-banner__quicklink">{ICONS['clock']} Mon &ndash; Sat: 9:00 AM &ndash; 9:00 PM</span>
          <a class="page-banner__quicklink" href="https://wa.me/{PHONE_WA}" target="_blank" rel="noopener">{ICONS['whatsapp']} WhatsApp: {WA_DISPLAY}</a>
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
                <option value="general">General Inquiry</option>
                <option value="product">Product Inquiry</option>
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

            <p class="form-submit-error" data-form-error hidden role="alert">
              Something went wrong sending your message. Please try again, or call us directly at <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.
            </p>

            <button type="submit" class="btn btn--primary btn--block mt-4">
              Send Message
              <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
            </button>
          </form>
        </div>"""

    contact_info = f"""        <div>
          <div class="card info-card">
            <h3 class="info-card__title">Contact Information</h3>
            <ul class="info-card__list">
              <li>{ICONS['map-pin']}<span>{ADDRESS_LINE1}<br />{ADDRESS_LINE2}<br />{ADDRESS_LINE3}</span></li>
              <li>{ICONS['phone']}<span><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br /><a href="tel:{PHONE2_TEL}">{PHONE2_DISPLAY}</a></span></li>
              <li>{ICONS['mail']}<span><a href="mailto:{EMAIL_PRIMARY}">{EMAIL_PRIMARY}</a><br /><a href="mailto:{EMAIL_SECONDARY}">{EMAIL_SECONDARY}</a></span></li>
              <li>{ICONS['clock']}<span>Monday &ndash; Saturday: 9:00 AM &ndash; 9:00 PM<br />Sunday: Closed</span></li>
            </ul>

            <div class="whatsapp-cta">
              <span class="whatsapp-cta__icon">{ICONS['whatsapp']}</span>
              <div class="whatsapp-cta__text">
                <strong>Chat with us on WhatsApp</strong>
                <p class="mb-0">Get a quick response to your queries.</p>
              </div>
              <a class="btn btn--sm btn--primary" href="https://wa.me/{PHONE_WA}" target="_blank" rel="noopener">Chat Now</a>
            </div>
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
            {img_placeholder('HM UNIQUE Chennai branch office', 'aspect-box--wide')}
          </div>
          <div class="branch-card__body">
            <h3 class="branch-card__title">HM UNIQUE &ndash; Chennai Branch</h3>
            <ul class="info-card__list">
              <li>{ICONS['map-pin']}<span>{ADDRESS_LINE1}, {ADDRESS_LINE2}, {ADDRESS_LINE3}</span></li>
              <li>{ICONS['phone']}<span><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br /><a href="tel:{PHONE2_TEL}">{PHONE2_DISPLAY}</a></span></li>
              <li>{ICONS['mail']}<span><a href="mailto:{EMAIL_SECONDARY}">{EMAIL_SECONDARY}</a></span></li>
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
          <p>Talk to our experts and get the best solution for your business.</p>
        </div>
        <button type="button" class="btn btn--white cta-band__action" data-modal-open="quote">
          Request a Quote
          {ICONS['circle-right']}
        </button>
        <div class="cta-band__media">
          {img_placeholder('Contact HM UNIQUE illustration', 'aspect-box--wide')}
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


def build_organization_schema():
    """Organization + LocalBusiness JSON-LD, sitewide (identical on
    every page — this is the entity graph for the business itself,
    not page-specific content)."""
    data = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "HM UNIQUE",
        "url": SITE_URL,
        "logo": f"{SITE_URL}/assets/logo/web/hm-unique-logo-192.png",
        "description": "Supplier of Electricals, Electronics Components, Hardwares, Industrial & Commercial Equipment and Industrial Safety & Packing Materials.",
        "telephone": PHONE_SCHEMA,
        "email": "hmunitecenterprises02@gmail.com",
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
            {
                "@type": "ContactPoint",
                "telephone": PHONE_SCHEMA,
                "contactType": "customer service",
                "email": "hmunitecenterprises02@gmail.com",
                "areaServed": "IN",
                "availableLanguage": ["en"],
            },
            {
                "@type": "ContactPoint",
                "telephone": PHONE2_SCHEMA,
                "contactType": "customer service",
                "areaServed": "IN",
                "availableLanguage": ["en"],
            },
        ],
    }
    return json.dumps(data, indent=2)


def build_website_schema():
    """WebSite JSON-LD, sitewide."""
    data = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "HM UNIQUE",
        "url": SITE_URL,
    }
    return json.dumps(data, indent=2)


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

    canonical_url = SITE_URL + page["canonical"]
    breadcrumb_schema = build_breadcrumb_schema(page["breadcrumb"], canonical_url)
    if breadcrumb_schema:
        blocks.append(breadcrumb_schema)

    if page["key"] in CATEGORIES:
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
    links = "\n  ".join(f'<link rel="stylesheet" href="{rel(f, depth)}" />' for f in css_files)

    canonical_url = SITE_URL + page["canonical"]
    og_image = f"{SITE_URL}/assets/common/og-default.jpg"

    favicon_dir = rel("assets/favicon", depth)
    manifest_href = rel("site.webmanifest", depth)
    browserconfig_href = rel("browserconfig.xml", depth)

    schema_scripts = build_schema_scripts(page, depth)

    return f"""<meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page['title']}</title>
  <meta name="description" content="{page['description']}" />
  <link rel="canonical" href="{canonical_url}" />

  <!-- Favicon package -->
  <link rel="icon" href="{favicon_dir}/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="{favicon_dir}/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="{favicon_dir}/favicon-16x16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="{favicon_dir}/apple-touch-icon.png" />
  <link rel="manifest" href="{manifest_href}" />
  <meta name="msapplication-config" content="{browserconfig_href}" />
  <meta name="theme-color" content="#0e2b3b" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="HM UNIQUE" />
  <meta property="og:title" content="{page['title']}" />
  <meta property="og:description" content="{page['description']}" />
  <meta property="og:url" content="{canonical_url}" />
  <meta property="og:image" content="{og_image}" />
  <meta property="og:locale" content="en_IN" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{page['title']}" />
  <meta name="twitter:description" content="{page['description']}" />
  <meta name="twitter:image" content="{og_image}" />

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

{build_thank_you_modal()}

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
    """Generates sitemap.xml from the exact same PAGES data that
    drives every canonical URL and internal link — guarantees the
    sitemap can never drift out of sync with the actual site."""
    from datetime import date

    today = date.today().isoformat()
    urls = []
    for p in PAGES:
        priority = "1.0" if p["key"] == "home" else "0.8"
        urls.append(
            f"""  <url>
    <loc>{SITE_URL}{p['canonical']}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>"""
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    out_path = os.path.join(ROOT, "sitemap.xml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    for p in PAGES:
        write_page(p)
    build_sitemap()
