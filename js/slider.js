/**
 * slider.js
 * Home hero carousel: accessible autoplay (with a pause/resume
 * control, keyboard/hover/hidden-tab pausing, and prefers-reduced-
 * motion support), dot pagination, prev/next arrows, and touch swipe
 * support. This module is written against the data-slider contract
 * below but stays a safe no-op on any page that doesn't have a
 * [data-slider] element.
 *
 * Markup contract:
 * <section data-slider tabindex="-1">
 *   <div data-slider-track>
 *     <div data-slider-slide>...</div>
 *     ...
 *   </div>
 *   <button data-slider-prev>...</button>
 *   <button data-slider-next>...</button>
 *   <button data-slider-playpause><i data-slider-playpause-icon></i></button>
 *   <div data-slider-dots></div>
 * </section>
 *
 * The root's own tabindex="-1" isn't a tab stop; it exists purely as
 * a safe, always-valid place to move focus to if a slide that
 * currently holds focus is about to be hidden (see setActiveSlide()).
 */

const AUTOPLAY_INTERVAL_MS = 5000;
const SWIPE_THRESHOLD_PX = 40;
// Slightly longer than css/pages/home.css's .hero__slider-track
// transition (650ms) so the real transitionend has every chance to
// fire first; this is purely a safety net for when it doesn't (no
// transition at all under prefers-reduced-motion, or a transition
// that gets interrupted), per "do not depend solely on
// transitionend" below.
const LOOP_SNAP_FALLBACK_MS = 750;

const REDUCED_MOTION_QUERY = "(prefers-reduced-motion: reduce)";

class Slider {
  constructor(rootEl) {
    this.root = rootEl;
    this.track = rootEl.querySelector("[data-slider-track]");
    this.slides = Array.from(rootEl.querySelectorAll("[data-slider-slide]"));
    this.prevBtn = rootEl.querySelector("[data-slider-prev]");
    this.nextBtn = rootEl.querySelector("[data-slider-next]");
    this.playPauseBtn = rootEl.querySelector("[data-slider-playpause]");
    this.playPauseIcon = rootEl.querySelector("[data-slider-playpause-icon]");
    this.dotsContainer = rootEl.querySelector("[data-slider-dots]");
    this.realCount = this.slides.length;
    this.currentIndex = 0;
    this.autoplayTimer = null;
    this.loopSnapFallbackTimer = null;
    this.pendingLoopSnap = false;

    // Autoplay runs only when every one of these is false — see
    // updateAutoplayState(). Each input is tracked independently so
    // no single event handler has to know about every other reason
    // autoplay might be paused.
    this.userPaused = false;
    this.isHovering = false;
    this.hasFocusWithin = false;
    // When the user explicitly activates Resume while keyboard focus
    // is still resting on the play/pause control, this lets autoplay
    // restart immediately without requiring focus to move anywhere —
    // see bindEvents() and updateAutoplayState(). It's cleared again
    // by an explicit Pause, or the next time focus freshly enters the
    // carousel, so a later Tab-in still pauses it as normal.
    this.focusPauseOverridden = false;
    this.isTabHidden = typeof document !== "undefined" && document.hidden;
    this.reducedMotionQuery =
      typeof window !== "undefined" && window.matchMedia
        ? window.matchMedia(REDUCED_MOTION_QUERY)
        : null;
    this.prefersReducedMotion = this.reducedMotionQuery?.matches ?? false;

    if (this.slides.length === 0) return;

    // Clone the first slide and append it after the last one so the
    // "last -> first" wrap can animate forward continuously instead of
    // snapping backwards. Once that clone finishes sliding into view
    // (or, under reduced motion, is skipped entirely — see next())
    // the track jumps (no transition) back to the real first slide at
    // index 0. The clone is permanently excluded from the
    // accessibility tree/tab order — it's a visual-only duplicate,
    // never a real destination.
    if (this.realCount > 1 && this.track) {
      const clone = this.slides[0].cloneNode(true);
      clone.setAttribute("aria-hidden", "true");
      clone.inert = true;
      this.track.appendChild(clone);
      this.slides.push(clone);

      this.track.addEventListener("transitionend", (event) => {
        if (event.target !== this.track || event.propertyName !== "transform") return;
        this.resolvePendingLoopSnap();
      });
    }

    this.applyReducedMotionPreference();
    this.setActiveSlide(0, { skipTransition: true });
    this.buildDots();
    this.bindEvents();
    this.updateAutoplayState();
  }

  // -------------------------------------------------------------
  // Active-slide / accessibility state
  // -------------------------------------------------------------

