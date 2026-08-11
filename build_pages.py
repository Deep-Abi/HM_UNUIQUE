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
        "description": "HM UNIQUE supplies quality Electricals, Electronics Components, Hardwares and Industrial &amp; Commercial Equipment. Trusted brands, wide product range and pan-India delivery.",
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
        "key": "about",
        "title": "About Us | HM UNIQUE",
        "path": "pages/about.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("About Us", None)],
        "description": "Learn about HM UNIQUE &mdash; 7+ years supplying Electricals, Electronics, Hardwares and Industrial Tools with a commitment to quality and customer satisfaction.",
        "canonical": "/pages/about.html",
    },
    {
        "key": "contact",
        "title": "Contact Us | HM UNIQUE",
        "path": "pages/contact.html",
        "depth": 1,
        "breadcrumb": [("Home", "../index.html"), ("Contact Us", None)],
        "description": "Get in touch with HM UNIQUE. Call, email or WhatsApp our team, or visit our Coimbatore head office and Chennai branch.",
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
    ("electricals", "Electricals", "pages/electricals.html"),
    ("electronics", "Electronics Components", "pages/electronics.html"),
    ("hardwares", "Hardwares", "pages/hardwares.html"),
    ("industrial", "Industrial &amp; Commercial Equipment", "pages/industrial-equipment.html"),
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
    dl_active = nav_current("download-centre", current_key)
    return f"""  <div class="utility-bar">
    <div class="container utility-bar__inner">
      <div class="utility-bar__contact">
        <a href="tel:+919876543210"><span>+91 98765 43210</span></a>
        <a href="mailto:info@hmunique.com"><span>info@hmunique.com</span></a>
      </div>
      <div class="utility-bar__links">
        <a href="{rel('pages/download-centre.html', depth)}"{dl_active}>Download Centre</a>
        <div class="utility-bar__socials">
          <a aria-label="Facebook" aria-disabled="true">FB</a>
          <a aria-label="LinkedIn" aria-disabled="true">IN</a>
          <a aria-label="Instagram" aria-disabled="true">IG</a>
        </div>
      </div>
    </div>
  </div>"""


def build_products_dropdown(current_key, depth):
    links = []
    for key, label, path in PRODUCT_ITEMS:
        active = nav_current(key, current_key)
        links.append(
            f"""          <li>
            <a class="products-dropdown__link" href="{rel(path, depth)}" data-nav-key-link="{key}"{active}>
              <span class="products-dropdown__icon" aria-hidden="true"></span>
              {label}
            </a>
          </li>"""
        )
    return "\n".join(links)


def build_primary_nav(current_key, depth):
    home_active = nav_current("home", current_key)
    about_active = nav_current("about", current_key)
    contact_active = nav_current("contact", current_key)
    products_open = current_key in {"electricals", "electronics", "hardwares", "industrial"}
    products_current = ' aria-current="page"' if products_open else ""

    return f"""      <ul class="primary-nav__list">
        <li class="primary-nav__item">
          <a class="primary-nav__link" href="{rel('index.html', depth)}" data-nav-key-link="home"{home_active}>Home</a>
        </li>
        <li class="primary-nav__item primary-nav__item--dropdown" data-nav-dropdown>
          <button type="button" class="primary-nav__link" data-nav-dropdown-trigger aria-haspopup="true" aria-expanded="false" aria-controls="products-dropdown-menu"{products_current}>
            Products
            <svg class="primary-nav__chevron" viewBox="0 0 10 6" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
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


def build_mobile_nav(current_key, depth):
    home_active = nav_current("home", current_key)
    about_active = nav_current("about", current_key)
    contact_active = nav_current("contact", current_key)
    dl_active = nav_current("download-centre", current_key)

    product_links = []
    for key, label, path in PRODUCT_ITEMS:
        active = nav_current(key, current_key)
        product_links.append(
            f'            <li><a class="mobile-nav__submenu-link" href="{rel(path, depth)}" data-nav-key-link="{key}"{active}>{label}</a></li>'
        )
    product_links_html = "\n".join(product_links)

    return f"""  <div class="mobile-nav-overlay" data-mobile-nav-overlay></div>
  <nav class="mobile-nav" id="mobile-navigation" data-mobile-nav aria-label="Mobile navigation">
    <div class="mobile-nav__header">
      <span class="site-logo__name">HM UNIQUE</span>
      <button type="button" class="mobile-nav__close" data-mobile-nav-close aria-label="Close menu">&times;</button>
    </div>
    <ul class="mobile-nav__list">
      <li><a class="mobile-nav__link" href="{rel('index.html', depth)}" data-nav-key-link="home"{home_active}>Home</a></li>
      <li class="mobile-nav__item" data-mobile-nav-item>
        <button type="button" class="mobile-nav__link mobile-nav__submenu-toggle" data-mobile-submenu-toggle aria-expanded="false" aria-controls="mobile-products-submenu">
          Products
          <svg class="primary-nav__chevron" viewBox="0 0 10 6" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
        </button>
        <ul class="mobile-nav__submenu" id="mobile-products-submenu">
{product_links_html}
        </ul>
      </li>
      <li><a class="mobile-nav__link" href="{rel('pages/about.html', depth)}" data-nav-key-link="about"{about_active}>About Us</a></li>
      <li><a class="mobile-nav__link" href="{rel('pages/contact.html', depth)}" data-nav-key-link="contact"{contact_active}>Contact Us</a></li>
      <li><a class="mobile-nav__link" href="{rel('pages/download-centre.html', depth)}" data-nav-key-link="download-centre"{dl_active}>Download Centre</a></li>
    </ul>
    <div class="mobile-nav__cta">
      <button type="button" class="btn btn--primary btn--block" data-modal-open="quote">Request a Quote</button>
    </div>
  </nav>"""


def build_header(current_key, depth):
    return f"""<header class="site-header" data-site-header>
{build_utility_bar(current_key, depth)}
  <div class="container site-header__inner">
    <a class="site-logo" href="{rel('index.html', depth)}" aria-label="HM UNIQUE home">
      <span class="site-logo__mark">
        <img src="{rel('assets/logo/hm-unique-logo.svg', depth)}" alt="HM UNIQUE logo" width="44" height="44" loading="eager" decoding="async" />
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
      <button type="button" class="btn btn--primary hide-on-mobile" data-modal-open="quote">
        Request a Quote
        <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
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
            parts.append('<span class="breadcrumb__sep">/</span>')
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
          <span class="site-logo__mark">
            <img src="{rel('assets/logo/hm-unique-logo-light.svg', depth)}" alt="HM UNIQUE logo" width="44" height="44" loading="lazy" decoding="async" />
          </span>
          <span class="site-logo__text">
            <span class="site-logo__name">HM UNIQUE</span>
            <span class="site-logo__tagline">Electricals &middot; Electronics &middot; Hardwares &middot; Industrial Tools</span>
          </span>
        </a>
        <p class="site-footer__about">HM UNIQUE is a trusted supplier of Electricals, Electronics, Hardwares and Industrial Tools committed to quality, reliability and customer satisfaction.</p>
        <div class="site-footer__socials">
          <a aria-label="Facebook" aria-disabled="true">FB</a>
          <a aria-label="LinkedIn" aria-disabled="true">IN</a>
          <a aria-label="Instagram" aria-disabled="true">IG</a>
          <a href="https://wa.me/919876543210" target="_blank" rel="noopener" aria-label="WhatsApp">WA</a>
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
        </ul>
      </div>

      <div class="site-footer__col">
        <h3 class="site-footer__heading">Contact Us</h3>
        <ul class="site-footer__contact">
          <li><span>123, Industrial Estate, Phase 1, Coimbatore &ndash; 641 021, Tamil Nadu, India</span></li>
          <li><a href="tel:+919876543210">+91 98765 43210</a></li>
          <li><a href="mailto:info@hmunique.com">info@hmunique.com</a></li>
          <li><span>Mon &ndash; Sat: 9:00 AM &ndash; 6:00 PM</span></li>
        </ul>
      </div>
    </div>
  </div>

  <div class="site-footer__bottom">
    <div class="container site-footer__bottom-inner">
      <span>&copy; <span data-current-year></span> HM UNIQUE. All Rights Reserved.</span>
      <div class="site-footer__bottom-links">
        <a aria-disabled="true">Privacy Policy</a>
        <a aria-disabled="true">Terms &amp; Conditions</a>
      </div>
    </div>
  </div>
</footer>"""


def build_floating_actions():
    return """<div class="floating-actions floating-actions--left">
  <a class="floating-btn floating-btn--whatsapp" href="https://wa.me/919876543210" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2z" fill="currentColor"/></svg>
  </a>
</div>
<div class="floating-actions floating-actions--right">
  <a class="floating-btn floating-btn--call" href="tel:+919876543210" aria-label="Call HM UNIQUE">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24 11 11 0 0 0 3.4.55 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11 11 0 0 0 .55 3.4 1 1 0 0 1-.25 1z" fill="currentColor"/></svg>
  </a>
</div>
<button type="button" class="scroll-top-btn" data-scroll-top aria-label="Scroll to top">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5l7 7M12 5l-7 7M12 5v14" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
</button>"""


def build_quote_modal():
    return """<div class="modal-overlay" data-modal="quote" aria-hidden="true">
  <div class="modal modal--quote" role="dialog" aria-modal="true" aria-labelledby="quote-modal-title">
    <button type="button" class="modal__close" data-modal-close aria-label="Close">&times;</button>

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

        <label class="form-checkbox">
          <input type="checkbox" name="privacy" data-required />
          <span>I agree to the <a aria-disabled="true">privacy policy</a>.</span>
        </label>

        <p class="form-submit-error" data-form-error hidden role="alert">
          Something went wrong sending your request. Please try again, or call us directly at <a href="tel:+919876543210">+91 98765 43210</a>.
        </p>

        <button type="submit" class="btn btn--primary btn--block mt-4">
          Submit Request
          <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h12M9 3l5 5-5 5" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
        </button>

        <p class="modal__note">
          <svg viewBox="0 0 16 16" aria-hidden="true" width="14" height="14"><path d="M8 1l6 2.5v4c0 4-2.6 6.7-6 7.5-3.4-.8-6-3.5-6-7.5v-4L8 1z" stroke="currentColor" stroke-width="1.2" fill="none"/></svg>
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
        <p><strong>Need Help?</strong><br />Call us at <a href="tel:+919876543210">+91 98765 43210</a></p>
      </div>
    </aside>
  </div>
</div>"""


def build_thank_you_modal():
    return """<div class="modal-overlay" data-modal="thank-you" aria-hidden="true">
  <div class="modal modal--thank-you" role="dialog" aria-modal="true" aria-labelledby="thank-you-modal-title">
    <button type="button" class="modal__close" data-modal-close aria-label="Close">&times;</button>

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
    "bolt": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2 4 14h6l-1 8 9-12h-6l1-8z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/></svg>',
    "chip": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="7" y="7" width="10" height="10" rx="1.5" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "wrench": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.1L3 18l3 3 6.6-6.3a4 4 0 0 0 5.1-5.4l-2.8 2.8-2-2 2.8-2.8z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/></svg>',
    "factory": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21V11l5 3v-3l5 3V8l6 4v9H3z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/><path d="M7 21v-4M12 21v-4M17 21v-4" stroke="currentColor" stroke-width="1.4"/></svg>',
    "grid": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="8" height="8" rx="1.2" stroke="currentColor" stroke-width="1.6" fill="none"/><rect x="13" y="3" width="8" height="8" rx="1.2" stroke="currentColor" stroke-width="1.6" fill="none"/><rect x="3" y="13" width="8" height="8" rx="1.2" stroke="currentColor" stroke-width="1.6" fill="none"/><rect x="13" y="13" width="8" height="8" rx="1.2" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>',
    "shield-check": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 4 5v6c0 5 3.4 8.7 8 10 4.6-1.3 8-5 8-10V5l-8-3z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/><path d="M8.5 12.2l2.4 2.4 4.6-4.8" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "award": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="5" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M8.5 12.5 7 22l5-3 5 3-1.5-9.5" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/></svg>',
    "truck": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 6h11v10H2z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/><path d="M13 10h4l4 3v3h-8z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/><circle cx="6" cy="18" r="1.8" stroke="currentColor" stroke-width="1.6" fill="none"/><circle cx="17" cy="18" r="1.8" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>',
    "tag": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3h6a3 3 0 0 1 3 3v6l-9 9-9-9 9-9z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/><circle cx="15" cy="9" r="1.4" fill="currentColor"/></svg>',
    "headset": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13v-1a8 8 0 0 1 16 0v1" stroke="currentColor" stroke-width="1.6" fill="none"/><rect x="2.5" y="13" width="4" height="6" rx="1.4" stroke="currentColor" stroke-width="1.6" fill="none"/><rect x="17.5" y="13" width="4" height="6" rx="1.4" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M20 19v1a3 3 0 0 1-3 3h-3" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>',
    "hard-hat": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 17a8 8 0 0 1 16 0z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/><path d="M2 17h20M11 5v4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "droplet": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2s7 8 7 13a7 7 0 1 1-14 0c0-5 7-13 7-13z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/></svg>',
    "building": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="1" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M8 8h2M14 8h2M8 12h2M14 12h2M8 16h2M14 16h2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "gear": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M12 2v3M12 19v3M22 12h-3M5 12H2M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1M18.4 18.4l-2.1-2.1M7.7 7.7 5.6 5.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "box": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 8l9-5 9 5-9 5-9-5z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/><path d="M3 8v9l9 5 9-5V8M12 13v9" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/></svg>',
    "arrow-right": '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h12M9 3l5 5-5 5" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>',
    "play": '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3l8 5-8 5V3z" fill="currentColor"/></svg>',
    "chevron-left": '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M10 2 4 8l6 6" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>',
    "chevron-right": '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M6 2l6 6-6 6" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>',
    "placeholder-image": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="1.5" stroke="currentColor" stroke-width="1.4" fill="none"/><circle cx="8.5" cy="9.5" r="1.6" stroke="currentColor" stroke-width="1.4" fill="none"/><path d="M21 16l-5.5-5.5L9 17" stroke="currentColor" stroke-width="1.4" fill="none" stroke-linejoin="round"/></svg>',
    "check": '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5l3.5 3.5L13 4" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "download": '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2v8m0 0 3-3m-3 3L5 7M2 12v1a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-1" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "file": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h9l5 5v15H6z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/><path d="M14 2v6h6" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/></svg>',
    "cable": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 8a4 4 0 0 1 8 0v8a4 4 0 0 0 8 0" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round"/><circle cx="4" cy="8" r="1.6" stroke="currentColor" stroke-width="1.6" fill="none"/><circle cx="20" cy="16" r="1.6" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>',
    "screw": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3 3-9 9-3 3v-3l9-9z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/><path d="M13 4l2 2M9 8l2 2M6 11l2 2M4 21l3-1-2-2z" stroke="currentColor" stroke-width="1.4" fill="none" stroke-linejoin="round"/></svg>',
    "pump": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="7" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M12 6v6l4 2" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "map-pin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22s7-7.5 7-13a7 7 0 1 0-14 0c0 5.5 7 13 7 13z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/><circle cx="12" cy="9" r="2.4" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M12 7v5l3.5 2" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.24 11 11 0 0 0 3.4.55 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11 11 0 0 0 .55 3.4 1 1 0 0 1-.25 1z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="1.5" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M4 6.5l8 6 8-6" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "target": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8" stroke="currentColor" stroke-width="1.6" fill="none"/><circle cx="12" cy="12" r="4.5" stroke="currentColor" stroke-width="1.6" fill="none"/><circle cx="12" cy="12" r="1.2" fill="currentColor"/></svg>',
    "compass": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.6" fill="none"/><path d="M15.5 8.5l-2 5-5 2 2-5z" stroke="currentColor" stroke-width="1.4" fill="none" stroke-linejoin="round"/></svg>',
    "handshake": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 12l4-4 4 2 3-3 4 4-3 3-3-2-3 3z" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/><path d="M14 11l4 4-2 2M6 13l-2 2 3 3" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "milestone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 2v20M5 4h13l-3 4 3 4H5" stroke="currentColor" stroke-width="1.6" fill="none" stroke-linejoin="round"/></svg>',
    "whatsapp": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2z" fill="currentColor"/></svg>',
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
    # -------------------------------------------------------------
    hero_badges = [
        ("grid", "Wide Product Range"),
        ("shield-check", "Quality Assured"),
        ("award", "Trusted Brands"),
        ("truck", "Timely Delivery"),
    ]
    hero_badges_html = "\n".join(
        f'''            <div class="trust-badge">
              <span class="trust-badge__icon">{ICONS[icon]}</span>
              <span>{label}</span>
            </div>'''
        for icon, label in hero_badges
    )

    # The concept shows 5 pagination dots on the hero carousel. Only one
    # hero design/copy was approved in the PDF, so every slide below
    # reuses that exact approved content rather than inventing new
    # marketing copy — this demonstrates the required slider mechanism
    # (autoplay, dots, manual arrows) without fabricating content that
    # wasn't in the source. Real slide variations (rotating photography,
    # alternate copy) should replace slides 2-5 once supplied.
    hero_slide = """          <div class="hero__slide" data-slider-slide>
            {}
          </div>""".format(img_placeholder("Electricals, electronics and industrial tools product collage", "aspect-box--tall"))
    hero_slides_html = "\n".join([hero_slide] * 5)

    hero_html = f"""    <section class="hero text-on-dark" aria-label="Hero">
      <div class="container hero__inner">
        <div class="hero__content">
          <span class="hero__eyebrow">One Source. Complete Solution.</span>
          <h1 class="hero__title">Your Trusted Partner in <span class="text-accent">Electricals, Electronics, Hardwares &amp; Industrial Tools</span></h1>
          <p class="hero__desc">Supplying quality products that power industries, build infrastructure and drive innovation.</p>

          <div class="hero__badges">
{hero_badges_html}
          </div>

          <div class="hero__actions">
            <a class="btn btn--primary" href="pages/electricals.html">
              Explore Products
              {ICONS['arrow-right']}
            </a>
            <a class="btn btn--outline-light" href="pages/about.html">
              {ICONS['play']}
              About HM Unique
            </a>
          </div>
        </div>

        <div class="hero__media">
          <div class="hero__slider" data-slider>
            <div class="hero__slider-track" data-slider-track>
{hero_slides_html}
            </div>
            <button type="button" class="btn-icon hero__nav hero__nav--prev" data-slider-prev aria-label="Previous slide">{ICONS['chevron-left']}</button>
            <button type="button" class="btn-icon hero__nav hero__nav--next" data-slider-next aria-label="Next slide">{ICONS['chevron-right']}</button>
          </div>
          <div class="hero__dots" data-slider-dots aria-label="Slide navigation"></div>
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # 4. PRODUCT CATEGORIES
    # -------------------------------------------------------------
    categories = [
        ("bolt", "Electricals", "Wires &amp; Cables, Switches, MCBs, Distribution Boards, Lighting &amp; more.", "pages/electricals.html"),
        ("chip", "Electronics Components", "CCTV, Sensors, Power Supplies, Automation, Test Instruments &amp; more.", "pages/electronics.html"),
        ("wrench", "Hardwares", "Fasteners, Hand Tools, Power Tools, Safety, Plumbing &amp; more.", "pages/hardwares.html"),
        ("factory", "Industrial &amp; Commercial Equipment", "Motors, Bearings, Pneumatics, Hydraulics, Welding &amp; more.", "pages/industrial-equipment.html"),
    ]
    category_cards_html = "\n".join(
        f"""          <article class="card card--hover category-card" data-animate="fade-up">
            <span class="card__icon">{ICONS[icon]}</span>
            <div class="category-card__media">
              {img_placeholder(name + ' category image')}
            </div>
            <h3 class="category-card__title">{name}</h3>
            <p class="category-card__desc">{desc}</p>
            <a class="link-arrow" href="{href}">
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
        <div class="grid grid--4">
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
        ("Hikvision CCTV Camera", "High clarity surveillance solutions."),
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
        <div class="grid grid--6">
{product_cards_html}
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # 6. WHY CHOOSE US
    # -------------------------------------------------------------
    why_choose = [
        ("shield-check", "Quality Products", "We supply only high quality products from trusted manufacturers."),
        ("grid", "Wide Range", "One-stop solution for Electricals, Electronics, Hardwares &amp; Industrial tools."),
        ("tag", "Competitive Pricing", "Best value for your money across all products."),
        ("truck", "Timely Delivery", "Prompt delivery ensuring minimal downtime for your projects."),
        ("headset", "Expert Support", "Our team is always ready to help you find the right products."),
    ]
    why_choose_html = "\n".join(
        f"""          <div class="feature-item" data-animate="fade-up">
            <span class="feature-item__icon">{ICONS[icon]}</span>
            <h3 class="feature-item__title">{title}</h3>
            <p class="feature-item__desc">{desc}</p>
          </div>"""
        for icon, title, desc in why_choose
    )

    why_choose_section = f"""    <section class="section section--dark text-on-dark" aria-labelledby="why-choose-heading">
      <div class="container">
        <div class="section-heading section-heading--center">
          <span class="eyebrow">Why Choose Us</span>
          <h2 class="section-heading__title" id="why-choose-heading">Commitment to Quality &amp; Service</h2>
        </div>
        <div class="grid grid--5">
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
        ("bolt", "Power &amp; Energy"),
        ("droplet", "Oil &amp; Gas"),
        ("truck", "Transportation"),
        ("building", "Infrastructure"),
        ("gear", "Automation"),
        ("box", "OEMs"),
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
    cta_section = f"""    <section class="section section--sm" aria-labelledby="cta-heading">
      <div class="container">
        <div class="cta-band text-on-dark">
          <div class="cta-band__inner">
            <div class="cta-band__text">
              <h2 class="cta-band__title" id="cta-heading">Looking for the Right Products for Your Project?</h2>
              <p>Send us your requirement and our experts will get back to you with the best solution.</p>
              <button type="button" class="btn btn--white mt-4" data-modal-open="quote">
                Request a Quote Now
                {ICONS['arrow-right']}
              </button>
            </div>
            <div class="cta-band__media">
              {img_placeholder('Request a quote illustration', 'aspect-box--square')}
            </div>
          </div>
        </div>
      </div>
    </section>"""

    return "\n\n".join([
        hero_html,
        categories_html,
        featured_html,
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
}


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

    hero_html = f"""    <section class="category-hero" aria-label="{cat['h1']} overview">
      <div class="container category-hero__inner">
        <div class="category-hero__content">
          <h1 class="category-hero__title">{cat['h1']}</h1>
          <p class="category-hero__desc">{cat['desc']}</p>
          <div class="category-hero__badges">
{badges_html}
          </div>
        </div>
        <div class="category-hero__media">
          {img_placeholder(cat['h1'] + ' hero image', 'aspect-box--tall')}
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # SUB-CATEGORY TAB STRIP
    # -------------------------------------------------------------
    tabs_html = "\n".join(
        f"""          <button type="button" class="category-tabs__item{' is-active' if i == 0 else ''}"{' aria-current="true"' if i == 0 else ''}>
            {ICONS[icon]}
            <span>{label}</span>
          </button>"""
        for i, (icon, label) in enumerate(cat["subcategories"])
    )

    tabs_section = f"""    <section class="section--sm section--light" aria-label="Sub-categories">
      <div class="container">
        <div class="category-tabs" data-tabs aria-label="{cat['h1']} sub-categories">
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

    products_section = f"""    <section class="section section--surface" aria-labelledby="popular-heading">
      <div class="container">
        <div class="section-heading section-heading--center">
          <h2 class="section-heading__title" id="popular-heading">{cat['popular_heading']}</h2>
          <p class="section-heading__subtitle">{cat['popular_sub']}</p>
        </div>
        <div class="grid grid--3">
{product_cards_html}
        </div>
      </div>
    </section>"""

    # -------------------------------------------------------------
    # INLINE CTA
    # -------------------------------------------------------------
    inline_cta = f"""    <section class="section--sm section--light" aria-label="Request more products">
      <div class="container">
        <div class="inline-cta">
          <span class="inline-cta__icon">{ICONS['file']}</span>
          <div class="inline-cta__text">
            <h3 class="inline-cta__title">Looking for more {cat['h1']} products?</h3>
            <p>We supply hundreds of additional variants from leading brands to match your exact requirements.</p>
          </div>
          <button type="button" class="btn btn--primary" data-modal-open="quote">
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

    catalogue_section = f"""    <section class="section--sm" aria-labelledby="catalogue-heading">
      <div class="container">
        <div class="cta-band cta-band--catalogue text-on-dark">
          <div class="catalogue-band__inner">
            <div class="catalogue-band__media">
              {img_placeholder(cat['catalogue_name'] + ' cover', 'aspect-box--square')}
            </div>
            <div class="catalogue-band__text">
              <h2 class="catalogue-band__title" id="catalogue-heading">Download Complete<br />{cat['catalogue_name']}</h2>
              <p>Browse detailed specifications, technical drawings, certifications and complete product information.</p>
              <div class="catalogue-band__features">
{catalogue_features_html}
              </div>
              <button type="button" class="btn btn--gold">
                {ICONS['download']}
                Download Catalogue PDF
              </button>
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

    return "\n\n".join([
        hero_html,
        tabs_section,
        products_section,
        inline_cta,
        catalogue_section,
        stats_section,
    ])


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
        <span class="page-banner__eyebrow">About HM UNIQUE</span>
        <h1 class="page-banner__title">Building Connections. Powering Industries.</h1>
        <p class="page-banner__desc">With 7+ years of experience, HM UNIQUE has emerged as a trusted supplier of Electricals, Electronics, Hardwares and Industrial Tools. Our commitment to quality, reliability and customer satisfaction drives everything we do.</p>
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
        f"""          <article class="milestone" data-animate="fade-up">
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
        ("grid", "Wide Product Range", "One-stop solution for Electricals, Electronics, Hardwares and Industrial Tools."),
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
        ("bolt", "Power &amp; Energy"),
        ("droplet", "Oil &amp; Gas"),
        ("truck", "Transportation"),
        ("building", "Infrastructure"),
        ("gear", "Automation"),
        ("box", "OEMs"),
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
    cta_section = f"""    <section class="section--sm" aria-labelledby="about-cta-heading">
      <div class="container">
        <div class="cta-band text-on-dark">
          <div class="cta-band__inner">
            <div class="cta-band__text">
              <h2 class="cta-band__title" id="about-cta-heading">Let&rsquo;s Build Something Great Together</h2>
              <p>Partner with HM UNIQUE for reliable, exceptional service and lasting business relationships.</p>
              <button type="button" class="btn btn--white mt-4" data-modal-open="quote">
                Request a Quote
                {ICONS['arrow-right']}
              </button>
            </div>
            <div class="cta-band__media">
              {img_placeholder('HM UNIQUE team illustration', 'aspect-box--square')}
            </div>
          </div>
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
        <span class="page-banner__eyebrow">Get In Touch</span>
        <h1 class="page-banner__title">Contact Us</h1>
        <p class="page-banner__desc">We&rsquo;re here to help you find the right products and solutions for your business.</p>
        <div class="page-banner__quicklinks">
          <span class="page-banner__quicklink">{ICONS['phone']} Call Us: +91 98765 43210</span>
          <span class="page-banner__quicklink">{ICONS['mail']} Email Us: info@hmunique.com</span>
          <span class="page-banner__quicklink">{ICONS['clock']} Mon &ndash; Sat: 9:00 AM &ndash; 6:00 PM</span>
          <span class="page-banner__quicklink">{ICONS['whatsapp']} WhatsApp: +91 98765 43210</span>
        </div>
      </div>
    </section>"""

    contact_form = f"""        <div>
          <h2 class="mb-2">Get In Touch</h2>
          <p class="text-body mb-5">Fill out the form and our team will get back to you shortly.</p>

          <p class="form-submit-error" data-form-error hidden role="alert">
            Something went wrong sending your message. Please try again, or call us directly at <a href="tel:+919876543210">+91 98765 43210</a>.
          </p>

          <form class="contact-form" data-form="contact" novalidate>
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

            <label class="form-checkbox">
              <input type="checkbox" name="privacy" data-required />
              <span>I agree to the <a aria-disabled="true">privacy policy</a>.</span>
            </label>

            <button type="submit" class="btn btn--primary btn--block mt-4">
              Send Message
              <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h12M9 3l5 5-5 5" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
            </button>
          </form>
        </div>"""

    contact_info = f"""        <div>
          <div class="info-card">
            <h3 class="info-card__title">Contact Information</h3>
            <ul class="info-card__list">
              <li>{ICONS['map-pin']}<span>Head Office<br />123, Industrial Estate, Phase 1, Coimbatore &ndash; 641 021, Tamil Nadu, India</span></li>
              <li>{ICONS['phone']}<span>+91 98765 43210<br />+91 422 456 7890</span></li>
              <li>{ICONS['mail']}<span>info@hmunique.com<br />sales@hmunique.com</span></li>
              <li>{ICONS['clock']}<span>Monday &ndash; Saturday: 9:00 AM &ndash; 6:00 PM<br />Sunday: Closed</span></li>
            </ul>

            <div class="whatsapp-cta">
              <span class="whatsapp-cta__icon">{ICONS['whatsapp']}</span>
              <div class="whatsapp-cta__text">
                <strong>Chat with us on WhatsApp</strong>
                <p class="mb-0">Get a quick response to your queries.</p>
              </div>
              <a class="btn btn--sm btn--primary" href="https://wa.me/919876543210" target="_blank" rel="noopener">Chat Now</a>
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
        <div class="info-card">
          <div class="flex flex--between flex--wrap flex--gap-3 mb-4">
            <div>
              <h3 class="info-card__title mb-1">Find Us Here</h3>
              <p class="text-body mb-0">We are located in the heart of the industrial hub for better connectivity and faster support.</p>
            </div>
            <a class="btn btn--outline btn--sm" href="https://maps.google.com" target="_blank" rel="noopener">
              Get Directions
              {ICONS['arrow-right']}
            </a>
          </div>
          <div class="aspect-box aspect-box--wide">
            {img_placeholder('Google Map showing HM UNIQUE head office location')}
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
        <article class="branch-card">
          <div class="branch-card__media">
            {img_placeholder('HM UNIQUE Chennai branch office', 'aspect-box--wide')}
          </div>
          <div class="branch-card__body">
            <h3 class="branch-card__title">HM UNIQUE &ndash; Chennai Branch</h3>
            <ul class="info-card__list">
              <li>{ICONS['map-pin']}<span>45, SIDCO Industrial Estate, Ambattur, Chennai &ndash; 600 098, Tamil Nadu, India</span></li>
              <li>{ICONS['phone']}<span>+91 44 2363 4567</span></li>
              <li>{ICONS['mail']}<span>chennai@hmunique.com</span></li>
              <li>{ICONS['clock']}<span>Mon &ndash; Sat: 9:00 AM &ndash; 6:00 PM</span></li>
            </ul>
          </div>
        </article>
      </div>
    </section>"""

    cta_section = f"""    <section class="section--sm" aria-labelledby="contact-cta-heading">
      <div class="container">
        <div class="cta-band text-on-dark">
          <div class="cta-band__inner">
            <div class="cta-band__text">
              <h2 class="cta-band__title" id="contact-cta-heading">Looking for the Right Products for Your Project?</h2>
              <p>Talk to our experts and get the best solution for your business.</p>
              <button type="button" class="btn btn--white mt-4" data-modal-open="quote">
                Request a Quote
                {ICONS['arrow-right']}
              </button>
            </div>
            <div class="cta-band__media">
              {img_placeholder('Contact HM UNIQUE illustration', 'aspect-box--square')}
            </div>
          </div>
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
# DOWNLOAD CENTRE PAGE
# ---------------------------------------------------------------------

DOWNLOAD_ITEMS = [
    ("file", "Electrical Catalogue", "Wires &amp; Cables, Switches, MCBs, Distribution Boards, Lighting and more.", "../assets/catalogue/electricals-catalogue.pdf"),
    ("chip", "Electronics Catalogue", "Passive, active, and semiconductor components for design and production.", "../assets/catalogue/electronics-catalogue.pdf"),
    ("wrench", "Hardware Catalogue", "Fasteners, hand tools, power tools, and industrial hardware accessories.", "../assets/catalogue/hardwares-catalogue.pdf"),
    ("factory", "Industrial Catalogue", "Material handling, pumps &amp; motors, ventilation, and facility equipment.", "../assets/catalogue/industrial-catalogue.pdf"),
    ("building", "Company Profile", "An overview of HM UNIQUE, our history, values, and capabilities.", "../assets/catalogue/company-profile.pdf"),
    ("box", "Product Datasheets", "Technical specifications and datasheets across our full product range.", "../assets/catalogue/product-datasheets.pdf"),
]


def build_download_centre_main():
    banner = f"""    <section class="page-banner text-on-dark" aria-label="Download Centre">
      <div class="container page-banner__inner">
        <span class="page-banner__eyebrow">Resources</span>
        <h1 class="page-banner__title">Download Centre</h1>
        <p class="page-banner__desc">Access our complete range of product catalogues, datasheets and company information &mdash; all in one place.</p>
      </div>
    </section>"""

    cards_html = "\n".join(
        f"""          <article class="card card--hover" data-animate="fade-up">
            <div class="download-card__media">
              {img_placeholder(title + ' cover', 'aspect-box--tall')}
            </div>
            <h3 class="download-card__title">{title}</h3>
            <p class="download-card__desc">{desc}</p>
            <a class="btn btn--gold btn--block" href="{href}" download>
              {ICONS['download']}
              Download PDF
            </a>
          </article>"""
        for icon, title, desc, href in DOWNLOAD_ITEMS
    )

    cards_section = f"""    <section class="section section--light" aria-labelledby="downloads-heading">
      <div class="container">
        <div class="section-heading section-heading--center">
          <span class="eyebrow">Resources</span>
          <h2 class="section-heading__title" id="downloads-heading">Available Downloads</h2>
        </div>
        <div class="grid grid--3">
{cards_html}
        </div>
      </div>
    </section>"""

    cta_section = f"""    <section class="section--sm" aria-labelledby="download-cta-heading">
      <div class="container">
        <div class="cta-band text-on-dark">
          <div class="cta-band__inner">
            <div class="cta-band__text">
              <h2 class="cta-band__title" id="download-cta-heading">Can&rsquo;t Find What You&rsquo;re Looking For?</h2>
              <p>Reach out to our team and we&rsquo;ll send you the specific documents or specifications you need.</p>
              <button type="button" class="btn btn--white mt-4" data-modal-open="quote">
                Request a Quote
                {ICONS['arrow-right']}
              </button>
            </div>
            <div class="cta-band__media">
              {img_placeholder('Download Centre illustration', 'aspect-box--square')}
            </div>
          </div>
        </div>
      </div>
    </section>"""

    return "\n\n".join([banner, cards_section, cta_section])


def build_organization_schema():
    """Organization + LocalBusiness JSON-LD, sitewide (identical on
    every page — this is the entity graph for the business itself,
    not page-specific content)."""
    data = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "HM UNIQUE",
        "url": SITE_URL,
        "logo": f"{SITE_URL}/assets/logo/hm-unique-logo.svg",
        "description": "Supplier of Electricals, Electronics Components, Hardwares and Industrial & Commercial Equipment.",
        "telephone": "+91-98765-43210",
        "email": "info@hmunique.com",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "123, Industrial Estate, Phase 1",
            "addressLocality": "Coimbatore",
            "addressRegion": "Tamil Nadu",
            "postalCode": "641021",
            "addressCountry": "IN",
        },
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "09:00",
            "closes": "18:00",
        },
        "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+91-98765-43210",
            "contactType": "customer service",
            "email": "info@hmunique.com",
            "areaServed": "IN",
            "availableLanguage": ["en"],
        },
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
        f"css/pages/{page['key']}.css" if page["key"] != "industrial" else "css/pages/industrial-equipment.css",
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

  <main id="main-content">
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
