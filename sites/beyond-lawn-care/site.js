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
})();
