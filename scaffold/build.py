#!/usr/bin/env python3
"""Build 10 sell-as-is DFW business sites from published live-site content."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render import cards, chips, contact_form, esc, page, reviews, theme_css

ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD = Path(__file__).resolve().parent
SITES = ROOT / "sites"


def hero(site: dict, h1: str, lede: str, secondary_href: str, secondary_label: str, panel: str) -> str:
    tel = site["phone_tel"]
    phone = site["phone_display"]
    return f'''    <section class="hero" id="top">
      <div class="wrap hero-grid">
        <div>
          <p class="eyebrow">{esc(site["eyebrow"])}</p>
          <h1>{esc(h1)}</h1>
          <p class="lede">{esc(lede)}</p>
          <div class="actions">
            <a class="btn btn-primary" href="tel:{esc(tel)}">Call {esc(phone)}</a>
            <a class="btn btn-ghost" href="{esc(secondary_href)}">{esc(secondary_label)}</a>
          </div>
        </div>
        <aside class="panel">{panel}</aside>
      </div>
    </section>'''


def page_hero(h1: str, lede: str) -> str:
    return f'''    <section class="page-hero">
      <div class="wrap">
        <h1>{esc(h1)}</h1>
        <p class="lede">{esc(lede)}</p>
      </div>
    </section>'''


def section(sid: str, heading: str, intro: str, inner: str, extra_class: str = "") -> str:
    cls = f' class="{extra_class}"' if extra_class else ""
    return f'''    <section{cls} id="{sid}">
      <div class="wrap">
        <div class="section-head">
          <h2>{esc(heading)}</h2>
          <p>{esc(intro)}</p>
        </div>
        {inner}
      </div>
    </section>'''


def kpis(items: list[tuple[str, str]]) -> str:
    return '<div class="kpis">' + "".join(
        f"<div><strong>{esc(v)}</strong><span>{esc(l)}</span></div>" for v, l in items
    ) + "</div>"


def write_site(site: dict, pages: dict[str, str]) -> None:
    dest = SITES / site["slug"]
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "assets").mkdir(exist_ok=True)
    (dest / "theme.css").write_text(theme_css(site), encoding="utf-8")
    shutil.copyfile(SCAFFOLD / "styles.css", dest / "styles.css")
    shutil.copyfile(SCAFFOLD / "site.js", dest / "site.js")
    for name, html in pages.items():
        (dest / name).write_text(html, encoding="utf-8")


def contact_page(site: dict, extra: str = "") -> str:
    body = f'''{page_hero("Contact", site.get("contact_lede", "Call, email, or send a message."))}
    <section>
      <div class="wrap contact-grid">
        <div class="prose">
          {extra}
          <p><strong>Phone:</strong> <a href="tel:{esc(site["phone_tel"])}">{esc(site["phone_display"])}</a></p>
          {f'<p><strong>Email:</strong> <a href="mailto:{esc(site["email"])}">{esc(site["email"])}</a></p>' if site.get("email") else ""}
          <p><strong>Location:</strong> {esc(site.get("address") or site["city"])}</p>
          {f'<p><strong>Hours:</strong> {esc(site["hours"])}</p>' if site.get("hours") else ""}
        </div>
        {contact_form(site)}
      </div>
    </section>'''
    return page(site, title=f"Contact | {site['name']}", description=f"Contact {site['name']}.", current="contact.html", body=body)


# ---------------------------------------------------------------------------
# 1 Speake's Plumbing
# ---------------------------------------------------------------------------
def speakes() -> dict:
    site = {
        "slug": "speakes-plumbing",
        "name": "Speake's Plumbing, Inc.",
        "tagline": "Garland & Richardson",
        "city": "Garland, TX",
        "logo": "assets/logo.png",
        "body_class": "theme-dark-header",
        "phone_display": "(972) 271-9144",
        "phone_tel": "+19722719144",
        "email": "spi87@icloud.com",
        "address": "633 N 5th St, Garland, TX 75040",
        "hours": "Monday–Friday 7:00 AM–5:00 PM",
        "eyebrow": "Local & family owned since 1987",
        "nav": [
            ("index.html", "Home"),
            ("about.html", "About Us"),
            ("services.html", "Services"),
            ("testimonials.html", "Testimonials"),
            ("contact.html", "Contact"),
        ],
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
        "legal": '© <span id="year"></span> Speake\'s Plumbing, Inc. Master Plumber Lic #16836. Licensed &amp; insured.',
        "footer_extra": "<p>Fax: (972) 278-6610</p><p>grantspeake@verizon.net</p>",
    }
    panel = f'''<strong>Call the shop</strong>
          <p><a href="tel:+19722719144">(972) 271-9144</a></p>
          <p>633 N 5th St, Garland, TX 75040</p>
          <p>Free estimates by phone · Emergency services available</p>
          {kpis([("1987", "Serving since"), ("#16836", "Master plumber"), ("9", "Licensed plumbers"), ("Mon–Fri", "7 AM–5 PM")])}'''
    index = page(site, title="Speake's Plumbing, Inc. | Garland & Richardson, TX", description="Licensed plumbers in Garland and Richardson. Drain cleaning, water heaters, fixtures, and emergency service. Master Plumber Lic #16836.", current="index.html", body=f'''{hero(site, "Local plumbing contractors in Garland & Richardson.", "Speake's Plumbing, Inc. is your complete source for residential and commercial plumbing needs. We have been serving Garland, Plano, and Richardson since 1987.", "services.html", "See services", panel)}
{section("services", "Services we provide", "Published on the Speake's Plumbing homepage.", f'<div class="cards">{cards([
    {"title": "Electric sewer & sink drain cleaning", "text": "High quality sewer and drain cleaning, service, and repair."},
    {"title": "Gas, water & sewer lines replaced", "text": "Line replacement when leaks or aging pipe need more than a patch."},
    {"title": "Water heaters serviced & installed", "text": "Hot water heater repair and installation for gas or electric units."},
    {"title": "Fixtures & fixture repair", "text": "Faucets, fixtures, and fixture replacement."},
    {"title": "Disposals", "text": "Garbage disposal repair, replacement, sales, and parts."},
    {"title": "Sewer & drain video inspection", "text": "Video inspection when a line needs a closer look."},
])}</div>')}
{section("about", "A licensed plumber on every job", "Grant Speake is the founder, president, owner, and master plumber. He started Speake's Plumbing, Inc. in 1987. His father and three brothers are licensed plumbers. He was born and raised in Garland.", f'<div class="chip-row">{chips(["Garland", "Richardson", "Plano", "Master Plumber Lic #16836", "Licensed & insured"])}</div>')}
{section("reviews", "Customer testimonials", "Reviews published on Speake's Plumbing.", f'<div class="cards">{reviews([
    {"quote": "Very fast service after calling them in the AM they arrived in the afternoon. Pretty fair pricing and the gentleman that came was very personable and answered any questions my husband had. Will definitely use them again!", "name": "Pamela J."},
    {"quote": "Speake's replaced two water heaters for me and did a great job. They were fast, friendly and prompt. I'll definitely use them again.", "name": "Michael W."},
    {"quote": "This is a great company. We've used them several times and recommend them to everyone who asks us for a plumber. Very friendly guys, honest and fair prices.", "name": "Brandon G."},
])}</div><p class="note"><a href="testimonials.html">Read more testimonials</a></p>', "reviews")}''')

    about = page(site, title="About Us | Speake's Plumbing, Inc.", description="Grant Speake founded Speake's Plumbing in 1987. Nine licensed plumbers, three master plumbers, eight stocked vans.", current="about.html", body=f'''{page_hero("About Speake's Plumbing, Inc.", "Professional plumbing contractors in Garland, TX.")}
    <section>
      <div class="wrap about-grid">
        <div class="prose">
          <p>Grant Speake is the Founder/President/Owner and Master Plumber. He started Speake's Plumbing, Inc. in 1987. His father and 3 brothers are licensed plumbers. He was born and raised in Garland.</p>
          <h2>Fully insured</h2>
          <p>We have many years of plumbing experience and 8 fully stocked vans. We employ 9 licensed plumbers, of which 3 are master plumbers. We are insured for your protection. We always send a licensed plumber to do the work.</p>
          <p>We keep a history of work done for each customer, which helps for future problems. We have weekly meetings to discuss how best to handle each situation and new products.</p>
          <p>If you have located us through this website, please mention this for our marketing purposes.</p>
          <p>Master Plumber Lic #16836. Fax: (972) 278-6610. Email: <a href="mailto:spi87@icloud.com">spi87@icloud.com</a> or <a href="mailto:grantspeake@verizon.net">grantspeake@verizon.net</a>.</p>
        </div>
        <div class="card">
          <h3>Finance options</h3>
          <p>Finance options are available in Garland, TX. Call (972) 271-9144 to ask about current terms.</p>
        </div>
      </div>
    </section>''')

    services = page(site, title="Plumbing Services | Speake's Plumbing, Inc.", description="Residential and commercial plumbing, water heaters, and products in Garland and Richardson.", current="services.html", body=f'''{page_hero("Residential, commercial, and water heaters", "No matter how big, small, or complicated your problem, our licensed and insured plumbers can fix it.")}
{section("residential", "Residential plumbing", "Clogged drains can be a sign of pipe damage from weather or tree roots. Catch problems early.", f'<div class="cards">{cards([
    {"title": "Bath and kitchen remodeling", "text": "Repair and remodel support for kitchens and baths."},
    {"title": "Drain cleaning, maintenance and repair", "text": "Electric snake service and pipe clearing."},
    {"title": "Garbage disposal repair and replacement", "text": "Disposal service, sales, and parts."},
    {"title": "Kitchen and bath fixture installation", "text": "Fixtures, faucets, tubs, and showers."},
    {"title": "Rooter service & sewer cleanout", "text": "Sewer cleanout, repair, and installation."},
    {"title": "Underground leak and pipe repair", "text": "Water line repair and replacement."},
    {"title": "Water heater repair and replacement", "text": "Gas or electric water heaters and pump installation."},
])}</div>')}
{section("commercial", "Commercial plumbing", "From a drain clog to new sewer lines or a water heating system, Speake's can handle commercial repair. We advise when to keep repairing a system and when it makes sense to replace it.", "<p class=\"prose\">We offer affordable and energy-efficient water heating equipment for business needs. You will always speak to a licensed plumber at 972-271-9144.</p>")}
{section("products", "Products & fixtures", "We stock options from Badger, Bradford White, Kohler, Moen, Rheem, Ruud, and more.", f'<div class="chip-row">{chips(["Backflow preventers", "Bathtubs & showers", "Boilers & water heaters", "Catch basins & traps", "Copper piping", "Faucets", "Flush valves", "Garbage disposals", "Pumps", "PVC & plastic pipe", "Sewer lines", "Sinks", "Tankless water heaters", "Thermostats", "Toilets", "Water mains"])}</div>')}''')

    testi = page(site, title="Testimonials | Speake's Plumbing, Inc.", description="Customer testimonials published by Speake's Plumbing in Garland, TX.", current="testimonials.html", body=f'''{page_hero("Plumbing company testimonials in Garland, TX", "Reviews published on the Speake's testimonials page.")}
{section("list", "What customers wrote", "Quoted as published. Template product slogans from the homepage slider are not included.", f'<div class="cards two">{reviews([
    {"quote": "Very fast service after calling them in the AM they arrived in the afternoon. Pretty fair pricing and the gentleman that came was very personable and answered any questions my husband had. Will definitely use them again!", "name": "Pamela J."},
    {"quote": "Speake's replaced the faucets in a old shower (circa 1955), unclogged the drain, replaced the sink hardware and the shower head in another bathroom. They even had to removed some of the vintage tile to install the new shower faucet. They were extremely careful and did a great job for an extremely reasonable price. Excellent, excellent experience!! I had requested an estimate from another plumber who told me (without looking at the house) that the job would take 3 times longer and cost 4 times as much as Speake's. I'm so glad I used Speake's. Definitely will recommend to all my friends.", "name": "Lyn B."},
    {"quote": "I was delighted this morning to hear a strong rainstorm with water pouring on my kitchen window. BUT it was not rain. It was a busted water spigot. I immediately found Speake's Plumbing and read the outstanding reviews, so I called Speake's. Plumbing genius Garlan made a replacement with a special kit he had in his truck. The whole issue was resolved in less than 20 minutes after his arrival and it only cost $189. Garlan was personable, professional and knew his trade. I would recommend Speake's over any plumbing company in the Metroplex.", "name": "Rex M."},
    {"quote": "Once again you guys have proven to be the very best plumbing company we've ever used! Late afternoon yesterday our hot water tank sprang a leak and soaked our hall carpet. Rusty was great to tell us exactly what we needed to do and he called another company out (Dry Force) to soak up the water. Kasey from Speaks was out first thing this morning to replace our tank. Very happy with them!", "name": "Debora G."},
    {"quote": "Very quick service. Had to power auger drain lines. Finally broke through whatever was backing up the sewage. We've used Speake's for a long time and they are still our go-to. After unclogging, they even went the extra step to add recommendations to the service bill.", "name": "Ashley S."},
    {"quote": "We called speakes to snake the main line on the roof. Due to a break down in communication they just snaked the bath tub. I call them and tell them of the error. And they came back out. Snaked the roof. Very happy with the service. Honest people and I appreciate that.", "name": "Ashley D."},
    {"quote": "Hot water heater went out Sunday night ... Speake's came Monday Morning! I called in soon after they opened at 7am. They were very polite, explained what they needed to do and were very clean. He showed me how to turn on the water heater and what to do if we ever needed to turn it off.", "name": "Janet U."},
    {"quote": "Very friendly and prompt plumbing service. Used to repair our hot water heater twice and they had a plumber at our house within a couple hours of our phone call both times. Rates are reasonable. Plumber polite, knowledgeable and thorough.", "name": "Christy H."},
    {"quote": "We only call Speakes Plumbing for our house and my mother's house. They have taken care of water heaters, foundation leaks, gas lines, and water lines. Lucas, Casey, or Lee are always friendly and professional. Highly recommend them!", "name": "Patricia W."},
    {"quote": "My brother hooked me up with them after I've been dealing with a leaky tub faucet for almost two years. My service technician Lee was fast and efficient. I would recommend them to anyone.", "name": "Martin W."},
])}</div>')}''')

    contact = contact_page(site, "<p>Call us for emergency plumbing repairs in Garland, TX. Hours of operation: Mon–Fri 7:00 AM–5:00 PM. Payment options are available — ask when you call.</p>")
    write_site(site, {"index.html": index, "about.html": about, "services.html": services, "testimonials.html": testi, "contact.html": contact})
    return site


# ---------------------------------------------------------------------------
# 2 Beyond Lawn Care
# ---------------------------------------------------------------------------
def beyond() -> dict:
    site = {
        "slug": "beyond-lawn-care",
        "name": "Beyond Lawn Care & Landscaping",
        "tagline": "Mesquite, TX",
        "city": "Mesquite, TX",
        "logo": "assets/logo.png",
        "logo_class": "logo wide",
        "phone_display": "(972) 803-7495",
        "phone_tel": "+19728037495",
        "email": "Info@beyondlawncares.com",
        "address": "Mesquite, TX 75149",
        "hours": "Mon–Fri 8 AM–5 PM · Sat 9 AM–2 PM · Sun closed",
        "eyebrow": "Mesquite, TX & surrounding areas",
        "nav": [
            ("index.html", "Home"),
            ("services.html", "Services"),
            ("packages.html", "Packages"),
            ("contact.html", "Contact"),
        ],
        "theme": {
            "bg": "#eef5ee",
            "surface": "#fbfff6",
            "ink": "#163022",
            "muted": "#4d6156",
            "brand": "#1b4332",
            "brand2": "#e85d04",
            "accent": "#e85d04",
            "hero_ink": "#f3fff6",
            "display": "Georgia, serif",
            "pattern": "radial-gradient(circle at 1px 1px, #fff 1px, transparent 0)",
        },
        "legal": "© <span id=\"year\"></span> Beyond Lawn Care &amp; Landscaping.",
    }
    panel = f'''<strong>Get an estimate</strong>
          <p><a href="tel:+19728037495">(972) 803-7495</a></p>
          <p><a href="mailto:Info@beyondlawncares.com">Info@beyondlawncares.com</a></p>
          <p>Mon–Fri 8 AM–5 PM · Sat 9 AM–2 PM · Sun closed</p>
          {kpis([("Weekly", "Mowing packages"), ("Commercial", "Groundskeeping"), ("Sod", "New installs"), ("Mesquite", "Home base")])}'''
    index = page(site, title="Lawn Care & Landscape Maintenance | Mesquite, TX", description="Professional lawn care and landscaping in Mesquite, Rowlett, Sunnyvale, Garland, Forney, Dallas, and Balch Springs.", current="index.html", body=f'''{hero(site, "Professional lawn care & landscaping in Mesquite, TX.", "We offer residential and commercial lawn care in Mesquite and surrounding areas — mowing, landscape maintenance, cleanups, sod, aeration, and commercial groundskeeping.", "packages.html", "View packages", panel)}
{section("about", "About Beyond Lawn Care & Landscaping", "We're committed to delivering top-tier residential and commercial lawn care in Mesquite, TX. We proudly serve Rowlett and Sunnyvale as our primary service areas, with additional coverage in Garland, Forney, and Dallas.", "<p>From routine lawn mowing and seasonal yard maintenance to landscaping, sod installation, grass seeding, weed control, property cleanups, and full-scale commercial groundskeeping, we handle every aspect of your outdoor upkeep. Our goal is to keep your property in excellent shape year-round, making your day-to-day a little easier.</p>")}
{section("services", "Our services", "Service lines published on the Beyond Lawn Care site.", f'<div class="cards">{cards([
    {"title": "Lawn care & mowing", "text": "Routine residential lawn mowing and year-round lawn maintenance in Mesquite."},
    {"title": "Landscape maintenance", "text": "Keeping residential landscapes well maintained."},
    {"title": "Property clean ups", "text": "Autumn leaves and other seasonal debris."},
    {"title": "Commercial lawn care", "text": "Mowing, edging, and debris cleanup for offices, retail, HOAs, and other commercial sites."},
    {"title": "Commercial landscape maintenance", "text": "Professional landscaping upkeep for business properties."},
    {"title": "Seasonal flower installations", "text": "Seasonal color for beds and frontage."},
    {"title": "Bush & hedge trimming", "text": "Trimming and landscape pruning."},
    {"title": "Mulch installations", "text": "Mulch installed after an on-site look at beds and plants."},
    {"title": "Core aeration", "text": "Aeration so nutrients and water reach grass roots."},
    {"title": "Overseeding", "text": "Help for patching and bare areas."},
    {"title": "Sod installation", "text": "New sod for a green lawn reset."},
    {"title": "Salt application", "text": "Winter salt application as listed on the public service menu."},
    {"title": "Sprinkler inspection & maintenance", "text": "Sprinkler system inspection and maintenance."},
    {"title": "Leaf cleanup", "text": "Seasonal leaf cleanup."},
])}</div>')}
{section("area", "Service area", "Cities named on the public site.", f'<div class="chip-row">{chips(["Mesquite, TX", "Sunnyvale, TX", "Garland, TX", "Forney, TX", "Rowlett, TX", "Balch Springs, TX", "Dallas"])}</div>')}''')

    services = page(site, title="Lawn Care Services | Beyond Lawn Care", description="Residential and commercial mowing, landscape maintenance, and cleanups in Mesquite, TX.", current="services.html", body=f'''{page_hero("Lawn care & mowing in Mesquite, TX", "When it comes to routine lawn services, Beyond Lawn Care & Landscaping is your trusted source for residential lawn mowing throughout Mesquite.")}
    <section>
      <div class="wrap prose">
        <p>We know you are busy, and keeping up with your property can be very time-consuming. We make it a priority to provide professional mowing and year-round lawn maintenance so you can enjoy your outdoor space without the work involved to maintain it. Contact us for a lawn care quote in Sunnyvale, Rowlett, Garland, Dallas, and Forney.</p>
        <h2>Commercial lawn care</h2>
        <p>Beyond Lawn Care & Landscaping provides commercial grass mowing and year-round lawn maintenance. Our team handles routine mowing, edging, and debris cleanup to ensure your business exterior stays neat and professional. We work with offices, retail spaces, HOAs, and other commercial sites. Request a free estimate to get started in Mesquite, Rowlett, Sunnyvale, Garland, Dallas and Forney.</p>
      </div>
    </section>''')

    packages = page(site, title="Lawn Care Packages | Beyond Lawn Care", description="Weekly, biweekly, tall grass, and recurring lawn care packages in Mesquite, TX.", current="packages.html", body=f'''{page_hero("Lawn care packages", "Get a quote: send photos to 972-803-7495 or use the estimate form. Include your name and address if submitting by phone.")}
{section("weekly", "Weekly lawn care package", "Ideal for customers who want a pristine lawn with consistent maintenance.", '''<div class="card prose">
          <p><strong>What's included:</strong> Weekly mowing and edging. Trimming around driveways, sidewalks, and flower beds. Grass clippings mulched as standard. Bagging available for an additional charge (half the standard service fee, added to the listed price). Basic debris removal (leaves, twigs, etc.). Quick inspection for pests or lawn health issues.</p>
          <ul class="hours-list">
            <li><span>Regular lawn</span><span class="price">$40–$50 / week</span></li>
            <li><span>Medium-large yard</span><span class="price">$60–$70 / week</span></li>
            <li><span>Large yard</span><span class="price">$90–$130 / week</span></li>
          </ul>
        </div>''')}
{section("biweekly", "Biweekly lawn care package", "Maintenance without the weekly commitment. Perfect for moderately growing lawns.", '''<div class="card prose">
          <p><strong>What's included:</strong> Biweekly mowing and edging, trimming around driveways, sidewalks, and flower beds, basic debris removal. Clippings mulched as standard; bagging extra as above.</p>
          <ul class="hours-list">
            <li><span>Regular lawn</span><span class="price">$60–$70 / visit</span></li>
            <li><span>Medium-large yard</span><span class="price">$90–$100 / visit</span></li>
            <li><span>Large yard</span><span class="price">$135–$200 / visit</span></li>
          </ul>
        </div>''')}
{section("addons", "Custom add-ons & other packages", "Initial mowing is the biweekly rate times a height multiplier (1x normal, 2x slightly tall, 3x very tall). After the first cut, standard recurring rates apply.", f'<div class="cards">{cards([
    {"title": "Fertilization", "text": "$50–$250 per application, depending on yard size."},
    {"title": "Aeration and overseeding", "text": "$150–$350 per session."},
    {"title": "Spring/fall clean-up", "text": "$150–$1,000 per session."},
    {"title": "Tall grass mowing", "text": "Published as a best-value package for overgrown lawns. Ask for current pricing."},
    {"title": "Recurring maintenance plan", "text": "Mowing plus landscaping bed trimming every 4–6 weeks. Pricing after the first mow or via photo submission."},
    {"title": "Landscaping & bush trimming", "text": "Deweeding and flower-bed pricing during the initial mow or from photos. Mulch, rock, and plant installs are quoted in person."},
])}</div>')}''')

    contact = contact_page(site, "<p>Complete the estimate form and a representative will be with you. No street address is published on the public site; service is based in Mesquite (75149) and the cities listed on the homepage.</p><p>The live site embeds a Google reviews widget. Those comments load in the browser and were not copied here.</p>")
    write_site(site, {"index.html": index, "services.html": services, "packages.html": packages, "contact.html": contact})
    return site


# ---------------------------------------------------------------------------
# 3 Hughes Mechanical
# ---------------------------------------------------------------------------
def hughes() -> dict:
    site = {
        "slug": "hughes-mechanical",
        "name": "Hughes Mechanical and Electrical Contractors",
        "tagline": "Arlington, TX since 1970",
        "city": "Arlington, TX",
        "logo": "assets/wordmark-header.png",
        "logo_class": "logo wide",
        "body_class": "theme-dark-header",
        "phone_display": "(817) 461-9241",
        "phone_tel": "+18174619241",
        "email": "sales@hughes-mech-elect.com",
        "address": "423 Dodson Lake Drive, Arlington, TX 76012",
        "hours": "Phones online 24/7 — a representative is available to take your call",
        "eyebrow": "Family owned. Family operated. Family oriented.",
        "nav": [
            ("index.html", "Home"),
            ("index.html#services", "Services"),
            ("index.html#about", "About"),
            ("contact.html", "Contact"),
        ],
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
        "legal": "© <span id=\"year\"></span> Hughes Mechanical and Electrical Contractors.",
    }
    panel = f'''<img class="logo" src="assets/logo.png" alt="Hughes Mechanical logo">
          <strong>Have questions or need a quote?</strong>
          <p><a href="tel:+18174619241">(817) 461-9241</a></p>
          <p><a href="mailto:sales@hughes-mech-elect.com">sales@hughes-mech-elect.com</a></p>
          <p>423 Dodson Lake Drive<br>Arlington, TX 76012</p>
          {kpis([("1970", "Family shop since"), ("24/7", "Phones online"), ("HVAC", "Resi to industrial"), ("Electrical", "Commercial lighting")])}'''
    index = page(site, title="Hughes Mechanical and Electrical Contractors | Arlington, TX", description="Family-owned HVAC and electrical contractors since 1970. 423 Dodson Lake Drive, Arlington. Call (817) 461-9241.", current="index.html", body=f'''{hero(site, "Your local family owned and operated HVAC and electrical contractors since 1970.", "Since 1970, Hughes Mechanical and Electrical Contractors has provided HVAC and electrical services to customers throughout the Dallas–Fort Worth Metroplex and areas spanning Texas. To us, our customers are family — a core value our company was founded and continues to operate upon.", "contact.html", "Get in touch", panel)}
{section("services", "Our services", "Interested in any of these services or additional ones not listed? Get in touch today.", f'<div class="cards">{cards([
    {"title": "Commercial HVAC", "text": "Equipment support for commercial properties across DFW and Texas job sites."},
    {"title": "Industrial HVAC", "text": "Heavier mechanical work for industrial facilities."},
    {"title": "Residential HVAC", "text": "Comfort system service for homes."},
    {"title": "Commercial electrical", "text": "Electrical contracting for business properties."},
    {"title": "Commercial lighting", "text": "Lighting work listed alongside electrical services."},
    {"title": "Commercial refrigeration", "text": "Refrigeration support for businesses that depend on cold storage."},
])}</div>')}
{section("about", "About Hughes", "Family owned. Family operated. Family oriented.", '''<div class="prose">
          <p>Our phones are online 24/7 and a representative is always readily available to take your call.</p>
          <p>Contact us today to experience it for yourself.</p>
        </div>''')}
{section("team", "Our team", "Names and roles published on the Hughes homepage.", f'<div class="cards">{cards([
    {"title": "Chris Hughes", "text": "Owner / Manager"},
    {"title": "Tony LaQuey", "text": "HVAC Technician"},
    {"title": "Jeff Johnson", "text": "HVAC Technician"},
    {"title": "Jordan Johnson", "text": "HVAC Technician"},
    {"title": "Hunter Hughes Jr.", "text": "Electrician"},
])}</div>')}''')
    contact = contact_page(site, "<p>Call (817) 461-9241 or email sales@hughes-mech-elect.com. The office is at 423 Dodson Lake Drive, Arlington, TX 76012.</p>")
    write_site(site, {"index.html": index, "contact.html": contact})
    return site


# ---------------------------------------------------------------------------
# 4 Victory Pest Control
# ---------------------------------------------------------------------------
def victory() -> dict:
    site = {
        "slug": "victory-pest-control",
        "name": "Victory Pest Control LLC",
        "tagline": "Dallas–Fort Worth Metroplex",
        "city": "Dallas–Fort Worth, TX",
        "logo": "assets/logo.jpg",
        "logo_class": "logo wide",
        "phone_display": "(972) 230-5526",
        "phone_tel": "+19722305526",
        "address": "234 Paradise Way, Red Oak, TX 75154",
        "hours": "Available 24 hours a day",
        "eyebrow": "Dallas–Fort Worth pest control",
        "contact_lede": "Call or send a message. Victory does not publish an email address.",
        "form_status": "Thank you. This page does not send messages automatically — please call (972) 230-5526 or (214) 543-6357 so the office receives your request.",
        "nav": [
            ("index.html", "Home"),
            ("services.html", "Services"),
            ("specials.html", "Specials"),
            ("about.html", "About"),
            ("reviews.html", "Reviews"),
            ("contact.html", "Contact"),
        ],
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
        "legal": "© <span id=\"year\"></span> Victory Pest Control LLC. Member TPCA and NPMA.",
        "footer_extra": "<p>Mobile: (214) 543-6357</p>",
    }
    panel = f'''<strong>Call or text</strong>
          <p><a href="tel:+19722305526">(972) 230-5526</a> · Mobile <a href="tel:+12145436357">(214) 543-6357</a></p>
          <p>234 Paradise Way, Red Oak, TX 75154</p>
          <p>Available 24 hours a day</p>
          {kpis([("John Gaines", "Owner"), ("2007", "Year established"), ("24/7", "Availability"), ("Red Oak", "Office")])}'''
    index = page(site, title="Victory Pest Control | Dallas–Fort Worth Metroplex", description="Residential and commercial pest control, wildlife, and bed bugs. Available 24 hours. Call or text (972) 230-5526.", current="index.html", body=f'''{hero(site, "Dallas–Fort Worth pest control.", "Victory Pest Control LLC is a premier pest control company serving the Dallas–Fort Worth Metroplex. With over 30 years of experience, we provide comprehensive solutions to residential and commercial customers.", "services.html", "See services", panel)}
{section("about", "Your trusted partner in pest management", "Our team is composed of certified pesticide applicators who design custom pest control plans. We are licensed and insured, with a one-year warranty and a promise to keep coming back until the problem is solved.", '''<div class="prose">
          <p>We offer free inspections, a 10% discount for yearly advance payments, and a referral program that rewards you with a 10% discount when a family member or friend signs up for our yearly agreement.</p>
          <p>Worried about termites? We provide free termite inspections and the necessary paperwork for mortgage approvals. Victory Pest Control is a local, minority veteran-owned, family-operated business. Owner John Gaines has been in the pest control business for over 30 years.</p>
        </div>''')}
{section("services", "Services", "Published service lines.", f'<div class="cards">{cards([
    {"title": "Residential & commercial pest control", "text": "Custom plans for homes and businesses, from flying insects to stored-product pests."},
    {"title": "Nuisance wildlife control", "text": "Humane small-animal trapping and wildlife removal."},
    {"title": "Bed bug control", "text": "Identification, elimination, and follow-up plans for homes and commercial properties."},
    {"title": "Termite inspections", "text": "Free termite inspections and mortgage paperwork."},
    {"title": "Integrated pest management", "text": "IPM inspections and reporting to AIB, ASI, FDA, and USDA standards."},
    {"title": "Specials", "text": "10% off yearly advance pay, 5% off when you schedule online, 10% referral credit, mosquito specials, and free termite inspections."},
])}</div>')}''')

    services = page(site, title="Pest Control Services | Victory Pest Control", description="Residential, commercial, wildlife, and bed bug services in DFW.", current="services.html", body=f'''{page_hero("Residential and commercial pest control", "Services range from flying insect control to small animal trapping. Established 2007.")}
{section("list", "Complete pest control services", "We're here to relieve your home and office of pests.", f'<div class="cards">{cards([
    {"title": "Rodent control and exclusion", "text": "Rodent work for homes and commercial accounts."},
    {"title": "Stored product pest control", "text": "Elimination of stored-product pests."},
    {"title": "Bird control", "text": "Bird control solutions."},
    {"title": "Integrated pest management", "text": "IPM inspections and reporting."},
    {"title": "Trailer and railcar fumigations", "text": "Fumigation work as published on the service list."},
    {"title": "Flying insect control", "text": "Flying insect programs."},
    {"title": "Small animal trapping", "text": "Nuisance wildlife and small-animal trapping."},
    {"title": "Bed bug control", "text": "Custom plans from certified pesticide applicators."},
])}</div>')}
{section("faq", "FAQs", "Published on the Victory FAQs page.", f'<div class="cards">{cards([
    {"title": "How long does it take for the pest treatment to become effective?", "text": "It varies depending on the pest or the type of treatment."},
    {"title": "Do you offer any natural or eco-friendly pest control options?", "text": "Yes! All of our treatments are eco-friendly."},
    {"title": "How often should I have my property treated for pests?", "text": "The state recommends that your property be treated for pests every quarter."},
])}</div>')}''')

    specials = page(site, title="Specials | Victory Pest Control", description="Published pest control specials from victorypestcontrol.com.", current="specials.html", body=f'''{page_hero("Special offers", "From the live Specials page. Call to confirm what is current.")}
{section("list", "A variety of specials to choose from", "Exceptional pest control services at competitive prices.", f'<div class="cards">{cards([
    {"title": "Yearly advance pay", "text": "Save 10% when you pay for a year in advance."},
    {"title": "Book online", "text": "Get 5% off when you schedule an appointment online."},
    {"title": "Referral", "text": "Refer a family member or friend and get 10% off when they sign up for the yearly agreement."},
    {"title": "Mosquito control special", "text": "Mosquito control special as listed on the live specials page."},
    {"title": "Free termite inspections", "text": "Free termite inspections."},
])}</div>')}''')

    about = page(site, title="About | Victory Pest Control", description="John Gaines, owner. Local, minority veteran-owned, family-operated pest control since 2007.", current="about.html", body=f'''{page_hero("Make your space pest-free", "Our owner, John Gaines, has been in the pest control business for over 30 years.")}
    <section>
      <div class="wrap prose">
        <p>We are proud of the work we do here at Victory Pest Control LLC and the numerous challenges that have come our way, which we have attacked with a smile and a work ethic that has gained us an excellent reputation and a strong base of satisfied customers.</p>
        <p>Our goal is simple: to bring you a cleaner, safer place to live, work, and play by offering an efficient, affordable pest control service to the Dallas–Fort Worth Metroplex.</p>
        <p>We are regulated by the Texas Department of Agriculture with continued education through the Structural Pest Control Services program. Victory Pest Control offers a unique SOS program: Solutions, Options, and Services. We take a customized approach to every residential, educational, governmental, and commercial account.</p>
        <p>Associations: TPCA (Texas Pest Control Association) and NPMA (National Pest Control Management Association). Year established: 2007. Payments: American Express, Cash, Check, Discover, MasterCard, Visa, Zelle, Invoice. Languages: English. Identifies as veteran-owned.</p>
      </div>
    </section>''')

    revs = page(site, title="Reviews | Victory Pest Control", description="Customer comments published on Victory Pest Control service pages.", current="reviews.html", body=f'''{page_hero("What customers are saying", "Comments published on Victory service pages. The dedicated reviews page on the live site does not list additional quotes.")}
{section("list", "Published reviews", "Quoted as they appear on the live site.", f'<div class="cards two">{reviews([
    {"quote": "I have never used a more friendly or effective pest control company. Ken is absolutely fantastic! I will never use anyone other than this company again!", "name": "Taylor Akin", "source": "Google"},
    {"quote": "Every person on staff here is amazing! They take such good care of their customers! Like family!", "name": "Michelle Owens", "source": "Facebook"},
    {"quote": "I recommend Victory Pest Control because I can guarantee they will fix the problem and take care of you. Not only that they follow up to make sure the problem is or did not persist. Definitely a business I can trust.", "name": "Camille Henderson", "source": "Facebook"},
])}</div>')}''')

    contact = contact_page(site, "<p>Owner John Gaines. Main: (972) 230-5526. Mobile: (214) 543-6357. 234 Paradise Way, Red Oak, TX 75154. Available 24 hours a day. No public email is listed. Payment: American Express, cash, check, Discover, MasterCard, Visa, Zelle, invoice.</p>")
    write_site(site, {"index.html": index, "services.html": services, "specials.html": specials, "about.html": about, "reviews.html": revs, "contact.html": contact})
    return site


# ---------------------------------------------------------------------------
# 5 CareMaster
# ---------------------------------------------------------------------------
def caremaster() -> dict:
    site = {
        "slug": "caremaster-building",
        "name": "CareMaster Building Services",
        "tagline": "Dallas / Fort Worth since 1982",
        "city": "Dallas / Fort Worth, TX",
        "logo": "assets/logo.jpg",
        "logo_class": "logo wide",
        "phone_display": "(469) 233-3366",
        "phone_tel": "+14692333366",
        "email": "customerservice@caremaster.biz",
        "address": "PO Box 29303, Dallas, TX 75229",
        "eyebrow": "Commercial janitorial care since 1982",
        "nav": [
            ("index.html", "Home"),
            ("about.html", "About Us"),
            ("services.html", "Services"),
            ("commitment.html", "Our Commitment"),
            ("contact.html", "Contact"),
        ],
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
        "legal": "© <span id=\"year\"></span> CareMaster Building Services.",
    }
    panel = f'''<strong>Talk with CareMaster</strong>
          <p><a href="tel:+14692333366">(469) 233-3366</a></p>
          <p><a href="mailto:customerservice@caremaster.biz">customerservice@caremaster.biz</a></p>
          <p>PO Box 29303, Dallas, TX 75229</p>
          {kpis([("1982", "In the industry"), ("John Lee", "President"), ("IICRC", "Carpet certified"), ("DFW", "Metroplex")])}'''
    index = page(site, title="CareMaster Building Services | Dallas Commercial Janitorial", description="Quality janitorial care for commercial property since 1982. Call (469) 233-3366.", current="index.html", body=f'''{hero(site, "Providing quality janitorial care for the commercial property industry since 1982.", "At CareMaster, service is our business. Our goal is to provide unsurpassed janitorial care through exceptional customer service, attention to detail, and competitive pricing.", "services.html", "See services", panel)}
{section("about", "Service is our business", "In three decades of experience we have learned to be flexible, creative, and committed from start to finish.", '''<div class="prose">
          <p>Our “coordinator” level of management provides an added benefit to our rigorous quality standards. Timely walk-throughs, inspections, and follow-ups are conducted during regular business hours. We also offer twenty-four hour customer service to guarantee a timely response to emergencies or challenges. Our commitment has resulted in far fewer tenant complaints than the industry average.</p>
          <p>We tailor offerings to the special needs of your building, facility, and tenants. Our integrated approach to cleaner, safer, and healthier environments enables the highest level of quality and service.</p>
        </div>''')}''')

    about = page(site, title="About Us | CareMaster Building Services", description="Founded from Richard Lee's vision; led by President John Lee since 1997.", current="about.html", body=f'''{page_hero("About CareMaster", "Commercial cleaning and building maintenance in the Dallas/Fort Worth Metroplex since 1982.")}
    <section>
      <div class="wrap prose">
        <p>In the early 1980s, Richard Lee, President John Lee’s brother, acted upon his desire to create viable career opportunities for fellow Korean-Americans. CareMaster Building Services evolved from this vision into a company offering superior quality, affordability and professionalism in janitorial services.</p>
        <p>Since taking over the business in 1997, John has successfully implemented many new concepts and strategies. His dedication is evident through his emphasis on personal attention to the buildings as well as building management. John is committed to building long-term customer relationships and maintaining superior customer service standards.</p>
        <h2>Mission</h2>
        <p>We strive to deliver quality janitorial care to the commercial property industry. We believe in offering a customized approach to a wide variety of customers while remaining 100% accountable to our clients and 100% committed to top-notch service. At CareMaster Building Services, you are our business.</p>
        <h2>Affiliations</h2>
        <div class="chip-row">{chips(["BOMA Dallas", "DFW Minority Business Development Council", "IFMA DFW", "North Central Texas Regional Certification Agency", "State of Texas — HUB", "The Rotary Club of Dallas", "Corporate Recycling Council"])}</div>
      </div>
    </section>''')

    services = page(site, title="Services | CareMaster Building Services", description="Full-service janitorial and maintenance contractor.", current="services.html", body=f'''{page_hero("Building services", "CareMaster Building Services is a full-service contractor for all your janitorial and maintenance needs.")}
{section("list", "Our services include", "Coordinator-level management on every program.", f'<div class="cards">{cards([
    {"title": "Full janitorial and commercial cleaning", "text": "Programs tailored to the building and its tenants."},
    {"title": "Carpet cleaning", "text": "Low moisture and full extraction."},
    {"title": "Hard floor stripping and refinishing", "text": "Hard-surface floor care."},
    {"title": "Move-in and make-ready cleaning", "text": "Turnover cleaning when a space changes hands."},
    {"title": "Post construction clean up and make-ready", "text": "After construction or renovation."},
    {"title": "Event cleaning", "text": "Extra hands when a property hosts an event."},
])}</div>')}''')

    commit = page(site, title="Our Commitment | CareMaster Building Services", description="Quality control, environmental responsibility, and 24-hour customer service.", current="commitment.html", body=f'''{page_hero("Our commitment", "Quality control is a team effort.")}
    <section>
      <div class="wrap prose">
        <p>After a background investigation, we provide all employees with intensive training and supervisory support. On-site orientation and training are conducted for every customer site, and we use a “team cleaning” method.</p>
        <p>We encourage and support LEED and Green Building (LEED-EB) programs. We purchase supplies and equipment that are safe for employees, customers, and the environment. Recycling and hazardous material disposal are part of regular training.</p>
        <p>You will always recognize our employees. All CareMaster employees have a neat, clean uniform appearance. We train employees to interact favorably with the people who use the building daily.</p>
        <p>Only experienced, competent laborers are offered employment. All potential employees complete a background investigation and reference check. We are IICRC Certified for Carpet Cleaning and Commercial CPT Maintenance.</p>
        <p>Mailing address: PO Box 29303, Dallas, TX 75229. Call (469) 233-3366 or email customerservice@caremaster.biz. Street hours are not published.</p>
      </div>
    </section>''')

    contact = contact_page(site, "<p>Phone 469.233.3366. Email customerservice@caremaster.biz. Mailing address: PO Box 29303, Dallas, TX 75229. Street hours are not published on caremaster.biz — none are added here. No customer reviews are published.</p>")
    write_site(site, {"index.html": index, "about.html": about, "services.html": services, "commitment.html": commit, "contact.html": contact})
    return site


# ---------------------------------------------------------------------------
# 6 Forum Terrace Church of Christ
# ---------------------------------------------------------------------------
def forum() -> dict:
    site = {
        "slug": "forum-terrace-church",
        "name": "Forum Terrace Church of Christ",
        "tagline": "Grand Prairie, TX",
        "city": "Grand Prairie, TX",
        "logo": "assets/logo.png",
        "logo_class": "logo wide",
        "body_class": "theme-dark-header",
        "phone_display": "(972) 922-3249",
        "phone_tel": "+19729223249",
        "address": "2446 Arkansas Lane, Grand Prairie, Texas 75052",
        "hours": "Sunday Bible Study 9:30 a.m. · Worship 10:30 a.m. · Worship 5:00 p.m. · Wednesday Bible Study 7:30 p.m.",
        "eyebrow": "A church family in Grand Prairie",
        "contact_lede": "Call Dan Vess or send a message. The congregation does not publish an email address.",
        "form_status": "Thank you. This page does not send messages automatically — please call (972) 922-3249 so someone receives your request.",
        "nav": [
            ("index.html", "Home"),
            ("location.html", "Location"),
            ("classes.html", "Bible Classes"),
            ("resources.html", "Resources"),
            ("contact.html", "Contact"),
        ],
        "theme": {
            "bg": "#f6efe6",
            "surface": "#fffaf2",
            "ink": "#3a241f",
            "muted": "#6b5348",
            "brand": "#1d597c",
            "brand2": "#e8d5a3",
            "accent": "#8b5a2b",
            "hero_ink": "#f8eedc",
            "display": "Georgia, serif",
            "pattern": "radial-gradient(circle at 50% 0, rgba(255,255,255,.2), transparent 42%)",
            "pattern_size": "100% 100%",
        },
        "legal": "© <span id=\"year\"></span> Forum Terrace Church of Christ.",
        "footer_extra": "<p>Dan Vess · (972) 922-3249</p>",
    }
    panel = f'''<strong>Service times</strong>
          <p>Sunday Bible Study 9:30 a.m.<br>Sunday Worship 10:30 a.m.<br>Sunday Worship 5:00 p.m.<br>Wednesday Bible Study 7:30 p.m.</p>
          <p>2446 Arkansas Lane, Grand Prairie, Texas 75052</p>
          {kpis([("Sunday", "Bible study & worship"), ("Wednesday", "7:30 p.m. study"), ("Dan Vess", "Contact"), ("Arkansas Ln", "Grand Prairie")])}'''
    index = page(site, title="Forum Terrace Church of Christ | Grand Prairie", description="A family of Christians in Grand Prairie. Sunday Bible study 9:30 a.m., worship 10:30 a.m. and 5:00 p.m.", current="index.html", body=f'''{hero(site, "The Forum Terrace Church of Christ in Grand Prairie welcomes you!", "We are a family of Christians who believe in God’s promise of salvation through His Son, Jesus Christ. We are here to help you on your journey to reach an eternal, spiritual home in Heaven.", "location.html", "Find us", panel)}
{section("who", "Who we are", "If you have questions about God, your soul, or the Church of Christ, we can help you find answers in God’s Word, the Bible.", "<p>Come by and see us at 2446 Arkansas Lane, Grand Prairie, Texas 75052. Give us a ring: Dan Vess, (972) 922-3249.</p>")}
{section("events", "Scheduled events", "Listed on the public homepage.", f'<div class="cards">{cards([
    {"title": "Leadership class", "text": "1st Sunday night of each month."},
    {"title": "Men’s business meeting / visitor status", "text": "2nd Sunday night."},
    {"title": "Children’s Bible drill", "text": "3rd Sunday night."},
    {"title": "Saturday singing", "text": "Day before singing night (Friday or Saturday practice)."},
    {"title": "Singing night", "text": "4th Sunday night."},
    {"title": "Quarterly prayer meeting", "text": "5th Sunday night."},
])}</div>')}
{section("resources", "Tracts, sermons, workbooks, and bulletins", "Published on forumterrace.org. Open the live pages for the files — titles are not rewritten here.", '''<div class="cards">
          <article class="card"><h3>Tracts</h3><p>Baptism, Bible, Blood, Christ, Church, Gospel, and other tracts.</p><p><a href="http://forumterrace.org/tracts/">forumterrace.org/tracts/</a></p></article>
          <article class="card"><h3>Sermons</h3><p>Why I Am a Member of The Church Of Christ series and other audio.</p><p><a href="http://forumterrace.org/sermons/">forumterrace.org/sermons/</a></p></article>
          <article class="card"><h3>Workbooks</h3><p>Bible class workbooks (the live Workbooks nav points here).</p><p><a href="http://forumterrace.org/bible-classes/">forumterrace.org/bible-classes/</a></p></article>
          <article class="card"><h3>Bulletins — The Forum</h3><p>Weekly bulletin archive.</p><p><a href="http://forumterrace.org/category/the-forum/">forumterrace.org/category/the-forum/</a></p></article>
        </div><p class="note">The member directory is gated on the live site and is not copied here.</p>''')}''')

    location = page(site, title="Location | Forum Terrace Church of Christ", description="2446 Arkansas Lane, Grand Prairie, Texas 75052.", current="location.html", body=f'''{page_hero("Where we are", "The Forum Terrace Church of Christ is located in the center of the Texas DFW Metroplex, on the eastern border of Arlington in Grand Prairie.")}
    <section>
      <div class="wrap prose">
        <p>Since we are centrally located, we are easy to get to from multiple surrounding communities. We’d love for you to come visit!</p>
        <p><strong>Forum Terrace Church of Christ</strong><br>2446 Arkansas Lane<br>Grand Prairie, Texas 75052<br>(972) 922-3249</p>
      </div>
    </section>''')

    classes = page(site, title="Bible Classes | Forum Terrace Church of Christ", description="Current and recent adult, young adult, and teen Bible classes.", current="classes.html", body=f'''{page_hero("Bible classes", "Class titles published on the Bible Classes page.")}
{section("current", "2026 classes", "Quarterly adult and young-adult studies.", f'<div class="cards">{cards([
    {"title": "2026 3rd Quarter Sunday Adult", "text": "Church Discipline"},
    {"title": "2026 2nd Quarter Sunday Adult", "text": "Job"},
    {"title": "2026 2nd Quarter Wednesday Adult", "text": "Dynamic Christian Life"},
    {"title": "2026 1st Quarter Sunday Adult", "text": "Spiritual Health CheckUp"},
    {"title": "2026 1st Quarter Wednesday Adult", "text": "Myth Busting"},
    {"title": "2026 1st Quarter Sunday Young Adult", "text": "Great Verses New Testament"},
    {"title": "2026 1st Quarter Wednesday Young Adult", "text": "Lord’s Supper"},
])}</div><p class="note">The full workbook list is on <a href="http://forumterrace.org/bible-classes/">forumterrace.org/bible-classes/</a>.</p>')}''')

    resources = page(site, title="Resources | Forum Terrace Church of Christ", description="Links to published tracts, sermons, workbooks, and bulletins.", current="resources.html", body=f'''{page_hero("Resources", "Open the congregation’s published pages. Content is not rewritten here.")}
{section("links", "On forumterrace.org", "Member directory is gated and skipped.", '''<div class="cards">
          <article class="card"><h3>Tracts</h3><p><a href="http://forumterrace.org/tracts/">forumterrace.org/tracts/</a></p></article>
          <article class="card"><h3>Sermons</h3><p><a href="http://forumterrace.org/sermons/">forumterrace.org/sermons/</a></p></article>
          <article class="card"><h3>Workbooks / Bible classes</h3><p><a href="http://forumterrace.org/bible-classes/">forumterrace.org/bible-classes/</a></p></article>
          <article class="card"><h3>Bulletins — The Forum</h3><p><a href="http://forumterrace.org/category/the-forum/">forumterrace.org/category/the-forum/</a></p></article>
        </div>''')}''')

    contact = contact_page(site, "<p>Have a question or comment? Call Dan Vess at (972) 922-3249. Come by 2446 Arkansas Lane, Grand Prairie, Texas 75052. No public email is listed. The member directory is gated and is not included here.</p>")
    write_site(site, {"index.html": index, "location.html": location, "classes.html": classes, "resources.html": resources, "contact.html": contact})
    return site


# ---------------------------------------------------------------------------
# 7 B&B Complete Auto
# ---------------------------------------------------------------------------
def bb() -> dict:
    site = {
        "slug": "bb-complete-auto",
        "name": "B&B Complete Auto Repair",
        "tagline": "Garland, Richardson & Dallas",
        "city": "Garland, TX",
        "logo": "assets/logo.png",
        "logo_class": "logo wide",
        "phone_display": "(214) 994-6989",
        "phone_tel": "+12149946989",
        "email": "ali@bbcompleteautorepair.com",
        "address": "2206 South Shiloh Road, Garland, TX 75041",
        "hours": "Monday–Saturday 8 AM–6 PM · Sunday closed",
        "eyebrow": "Complete car care at affordable rates",
        "nav": [
            ("index.html", "Home"),
            ("about.html", "About"),
            ("services.html", "Services"),
            ("areas.html", "Service Areas"),
            ("faq.html", "F.A.Q."),
            ("contact.html", "Contact"),
        ],
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
        "legal": "© <span id=\"year\"></span> B&amp;B Complete Auto Repair. License CO16-0388.",
    }
    panel = f'''<strong>Book the bay</strong>
          <p><a href="tel:+12149946989">(214) 994-6989</a></p>
          <p>2206 South Shiloh Road, Garland, TX 75041</p>
          <p>Monday–Saturday 8 AM–6 PM · Sunday closed</p>
          {kpis([("Sat", "Open 8–6"), ("All makes", "Foreign & domestic"), ("CO16-0388", "License"), ("Written", "Estimates")])}'''
    index = page(site, title="B&B Complete Auto Repair | Garland, Richardson & Dallas", description="One-stop auto repair on South Shiloh Road. Call (214) 994-6989. Open Monday–Saturday 8–6.", current="index.html", body=f'''{hero(site, "Automotive repair in Dallas, Richardson and Garland.", "B&B Complete Auto Repair is the one-stop auto repair shop you need, providing a complete range of car care services at affordable rates.", "services.html", "See shop services", panel)}
{section("services", "Services include", "Fully equipped for maintenance and repair on all makes and models, foreign or domestic.", f'<div class="cards">{cards([
    {"title": "Oil and filter changes", "text": "Factory-scheduled maintenance and oil service."},
    {"title": "Radiator repair", "text": "Cooling system repair and inspection."},
    {"title": "Auto body & collision", "text": "Auto body services and collision repair."},
    {"title": "Auto glass", "text": "Auto glass repair and replacement."},
    {"title": "Brakes", "text": "Brake check and repair."},
    {"title": "Exhaust", "text": "Exhaust system repair."},
    {"title": "Transmission", "text": "Transmission repair and rebuild."},
    {"title": "Engine repair", "text": "Engine diagnostics and repair."},
    {"title": "Tires & alignment", "text": "Tire services, rotation, and wheel alignment."},
    {"title": "Diagnostics", "text": "Check-engine light diagnostics and computer diagnostics."},
    {"title": "German auto repair", "text": "Service page for German vehicles, listed in the shop nav."},
    {"title": "Battery & electrical", "text": "Battery and electrical repairs."},
    {"title": "Inspections & warranties", "text": "Preventative maintenance, inspections, and warranty programs."},
])}</div>')}
{section("why", "Honest automotive professionals", "Fair and honest pricing, written estimates, computer diagnostics, local shuttle services, towing services, factory trained technicians, worry-free warranty protection, brand name parts, and loaner vehicles.", "<p>The live site’s gallery is empty and reviews load only through an Elfsight widget. No reviews are copied here.</p>")}''')

    about = page(site, title="About | B&B Complete Auto Repair", description="Certified mechanics, written estimates, and customer service in Garland.", current="about.html", body=f'''{page_hero("About B&B Complete Auto Repair", "Auto maintenance in Dallas, Richardson and Garland.")}
    <section>
      <div class="wrap prose">
        <p>B&B Complete Auto Repair is committed to offering quality customer service from our fully equipped car care center. Our certified mechanics can handle any repair or maintenance problem from basic tire services to complete transmission repair and have developed long-standing working relationships with clients based on honesty and personalized service.</p>
        <p>We’ll discuss everything with you and try to remain within your budget. Regular tune-ups add longevity. We use the latest methods, tools and techniques. Our skilled technicians take the time to clearly explain your repair options, provide detailed written estimates, and help with insurance processing.</p>
        <p>When your vehicle must remain in the shop, our staff will make arrangements for a loaner vehicle, shuttle services, or discounted car rentals.</p>
      </div>
    </section>''')

    services = page(site, title="Auto Repair Services | B&B Complete Auto Repair", description="Diagnostics, brakes, engines, transmissions, glass, German repair, and more.", current="services.html", body=f'''{page_hero("Complete automotive services", "Nav service lines from bbcompleteautorepair.com.")}
{section("list", "Auto repair services", "As listed in the public navigation and homepage service list.", f'<div class="cards">{cards([
    {"title": "Auto glass", "text": "Auto glass repair and replacement."},
    {"title": "German auto repair", "text": "Repair for German makes."},
    {"title": "Brake services", "text": "Brake check and repair."},
    {"title": "Collision repair", "text": "Auto body services and collision repair."},
    {"title": "Engine repair", "text": "Engine diagnostics and repair."},
    {"title": "Exhaust repair", "text": "Exhaust system repair."},
    {"title": "Oil change", "text": "Oil and filter changes."},
    {"title": "Radiator repair and inspection", "text": "Cooling system repair and inspection."},
    {"title": "Auto diagnostics", "text": "Check-engine light and computer diagnostics."},
    {"title": "Tire rotation and alignment", "text": "Rotation and wheel alignment."},
    {"title": "Tire services", "text": "Tire service and replacement."},
    {"title": "Transmission service", "text": "Transmission repair, rebuild, inspection, and flush."},
])}</div>')}''')

    areas = page(site, title="Service Areas | B&B Complete Auto Repair", description="Dallas, Garland, and Richardson auto repair.", current="areas.html", body=f'''{page_hero("Service areas", "Cities named on the public service-areas page.")}
{section("cities", "Dallas, Garland, and Richardson", "Each service line on their areas page is listed for these three cities.", f'<div class="chip-row">{chips(["Dallas", "Garland", "Richardson"])}</div><p class="note">Service lines named there include auto glass, maintenance and inspection, brakes, collision, differential, engine, exhaust, garage mechanic, oil change, radiator, tire rotation, tire service, and transmission.</p>')}''')

    faq = page(site, title="F.A.Q. | B&B Complete Auto Repair", description="Published automotive repair FAQs.", current="faq.html", body=f'''{page_hero("Frequently asked questions", "From the public F.A.Q. page.")}
{section("q", "Answers", "Quoted from the live FAQ.", f'<div class="cards two">{cards([
    {"title": "What kind of cars do you repair?", "text": "A complete range of repair and maintenance services. We handle all makes and models of cars, trucks and SUVs whether imported or domestic."},
    {"title": "What are my payment options?", "text": "VISA, MasterCard, debit, and cash. Payment plans for major repairs — call for more information."},
    {"title": "How often do I need an oil change?", "text": "The general rule is every 5000 miles. Follow the manufacturer’s instructions and consult our auto repair experts."},
    {"title": "How often should my brake system be inspected?", "text": "According to the manufacturer’s recommendation, every 12 months."},
    {"title": "What if my check-engine light comes on?", "text": "It doesn’t necessarily signal a need for major repairs. Have your vehicle checked by a professional."},
    {"title": "Do you offer transmission maintenance?", "text": "Inspection and transmission flush services that include filter, gasket and fluid replacement. Certified mechanics provide complete transmission repairs and rebuilds for any foreign or domestic vehicle."},
    {"title": "Is preventative maintenance important?", "text": "Yes. If your vehicle is properly maintained it will last longer, operate more efficiently and save you money. Your owner’s manual outlines recommended schedules."},
    {"title": "My car is leaking clear fluid. Is that dangerous?", "text": "Liquid leaking is usually a sign that something is wrong. Clear liquid may be water condensation from the AC, which is normal, or brake fluid, which is usually yellowish with an oily feel."},
    {"title": "My car smells funny but is running fine. Should I be worried?", "text": "The moment your vehicle begins emitting an odor, bring it in. Smells can signal a stuck brake, overheated engine, fuel leak, or electrical short."},
])}</div>')}''')

    contact = contact_page(site, "<p>License: CO16-0388. Email ali@bbcompleteautorepair.com. 2206 South Shiloh Road, Garland, TX 75041. Monday–Saturday 8 AM–6 PM. Sunday closed.</p>")
    write_site(site, {"index.html": index, "about.html": about, "services.html": services, "areas.html": areas, "faq.html": faq, "contact.html": contact})
    return site


# ---------------------------------------------------------------------------
# 8 Ferraro DDS
# ---------------------------------------------------------------------------
def ferraro() -> dict:
    site = {
        "slug": "ferraro-dds",
        "name": "Daniel L. Ferraro, D.D.S.",
        "tagline": "Grand Prairie & Arlington",
        "city": "Grand Prairie, TX",
        "logo": "assets/logo.png",
        "body_class": "theme-dark-header",
        "phone_display": "(972) 988-8044",
        "phone_tel": "+19729888044",
        "email": "danielferrarodds@sbcglobal.net",
        "address": "2985 S. Hwy 360, Suite 210, Grand Prairie, Texas 75052",
        "hours": "Monday–Thursday 8:00 AM–5:00 PM",
        "eyebrow": "Grand Prairie / Arlington · 30+ years",
        "nav": [
            ("index.html", "Home"),
            ("about.html", "About"),
            ("services.html", "Services"),
            ("testimonials.html", "Testimonials"),
            ("contact.html", "Contact"),
        ],
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
            "pattern_size": "100% 100%",
        },
        "legal": "© <span id=\"year\"></span> Daniel L. Ferraro, D.D.S.",
        "footer_extra": "<p>Emerald Square Shopping Center · N.E. corner of Hwy 360 and Mayfield Rd.</p>",
    }
    panel = f'''<strong>Call the office</strong>
          <p><a href="tel:+19729888044">(972) 988-8044</a></p>
          <p>2985 S. Hwy 360, Suite 210<br>Grand Prairie, Texas 75052</p>
          <p>Monday–Thursday 8:00 AM–5:00 PM</p>
          <p>Friday hours are not listed on the published site</p>
          {kpis([("1986", "DDS, UT San Antonio"), ("3M", "Mini-implant certified"), ("Hwy 360", "Emerald Square"), ("Mon–Thu", "8:00–5:00")])}'''
    index = page(site, title="Grand Prairie Dentist | Dr. Daniel Ferraro, DDS", description="General dentistry and implants in Grand Prairie at Hwy 360 and Mayfield. Call (972) 988-8044.", current="index.html", body=f'''{hero(site, "Welcome to our dental practice.", "Daniel L. Ferraro, D.D.S. — proudly serving the Grand Prairie/Arlington areas’ dental needs for over 30 years. Superior dental care, comfortably, conservatively, in a relaxed environment, at a reasonable cost.", "services.html", "Our services", panel)}
{section("welcome", "Convenient Grand Prairie location", "We are in Emerald Square Shopping Center at the N.E. corner of Hwy 360 and Mayfield Rd. in Grand Prairie, one exit north of Interstate 20 on Hwy 360.", '''<div class="prose">
          <p>Dr. Ferraro is certified by 3M in the placement of mini-implants — small diameter, self-tapping, one-piece, low-cost implants that can support fixed or removable replacement teeth.</p>
          <p>We provide all phases of general dentistry including guaranteed beautiful veneers, metal-free crowns and bridge, fillings, one-appointment root canal therapy, extractions, dentures, and bleaching. We also provide routine placement and restoration of conventional implants.</p>
          <p>Published implant special: $1100/implant, or $2100 including the abutment and the crown (sometimes a specialist is necessary if there is not enough available bone). The homepage also lists implant specials at $2400 — call to confirm current pricing. Free implant consultations, free second opinions, and free consultations for patients without dental insurance if you call and ask. X-rays included if needed.</p>
        </div>''')}''')

    about = page(site, title="About & Meet the Doctor | Daniel L. Ferraro, D.D.S.", description="Dr. Ferraro graduated from UT Dental School at San Antonio in 1986.", current="about.html", body=f'''{page_hero("Meet the doctor", "Daniel L. Ferraro, D.D.S.")}
    <section>
      <div class="wrap prose">
        <p><img class="portrait" src="assets/doctor.webp" alt="Daniel L. Ferraro, D.D.S."></p>
        <p>Daniel L. Ferraro, D.D.S. graduated from The University of Texas Dental School at San Antonio in 1986, and has been in private practice in Grand Prairie, TX ever since. Originally from Pittsburgh, PA, he moved to Arlington, TX in 1978 from Rhode Island. Dr. Ferraro graduated from The University of Texas at Arlington in 1981 with a B.S. in Biology and a minor in Chemistry.</p>
        <p>2016 marked the 25th anniversary of marriage to the former Karen Flores of San Antonio. Blessed with four children: daughters Victoria and Samantha, and sons Nicolas and Christopher. Outside interests include watching all sports and being an active member of Fielder Road Baptist Church.</p>
        <h2>The practice</h2>
        <p>We are proud to provide a state-of-the-art facility. Our office meets and surpasses OSHA and CDC standards. We welcome all patients as if they were family.</p>
        <p>We submit insurance forms and help you recover benefits. Payment: check, cash, any major credit card, and CareCredit (a one-year interest-free financing option). Please provide at least 24 hours notice if you cannot keep an appointment; a fee may be charged for no-shows without sufficient notice.</p>
      </div>
    </section>''')

    services = page(site, title="Our Services | Daniel L. Ferraro, D.D.S.", description="Hygiene, implants, cosmetic, endodontics, restorative, pediatric, periodontics, and oral surgery.", current="services.html", body=f'''{page_hero("Our services", "Treatments listed on the practice site.")}
{section("list", "Care we provide", "Confirm current details by phone.", f'<div class="cards">{cards([
    {"title": "Dental hygiene", "text": "Annual checkups and cleanings to keep teeth happy and healthy."},
    {"title": "Implants & mini-implants", "text": "Conventional implants and 3M-certified mini-implants. Free consults."},
    {"title": "Cosmetic", "text": "Beautiful veneers, whitening, and bonding."},
    {"title": "Endodontics", "text": "Root canal therapy (including one-appointment) and retreatment."},
    {"title": "Restorative", "text": "Bridges, metal-free crowns, dentures, and bonding."},
    {"title": "Pediatric", "text": "Sealants and mouth guards."},
    {"title": "Periodontics", "text": "Crown lengthening, frenectomy, occlusal adjustment, cosmetic periodontal surgery, gum disease, scaling and root planing."},
    {"title": "Oral surgery", "text": "Extractions, wisdom teeth, extraction site preservation."},
    {"title": "TMJ & night guards", "text": "TMJ care and night guards."},
    {"title": "Technology", "text": "Panorex, rotary endodontics, and oral cancer screenings."},
])}</div>')}''')

    testi = page(site, title="Testimonials | Daniel L. Ferraro, D.D.S.", description="Published patient note from the practice testimonials page.", current="testimonials.html", body=f'''{page_hero("Patient testimonials", "Selected by Dallas/Fort Worth Top Rated Doctors, 2016.")}
{section("one", "Published comment", "The practice site publishes this one patient quote. No other reviews are copied.", f'<div class="cards">{reviews([{"quote": "I am so proud of my new teeth. I can smile and smile and smile!", "name": "Mrs. Conger", "stars": ""}])}</div>')}''')

    contact = contact_page(site, "<p>Email danielferrarodds@sbcglobal.net. Monday–Thursday 8:00 AM–5:00 PM. Friday hours are not listed on the published site. The live website was behind a Cloudflare challenge when fetched; the logo and copy come from the public October 2025 archive of grandprairie-arlingtondental.com.</p>")
    write_site(site, {"index.html": index, "about.html": about, "services.html": services, "testimonials.html": testi, "contact.html": contact})
    return site


# ---------------------------------------------------------------------------
# 9 Garden Restaurant
# ---------------------------------------------------------------------------
def garden() -> dict:
    site = {
        "slug": "garden-restaurant",
        "name": "Garden Restaurant",
        "tagline": "Garland, TX",
        "city": "Garland, TX",
        "logo": "assets/logo.png",
        "logo_class": "logo wide",
        "phone_display": "(972) 487-8289",
        "phone_tel": "+19724878289",
        "email": "gardenrestaurant@zing.com",
        "address": "3555 W Walnut St, Garland, TX 75042",
        "hours": "Daily 10:00 AM–10:00 PM",
        "eyebrow": "Chinese restaurant in Garland",
        "nav": [
            ("index.html", "Home"),
            ("about.html", "About Us"),
            ("menu.html", "Menu"),
            ("contact.html", "Contact"),
        ],
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
            "pattern_size": "100% 100%",
        },
        "legal": "© <span id=\"year\"></span> Garden Restaurant. All rights reserved.",
    }
    panel = f'''<strong>Visit or call ahead</strong>
          <p><a href="tel:+19724878289">(972) 487-8289</a></p>
          <p>3555 W Walnut St, Garland, TX 75042</p>
          <p>Open daily 10:00 AM–10:00 PM</p>
          {kpis([("Dine-in", "Family tables"), ("Takeout", "Call or order ahead"), ("Delivery", "3rd-party partners"), ("Walnut", "Garland")])}'''
    index = page(site, title="Garden Restaurant | Garland, TX", description="Chinese restaurant at 3555 W Walnut St, Garland. Open daily 10 AM–10 PM. Call (972) 487-8289.", current="index.html", body=f'''{hero(site, "Fresh and flavorful dishes in Garland, TX.", "Welcome to Garden Restaurant. We’re proud to serve a variety of delicious meals made with care and quality ingredients — for a quick bite or dining with family and friends.", "menu.html", "See the menu", panel)}
{section("about", "About us", "We strive to create a warm and welcoming atmosphere for everyone. Join us today and enjoy great food, great service, and a cozy experience.", f'<div class="cards">{cards([
    {"title": "Takeout", "text": "Yes. We offer takeout during regular business hours. Order ahead online and pick up during the estimated time, or call to place an order."},
    {"title": "Hours", "text": "Monday–Sunday 10:00 AM–10:00 PM, as published on the contact page."},
    {"title": "Location", "text": "3555 W Walnut St, Garland, TX 75042, USA."},
    {"title": "Contact-free delivery", "text": "Yes — via 3rd-party partners if you select that option during checkout."},
])}</div>')}''')

    about = page(site, title="About Us | Garden Restaurant", description="Chinese restaurant in Garland serving dine-in, takeout, and delivery.", current="about.html", body=f'''{page_hero("About Garden Restaurant", "Your go-to spot for fresh and flavorful dishes in Garland, TX.")}
    <section>
      <div class="wrap prose">
        <p>We’re proud to serve a variety of delicious meals made with care and quality ingredients. Whether you’re stopping by for a quick bite or dining with family and friends, we strive to create a warm and welcoming atmosphere for everyone.</p>
        <p>Jobs: the restaurant publishes a hiring form on the live site. Call if you have questions about joining the team.</p>
        <p>The published About and Events pages are short. No extra event copy is added here.</p>
      </div>
    </section>''')

    def menu_block(title: str, items: list) -> str:
        rows = "".join(f"<li><span>{esc(n)}</span><span class=\"price\">{esc(p)}</span></li>" for n, p in items)
        return f'<article class="card"><h3>{esc(title)}</h3><ul class="menu-list">{rows}</ul></article>'

    menu_data = json.loads((SCAFFOLD / "garden-menu.json").read_text(encoding="utf-8"))
    blocks = "\n        ".join(menu_block(title, items) for title, items in menu_data)

    menu = page(site, title="Menu | Garden Restaurant", description="Full priced menu from gardenrestaurantgarland.com/menu.php.", current="menu.html", body=f'''{page_hero("Menu", "All categories and prices as published on the restaurant menu page. Call to confirm today’s availability.")}
    <section>
      <div class="wrap cards two">
        {blocks}
      </div>
      <div class="wrap"><p class="note">Full priced menu from gardenrestaurantgarland.com/menu.php. Call (972) 487-8289 to confirm today’s availability. The live site publishes no reviews; none are added here.</p></div>
    </section>''')

    contact = contact_page(site, "<p>Email gardenrestaurant@zing.com. Reservations and catering inquiries are listed on the live contact form.</p>")
    write_site(site, {"index.html": index, "about.html": about, "menu.html": menu, "contact.html": contact})
    return site


# ---------------------------------------------------------------------------
# 10 Law Office of Len Conner
# ---------------------------------------------------------------------------
def len_conner() -> dict:
    site = {
        "slug": "len-conner-law",
        "name": "Law Office of Len Conner",
        "tagline": "Irving family law",
        "city": "Irving, TX",
        "logo": "assets/logo.jpg",
        "logo_class": "logo wide",
        "phone_display": "(972) 445-1500",
        "phone_tel": "+19724451500",
        "address": "600 John Carpenter Freeway, Ste 238, Irving, Texas 75062",
        "eyebrow": "Divorce & family law",
        "nav": [
            ("index.html", "Home"),
            ("about.html", "Firm & Attorney"),
            ("practice.html", "Practice Areas"),
            ("contact.html", "Contact"),
        ],
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
            "pattern_size": "100% 100%",
        },
        "legal": "© <span id=\"year\"></span> Len Conner &amp; Associates. Unless otherwise indicated, attorneys listed are not certified by the Texas Board of Legal Specialization. This site is general information only and does not create an attorney-client relationship.",
        "form_status": "Thank you. Do not include confidential case facts here. Please call (972) 445-1500 so the office receives your request.",
    }
    cities = [
        "Irving", "Dallas", "Cedar Hill", "Mesquite", "Garland", "Grand Prairie", "Las Colinas",
        "Richardson", "Plano", "Highland Park", "Arlington", "Hurst", "Euless", "Bedford",
        "Southlake", "Grapevine", "Colleyville", "Lewisville", "Denton", "The Colony", "Coppell",
        "Flower Mound", "Corinth", "Argyle", "Fort Worth", "Frisco", "Sachse", "McKinney",
        "Park Cities", "Duncanville", "Desoto", "Dallas County", "Tarrant County", "Denton County", "Collin County",
    ]
    panel = f'''<strong>Office</strong>
          <p><a href="tel:+19724451500">(972) 445-1500</a></p>
          <p>600 John Carpenter Freeway, Ste 238<br>Irving, Texas 75062</p>
          <p>Corner of John Carpenter Freeway and Rochelle Boulevard</p>
          {kpis([("Family law", "Practice focus"), ("J.D., M.B.A.", "Len M. Conner"), ("Irving", "John Carpenter Fwy"), ("DFW", "Surrounding counties")])}'''
    badges = '''<div class="badge-row">
          <img src="assets/badge-best-in-irving.png" alt="Best in Irving 2022 Winner">
          <img src="assets/badge-superlawyers.jpg" alt="Rated by Super Lawyers — Len Michael Conner">
          <img src="assets/badge-avvo.jpeg" alt="Avvo Rating 10.0 Superb">
        </div>'''
    index = page(site, title="Attorney Len Conner | Irving Divorce & Family Law", description="The Law Office of Len Conner focuses on comprehensive divorce and family law. Call (972) 445-1500.", current="index.html", body=f'''{hero(site, "Irving & Dallas County family law lawyer.", "The Law Office of Len Conner focuses on comprehensive divorce and family law representation. Len has spent his entire legal career on family law matters, identifying and implementing the best solutions for his clients.", "practice.html", "Practice areas", panel)}
{section("intro", "Your decisions are only as good as the information and advice you receive.", "Though Len has extensive family law litigation experience, he will also help you use negotiated settlements, mediation, and a collaborative divorce process.", f'''<div class="prose">
          <p>Our office partners with psychologists, social workers, financial advisors, private investigators, and tax professionals. To set up a confidential meeting, call 972-445-1500. Our office is in Irving; we represent clients in surrounding cities and counties.</p>
          <p>Fully licensed by the Texas Supreme Court. Admitted to the U.S. Federal Courts, Northern District of Texas. Member of the Texas Family Law Section of the Texas State Bar Association.</p>
          {badges}
        </div>''')}
{section("reviews", "Client testimonials", "The five comments published on the lonestarlaw.net homepage. The /testimonials/ page returns 404.", f'<div class="cards two">{reviews([
    {"quote": "Len is an outstanding, sensible lawyer that makes wise decisions with time and money, consistently considering what's in the best interest of his client in the long term. I'm thankful he walked me through such a difficult time. I highly recommend him.", "name": "Marie", "stars": ""},
    {"quote": "Len Conner is an exceptional attorney with an incredible disposition and knowledge for family law. He helped us with a child support case that had been drowning us for years. He cares for his clients and the outcome of the case.", "name": "Marc and Jill", "stars": ""},
    {"quote": "Len is a great lawyer that keeps his clients needs top of mind. I felt like Mr. Conner and his team truly understood my needs and was genuine in their approach. I believe they really cared for my children and their well-being.", "name": "David", "stars": ""},
    {"quote": "Len Conner and his staff are the real deal. They tell you like it is. They have always been available when I needed them. He will guide you to do what is best for you and your pocket book, not his pocket book.", "name": "Dena", "stars": ""},
    {"quote": "From the very start I was confident Len Conner and his team were indeed experts at Family Law. They were patient with me in walking me through the process of divorce, and continually informed me of all of my options.", "name": "Kelly", "stars": ""},
])}</div>', "reviews")}
{section("area", "Cities and counties we serve", "Listed on the public site.", f'<div class="chip-row">{chips(cities)}</div>')}''')

    about = page(site, title="Firm Overview & Len M. Conner | Law Office of Len Conner", description="Dallas-born Irving family law attorney and mediator.", current="about.html", body=f'''{page_hero("Firm overview", "Dallas divorce and family law attorney serving Fort Worth, Irving, Plano & Frisco.")}
    <section>
      <div class="wrap prose">
        <p>Len Conner & Associates maintains the ability to provide quality representation throughout Texas. We routinely represent clients from across the United States and throughout the world, including Afghanistan, Costa Rica, India, Iraq, Germany, Mexico, Japan, and the Philippines.</p>
        <p>The firm focuses exclusively on Texas family law and divorce. Attorney Len Conner often lectures lawyers on family and divorce topics for continuing legal education.</p>
        <h2>Len M. Conner, J.D., M.B.A., B.B.A.</h2>
        <p>Len Conner was born in Dallas, Texas and raised in Irving. He attended the University of North Texas and earned his Bachelor’s degree in business management in 1990. He worked in the pharmaceutical industry while he attended Dallas Baptist University and earned his Master’s in Business Administration. He then attended Texas Wesleyan University School of Law, earned his Juris Doctor, and was a member of Law Review.</p>
        <p>Mr. Conner is a family law mediator and conflict resolution mediator. He is licensed by the Texas Supreme Court and admitted to practice in the United States Federal District Courts in the Northern District of Texas. Memberships include the American Bar Association, Texas Bar Association, Dallas Bar Association, Tarrant County Bar Association, American Trial Lawyers Association, the Family Law Section of the State Bar of Texas, and the Annette Stewart Inn of Court. He has lectured on alimony, spousal support, spousal maintenance, and contested temporary orders hearings.</p>
        <p>Mr. Conner limits the number of matters he handles so every client receives personal attention. He personally supervises every case and typically returns calls the same day.</p>
      </div>
    </section>''')

    practice = page(site, title="Practice Areas | Law Office of Len Conner", description="Contested and uncontested divorce, custody, support, military divorce, mediation, and more.", current="practice.html", body=f'''{page_hero("Practice areas", "We dedicate our practice exclusively to divorce and family law.")}
{section("list", "Matters we handle", "Published practice-area list.", f'<div class="cards">{cards([
    {"title": "Contested divorce", "text": "Litigation when the parties cannot agree."},
    {"title": "Uncontested divorce", "text": "Agreed-upon divorce."},
    {"title": "Modifications & enforcements", "text": "Changing or enforcing existing orders."},
    {"title": "Child support", "text": "Support matters for Texas families."},
    {"title": "Child custody", "text": "Custody and visitation."},
    {"title": "Interstate visitation", "text": "Visitation across state lines."},
    {"title": "Collaborative divorce", "text": "Resolving issues without court intervention."},
    {"title": "Military divorce", "text": "Unique issues and challenges in military divorce proceedings."},
    {"title": "Termination of parental rights", "text": "Parental-rights termination matters."},
    {"title": "Stepparent adoptions", "text": "Stepparent adoption."},
    {"title": "Mediation & arbitration", "text": "Family law mediation and arbitration."},
    {"title": "Paternity rights", "text": "Paternity determinations."},
    {"title": "Marital property", "text": "Property issues in divorce."},
    {"title": "Domestic violence", "text": "Family-violence related matters."},
    {"title": "Criminal law in divorce", "text": "When criminal issues intersect with the family case."},
    {"title": "Grandparents’ rights", "text": "Grandparent rights under Texas law."},
    {"title": "Fathers’ rights", "text": "Fathers’ rights in Texas."},
])}</div><p class="note">Also published: divorce myths, divorce FAQs, and a legal glossary on lonestarlaw.net.</p>')}''')

    contact = contact_page(site, "<p>The office is at the corner of John Carpenter Freeway and Rochelle Boulevard. No public email or office hours are listed on lonestarlaw.net. Do not send confidential case facts through this page — call (972) 445-1500.</p>")
    write_site(site, {"index.html": index, "about.html": about, "practice.html": practice, "contact.html": contact})
    return site


GALLERY_META = [
    ("speakes-plumbing", "Speake's Plumbing, Inc.", "Garland, TX", "Residential & commercial plumbing"),
    ("beyond-lawn-care", "Beyond Lawn Care & Landscaping", "Mesquite, TX", "Lawn care & landscaping"),
    ("hughes-mechanical", "Hughes Mechanical and Electrical", "Arlington, TX", "HVAC & electrical contractors"),
    ("victory-pest-control", "Victory Pest Control LLC", "Dallas–Fort Worth", "Pest & wildlife control"),
    ("caremaster-building", "CareMaster Building Services", "Dallas / Fort Worth", "Commercial janitorial"),
    ("forum-terrace-church", "Forum Terrace Church of Christ", "Grand Prairie, TX", "Congregation site"),
    ("bb-complete-auto", "B&B Complete Auto Repair", "Garland, TX", "Auto repair & maintenance"),
    ("ferraro-dds", "Daniel L. Ferraro, D.D.S.", "Grand Prairie, TX", "General dentistry"),
    ("garden-restaurant", "Garden Restaurant", "Garland, TX", "Chinese restaurant"),
    ("len-conner-law", "Law Office of Len Conner", "Irving, TX", "Divorce & family law"),
]


def write_gallery() -> None:
    cards_html = "\n".join(
        f'''<article class="card">
      <p class="muted">{esc(city)}</p>
      <h3>{esc(name)}</h3>
      <p>{esc(industry)}</p>
      <p><a class="btn btn-dark" href="sites/{esc(slug)}/index.html">Open site</a></p>
      <p class="note"><code>sites/{esc(slug)}/</code></p>
    </article>'''
        for slug, name, city, industry in GALLERY_META
    )
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>DFW site rebuilds</title>
  <meta name="description" content="Ten local-business website rebuilds.">
  <link rel="stylesheet" href="scaffold/styles.css">
  <link rel="stylesheet" href="gallery.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap header-row">
      <a class="brand" href="#top">
        <span class="brand-text">
          <strong>DFW site rebuilds</strong>
          <span>Ten local business websites</span>
        </span>
      </a>
    </div>
  </header>
  <main id="main">
    <section class="hero" id="top">
      <div class="wrap">
        <p class="eyebrow">Static HTML · GitHub Pages</p>
        <h1>DFW site rebuilds.</h1>
        <p class="lede">Open any card, or zip a single folder under <code>sites/</code>. Each folder is a finished site with the business’s published content and existing logo.</p>
      </div>
    </section>
    <section>
      <div class="wrap">
        <div class="cards gallery-cards">
          {cards_html}
        </div>
      </div>
    </section>
  </main>
  <footer class="site-footer">
    <div class="wrap">
      <p>GitHub Pages from this repo root. No custom domains. No Azure hosting.</p>
    </div>
  </footer>
</body>
</html>
'''
    (ROOT / "index.html").write_text(html, encoding="utf-8")


README = """# DFW site rebuilds

