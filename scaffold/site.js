(function () {
  var nav = document.getElementById("site-nav");
  var toggle = document.getElementById("menu-toggle");
  var year = document.getElementById("year");
  var form = document.getElementById("demo-form");
  var status = document.getElementById("form-status");

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
      status.classList.add("show");
      status.focus();
      form.reset();
    });
  }
})();
