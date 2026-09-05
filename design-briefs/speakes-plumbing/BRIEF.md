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

## Content / nav / image / favicon parity (Scout fold — authoritative)

_Folded from `/workspace/dfw-parity/speakes-plumbing.md` (Scout public HTML inventory, 2026-09-05). Supersedes thinner lists for Eng._

## speakes-plumbing

Source: https://www.speakesplumbing.com/ (public homepage HTML via curl + WebFetch, 2026-09-05). URLs below are copied as present in live markup (including `cdn-website.com//` double-slash paths).

### Primary nav (with dropdown children)

Header `<nav class="u_1322900430 … main-navigation unifiednav">` — **11 top-level items** in order:

1. **Home** → `/`
2. **About Us** → `/about-us`
3. **Financing** → `/financing` *(angle-down icon present; no submenu children in HTML)*
4. **Residential** → `/residential`
5. **Commercial** → `/commercial`
6. **Water Heaters** → `/water-heaters`
7. **Products** → `/products`
8. **Testimonials** → `/testimonials`
9. **Contact Us** → `/contact-us`
10. **Service Areas** → `#` *(has submenu; `aria-haspopup="true"`)*
    - **Garland, TX** → `#` *(nested submenu)*
      - **Hot Water Heater Repair Garland, TX** → `/hot-water-heater-repair-garland-tx`
      - **Plumbers in Garland, TX** → `/plumbers-garland-tx`
    - **Richardson, TX** → `#` *(nested submenu)*
      - **Hot Water Heater Repair  Richardson, TX** → `/hot-water-heater-repair-richardson-tx` *(label has two spaces before “Richardson” in live `data-link-text`)*
      - **Plumbers Serving Richardson** → `/plumbers-serving-richardson-tx`
11. **Blog** → `/blog` *(angle-down icon present; no submenu children in HTML)*

**Footer nav:** Distinct footer `<nav class="u_1961877140 …">` (`hide-for-small hide-for-medium`) duplicates the **same 11 labels, hrefs, and Service Areas nested children** as the header (pipe dividers via `data-divider="PIPE"`). Not a separate service-area-only footer menu.

**Parity note:** Live header = **11** top-level items. Site JS `Parameters.NavigationAreaParams.NavbarSize` = **5** (matches flagged “~11 header items vs rebuild 5”).

### Key images / heroes

| Role | Absolute URL | Notes from live HTML |
| --- | --- | --- |
| **Logo** | `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/077-162h.png` | Header `img`; alt/title `Speake's Plumbing, Inc.`; `data-dm-image-path` → `https://cdn.website.thryv.com/07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/077.png` |
| **Hero / banner slides (gallery-bg)** | `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/84182db-1920w.jpg` | First of 3 slides in base64 `data-gallery-bg` on hero rows (`u_1250640656` / `u_1992283242`); also CSS `background-image` on those rows |
| | `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/842-1920w.jpg` | Hero gallery slide 2 (`data-gallery-bg`) |
| | `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/843-1920w.jpg` | Hero gallery slide 3 (`data-gallery-bg`) |
| **About / team photo** | `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/839-1920w.jpg` | `img` alt: `Grant Speak next to van - Plumbing in Garland, TX` (also `839-486w.jpg` responsive variant of same asset) |
| **Mid-page parallax / CTA band** | `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/74882db-472838cf-1920w.jpg` | `data-background-image` on row with “Proudly serving Garland…” copy |
| **Testimonials / lower parallax band** | `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/74782db-0fba6051-1920w.jpg` | `data-background-image` + CSS on parallax rows (`u_1831147509`, `u_1013970563`, etc.) |
| **Header/footer texture** | `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/11782db-1920w.png` | Header top bar CSS bg; footer row `data-background-image` |
| **Homepage video (no poster)** | `https://videos.dexmedia.com/MP41280x720/950.0015316243_A.mp4` | `<video controls autoplay>` custom HTML; **no `poster` attribute**. Extra fallback source in markup: `https://www.quirksmode.org/html5/videos/big_buck_bunny.webmwe` |

**Not found on homepage as dedicated assets:** separate service-card images; photo gallery notables beyond hero slides / team photo; video poster image.

### Favicon

- **apple-touch-icon:** `https://irp.cdn-website.com/07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/077.png`
- **icon (x-icon):** `https://irp.cdn-website.com/07f850f089c4441eb0eefb4dceb83ed0/site_favicon_16_1619588441097.ico`

No `rel="shortcut icon"` link found in homepage HTML.

### Capture notes

- Platform: Duda / Thryv (`irp.cdn-website.com`, SiteAlias `07f850f089c4441eb0eefb4dceb83ed0`).
- Captured from public homepage HTML only (`curl -sL` + WebFetch). No invented labels or URLs.
- Primary nav labels taken from `data-link-text` / visible nav text inside header `unifiednav`.
- Only **Service Areas** has real dropdown children in the DOM; Financing/Blog show decorative `icon-angle-down` without child `<ul>`.
- Many CDN paths use a literal double slash after the host (`…com//07f850…`); reported as in source.
- Tiny footer share-related `img` also present: `https://irp.cdn-website.com//07f850f089c4441eb0eefb4dceb83ed0/dms3rep/multi/opt/511-81bc6217-24w.png` (20×20; not a hero/brand asset).


### Parity emphasis (exemplar)
- **11 top-level** items; only Service Areas has real nested children (Garland + Richardson, 2 each).
- Eng must ship hero gallery slides 84182db / 842 / 843 + Grant-at-van photo + parallax bands — not logo-only.
- Homepage video URL present; **no poster** — do not invent poster art.
- Favicon: live `.ico` + apple-touch from `077.png`.