Ten static website rebuilds for local Dallas–Fort Worth businesses.  
Each folder under `sites/` is a finished site Matthew can open or zip and sell as-is.

**$0 Azure.** No App Service, no custom domains, no paid hosting.  
**No outreach.** Public pages were fetched only. No emails, calls, or live-site form submissions.

## Open locally

From this repo root:

```bash
python3 -m http.server 8080
```

Then open [http://127.0.0.1:8080/](http://127.0.0.1:8080/).

Or open any file directly:

- Gallery: `index.html`
- A single site: `sites/<slug>/index.html`

## Zip one site

Each folder under `sites/` is self-contained (`index.html`, extra pages, `styles.css`, `theme.css`, `site.js`, `assets/`).

```bash
cd sites
zip -r speakes-plumbing.zip speakes-plumbing
```

Unzip and open `index.html`. No build step, no Node, no Azure.

## GitHub Pages

Publish this repo root. Keep `.nojekyll`. The gallery at `/` links to `/sites/<slug>/`.

Preview URLs:

1. https://knecoswd.github.io/dfw-concept-sites/sites/speakes-plumbing/
2. https://knecoswd.github.io/dfw-concept-sites/sites/beyond-lawn-care/
3. https://knecoswd.github.io/dfw-concept-sites/sites/hughes-mechanical/
4. https://knecoswd.github.io/dfw-concept-sites/sites/victory-pest-control/
5. https://knecoswd.github.io/dfw-concept-sites/sites/caremaster-building/
6. https://knecoswd.github.io/dfw-concept-sites/sites/forum-terrace-church/
7. https://knecoswd.github.io/dfw-concept-sites/sites/bb-complete-auto/
8. https://knecoswd.github.io/dfw-concept-sites/sites/ferraro-dds/
9. https://knecoswd.github.io/dfw-concept-sites/sites/garden-restaurant/
10. https://knecoswd.github.io/dfw-concept-sites/sites/len-conner-law/

## The 10 sites

| # | Business | City | Folder |
| --- | --- | --- | --- |
| 1 | Speake's Plumbing, Inc. | Garland | [`sites/speakes-plumbing/`](sites/speakes-plumbing/) |
| 2 | Beyond Lawn Care & Landscaping | Mesquite | [`sites/beyond-lawn-care/`](sites/beyond-lawn-care/) |
| 3 | Hughes Mechanical and Electrical | Arlington | [`sites/hughes-mechanical/`](sites/hughes-mechanical/) |
| 4 | Victory Pest Control LLC | DFW | [`sites/victory-pest-control/`](sites/victory-pest-control/) |
| 5 | CareMaster Building Services | Dallas / Fort Worth | [`sites/caremaster-building/`](sites/caremaster-building/) |
| 6 | Forum Terrace Church of Christ | Grand Prairie | [`sites/forum-terrace-church/`](sites/forum-terrace-church/) |
| 7 | B&B Complete Auto Repair | Garland | [`sites/bb-complete-auto/`](sites/bb-complete-auto/) |
| 8 | Daniel L. Ferraro, D.D.S. | Grand Prairie | [`sites/ferraro-dds/`](sites/ferraro-dds/) |
| 9 | Garden Restaurant | Garland | [`sites/garden-restaurant/`](sites/garden-restaurant/) |
| 10 | Law Office of Len Conner | Irving | [`sites/len-conner-law/`](sites/len-conner-law/) |

## Shared scaffold

- [`scaffold/styles.css`](scaffold/styles.css) — layout, mobile nav, forms
- [`scaffold/site.js`](scaffold/site.js) — menu + on-page form confirmation (does not email the business)
- [`scaffold/build.py`](scaffold/build.py) — rebuilds all 10 folders from the shared files

```bash
python3 scaffold/build.py
```

Contact forms stay on the page. They do not email, store, or submit to the businesses. Please call so the office receives the request.

## Source notes

- **Logos** are the businesses’ existing marks downloaded from their live sites (or the public Wayback copy for Ferraro) and stored under `sites/<slug>/assets/`.
- **Beyond Lawn Care** embeds Google reviews via Elfsight. Review text is not in the HTML and was not invented.
- **Hughes Mechanical** publishes no customer reviews. None were added. Wix placeholder socials were ignored.
- **Victory Pest Control** uses the brand VPC logo (`victory-pest-control-llc-logo-0510bb09-1920w.jpg`), not the Hibu template gen-logo. Owner John Gaines. (972) 230-5526 / mobile (214) 543-6357. 234 Paradise Way, Red Oak, TX 75154. 24 hours. No email. Reviews only: Taylor Akin, Camille Henderson, Michelle Owens. Live “Lorem Ipsum” tagline and `{{placeholder_*}}` tokens were not copied.
- **CareMaster** logo is `logo-2.jpg` from nccdn. Since 1982; Richard Lee / President John Lee. 469.233.3366; customerservice@caremaster.biz; PO Box 29303, Dallas, TX 75229. No reviews. Street hours are not published.
- **Forum Terrace** logo is `cropped-FTCoC_Logo_646x200.png`. 2446 Arkansas Lane; Dan Vess (972) 922-3249; Sun 9:30 / 10:30 / 5:00 and Wed 7:30. Tracts, sermons, workbooks, and bulletins are links to the live HTTP pages. Member directory is gated and skipped. No reviews or email.
- **Ferraro DDS** live site returned Cloudflare 403. Content, the published logo (`…00551Dentallogodesign…png`), and the doctor photo come from the public October 2025 archive / practice CDN. Hours used: Monday–Thursday 8–5. Friday is blank on the source. Email: danielferrarodds@sbcglobal.net. One published quote (Mrs. Conger). Top Rated Doctors 2016.
- **B&B Complete Auto** reviews are Elfsight JS only. Gallery is empty. No reviews or photos were invented. License CO16-0388.
- **Garden Restaurant** menu is the full priced list from `/menu.php` (10 categories). No site reviews. About/Events stay thin.
- **Len Conner** homepage testimonials only (Marie, Marc and Jill, David, Dena, Kelly). `/testimonials/` is 404. No public email or hours. Super Lawyers, Avvo, and Best in Irving 2022 badges from the live site.
- **Speake's** homepage slider labels MashIt / FabuFit / YesSuits are template chrome, not used as company names.
"""


def main() -> None:
    builders = [speakes, beyond, hughes, victory, caremaster, forum, bb, ferraro, garden, len_conner]
    built = [fn() for fn in builders]
    write_gallery()
    (ROOT / "README.md").write_text(README, encoding="utf-8")
    (ROOT / "sites-data.json").write_text(
        json.dumps([{"slug": s["slug"], "name": s["name"], "city": s["city"]} for s in built], indent=2),
        encoding="utf-8",
    )
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Wrote {len(built)} sites")


if __name__ == "__main__":
    main()
