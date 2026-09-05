# Law Office of Len Conner — design brief

**Live:** https://www.lonestarlaw.net/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/len-conner-law/  
**Vibe match: 4/10** — Rebuild invented navy/gold “prestige firm.” Live is **maroon `#77080a`** chrome (nav bar, CTAs, logo type), **white header**, **beach family photo hero** with maroon headline. Standing rule: match live — do **not** keep navy/gold as primary.

## Color tokens (LIVE — use these)
| Token | Hex |
| --- | --- |
| `--brand` | `#77080a` |
| Logo maroon | keep in `assets/logo.jpg` (don’t recolor mark) |
| Badge gold | `#ffbe01` / `#f3ae05` — Super Lawyers / Best in Irving **only** |
| Badge blue | award seals only |
| `--ink` | `#333333` |
| `--muted` | `#666666` |
| `--bg` | `#f5f5f5` / cream |
| `--surface` | `#ffffff` |
| `--hero-ink` | `#77080a` on light photo (or white if overlay darkens) |
| `--font-display` | serif for firm name/headings; sans for nav/CTAs |

## Layout intent
- Traditional family-law site: white header + diamond LC logo + phone, full-width maroon nav, lifestyle beach hero, practice copy, trust badges, five homepage testimonials only.
- Phone `972-445-1500` everywhere it matters.
- No public email/hours invent. `/testimonials/` 404 — don’t add fake page.

## Eng change list
1. `theme.css`: `--brand` → `#77080a`; drop navy `#0f2744` as primary; gold only on badges/eyebrows.
2. Header: white bar; maroon phone; maroon nav strip with white links (scaffold needs a maroon-nav modifier).
3. Hero: beach/family photo underlay (published asset if available) + maroon headline/CTA — not solid navy wash.
4. `.btn-primary` → maroon fill, white text.
5. Keep five quotes (Marie, Marc and Jill, David, Dena, Kelly); keep badge images with alts.
6. Strip any “404” meta/debug copy if present.

## Keep
- Cities served; Irving address; logo; badges; homepage quotes only.

## 508 notes
- Maroon `#77080a` on white: verify body links ≥4.5:1 (darken if needed).
- Maroon nav + white links: OK if ≥4.5:1.
- Hero maroon on beach photo: ensure overlay/shadow for contrast.
- Badge `alt` includes award name + year.
- Form labels; focus visible on maroon controls (light ring).


---

## Content / nav / image / favicon parity (Scout fold — authoritative)

_Folded from `/workspace/dfw-parity/len-conner-law.md` (Scout public HTML inventory, 2026-09-05). Supersedes thinner nav/image lists above for Eng._

## len-conner-law

Source: https://www.lonestarlaw.net/ (public homepage HTML via curl, 2026-09-05). URLs below are copied as present in live markup (including `http://` vs `https://` as served). Never invented.

**Live title:** Attorney Len Conner - Irving, Dallas County Divorce & Family Law

### Primary nav (with dropdown children)

Header `#nav` → `<ul id="menu-top-menu" class="menu genesis-nav-menu menu-primary">` (Genesis / WordPress):

1. **Home** → `/` *(absolute: `https://www.lonestarlaw.net/`)*
2. **Firm Overview** → `https://www.lonestarlaw.net/firm-overview/`
   - **Len M. Conner** → `https://www.lonestarlaw.net/len-m-conner/`
3. **Practice Areas** → `https://www.lonestarlaw.net/practice-areas/`
   - **Contested Divorce** → `https://www.lonestarlaw.net/contested-divorce/`
   - **Uncontested Divorce** → `https://www.lonestarlaw.net/uncontested-divorce/`
   - **Modifications & Enforcements** → `https://www.lonestarlaw.net/modifications-enforcements/` *(label entity `&#038;` in HTML)*
   - **Child Support** → `https://www.lonestarlaw.net/child-support/`
   - **Child Custody** → `https://www.lonestarlaw.net/child-custody/`
   - **Interstate Visitation** → `https://www.lonestarlaw.net/interstate-visitation/`
   - **Collaborative Divorce** → `https://www.lonestarlaw.net/collaborative-divorce/`
   - **Military Divorce** → `https://www.lonestarlaw.net/military-divorce/`
   - **Termination of Parental Rights** → `https://www.lonestarlaw.net/termination-parental-rights/`
   - **Stepparent Adoptions** → `https://www.lonestarlaw.net/stepparent-adoptions/`
   - **Mediation & Arbitration** → `https://www.lonestarlaw.net/mediation-arbitration/` *(label entity `&#038;` in HTML)*
   - **Paternity Rights** → `https://www.lonestarlaw.net/paternity/`
   - **Divorce Myths** → `https://www.lonestarlaw.net/divorce-myths/`
   - **Marital Property** → `https://www.lonestarlaw.net/marital-property/`
   - **Domestic Violence** → `https://www.lonestarlaw.net/domestic-violence/`
   - **Divorce FAQs** → `https://www.lonestarlaw.net/divorce-faqs/`
   - **Criminal Law in Divorce** → `https://www.lonestarlaw.net/criminal-law-divorce/`
   - **Grandparents’ Rights** → `https://www.lonestarlaw.net/grandparents-rights/`
   - **Fathers’ Rights** → `https://www.lonestarlaw.net/fathers-rights/`
   - **Legal Glossary** → `https://www.lonestarlaw.net/legal-glossary/`
