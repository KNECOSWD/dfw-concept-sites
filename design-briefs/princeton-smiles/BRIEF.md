# Princeton Smiles Dentistry — independent sales unit

**Live:** https://princetonsmiles.com/  
**Do not confuse with** NJ `princetonsmile.com`.  
**Rebuild:** `sites/princeton-smiles/` · GitHub Pages static · **$500** offer path  
**Offer / unit:** Independent KNECO sales preview. Not one of the original ten DFW parity sites.

## Hard locks (this preview)

1. **Generic media only.** Header uses a **generic SVG wordmark** + generic teal tooth favicon (`assets/wordmark.svg`, `assets/favicon.svg`, generated PNGs). Hero and section photos are **Unsplash stock clinical interiors** (`hero-clinical.jpg`, `comfort-clinical.jpg`, `tech-clinical.jpg`). **No live logo, no Dr. Kumar photo, no staff headshots, no live favicon.** Customer marks are a hard FAIL until approval.
2. **Preview-safe contact form.** `preventDefault` on-page confirmation only. Does **not** POST or mailto `princetonsmiles@gmail.com`. Email is display-only. No appointment / CareCredit / payment transaction.
3. **Exp 3 chrome.** Sticky finished header. Hero has a **full-bleed light scrim** plus a **white plate under the full heading bounds** (eyebrow + H1 + lede + actions). Primary CTA is **Call (972) 736-3888** only — no Schedule / appointment pile-up. Secondary: View dental services + contact form.
4. **No soft-404 nav.** Live traps (HTTP 200 blog-fallback) are **not** linked: `/about/` `/blog/` `/meet-dr-kumar/` `/financing/` `/testimonials/` `/appointment/` `/gallery/` `/patient-financing/` `/view-financing-options/` `/financing-options/` `/payments-and-financing/` `/patient-forms/` `/carecredit/` `/payment-options/`. Hard 404s also omitted: `/new-patients/financing/` `/services/oral-surgery/`. `/sitemap.xml` is 500 — unused.
5. **No AggregateRating / invented reviews.** Homepage quotes only: Steve S. (McKinney), William K. (Farmersville), Rebekah A. (Princeton), Leanna M. (Princeton). Schema is `Dentist` + NAP/hours only.
6. **Wylie FLAG.** Live `/contact/` emergency copy tells people to “call or visit our **Wylie** dental practice.” That is a NAP conflict with Princeton. **Choice:** omit the emergency blurb entirely; do not invent a Princeton emergency policy. Phone-first contact + published hours only. Live `/services/` “call our Wylie office” neutralized to **Princeton office**.
7. Responsive; local assets; no lorem; no oral-surgery or financing vanity pages; published service capability kept on real destinations.
8. **$0 Azure.** Static GitHub Pages only.

## Nav (working destinations only)

| Label | File | Live counterpart |
| --- | --- | --- |
| Home | `index.html` | `/` |
| Services | `services.html` + 15 published service pages | `/services/` and working `/services/<slug>/` |
| New Patients | `new-patients.html` | `/new-patients/` (forms/financing links stripped — those targets are soft-404) |
| Team | `team.html` | `/team/` (text bios; no photos) |
| Contact | `contact.html` | `/contact/` |

Not in nav: Blog (`/updates/` exists; `/blog/` is a soft-404), About, Meet Dr. Kumar, Gallery, Appointment, Testimonials page, Financing tree.

## Vault / published facts

- **Practice:** Princeton Smiles Dentistry; Dr. Kumar named in text (opened Princeton practice **2011** on the team page). Footer line **Since 2005** is published on the live site.
- **NAP:** 501 Princeton Dr., Suite 103B, Princeton, Texas 75407 · (972) 736-3888 · princetonsmiles@gmail.com
- **Hours:** Mon–Thu 8AM–5PM; Friday 8AM–12PM; Sat–Sun Closed
- **Towns:** Farmersville, Blue Ridge, New Hope, Merit
- **Tech:** intraoral cameras, digital X-rays, digital photography
- **Services (no capability loss):** implant placement/restoration, orthodontics / ClearCorrect, cosmetic smile makeovers / veneers / whitening, wisdom teeth, sedation (nitrous / oral / IV), laser, porcelain crowns, crown & bridge, tooth-colored fillings, dentures/partials, root canals, general & family dentistry
- **Facebook (published):** http://www.facebook.com/pages/Princeton-Smiles/120125238064542

## Color

| Token | Hex | Notes |
| --- | --- | --- |
| Proposed brand | `#1B7A8F` | Clinical teal |
| Call / deep brand | `#0F4C5C` | Primary buttons |
| Live sample | `#db6159` | Coral accent on live homepage (`style="color: #db6159"`). CF allowed a fetch. **This redesign ships proposed teal**, not live coral. |
| Call contrast | White on `#0F4C5C` | Passes WCAG 2.2 AA (normal text). `#1B7A8F` on white is ~5:1 — used for large accents, not small body text. Body links use `#0F4C5C`. |

## Sketch layout

Sticky chrome → hero (stock + scrim + plate + Call) → trust/hours/NAP → treatments grid → tech/comfort → four published testimonials → contact (safe form + map + hours) → footer.

## Media inventory (generic only)

| File | Source | Role |
| --- | --- | --- |
| `wordmark.svg` | Drawn here | Generic text wordmark + tooth mark |
| `favicon.svg` / PNGs | Drawn here | Generic favicon |
| `hero-clinical.jpg` | Unsplash `photo-1629909613654-28e377c37b09` | Hero operatory (no people) |
| `comfort-clinical.jpg` | Unsplash `photo-1598256989800-fe5f95da9787` | Tech/comfort band |
| `tech-clinical.jpg` | Unsplash `photo-1606811841689-23dfddce3e95` | Services stock (generic clinician + digital X-ray — **not** a customer photo) |

**Not shipped:** live `Vinay-Kumar-Dentist-Princeton.png`, live logo, live favicon, `Wylie-Village-Dentistry-1.jpg` (live porcelain-crowns tile).

## 508

- Skip link; `:focus-visible`; 44×44 targets; labeled form; errors not color-only
- Mobile header Call hidden so the wordmark is not crowded (Exp 3); sticky callbar keeps Call
- No dark type on the hero photo — plate + scrim
- Map iframe has a title
