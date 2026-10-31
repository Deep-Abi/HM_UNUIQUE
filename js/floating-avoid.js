/**
 * floating-avoid.js
 *
 * The fixed WhatsApp / Call / scroll-to-top buttons sit in the bottom
 * corners of the viewport, so on a short or narrow screen they can rest on
 * top of copy and calls to action that scroll underneath them (the homepage
 * hero at 512x384 CSS px, for example). Static CSS cannot prevent that
 * because the copy spans the width of a phone screen.
 *
 * An element opts in with  data-float-avoid="<selector>"  (the selector is
 * resolved inside that element). While any text line, icon or button box
 * matched by it would be covered by a floating button, that button is eased
 * out of the way (.is-avoiding: transparent, not clickable). It returns as
 * soon as the copy has scrolled clear. A button that has keyboard focus is
 * always shown (see components.css), so nothing becomes unreachable by
 * keyboard. Pages with no data-float-avoid element are untouched.
 *
 * The Contact page also opts in its enquiry form (labels, fields, validation
 * messages, consent, submit), so the buttons never sit over a field.
 */

const FLOAT_SELECTOR = ".floating-btn, .scroll-top-btn";
const MARGIN_PX = 6;

function collectRects(zone, selector) {
  const rects = [];
  const range = document.createRange();
  zone.querySelectorAll(selector).forEach((root) => {
    // Slides that are not showing are inert; their copy is off-screen.
    if (root.closest("[inert]")) return;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const node = walker.currentNode;
      if (!node.nodeValue.trim()) continue;
      range.selectNodeContents(node);
      for (const r of range.getClientRects()) {
        if (r.width > 1 && r.height > 1) rects.push(r);
      }
    }
    // Buttons/links (their whole box), form controls (a field's box has no
    // text node of its own) and icon glyphs.
    const boxes = ".btn, a, button, svg, i, input, select, textarea";
    // querySelectorAll skips `root` itself, so a matched control (an input
    // or button chosen directly by data-float-avoid) is added explicitly.
    const own = root.matches(boxes) ? [root] : [];
    [...own, ...root.querySelectorAll(boxes)].forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.width > 1 && r.height > 1) rects.push(r);
    });
  });
  return rects;
}

export function initFloatingAvoid() {
  const zones = Array.from(document.querySelectorAll("[data-float-avoid]"));
  const floats = Array.from(document.querySelectorAll(FLOAT_SELECTOR));
  if (!zones.length || !floats.length) return;

  let queued = false;

  const update = () => {
    queued = false;
    const vh = window.innerHeight;
    const blockers = [];
    zones.forEach((zone) => {
      const z = zone.getBoundingClientRect();
      if (z.bottom < 0 || z.top > vh) return; // zone not on screen
      blockers.push(...collectRects(zone, zone.dataset.floatAvoid));
    });
    floats.forEach((btn) => {
      const f = btn.getBoundingClientRect();
      if (f.width === 0) return;
      const hit = blockers.some(
        (r) =>
          r.left < f.right + MARGIN_PX &&
          r.right > f.left - MARGIN_PX &&
          r.top < f.bottom + MARGIN_PX &&
          r.bottom > f.top - MARGIN_PX
      );
      btn.classList.toggle("is-avoiding", hit);
    });
  };

  const queue = () => {
    if (queued) return;
    queued = true;
    window.requestAnimationFrame(update);
  };

  window.addEventListener("scroll", queue, { passive: true });
  window.addEventListener("resize", queue);
  window.addEventListener("load", queue);
  // Carousel: slides move on transitionend / on click / on keyboard.
  document.addEventListener("transitionend", queue, true);
  document.addEventListener("click", queue, true);
  document.addEventListener("keyup", queue, true);
  // Forms: focusing/typing can scroll the page or reveal a validation
  // message, which changes what sits under a floating button.
  document.addEventListener("focusin", queue, true);
  document.addEventListener("input", queue, true);
  document.addEventListener("change", queue, true);
  document.addEventListener("submit", queue, true);
  if (window.ResizeObserver) {
    const ro = new ResizeObserver(queue);
    zones.forEach((z) => ro.observe(z));
  }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(queue);
  queue();
}