4. **Read Our Blog** → `https://www.lonestarlaw.net/read-blog/`
5. **Make a Payment** → `https://square.link/u/gfg5dcET`
6. **Contact Us** → `https://www.lonestarlaw.net/contact-us/`

### Key images / heroes

| Role | Absolute URL | Notes from live HTML |
| --- | --- | --- |
| **Header / chat logo** | `https://www.lonestarlaw.net/wp-content/themes/enterprise/images/logo.jpg` | Theme logo `img` (header + chat pop) |
| **Hero Master Slider slide 1** | `https://www.lonestarlaw.net/wp-content/uploads/2016/03/banner-main.jpg` | `ms-slide` `data-src`; overlay title “Divorce & Family Law” |
| **Hero Master Slider slide 2** | `https://www.lonestarlaw.net/wp-content/uploads/2016/03/banner-main3.jpg` | Overlay title “Child Custody” |
| **Hero Master Slider slide 3** | `https://www.lonestarlaw.net/wp-content/uploads/2016/03/banner4.jpg` | Overlay title “Military Divorce Issues” |
| **Best of Irving badge** | `http://www.lonestarlaw.net/wp-content/uploads/2022/08/BII_winner_logo_22.png` | `img.alignright` width 150px (scheme `http` as in markup) |
| **Homepage content photo** | `http://www.lonestarlaw.net/wp-content/uploads/2022/06/IMG_2788.jpg` | Text widget `img` (scheme `http` as in markup) |
| **Attorney block photo** | `https://www.lonestarlaw.net/wp-content/uploads/2016/02/attornysimg1.jpg` | alt `attornysimg1` |
| **Footer map thumbnail** | `https://www.lonestarlaw.net/wp-content/themes/enterprise/images/footer-map.jpg` | alt `Map Image` |
| **Super Lawyers / Super badge** | `https://www.lonestarlaw.net/wp-content/themes/enterprise/images/super-badge.jpg` | alt `Super badge` |
| **Avvo badge** | `http://www.lonestarlaw.net/wp-content/uploads/2022/06/len-avvo-rating-reviews.jpeg` | alt `Avvo Badge`; width 200 (scheme `http` as in markup) |
| **Visa / payment mark** | `https://www.lonestarlaw.net/wp-content/uploads/2016/02/visaimg.png` | alt `visaimg` |

**Not brand/hero (plugin placeholders):** Master Slider `blank.gif` at `https://www.lonestarlaw.net/wp-content/plugins/master-slider/public/assets/css/blank.gif`; review avatars `…/business-reviews-bundle/assets/img/fb_avatar.png`.

### Favicon

- **icon:** `https://www.lonestarlaw.net/wp-content/themes/enterprise/images/favicon.ico` (`<link rel="icon" …>`)

No apple-touch-icon link found in homepage HTML.

### Capture notes

- Platform: WordPress + Genesis child theme `enterprise`; hero via Master Slider plugin.
- Captured from public homepage HTML only. No invented labels or URLs.
- Practice Areas submenu is the large dropdown (20 children); Firm Overview has one child (Len M. Conner).
- Some content image `src` attributes remain `http://www.lonestarlaw.net/…` in the live HTML; reported verbatim.


### Parity emphasis
- **Practice Areas dropdown = 20 children** (incl. Child Support, Criminal Law in Divorce, Grandparents’ Rights, Fathers’ Rights, Legal Glossary — not only the first 15).
- Firm Overview child: Len M. Conner.
- Also restore **Read Our Blog** + **Make a Payment** (Square link).


