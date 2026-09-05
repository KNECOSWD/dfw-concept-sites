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
    if site.get("hide_brand_text"):
        return f'''<a class="brand" href="index.html">
        <img class="{esc(logo_class)}" src="{esc(logo)}" alt="{esc(site["name"])}">
      </a>'''
    return f'''<a class="brand" href="index.html">
        <img class="{esc(logo_class)}" src="{esc(logo)}" alt="{esc(site["name"])}">
        <span class="brand-text">
          <strong>{esc(site["name"])}</strong>
          <span>{esc(site["tagline"])}</span>
        </span>
      </a>'''


def header_cta(site: dict) -> str:
    if site.get("hide_header_cta"):
        return ""
    phone = site["phone_display"]
    tel = site["phone_tel"]
    href = site.get("header_cta_href", f"tel:{esc(tel)}")
    label = site.get("header_cta_label", f"Call {phone}")
    css = site.get("header_cta_class", "btn btn-dark header-cta")
    extra = ' target="_blank" rel="noopener noreferrer"' if href.startswith("http") else ""
    return f'<a class="{esc(css)}" href="{esc(href)}"{extra}>{esc(label)}</a>'


def header(site: dict, current: str) -> str:
    phone = site["phone_display"]
    tel = site["phone_tel"]
    body = site.get("body_class", "")
    strip = site.get("contact_strip", "")
    links = nav_links(site, current)
    cta = header_cta(site)
    skip = '  <a class="skip" href="#main">Skip to content</a>'
    menu = '<button class="menu-btn" id="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>'

    if "theme-centered-header" in body:
        return f'''{skip}
  {strip}
  <header class="site-header">
    <div class="wrap header-centered">
      {brand(site)}
      {menu}
      <nav id="site-nav" class="nav" aria-label="Primary">
        {links}
      </nav>
    </div>
  </header>'''

    if "theme-bar-nav" in body:
        phone_link = f'<a class="header-phone" href="tel:{esc(tel)}">{esc(phone)}</a>'
        return f'''{skip}
  {strip}
  <header class="site-header">
    <div class="wrap header-row">
      {brand(site)}
      {phone_link}
      {cta}
      {menu}
    </div>
    <nav id="site-nav" class="nav nav-bar" aria-label="Primary">
        {links}
    </nav>
  </header>'''

    return f'''{skip}
  {strip}
  <header class="site-header">
    <div class="wrap header-row">
      {brand(site)}
      <nav id="site-nav" class="nav" aria-label="Primary">
        {links}
      </nav>
      {cta}
      {menu}
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
        star_row = f'<div class="stars" aria-hidden="true">{esc(stars)}</div>' if stars else ""
        out.append(
            f'''<article class="card review">
          {star_row}
          <blockquote>
            <p>“{esc(item["quote"])}”</p>
            <footer class="muted">— {esc(item["name"])}{source}</footer>
          </blockquote>
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
    return f'''        <form class="card form" id="contact-form" novalidate>
          <p>{esc(intro or "Send a message and follow up by phone so nothing is missed.")}</p>
          <p class="note">This form stays on this page. It does not email the business.</p>
          <div class="field">
            <label for="contact-name">Name</label>
            <input id="contact-name" name="name" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="contact-phone">Phone</label>
            <input id="contact-phone" name="phone" type="tel" autocomplete="tel">
          </div>
          <div class="field">
            <label for="contact-email">Email</label>
            <input id="contact-email" name="email" type="email" autocomplete="email">
          </div>
          <div class="field">
            <label for="contact-message">Message</label>
            <textarea id="contact-message" name="message" rows="4" required></textarea>
          </div>
          <p class="form-error" id="form-error" hidden>Please complete the required fields: name and message.</p>
          <button class="btn btn-dark" type="submit">Send message</button>
          <p class="form-status" id="form-status" role="status" tabindex="-1">{esc(status)}</p>
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
  --font: {t.get("font", '"Segoe UI", "Helvetica Neue", system-ui, sans-serif')};
  --hero-pattern: {t["pattern"]};
  --hero-pattern-size: {t.get("pattern_size", "24px 24px")};
  --focus: {t.get("focus", "#111111")};
  --cta-ink: {t.get("cta_ink", "#ffffff")};
}}
{t.get("extra_css", "")}
"""
