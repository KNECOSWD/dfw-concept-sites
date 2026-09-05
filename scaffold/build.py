#!/usr/bin/env python3
"""Generate 10 self-contained KNECO concept sites from the shared scaffold."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD = Path(__file__).resolve().parent
SITES = ROOT / "sites"

MARKS = {
    "drop": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2s7 8.2 7 13a7 7 0 1 1-14 0C5 10.2 12 2 12 2z"/></svg>',
    "leaf": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 19c8-1 13-7 14-15-8 1-13 7-14 15zm0 0c2-4 6-7 11-8"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2 4 14h7l-1 8 10-14h-7l0-6z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 4 6v6c0 5.2 3.4 9.8 8 11 4.6-1.2 8-5.8 8-11V6l-8-4z"/></svg>',
    "building": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 21V5l8-3 8 3v16H4zm4-3h2v-3H8v3zm6 0h2v-3h-2v3zM8 12h2V9H8v3zm6 0h2V9h-2v3z"/></svg>',
    "cross": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 3h4v6h6v4h-6v8h-4v-8H4V9h6V3z"/></svg>',
    "wrench": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 7a5 5 0 0 1-6.7 4.7L7 19.1 4.9 17l7.4-7.3A5 5 0 1 1 21 7z"/></svg>',
    "tooth": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4c2-.8 3.2.4 5 .4S15 3.2 17 4c2 .8 2.6 3 2.2 5.2C18.6 12 17 21 14.5 21S13 15 12 15s-1.2 6-2.5 6S5.4 12 4.8 9.2C4.4 7 5 4.8 7 4z"/></svg>',
    "bowl": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 10h16l-1.2 5.2A5 5 0 0 1 13.9 19h-3.8a5 5 0 0 1-4.9-3.8L4 10zm4-5h8l1 3H7l1-3z"/></svg>',
    "scale": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2v2l8 3-4.2 7H16c0 2.2-1.8 4-4 4s-4-1.8-4-4h.2L4 7l8-3V2zm-5.2 8.1L8.8 7.4 6.8 10.1h5.6L8.8 7.4 6.8 10.1zM15.2 7.4l2 2.7h-4zM11 21h2v-3h-2v3z"/></svg>',
}


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def phone_link(site: dict) -> str:
    return f'tel:{site["phone_tel"]}'


def address_html(site: dict) -> str:
    flag = ' <span class="placeholder-flag">placeholder</span>' if site.get("address_placeholder") else ""
    return f'{esc(site["address"])}{flag}'


def phone_html(site: dict) -> str:
    flag = ' <span class="placeholder-flag">placeholder</span>' if site.get("phone_placeholder") else ""
    return f'<a href="{phone_link(site)}">{esc(site["phone_display"])}</a>{flag}'


def chips(items: list[str]) -> str:
    return "\n".join(f'<span class="chip">{esc(item)}</span>' for item in items)


def cards(items: list[dict]) -> str:
    return "\n".join(
        f'<article class="card"><h3>{esc(item["title"])}</h3><p>{esc(item["text"])}</p></article>'
        for item in items
    )


def reviews(items: list[dict]) -> str:
    return "\n".join(
        f'''<article class="card review">
          <div class="stars" aria-label="Five star placeholder">★★★★★</div>
          <p>“{esc(item["quote"])}”</p>
          <p class="muted">— {esc(item["name"])}</p>
        </article>'''
        for item in items
    )


def render(site: dict) -> str:
    theme = site["theme"]
    mark = MARKS[site["mark"]]
    cta_label = site["cta_label"]
    form_note = site.get(
        "form_note",
        "This form is a concept demo only. It does not send a message to the business.",
    )
    extra_note = site.get("extra_note", "")
    extra_block = f"<p class=\"note\">{esc(extra_note)}</p>" if extra_note else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(site["title"])}</title>
  <meta name="description" content="{esc(site["description"])}">
  <meta name="robots" content="noindex, nofollow">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="theme.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap header-row">
      <a class="brand" href="#top">
        <span class="mark">{mark}</span>
        <span class="brand-text">
          <strong>{esc(site["name"])}</strong>
          <span>{esc(site["city"])}</span>
        </span>
      </a>
      <nav id="site-nav" class="nav" aria-label="Primary">
        <a href="#services">{esc(site["services_nav"])}</a>
        <a href="#area">Service area</a>
        <a href="#reviews">{esc(site["reviews_nav"])}</a>
        <a href="#contact">Contact</a>
      </nav>
      <a class="btn btn-dark header-cta" href="{phone_link(site)}">{esc(cta_label)}</a>
      <button class="menu-btn" id="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    </div>
  </header>

  <main id="main">
    <section class="hero" id="top">
      <div class="wrap hero-grid">
        <div>
          <p class="eyebrow">{esc(site["eyebrow"])}</p>
          <h1>{esc(site["headline"])}</h1>
          <p class="lede">{esc(site["lede"])}</p>
          <div class="actions">
            <a class="btn btn-primary" href="{phone_link(site)}">{esc(cta_label)}</a>
            <a class="btn btn-ghost" href="#contact">{esc(site["secondary_cta"])}</a>
          </div>
        </div>
        <aside class="panel">
          <strong>{esc(site["panel_title"])}</strong>
          <p>{phone_html(site)}</p>
          <p>{address_html(site)}</p>
          <p>{esc(site["hours"])}</p>
          <div class="kpis">
            {"".join(f'<div><strong>{esc(k["value"])}</strong><span>{esc(k["label"])}</span></div>' for k in site["kpis"])}
          </div>
        </aside>
      </div>
    </section>

    <section id="services">
      <div class="wrap">
        <div class="section-head">
          <h2>{esc(site["services_heading"])}</h2>
          <p>{esc(site["services_intro"])}</p>
        </div>
        <div class="cards">
          {cards(site["services"])}
        </div>
      </div>
    </section>

    <section id="about">
      <div class="wrap about-grid">
        <div>
          <div class="section-head">
            <h2>{esc(site["about_heading"])}</h2>
            <p>{esc(site["about"])}</p>
          </div>
          {extra_block}
        </div>
        <div class="card">
          <h3>{esc(site["why_heading"])}</h3>
          <p>{esc(site["why"])}</p>
        </div>
      </div>
    </section>

    <section id="area">
      <div class="wrap">
        <div class="section-head">
          <h2>Service area</h2>
          <p>{esc(site["area_intro"])}</p>
        </div>
        <div class="chip-row">
          {chips(site["areas"])}
        </div>
      </div>
    </section>

    <section class="reviews" id="reviews">
      <div class="wrap">
        <div class="section-head">
          <h2>{esc(site["reviews_heading"])}</h2>
          <p>Placeholder comments for this concept demo — not copied from the live site and not claimed as verified reviews.</p>
        </div>
        <div class="cards">
          {reviews(site["reviews"])}
        </div>
      </div>
    </section>

    <section id="contact">
      <div class="wrap contact-grid">
        <div>
          <div class="section-head">
            <h2>{esc(site["contact_heading"])}</h2>
            <p>{esc(site["contact_intro"])}</p>
          </div>
          <p><strong>Phone:</strong> {phone_html(site)}</p>
          <p><strong>Location:</strong> {address_html(site)}</p>
          <p><strong>Hours:</strong> {esc(site["hours"])}</p>
          <p class="note">Reference homepage: {esc(site["source"])}</p>
        </div>
        <form class="card form" id="demo-form" novalidate>
          <label>Name <input name="name" autocomplete="name"></label>
          <label>Phone <input name="phone" autocomplete="tel"></label>
          <label>Message <textarea name="message" rows="4"></textarea></label>
          <button class="btn btn-dark" type="submit">{esc(site["form_cta"])}</button>
          <p class="note">{esc(form_note)}</p>
          <p class="form-status" id="form-status" tabindex="-1">Thanks — this concept page stored nothing and did not contact the business.</p>
        </form>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <strong>{esc(site["name"])}</strong>
        <p>{esc(site["city"])} · {esc(site["industry"])}</p>
      </div>
      <p>KNECO $500 DFW concept test · Matthew Sullivan / KNECOSWD</p>
    </div>
    <div class="wrap">
      <p class="demo-note">Concept demo / not the live business site. Static HTML only. No Azure hosting. No outreach was sent to this business.</p>
      <p class="demo-note">© <span id="year"></span> concept layout by KNECO. Business names used only for a private mock.</p>
    </div>
  </footer>

  <div class="callbar">
    <a class="btn btn-primary" href="{phone_link(site)}">{esc(cta_label)}</a>
    <a class="btn btn-dark" href="#contact">Contact</a>
  </div>
  <script src="site.js"></script>
</body>
</html>
'''


def theme_css(site: dict) -> str:
    t = site["theme"]
    return f"""/* Brand tokens for {site["slug"]} */
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
}}
"""


SITES_DATA = [
    {
        "slug": "speakes-plumbing",
        "name": "Speake's Plumbing",
        "title": "Speake's Plumbing | Garland & Richardson concept",
        "description": "Concept marketing page for Speake's Plumbing, a local Garland plumber.",
        "city": "Garland, TX",
        "industry": "Residential & commercial plumbing",
        "source": "https://www.speakesplumbing.com/",
        "phone_display": "(972) 271-9144",
        "phone_tel": "+19722719144",
        "phone_placeholder": False,
        "address": "633 N 5th St, Garland, TX 75040",
        "address_placeholder": False,
        "hours": "Free estimates by phone · Emergency service available",
        "eyebrow": "Local · family owned since 1987",
        "headline": "Licensed plumbers for Garland and Richardson.",
        "lede": "Drain cleaning, water heaters, fixture repair, and line replacement from a shop that has served Garland, Plano, and Richardson for decades.",
        "cta_label": "Call (972) 271-9144",
        "secondary_cta": "See services",
        "panel_title": "Call the shop",
        "services_nav": "Services",
        "reviews_nav": "Reviews",
        "services_heading": "Plumbing services",
        "services_intro": "Public homepage services, rewritten for this concept layout.",
        "about_heading": "A neighborhood plumbing shop",
        "about": "Speake's Plumbing, Inc. presents itself as a complete source for residential and commercial plumbing in Garland and nearby cities. The live site notes licensed plumbers on the job and a Master Plumber license number published on their homepage.",
        "why_heading": "What this mock emphasizes",
        "why": "A clear phone estimate, a short service list, and a Garland address — the basics a homeowner needs before they call.",
        "extra_note": "Their public homepage lists Master Plumber Lic #16836. This mock does not add any other credentials.",
        "area_intro": "Areas named on their public site.",
        "areas": ["Garland", "Richardson", "Plano", "Nearby Dallas County"],
        "reviews_heading": "Sample neighbor comments",
        "contact_heading": "Request a phone estimate",
        "contact_intro": "Use the public shop number from their homepage. The form below is demo-only.",
        "form_cta": "Show demo confirmation",
        "kpis": [
            {"value": "1987", "label": "Serving since"},
            {"value": "Licensed", "label": "Plumber on site"},
            {"value": "Free", "label": "Phone estimates"},
            {"value": "Local", "label": "Family owned"},
        ],
        "services": [
            {"title": "Drain & sewer cleaning", "text": "Electric sewer and sink drain cleaning, plus video inspection when a line needs a closer look."},
            {"title": "Water heaters", "text": "Service and replacement for hot water systems in homes and small commercial spaces."},
            {"title": "Gas, water & sewer lines", "text": "Line replacement when leaks or aging pipe need more than a patch."},
            {"title": "Fixtures & disposals", "text": "Faucets, fixtures, and garbage disposal repair or swap-outs."},
            {"title": "Remodel plumbing", "text": "Repair and remodel support for kitchens and baths in the Garland area."},
            {"title": "Emergency help", "text": "Their public site highlights emergency service for urgent leaks and backups."},
        ],
        "reviews": [
            {"quote": "They showed up, explained the leak, and finished without a sales pitch.", "name": "A. Rivera, concept placeholder"},
            {"quote": "Water heater swap was scheduled quickly and the crew stayed tidy.", "name": "J. Nguyen, concept placeholder"},
            {"quote": "Fair price for a drain clean-out. Would call the same shop again.", "name": "M. Ellis, concept placeholder"},
        ],
        "mark": "drop",
        "theme": {
            "bg": "#f3efe8",
            "surface": "#fffdf8",
            "ink": "#1c2430",
            "muted": "#5c6570",
            "brand": "#16324f",
            "brand2": "#c47a3a",
            "accent": "#c47a3a",
            "hero_ink": "#f7f1e8",
            "display": '"Palatino Linotype", Georgia, serif',
            "pattern": "radial-gradient(circle at 20% 20%, #fff 0 2px, transparent 2.5px)",
        },
    },
    {
        "slug": "beyond-lawn-care",
        "name": "Beyond Lawn Care",
        "title": "Beyond Lawn Care | Mesquite landscaping concept",
        "description": "Concept marketing page for Beyond Lawn Care & Landscaping in Mesquite.",
        "city": "Mesquite, TX",
        "industry": "Lawn care & landscaping",
        "source": "https://www.beyondlawncares.com/",
        "phone_display": "(972) 803-7495",
        "phone_tel": "+19728037495",
        "phone_placeholder": False,
        "address": "Mesquite, TX — street not listed on their public homepage",
        "address_placeholder": True,
        "hours": "Mon–Fri 8 AM–5 PM · Sat 9 AM–2 PM · Sun closed",
        "eyebrow": "Mesquite lawns and commercial grounds",
        "headline": "Keep the yard ready so your week stays easier.",
        "lede": "Mowing, landscape maintenance, cleanups, sod, aeration, and commercial groundskeeping for Mesquite, Rowlett, Sunnyvale, and nearby cities.",
        "cta_label": "Call (972) 803-7495",
        "secondary_cta": "Browse services",
        "panel_title": "Ask for a quote",
        "services_nav": "Services",
        "reviews_nav": "Reviews",
        "services_heading": "Outdoor care",
        "services_intro": "Service list taken from their public homepage, rewritten for this mock.",
        "about_heading": "Beyond the weekly cut",
        "about": "Beyond Lawn Care & Landscaping describes itself as a residential and commercial crew focused on year-round upkeep. Primary service cities on their site are Rowlett and Sunnyvale, with more coverage in Garland, Forney, and Dallas.",
        "why_heading": "What this mock emphasizes",
        "why": "A simple estimate path, a readable service grid, and hours a property manager can scan on a phone.",
        "area_intro": "Cities named on their public homepage.",
        "areas": ["Mesquite", "Rowlett", "Sunnyvale", "Garland", "Forney", "Dallas"],
        "reviews_heading": "Sample yard comments",
        "contact_heading": "Request a service quote",
        "contact_intro": "Call the public number from their site. No street address was clearly published there, so the location line is marked placeholder.",
        "form_cta": "Show demo confirmation",
        "kpis": [
            {"value": "Residential", "label": "Weekly lawns"},
            {"value": "Commercial", "label": "Groundskeeping"},
            {"value": "Seasonal", "label": "Cleanups"},
            {"value": "Sod", "label": "New turf installs"},
        ],
        "services": [
            {"title": "Lawn care & mowing", "text": "Routine cuts and basic lawn care so the frontage stays consistent."},
            {"title": "Landscape maintenance", "text": "Beds, edges, and planted areas kept on a regular schedule."},
            {"title": "Property cleanups", "text": "Seasonal debris, leaf drops, and catch-up visits after weather."},
            {"title": "Commercial grounds", "text": "Mowing and landscape maintenance for business properties."},
            {"title": "Aeration & overseeding", "text": "Help for compacted soil and thin, patchy turf."},
            {"title": "Sod installation", "text": "New sod when a lawn needs a reset instead of another overseed."},
        ],
        "reviews": [
            {"quote": "They kept the HOA frontage tidy without us chasing the schedule.", "name": "R. Patel, concept placeholder"},
            {"quote": "Cleanup after the storm was the difference between messy and presentable.", "name": "C. Brooks, concept placeholder"},
            {"quote": "Sod install looked even. Communication was plain and useful.", "name": "L. Ortiz, concept placeholder"},
        ],
        "mark": "leaf",
        "theme": {
            "bg": "#eef5ee",
            "surface": "#fbfff6",
            "ink": "#163022",
            "muted": "#4d6156",
            "brand": "#1b4332",
            "brand2": "#74c69d",
            "accent": "#2d6a4f",
            "hero_ink": "#f3fff6",
            "display": "Georgia, serif",
            "pattern": "radial-gradient(circle at 1px 1px, #fff 1px, transparent 0)",
        },
    },
    {
        "slug": "hughes-mechanical",
        "name": "Hughes Mechanical",
        "title": "Hughes Mechanical | Arlington HVAC concept",
        "description": "Concept marketing page for Hughes Mechanical and Electrical Contractors.",
        "city": "Arlington, TX",
        "industry": "HVAC & electrical contractors",
        "source": "https://www.hughescontractorsllc.com/",
        "phone_display": "(817) 461-9241",
        "phone_tel": "+18174619241",
        "phone_placeholder": False,
        "address": "Arlington, TX — street not listed on their public homepage",
        "address_placeholder": True,
        "hours": "Phones highlighted as available around the clock on their site",
        "eyebrow": "Family owned since 1970",
        "headline": "HVAC and electrical crews who treat the customer like family.",
        "lede": "Hughes Mechanical and Electrical Contractors serves commercial, industrial, and residential jobs from Arlington across DFW and other Texas work.",
        "cta_label": "Call (817) 461-9241",
        "secondary_cta": "View trades",
        "panel_title": "Talk to the office",
        "services_nav": "Services",
        "reviews_nav": "Reviews",
        "services_heading": "Mechanical & electrical",
        "services_intro": "Trades listed on their public homepage.",
        "about_heading": "A long-running Arlington shop",
        "about": "Their site leads with family ownership and a 1970 start date. The public team list includes owner/manager Chris Hughes, HVAC technicians, and electrician Hunter Hughes Jr.",
        "why_heading": "What this mock emphasizes",
        "why": "A 24/7 phone path and a short trade list for facility managers who need HVAC, lighting, or refrigeration help.",
        "area_intro": "Geography described on their public homepage.",
        "areas": ["Arlington", "Dallas–Fort Worth", "Texas job sites"],
        "reviews_heading": "Sample customer notes",
        "contact_heading": "Ask for a quote",
        "contact_intro": "Use the number published on their homepage. Street address is marked placeholder because it was not on that page.",
        "form_cta": "Show demo confirmation",
        "kpis": [
            {"value": "1970", "label": "Family shop since"},
            {"value": "HVAC", "label": "Resi to industrial"},
            {"value": "Electrical", "label": "Commercial lighting"},
            {"value": "24/7", "label": "Phone coverage"},
        ],
        "services": [
            {"title": "Residential HVAC", "text": "Comfort system service for homes in and around Arlington."},
            {"title": "Commercial HVAC", "text": "Equipment support for offices, retail, and other commercial spaces."},
            {"title": "Industrial HVAC", "text": "Heavier mechanical work when a facility needs more than a rooftop swap."},
            {"title": "Commercial electrical", "text": "Electrical contracting for business properties."},
            {"title": "Commercial lighting", "text": "Lighting work listed alongside their electrical services."},
            {"title": "Commercial refrigeration", "text": "Refrigeration support for businesses that depend on cold storage."},
        ],
        "reviews": [
            {"quote": "They treated a rooftop repair like a relationship, not a ticket.", "name": "S. Hale, concept placeholder"},
            {"quote": "Electrician and HVAC tech coordinated instead of bouncing us around.", "name": "D. Kim, concept placeholder"},
            {"quote": "Quoted clearly and showed up when the walk-in started failing.", "name": "P. Grant, concept placeholder"},
        ],
        "mark": "bolt",
        "theme": {
            "bg": "#eef2f6",
            "surface": "#ffffff",
            "ink": "#152033",
            "muted": "#5a6575",
            "brand": "#1d3557",
            "brand2": "#e76f51",
            "accent": "#e76f51",
            "hero_ink": "#f4f7fb",
            "display": '"Segoe UI Semibold", "Segoe UI", sans-serif',
            "pattern": "linear-gradient(90deg, rgba(255,255,255,.18) 1px, transparent 1px), linear-gradient(rgba(255,255,255,.18) 1px, transparent 1px)",
        },
    },
    {
        "slug": "victory-pest-control",
        "name": "Victory Pest Control",
        "title": "Victory Pest Control | Red Oak & DeSoto concept",
        "description": "Concept marketing page for Victory Pest Control LLC in the DFW Metroplex.",
        "city": "Red Oak / DeSoto, TX",
        "industry": "Pest & wildlife control",
        "source": "https://www.victorypestcontrol.com/",
        "phone_display": "(972) 230-5526",
        "phone_tel": "+19722305526",
        "phone_placeholder": False,
        "address": "Red Oak / DeSoto, TX — street not listed on their public homepage",
        "address_placeholder": True,
        "hours": "Available 24 hours a day, per their public site",
        "eyebrow": "Dallas–Fort Worth pest control",
        "headline": "Custom pest plans, then they keep coming back until it is solved.",
        "lede": "Residential and commercial pest control, wildlife work, and bed bug service from a local family-operated company that publishes a one-year warranty and free estimates within 24 hours.",
        "cta_label": "Call (972) 230-5526",
        "secondary_cta": "See programs",
        "panel_title": "Call or text the office",
        "services_nav": "Services",
        "reviews_nav": "Reviews",
        "services_heading": "Pest programs",
        "services_intro": "Service lines named on their public homepage.",
        "about_heading": "A local family operation",
        "about": "Victory Pest Control LLC describes 30+ years in the trade, certified pesticide applicators, and membership in industry associations. They also describe the company as local, minority veteran-owned, and family-operated. This mock uses none of the official seals of any government or VA office.",
        "why_heading": "What this mock emphasizes",
        "why": "After-hours phone access, a warranty promise, and three clear service lanes instead of a long chemical catalog.",
        "extra_note": "No license number was published on the pages reviewed, so none is shown here.",
        "area_intro": "They publicly serve the Dallas–Fort Worth Metroplex, including the Red Oak and DeSoto area named for this test.",
        "areas": ["Red Oak", "DeSoto", "Dallas–Fort Worth Metroplex"],
        "reviews_heading": "Sample service notes",
        "contact_heading": "Request a callback",
        "contact_intro": "Main phone is from their public contact page. Alternate mobile listed there is (214) 543-6357.",
        "form_cta": "Show demo confirmation",
        "kpis": [
            {"value": "30+", "label": "Years in the trade"},
            {"value": "24/7", "label": "Availability"},
            {"value": "1 year", "label": "Warranty language"},
            {"value": "Free", "label": "Estimate in 24 hours"},
        ],
        "services": [
            {"title": "Residential pest control", "text": "Custom plans for homes, with a public promise to return until the problem is handled."},
            {"title": "Commercial pest control", "text": "Service for businesses that need a reliable, documented vendor."},
            {"title": "Nuisance wildlife", "text": "Humane removal language from their site for animals that should not be in the structure."},
            {"title": "Bed bug control", "text": "Targeted bed bug work for homes and commercial properties."},
            {"title": "Termite inspections", "text": "They advertise free termite inspections and paperwork help for mortgage approvals."},
            {"title": "Yearly agreements", "text": "Advance-pay and referral discounts are described on their public homepage."},
        ],
        "reviews": [
            {"quote": "They explained the plan, then actually followed up after the first visit.", "name": "T. Cole, concept placeholder"},
            {"quote": "Wildlife issue was handled without turning the backyard into a mess.", "name": "H. Daniels, concept placeholder"},
            {"quote": "Night call picked up. That mattered more than a brochure.", "name": "K. Sims, concept placeholder"},
        ],
        "mark": "shield",
        "theme": {
            "bg": "#f4f1e6",
            "surface": "#fffdf6",
            "ink": "#24301c",
            "muted": "#5c604c",
            "brand": "#2d4a22",
            "brand2": "#d4a017",
            "accent": "#c39212",
            "hero_ink": "#f8f3df",
            "display": "Georgia, serif",
            "pattern": "repeating-linear-gradient(135deg, rgba(255,255,255,.12) 0 8px, transparent 8px 16px)",
        },
    },
    {
        "slug": "caremaster-building",
        "name": "CareMaster Building",
        "title": "CareMaster Building Services | Dallas janitorial concept",
        "description": "Concept marketing page for CareMaster Building Services in Dallas.",
        "city": "Dallas, TX",
        "industry": "Commercial janitorial & building services",
        "source": "http://www.caremaster.biz/",
        "phone_display": "(214) 366-3366",
        "phone_tel": "+12143663366",
        "phone_placeholder": False,
        "address": "10031 Monroe Drive, Suite 201, Dallas, TX 75229",
        "address_placeholder": False,
        "hours": "Coordinator walk-throughs in business hours · 24-hour customer service for emergencies",
        "eyebrow": "Commercial property care since 1982",
        "headline": "Janitorial care with a coordinator, not just a night crew.",
        "lede": "CareMaster Building Services sells cleaner, safer buildings through inspections, follow-ups, and one vendor for multiple facility needs.",
        "cta_label": "Call (214) 366-3366",
        "secondary_cta": "See building services",
        "panel_title": "Property contacts",
        "services_nav": "Services",
        "reviews_nav": "Reviews",
        "services_heading": "Building services",
        "services_intro": "Core and add-on work listed on their public pages.",
        "about_heading": "Service is the product",
        "about": "Their homepage focuses on three decades in building services, coordinator-level management, daytime inspections, and fewer tenant complaints than the industry average. Email published on their site: customerservice@caremaster.biz.",
        "why_heading": "What this mock emphasizes",
        "why": "A single-invoice vendor story for property managers who are tired of juggling cleaners, floors, and after-hours calls.",
        "area_intro": "Cities named on their public services page.",
        "areas": ["Dallas", "Plano", "Richardson", "Addison", "Arlington", "Mesquite", "Garland", "Frisco", "Carrollton"],
        "reviews_heading": "Sample manager comments",
        "contact_heading": "Talk with CareMaster",
        "contact_intro": "Phone and suite address come from their public site. This form does not email the company.",
        "form_cta": "Show demo confirmation",
        "kpis": [
            {"value": "1982", "label": "In the industry"},
            {"value": "24 hr", "label": "Customer service"},
            {"value": "One vendor", "label": "Many building tasks"},
            {"value": "Daytime", "label": "Walk-throughs"},
        ],
        "services": [
            {"title": "Full janitorial", "text": "Commercial cleaning programs tailored to a building and its tenants."},
            {"title": "Carpet & hard floors", "text": "Low-moisture or extraction carpet work, plus strip and refinish for hard floors."},
            {"title": "Windows & power washing", "text": "Exterior presentation work for glass, sidewalks, and building skin."},
            {"title": "Post-construction", "text": "Make-ready and post-construction cleanup when a space turns over."},
            {"title": "Emergency & event cleaning", "text": "After-hours response plus event support when a property needs extra hands."},
            {"title": "Added facility help", "text": "Their public list also mentions parking lots, marble, temporary labor, and other add-ons on request."},
        ],
        "reviews": [
            {"quote": "The coordinator checked the floors before tenants complained. That is rare.", "name": "N. Alvarez, concept placeholder"},
            {"quote": "One invoice for nights, carpets, and a weekend event. Easier accounting.", "name": "B. Cho, concept placeholder"},
            {"quote": "Emergency water mess was handled without waiting for the next business day.", "name": "I. Freeman, concept placeholder"},
        ],
        "mark": "building",
        "theme": {
            "bg": "#eef3f3",
            "surface": "#ffffff",
            "ink": "#17202a",
            "muted": "#5b6770",
            "brand": "#1a2332",
            "brand2": "#2a9d8f",
            "accent": "#2a9d8f",
            "hero_ink": "#eef8f6",
            "display": '"Segoe UI", system-ui, sans-serif',
            "pattern": "repeating-linear-gradient(90deg, rgba(255,255,255,.08) 0 2px, transparent 2px 18px)",
        },
    },
    {
        "slug": "forum-terrace-church",
        "name": "Forum Terrace Church of Christ",
        "title": "Forum Terrace Church of Christ | Grand Prairie concept",
        "description": "Concept welcome page for Forum Terrace Church of Christ in Grand Prairie.",
        "city": "Grand Prairie, TX",
        "industry": "Congregation welcome site",
        "source": "http://forumterrace.org/",
        "phone_display": "(972) 922-3249",
        "phone_tel": "+19729223249",
        "phone_placeholder": False,
        "address": "2446 Arkansas Lane, Grand Prairie, TX 75052",
        "address_placeholder": False,
        "hours": "Call for this week’s gathering times — Sunday morning times were not listed on the homepage reviewed",
        "eyebrow": "A church family in Grand Prairie",
        "headline": "Welcome. We will open the Bible with you.",
        "lede": "Forum Terrace Church of Christ is a congregation that points visitors to salvation in Jesus Christ and to answers in Scripture — not to any government office.",
        "cta_label": "Call (972) 922-3249",
        "secondary_cta": "See gatherings",
        "panel_title": "Come see us",
        "services_nav": "Gatherings",
        "reviews_nav": "Welcome notes",
        "services_heading": "Scheduled gatherings",
        "services_intro": "Events named on their public homepage. This mock does not invent Sunday morning times they did not publish.",
        "about_heading": "Who we are",
        "about": "They describe themselves as a family of Christians helping people toward an eternal home in Heaven, with questions answered from the Bible. The public contact name on their site is Dan Vess.",
        "why_heading": "What this mock emphasizes",
        "why": "A warm welcome, a street address, and a phone a visitor can actually dial — without looking official or civic.",
        "area_intro": "A Grand Prairie congregation, open to neighbors across nearby cities.",
        "areas": ["Grand Prairie", "Arlington", "Dallas", "Nearby Mid-Cities"],
        "reviews_heading": "Sample visitor notes",
        "contact_heading": "Plan a visit",
        "contact_intro": "Call the number published on their site or use the demo form. Nothing is sent to the congregation.",
        "form_cta": "Show demo confirmation",
        "kpis": [
            {"value": "Bible", "label": "Open-book answers"},
            {"value": "Family", "label": "Congregation life"},
            {"value": "Welcome", "label": "Visitors included"},
            {"value": "Local", "label": "Arkansas Lane"},
        ],
        "services": [
            {"title": "Lord’s Day gatherings", "text": "Weekly worship and teaching. Call for the current Sunday times before you drive."},
            {"title": "Leadership class", "text": "Listed on their site for the first Sunday night of each month."},
            {"title": "Visitor status", "text": "Second Sunday night gathering named on their public calendar."},
            {"title": "Children’s Bible drill", "text": "Third Sunday night activity listed for families."},
            {"title": "Singing night", "text": "Fourth Sunday night, with practice on the Friday or Saturday before."},
            {"title": "Quarterly prayer meeting", "text": "Fifth Sunday night when the calendar includes one."},
        ],
        "reviews": [
            {"quote": "Someone met us at the door and sat with us. That was enough to come back.", "name": "Visitor note, concept placeholder"},
            {"quote": "Classes stayed in the text. No pressure to fill out a civic form.", "name": "Neighbor note, concept placeholder"},
            {"quote": "Bulletin writing was practical. We knew what this Sunday was about.", "name": "Member note, concept placeholder"},
        ],
        "mark": "cross",
        "theme": {
            "bg": "#f6efe6",
            "surface": "#fffaf2",
            "ink": "#3a241f",
            "muted": "#6b5348",
            "brand": "#5c2a2a",
            "brand2": "#e8d5a3",
            "accent": "#8b5a2b",
            "hero_ink": "#f8eedc",
            "display": "Georgia, serif",
            "pattern": "radial-gradient(circle at 50% 0, rgba(255,255,255,.2), transparent 42%)",
        },
    },
    {
        "slug": "bb-complete-auto",
        "name": "B&B Complete Auto",
        "title": "B&B Complete Auto Repair | Garland concept",
        "description": "Concept marketing page for B&B Complete Auto Repair in Garland.",
        "city": "Garland, TX",
        "industry": "Auto repair & maintenance",
        "source": "https://bbcompleteautorepair.com/",
        "phone_display": "(214) 994-6989",
        "phone_tel": "+12149946989",
        "phone_placeholder": False,
        "address": "2206 South Shiloh Road, Garland, TX 75041",
        "address_placeholder": False,
        "hours": "Monday–Saturday 8 AM–6 PM · Sunday closed",
        "eyebrow": "Garland, Richardson, and Dallas drivers",
        "headline": "One shop for diagnostics, repairs, and getting you back on the road.",
        "lede": "B&B Complete Auto Repair lists full-service care for foreign and domestic vehicles, with written estimates and factory-trained technicians.",
        "cta_label": "Call (214) 994-6989",
        "secondary_cta": "See shop services",
        "panel_title": "Book the bay",
        "services_nav": "Services",
        "reviews_nav": "Reviews",
        "services_heading": "Shop services",
        "services_intro": "Work listed on their public site, condensed for a phone-first page.",
        "about_heading": "Honest repairs, plain estimates",
        "about": "Their site stresses fair pricing, computer diagnostics, shuttle and towing help, loaner vehicles, and brand-name parts. Public contact email: ali@bbcompleteautorepair.com.",
        "why_heading": "What this mock emphasizes",
        "why": "A Shiloh Road address, Saturday hours, and a service list that covers the usual ‘check engine’ week.",
        "area_intro": "Cities named on their public homepage.",
        "areas": ["Garland", "Richardson", "Dallas"],
        "reviews_heading": "Sample driver comments",
        "contact_heading": "Schedule an inspection",
        "contact_intro": "Phone, hours, and street address come from their public contact page.",
        "form_cta": "Show demo confirmation",
        "kpis": [
            {"value": "Sat", "label": "Open 8–6"},
            {"value": "All makes", "label": "Foreign & domestic"},
            {"value": "Written", "label": "Estimates"},
            {"value": "Shuttle", "label": "Local ride help"},
        ],
        "services": [
            {"title": "Diagnostics", "text": "Check-engine and computer diagnostics before parts get thrown at the car."},
            {"title": "Brakes, tires & alignment", "text": "Brake work, tire service, rotation, and wheel alignment."},
            {"title": "Engines & transmissions", "text": "Repair and rebuild work when the problem is deeper than a sensor."},
            {"title": "Oil, cooling & batteries", "text": "Maintenance, radiator work, and electrical / battery repairs."},
            {"title": "Body & glass", "text": "Collision, auto body, and auto glass repair or replacement."},
            {"title": "Inspections & warranties", "text": "Preventative maintenance, inspections, and warranty programs listed on their site."},
        ],
        "reviews": [
            {"quote": "They showed me the worn pad instead of just pointing at a total.", "name": "E. Vargas, concept placeholder"},
            {"quote": "Shuttle saved the workday. Car was ready when they said.", "name": "A. Moss, concept placeholder"},
            {"quote": "Domestic truck and a European sedan — both left sorted.", "name": "J. Hale, concept placeholder"},
        ],
        "mark": "wrench",
        "theme": {
            "bg": "#f1eeea",
            "surface": "#fffaf6",
            "ink": "#1b1b1b",
            "muted": "#5c5854",
            "brand": "#1c1c1c",
            "brand2": "#c1121f",
            "accent": "#c1121f",
            "hero_ink": "#f6f1ea",
            "display": '"Segoe UI Semibold", "Segoe UI", sans-serif',
            "pattern": "repeating-linear-gradient(-18deg, rgba(255,255,255,.08) 0 10px, transparent 10px 20px)",
        },
    },
    {
        "slug": "ferraro-dds",
        "name": "Daniel L. Ferraro, D.D.S.",
        "title": "Daniel L. Ferraro, D.D.S. | Grand Prairie dental concept",
        "description": "Concept marketing page for Dr. Daniel L. Ferraro in Grand Prairie.",
        "city": "Grand Prairie, TX",
        "industry": "General dentistry",
        "source": "https://www.grandprairie-arlingtondental.com/",
        "phone_display": "(972) 988-8044",
        "phone_tel": "+19729888044",
        "phone_placeholder": False,
        "address": "2985 S. Highway 360, Suite 210, Grand Prairie, TX 75052",
        "address_placeholder": False,
        "hours": "Monday–Thursday 8:00 AM–5:00 PM · Friday–Sunday closed, per their public office hours",
        "eyebrow": "Grand Prairie & Arlington · 30+ years",
        "headline": "Comfortable, conservative dentistry in a relaxed office.",
        "lede": "Dr. Ferraro’s public site highlights general dentistry, implants, and free consultations from Emerald Square Shopping Center at Hwy 360 and Mayfield.",
        "cta_label": "Call (972) 988-8044",
        "secondary_cta": "See dental care",
        "panel_title": "Call the office",
        "services_nav": "Care",
        "reviews_nav": "Notes",
        "services_heading": "Dental care",
        "services_intro": "Treatments described on their public homepage. Prices mentioned there can change — confirm by phone.",
        "about_heading": "A long-standing neighborhood practice",
        "about": "The practice presents conservative care at a reasonable cost. They note 3M certification for mini-implants and offer free implant consults, second opinions, and consults for patients without dental insurance if you call and ask.",
        "why_heading": "What this mock emphasizes",
        "why": "A map-able suite, weekday hours, and a calm tone instead of a coupon wall.",
        "area_intro": "Communities named on their public homepage.",
        "areas": ["Grand Prairie", "Arlington"],
        "reviews_heading": "Sample patient notes",
        "contact_heading": "Schedule a visit",
        "contact_intro": "Phone and suite come from public listings tied to their practice site. This form does not book an appointment.",
        "form_cta": "Show demo confirmation",
        "kpis": [
            {"value": "30+", "label": "Years of care"},
            {"value": "Hwy 360", "label": "Emerald Square"},
            {"value": "Mon–Thu", "label": "Office days"},
            {"value": "Consults", "label": "Call to ask"},
        ],
        "services": [
            {"title": "Checkups & cleanings", "text": "Routine visits they describe as the path to healthier teeth over a lifetime."},
            {"title": "Fillings, crowns & bridges", "text": "Metal-free crowns and bridges plus everyday restorative work."},
            {"title": "Veneers & whitening", "text": "Cosmetic options listed alongside conservative general dentistry."},
            {"title": "Root canals & extractions", "text": "Same-visit root canal therapy and extractions as published on their site."},
            {"title": "Dentures", "text": "Removable replacement teeth when a fixed option is not the plan."},
            {"title": "Implants", "text": "Mini-implants and conventional implant placement/restoration, with consults by phone."},
        ],
        "reviews": [
            {"quote": "The visit felt unhurried. They explained options without rushing a crown.", "name": "S. Bell, concept placeholder"},
            {"quote": "Easy to find off 360. Front desk booked a second-opinion slot the same week.", "name": "R. Diaz, concept placeholder"},
            {"quote": "Conservative plan, which is what I wanted.", "name": "M. Price, concept placeholder"},
        ],
        "mark": "tooth",
        "theme": {
            "bg": "#eef6f6",
            "surface": "#ffffff",
            "ink": "#16333a",
            "muted": "#547077",
            "brand": "#0d7377",
            "brand2": "#14919b",
            "accent": "#0d7377",
            "hero_ink": "#eef8f8",
            "display": "Georgia, serif",
            "pattern": "radial-gradient(circle at 12% 80%, rgba(255,255,255,.25), transparent 28%), radial-gradient(circle at 88% 20%, rgba(255,255,255,.18), transparent 24%)",
        },
    },
    {
        "slug": "garden-restaurant",
        "name": "Garden Restaurant",
        "title": "Garden Restaurant | Garland dining concept",
        "description": "Concept marketing page for Garden Restaurant in Garland.",
        "city": "Garland, TX",
        "industry": "Chinese restaurant",
        "source": "https://gardenrestaurantgarland.com/",
        "phone_display": "(972) 487-8289",
        "phone_tel": "+19724878289",
        "phone_placeholder": False,
        "address": "3555 W Walnut St, Garland, TX 75042",
        "address_placeholder": False,
        "hours": "Public listings commonly show 10 AM–10 PM daily — call to confirm tonight",
        "eyebrow": "Fresh plates in Garland",
        "headline": "Come in for a family table, or call ahead for pickup.",
        "lede": "Garden Restaurant’s public site describes a warm Garland dining room with takeout, delivery partners, and meals made with care.",
        "cta_label": "Call (972) 487-8289",
        "secondary_cta": "See the table",
        "panel_title": "Order or visit",
        "services_nav": "The table",
        "reviews_nav": "Notes",
        "services_heading": "How people eat here",
        "services_intro": "Offerings described on their public site, without copying a copyrighted menu.",
        "about_heading": "A neighborhood dining room",
        "about": "They invite guests for a quick bite or a meal with family and friends. Takeout can be ordered ahead online or by phone. Contact-free delivery is offered through third-party partners at checkout.",
        "why_heading": "What this mock emphasizes",
        "why": "A Walnut Street address, a tap-to-call number, and dining options a hungry guest can scan in ten seconds.",
        "area_intro": "A Garland restaurant serving nearby neighborhoods.",
        "areas": ["Garland", "Richardson", "Mesquite", "North Dallas"],
        "reviews_heading": "Sample diner notes",
        "contact_heading": "Call the restaurant",
        "contact_intro": "Phone and street address are on their public homepage. Public email listed there: gardenrestaurant@zing.com.",
        "form_cta": "Show demo confirmation",
        "kpis": [
            {"value": "Dine-in", "label": "Family tables"},
            {"value": "Takeout", "label": "Call or order ahead"},
            {"value": "Delivery", "label": "Partner checkout"},
            {"value": "Walnut", "label": "Easy Garland stop"},
        ],
        "services": [
            {"title": "Dine-in", "text": "A welcoming room for weeknights, weekends, and family gatherings."},
            {"title": "Takeout", "text": "Order ahead online or call during regular hours for pickup."},
            {"title": "Delivery", "text": "Third-party delivery, including a contact-free option at checkout."},
            {"title": "Chinese favorites", "text": "A broad menu of cooked-to-order dishes. Ask the restaurant for today’s specials."},
            {"title": "Shareable plates", "text": "Better for a table than a solo desk lunch — come with people if you can."},
            {"title": "Weeknight pickup", "text": "A simple phone path when you want dinner without the dining room."},
        ],
        "reviews": [
            {"quote": "Hot takeout, easy parking, and enough food for leftovers.", "name": "Y. Chen, concept placeholder"},
            {"quote": "We go when the whole family wants one table and no decisions at home.", "name": "The Ramirez family, concept placeholder"},
            {"quote": "Called ahead, walked in, and the bag was waiting.", "name": "G. Stone, concept placeholder"},
        ],
        "mark": "bowl",
        "theme": {
            "bg": "#f7efe8",
            "surface": "#fffaf4",
            "ink": "#3b1c16",
            "muted": "#6e4d42",
            "brand": "#8b1e1e",
            "brand2": "#d4a017",
            "accent": "#c39212",
            "hero_ink": "#fff4e0",
            "display": "Georgia, serif",
            "pattern": "radial-gradient(circle at 30% 20%, rgba(255,220,140,.25), transparent 26%), radial-gradient(circle at 80% 70%, rgba(255,255,255,.12), transparent 22%)",
        },
    },
    {
        "slug": "len-conner-law",
        "name": "Law Office of Len Conner",
        "title": "Law Office of Len Conner | Irving family law concept",
        "description": "Concept marketing page for the Law Office of Len Conner in Irving.",
        "city": "Irving, TX",
        "industry": "Divorce & family law",
        "source": "https://www.lonestarlaw.net/",
        "phone_display": "(972) 445-1500",
        "phone_tel": "+19724451500",
        "phone_placeholder": False,
        "address": "600 John Carpenter Freeway, Ste 238, Irving, TX 75062",
        "address_placeholder": False,
        "hours": "Call to schedule a confidential consultation",
        "eyebrow": "Irving family law",
        "headline": "Clear guidance when the family case is the whole case.",
        "lede": "Len Conner’s public site focuses on divorce and family law, with litigation experience plus settlement, mediation, and collaborative options.",
        "cta_label": "Call (972) 445-1500",
        "secondary_cta": "See practice focus",
        "panel_title": "Office",
        "services_nav": "Practice",
        "reviews_nav": "Notes",
        "services_heading": "Family law focus",
        "services_intro": "Matters described on their public pages. This is not legal advice.",
        "about_heading": "A family-law practice",
        "about": "The firm is in Irving at John Carpenter Freeway and Rochelle Boulevard and lists work across Dallas, Tarrant, Denton, and Collin Counties. Their site states attorneys are fully licensed by the Texas Supreme Court and admitted to the U.S. Federal Courts, Northern District of Texas, and that unless otherwise indicated they are not certified by the Texas Board of Legal Specialization.",
        "why_heading": "What this mock emphasizes",
        "why": "A confidential phone path, a mapped Irving suite, and a tone that stays human without promising outcomes.",
        "extra_note": "Information on this concept page is general only. It does not create an attorney-client relationship.",
        "area_intro": "Communities named on their public contact page.",
        "areas": [
            "Irving",
            "Dallas",
            "Garland",
            "Grand Prairie",
            "Arlington",
            "Plano",
            "Fort Worth",
            "Dallas / Tarrant / Denton / Collin Counties",
        ],
        "reviews_heading": "Sample client notes",
        "contact_heading": "Request a confidential call",
        "contact_intro": "Phone and suite are published on their contact page. Do not send confidential facts through this demo form.",
        "form_cta": "Show demo confirmation",
        "form_note": "Demo only — nothing is sent, stored, or reviewed by an attorney. Do not include confidential case facts.",
        "kpis": [
            {"value": "Family law", "label": "Practice focus"},
            {"value": "Irving", "label": "John Carpenter office"},
            {"value": "DFW", "label": "Surrounding counties"},
            {"value": "Call", "label": "Confidential intake"},
        ],
        "services": [
            {"title": "Divorce", "text": "Guidance through divorce options, including negotiation and litigation when needed."},
            {"title": "Children & support", "text": "Child-related matters and support issues as described in their public materials."},
            {"title": "Mediation", "text": "A path to settle differences without trying every issue in a courtroom."},
            {"title": "Collaborative process", "text": "A structured alternative they list alongside traditional case work."},
            {"title": "Settlement strategy", "text": "Their public tone stresses wise use of time and money, not a fight for its own sake."},
            {"title": "Professional team", "text": "They mention working with financial, counseling, and other specialists when a case needs it."},
        ],
        "reviews": [
            {"quote": "They explained likely paths without pretending the case was simple.", "name": "A. Morgan, concept placeholder"},
            {"quote": "I never felt like the meter mattered more than the children.", "name": "R. Walsh, concept placeholder"},
            {"quote": "Staff returned calls. In a family case, that is the whole job some days.", "name": "C. Bennett, concept placeholder"},
        ],
        "mark": "scale",
        "theme": {
            "bg": "#eef2f6",
            "surface": "#fbfcfe",
            "ink": "#122033",
            "muted": "#5a6573",
            "brand": "#0f2744",
            "brand2": "#c5a572",
            "accent": "#b08948",
            "hero_ink": "#f4efe4",
            "display": "Georgia, serif",
            "pattern": "linear-gradient(180deg, rgba(197,165,114,.16), transparent 32%)",
        },
    },
]


GALLERY = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>KNECO DFW concept gallery</title>
  <meta name="description" content="Ten static marketing concept mocks for a KNECO $500 DFW test.">
  <meta name="robots" content="noindex, nofollow">
  <link rel="stylesheet" href="scaffold/styles.css">
  <link rel="stylesheet" href="gallery.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap header-row">
      <a class="brand" href="#top">
        <span class="mark"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 18V6l8-3 8 3v12l-8 3-8-3zm8-12v12"></path></svg></span>
        <span class="brand-text">
          <strong>KNECO concept gallery</strong>
          <span>$500 DFW test · Matthew Sullivan / KNECOSWD</span>
        </span>
      </a>
    </div>
  </header>
  <main id="main">
    <section class="hero" id="top">
      <div class="wrap">
        <p class="eyebrow">Static HTML only · $0 Azure</p>
        <h1>Ten local-business concept sites.</h1>
        <p class="lede">Open any card, or zip a single folder under <code>sites/</code>. None of these pages is the live business site. No forms were submitted to the companies.</p>
      </div>
    </section>
    <section>
      <div class="wrap">
        <div class="cards gallery-cards">
          {cards}
        </div>
      </div>
    </section>
  </main>
  <footer class="site-footer">
    <div class="wrap">
      <p>Concept demo / not live business sites. Prepared for KNECO $500 DFW concept test.</p>
      <p class="demo-note">GitHub Pages–ready from this repo root. No App Service, custom domains, or paid hosting required.</p>
    </div>
  </footer>
</body>
</html>
'''


def gallery_card(site: dict) -> str:
    return f'''<article class="card">
      <p class="muted">{esc(site["city"])}</p>
      <h3>{esc(site["name"])}</h3>
      <p>{esc(site["industry"])}</p>
      <p><a class="btn btn-dark" href="sites/{esc(site["slug"])}/index.html">Open mock</a></p>
      <p class="note"><code>sites/{esc(site["slug"])}/</code></p>
    </article>'''


def write_sites() -> None:
    SITES.mkdir(exist_ok=True)
    for site in SITES_DATA:
        dest = SITES / site["slug"]
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "index.html").write_text(render(site), encoding="utf-8")
        (dest / "theme.css").write_text(theme_css(site), encoding="utf-8")
        shutil.copyfile(SCAFFOLD / "styles.css", dest / "styles.css")
        shutil.copyfile(SCAFFOLD / "site.js", dest / "site.js")

    cards_html = "\n".join(gallery_card(site) for site in SITES_DATA)
    (ROOT / "index.html").write_text(GALLERY.replace("{cards}", cards_html), encoding="utf-8")
    (ROOT / "sites-data.json").write_text(json.dumps(SITES_DATA, indent=2), encoding="utf-8")
    print(f"Wrote {len(SITES_DATA)} sites")


if __name__ == "__main__":
    write_sites()
