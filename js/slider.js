/**
 * slider.js
 * Home hero carousel: autoplay, dot pagination, prev/next arrows, and
 * touch swipe support. This module is written against the data-slider
 * contract below but stays a safe no-op on any page that doesn't have
 * a [data-slider] element yet — the Home hero itself is built in
 * Phase 3, this file only needs to exist and be wired now.
 *
 * Expected markup contract (for Phase 3):
 * <div data-slider>
 *   <div data-slider-track>
 *     <div data-slider-slide>...</div>
 *     ...
 *   </div>
 *   <button data-slider-prev>...</button>
 *   <button data-slider-next>...</button>
 *   <div data-slider-dots></div>
 * </div>
 */

const AUTOPLAY_INTERVAL_MS = 6000;
const SWIPE_THRESHOLD_PX = 40;

class Slider {
  constructor(rootEl) {
    this.root = rootEl;
    this.track = rootEl.querySelector("[data-slider-track]");
    this.slides = Array.from(rootEl.querySelectorAll("[data-slider-slide]"));
    this.prevBtn = rootEl.querySelector("[data-slider-prev]");
    this.nextBtn = rootEl.querySelector("[data-slider-next]");
    this.dotsContainer = rootEl.querySelector("[data-slider-dots]");
    this.currentIndex = 0;
    this.autoplayTimer = null;

    if (this.slides.length === 0) return;

    this.buildDots();
    this.bindEvents();
    this.goTo(0);
    this.startAutoplay();
  }

  buildDots() {
    if (!this.dotsContainer) return;
    this.dots = this.slides.map((_, index) => {
      const dot = document.createElement("button");
      dot.type = "button";
      dot.setAttribute("aria-label", `Go to slide ${index + 1}`);
      dot.addEventListener("click", () => this.goTo(index));
      this.dotsContainer.appendChild(dot);
      return dot;
    });
  }

  bindEvents() {
    this.prevBtn?.addEventListener("click", () => this.prev());
    this.nextBtn?.addEventListener("click", () => this.next());

    this.root.addEventListener("mouseenter", () => this.stopAutoplay());
    this.root.addEventListener("mouseleave", () => this.startAutoplay());

    let touchStartX = 0;
    this.root.addEventListener(
      "touchstart",
      (event) => {
        touchStartX = event.touches[0].clientX;
      },
      { passive: true }
    );
    this.root.addEventListener(
      "touchend",
      (event) => {
        const deltaX = event.changedTouches[0].clientX - touchStartX;
        if (Math.abs(deltaX) < SWIPE_THRESHOLD_PX) return;
        deltaX > 0 ? this.prev() : this.next();
      },
      { passive: true }
    );
  }

  goTo(index) {
    this.currentIndex = (index + this.slides.length) % this.slides.length;
    if (this.track) {
      this.track.style.transform = `translateX(-${this.currentIndex * 100}%)`;
    }
    this.dots?.forEach((dot, i) => {
      dot.classList.toggle("is-active", i === this.currentIndex);
    });
  }

  next() {
    this.goTo(this.currentIndex + 1);
  }

  prev() {
    this.goTo(this.currentIndex - 1);
  }

  startAutoplay() {
    this.stopAutoplay();
    this.autoplayTimer = window.setInterval(() => this.next(), AUTOPLAY_INTERVAL_MS);
  }

  stopAutoplay() {
    if (this.autoplayTimer) window.clearInterval(this.autoplayTimer);
  }
}

export function initSlider() {
  document.querySelectorAll("[data-slider]").forEach((rootEl) => new Slider(rootEl));
}
