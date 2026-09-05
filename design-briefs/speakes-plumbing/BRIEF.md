# Speake's Plumbing — design brief

**Live:** https://www.speakesplumbing.com/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/speakes-plumbing/  
**Shots:** `live-home.png`, `live-hero.png`, `rebuild-home.png`, `rebuild-hero.png`  
**Note:** Headless Chrome initially failed (`ERR_INSUFFICIENT_RESOURCES` / intermittent 403); live shots captured successfully on retry. Colors also confirmed via live HTML (`rgb(122,0,26)`, `#990021`) + PNG sampling.

## 1. Vibe match score
**4 / 10** — Rebuild reads as navy + copper “premium contractor” with Palatino/serif; live is a utilitarian burgundy/maroon Duda plumber site (faucet logo, gray multi-row nav, photo hero with maroon welcome band, sans-serif only).

## 2. Color tokens (sampled from LIVE)
| Token | Hex | Role |
| --- | --- | --- |
| `--bg` | `#f5f5f5` / `#faf9f9` | Page wash / light grid header field |
| `--surface` | `#ffffff` | Panels, cards, body |
| `--ink` | `#333333` | Body copy |
| `--muted` | `#617379` | Secondary labels (“Licensed & Insured”, address) |
| `--brand` | `#7a001a` | Primary burgundy (`rgb(122,0,26)`); logo wordmark, banners |
| `--brand-2` / `--accent` | `#990021` | Buttons, active nav, CTA fills |
| `--nav-bar` | `#888888` | Medium-gray full-width nav strip |
| `--hero-ink` | `#ffffff` | Text on maroon bands / dark hero overlays |
| `--font` | `Open Sans`, system-ui, sans-serif | Body + UI |
| `--font-display` | `Acme`, `Open Sans`, sans-serif | Headings (not Palatino/Georgia) |

Drop scaffold copper `#c47a3a` and navy `#16324f` entirely for this site.

## 3. Layout intent
- **Nav:** Multi-link horizontal bar on medium gray; white link text; active/hover in burgundy. Not a dark sticky “executive” header.
- **Header chrome:** Light grid background; left logo + wordmark + address/license; center trust line + “Leave Us A Review”; right “Free Estimates by Phone” + large black tel.
- **Hero:** Full-bleed plumbing photo (pipes/wrench) with solid maroon bottom band: “Welcome to Speake's Plumbing, Inc.” — not a two-column dark dotted hero + shop card.
- **Density:** Medium; clear horizontal section bands (white body / maroon testimonial header / gray footer / maroon legal bar). Practical service-business, not spa/premium.
- **Typography:** All sans; bold for name + phone; no display serif.

## 4. Concrete CSS/HTML change list (Engineering)
1. **`theme.css`:** Set `--brand:#7a001a`, `--brand-2:#990021`, `--accent:#990021`, `--bg:#faf9f9`, `--surface:#ffffff`, `--ink:#333333`, `--muted:#617379`, `--hero-ink:#ffffff`. Remove navy/copper values.
2. **`theme.css` / `styles.css`:** Change `--font-display` to `Acme, "Open Sans", system-ui, sans-serif` (or Open Sans only if Acme not loaded). Drop Palatino.
3. **Header:** Remove or override `.theme-dark-header` so `.site-header` is light (`--surface` / `#f5f5f5`) with burgundy text; add optional light grid if cheap (`background-image` faint squares) — do not invent a new brand mark.
4. **Nav:** Restyle nav strip to gray `#888888` with white links and burgundy active; keep existing logo `assets/logo.png` only.
5. **Buttons:** `.btn-primary` / header call CTA → burgundy fill `#990021`, white text; remove orange primary.
6. **Hero (`index.html` + CSS):** Prefer photo-backed hero (use existing live-style plumbing photo if in assets) + maroon welcome band; shrink/remove radial dot pattern and “Call the shop” glass panel, or restyle panel to white/light with burgundy accents so it doesn’t read hotel.
7. **Footer:** Gray upper + thin maroon legal bar to echo live banding (colors only — keep real contact content).
8. **Do not** invent a new logo, copper accents, or serif “authority” look.

