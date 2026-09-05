# B&B Complete Auto Repair — design brief

**Live:** https://bbcompleteautorepair.com/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/bb-complete-auto/  
**Shots:** `live-home.png`, `live-hero.png`, `rebuild-home.png`, `rebuild-hero.png`  
**Vibe match: 5/10** — Red + charcoal family is right, but live is a **centered-logo WordPress shop** (white header → dark nav strip → photo hero of the bay). Rebuild is a **modern left-logo scaffold** with carbon-fiber dark hero, red radial glow, and “Book the bay” KPI panel — reads agency/premium, not LinkNow/gbm auto shop.

## Color tokens (LIVE — from theme CSS + screenshots)
| Token | Hex | Notes |
| --- | --- | --- |
| `--brand` | `#202020` / `#393939` | Dark nav / phone chip |
| `--brand-2` / `--accent` | `#ee0101` | Live theme red (also `#c00`); logo mark is vivid red |
| Support blue | `#3279BB` | Theme link/utility blue — optional secondary only |
| `--ink` | `#1b1b1b` / `#333333` | Body |
| `--muted` | `#5c5854` | Tagline under logo |
| `--bg` | `#f1eeea` / light gray | Content wash below hero |
| `--surface` | `#ffffff` | Header / cards |
| `--hero-ink` | `#ffffff` | On dark overlays |
| `--font-display` | `Michroma, "Open Sans", system-ui, sans-serif` | Live loads Michroma + Open Sans — not display serif |

Current rebuild `theme.css` uses `#c1121f` — close; **prefer `#ee0101`** to match live CTA/theme red.

## Layout intent
- **Live pattern:** Social icons (L) · **centered checkered-flag logo** · phone chip (R) → full-width **charcoal nav** (Home / About / Auto Repair Services / F.A.Q. / Gallery / Contact / Service Areas) → **full-bleed shop exterior photo** (cars in bays) with heavy dark wash.
- **Not** a two-column “Book the bay” glass card on carbon fiber.
- Density: practical services list + trust bullets; empty Gallery stays empty; Elfsight reviews widget only.
- Phone always loud: `(214) 994-6989`. License **CO16-0388**.

## Eng change list
1. **Unify accent** to live `#ee0101` (drop competing reds `#c1121f` / WP preset `#cf2e2e` in UI chrome).
2. **Hero treatment:** prefer shop photo + dark wash (live) over diagonal carbon pattern + red radial; if keeping scaffold hero, mute the glow and flatten texture.
3. **Header chrome:** live is centered logo + dark nav bar; rebuild sticky white left-logo is fine for sell-as-is scaffold but pull visual weight toward shop-photo energy, not boutique auto.
4. Soften “Book the bay” panel (or restyle as simple contact strip) so it doesn’t dominate.
5. Service cards: denser, mechanic-practical — less boutique padding.
6. Fonts: Michroma/Open Sans stack for display/body proximity to live; keep sans, no Georgia.
7. IA: keep Gallery + Areas + FAQ; no invented review stars in HTML — Elfsight only if used.
8. **Keep published logo** (`assets/logo.png` / live checkered-flag mark) — do not redraw wordmark.

## Keep
- Checkered-flag + red **B&B** logo asset only.
- Real services, address `2206 South Shiloh Road, Garland, TX 75041`, Mon–Sat 8–6, license CO16-0388.
- Skip link, `tel:` CTAs, empty gallery honesty, no fake reviews.

## 508 notes
- White on `#ee0101` for primary buttons; verify ≥4.5:1.
- Red links on white: darken to ~`#b80000` for small body text if `#ee0101` fails.
- Charcoal nav: white text OK; ensure focus ring visible on dark bar (light outline).
- Hero photo: descriptive `alt` (shop exterior / vehicles in bays) — not empty if informative.
- Heading order: one `h1`; services as `h2`/`h3`.
- Contact form: visible labels; errors not color-only.


---

## Content / nav / image / favicon parity (Scout fold — authoritative)

_Folded from `/workspace/dfw-parity/bb-complete-auto.md` (Scout public HTML inventory, 2026-09-05). Supersedes thinner lists for Eng._

# CONTENT PARITY — bb-complete-auto

