#!/usr/bin/env python3
"""Generate Princeton Smiles static pages. Run from this folder."""
from __future__ import annotations

import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

PHONE_DISPLAY = "(972) 736-3888"
PHONE_TEL = "+19727363888"
EMAIL = "princetonsmiles@gmail.com"
ADDRESS_1 = "501 Princeton Dr., Suite 103B"
ADDRESS_2 = "Princeton, Texas 75407"
MAP_SRC = (
    "https://maps.google.com/maps?q=501+Princeton+Dr+Suite+103B+Princeton+TX+75407"
    "&z=16&output=embed"
)

NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("new-patients.html", "New Patients"),
    ("team.html", "Team"),
    ("contact.html", "Contact"),
]


def png(path: Path, w: int, h: int, pixel):
    raw = bytearray()
    for y in range(h):
        raw.append(0)
        for x in range(w):
            raw.extend(pixel(x, y))

    def chunk(tag: bytes, data: bytes) -> bytes:
        return (
            struct.pack(">I", len(data))
            + tag
            + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    out = b"\x89PNG\r\n\x1a\n"
    out += chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
    out += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    out += chunk(b"IEND", b"")
    path.write_bytes(out)


def tooth_icon(size: int):
    def pixel(x, y):
        # Teal rounded square + generic white tooth. Not a customer mark.
        pad = size * 0.08
        rx, ry = x + 0.5, y + 0.5
        if rx < pad or ry < pad or rx > size - pad or ry > size - pad:
            return (0, 0, 0, 0)
        # rounded corners
        r = size * 0.18
        corners = (
            (pad + r, pad + r),
            (size - pad - r, pad + r),
            (pad + r, size - pad - r),
            (size - pad - r, size - pad - r),
        )
        if (rx < pad + r and ry < pad + r and (rx - corners[0][0]) ** 2 + (ry - corners[0][1]) ** 2 > r * r) or (
            rx > size - pad - r and ry < pad + r and (rx - corners[1][0]) ** 2 + (ry - corners[1][1]) ** 2 > r * r
        ) or (
            rx < pad + r and ry > size - pad - r and (rx - corners[2][0]) ** 2 + (ry - corners[2][1]) ** 2 > r * r
        ) or (
            rx > size - pad - r and ry > size - pad - r and (rx - corners[3][0]) ** 2 + (ry - corners[3][1]) ** 2 > r * r
        ):
            return (0, 0, 0, 0)
        # tooth
        cx, cy = size / 2, size / 2 + size * 0.02
        nx = (rx - cx) / (size * 0.18)
        ny = (ry - cy) / (size * 0.28)
        in_tooth = nx * nx + (ny + 0.15) ** 2 < 1.05 and ny < 0.72
        if in_tooth:
            return (255, 255, 255, 255)
        return (15, 76, 92, 255)

    return pixel


def write_favicons():
    png(ASSETS / "favicon-16.png", 16, 16, tooth_icon(16))
    png(ASSETS / "favicon.png", 32, 32, tooth_icon(32))
    png(ASSETS / "apple-touch-icon.png", 180, 180, tooth_icon(180))


def chrome(active: str, title: str, description: str, extra_head: str = "") -> tuple[str, str]:
    nav_html = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == active else ""
        nav_html.append(f'        <a href="{href}"{current}>{label}</a>')
    nav = "\n".join(nav_html)
    head = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/favicon.png">
  <link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16.png">
  <link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="theme.css">
  {extra_head}
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="wrap header-row">
      <a class="brand" href="index.html">
        <img class="logo wide" src="assets/wordmark.svg" alt="Princeton Smiles Dentistry">
        <span class="brand-text">
          <strong>Princeton Smiles</strong>
          <span>Dentistry · Princeton, TX</span>
        </span>
      </a>
      <nav id="site-nav" class="nav" aria-label="Primary">
{nav}
      </nav>
      <a class="btn btn-dark header-cta" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      <button class="menu-btn" id="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    </div>
  </header>
  <main id="main">
"""
    foot = f"""  </main>
  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <strong>Princeton Smiles Dentistry</strong>
        <p>Dr. Kumar and team · Princeton, Texas</p>
        <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
        <p>{ADDRESS_1}<br>{ADDRESS_2}</p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div>
        <p>Monday–Thursday 8AM–5PM · Friday 8AM–12PM · Saturday–Sunday Closed</p>
        <p>Since 2005, Dr. Kumar has upheld a reputation for excellence. Conveniently located in Princeton, we see patients from Farmersville, Blue Ridge, New Hope, and Merit.</p>
        <p><a href="http://www.facebook.com/pages/Princeton-Smiles/120125238064542">Facebook</a></p>
        <p class="legal">© <span id="year"></span> Princeton Smiles Dentistry. Preview site — generic wordmark and stock clinical imagery only.</p>
      </div>
    </div>
  </footer>
  <div class="callbar">
    <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    <a class="btn btn-dark" href="contact.html">Contact</a>
  </div>
  <script src="site.js"></script>
</body>
</html>
"""
    return head, foot


SCHEMA = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Dentist",
    "name": "Princeton Smiles Dentistry",
    "url": "https://princetonsmiles.com/",
    "telephone": "+19727363888",
    "email": "princetonsmiles@gmail.com",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "501 Princeton Dr., Suite 103B",
      "addressLocality": "Princeton",
      "addressRegion": "TX",
      "postalCode": "75407"
    },
    "openingHoursSpecification": [
      {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday"],"opens":"08:00","closes":"17:00"},
      {"@type":"OpeningHoursSpecification","dayOfWeek":"Friday","opens":"08:00","closes":"12:00"}
    ]
  }
  </script>"""

SERVICES = [
    {
        "slug": "dental-implants",
        "title": "Dental Implants",
        "lead": "Implant placement and restoration at the Princeton office.",
        "body": [
            "Dental implants provide patients with missing teeth an alternative to bridges, partials, and full dentures. Implants can be used to replace a single tooth or multiple teeth. They also support partials and dentures, stopping slippage and restoring functionality. Strong and durable, dental implants can help you achieve a beautiful, natural-looking smile.",
            "How Dental Implants Work. Dr. Kumar will examine your bone density and current oral health. If we decide dental implants are a good fit for you, we’ll proceed with a treatment plan. First, we place the implants in your jawbone to create a solid foundation. After the treatment area heals, we place your custom prosthetics on the implant posts. As an implant dentist with specialized training, Dr. Kumar performs the entire procedure at our Princeton dental practice.",
            "Benefits of Dental Implants. With dental implants, you won’t have to worry about clasps, adhesives, or crowning healthy teeth. The only replacement-tooth solution to anchor teeth in the jawbone, implants stimulate healthy bone growth and prevent a “shrunken” facial appearance. Plus, they restore functionality, allowing you to chew foods you love. Dental implants can restore your smile for potentially a lifetime.",
        ],
    },
    {
        "slug": "braces-orthodontics",
        "title": "Braces (Orthodontics)",
        "lead": "Orthodontics for children, teens, and adults, including traditional braces.",
        "body": [
            "Braces for your child. We recommend bringing your child in for an orthodontic consultation by age seven. In some cases, it’s necessary to start orthodontic treatment before the jaw and gums fully develop. When all your child’s teeth emerge, we may need to perform a second treatment phase.",
            "At our Princeton dental practice, we offer traditional braces for children, teens, and adults, and we also offer ClearCorrect invisible braces. More adults than ever wear braces these days. Some adults, however, want to avoid the youthful image surrounding traditional braces, which is why we also provide a clear aligner option.",
        ],
    },
    {
        "slug": "clearcorrect-invisible-braces",
        "title": "ClearCorrect Invisible Braces",
        "lead": "Custom transparent aligners planned by Dr. Kumar.",
        "body": [
            "How ClearCorrect™ Braces Work. ClearCorrect invisible braces, a custom set of transparent aligners, reposition your teeth and straighten your smile according to a comprehensive treatment plan Dr. Kumar designs. When you need to eat, brush, floss, or clean your ClearCorrect braces, you can remove them.",
            "The ClearCorrect™ Process. If we determine that you are a good candidate for ClearCorrect invisible braces, Dr. Kumar will take impressions of your teeth and plan a course of treatment. Once the process begins, you can change the aligners every two weeks until your smile is straight.",
        ],
    },
    {
        "slug": "cosmetic-dentistry",
        "title": "Cosmetic Dentistry",
        "lead": "Cosmetic smile makeovers using published restorative options.",
        "body": [
            "Using modern dental technology, we can craft cosmetic restorations that look and feel completely natural. Our porcelain veneers and crowns mimic natural tooth enamel, and our teeth whitening system gently removes discolorations to reveal brighter, whiter teeth.",
            "Dr. Kumar’s advanced services include implant dentures, braces for teens and adults, and all-porcelain veneers. As our patient, you can rely on us for complete care in an environment where you will feel relaxed and respected.",
        ],
    },
    {
        "slug": "porcelain-veneers",
        "title": "Porcelain Veneers",
        "lead": "All-porcelain veneers as published on the live services list.",
        "body": [
            "Strong and Stain Resistant. Porcelain veneers don’t just visibly restore your smile. They support it. During the bonding process, we attach the veneers to the surface of your teeth to make your teeth stronger and more durable. Besides strengthening your smile, porcelain veneers also resist stains.",
            "Quick and Conservative. Depending on your current oral health, we can place your veneers in just two easy visits. This includes the design, preparation, and final placement. The procedure is considered conservative, because unlike other treatments, only a small amount of tooth enamel is prepared.",
        ],
    },
    {
        "slug": "teeth-whitening",
        "title": "Teeth Whitening",
        "lead": "In-office and at-home whitening options, including Zoom! Whitening.",
        "body": [
            "Whitening Options. Visit our Princeton dental practice, and Dr. Kumar will evaluate your current oral health. If he believes teeth whitening is a good option for you, you can choose from our convenient whitening options. We offer at-home whitening, which takes a little more time, and in-office whitening.",
            "Zoom! Whitening. Zoom! Whitening is widely recognized as the fastest way to whiten your teeth. The easy process takes about an hour and removes the toughest of stains, including those left behind by coffee, tobacco, and the aging process.",
        ],
    },
    {
        "slug": "wisdom-teeth-removal",
        "title": "Wisdom Teeth Removal",
        "lead": "Evaluation and removal of wisdom teeth at the Princeton practice.",
        "body": [
            "Wisdom teeth are the last teeth to erupt within the mouth. When they align properly and gum tissue is healthy, wisdom teeth do not have to be removed. Unfortunately, this does not generally happen. The extraction of wisdom teeth is necessary when they are prevented from properly erupting within the mouth. They may grow sideways, partially emerge from the gum and even remain trapped beneath the gum and bone.",
            "These poorly positioned impacted teeth can cause many problems. When they are partially erupted, the opening around the tooth allows bacteria to grow and will eventually cause an infection. The pressure from the erupting wisdom tooth may move other teeth and disrupt the orthodontic or natural alignment of teeth. Removal of the offending impacted tooth or teeth usually resolves these problems. Early removal is recommended to avoid such future problems and to decrease the surgical risk involved with the procedure.",
            "With an oral examination and x-rays of the mouth, Dr. Kumar can evaluate the position of the wisdom teeth and predict if there may be present or future problems. Wisdom teeth surgery is performed under appropriate anesthesia to maximize patient comfort. Dr. Kumar has the training, license and experience to provide various types of anesthesia for patients and help choose the best option for them.",
        ],
    },
    {
        "slug": "sedation-dentistry",
        "title": "Sedation Dentistry",
        "lead": "Nitrous oxide, oral sedation, and IV sedation as published.",
        "body": [
            "Sedation dentistry is used to provide a relaxing and anxiety-free experience for patients receiving dental treatment. Sedation is a process used to establish a relaxed, easy and calm state through the use of sedatives. One of the major benefits of sedation dentistry is that people often feel like their dental procedure lasts only a few minutes, when in fact it might have taken hours to perform.",
            "The term sleep dentistry is sometimes used to describe sedation dentistry, but this term is misleading. In actual fact, you do not sleep during the procedure, but because of the effects produced by the sedation medicine, you may feel sleepy.",
            "Nitrous Oxide (Laughing Gas) is mixed with oxygen and inhaled through a small mask that fits over your nose to help you relax. It is not intended to put you to sleep. You will be able to hear and respond to any requests or directions. The effects of nitrous oxide wear off soon after the mask is removed.",
            "Oral Sedation. Sedative medicine is given by mouth in liquid or pill form. Most people feel calmer and more relaxed after taking sedative medication. With oral sedation Dr. Kumar can often perform multiple procedures in a single appointment, without sacrificing either patient safety or clinical quality.",
            "IV Sedation allows unprecedented control over relaxation levels, so we can tailor the sedation to your specific needs. Typically, patients remain conscious and can respond to questions but do not experience extreme nervousness or discomfort, remembering little about the appointment afterwards.",
        ],
    },
    {
        "slug": "laser-dentistry",
        "title": "Laser Dentistry",
        "lead": "Published laser applications for fillings, gum treatment, and whitening.",
        "body": [
            "Versatility and Applications. Lasers can cure (harden) dental materials, scan teeth to detect decay, vaporize decay and prep teeth for fillings, and activate whitening gel to brighten smiles. Currently, dental applications include gum disease treatments, gum re-contouring, and related restorative care.",
        ],
    },
    {
        "slug": "porcelain-crowns",
        "title": "Porcelain Crowns",
        "lead": "Precious metal, porcelain-fused-to-metal, or all-porcelain crowns.",
        "body": [
            "We use precious metal, porcelain pressed (or fused) to metal, or all-porcelain crowns. To maintain a fully white smile, we recommend all-ceramic crowns. Our precise color-matching system allows us to find the right shade of porcelain to blend with your natural tooth color.",
            "Typically, we can design, fit, and place your crowns in just a couple of short appointments. Once a crown is placed, you can care for it as you do your natural teeth. Conscientious brushing twice a day and daily flossing will protect the base of your crown from bacterial growth.",
        ],
    },
    {
        "slug": "crown-and-bridge-treatments",
        "title": "Crown and Bridge Treatments",
        "lead": "Fixed bridges attached to neighboring crowned teeth.",
        "body": [
            "What is a Fixed Bridge? A bridge is a prosthetic tooth (or teeth) that attaches on one or both sides to teeth prepared with dental crowns. A fixed bridge is joined onto the neighboring abutment teeth (crowned teeth) and consists of three basic units: the false tooth and the supporting crowns.",
        ],
    },
    {
        "slug": "tooth-colored-fillings",
        "title": "Tooth Colored Fillings",
        "lead": "Composite resin fillings matched to natural tooth color.",
        "body": [
            "Because composite resins are not made of metal, we can blend and mix shades to find the perfect color to match your natural teeth. This means only you and your dentist will know you have fillings. Another pro is that the tooth/composite bond actually supports the remaining tooth structure.",
        ],
    },
    {
        "slug": "dentures-and-partials",
        "title": "Dentures and Partials",
        "lead": "Partials, full dentures, and implant-supported options.",
        "body": [
            "What is a Partial? A partial denture, commonly referred to as simply a partial, consists of multiple teeth on a gum colored base. The teeth are not in a row, but rather spread across the base to fit like a puzzle with your existing teeth. A partial is normally secured with clips.",
            "What is a Denture? A full denture is a complete top or bottom row of teeth mounted on a gum-colored base. Dentures can be closed or open palate, and they may require denture adhesive to hold them in place.",
            "Implant-Supported Dentures and Partials. Dental implants are small titanium posts anchored into the jawbone. If you prefer a secure full or partial denture and do not want clips or adhesive, then consider implant-supported dentures.",
        ],
    },
    {
        "slug": "root-canals",
        "title": "Root Canals",
        "lead": "Root canal therapy with published comfort notes.",
        "body": [
            "Will root canal therapy hurt? Not with today’s advanced analgesics and technology. In fact, the entire process can be so comfortable that many patients doze off. Oftentimes, root canal therapy can be completed in a single appointment. We simply clean out the diseased canal, fill it, and restore the tooth.",
        ],
    },
    {
        "slug": "general-family-dentistry",
        "title": "General & Family Dentistry",
        "lead": "Prevention-focused care for patients of all ages.",
        "body": [
            "Many people mistakenly believe that tooth decay, bad breath, and gum disease are simply a part of life. They don’t have to be! Our family dental practice emphasizes prevention – meaning that we partner with our patients in the defense against common dental problems, including tooth decay, bad breath, and gum disease.",
            "Tooth Decay. 90% of adults have experienced some level of tooth decay. With regular cleanings, proper home-care, and pro-active treatments, we can protect your tooth structure from attacking plaque and bacteria. Our doctors may recommend dental sealants or fluoride supplements for an extra measure of prevention.",
            "Bad Breath (Halitosis). Bad breath usually stems from poor oral hygiene: patients who don’t floss regularly are especially prone. Oftentimes, bad breath is a sign of early-stage gum disease, so visit our office for an exam and further instruction.",
            "Gum Disease is the number one cause of adult tooth loss. Brushing, flossing, and regular dental exams and cleanings are your best defense. We can also help with screening for oral cancer, alleviating headaches and jaw tension (bruxism/grinding), and preventing sports-related injuries with mouth guards.",
            "Pediatric Care. The ADA recommends that children begin seeing a dentist no later than age one. We also recommend bringing your child with you to your dental visits. At Princeton Smiles Dentistry, we believe that oral health starts early, so we see children as young as three.",
        ],
    },
]


def service_cards(prefix=""):
    cards = []
    for s in SERVICES:
        cards.append(
            f'<a class="card treatment-card" href="{prefix}{s["slug"]}.html"><h3>{s["title"]}</h3><p>{s["lead"]}</p></a>'
        )
    return "\n".join(cards)


def write_index():
    head, foot = chrome(
        "index.html",
        "Princeton Smiles Dentistry | Family Dentist in Princeton, TX",
        "Family and cosmetic dentistry with Dr. Kumar in Princeton, Texas. Call (972) 736-3888.",
        SCHEMA,
    )
    body = f"""
    <section class="hero" id="top">
      <div class="hero-media" role="img" aria-label="Generic stock photo of a modern dental treatment room"></div>
      <div class="hero-scrim" aria-hidden="true"></div>
      <div class="wrap">
        <div class="hero-plate">
          <p class="eyebrow">Princeton, Texas · Since 2005</p>
          <h1>Put your best smile forward with comprehensive dental care from Dr. Kumar and his team.</h1>
          <p class="lede">With advanced training in many areas, Dr. Kumar provides a comprehensive array of services, including dental implant placement and restoration, orthodontics, and cosmetic smile makeovers.</p>
          <div class="actions">
            <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
            <a class="btn btn-ghost" href="services.html">View dental services</a>
          </div>
        </div>
      </div>
    </section>

    <section class="trust-band" id="hours">
      <div class="wrap trust-grid">
        <div>
          <strong>Office</strong>
          <p>{ADDRESS_1}<br>{ADDRESS_2}</p>
        </div>
        <div>
          <strong>Call</strong>
          <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        </div>
        <div>
          <strong>Hours</strong>
          <p>Mon–Thu 8AM–5PM<br>Friday 8AM–12PM · Sat–Sun Closed</p>
        </div>
      </div>
    </section>

    <section id="treatments">
      <div class="wrap">
        <div class="section-head">
          <h2>Treatments</h2>
          <p>As a general and family dental practice dedicated to comprehensive care, we provide services suitable for patients of all ages. From age 4 to 104, patients can find the services they need for optimal oral health and beautiful smiles.</p>
        </div>
        <div class="cards">
          {service_cards()}
        </div>
        <p class="section-cta"><a class="btn btn-dark" href="services.html">View complete list of treatments</a></p>
      </div>
    </section>

    <section id="tech">
      <div class="wrap media-split">
        <img src="assets/comfort-clinical.jpg" alt="Generic stock photo of a clean dental treatment room">
        <div class="prose">
          <div class="section-head">
            <h2>Technology and comfort</h2>
            <p>Dedicated to your optimal oral health, Dr. Kumar and our team strive to develop strong, long-lasting relationships with our patients.</p>
          </div>
          <p>Your comfort always comes first, and we have invested in modern technology to improve your experience. At our office, we feature state-of-the-art diagnostics, including intraoral cameras, digital X-rays, and digital photography.</p>
          <p>At Princeton Smiles, our goal is to provide patients of all ages with quality dental care in a calm and comfortable manner. We are committed to working together with you, no matter what your needs are.</p>
        </div>
      </div>
    </section>

    <section class="reviews" id="testimonials">
      <div class="wrap">
        <div class="section-head">
          <h2>What patients have written</h2>
          <p>These four quotes appear on the published homepage. No extra reviews were added.</p>
        </div>
        <div class="cards two">
          <article class="card review">
            <p>It had been too long since seeing a dentist. I read reviews and made an appointment with Dr. Kumar. I had quite a bit of work done in one visit and it went better than I expected. The 3.5 hour appointment started on time and ended 8 minutes earlier than had planned. Dr Kumar is great with his technique, the shots he gave did not hurt near as bad as other dentists in the past and he kept me informed as he worked on different procedures as to what to expect. The staff he has is awesome. Every person is kind and puts the patient at ease. I have found my new dentist.</p>
            <p><cite>Steve S.</cite> · McKinney, TX</p>
          </article>
          <article class="card review">
            <p>I couldn't have asked for a better experience inspite of the circumstances. Dr Kumar and his staff took care of of me as a walk-in on a day that was for appointments only. I appreciate their professionalism and expertise.</p>
            <p><cite>William K.</cite> · Farmersville, TX</p>
          </article>
          <article class="card review">
            <p>Root Canal's are not anything anyone looks forward to. My tooth was infected and swelling with tremendous pain, and Dr. Kumar and his staff assited me and took tremendous care of me and my tooth. Dr. Kumar is by far the most gentle and caring Dentist I have ever sat under the care of. I am grateful for the caring attentiveness of his staff. They called the following day just to see how I was feeling.</p>
            <p><cite>Rebekah A.</cite> · Princeton, TX</p>
          </article>
          <article class="card review">
            <p>I am so impressed with Princeton Smiles and their staff. They did an awesome job with our first visit. Dr Kumar was so helpful and willing to help me reach the perfect smile I have been looking for. I have gone to other dentists who didn't even want to talk to me about fixing my smile. Thank you Dr Kumar and your staff for being so kind, patient, and caring.</p>
            <p><cite>Leanna M.</cite> · Princeton, TX</p>
          </article>
        </div>
      </div>
    </section>

    <section id="contact">
      <div class="wrap contact-grid">
        <div>
          <div class="section-head">
            <h2>Visit the Princeton office</h2>
            <p>Call first. The preview form on this page stays here and does not email the practice.</p>
          </div>
          <div class="prose">
            <p><strong>Phone:</strong> <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
            <p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
            <p><strong>Address:</strong> {ADDRESS_1}, {ADDRESS_2}</p>
          </div>
          <ul class="hours-list">
            <li><span>Monday–Thursday</span><span>8AM–5PM</span></li>
            <li><span>Friday</span><span>8AM–12PM</span></li>
            <li><span>Saturday–Sunday</span><span>Closed</span></li>
          </ul>
          <iframe class="map-frame" title="Map of Princeton Smiles Dentistry" src="{MAP_SRC}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <form class="card form" id="contact-form" novalidate>
          <p>Send a message, then follow up by phone so the office receives it.</p>
          <p class="form-preview-note">Preview-safe form. It does not email {EMAIL} and does not create an appointment.</p>
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
          <p class="form-status" id="form-status" role="status" tabindex="-1">Thank you. This page does not send messages automatically — please call {PHONE_DISPLAY} so the office receives your request.</p>
        </form>
      </div>
    </section>
"""
    (ROOT / "index.html").write_text(head + body + foot, encoding="utf-8")


def write_services():
    head, foot = chrome(
        "services.html",
        "Dental Services | Princeton Smiles Dentistry",
        "Implants, orthodontics, cosmetic smile makeovers, wisdom teeth, sedation, laser, crowns, fillings, and dentures in Princeton, TX.",
    )
    cards = service_cards()
    body = f"""
    <section class="page-hero">
      <div class="wrap">
        <h1>Dental services</h1>
        <p class="lede">Put your best smile forward. Dr. Kumar’s published care includes implant dentures, braces for teens and adults, and all-porcelain veneers — plus the treatments listed below.</p>
        <div class="actions">
          <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
        </div>
      </div>
    </section>
    <section>
      <div class="wrap">
        <img src="assets/tech-clinical.jpg" alt="Generic stock photo of a dentist reviewing a digital dental X-ray with a patient" class="media-well">
        <div class="prose">
          <p>As a general and family dental practice dedicated to comprehensive care, we provide services suitable for patients of all ages. From age 4 to 104, patients can find the services they need for optimal oral health and beautiful smiles. If you have any questions, please call our Princeton office. Dr. Kumar and our friendly team look forward to meeting you and discovering how we can improve your oral health and your smile.</p>
        </div>
        <div class="cards" style="margin-top:1.6rem">
          {cards}
        </div>
      </div>
    </section>
"""
    (ROOT / "services.html").write_text(head + body + foot, encoding="utf-8")


def write_service_pages():
    for s in SERVICES:
        head, foot = chrome(
            "services.html",
            f"{s['title']} | Princeton Smiles Dentistry",
            f"{s['lead']} Call {PHONE_DISPLAY}.",
        )
        paras = "\n".join(f"          <p>{p}</p>" for p in s["body"])
        others = "".join(
            f'<li><a href="{o["slug"]}.html">{o["title"]}</a></li>'
            for o in SERVICES
            if o["slug"] != s["slug"]
        )
        body = f"""
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow"><a href="services.html">All services</a></p>
        <h1>{s["title"]}</h1>
        <p class="lede">{s["lead"]}</p>
        <div class="actions">
          <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
          <a class="btn btn-ghost" href="services.html">View dental services</a>
        </div>
      </div>
    </section>
    <section>
      <div class="wrap split">
        <div class="prose">
{paras}
        </div>
        <aside class="card">
          <h3>More treatments</h3>
          <ul class="prose">
            {others}
          </ul>
        </aside>
      </div>
    </section>
"""
        (ROOT / f"{s['slug']}.html").write_text(head + body + foot, encoding="utf-8")


def write_new_patients():
    head, foot = chrome(
        "new-patients.html",
        "New Patients | Princeton Smiles Dentistry",
        "New patient visit notes for Princeton Smiles Dentistry. Call (972) 736-3888.",
    )
    body = f"""
    <section class="page-hero">
      <div class="wrap">
        <h1>New patients</h1>
        <p class="lede">At Princeton Smiles, we value the individual needs of our patients and provide a range of dental services to meet those needs.</p>
        <div class="actions">
          <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
        </div>
      </div>
    </section>
    <section>
      <div class="wrap prose">
        <p>Dr. Kumar and our team strive to give you comprehensive care, treating all your dental concerns in one location. Most of all, we want your visit to be relaxing and enjoyable.</p>
        <h2>New patient forms</h2>
        <p>New patient forms can be completed at the office. If you would rather fill them out in our office, we ask that you arrive at least 15 minutes early, which will give us time to prepare your paperwork accordingly. Call {PHONE_DISPLAY} if you have questions before your visit.</p>
        <h2>Insurance options</h2>
        <p>For your convenience, we accept most insurance plans and file all insurance claims in our office. We understand that dental insurance can be confusing, so we do everything in our power to make sure you make an informed decision about your dental health care.</p>
        <h2>Payments</h2>
        <p>We accept American Express, MasterCard, Visa, and Discover. After reviewing your fees beyond insurance, we will create a custom payment tailored to your budget.</p>
        <p class="note">Published “view financing options” and patient-form download links on the live site currently resolve to soft-404 pages, so they are not linked here. Ask the office by phone about current payment arrangements.</p>
      </div>
    </section>
"""
    (ROOT / "new-patients.html").write_text(head + body + foot, encoding="utf-8")


def write_team():
    head, foot = chrome(
        "team.html",
        "Meet Our Team | Princeton Smiles Dentistry",
        "Dr. Vinay Kumar and the Princeton Smiles team. Named in text only — no doctor or staff photos in this preview.",
    )
    body = f"""
    <section class="page-hero">
      <div class="wrap">
        <h1>Meet our team</h1>
        <p class="lede">Published biographies from the live team page. This preview uses names and text only — no doctor photos or staff headshots.</p>
        <div class="actions">
          <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
        </div>
      </div>
    </section>
    <section>
      <div class="wrap cards two">
        <article class="card team-card">
          <h2>Dr. Vinay Kumar</h2>
          <p>Dr. Kumar grew up in Richardson, Texas and attended JJ Pearce High School. Dr. Kumar attended the University of Texas at Dallas for his undergraduate and graduate studies. He completed his dental education at Baylor College of Dentistry in Dallas, Texas.</p>
          <p>Dr. Kumar holds membership with American Dental Association, Texas Dental Association, Dallas County Dental Society, North Texas Dental Society and Academy of General Dentistry. He opened his practice in Princeton, TX in 2011.</p>
          <p>During his free time, Dr. Kumar loves spending time with his wife Alex and their three boys. He also enjoys playing volleyball, watching his boys play sports, traveling and cheering for his favorite Dallas teams.</p>
        </article>
        <article class="card team-card">
          <h2>Dr. Alekhya Patagarla</h2>
          <p>Howdy Y’all!</p>
          <p>I am Alekhya Patagarla DDS MHA, an artist by nature and dentist by profession. In molding the masterpiece of my life chapters, I had to use many bright colors of excellence as well as overcome the muted colors of challenge. Although initially, my career in dentistry started by chance and not by choice, I have come to realize it is a perfect fit and my developing passion is stronger with each new experience I gain.</p>
          <p>I started my early education at a missionary school that helped me build a self-disciplined and focused approach to life. I finished my Bachelor’s in Dental Surgery (BDS) in India and worked for 5 years before moving to the United States. I did my Master of Healthcare Administration (MHA) at Western Kentucky University (WKU), Kentucky where I was recognized for my active participation in community development and welfare programs while serving as a graduate assistant on full scholarship. I then went onto graduate on Dean’s list at the prestigious University of Southern California (USC-Go Trojans) with a DDS degree (Doctor of Dental Surgery).</p>
          <p>I grew up with my grandparents that taught me a lot about being grateful and giving back to the society. I am a passionate human being with skills to serve patients of all ages. My patients call me “Dr. I-LIKE-YA” because I give them comfort and add a tinge of humor to ease their anxiety towards dentistry.</p>
          <p>Fun facts about me, if I am not working I will be playing ping pong with my husband or painting on canvas. I am a professional Indian classical dancer and be ready to dance any form any time 24X7.</p>
        </article>
        <article class="card team-card">
          <h3>Maria (Receptionist)</h3>
          <p>Maria.</p>
        </article>
        <article class="card team-card">
          <h3>Liz (Dental Assistant)</h3>
          <p>Liz</p>
        </article>
        <article class="card team-card">
          <h3>Perla (Registered Dental Assistant)</h3>
          <p>Perla is a certified dental assistant by the Texas State Board of Dental Examiner. She has over 5 years of experience as a dental assistant. She is certified in CPR. Her goal is to make every patient feel comfortable and welcomed at our office. She goes above and beyond in making sure every treatment is tailored to each patient's needs. Outside the office, Perla enjoys spending time with her family, friends and trying food at different restaurants.</p>
        </article>
        <article class="card team-card">
          <h3>Veronica (Registered Dental Assistant)</h3>
          <p>Veronica was born and raised in Austin, Texas. She has been a dental assistant since 2016. She moved to Dallas area in 2017 with her husband. Veronica is always ready to meet and greet patients with a warm smile. She continually strives in excellence in every aspect of her patient care. Her favorite hobbies outside of work are baking and going on long trail rides with her horses. She enjoys watching sunsets after her long rides and caring for her farm animals and her dogs Bella, Chucho, Lobo with her husband. She also enjoys taking short trips to her hometown to visit her parents and siblings.</p>
        </article>
      </div>
    </section>
"""
    (ROOT / "team.html").write_text(head + body + foot, encoding="utf-8")


def write_contact():
    head, foot = chrome(
        "contact.html",
        "Contact | Princeton Smiles Dentistry",
        "Call Princeton Smiles Dentistry at (972) 736-3888. 501 Princeton Dr., Suite 103B, Princeton, Texas 75407.",
    )
    body = f"""
    <section class="page-hero">
      <div class="wrap">
        <h1>Contact us</h1>
        <p class="lede">Phone-first contact for the Princeton office. The form on this page is preview-safe and does not email the practice.</p>
        <div class="actions">
          <a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
        </div>
      </div>
    </section>
    <section>
      <div class="wrap contact-grid">
        <div class="prose">
          <p><strong>Princeton Smiles Dentistry</strong><br>{ADDRESS_1}<br>{ADDRESS_2}</p>
          <p><strong>Phone:</strong> <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
          <p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
          <ul class="hours-list">
            <li><span>Monday–Thursday</span><span>8AM–5PM</span></li>
            <li><span>Friday</span><span>8AM–12PM</span></li>
            <li><span>Saturday–Sunday</span><span>Closed</span></li>
          </ul>
          <iframe class="map-frame" title="Map of Princeton Smiles Dentistry" src="{MAP_SRC}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <form class="card form" id="contact-form" novalidate>
          <p>Send a message, then follow up by phone so the office receives it.</p>
          <p class="form-preview-note">Preview-safe form. It does not email {EMAIL} and does not book an appointment.</p>
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
          <p class="form-status" id="form-status" role="status" tabindex="-1">Thank you. This page does not send messages automatically — please call {PHONE_DISPLAY} so the office receives your request.</p>
        </form>
      </div>
    </section>
"""
    (ROOT / "contact.html").write_text(head + body + foot, encoding="utf-8")


def main():
    write_favicons()
    write_index()
    write_services()
    write_service_pages()
    write_new_patients()
    write_team()
    write_contact()
    print("Wrote Princeton Smiles pages and generic favicons.")


if __name__ == "__main__":
    main()
