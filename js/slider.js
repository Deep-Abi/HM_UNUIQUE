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

const AUTOPLAY_INTERVAL_MS = 5000;
const SWIPE_THRESHOLD_PX = 40;

class Slider {
  constructor(rootEl) {
    this.root = rootEl;
    this.track = rootEl.querySelector("[data-slider-track]");
    this.slides = Array.from(rootEl.querySelectorAll("[data-slider-slide]"));
    this.prevBtn = rootEl.querySelector("[data-slider-prev]");
    this.nextBtn = rootEl.querySelector("[data-slider-next]");
    this.dotsContainer = rootEl.querySelector("[data-slider-dots]");
    this.realCount = this.slides.length;
    this.currentIndex = 0;
    this.autoplayTimer = null;

    if (this.slides.length === 0) return;

    // Clone the first slide and append it after the last one so the
    // "last -> first" wrap can animate forward continuously instead of
    // snapping backwards. Once that clone finishes sliding into view we
    // jump (no transition) to the real first slide at index 0.
    if (this.realCount > 1 && this.track) {
      const clone = this.slides[0].cloneNode(true);
      clone.setAttribute("aria-hidden", "true");
      clone.setAttribute("inert", "");
      this.track.appendChild(clone);
      this.slides.push(clone);

      this.track.addEventListener("transitionend", (event) => {
        if (event.target !== this.track) return;
        if (this.currentIndex === this.realCount) {
          this.track.style.transition = "none";
          this.currentIndex = 0;
          this.track.style.transform = "translateX(0%)";
          // Force reflow so the transition-less jump applies before
          // transitions are re-enabled for the next slide change.
          void this.track.offsetHeight;
          this.track.style.transition = "";
        }
      });
    }

    this.buildDots();
    this.bindEvents();
    this.goTo(0);
    this.startAutoplay();
  }

  buildDots() {
    if (!this.dotsContainer) return;
    this.dots = Array.from({ length: this.realCount }, (_, index) => {
      const dot = document.createElement("button");
      dot.type = "button";
      dot.setAttribute("aria-label", `Go to slide ${index + 1}`);
      dot.addEventListener("click", () => {
        this.goTo(index);
        this.startAutoplay();
      });
      this.dotsContainer.appendChild(dot);
      return dot;
    });
  }

  bindEvents() {
    this.prevBtn?.addEventListener("click", () => {
      this.prev();
      this.startAutoplay();
    });
    this.nextBtn?.addEventListener("click", () => {
      this.next();
      this.startAutoplay();
    });

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
    this.currentIndex = (index + this.realCount) % this.realCount;
    if (this.track) {
      this.track.style.transform = `translateX(-${this.currentIndex * 100}%)`;
    }
    this.dots?.forEach((dot, i) => {
      dot.classList.toggle("is-active", i === this.currentIndex);
    });
  }

  next() {
    if (this.currentIndex === this.realCount - 1 && this.slides.length > this.realCount) {
      // Slide forward into the cloned first slide; transitionend snaps
      // back to the real index 0 without an animation.
      this.currentIndex = this.realCount;
      if (this.track) {
        this.track.style.transform = `translateX(-${this.currentIndex * 100}%)`;
      }
      this.dots?.forEach((dot, i) => dot.classList.toggle("is-active", i === 0));
      return;
    }
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