  /**
   * Makes `index` (a real slide index, never the clone) the only
   * slide exposed to keyboard and assistive tech, and moves the
   * track. Synchronizes visibility, inert and aria-hidden together so
   * they can never drift apart, and makes sure focus is never left
   * stranded inside a slide that's about to become inactive.
   */
  setActiveSlide(index, { skipTransition = false } = {}) {
    const previousIndex = this.currentIndex;
    this.currentIndex = index;

    if (skipTransition && this.track) {
      this.track.style.transition = "none";
    }
    if (this.track) {
      this.track.style.transform = `translateX(-${index * 100}%)`;
    }
    if (skipTransition && this.track) {
      void this.track.offsetHeight;
      // Restore whatever applyReducedMotionPreference() last set,
      // never blindly clear it — clearing it would fall back to the
      // CSS stylesheet's animated transition even while reduced
      // motion is active, re-enabling the exact sliding animation
      // this is meant to avoid.
      this.track.style.transition = this.prefersReducedMotion ? "none" : "";
    }

    this.slides.forEach((slide, i) => {
      // The clone (i === realCount) is never active — it's excluded
      // up front in the constructor and stays that way permanently.
      const isActive = i === index && i < this.realCount;
      if (!isActive && slide.contains(document.activeElement)) {
        // Never leave focus inside a slide that's about to become
        // inactive — move it to the carousel's own safe, always-
        // focusable root first. (Browsers also forcibly blur a
        // focused inert descendant, but doing this explicitly first
        // gives a deliberate, predictable focus target instead of
        // whatever the browser's own fallback happens to be.)
        this.root.focus();
      }
      slide.inert = !isActive;
      // aria-hidden is an enumerated attribute ("true" / "false"), not a
      // boolean one: toggleAttribute() would write aria-hidden="" for the
      // hidden state, which is not the "true" token. Inactive slides (and
      // the permanent loop clone) get an explicit "true"; the active slide
      // simply has no aria-hidden.
      if (isActive) {
        slide.removeAttribute("aria-hidden");
      } else {
        slide.setAttribute("aria-hidden", "true");
      }
    });

    this.dots?.forEach((dot, i) => {
      const isActive = i === index;
      dot.classList.toggle("is-active", isActive);
      // aria-current is a token attribute, not a boolean one:
      // toggleAttribute's "true" state would set aria-current="" (an
      // empty string), which isn't the "true" token the spec defines
      // for this kind of current-item marker. Set the explicit value
      // on the active dot and remove the attribute entirely from the
      // rest, rather than toggling its mere presence.
      if (isActive) {
        dot.setAttribute("aria-current", "true");
      } else {
        dot.removeAttribute("aria-current");
      }
    });

    return previousIndex;
  }

  // -------------------------------------------------------------
  // Dots
  // -------------------------------------------------------------

  buildDots() {
    if (!this.dotsContainer) return;
    this.dots = Array.from({ length: this.realCount }, (_, index) => {
      const dot = document.createElement("button");
      dot.type = "button";
      dot.setAttribute("aria-label", `Go to slide ${index + 1} of ${this.realCount}`);
      if (index === this.currentIndex) dot.classList.add("is-active");
      if (index === this.currentIndex) dot.setAttribute("aria-current", "true");
      dot.addEventListener("click", () => {
        this.goTo(index);
        // A manual dot click isn't the explicit pause control, so it
        // follows the same "respect an explicit pause" rule as the
        // prev/next buttons — see bindEvents().
        this.updateAutoplayState();
      });
      this.dotsContainer.appendChild(dot);
      return dot;
    });
  }

  // -------------------------------------------------------------
  // Events
  // -------------------------------------------------------------

