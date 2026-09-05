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

## Content / nav parity (HARD GATE)

**Parity status:** FAIL — Practice Areas dropdown (~15 children), Blog, Make a Payment missing; Firm Overview children incomplete.

### Live nav map
- **Home** → `https://www.lonestarlaw.net/`
- **Firm Overview** (dropdown)
  - Len M. Conner → `https://www.lonestarlaw.net/len-m-conner/`
- **Practice Areas** (dropdown)
  - Contested Divorce → `https://www.lonestarlaw.net/contested-divorce/`
  - Uncontested Divorce → `https://www.lonestarlaw.net/uncontested-divorce/`
  - Modifications & Enforcements → `https://www.lonestarlaw.net/modifications-enforcements/`
  - Child Custody → `https://www.lonestarlaw.net/child-custody/`
  - Interstate Visitation → `https://www.lonestarlaw.net/interstate-visitation/`
  - Collaborative Divorce → `https://www.lonestarlaw.net/collaborative-divorce/`
  - Military Divorce → `https://www.lonestarlaw.net/military-divorce/`
  - Termination of Parental Rights → `https://www.lonestarlaw.net/termination-parental-rights/`
  - Stepparent Adoptions → `https://www.lonestarlaw.net/stepparent-adoptions/`
  - Mediation & Arbitration → `https://www.lonestarlaw.net/mediation-arbitration/`
  - Paternity Rights → `https://www.lonestarlaw.net/paternity/`
  - Divorce Myths → `https://www.lonestarlaw.net/divorce-myths/`
  - Marital Property → `https://www.lonestarlaw.net/marital-property/`
  - Domestic Violence → `https://www.lonestarlaw.net/domestic-violence/`
  - Divorce FAQs → `https://www.lonestarlaw.net/divorce-faqs/`
- **Read Our Blog** → `https://www.lonestarlaw.net/read-blog/`
- **Make a Payment** → `https://square.link/u/gfg5dcET`
- **Contact Us** → `https://www.lonestarlaw.net/contact-us/`



### Rebuild nav map (current)
- Home → `index.html`
- Firm & Attorney → `about.html`
- Practice Areas → `practice.html`
- Contact → `contact.html`

### Eng requirement
Restore **full live header IA** (every top item + dropdown children). Collapsing only OK if every destination stays reachable with the **same labels**. Do not strip Financing / service-area / deep service pages into a thin 4–5 link bar.

## Image inventory (Eng must incorporate)

Homepage (and linked gallery/team) assets from live — download into `assets/` and place in matching sections (hero / gallery / team / services). Do not leave pages image-thin vs live.

1. **logo** — `https://www.lonestarlaw.net/wp-content/themes/enterprise/images/logo.jpg` alt="Logo"
2. **logo** — `http://www.lonestarlaw.net/wp-content/uploads/2022/08/BII_winner_logo_22.png`
3. **content** — `http://www.lonestarlaw.net/wp-content/uploads/2022/06/IMG_2788.jpg`
4. **content** — `https://www.lonestarlaw.net/wp-content/uploads/2016/02/attornysimg1.jpg` alt="attornysimg1"
5. **content** — `https://www.lonestarlaw.net/wp-content/plugins/business-reviews-bundle/assets/img/fb_avatar.png` alt="Derek B."
6. **content** — `https://www.lonestarlaw.net/wp-content/themes/enterprise/images/footer-map.jpg` alt="Map Image"
7. **content** — `https://www.lonestarlaw.net/wp-content/themes/enterprise/images/super-badge.jpg` alt="Super badge"
8. **content** — `http://www.lonestarlaw.net/wp-content/uploads/2022/06/len-avvo-rating-reviews.jpeg` alt="Avvo Badge"
9. **content** — `https://www.lonestarlaw.net/wp-content/uploads/2016/02/visaimg.png` alt="visaimg"

Parsed homepage image count (raw): **10**. Also pull gallery/inner-page images when those routes are restored.

## Favicon

- **Live source:** `https://www.lonestarlaw.net/wp-content/themes/enterprise/images/favicon.ico`
- **Local capture:** `/workspace/dfw-design-briefs/favicons/len-conner-law.ico`
- **Note:** Ship this favicon (or logo-derived 32/180) — never invent a new mark.

