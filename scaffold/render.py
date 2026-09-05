"""Shared HTML chrome for sell-as-is local-business sites."""

from __future__ import annotations


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def nav_links(site: dict, current: str) -> str:
    items = []
    for href, label in site["nav"]:
        cur = ' aria-current="page"' if href == current else ""
        items.append(f'<a href="{esc(href)}"{cur}>{esc(label)}</a>')
    return "\n        ".join(items)


def brand(site: dict) -> str:
    logo = site["logo"]
    logo_class = site.get("logo_class", "logo")
    return f'''<a class="brand" href="index.html">
        <img class="{esc(logo_class)}" src="{esc(logo)}" alt="{esc(site["name"])}">
        <span class="brand-text">
          <strong>{esc(site["name"])}</strong>
          <span>{esc(site["tagline"])}</span>
        </span>
      </a>'''


def header(site: dict, current: str) -> str:
    phone = site["phone_display"]
    tel = site["phone_tel"]
    return f'''  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap header-row">
      {brand(site)}
      <nav id="site-nav" class="nav" aria-label="Primary">
        {nav_links(site, current)}
      </nav>
      <a class="btn btn-dark header-cta" href="tel:{esc(tel)}">Call {esc(phone)}</a>
      <button class="menu-btn" id="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    </div>
  </header>'''


def footer(site: dict) -> str:
    extra = site.get("footer_extra", "")
    legal = site.get(
        "legal",
        f'© <span id="year"></span> {esc(site["name"])}. All rights reserved.',
    )
    phone = site["phone_display"]
    tel = site["phone_tel"]
    return f'''  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <strong>{esc(site["name"])}</strong>
        <p>{esc(site["city"])}</p>
        <p><a href="tel:{esc(tel)}">{esc(phone)}</a></p>
        <p>{esc(site.get("address", ""))}</p>
      </div>
      <div>
        {extra}
        <p class="legal">{legal}</p>
      </div>
    </div>
  </footer>
  <div class="callbar">
    <a class="btn btn-primary" href="tel:{esc(tel)}">Call {esc(phone)}</a>
    <a class="btn btn-dark" href="{esc(site.get("contact_href", "contact.html"))}">Contact</a>
  </div>
  <script src="site.js"></script>'''


def page(site: dict, *, title: str, description: str, current: str, body: str) -> str:
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="theme.css">
</head>
<body{(' class="' + esc(site["body_class"]) + '"') if site.get("body_class") else ""}>
{header(site, current)}
  <main id="main">
{body}
  </main>
{footer(site)}
</body>
</html>
'''


def cards(items: list[dict]) -> str:
    out = []
    for item in items:
        extra = item.get("extra", "")
        out.append(
            f'<article class="card"><h3>{esc(item["title"])}</h3><p>{esc(item["text"])}</p>{extra}</article>'
        )
    return "\n".join(out)


def reviews(items: list[dict]) -> str:
    out = []
    for item in items:
        stars = item.get("stars", "★★★★★")
        source = f' <span class="muted">({esc(item["source"])})</span>' if item.get("source") else ""
        out.append(
            f'''<article class="card review">
          <div class="stars" aria-hidden="true">{stars}</div>
          <p>“{esc(item["quote"])}”</p>
          <p class="muted">— {esc(item["name"])}{source}</p>
        </article>'''
        )
    return "\n".join(out)


def chips(items: list[str]) -> str:
    return "\n".join(f'<span class="chip">{esc(item)}</span>' for item in items)


def contact_form(site: dict, intro: str = "") -> str:
    status = site.get(
        "form_status",
        "Thank you. This page does not send messages automatically — please call or email so the office receives your request.",
    )
    return f'''        <form class="card form" id="contact-form">
          <p>{esc(intro or "Send a message and follow up by phone so nothing is missed.")}</p>
          <label>Name <input name="name" autocomplete="name" required></label>
          <label>Phone <input name="phone" autocomplete="tel"></label>
          <label>Email <input name="email" type="email" autocomplete="email"></label>
          <label>Message <textarea name="message" rows="4" required></textarea></label>
          <button class="btn btn-dark" type="submit">Send message</button>
          <p class="form-status" id="form-status" tabindex="-1">{esc(status)}</p>
        </form>'''


def theme_css(site: dict) -> str:
    t = site["theme"]
    return f"""/* Brand tokens sampled from the live {site["slug"]} site */
:root {{
  --bg: {t["bg"]};
  --surface: {t["surface"]};
  --ink: {t["ink"]};
  --muted: {t["muted"]};
  --brand: {t["brand"]};
  --brand-2: {t["brand2"]};
  --accent: {t["accent"]};
  --hero-ink: {t["hero_ink"]};
  --font-display: {t["display"]};
  --hero-pattern: {t["pattern"]};
  --hero-pattern-size: {t.get("pattern_size", "24px 24px")};
}}
{t.get("extra_css", "")}
"""