  bindEvents() {
    this.prevBtn?.addEventListener("click", () => {
      this.prev();
      this.updateAutoplayState();
    });
    this.nextBtn?.addEventListener("click", () => {
      this.next();
      this.updateAutoplayState();
    });

    this.playPauseBtn?.addEventListener("click", () => {
      const wasPaused = this.userPaused;
      this.userPaused = !this.userPaused;
      if (this.userPaused) {
        // An explicit pause always wins outright and clears any
        // earlier override, so the next Resume has to be deliberately
        // activated again rather than inheriting a stale one.
        this.focusPauseOverridden = false;
      } else if (wasPaused && this.hasFocusWithin) {
        // Explicitly resuming while keyboard focus is still on this
        // control: let rotation actually restart now, without
        // requiring focus to leave the carousel first. This does not
        // move focus anywhere, and a later focusin event (e.g.
        // Tab-ing on to the next control) still pauses it again as
        // normal — see the focusin handler below.
        this.focusPauseOverridden = true;
      }
      this.syncPlayPauseControl();
      this.updateAutoplayState();
    });

    // Mouse hover pauses autoplay without touching the explicit-pause
    // flag, so leaving the carousel resumes it again (unless the user
    // had already explicitly paused it, or another reason to stay
    // paused still applies) — see updateAutoplayState().
    this.root.addEventListener("mouseenter", () => {
      this.isHovering = true;
      this.updateAutoplayState();
    });
    this.root.addEventListener("mouseleave", () => {
      this.isHovering = false;
      this.updateAutoplayState();
    });

    // Keyboard focus landing anywhere inside the carousel (an arrow
    // button, a dot, or a link/button inside the active slide) pauses
    // autoplay for as long as focus stays inside, same as hovering.
    // Gated on :focus-visible rather than firing for any focus at
    // all: a plain "focusin pauses" rule would also fire for the
    // ordinary mouse-click focus a button receives when clicked —
    // including this carousel's own pause/resume button — which would
    // make clicking "Resume" immediately re-pause itself, since focus
    // never leaves the control that was just clicked. :focus-visible
    // reflects browsers' own keyboard-vs-pointer distinction, so a
    // mouse click on Resume doesn't retrigger the pause, while
    // Tab-ing into the carousel still does.
    this.root.addEventListener("focusin", (event) => {
      if (!event.target.matches?.(":focus-visible")) return;
      // A fresh entry into the carousel (focus wasn't already inside
      // it) always (re)pauses it, clearing any earlier explicit-
      // resume-while-focused override from a previous visit — moving
      // focus between controls that are already inside the carousel
      // (e.g. Resume -> next dot) is not a fresh entry and leaves the
      // override as-is.
      if (!this.hasFocusWithin) {
        this.focusPauseOverridden = false;
      }
      this.hasFocusWithin = true;
      this.updateAutoplayState();
    });
    this.root.addEventListener("focusout", () => {
      // focusout fires before the new element actually has focus, so
      // defer the "is focus still inside (and still keyboard-style)?"
      // check to the next frame rather than reading
      // document.activeElement synchronously.
      requestAnimationFrame(() => {
        const active = document.activeElement;
        this.hasFocusWithin = this.root.contains(active) && !!active?.matches?.(":focus-visible");
        if (!this.hasFocusWithin) {
          // Focus has actually left the carousel entirely; drop the
          // override so the next entry starts from a clean state.
          this.focusPauseOverridden = false;
        }
        this.updateAutoplayState();
      });
    });

    // Pause while this browser tab isn't visible; resume on return
    // only if nothing else is still holding it paused.
    document.addEventListener("visibilitychange", () => {
      this.isTabHidden = document.hidden;
      this.updateAutoplayState();
    });

    // Live-react to the OS/browser-level reduced-motion setting
    // changing while the page stays open, in either direction.
    this.reducedMotionQuery?.addEventListener?.("change", (event) => {
      this.prefersReducedMotion = event.matches;
      this.applyReducedMotionPreference();
      this.updateAutoplayState();
    });

    let touchStartX = 0;
    let touchStartY = 0;
    let touchStartedOnControl = false;
    this.root.addEventListener(
      "touchstart",
      (event) => {
        touchStartX = event.touches[0].clientX;
        touchStartY = event.touches[0].clientY;
        // A tap that starts on an actual link/button (a slide's CTA,
        // the arrows, a dot, the play/pause control) is a tap, not a
        // swipe gesture — never let swipe-distance math second-guess
        // it into also changing slides underneath the person's tap.
        touchStartedOnControl = !!event.target.closest("a, button");
      },
      { passive: true }
    );
    this.root.addEventListener(
      "touchend",
      (event) => {
        if (touchStartedOnControl) return;
        const deltaX = event.changedTouches[0].clientX - touchStartX;
        const deltaY = event.changedTouches[0].clientY - touchStartY;
        // Require the gesture to be clearly more horizontal than
        // vertical before treating it as a swipe, so a vertical page
        // scroll that happens to drift sideways a little never gets
        // misread as a slide-change request. (These listeners are
        // passive and never call preventDefault, so vertical page
        // scrolling itself is never blocked either way.)
        if (Math.abs(deltaX) < SWIPE_THRESHOLD_PX) return;
        if (Math.abs(deltaX) <= Math.abs(deltaY)) return;
        deltaX > 0 ? this.prev() : this.next();
        this.updateAutoplayState();
      },
      { passive: true }
    );
  }

  // -------------------------------------------------------------
  // Reduced motion
  // -------------------------------------------------------------

  applyReducedMotionPreference() {
    if (!this.track) return;
    // The CSS transition is the ONLY thing that produces the sliding
    // animation; removing it here (rather than toggling a class the
    // stylesheet would also need a matching rule for) is enough to
    // satisfy "avoid sliding animation when enabled" while leaving
    // every other visual rule in css/pages/home.css untouched.
    this.track.style.transition = this.prefersReducedMotion ? "none" : "";
  }

  // -------------------------------------------------------------
  // Autoplay state machine
  // -------------------------------------------------------------

