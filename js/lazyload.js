/**
 * lazyload.js
 * Most images use the native `loading="lazy"` attribute directly in
 * the HTML, which needs no JavaScript. This module only handles the
 * cases native lazy-loading can't: elements that set their image via
 * a CSS background (e.g. [data-bg-src]), where an IntersectionObserver
 * is required.
 */

export function initLazyLoad() {
  const bgTargets = document.querySelectorAll("[data-bg-src]");
  if (bgTargets.length === 0) return;

  const supportsIO = "IntersectionObserver" in window;

  const applyBackground = (el) => {
    const src = el.dataset.bgSrc;
    if (!src) return;
    el.style.backgroundImage = `url("${src}")`;
    el.classList.add("is-loaded");
  };

  if (!supportsIO) {
    // Fallback for very old browsers: just load everything immediately
    bgTargets.forEach(applyBackground);
    return;
  }

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          applyBackground(entry.target);
          obs.unobserve(entry.target);
        }
      });
    },
    { rootMargin: "200px 0px" }
  );

  bgTargets.forEach((el) => observer.observe(el));
}
