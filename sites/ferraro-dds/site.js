(function () {
  var nav = document.getElementById("site-nav");
  var toggle = document.getElementById("menu-toggle");
  var year = document.getElementById("year");
  var form = document.getElementById("contact-form");
  var status = document.getElementById("form-status");
  var error = document.getElementById("form-error");

  if (year) {
    year.textContent = String(new Date().getFullYear());
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll(".nav-toggle").forEach(function (btn) {
    btn.addEventListener("click", function (event) {
      event.preventDefault();
      var item = btn.closest(".nav-item, .nav-sub-item");
      if (!item) return;
      var willOpen = !item.classList.contains("open");
      var parent = item.parentElement;
      if (parent) {
        parent.querySelectorAll(":scope > .nav-item.open, :scope > .nav-sub-item.open").forEach(function (sib) {
          if (sib !== item) {
            sib.classList.remove("open");
            var other = sib.querySelector(".nav-toggle");
            if (other) other.setAttribute("aria-expanded", "false");
          }
        });
      }
      item.classList.toggle("open", willOpen);
      btn.setAttribute("aria-expanded", willOpen ? "true" : "false");
    });
  });

  function applyReducedMotionMedia() {
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
    var videos = document.querySelectorAll("video.videobgframe");
    function sync() {
      videos.forEach(function (video) {
        if (reduce.matches) {
          video.pause();
          video.removeAttribute("autoplay");
          video.setAttribute("hidden", "");
          video.classList.add("is-reduced");
        } else {
          video.removeAttribute("hidden");
          video.classList.remove("is-reduced");
          var play = video.play();
          if (play && typeof play.catch === "function") play.catch(function () {});
        }
      });
    }
    sync();
    if (typeof reduce.addEventListener === "function") {
      reduce.addEventListener("change", sync);
    } else if (typeof reduce.addListener === "function") {
      reduce.addListener(sync);
    }
  }
  applyReducedMotionMedia();

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && nav) {
      nav.querySelectorAll(".open").forEach(function (el) {
        el.classList.remove("open");
      });
      nav.querySelectorAll("[aria-expanded='true']").forEach(function (el) {
        if (el.id !== "menu-toggle") el.setAttribute("aria-expanded", "false");
      });
    }
  });

  if (form && status) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var name = form.elements.namedItem("name");
      var message = form.elements.namedItem("message");
      var missing = !name || !String(name.value).trim() || !message || !String(message.value).trim();
      if (missing) {
        if (error) {
          error.hidden = false;
          error.focus();
        }
        return;
      }
      if (error) {
        error.hidden = true;
      }
      status.classList.add("show");
      status.focus();
      form.reset();
    });
  }

  function initHeroCarousel() {
    var root = document.querySelector("[data-hero-carousel]");
    if (!root) return;
    var slides = root.querySelectorAll(".hero-slide");
    if (slides.length < 2) return;
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
    var index = 0;
    var timer = null;
    var paused = false;
    var pauseBtn = root.querySelector("[data-hero-pause]");
    var dots = root.querySelectorAll("[data-hero-dot]");

    function show(next) {
      index = (next + slides.length) % slides.length;
      slides.forEach(function (slide, n) {
        slide.classList.toggle("is-active", n === index);
      });
      dots.forEach(function (dot, n) {
        var current = n === index;
        dot.setAttribute("aria-current", current ? "true" : "false");
      });
    }
    function stop() {
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
    }
    function start() {
      stop();
      if (reduce.matches || paused) return;
      timer = setInterval(function () {
        show(index + 1);
      }, 6500);
    }
    if (pauseBtn) {
      pauseBtn.addEventListener("click", function () {
        paused = !paused;
        pauseBtn.setAttribute("aria-pressed", paused ? "true" : "false");
        pauseBtn.textContent = paused ? "Play" : "Pause";
        if (paused) stop();
        else start();
      });
    }
    dots.forEach(function (dot, n) {
      dot.addEventListener("click", function () {
        show(n);
        start();
      });
    });
    show(0);
    start();
    if (typeof reduce.addEventListener === "function") {
      reduce.addEventListener("change", start);
    } else if (typeof reduce.addListener === "function") {
      reduce.addListener(start);
    }
  }
  initHeroCarousel();

})();