  /** The single source of truth for whether autoplay should be
   * running right now. Always stops any existing timer first, then
   * starts a new one only if every pause condition is false — this
   * ordering is what guarantees at most one timer ever exists, no
   * matter how many of the independent event handlers above fire in
   * quick succession ("avoid duplicate timers"). */
  updateAutoplayState() {
    this.stopAutoplay();
    // Keyboard focus inside the carousel blocks autoplay, UNLESS an
    // explicit Resume activation just overrode it for this same focus
    // visit (see bindEvents()'s playPauseBtn handler and the focusin
    // handler above).
    const focusBlocksAutoplay = this.hasFocusWithin && !this.focusPauseOverridden;
    const shouldPlay =
      this.realCount > 1 &&
      !this.userPaused &&
      !this.isHovering &&
      !focusBlocksAutoplay &&
      !this.isTabHidden &&
      !this.prefersReducedMotion;
    if (shouldPlay) {
      this.autoplayTimer = window.setInterval(() => this.next(), AUTOPLAY_INTERVAL_MS);
    }
  }

  stopAutoplay() {
    if (this.autoplayTimer) {
      window.clearInterval(this.autoplayTimer);
      this.autoplayTimer = null;
    }
  }

  syncPlayPauseControl() {
    if (!this.playPauseBtn) return;
    this.playPauseBtn.setAttribute(
      "aria-label",
      this.userPaused ? "Resume slideshow" : "Pause slideshow"
    );
    this.playPauseIcon?.classList.toggle("fa-pause", !this.userPaused);
    this.playPauseIcon?.classList.toggle("fa-play", this.userPaused);
  }

  // -------------------------------------------------------------
  // Navigation / looping
  // -------------------------------------------------------------

  /** If a forward loop-wrap (last slide -> clone) is still waiting to
   * snap back to the real first slide, do that right now. Called at
   * the start of every other navigation method so rapid repeated
   * clicks can never leave currentIndex pointing at the out-of-range
   * clone slot — the exact failure mode that produced a blank/
   * incorrect slide when next() was clicked again before the
   * original snap had happened. */
  resolvePendingLoopSnap() {
    if (!this.pendingLoopSnap) return;
    if (this.loopSnapFallbackTimer) {
      window.clearTimeout(this.loopSnapFallbackTimer);
      this.loopSnapFallbackTimer = null;
    }
    this.pendingLoopSnap = false;
    this.setActiveSlide(0, { skipTransition: true });
  }

  goTo(index) {
    this.resolvePendingLoopSnap();
    this.setActiveSlide((index + this.realCount) % this.realCount);
  }

  next() {
    this.resolvePendingLoopSnap();

    const isLastRealSlide = this.currentIndex === this.realCount - 1;
    const hasClone = this.slides.length > this.realCount;

    if (isLastRealSlide && hasClone) {
      if (this.prefersReducedMotion) {
        // No sliding animation at all under reduced motion: jump
        // straight to the real first slide, skipping the animated
        // clone step (and the transition it would otherwise need)
        // entirely, so there's nothing to "snap back" from.
        this.goTo(0);
        return;
      }

      // Animate forward into the cloned first slide. The dots/aria
      // state already reflect "slide 1" (via the dot-only update
      // below) so pagination reads correctly throughout the
      // animation, even though currentIndex itself is still the
      // transient clone index until the snap resolves.
      this.currentIndex = this.realCount;
      if (this.track) {
        this.track.style.transform = `translateX(-${this.currentIndex * 100}%)`;
      }
      this.dots?.forEach((dot, i) => {
        const isActive = i === 0;
        dot.classList.toggle("is-active", isActive);
        // Same explicit-value requirement as setActiveSlide() above —
        // this transient clone-step update must match it exactly.
        if (isActive) {
          dot.setAttribute("aria-current", "true");
        } else {
          dot.removeAttribute("aria-current");
        }
      });

      this.pendingLoopSnap = true;
      // transitionend (bound once in the constructor) is the normal
      // path; this timeout is the explicit fallback for when it
      // doesn't fire — reduced motion toggled mid-flight, an
      // interrupted/cancelled transition, etc. — so looping never
      // depends on transitionend alone.
      if (this.loopSnapFallbackTimer) window.clearTimeout(this.loopSnapFallbackTimer);
      this.loopSnapFallbackTimer = window.setTimeout(() => {
        this.loopSnapFallbackTimer = null;
        this.resolvePendingLoopSnap();
      }, LOOP_SNAP_FALLBACK_MS);
      return;
    }

    this.goTo(this.currentIndex + 1);
  }

  prev() {
    this.resolvePendingLoopSnap();
    this.goTo(this.currentIndex - 1);
  }
}

export function initSlider() {
  document.querySelectorAll("[data-slider]").forEach((rootEl) => new Slider(rootEl));
}
