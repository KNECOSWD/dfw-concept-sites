# Garden Restaurant — design brief

**Live:** https://gardenrestaurantgarland.com/  
**Rebuild:** https://knecoswd.github.io/dfw-concept-sites/sites/garden-restaurant/  
**Vibe match: 8/10** — Sell-as-is target is **warm red/gold Chinese restaurant**. Rebuild already uses deep banquet red `#8b1e1e` + gold accents on a cream page — correct family. Live Zing theme is teal `#18A687` CTAs + gold `#B8A51C` on a dark food-photo hero (not red). Do **not** retune rebuild to teal; keep red/gold and borrow live’s food-photo / Order CTA energy.

## Color tokens (LIVE — reference only)
| Token | Hex | Notes |
| --- | --- | --- |
| `--brand` (live CTA) | `#18A687` | Teal Order buttons — **do not adopt as rebuild primary** |
| `--brand-2` / gold | `#B8A51C` | Live secondary / theme `bg_color` |
| `--ink` | `#343a40` / `#334152` | Body |
| `--muted` | `#495057` | Secondary |
| `--bg` / `--surface` | `#ffffff` | Light chrome over photo |
| `--hero-ink` | `#ffffff` | On dark food overlay |
| Logo wordmark | white + black outline | Keep existing logo asset |

## Target tokens (rebuild / Eng)
| Token | Hex |
| --- | --- |
| `--brand` | `#8b1e1e` |
| `--brand-2` / accent | `#d4a017` / `#c39212` (push CTAs toward true gold, not copper `#ad6b52`) |
| `--bg` | `#f7efe8` |
| `--surface` | `#fffaf4` |
| `--ink` | `#3b1c16` |
| `--muted` | `#6e4d42` |
| `--hero-ink` | `#fff4e0` |

## Layout intent
- Warm welcoming Chinese restaurant: red/gold hero, clear Call + Menu CTAs, hours/address card, takeout/delivery signals.
- Live pattern to borrow: full-bleed **food photography** under a dark wash + prominent **Order PickUp | Delivery** path (link only — no new forms/outreach).
- Keep dual-column hero (copy left / visit panel right) from scaffold; cream body with FAQ-style cards.
- Keep existing logo (`assets/logo.png`).

## Eng change list (concrete CSS/HTML)
1. `theme.css`: keep `--brand:#8b1e1e`; set `--brand-2`/`--accent` to `#d4a017` / `#c39212` so `.btn-primary` reads gold, not muted copper.
2. `.hero`: optional `background-image` of published dish photo + `linear-gradient` red/burgundy wash (`rgba(139,30,30,.72)` → transparent) — keep warm red, don’t go teal.
3. Header `.btn-dark` / `.header-cta`: stay deep red; add secondary ghost or text link “Order PickUp | Delivery” pointing to live order URL if already known in copy — **no new form**.
4. Restore **Gallery** nav item if assets exist on live; else omit (don’t invent photos).
5. `.eyebrow`: gold `#c39212` uppercase tracking; `.hero h1` stays `--font-display` Georgia on `--hero-ink`.
6. Body cards: cream `--bg`, red `h3` accents; ensure Menu page prices stay dark ink on cream (not gold text).

## Keep
- Existing logo wordmark; phone `(972) 487-8289`; address Walnut St; hours; real menu prices; no fake reviews/dishes.

## 508 notes
- White/cream text on `#8b1e1e` hero: OK; gold `#d4a017` on white fails for small text — use gold for large eyebrows/buttons with dark ink text, or dark ink for prices.
- Teal live buttons used black text on `#18A687` — if any teal remnant appears, prefer white-on-red or dark-on-gold with ≥4.5:1.
- Skip link already present; ensure focus ring visible on red header CTA (light outline).
- One `h1` in hero; About/FAQ as `h2`/`h3`; decorative food image needs meaningful `alt` or empty alt if purely decorative behind overlay.
