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

    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

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
