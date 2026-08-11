/**
 * animations.js
 * Scroll-triggered reveal for any element carrying [data-animate], and
 * an animated count-up for stat numbers carrying [data-count-to].
 * Respects prefers-reduced-motion by simply doing nothing (the CSS
 * fallback in animations.css already shows the content at full
 * opacity in that case).
 */

function initScrollReveal() {
  const targets = document.querySelectorAll("[data-animate]");
  if (targets.length === 0) return;

  const prefersReducedMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;
  if (prefersReducedMotion) return;

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          obs.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
  );

  targets.forEach((el) => observer.observe(el));
}

/**
 * Animates a numeric stat (e.g. "5000+") counting up from 0 once it
 * scrolls into view. Expects data-count-to="5000" and preserves any
 * suffix already in the element's text (e.g. "+", "%").
 */
function initCountUp() {
  const targets = document.querySelectorAll("[data-count-to]");
  if (targets.length === 0) return;

  const DURATION_MS = 1200;

  const animateCount = (el) => {
    const target = Number(el.dataset.countTo);
    const suffix = el.dataset.countSuffix || "";
    if (Number.isNaN(target)) return;

    const start = performance.now();

    const step = (now) => {
      const progress = Math.min((now - start) / DURATION_MS, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
      const current = Math.round(target * eased);
      el.textContent = `${current}${suffix}`;
      if (progress < 1) requestAnimationFrame(step);
    };

    requestAnimationFrame(step);
  };

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCount(entry.target);
          obs.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.4 }
  );

  targets.forEach((el) => observer.observe(el));
}

export function initScrollAnimations() {
  initScrollReveal();
  initCountUp();
}