## 5. 508-relevant design risks
- **Contrast:** White on `#888888` nav may fail WCAG AA for small text — darken nav to ~`#5a5a5a` or use darker link treatment if keeping gray.
- **Contrast:** Burgundy `#7a001a` / `#990021` on white for body links/buttons should be checked (≥4.5:1); white on burgundy for large CTAs usually OK.
- **Focus:** Scaffold gold/outline focus can disappear on burgundy/gray — use high-contrast focus ring (e.g. 2px white + dark outline).
- **Alt text:** Keep descriptive alt on faucet logo; hero pipe photo needs meaningful alt (not empty).
- **Heading order:** Single `h1` in hero; section titles `h2`; service cards `h3` — no skips.
- **Skip link:** Present in rebuild — verify visible on keyboard focus against light header.
- **Forms (contact):** Visible `<label>` per input; errors not color-only.

## 6. What already matches (keep)
- Real Speake content: address, (972) 271-9144, Master Plumber Lic #16836, since-1987 story, published service list, published testimonials only (no lorem).
- Existing logo asset only (do not replace).
- Skip link, `tel:` CTAs, sell-as-is multi-page structure (About / Services / Testimonials / Contact).
- Card grid for services + testimonial quotes already useful — just recolor and densify toward live utilitarian vibe.


---

## Content / nav parity (HARD GATE)

**Parity status:** EXEMPLAR FAIL — live ~11 top items + Service Areas dropdown (4 children) + Blog; rebuild only Home/About/Services/Testimonials/Contact. Financing, Residential, Commercial, Water Heaters, Products, Service Areas pages, and Blog are missing destinations.

### Live nav map
- **Home** → `https://www.speakesplumbing.com/`
- **About Us** → `https://www.speakesplumbing.com/about-us`
- **Financing** → `https://www.speakesplumbing.com/financing`
- **Residential** → `https://www.speakesplumbing.com/residential`
- **Commercial** → `https://www.speakesplumbing.com/commercial`
- **Water Heaters** → `https://www.speakesplumbing.com/water-heaters`
- **Products** → `https://www.speakesplumbing.com/products`
- **Testimonials** → `https://www.speakesplumbing.com/testimonials`
- **Contact Us** → `https://www.speakesplumbing.com/contact-us`
- **Service Areas** (dropdown)
  - Garland, TX — Hot Water Heater Repair → `https://www.speakesplumbing.com/hot-water-heater-repair-garland-tx`
  - Garland, TX — Plumbers → `https://www.speakesplumbing.com/plumbers-garland-tx`
  - Richardson, TX — Hot Water Heater Repair → `https://www.speakesplumbing.com/hot-water-heater-repair-richardson-tx`
  - Richardson, TX — Plumbers Serving Richardson → `https://www.speakesplumbing.com/plumbers-serving-richardson-tx`
- **Blog** → `https://www.speakesplumbing.com/blog`



### Rebuild nav map (current)
- Home → `index.html`
- About Us → `about.html`
- Services → `services.html`
- Testimonials → `testimonials.html`
- Contact → `contact.html`

### Eng requirement
Restore **full live header IA** (every top item + dropdown children). Collapsing only OK if every destination stays reachable with the **same labels**. Do not strip Financing / service-area / deep service pages into a thin 4–5 link bar.

## Image inventory (Eng must incorporate)

Homepage (and linked gallery/team) assets from live — download into `assets/` and place in matching sections (hero / gallery / team / services). Do not leave pages image-thin vs live.

1. **content** — `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/077-162h.png` alt="Speake"
2. **hero/banner** — `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/839-1920w.jpg` alt="Grant Speak next to van - Plumbing in Garland, TX"
3. **hero/banner** — `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/839-486w.jpg` alt="Grant Speak next to van - Plumbing in Garland, TX"
4. **content** — `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/511-81bc6217-24w.png`
5. **content** — `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/11782db-1920w.png`
6. **content** — `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/84182db-1920w.jpg`
7. **content** — `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/74782db-0fba6051-1920w.jpg`

Parsed homepage image count (raw): **9**. Also pull gallery/inner-page images when those routes are restored.

## Favicon

- **Live source:** `https://irp.cdn-website.com/07f850f089c4441eb0eefb4dceb83ed0/site_favicon_16_1619588441097.ico`
- **Local capture:** `/workspace/dfw-design-briefs/favicons/speakes-plumbing.ico`
- **Note:** Ship this favicon (or logo-derived 32/180) — never invent a new mark.