**Live source:** https://bbcompleteautorepair.com/  
**Fetched:** 2026-09-05 (HTTPS 200; public homepage HTML only)  
**Page title:** B&B Complete Auto Repair | Contact Us Now  
**Notes:** No invented URLs or labels.

---

## 1. Primary navigation (+ dropdown children)

Source: homepage `<nav>` page-list menu (Foundation top-bar).

| Label | Absolute URL | Dropdown children |
|-------|--------------|-------------------|
| Home | https://bbcompleteautorepair.com/home/ | *(none)* |
| About | https://bbcompleteautorepair.com/about-us/ | *(none)* |
| Auto Repair Services | https://bbcompleteautorepair.com/auto-repair-services/ | **see below** |
| F.A.Q. | https://bbcompleteautorepair.com/faq/ | *(none)* |
| Gallery | https://bbcompleteautorepair.com/gallery/ | *(none)* |
| Contact | https://bbcompleteautorepair.com/contact-us/ | *(none)* |
| Service Areas | https://bbcompleteautorepair.com/service-areas/ | *(none)* |

**Dropdown — Auto Repair Services** (`page_item_has_children` / nested `<ul>`):

| Child label | Absolute URL |
|-------------|--------------|
| Auto Glass | https://bbcompleteautorepair.com/auto-repair-services/auto-glass/ |
| German Auto Repair | https://bbcompleteautorepair.com/auto-repair-services/german-auto-repair/ |
| Brake Services | https://bbcompleteautorepair.com/auto-repair-services/brake-services/ |
| Collision Repair | https://bbcompleteautorepair.com/auto-repair-services/collision-repair/ |
| Engine Repair | https://bbcompleteautorepair.com/auto-repair-services/engine-repair/ |
| Exhaust Repair | https://bbcompleteautorepair.com/auto-repair-services/exhaust-repair/ |
| Oil Change | https://bbcompleteautorepair.com/auto-repair-services/oil-change/ |
| Radiator Repair and Inspection | https://bbcompleteautorepair.com/auto-repair-services/radiator-repair-and-inspection/ |
| Auto Diagnostics | https://bbcompleteautorepair.com/auto-repair-services/auto-diagnostics/ |
| Tire Rotation and Alignment | https://bbcompleteautorepair.com/auto-repair-services/tire-rotation-and-alignment/ |
| Tire Services | https://bbcompleteautorepair.com/auto-repair-services/tire-services/ |
| Transmission Service | https://bbcompleteautorepair.com/auto-repair-services/transmission-service/ |

**Header chrome (not primary nav items):** Facebook, Instagram, Google Maps place link, phone `tel:+12149946989` → (214) 994-6989.

---

## 2. Key live images / heroes (absolute URLs)

### Logo (header)
- https://bbcompleteautorepair.com/wp-content/uploads/sites/515/2022/04/logo.png  
  *(alt: B&B Complete Auto Repair)*

### Hero / location image (header)
- https://bbcompleteautorepair.com/wp-content/uploads/sites/515/2022/03/home-bg.jpg  
  *(alt: B&B Complete Auto Repair Location)*

### Homepage section images (theme)
- https://bbcompleteautorepair.com/wp-content/themes/gbm/images/home-01.jpg
- https://bbcompleteautorepair.com/wp-content/themes/gbm/images/home-02.jpg

### Google review badge
- https://bbcompleteautorepair.com/wp-content/uploads/sites/515/2025/11/review-w.png  
  *(alt: Leave A Google Review)*

### Footer host logo (present on page; third-party)
- https://linknow.com/linknow_images/linknow-logo-white.png  
  *(alt: Website Hosted By LinkNow™ Media)*

---

## 3. Favicon URL(s)

**None declared** in homepage `<head>` (no `rel="icon"`, `shortcut icon`, or `apple-touch-icon` links).

Probes from this inventory pass:
- `https://bbcompleteautorepair.com/favicon.ico` → **HTTP 404**
- `https://bbcompleteautorepair.com/favicon.png` → **HTTP 404**
- `https://bbcompleteautorepair.com/apple-touch-icon.png` → **HTTP 404**



### Parity emphasis
- **Auto Repair Services** dropdown = **12 children** (restore all).
- Gallery + Service Areas are top-level — rebuild must not drop Gallery.
- Favicon: none on live — **derive from** `…/logo.png` (local `favicons/bb-complete-auto.png`). Never invent a mark.


